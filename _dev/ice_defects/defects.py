"""Animations for the proton-disorder and point-defect sections.

Every animation runs on a model rather than a drawing: the square-ice lattice
of ``squareice.py`` for the ice rules, ionic and Bjerrum defects, doping,
conduction and dielectric relaxation; a honeycomb lattice (the basal plane of
ice Ih seen down the c-axis) for vacancies and interstitials; and Langevin
dynamics in a periodic potential for thermally activated jumps.
"""
import numpy as np
from matplotlib.collections import EllipseCollection, LineCollection
from matplotlib.patches import Circle, Rectangle

from common import FS, FS_TICK, INK, Video, arrow, mechanism, ramp, readout, smooth
import figstyle as fs  # noqa: E402
from squareice import D_OH, DIRS, R_H, R_O, Script, SquareIce, draw_ice

LIGHT_RED, LIGHT_BLUE = "#f4b6b6", "#b9d4ef"


# -- helpers ------------------------------------------------------------------------
def wraps(ice, b):
    return not np.allclose(ice.pos[ice.end[b, 0]] + ice.bdir[b], ice.pos[ice.end[b, 1]])


def inside(ice, p, m=0.8):
    return m <= p[0] <= ice.nx - 1 - m and m <= p[1] <= ice.ny - 1 - m


def field_arrow(ax, x, y, L=2.2, on=1.0, label="$E$"):
    if on <= 0:
        return
    arrow(ax, x, y, L * on, 0, color=INK, lw=2.4)
    ax.text(x + 0.5 * L * on, y + 0.25, label, ha="center", va="bottom", fontsize=FS)


def frame_of(script, t, a=0.0, b=1.0):
    return script.at(ramp(t, a, b))


def draw_script(ax, script, t, a=0.0, b=1.0, **kw):
    ice, moving, rec, f = frame_of(script, t, a, b)
    if f < 1 and rec["ev"][0] == "flip":
        loop = rec["ev"][1]
    else:
        loop = rec["note"].get("loop", ()) if f < 1 else ()
    kw.setdefault("trail_bonds", rec["trail_b"])
    kw.setdefault("trail_sites", rec["trail_s"])
    draw_ice(ax, ice, moving, loop_bonds=loop, **kw)
    return ice, moving, rec, f


def count_done(script, t, a, b, kind_note):
    """How many events carrying note[kind_note] have finished by time t."""
    u = ramp(t, a, b) * script.total()
    n, x = 0, 0.0
    for r in script.events:
        x += r["dur"]
        if x <= u + 1e-9 and r["note"].get(kind_note):
            n += 1
    return n


def best_of(build, seeds=range(24)):
    """Run a randomized script builder ``build(rng) -> (script, score)`` for several
    seeds and keep the highest-scoring script: the walks stay random but readable."""
    return max((build(np.random.default_rng(s)) for s in seeds), key=lambda r: r[1])[0]


# -- ionic and Bjerrum walks -----------------------------------------------------------------
def h3o_hop(ice, p, rng, xdir=1.0, ydir=0.0, avoid=()):
    npr = ice.nprot()
    best = None
    for b, e, k in ice.owned(p):
        t = int(ice.end[b, 1 - e])
        if wraps(ice, b) or npr[t] != 2 or t in avoid or not inside(ice, ice.pos[t]):
            continue
        d = ice.pos[t] - ice.pos[p]
        score = xdir * d[0] + ydir * d[1] + 0.8 * rng.random()
        if best is None or score > best[0]:
            best = (score, b, t)
    return None if best is None else best[1:]


def oh_hop(ice, q, rng, xdir=-1.0, ydir=0.0, avoid=()):
    npr = ice.nprot()
    best = None
    for b, e, k in ice.bonds_of(q):
        if ice.own[b, e] or not ice.own[b, 1 - e]:
            continue
        t = int(ice.end[b, 1 - e])
        if wraps(ice, b) or npr[t] != 2 or t in avoid or not inside(ice, ice.pos[t]):
            continue
        d = ice.pos[t] - ice.pos[q]
        score = xdir * d[0] + ydir * d[1] + 0.8 * rng.random()
        if best is None or score > best[0]:
            best = (score, b, t)
    return None if best is None else best[1:]


def d_move(ice, bd, rng, xdir=1.0, ydir=0.0, frozen=(), avoid=()):
    """A rotation that hands the D-defect on bond bd to a neighbouring bond
    (not one in ``avoid``), preferring the direction (xdir, ydir)."""
    occ = ice.occ()
    best = None
    for w in ice.end[bd]:
        w = int(w)
        if w in frozen:
            continue
        for c, e, k in ice.bonds_of(w):
            if c == bd or c in avoid or ice.own[c, e] or occ[c] != 1 or wraps(ice, c):
                continue
            m = ice.bond_mid(c)
            if not inside(ice, m, 0.4):
                continue
            d = m - ice.bond_mid(bd)
            score = xdir * d[0] + ydir * d[1] + 0.8 * rng.random()
            if best is None or score > best[0]:
                best = (score, w, c)
    return None if best is None else best[1:]          # rotate(w, bd, c); D moves to c


def l_move(ice, bl, rng, xdir=-1.0, ydir=0.0, frozen=(), avoid=()):
    """A rotation that hands the L-defect on bond bl to a neighbouring bond
    (not one in ``avoid``), preferring the direction (xdir, ydir)."""
    occ = ice.occ()
    best = None
    for w in ice.end[bl]:
        w = int(w)
        if w in frozen:
            continue
        for c, e, k in ice.owned(w):
            if c == bl or c in avoid or occ[c] != 1 or wraps(ice, c):
                continue
            m = ice.bond_mid(c)
            if not inside(ice, m, 0.4):
                continue
            d = m - ice.bond_mid(bl)
            score = xdir * d[0] + ydir * d[1] + 0.8 * rng.random()
            if best is None or score > best[0]:
                best = (score, w, c)
    return None if best is None else best[1:]          # rotate(w, c, bl); L moves to c


