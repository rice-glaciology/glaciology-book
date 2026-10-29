"""Two-dimensional square ice: the textbook model of the ice rules and their defects.

Each oxygen sits on a square lattice and is hydrogen-bonded to its four
neighbours, the two-dimensional stand-in for the tetrahedral coordination of
ice Ih. Each bond carries one proton, near one end or the other, and the ice
rules require two protons near every oxygen (Fletcher 1970, ch. 7; Petrenko
& Whitworth 1999, ch. 4 and 6). The lattice is periodic (a torus); bonds that
cross the edge of the drawing are shown as half-length stubs on both sides.

A bond's state is which of its two ends "owns" a proton:

    one owner   a normal bond
    two owners  a D (doubly occupied) Bjerrum defect
    no owner    an L (empty) Bjerrum defect

and an oxygen with three or one owned protons is an H3O+ or OH- ionic defect.
A proton transfer along a bond moves an ionic defect; a molecular rotation,
which moves one of a molecule's protons onto another of its bonds, moves a
Bjerrum defect.
"""
import numpy as np
from matplotlib.collections import EllipseCollection, LineCollection

from common import FS_TICK, INK, smooth   # first: it puts the repository root on the path
import figstyle as fs  # noqa: E402

D_OH = 0.30                      # O-H distance as a fraction of the O-O spacing
R_O, R_H = 0.17, 0.07            # drawing radii of oxygens and protons
DIRS = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]], float)   # right, up, left, down

FILL_WATER = "white"
FILL_H3O = "#f4b6b6"             # light red: H3O+
FILL_OH = "#b9d4ef"              # light blue: OH-
TRAIL = "#fdd49e"                # light orange: bonds or molecules a defect has passed


class SquareIce:
    def __init__(self, nx, ny):
        self.nx, self.ny = nx, ny
        self.N = N = nx * ny
        s = np.arange(N)
        i, j = s % nx, s // nx
        self.pos = np.c_[i, j].astype(float)
        right, up = (i + 1) % nx + nx * j, i + nx * ((j + 1) % ny)
        left, down = (i - 1) % nx + nx * j, i + nx * ((j - 1) % ny)
        # bond 2s goes right from s, bond 2s+1 goes up; end 0 is s
        self.end = np.zeros((2 * N, 2), int)
        self.end[0::2, 0], self.end[0::2, 1] = s, right
        self.end[1::2, 0], self.end[1::2, 1] = s, up
        self.bdir = np.zeros((2 * N, 2))
        self.bdir[0::2] = (1, 0)
        self.bdir[1::2] = (0, 1)
        # the four bonds of each site in DIRS order, as (bond, which end the site is)
        self.sb = np.zeros((N, 4, 2), int)
        self.sb[:, 0, 0], self.sb[:, 1, 0] = 2 * s, 2 * s + 1
        self.sb[:, 2, 0], self.sb[:, 2, 1] = 2 * left, 1
        self.sb[:, 3, 0], self.sb[:, 3, 1] = 2 * down + 1, 1
        self.own = np.zeros((2 * N, 2), bool)
        self.own[:, 0] = True            # ordered start: every site owns its right and up bonds
        self.special = {}                # site -> (fill colour, label), e.g. a fluorine

    # -- bookkeeping ---------------------------------------------------------
    def copy(self):
        c = SquareIce.__new__(SquareIce)
        c.__dict__.update(self.__dict__)
        c.own = self.own.copy()
        c.special = dict(self.special)
        return c

    def site(self, i, j):
        return int((i % self.nx) + self.nx * (j % self.ny))

    def nprot(self):
        """Protons near each oxygen."""
        return self.own[self.sb[..., 0], self.sb[..., 1]].sum(1)

    def occ(self):
        """Protons on each bond."""
        return self.own.sum(1)

    def obeys_rules(self):
        return bool(np.all(self.occ() == 1) and np.all(self.nprot() == 2))

    def dipole(self):
        """Dipole of each molecule: the sum of unit vectors toward its protons."""
        return self.own[self.sb[..., 0], self.sb[..., 1]].astype(float) @ DIRS

    def end_of(self, b, s):
        return 0 if self.end[b, 0] == s else 1

    def bonds_of(self, s):
        """(bond, end, direction index) for the four bonds of site s."""
        return [(int(b), int(e), k) for k, (b, e) in enumerate(self.sb[s])]

    def owned(self, s):
        return [(b, e, k) for b, e, k in self.bonds_of(s) if self.own[b, e]]

    def bond_mid(self, b):
        return self.pos[self.end[b, 0]] + 0.5 * self.bdir[b]

    # -- moves -----------------------------------------------------------------
    def transfer(self, b):
        """Move the proton on bond b to the other end (an ionic hop)."""
        assert self.own[b].sum() == 1
        self.own[b] = ~self.own[b]

    def rotate(self, s, b_from, b_to):
        """Molecule s moves one of its protons from bond b_from to bond b_to."""
        ef, et = self.end_of(b_from, s), self.end_of(b_to, s)
        assert self.own[b_from, ef] and not self.own[b_to, et]
        self.own[b_from, ef] = False
        self.own[b_to, et] = True

    def flip(self, bonds):
        for b in bonds:
            self.transfer(b)

    def loop(self, rng, start, forbid=(), max_steps=400):
        """A closed loop along which every proton can be moved to the other end of
        its bond without breaking the ice rules: follow owned bonds from site to site
        until the path closes. Returns (bonds, sites) of the cycle, or None."""
        path, bonds, seen, s = [start], [], {start: 0}, start
        for _ in range(max_steps):
            out = [(b, e) for b, e, _ in self.owned(s) if b not in forbid]
            if not out:
                return None
            b, e = out[rng.integers(len(out))]
            t = int(self.end[b, 1 - e])
            bonds.append(b)
            if t in seen:
                k = seen[t]
                return bonds[k:], path[k:]
            seen[t] = len(path)
            path.append(t)
            s = t
        return None

    def randomize(self, rng, n=400, forbid=()):
        for _ in range(n):
            r = self.loop(rng, int(rng.integers(self.N)), forbid)
            if r:
                self.flip(r[0])
        return self


