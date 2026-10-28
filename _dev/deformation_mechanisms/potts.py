"""Recrystallization and grain growth with a Monte Carlo Potts model.

Each grid site belongs to a grain (an integer label). A site may switch to the
label of a neighbor; the energy change is

    dE = J * (change in number of unlike neighbors)       boundary energy
       + (E_neighbor - E_site)                              stored strain energy

Boundary energy alone gives curvature-driven normal grain growth. Adding
stored energy (dislocation density) makes strain-free grains sweep into
deformed ones: strain-induced boundary migration and the growth of new nuclei.
Sites are darker where the stored energy is higher.
"""
import numpy as np

import figstyle as fs
from common import (ACCENT, INK, Video, load_arrows, mechanism, orient_color, smooth)

NX, NY = 180, 112
UP = 4  # upsampling for crisp boundaries
DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


class Potts:
    def __init__(self, ngrains, rng, J=1.0, kT=0.45):
        self.rng, self.J, self.kT = rng, J, kT
        yy, xx = np.mgrid[0:NY, 0:NX]
        seeds = np.c_[rng.uniform(0, NX, ngrains), rng.uniform(0, NY, ngrains)]
        d = np.full((NY, NX), np.inf)
        self.L = np.zeros((NY, NX), int)
        for k, (sx, sy) in enumerate(seeds):  # periodic Voronoi
            dx = np.abs(xx - sx); dx = np.minimum(dx, NX - dx)
            dy = np.abs(yy - sy); dy = np.minimum(dy, NY - dy)
            dk = dx ** 2 + dy ** 2
            m = dk < d
            d[m], self.L[m] = dk[m], k
        self.theta = list(rng.uniform(0, np.pi, ngrains))
        self.E = np.zeros((NY, NX))
        self.sub = [((yy % 2) == a) & ((xx % 2) == b) for a in (0, 1) for b in (0, 1)]
        self.sweeps = 0

    def new_label(self, theta):
        self.theta.append(theta)
        return len(self.theta) - 1

    def sweep(self, n=1):
        L, E, J = self.L, self.E, self.J
        for _ in range(n):
            for mask in self.sub:
                k = self.rng.integers(0, 8, size=L.shape)
                cand = np.empty_like(L)
                candE = np.empty_like(E)
                for i, (dy, dx) in enumerate(DIRS):
                    m = k == i
                    cand[m] = np.roll(L, (-dy, -dx), axis=(0, 1))[m]
                    candE[m] = np.roll(E, (-dy, -dx), axis=(0, 1))[m]
                act = mask & (cand != L)
                if not act.any():
                    continue
                n_old = np.zeros(L.shape, int)
                n_new = np.zeros(L.shape, int)
                for dy, dx in DIRS:
                    nb = np.roll(L, (-dy, -dx), axis=(0, 1))
                    n_old += nb != L
                    n_new += nb != cand
                dE = J * (n_new - n_old) + (candE - E)
                acc = act & ((dE <= 0) | (self.rng.random(L.shape) < np.exp(-np.clip(dE, 0, 50) / self.kT)))
                L[acc] = cand[acc]
                E[acc] = candE[acc]
            self.sweeps += 1

    def boundary_sites(self):
        b = np.zeros(self.L.shape, bool)
        for dy, dx in DIRS:
            b |= np.roll(self.L, (-dy, -dx), axis=(0, 1)) != self.L
        return b

    def image(self, Emax):
        th = np.array(self.theta)
        rgb = orient_color(th)[:, :3][self.L]
        rgb = rgb * (1 - 0.55 * np.clip(self.E / Emax, 0, 1) ** 1.2)[..., None]
        big = np.kron(self.L, np.ones((UP, UP), int))
        img = np.kron(rgb, np.ones((UP, UP, 1)))
        edge = (big != np.roll(big, 1, 0)) | (big != np.roll(big, 1, 1))
        edge |= np.roll(edge, 1, 0) | np.roll(edge, 1, 1)
        img[edge] = np.array([0.12, 0.16, 0.2])
        return img

    def orientation_hist(self, bins=9):
        """Area fraction by c-axis angle from the vertical compression axis (0-90°)."""
        th = np.array(self.theta)[self.L].ravel()
        ang = np.degrees(np.abs(((th - np.pi / 2) + np.pi / 2) % np.pi - np.pi / 2))
        h, _ = np.histogram(ang, bins=bins, range=(0, 90))
        return h / h.sum()