def mini_molecule(ax, c, ks, scale=0.55, ring=False):
    """One oxygen with its four bonds and protons on the bond directions ``ks``."""
    Lb = 2 * scale                                   # full O-O bond; the stub drawn is half of it
    segs = [[c, c + scale * DIRS[k]] for k in range(4)]
    ax.add_collection(LineCollection(segs, colors="0.6", linewidths=1.0, zorder=1))
    for k in ks:
        p = c + D_OH * Lb * DIRS[k]
        ax.plot(*np.c_[c, p], color=INK, lw=2.4, zorder=2)
        ax.add_patch(Circle(p, R_H * Lb, facecolor=INK, edgecolor=INK, zorder=3))
    ax.add_patch(Circle(c, R_O * Lb, facecolor="white", edgecolor=fs.RED if ring else INK,
                        lw=3.2 if ring else 1.2, zorder=4))


ORIENTATIONS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]   # pairs of bond directions


# -- 1. proton disorder and the ice rules --------------------------------------------------
@mechanism("proton-disorder", 1)
def proton_disorder():
    nx, ny = 10, 6
    rng = np.random.default_rng(12)
    ice = SquareIce(nx, ny).randomize(rng, 600)
    h = ice.site(4, 3)
    sc = Script(ice)
    sc.add(("pause",), 4.2)
    tries = 0
    while sum(1 for r in sc.events if r["ev"][0] == "flip") < 6 and tries < 5000:
        tries += 1
        nflip = sum(1 for r in sc.events if r["ev"][0] == "flip")
        r = sc.ice.loop(rng, h if nflip % 2 == 0 else int(rng.integers(sc.ice.N)))
        if not r:
            continue
        bonds, sites = r
        if not (4 <= len(bonds) <= 10) or any(wraps(sc.ice, b) for b in bonds):
            continue
        if nflip % 2 == 0 and h not in sites:
            continue
        sc.add(("pause",), 0.8, note={"loop": bonds})
        sc.add(("flip", bonds), 1.3, note={"flip": True})
    sc.add(("pause",), 3.6)
    N = nx * ny

    v = Video(
        slug="proton-disorder",
        title="Proton disorder and the ice rules",
        captions=[(0.0, "The oxygens sit on a fixed lattice; each bond holds one proton, near one end or the other"),
                  (0.10, "The ice rules: two protons near every oxygen, so every molecule stays H$_2$O"),
                  (0.205, "Reversing every proton around a closed loop (orange) gives another arrangement that obeys the rules"),
                  (0.56, "So the protons can take an enormous number of arrangements: the crystal is proton-disordered"),
                  (0.825, "(B) Pauling's count gives a residual entropy of $R\\,\\ln(3/2)$, as measured")],
        panels=[dict(rect=[0.02, 0.09, 0.58, 0.79], kind="field", xlim=(-0.9, nx - 0.1),
                     ylim=(-2.1, ny - 0.1), letter="A", letter_at=(0.03, 0.97)),
                dict(rect=[0.63, 0.09, 0.35, 0.74], kind="field", xlim=(0, 4.4), ylim=(0, 5.4),
                     letter="B", letter_at=(0.05, 0.97), title="Pauling's count")],
        seconds=22)

    def draw(axs, t):
        ax, bx = axs
        ice_now, moving, rec, f = draw_script(ax, sc, t, ring_sites=[h], trail_bonds=(), trail_sites=())
        nflip = count_done(sc, t, 0, 1, "flip")
        readout(ax, 2.2, -1.45, f"loops reversed: {nflip}")
        readout(ax, 6.7, -1.45, f"$N={N}$: $(3/2)^{{{N}}}\\approx4\\times10^{{10}}$ arrangements")
        # (B) the six orientations allowed around one oxygen
        state = rec["before"] if f < 0.5 else (sc.ice if rec is sc.events[-1] else
                                                sc.events[sc.events.index(rec) + 1]["before"])
        ks = tuple(sorted(k for b, e, k in state.owned(h)))
        for n, o in enumerate(ORIENTATIONS):
            c = np.array([0.8 + 1.4 * (n % 3), 4.45 - 1.45 * (n // 3)])
            mini_molecule(bx, c, o, ring=(o == ks))
        bx.text(2.2, 2.05, "6 of the 16 proton arrangements around\nan oxygen obey the ice rules",
                ha="center", va="center", fontsize=FS_TICK)
        bx.text(2.2, 1.15, r"$W = 2^{2N}\,(6/16)^N = (3/2)^N$", ha="center", va="center", fontsize=FS)
        bx.text(2.2, 0.45, r"$S = R\ln(3/2) \approx 3.4$ J mol$^{-1}$ K$^{-1}$", ha="center", va="center",
                fontsize=FS)

    return v, draw


# -- 2. ionic defects ----------------------------------------------------------------------
@mechanism("ionic-defects", 2)
def ionic_defects():
    nx, ny = 16, 6
    rng = np.random.default_rng(4)
    ice = SquareIce(nx, ny).randomize(rng, 800)
    # start where the bond to the right of s0 carries s0's proton
    s0 = next(s for s in (ice.site(i, j) for i in (6, 5, 7, 4) for j in (3, 2)) if ice.own[2 * s, 0])
    def build(rng):
        sc = Script(ice)
        sc.add(("pause",), 2.2)
        sc.add(("transfer", 2 * s0), 1.3, note={"pair": True})
        p, q = int(ice.end[2 * s0, 1]), s0                # H3O+ at p, OH- at q
        seen = {p, q}                                     # neither defect revisits a molecule
        sc.add(("pause",), 0.8)
        n = 0
        for step in range(13):
            if step % 3 != 2:
                mv = h3o_hop(sc.ice, p, rng, xdir=1.0, avoid=seen)
                if mv:
                    b, p = mv
                    sc.add(("transfer", b), 0.7, note={"plus": True})
            else:
                mv = oh_hop(sc.ice, q, rng, xdir=-1.0, avoid=seen)
                if mv:
                    b, q = mv
                    sc.add(("transfer", b), 1.2, note={"minus": True})
            if mv:
                seen.add(mv[1])
                n += 1
        sc.add(("pause",), 3.2)
        return sc, ice.pos[p][0] - ice.pos[q][0] + n

    sc = best_of(build)

    v = Video(
        slug="ionic-defects",
        title="Ionic defects: H$_3$O$^+$ and OH$^-$",
        captions=[(0.0, "Square ice obeying the ice rules, in an electric field $E$"),
                  (0.11, "A proton jumps along its bond: an H$_3$O$^+$ and an OH$^-$ form"),
                  (0.22, "Further jumps separate them; the positive defect runs with the field by passing on a proton"),
                  (0.48, "The OH$^-$ moves more slowly: a proton vacancy handed from molecule to molecule"),
                  (0.74, "Every bond crossed keeps its proton on the far side (orange): the path is left polarized")],
        xlim=(-0.9, nx - 0.1), ylim=(-1.9, ny + 0.7), seconds=18)

    def draw(ax, t):
        draw_script(ax, sc, t)
        field_arrow(ax, nx / 2 - 1.1, ny - 0.15)
        readout(ax, 3.0, -1.3, f"OH$^-$ jumps: {count_done(sc, t, 0, 1, 'minus')}")
        readout(ax, nx - 4.0, -1.3, f"H$_3$O$^+$ jumps: {count_done(sc, t, 0, 1, 'plus')}")

    return v, draw


# -- 3. Bjerrum defects ------------------------------------------------------------------------
@mechanism("bjerrum-defects", 3)
def bjerrum_defects():
    nx, ny = 16, 6

    def build(rng):
        ice = SquareIce(nx, ny).randomize(rng, 800)
        m = ice.site(7, 3)
        own = ice.owned(m)
        free = [(b, e, k) for b, e, k in ice.bonds_of(m) if not ice.own[b, e]]
        # create the pair so that D starts to the right and L to the left where possible
        pick = max(((o, f) for o in own for f in free),
                   key=lambda of: ice.bond_mid(of[1][0])[0] - ice.bond_mid(of[0][0])[0])
        bl, bd = pick[0][0], pick[1][0]
        sc = Script(ice)
        sc.add(("pause",), 2.2)
        sc.add(("rotate", m, bl, bd), 1.6, note={"pair": True})
        sc.add(("pause",), 0.8)
        seen = {bl, bd}                                   # neither defect revisits a bond
        n = 0
        for step in range(12):
            if step % 2 == 0:
                mv = d_move(sc.ice, bd, rng, xdir=1.0, avoid=seen)
                if mv:
                    w, c = mv
                    sc.add(("rotate", w, bd, c), 1.0, note={"D": True})
                    bd = c
            else:
                mv = l_move(sc.ice, bl, rng, xdir=-1.0, avoid=seen)
                if mv:
                    w, c = mv
                    sc.add(("rotate", w, c, bl), 1.0, note={"L": True})
                    bl = c
            if mv:
                seen.add(mv[1])
                n += 1
        sc.add(("pause",), 3.2)
        sep = ice.bond_mid(bd) - ice.bond_mid(bl)
        return sc, sep[0] - 0.5 * abs(sep[1]) + n

    sc = best_of(build, range(60))

    v = Video(
        slug="bjerrum-defects",
        title="Orientational (Bjerrum) defects: D and L",
        captions=[(0.0, "Square ice obeying the ice rules"),
                  (0.11, "One molecule rotates, moving a proton onto a neighboring bond"),
                  (0.19, "That bond now holds two protons (a D-defect) and the bond it left holds none (an L-defect)"),
                  (0.30, "Each rotation of a neighboring molecule hands a defect on, so the pair drifts apart"),
                  (0.64, "Every molecule a defect passes is left reoriented (orange): the only way molecules in ice can turn")],
        xlim=(-0.9, nx - 0.1), ylim=(-1.9, ny + 0.7), seconds=18)

    def draw(ax, t):
        draw_script(ax, sc, t)
        readout(ax, 3.0, -1.3, f"L-defect steps: {count_done(sc, t, 0, 1, 'L')}")
        readout(ax, nx - 4.0, -1.3, f"D-defect steps: {count_done(sc, t, 0, 1, 'D')}")

    return v, draw


# -- 4. HF as a dopant ---------------------------------------------------------------------------
@mechanism("hf-doping", 4)
def hf_doping():
    nx, ny = 16, 6
    rng = np.random.default_rng(21)
    ice = SquareIce(nx, ny).randomize(rng, 800)
    FILL_F = "#fdd49e"

    def owns(s, k):
        return any(kk == k for b, e, kk in ice.owned(s))

    # f1 loses the proton on its left or lower bond, so its L-defect can leave that way;
    # f2 keeps the proton on its right bond, so the H3O+ it releases heads into open lattice
    f1 = next(s for s in (ice.site(i, j) for i in (5, 4, 6) for j in (3, 2)) if owns(s, 2) or owns(s, 3))
    f2 = next(s for s in (ice.site(i, j) for i in (10, 11, 9) for j in (3, 2)) if owns(s, 0))
    for fsite, gone in ((f1, 2 if owns(f1, 2) else 3), (f2, None)):
        own = ice.owned(fsite)
        b, e, k = next(o for o in own if (o[2] == gone if gone is not None else o[2] != 0))
        ice.own[b, e] = False                     # one proton fewer: that bond is left empty
        ice.special[fsite] = (FILL_F, "F")
    def build(rng):
        sc = Script(ice)
        sc.add(("pause",), 4.0)
        # the L-defect bound at f1 breaks away by rotations of its neighbours (never of F)
        bl = next(b for b, e, k in ice.bonds_of(f1) if ice.occ()[b] == 0)
        seen, n = {bl}, 0
        for step in range(6):
            mv = l_move(sc.ice, bl, rng, xdir=-0.8, ydir=-0.5, frozen=(f1, f2), avoid=seen)
            if mv:
                w, c = mv
                sc.add(("rotate", w, c, bl), 1.0, note={"L": True})
                bl = c
                seen.add(c)
                n += 1
        sc.add(("pause",), 1.0)
        # at f2 the fluorine's own proton jumps to a neighbour: F- stays, an H3O+ is released
        bF, eF, kF = sc.ice.owned(f2)[0]
        p = int(sc.ice.end[bF, 1 - eF])
        sc.add(("transfer", bF), 1.2, note={"plus": True})
        sc.add(("set", lambda s: s.special.__setitem__(f2, (FILL_F, "F$^-$"))), 0.0)
        seen = {f2, p}
        for step in range(5):
            mv = h3o_hop(sc.ice, p, rng, xdir=1.0, ydir=0.3, avoid=seen)
            if mv:
                b, p = mv
                seen.add(p)
                sc.add(("transfer", b), 0.7, note={"plus": True})
                n += 1
        sc.add(("pause",), 3.2)
        away = (np.hypot(*(ice.bond_mid(bl) - ice.pos[f1])) + np.hypot(*(ice.pos[p] - ice.pos[f2])))
        return sc, away + 2 * n

    sc = best_of(build)

    v = Video(
        slug="hf-doping",
        title="Impurities as dopants: HF in ice",
        captions=[(0.0, "Two HF molecules (F) replace water molecules; each has one proton where water has two"),
                  (0.12, "So each leaves one of its bonds empty: an L-defect bound to the fluorine"),
                  (0.21, "The L-defect breaks away and wanders off by rotations of the neighboring molecules"),
                  (0.575, "Or the fluorine's proton jumps to a neighbor, releasing an H$_3$O$^+$ that moves off"),
                  (0.83, "HF donates L-defects and H$_3$O$^+$; NH$_3$ does the reverse, giving D-defects and OH$^-$")],
        xlim=(-0.9, nx - 0.1), ylim=(-1.9, ny + 0.7), seconds=18)

    def draw(ax, t):
        draw_script(ax, sc, t)
        readout(ax, 3.0, -1.3, f"free L-defect steps: {count_done(sc, t, 0, 1, 'L')}")
        readout(ax, nx - 4.0, -1.3, f"H$_3$O$^+$ jumps: {count_done(sc, t, 0, 1, 'plus')}")

    return v, draw


# -- 5. vacancies, interstitials and self-diffusion -----------------------------------------------
def honeycomb(nx, ny):
    """Oxygen sites of the basal plane seen down the c-axis (puckering ignored): a
    honeycomb with bond length 1, periodic in x. Returns positions, neighbour lists,
    and the centres of the hexagonal rings (the open channels along c)."""
    a = np.sqrt(3)
    pts, centres = [], []
    for j in range(ny):
        for i in range(nx):
            xa = (a * i + 0.5 * a * j) % (a * nx)
            pts.append((xa, 1.5 * j))
            pts.append((xa, 1.5 * j + 1.0))
            centres.append(((xa + 0.5 * a) % (a * nx), 1.5 * j + 0.5))   # ring centre: A + (sqrt3/2, 1/2)
    P = np.array(pts)
    Wx = a * nx
    d = P[:, None, :] - P[None, :, :]
    d[..., 0] = (d[..., 0] + Wx / 2) % Wx - Wx / 2
    r = np.hypot(d[..., 0], d[..., 1])
    nbr = [list(np.where((r[k] > 0.5) & (r[k] < 1.2))[0]) for k in range(len(P))]
    C = np.array(centres)
    dc = C[:, None, :] - C[None, :, :]
    dc[..., 0] = (dc[..., 0] + Wx / 2) % Wx - Wx / 2
    rc = np.hypot(dc[..., 0], dc[..., 1])
    cnbr = [list(np.where((rc[k] > 0.5) & (rc[k] < 1.9))[0]) for k in range(len(C))]
    return P, nbr, C, cnbr, Wx


@mechanism("self-diffusion", 5)
def self_diffusion():
    nx, ny = 11, 5
    P, nbr, C, cnbr, Wx = honeycomb(nx, ny)
    rng = np.random.default_rng(5)
    ymax = P[:, 1].max()
    # the tracer (a labelled molecule) near the middle; the vacancy beside it
    tracer = int(np.argmin(np.hypot(P[:, 0] - Wx / 2, P[:, 1] - ymax / 2)))
    vac = int(nbr[tracer][0])
    # a channel is drawn (and open to the interstitial) only if its whole ring of six is drawn
    whole = np.array([np.sum(np.abs(np.hypot(*(P - c).T) - 1.0) < 0.05) == 6 for c in C])
    inter = int(np.argmin(np.hypot(C[:, 0] - Wx * 0.2, C[:, 1] - ymax * 0.55) + 99 * ~whole))
    n_hops = 80
    hops = []                         # (moving molecule's old site, new site, tracer moved?)
    vac_path, tr_path, int_path = [vac], [tracer], [inter]
    occupant = np.arange(len(P))      # which molecule is at each site; -1 = vacancy
    occupant[vac] = -1
    for k in range(n_hops):
        # the vacancy steps to a random neighbour; avoid running off the top and bottom rows
        cand = [w for w in nbr[vac] if 0.4 < P[w, 1] < ymax - 0.4 and abs(P[w, 0] - P[vac, 0]) < 1.5]
        w = int(cand[rng.integers(len(cand))])
        moved_tracer = (w == tracer)
        hops.append((w, vac, moved_tracer))
        occupant[vac], occupant[w] = occupant[w], -1
        if moved_tracer:
            tracer = vac
        vac = w
        vac_path.append(vac)
        tr_path.append(tracer)
        if k % 4 == 3:                # the interstitial hops between channels less often here
            cc = [c for c in cnbr[inter] if whole[c] and abs(C[c, 0] - C[inter, 0]) < 2.0]
            inter = int(cc[rng.integers(len(cc))]) if cc else inter
        int_path.append(inter)

    v = Video(
        slug="self-diffusion",
        title="Self-diffusion: vacancies and interstitials",
        captions=[(0.0, "A basal plane seen down the c-axis: oxygens (protons omitted) and the open channels between them"),
                  (0.06, "A vacancy (dashed) moves whenever a neighboring molecule jumps into it"),
                  (0.30, "A labeled molecule (green) moves only when the vacancy happens to be beside it"),
                  (0.55, "An interstitial molecule (blue) travels through the open channels"),
                  (0.80, "Whole molecules diffuse this way, which is why every isotope tracer diffuses at the same rate")],
        xlim=(-1.0, Wx + 0.2), ylim=(-1.6, ymax + 0.8), seconds=18)

    def draw(ax, t):
        u = ramp(t, 0.05, 0.95) * n_hops
        k = min(int(u), n_hops - 1)
        f = smooth(u - k, 0.1, 0.9) if u < n_hops else 1.0
        if u >= n_hops:
            k, f = n_hops - 1, 1.0
        # bonds (skip the ones that wrap around)
        segs = [[P[a], P[b]] for a in range(len(P)) for b in nbr[a] if a < b and abs(P[a, 0] - P[b, 0]) < 1.5]
        ax.add_collection(LineCollection(segs, colors="0.7", linewidths=1.0, zorder=1))
        # channels
        for c in C[whole]:
            ax.add_patch(Circle(c, 0.12, facecolor="0.92", edgecolor="none", zorder=0.5))
        # molecule positions at hop k
        w, vsite, moved_tracer = hops[k]
        tr_site = tr_path[k]
        pos = P.copy()
        mover = w
        pos[mover] = (1 - f) * P[w] + f * P[vsite]
        empty = vsite if f < 1 else w
        show = np.ones(len(P), bool)
        if f < 1:
            show[vsite] = False                      # the vacancy, until the molecule arrives
        else:
            show[w] = False
        face = np.array(["white"] * len(P), dtype=object)
        tsite = tr_site
        if moved_tracer and mover == tr_site:
            face[mover] = fs.GREEN
        else:
            face[tsite] = fs.GREEN
        idx = np.where(show)[0]
        n = len(idx)
        ax.add_collection(EllipseCollection(np.full(n, 0.5), np.full(n, 0.5), np.zeros(n), units="xy",
                                            offsets=pos[idx], offset_transform=ax.transData,
                                            facecolors=list(face[idx]), edgecolors=INK, linewidths=1.2,
                                            zorder=3))
        ax.add_patch(Circle(P[empty], 0.25, facecolor="none", edgecolor=INK, lw=1.6, ls="--", zorder=3))
        # tracer path
        path = [P[s] for s in tr_path[: k + 1]] + [pos[mover] if (moved_tracer and mover == tr_site) else P[tsite]]
        path = np.array(path)
        ax.plot(path[:, 0], path[:, 1], color=fs.GREEN, lw=2.2, zorder=2.5)
        # interstitial
        i0, i1 = int_path[k], int_path[k + 1]
        ip = C[i0] if i0 == i1 else (1 - f) * C[i0] + f * C[i1]
        ax.add_patch(Circle(ip, 0.25, facecolor=fs.BLUE, edgecolor=INK, lw=1.2, zorder=3.5))
        nv = k + (1 if f >= 1 else 0)
        nt = sum(1 for h in hops[:nv] if h[2])
        ni = sum(1 for a, b in zip(int_path[:nv], int_path[1:nv + 1]) if a != b)
        readout(ax, Wx * 0.17, -1.05, f"vacancy jumps: {nv}")
        readout(ax, Wx * 0.5, -1.05, f"labeled-molecule jumps: {nt}")
        readout(ax, Wx * 0.83, -1.05, f"interstitial jumps: {ni}")

    return v, draw


# -- 6. thermally activated jumps: the Arrhenius law ------------------------------------------
KT_STAGES = [0.15, 0.20, 0.25, 0.33]       # k_B T / dU


def langevin(x, v, kT, steps, dt, rng, gamma=1.0):
    """Underdamped Langevin dynamics in U = (1 - cos 2 pi x) / 2 (barrier 1, period 1)."""
    c = np.sqrt(2 * gamma * kT * dt)
    for _ in range(steps):
        force = -np.pi * np.sin(2 * np.pi * x)
        v = v + dt * (force - gamma * v) + c * rng.normal(size=x.shape)
        x = x + dt * v
    return x, v


def measured_rates(rng, n=3000, t_total=400.0, dt=0.02):
    """Jump rate per unit time at each stage temperature, from an ensemble."""
    rates = []
    for kT in KT_STAGES:
        x = np.zeros(n)
        v = rng.normal(scale=np.sqrt(kT), size=n)
        x, v = langevin(x, v, kT, 500, dt, rng)       # equilibrate in the well
        well = np.round(x)
        jumps = 0
        steps = int(t_total / dt / 50)
        for _ in range(steps):
            x, v = langevin(x, v, kT, 50, dt, rng)
            w = np.round(x)
            jumps += np.count_nonzero(w != well)
            well = w
        rates.append(jumps / (n * t_total))
    return np.array(rates)


def sci(x, digits=1):
    """x as a LaTeX a x 10^b string."""
    e = int(np.floor(np.log10(x)))
    return f"${x / 10 ** e:.{digits}f}\\times10^{{{e}}}$"


@mechanism("thermal-activation", 6)
def thermal_activation():
    rng = np.random.default_rng(2)
    rows, wells = 6, 6
    frames_per_stage, dt, sub = 110, 0.02, 20      # 0.4 time units per frame
    amp, gap, rb = 0.45, 0.75, 0.11                # drawn barrier height, row spacing, ball radius
    a, b = 0.03, 0.85                              # the four temperatures play over [a, b]
    # the displayed trajectories, one per row, through the four temperatures
    X = np.zeros((len(KT_STAGES) * frames_per_stage + 1, rows))
    x = np.zeros(rows)
    v = np.zeros(rows)
    k = 0
    for kT in KT_STAGES:
        for _ in range(frames_per_stage):
            x, v = langevin(x, v, kT, sub, dt, rng)
            k += 1
            X[k] = x
    rates = measured_rates(np.random.default_rng(3))
    inv = 1 / np.array(KT_STAGES)
    slope, icpt = np.polyfit(inv, np.log(rates), 1)
    nframes = X.shape[0] - 1
    top = (rows - 1) * gap + amp

    v_ = Video(
        slug="thermal-activation",
        title="Thermally activated jumps: the Arrhenius law",
        captions=[(0.0, "Defects rattle in potential wells; to jump they must borrow an energy $\\Delta U$ from the lattice"),
                  (0.12, "Cold: hardly any attempt has the energy, so jumps are rare"),
                  (0.24, "Warmer: the high-energy tail of the Boltzmann distribution beyond $\\Delta U$ grows (B)"),
                  (0.45, "The jump rate rises steeply, as $\\nu_0\\exp(-\\Delta U/kT)$"),
                  (0.85, "(C) The logarithm of the rate against $1/T$ is a straight line of slope $-\\Delta U/k$")],
        panels=[dict(rect=[0.02, 0.09, 0.56, 0.79], kind="field", xlim=(-0.7, wells - 0.3),
                     ylim=(-1.3, top + 0.45), letter="A", letter_at=(0.03, 0.97)),
                dict(rect=[0.65, 0.58, 0.32, 0.27], kind="plot", letter="B", letter_at=(0.08, 0.84)),
                dict(rect=[0.65, 0.17, 0.32, 0.27], kind="plot", letter="C", letter_at=(0.92, 0.84))],
        seconds=20)

    def draw(axs, t):
        ax, bx, cx = axs
        fr = int(round(ramp(t, a, b) * nframes))
        stage = min(fr // frames_per_stage, len(KT_STAGES) - 1)
        kT = KT_STAGES[stage]
        xs = np.linspace(-0.5, wells - 0.5, 400)
        for r in range(rows):
            y0 = r * gap
            ax.plot(xs, y0 + amp * 0.5 * (1 - np.cos(2 * np.pi * xs)), color="0.55", lw=1.2, zorder=1)
            xw = (X[fr, r] + 0.5) % wells - 0.5        # each ball wraps round its row of wells
            yb = y0 + amp * 0.5 * (1 - np.cos(2 * np.pi * xw)) + rb
            ax.add_patch(Circle((xw, yb), rb, facecolor=fs.RED, edgecolor=INK, lw=1.0, zorder=3))
        # jumps so far at this temperature
        seg = X[stage * frames_per_stage:fr + 1]
        jumps = int(np.count_nonzero(np.diff(np.round(seg), axis=0))) if len(seg) > 1 else 0
        readout(ax, 0.9, -0.8, f"$kT/\\Delta U$ = {kT:.2f}")
        readout(ax, 3.7, -0.8, f"jumps at this temperature: {jumps}")
        # (B) Boltzmann distribution and the fraction above the barrier
        E = np.linspace(0, 1.6, 300)
        p = np.exp(-E / kT) / kT
        bx.plot(E, p, color=INK)
        hi = E >= 1.0
        bx.fill_between(E[hi], 1e-5, p[hi], color=fs.RED, alpha=0.5, lw=0)
        bx.axvline(1.0, color=INK, ls="--", lw=1.2)
        bx.set_yscale("log")
        bx.set_ylim(1e-5, 1e3)
        bx.set_xlim(0, 1.6)
        bx.set_yticks([1e-4, 1e-2, 1e0, 1e2])
        bx.set_xlabel(r"energy $E/\Delta U$")
        bx.set_ylabel("probability")
        bx.text(0.04, 0.32, "fraction above $\\Delta U$:\n" + sci(np.exp(-1 / kT)), transform=bx.transAxes,
                fontsize=FS_TICK, va="top")
        fs.grid(bx)
        # (C) Arrhenius plot: a point as each temperature finishes, then the fit
        done = min(fr // frames_per_stage, len(KT_STAGES))
        cx.plot(inv[:done], rates[:done], "o", color=fs.RED, mec=INK, zorder=3)
        if done == len(KT_STAGES):
            xx = np.linspace(2.6, 7.2, 10)
            cx.plot(xx, np.exp(icpt + slope * xx), color=fs.GREY, ls="--", lw=1.4, zorder=1)
            cx.text(0.06, 0.08, f"slope ${slope:.2f}$", transform=cx.transAxes, fontsize=FS_TICK)
        cx.set_yscale("log")
        cx.set_xlim(2.6, 7.2)
        cx.set_ylim(rates.min() / 3, rates.max() * 3)
        cx.set_xlabel(r"$\Delta U/kT$")
        cx.set_ylabel("jump rate")
        fs.grid(cx)

    return v_, draw


# -- 7. the conduction cycle: ionic and Bjerrum defects together -----------------------------------
@mechanism("conduction-cycle", 7)
def conduction_cycle():
    nx, ny, j0 = 14, 5, 2
    rng = np.random.default_rng(7)
    ice = SquareIce(nx, ny)                                 # every row bond owned by its left end
    row = [2 * ice.site(i, j0) for i in range(nx)]          # the row's horizontal bonds
    ice.randomize(rng, 800, forbid=set(row))
    assert all(ice.own[b, 0] for b in row) and ice.obeys_rules()
    sc = Script(ice)
    sc.add(("pause",), 1.8)
    # 1. an ionic pair: H3O+ runs right, OH- runs left, until they meet round the ring
    k = 4
    s = ice.site(k, j0)
    sc.add(("transfer", 2 * s), 1.2, note={"ion": True})
    p, q = (k + 1) % nx, k                                  # columns of H3O+ and OH-
    step = 0
    while (p - q) % nx != 0 and len(sc.events) < 60:
        if step % 3 != 2:
            b = 2 * sc.ice.site(p, j0)                       # H3O+ passes its proton right
            sc.add(("transfer", b), 0.55, note={"ion": True})
            p = (p + 1) % nx
        else:
            b = 2 * sc.ice.site(q - 1, j0)                   # OH- takes the proton from its left
            sc.add(("transfer", b), 0.9, note={"ion": True})
            q = (q - 1) % nx
        step += 1
    sc.add(("pause",), 1.6, note={"polarized": True})
    # 2. a new ionic pair cannot separate along the row: the proton jumps back
    b = 2 * sc.ice.site(7, j0)
    sc.add(("transfer", b), 0.9)
    sc.add(("pause",), 0.5)
    sc.add(("transfer", b), 0.9)
    sc.add(("pause",), 1.2)
    # 3. a Bjerrum pair: D runs right, L runs left, turning each molecule back
    k = 9
    s = sc.ice.site(k, j0)
    bl, bd = 2 * sc.ice.site(k - 1, j0), 2 * s
    sc.add(("rotate", s, bl, bd), 1.2, note={"bj": True})
    pd, pl = k + 1, k - 1                                    # columns of the molecules that move next
    step = 0
    while sc.ice.occ()[bd] == 2 and len(sc.events) < 120:
        if step % 2 == 0:
            w = sc.ice.site(pd, j0)
            nb = 2 * w
            sc.add(("rotate", w, bd, nb), 0.75, note={"bj": True})
            bd, pd = nb, (pd + 1) % nx
        else:
            w = sc.ice.site(pl, j0)
            nb = 2 * sc.ice.site(pl - 1, j0)
            sc.add(("rotate", w, nb, bl), 0.75, note={"bj": True})
            bl, pl = nb, (pl - 1) % nx
        step += 1
        if sc.ice.occ()[bd] == 1 and sc.ice.occ()[bl] == 1:
            break
    sc.add(("pause",), 4.2)
    assert sc.ice.obeys_rules()

    v = Video(
        slug="conduction-cycle",
        title="Why ice conducts only with both kinds of defect",
        captions=[(0.0, "One row of molecules (shaded) in a field $E$; the lattice is periodic, so the row closes on itself"),
                  (0.055, "An ionic pair forms: H$_3$O$^+$ runs with the field, OH$^-$ against it, until they meet"),
                  (0.365, "Every bond in the row now holds its proton on its right: the row is polarized"),
                  (0.41, "A proton can now only jump back, against the field, and it soon returns: ions alone are blocked"),
                  (0.52, "A Bjerrum pair forms: D runs with the field, L against it, turning each molecule back"),
                  (0.87, "The row is restored. Ionic ($\\approx0.6e$) and Bjerrum ($\\approx0.4e$) defects together carry one proton")],
        xlim=(-1.3, nx + 0.3), ylim=(-1.9, ny + 0.8), seconds=24)

    def draw(ax, t):
        ax.add_patch(Rectangle((-1.2, j0 - 0.42), nx + 1.4, 0.84, facecolor="#fff3c4", edgecolor="none",
                               zorder=0))
        ice_now, moving, rec, f = draw_script(ax, sc, t, trail_bonds=(), trail_sites=())
        field_arrow(ax, nx / 2 - 1.1, ny - 0.15)
        right = sum(1 for b in row if ice_now.own[b, 1])
        ions = count_done(sc, t, 0, 1, "ion")
        bj = count_done(sc, t, 0, 1, "bj")
        n_ion = sum(1 for r in sc.events if r["note"].get("ion"))
        n_bj = sum(1 for r in sc.events if r["note"].get("bj"))
        charge = 0.62 * ions / n_ion + 0.38 * bj / n_bj
        readout(ax, 3.2, -1.3, f"row bonds with proton on the right: {right}/{nx}")
        readout(ax, nx - 3.4, -1.3, f"charge carried round: {charge:.2f}$e$")

    return v, draw


# -- 8. dielectric relaxation ------------------------------------------------------------------------
N_PAIRS, MC_PER_FRAME = 8, 3        # Bjerrum pairs in the dielectric clip; Monte Carlo steps per frame


def bjerrum_mc(ice, rng, E_of, n_steps, kT=1.0, record_every=1):
    """Metropolis dynamics of a fixed population of D- and L-defects in a field along x.
    Returns snapshots of the proton arrangement and the mean dipole (polarization)."""
    snaps, P = [], []
    for step in range(n_steps):
        E = E_of(step)
        occ = ice.occ()
        defects = np.where(occ != 1)[0]
        b = int(defects[rng.integers(len(defects))])
        moves = []
        if occ[b] == 2:
            for w in ice.end[b]:
                for c, e, k in ice.bonds_of(int(w)):
                    if c != b and not ice.own[c, e] and occ[c] == 1:
                        moves.append((int(w), b, c))
        else:
            for w in ice.end[b]:
                for c, e, k in ice.owned(int(w)):
                    if c != b and occ[c] == 1:
                        moves.append((int(w), c, b))
        if moves:
            w, bf, bt = moves[rng.integers(len(moves))]
            kf = [k for bb, e, k in ice.bonds_of(w) if bb == bf][0]
            kt = [k for bb, e, k in ice.bonds_of(w) if bb == bt][0]
            dpx = DIRS[kt][0] - DIRS[kf][0]
            if rng.random() < np.exp(min(0.0, E * dpx / kT)):
                ice.rotate(w, bf, bt)
        if step % record_every == 0:
            snaps.append(ice.own.copy())
            P.append(ice.dipole()[:, 0].mean())
    return snaps, np.array(P)


@mechanism("dielectric-relaxation", 8)
def dielectric_relaxation():
    nx, ny = 12, 8
    rng = np.random.default_rng(8)
    ice = SquareIce(nx, ny).randomize(rng, 900)
    # a fixed population of Bjerrum pairs, made by rotating molecules
    pairs = 0
    for s in rng.permutation(ice.N):
        s, occ = int(s), ice.occ()
        own = [o for o in ice.owned(s) if occ[o[0]] == 1]
        free = [o for o in ice.bonds_of(s) if not ice.own[o[0], o[1]] and occ[o[0]] == 1]
        if len(own) == 2 and free:
            ice.rotate(s, own[0][0], free[0][0])
            pairs += 1
        if pairs == N_PAIRS:
            break
    n_frames, per = 1200, MC_PER_FRAME                    # Monte Carlo steps per frame
    E0 = 0.8
    t_on, t_off, t_osc = 0.06, 0.36, 0.66

    def field(u):
        if u < t_on or t_off <= u < t_osc:
            return 0.0
        if u < t_off:
            return E0
        return E0 * np.sin(2 * np.pi * (u - t_osc) / 0.025)

    snaps, P = bjerrum_mc(ice, rng, lambda st: field(st / (n_frames * per)), n_frames * per,
                          record_every=per)
    u_grid = np.linspace(0, 1, len(P))
    fE = np.array([field(x) for x in u_grid]) / E0

    v = Video(
        slug="dielectric-relaxation",
        title="Dielectric relaxation: Bjerrum defects turn the dipoles",
        captions=[(0.0, "Molecules colored by their dipole across the page: red points right, blue left, white neither"),
                  (0.06, "A field $E$ is switched on; wandering D- and L-defects leave molecules turned along it"),
                  (0.20, "The polarization grows to a large equilibrium value (B): the high static permittivity, near 100"),
                  (0.36, "Switch the field off and the same defects randomize the dipoles again, over the relaxation time"),
                  (0.66, "A field alternating faster than the defects can follow barely polarizes the ice ($\\varepsilon\\approx3.2$)")],
        panels=[dict(rect=[0.02, 0.09, 0.58, 0.79], kind="field", xlim=(-0.9, nx - 0.1), ylim=(-1.8, ny + 0.6),
                     letter="A", letter_at=(0.03, 0.97)),
                dict(rect=[0.69, 0.22, 0.28, 0.52], kind="plot", letter="B", letter_at=(0.08, 0.92))],
        seconds=20)

    def draw(axs, t):
        ax, bx = axs
        u = float(np.clip(t, 0, 1))
        k = int(round(u * (len(snaps) - 1)))
        state = ice.copy()
        state.own = snaps[k]
        px = state.dipole()[:, 0]
        fills = [LIGHT_RED if p > 0 else LIGHT_BLUE if p < 0 else "white" for p in px]
        draw_ice(ax, state, fills=fills, labels=True)
        E = field(u)
        if abs(E) > 1e-6:
            on = abs(E) / E0
            field_arrow(ax, nx / 2 - 1.1 * np.sign(E) * on, ny - 0.15, L=2.2 * np.sign(E), on=on)
        readout(ax, 2.6, -1.25, f"field: {'on' if abs(E) > 1e-6 else 'off'}")
        readout(ax, nx - 3.5, -1.25, f"polarization: {P[k]:+.2f}")
        # (B) field and polarization against time
        bx.plot(u_grid, fE, color=fs.GREY, lw=1.0, alpha=0.35)
        bx.plot(u_grid[: k + 1], fE[: k + 1], color=fs.GREY, lw=1.6, label="field $E/E_0$")
        bx.plot(u_grid[: k + 1], P[: k + 1], color=fs.RED, label=r"polarization $\langle p_x\rangle$")
        bx.set_xlim(0, 1)
        bx.set_ylim(-1.25, 1.6)
        bx.set_xticks([])
        bx.set_xlabel("time")
        bx.set_ylabel(r"$E/E_0$ and $\langle p_x\rangle$")
        bx.legend(loc="lower left", fontsize=13)
        fs.grid(bx)

    return v, draw