# -- geometry for drawing ----------------------------------------------------------
def proton_xy(ice, b, e, f=0.0):
    """Proton on bond b near end e, moved a fraction f of the way to the other end."""
    d = ice.bdir[b] * (1.0 if e == 0 else -1.0)
    return ice.pos[ice.end[b, e]] + (D_OH + f * (1 - 2 * D_OH)) * d


def rotation_xy(ice, s, k_from, k_to, f, other_k=None):
    """A proton swinging around oxygen s from bond direction k_from to k_to."""
    a1 = np.arctan2(*DIRS[k_from][::-1])
    a2 = np.arctan2(*DIRS[k_to][::-1])
    da = (a2 - a1 + np.pi) % (2 * np.pi) - np.pi
    if abs(abs(da) - np.pi) < 1e-6 and other_k is not None:
        # half a turn: swing through the side away from the molecule's other proton
        ao = np.arctan2(*DIRS[other_k][::-1])
        mid = a1 + np.pi / 2
        da = np.pi if np.cos(mid - ao) < 0 else -np.pi
    a = a1 + f * da
    return ice.pos[s] + D_OH * np.array([np.cos(a), np.sin(a)])


def _anchor(ice, b, e, f, p):
    """The oxygen a proton in mid-transfer is bonded to: the one it left until halfway,
    then the one it is joining (unwrapped, so the line stays on the drawn bond)."""
    d = ice.bdir[b] * (1.0 if e == 0 else -1.0)
    s = D_OH + f * (1 - 2 * D_OH)
    return p - s * d if f < 0.5 else p + (1 - s) * d


def _bond_segments(ice, bonds):
    segs = []
    for b in bonds:
        p0 = ice.pos[ice.end[b, 0]]
        p1 = ice.pos[ice.end[b, 1]]
        if np.allclose(p0 + ice.bdir[b], p1):
            segs.append([p0, p1])
        else:                                      # wraps around the torus: two stubs
            segs.append([p0, p0 + 0.5 * ice.bdir[b]])
            segs.append([p1 - 0.5 * ice.bdir[b], p1])
    return segs