def draw_field(ax, model, Emax):
    ax.imshow(model.image(Emax), extent=(0, NX, 0, NY), origin="lower", interpolation="nearest", zorder=1)
    ax.plot([0, NX, NX, 0, 0], [0, 0, NY, NY, 0], color=INK, lw=fs.s(0.6), zorder=2)


def draw_hist(bx, model):
    """(b) Area fraction of each c-axis angle from the compression axis, in the colour bands."""
    p = model.orientation_hist()
    edges = np.linspace(0, 90, len(p) + 1)
    mids = 0.5 * (edges[:-1] + edges[1:])
    bx.bar(mids, p, width=0.9 * (edges[1] - edges[0]), color=orient_color(np.radians(90 - mids)),
           edgecolor=INK, lw=fs.s(0.5), zorder=3)
    bx.set_xlim(0, 90); bx.set_ylim(0, 0.6)
    bx.set_xticks([0, 45, 90]); bx.set_yticks([0, 0.2, 0.4, 0.6])
    bx.set_xlabel("c-axis angle from compression (°)")
    bx.set_ylabel("area fraction")
    fs.grid(bx)


PANELS = [dict(rect=[0.02, 0.10, 0.64, 0.86], kind="field", xlim=(-4, NX + 4), ylim=(-18, NY + 18),
               letter="a", letter_at=(0.035, 0.90)),
          dict(rect=[0.75, 0.26, 0.22, 0.52], kind="plot", letter="b", letter_at=(0.10, 0.90))]


class Runner:
    """Advance a simulation monotonically with t; restart if t goes backwards."""

    def __init__(self, make, total_sweeps, step):
        self.make, self.total, self.step = make, total_sweeps, step
        self.model, self.t = None, None

    def at(self, t):
        if self.model is None or t < self.t:
            self.model, self.t = self.make(), 0.0
            self.done = 0
        target = int(round(self.total * t))
        while self.done < target:
            n = min(4, target - self.done)
            self.step(self.model, self.done, n)
            self.done += n
        self.t = t
        return self.model


def softness(theta):
    """Schmid-like factor for vertical compression: 1 for c-axes at 45°."""
    return np.abs(np.sin(2 * np.asarray(theta)))


def soft_orientation(rng):
    return (np.pi / 4 + rng.normal(0, 0.22)) * rng.choice([1, 3])


# -- 12. strain-induced boundary migration ----------------------------------------
@mechanism("migration-recrystallization", 12)
def migration():
    EMAX = 0.9

    def make():
        rng = np.random.default_rng(14)
        m = Potts(42, rng, kT=0.3)
        m.sweep(12)
        s = softness(m.theta)
        Eg = EMAX * (1 - s) ** 1.5 * rng.uniform(0.8, 1.0, len(s))
        m.E = Eg[m.L]
        return m

    def step(m, done, n):
        m.sweep(n)
        s = softness(m.theta)[m.L]
        m.E = np.minimum(m.E + 0.003 * n * (1 - s), EMAX)  # deformation keeps storing energy

    run = Runner(make, 170, step)

    v = Video(
        slug="migration-recrystallization",
        captions=[(0.0, '(a) deformed warm ice, darker = more stored strain energy; (b) c-axis angles'),
                  (0.2, 'Clean, well-oriented grains bulge into deformed neighbours'),
                  (0.7, 'The survivors are oriented for basal slip')],
        panels=PANELS, seconds=15)

    def draw(axs, t):
        ax, bx = axs
        m = run.at(t)
        draw_field(ax, m, EMAX)
        draw_hist(bx, m)
        load_arrows(ax, (0, NX, 0, NY), "compress-y", strength=1.0, size=0.06, gap=0.02)

    return v, draw


