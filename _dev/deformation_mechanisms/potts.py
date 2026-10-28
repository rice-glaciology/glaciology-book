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

from common import (ACCENT, ACCENT2, FAINT, INK, MUTED, STRESS, Video, load_arrows,
                    mechanism, orient_color, smooth)

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
    ax.plot([0, NX, NX, 0, 0], [0, 0, NY, NY, 0], color=INK, lw=1.5, zorder=2)


def draw_hist(ax, model, x0=NX + 12, y0=14, w=36, h=62, title="c-axis angle\nfrom compression"):
    p = model.orientation_hist()
    nb = len(p)
    bw = w / nb
    for i, pi in enumerate(p):
        mid = (i + 0.5) * 90 / nb
        col = orient_color(np.radians(90 - mid))
        ax.add_patch(_rect(x0 + i * bw, y0, bw * 0.9, h * min(pi / 0.35, 1.0), col))
    ax.plot([x0, x0 + w], [y0, y0], color=INK, lw=1)
    ax.text(x0 + w / 2, y0 + h + 6, title, ha="center", va="bottom", fontsize=11)
    for v, lab in ((0, "0°"), (45, "45°"), (90, "90°")):
        ax.text(x0 + w * v / 90, y0 - 4, lab, ha="center", va="top", fontsize=10, color=MUTED)
    ax.text(x0 + w / 2, y0 - 13, "area fraction", ha="center", va="top", fontsize=10, color=MUTED)


def _rect(x, y, w, h, col):
    from matplotlib.patches import Rectangle
    return Rectangle((x, y), w, h, facecolor=col, edgecolor=INK, lw=0.6, zorder=3)


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
        title="Migration recrystallization",
        scale="Grain scale · millimetres to centimetres",
        facts=[("What happens", "Boundaries bulge and sweep from grains with few dislocations into grains with many"),
               ("Driving force", "Difference in stored strain energy (dislocation density) across a boundary"),
               ("When", "Warm ice, above about -10 °C, with fast deformation"),
               ("Consequence", "Large, interlocking grains; the survivors are those well oriented for basal slip, so fabrics form fast")],
        where="Warm basal ice of ice sheets, temperate glaciers and shear margins: interlocking "
              "grains up to centimetres across and multi-maximum fabrics.",
        captions=[(0.0, "Deformed warm ice under vertical compression. Darker grains hold more dislocations (more stored strain energy)."),
                  (0.08, "Hard grains (c-axes near 0° or 90° to the load) cannot slip, so they keep storing dislocations."),
                  (0.20, "Soft grains, oriented for easy slip, recover and stay clean. Their boundaries bulge into dirty neighbors."),
                  (0.45, "Each swept region is reset to strain-free crystal of the growing grain's orientation."),
                  (0.70, "The survivors are well-oriented grains with irregular, lobate boundaries: watch the orientation histogram shift."),
                  (0.88, "Migration recrystallization manufactures the soft fabric that makes tertiary creep fast.")],
        xlim=(-4, NX + 54), ylim=(-26, NY + 12), seconds=15)

    def draw(ax, t):
        m = run.at(t)
        draw_field(ax, m, EMAX)
        draw_hist(ax, m)
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
        title="Nucleation of new grains",
        scale="Grain scale · millimetres",
        facts=[("What happens", "Small strain-free grains appear at highly deformed sites and grow into the old grains"),
               ("Where nuclei form", "Grain boundaries, triple junctions and kink bands, where dislocations pile up"),
               ("New orientations", "Often well oriented for basal slip, unrelated to the parent grain"),
               ("Consequence", "Grain size resets; strain softening as new soft grains take over")],
        where="Warm, rapidly deforming ice near the bed and in shear margins, and in laboratory "
              "tests where it drives the tertiary acceleration of the creep curve.",
        captions=[(0.0, "Heavily deformed ice: every grain is dark with stored dislocations."),
                  (0.06, "New strain-free grains (bright) nucleate where dislocations are densest, along the old boundaries."),
                  (0.25, "They grow rapidly, because the stored energy of the old grains drives their boundaries forward."),
                  (0.50, "A necklace of new grains outlines the old ones, then consumes them."),
                  (0.75, "The new grains favor orientations soft for basal slip, so the ice weakens: tertiary creep.")],
        xlim=(-4, NX + 54), ylim=(-26, NY + 12), seconds=15)

    def draw(ax, t):
        m = run.at(t)
        draw_field(ax, m, EMAX)
        draw_hist(ax, m)
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
        title="Normal grain growth",
        scale="Grain scale · millimetres, over centuries",
        facts=[("What happens", "Curved boundaries migrate toward their centers of curvature; small grains shrink and vanish"),
               ("Driving force", "Grain-boundary energy (~0.065 J/m²): less boundary area, lower energy"),
               ("Growth law", "$d^{2} - d_0^{2} = K\\,t$,  K ∝ exp(-Q/RT)"),
               ("Activation energy", "~40 to 50 kJ/mol"),
               ("Consequence", "Grains coarsen steadily with age: a clock for ice-core depth and temperature")],
        where="Firn and the upper few hundred metres of polar ice sheets, where grain area grows "
              "linearly with age until polygonization caps it.",
        captions=[(0.0, "A fine-grained aggregate with no stored strain energy. Only the boundaries carry energy."),
                  (0.06, "Boundaries move toward their centers of curvature: small, many-cornered-concave grains shrink."),
                  (0.35, "Grains with few neighbors vanish; their neighbors absorb the area."),
                  (0.60, "Mean grain area grows linearly with time (right): d² - d0² = K t, as seen in polar firn and ice."),
                  (0.85, "Growth is slow and thermally activated: centuries in cold polar ice.")],
        xlim=(-4, NX + 54), ylim=(-26, NY + 12), seconds=15)

    def draw(ax, t):
        m = run.at(t)
        draw_field(ax, m, 1.0)
        # mean grain area vs time
        x0, y0, w, h = NX + 12, 14, 36, 62
        ax.plot([x0, x0 + w], [y0, y0], color=INK, lw=1)
        ax.plot([x0, x0], [y0, y0 + h], color=INK, lw=1)
        if hist:
            tt = np.array([a for a, _ in hist]) / TOTAL
            aa = np.array([b for _, b in hist])
            ax.plot(x0 + w * tt, y0 + h * aa / 600.0, color=ACCENT, lw=2.2, zorder=4)
            ax.plot(x0 + w * tt[-1], y0 + h * aa[-1] / 600.0, "o", color=ACCENT, ms=6, zorder=5)
        ax.text(x0 + w / 2, y0 + h + 10, "mean grain area", ha="center", va="bottom", fontsize=11)
        ax.text(x0 + w / 2, y0 - 4, "time", ha="center", va="top", fontsize=10, color=MUTED)

    return v, draw