def draw_ice(ax, ice, moving=None, trail_bonds=(), trail_sites=(), ring_sites=(),
             loop_bonds=(), labels=True, fills=None):
    """Draw a SquareIce state, optionally with protons in motion.

    ``ice`` is the state before the move, with every proton in its starting place.
    moving:
        ("transfer", b, e, f)            the proton on bond b near end e, moved a fraction
                                         f of the way across (an ionic hop);
        ("rotate", s, b_from, b_to, f)   molecule s swinging a proton from one of its
                                         bonds to another (a Bjerrum step);
        ("flip", [(b, e), ...], f)       every proton on a loop crossing its bond together.
    A moving proton counts with whichever oxygen (and, for a rotation, bond) it is
    nearer, so defect colours and labels change halfway through the move.
    fills: optional per-site face colours, overriding the defect colours.
    """
    allb = range(2 * ice.N)
    occ = ice.occ().copy()
    npr = ice.nprot().copy()
    skip, movers, rot = set(), [], None
    if moving is not None:
        kind, f = moving[0], moving[-1]
        if kind == "transfer":
            _, b, e, f = moving
            movers = [(b, e)]
        elif kind == "flip":
            movers = list(moving[1])
        else:
            _, s, bf, bt, f = moving
            ef = ice.end_of(bf, s)
            skip.add((bf, ef))
            rot = (s, bf, bt, f)
            if f >= 0.5:
                occ[bf] -= 1
                occ[bt] += 1
        for b, e in movers:
            skip.add((b, e))
            if f >= 0.5:
                npr[ice.end[b, e]] -= 1
                npr[ice.end[b, 1 - e]] += 1
    # underlays: a loop about to flip, a defect's trail, the Bjerrum defects
    if len(loop_bonds):
        ax.add_collection(LineCollection(_bond_segments(ice, loop_bonds), colors=fs.ORANGE,
                                         linewidths=9, alpha=0.55, zorder=0.5, capstyle="round"))
    if len(trail_bonds):
        ax.add_collection(LineCollection(_bond_segments(ice, trail_bonds), colors=TRAIL,
                                         linewidths=9, zorder=0.6, capstyle="round"))
    dbonds = [b for b in allb if occ[b] == 2]
    lbonds = [b for b in allb if occ[b] == 0]
    if dbonds:
        ax.add_collection(LineCollection(_bond_segments(ice, dbonds), colors=fs.GREEN,
                                         linewidths=8, alpha=0.6, zorder=0.7))
    if lbonds:
        ax.add_collection(LineCollection(_bond_segments(ice, lbonds), colors=fs.PURPLE,
                                         linewidths=8, alpha=0.6, zorder=0.7))
    # hydrogen bonds
    ax.add_collection(LineCollection(_bond_segments(ice, allb), colors="0.6", linewidths=1.0, zorder=1))
    # protons and their covalent O-H bonds
    hp, cov = [], []
    for b in allb:
        for e in (0, 1):
            if ice.own[b, e] and (b, e) not in skip:
                p = proton_xy(ice, b, e)
                hp.append(p)
                cov.append([p, _anchor(ice, b, e, 0.0, p)])
    if moving is not None:
        for b, e in movers:
            p = proton_xy(ice, b, e, f)
            hp.append(p)
            cov.append([p, _anchor(ice, b, e, f, p)])
        if rot is not None:
            s, bf, bt, f = rot
            kf = [k for b, e, k in ice.bonds_of(s) if b == bf][0]
            kt = [k for b, e, k in ice.bonds_of(s) if b == bt][0]
            others = [k for b, e, k in ice.owned(s) if b != bf]
            p = rotation_xy(ice, s, kf, kt, f, others[0] if others else None)
            hp.append(p)
            cov.append([p, ice.pos[s]])
    ax.add_collection(LineCollection(cov, colors=INK, linewidths=2.4, zorder=2))
    if hp:
        hp = np.array(hp)
        n = len(hp)
        ax.add_collection(EllipseCollection(np.full(n, 2 * R_H), np.full(n, 2 * R_H), np.zeros(n),
                                            units="xy", offsets=hp, offset_transform=ax.transData,
                                            facecolors=INK, edgecolors=INK, zorder=3))
    # oxygens
    face = []
    for s in range(ice.N):
        if fills is not None:
            face.append(fills[s])
        elif s in ice.special:
            face.append(ice.special[s][0])
        elif npr[s] >= 3:
            face.append(FILL_H3O)
        elif npr[s] <= 1:
            face.append(FILL_OH)
        else:
            face.append(FILL_WATER)
    edge = [INK] * ice.N
    lw = np.full(ice.N, 1.2)
    for s in trail_sites:
        edge[s], lw[s] = fs.ORANGE, 3.0
    for s in ring_sites:
        edge[s], lw[s] = fs.RED, 3.2
    ax.add_collection(EllipseCollection(np.full(ice.N, 2 * R_O), np.full(ice.N, 2 * R_O),
                                        np.zeros(ice.N), units="xy", offsets=ice.pos,
                                        offset_transform=ax.transData, facecolors=face,
                                        edgecolors=edge, linewidths=lw, zorder=4))
    for s, (_, lab) in ice.special.items():
        ax.text(*ice.pos[s], lab, ha="center", va="center", fontsize=FS_TICK - (1 if len(lab) == 1 else 3),
                zorder=5)
    if not labels:
        return
    for s in range(ice.N):
        if s in ice.special:
            continue
        if npr[s] >= 3:
            ax.text(ice.pos[s][0], ice.pos[s][1] + 0.36, "H$_3$O$^+$", ha="center", va="bottom",
                    fontsize=FS_TICK - 1, color=fs.RED, zorder=6)
        elif npr[s] <= 1:
            ax.text(ice.pos[s][0], ice.pos[s][1] + 0.36, "OH$^-$", ha="center", va="bottom",
                    fontsize=FS_TICK - 1, color=fs.BLUE, zorder=6)
    for b, lab, col in [(b, "D", fs.GREEN) for b in dbonds] + [(b, "L", fs.PURPLE) for b in lbonds]:
        m = ice.bond_mid(b)
        off = np.array([0.0, 0.2]) if ice.bdir[b][0] else np.array([0.2, 0.0])
        ax.text(*(m + off), lab, ha="center", va="center", fontsize=FS_TICK, color=col,
                weight="bold", zorder=6)