# -- 13. nucleation (discontinuous dynamic recrystallization) --------------------
@mechanism("nucleation-recrystallization", 13)
def nucleation():
    EMAX = 1.1

    def make():
        rng = np.random.default_rng(31)
        m = Potts(30, rng, kT=0.5)
        m.sweep(12)
        Eg = rng.uniform(0.7, 1.05, len(m.theta))
        m.E = Eg[m.L]
        m.new_grains = set()
        return m

    def step(m, done, n):
        rng = m.rng
        # nucleate at high-energy boundary sites, mostly early on
        frac = done / 340
        k = rng.poisson(n * 0.55 * np.exp(-2.5 * frac)) if frac < 0.8 else 0
        if k:
            b = m.boundary_sites() & (m.E > 0.5)
            ys, xs = np.nonzero(b)
            for _ in range(k if len(ys) else 0):
                i = rng.integers(len(ys))
                lab = m.new_label(soft_orientation(rng))
                m.new_grains.add(lab)
                yy, xx = np.mgrid[-2:3, -2:3]
                disk = (yy ** 2 + xx ** 2) <= 5
                Y = (ys[i] + yy[disk]) % NY
                X = (xs[i] + xx[disk]) % NX
                m.L[Y, X] = lab
                m.E[Y, X] = 0.0
        m.sweep(n)
        m.E = np.minimum(m.E + 0.001 * n, EMAX)

    run = Runner(make, 340, step)

    v = Video(
        slug="nucleation-recrystallization",
        captions=[(0.0, '(a) heavily deformed ice, darker = more stored strain energy; (b) c-axis angles'),
                  (0.06, 'Strain-free nuclei form at old grain boundaries'),
                  (0.5, 'New grains consume the deformed matrix')],
        panels=PANELS, seconds=15)

    def draw(axs, t):
        ax, bx = axs
        m = run.at(t)
        draw_field(ax, m, EMAX)
        draw_hist(bx, m)
        load_arrows(ax, (0, NX, 0, NY), "compress-y", strength=1.0, size=0.06, gap=0.02)

    return v, draw


# -- 14. normal grain growth -----------------------------------------------------
@mechanism("grain-growth", 14)
def grain_growth():
    TOTAL = 420
    hist = []

    def make():
        hist.clear()
        rng = np.random.default_rng(7)
        m = Potts(420, rng, kT=0.5)
        m.sweep(3)
        return m

    def step(m, done, n):
        m.sweep(n)
        hist.append((m.sweeps, NX * NY / len(np.unique(m.L))))

    run = Runner(make, TOTAL, step)

    v = Video(
        slug="grain-growth",
        captions=[(0.0, '(a) no stored energy: boundary energy alone drives growth'),
                  (0.35, 'Small grains shrink and vanish'),
                  (0.6, '(b) mean grain area grows linearly in time')],
        panels=PANELS, seconds=15)

    def draw(axs, t):
        ax, bx = axs
        m = run.at(t)
        draw_field(ax, m, 1.0)
        # (b) mean grain area against time
        if hist:
            tt = np.array([a for a, _ in hist])
            aa = np.array([b for _, b in hist])
            bx.plot(tt, aa, color=fs.RED, zorder=4)
            bx.plot(tt[-1], aa[-1], "o", color=fs.RED, mec=INK, mew=fs.s(0.5), zorder=5)
        bx.set_xlim(0, TOTAL); bx.set_ylim(0, 600)
        bx.set_xlabel("Monte Carlo steps")
        bx.set_ylabel("mean grain area (cells)")
        fs.nice_ticks(bx)
        fs.grid(bx)

    return v, draw