# -- scripted sequences -----------------------------------------------------------------
class Script:
    """A sequence of events on a SquareIce state, played back over normalized time.

    Events: ("transfer", b), ("rotate", s, b_from, b_to), ("flip", bonds) (a loop of
    simultaneous transfers), ("pause",) and ("set", fn) (an instant change). Each
    record keeps the state before it, the defect trail so far and an optional note.
    """

    def __init__(self, ice):
        self.ice = ice.copy()
        self.events = []
        self.trail_b, self.trail_s = set(), set()

    def add(self, ev, dur=1.0, note=None, trail=True):
        rec = dict(ev=ev, dur=dur, note=note or {}, before=self.ice.copy(),
                   trail_b=set(self.trail_b), trail_s=set(self.trail_s))
        kind = ev[0]
        if kind == "transfer":
            self.ice.transfer(ev[1])
            if trail:
                self.trail_b.add(ev[1])
        elif kind == "rotate":
            self.ice.rotate(*ev[1:])
            if trail:
                self.trail_s.add(ev[1])
        elif kind == "flip":
            self.ice.flip(ev[1])
        elif kind == "set":
            ev[1](self.ice)
        self.events.append(rec)
        return rec

    def total(self):
        return sum(r["dur"] for r in self.events)

    def after(self, rec):
        i = self.events.index(rec)
        return self.events[i + 1]["before"] if i + 1 < len(self.events) else self.ice

    def at(self, u):
        """What to draw at progress u in [0, 1]: (state, moving, record, f)."""
        x = float(np.clip(u, 0, 1)) * self.total()
        for r in self.events:
            if x < r["dur"] or r is self.events[-1]:
                f = smooth(min(x / r["dur"], 1.0)) if r["dur"] > 0 else 1.0
                return self._frame(r, f)
            x -= r["dur"]

    def _frame(self, r, f):
        ev, ice = r["ev"], r["before"]
        if f >= 1.0:
            return self.after(r), None, r, 1.0
        kind = ev[0]
        if kind == "transfer":
            b = ev[1]
            return ice, ("transfer", b, 0 if ice.own[b, 0] else 1, f), r, f
        if kind == "rotate":
            return ice, ("rotate",) + tuple(ev[1:]) + (f,), r, f
        if kind == "flip":
            return ice, ("flip", [(b, 0 if ice.own[b, 0] else 1) for b in ev[1]], f), r, f
        return ice, None, r, f
