"""Atomic-scale mechanisms: elasticity, basal glide, non-basal glide, climb, kinking.

The crystal is a 2D hexagonal lattice seen edge-on to the basal planes: each
horizontal row of molecules is one basal plane and the c-axis points up.
Dislocations are drawn with the linear-elastic displacement field of an edge
dislocation, so the atoms around a core are distorted the way they should be.
The proton (hydrogen) arrangement is not drawn.
"""
import numpy as np
from matplotlib.collections import EllipseCollection, LineCollection
from matplotlib.patches import Polygon
from scipy.spatial import cKDTree

import figstyle as fs
from common import (ACCENT, ACCENT2, FAINT, FS, FS_TICK, ICE, INK, MUTED, Video, arrow,
                    data_letter, load_arrows, readout, mechanism, orient_color, ramp, smooth)

H = np.sqrt(3) / 2  # spacing between basal planes (nearest-neighbor distance = 1)


# -- lattice and dislocation geometry -------------------------------------
def hex_lattice(nx, ny):
    """Sites (x, y) and row index j for a hexagonal patch, rows j = -ny..ny."""
    pts, rows = [], []
    for j in range(-ny, ny + 1):
        for i in range(-nx, nx + 1):
            pts.append((i + 0.5 * (j % 2), j * H))
            rows.append(j)
    return np.array(pts, float), np.array(rows)


def edge_field(P, path, b=1.0, nu=0.3, core=0.35):
    """Displacement of sites P by an edge dislocation that travelled along `path`.

    `path` is the core's trajectory [(x, y), ...]; the last point is the current
    core. The slipped surface (where the lattice is offset by b) follows the
    path, so glide, climb, and glide again on a new plane are all handled. The
    elastic strain terms are those of the current core. Extra half-plane is
    above the glide plane for b > 0.
    """
    z = P[:, 0] + 1j * P[:, 1]
    pts = [complex(*p) for p in path]
    theta = np.angle(z - pts[0])
    for a, c in zip(pts[:-1], pts[1:]):
        theta = theta + np.angle((z - c) / (z - a))
    d = z - pts[-1]
    dx, dy = d.real, d.imag
    r2 = dx ** 2 + dy ** 2 + core ** 2
    ux = b / (2 * np.pi) * (theta + dx * dy / (2 * (1 - nu) * r2))
    uy = -b / (2 * np.pi) * ((1 - 2 * nu) / (4 * (1 - nu)) * np.log(r2)
                             + (dx ** 2 - dy ** 2) / (4 * (1 - nu) * r2))
    return np.c_[ux, uy]


def slip_step(P, y0, b=1.0):
    """Displacement after a dislocation has crossed the whole crystal on plane y0."""
    u = np.zeros_like(P)
    u[:, 0] = 0.5 * b * np.sign(P[:, 1] - y0)
    return u


def glide_disp(P, y0, s, x_in, x_out, b=1.0):
    """Displacement for one dislocation at position s along plane y0.

    The core nucleates at the left surface (x_in) and leaves at the right
    (x_out); the field fades in on entry and becomes a clean surface step on exit.
    """
    if s <= x_in - 1.5:
        return np.zeros_like(P)
    if s >= x_out + 1.5:
        return slip_step(P, y0, b)
    u = edge_field(P, [(-400, y0), (s, y0)], b)
    if s < x_in:
        u *= smooth(s, x_in - 1.5, x_in)
    if s > x_out:
        w = smooth(s, x_out, x_out + 1.5)
        u = (1 - w) * u + w * slip_step(P, y0, b)
    return u


# -- drawing ----------------------------------------------------------------
def draw_atoms(ax, Q, colors, r=0.27, edge=INK, lw=fs.s(0.4), z=3):
    n = len(Q)
    ax.add_collection(EllipseCollection(
        np.full(n, 2 * r), np.full(n, 2 * r), np.zeros(n), units="xy", offsets=Q,
        offset_transform=ax.transData, facecolors=colors, edgecolors=edge,
        linewidths=lw, zorder=z))


def draw_bonds(ax, Q, rows, cutoff=1.32, strain_colors=False):
    """Bonds to neighbors. In-plane (basal) bonds are dark, between-plane ones light."""
    pairs = np.array(sorted(cKDTree(Q).query_pairs(cutoff)))
    if len(pairs) == 0:
        return
    seg = Q[pairs]
    same = rows[pairs[:, 0]] == rows[pairs[:, 1]]
    if strain_colors:
        L = np.linalg.norm(seg[:, 1] - seg[:, 0], axis=1)
        e = np.clip((L - 1.0) / 0.12, -1, 1)
        grey = np.array(matplotlib_color("0.55"))
        red, blue = np.array(matplotlib_color(fs.RED)), np.array(matplotlib_color(fs.BLUE))
        col = np.where(e[:, None] > 0, (1 - e[:, None]) * grey + e[:, None] * red,
                       (1 + e[:, None]) * grey - e[:, None] * blue)
        ax.add_collection(LineCollection(seg, colors=col, linewidths=fs.s(1.1), zorder=2))
        return
    ax.add_collection(LineCollection(seg[same], colors=INK, linewidths=fs.s(0.9), zorder=2))
    ax.add_collection(LineCollection(seg[~same], colors="0.65", linewidths=fs.s(0.45), zorder=2))


def draw_core(ax, x, y, size=0.7, color=ACCENT, up=True, angle=0.0, lw=fs.s(1.5)):
    """The edge-dislocation symbol: a bar on the glide plane and a stem along the
    extra half-plane."""
    c, s = np.cos(angle), np.sin(angle)
    R = np.array([[c, -s], [s, c]])
    bar = np.array([[-size, 0], [size, 0]]) @ R.T + (x, y)
    stem = np.array([[0, 0], [0, 1.3 * size if up else -1.3 * size]]) @ R.T + (x, y)
    ax.plot(*bar.T, color=color, lw=lw, zorder=6, solid_capstyle="round")
    ax.plot(*stem.T, color=color, lw=lw, zorder=6, solid_capstyle="round")


def caxis(ax, x, y, L=2.0, angle=np.pi / 2, label="c", color=INK):
    dx, dy = L * np.cos(angle), L * np.sin(angle)
    arrow(ax, x, y, dx, dy, color=color)
    ax.text(x + dx * 1.15, y + dy * 1.15, label, fontsize=FS, style="italic",
            color=color, ha="center", va="center")


def core_glow(Q, cores, base=ICE, hot=ACCENT, width=1.8):
    """Atom colors: tint atoms near any dislocation core."""
    base = np.array(matplotlib_color(base))
    hot = np.array(matplotlib_color(hot))
    w = np.zeros(len(Q))
    for (x, y) in cores:
        w = np.maximum(w, np.exp(-((Q[:, 0] - x) ** 2 + (Q[:, 1] - y) ** 2) / width ** 2))
    w = 0.75 * w[:, None]
    return (1 - w) * base + w * (0.45 * hot + 0.55 * np.array([1, 1, 1, 1]))


def matplotlib_color(c):
    from matplotlib.colors import to_rgba
    return to_rgba(c)


# -- 1. elasticity -----------------------------------------------------------
@mechanism("elastic", 1)
def elastic():
    P, rows = hex_lattice(9, 4)
    P[:, 1] -= 0.3

    def gamma(t):
        return 0.16 * (smooth(t, 0.08, 0.28) - smooth(t, 0.52, 0.68))

    v = Video(
        slug="elastic",
        title="Elastic deformation",
        captions=[(0.0, 'Unloaded crystal; each row of molecules is a basal plane'),
                  (0.08, 'Shear applied: bonds stretch (red) and compress (blue)'),
                  (0.52, 'Load removed: the crystal recovers exactly')],
        panels=[dict(rect=[0.02, 0.09, 0.62, 0.79], kind="field", xlim=(-13, 11), ylim=(-7.4, 6.8), letter="A"),
                dict(rect=[0.74, 0.26, 0.22, 0.46], kind="plot", letter="B", letter_at=(0.10, 0.90))],
        seconds=12)

    def draw(axs, t):
        ax, bx = axs
        g = gamma(t)
        Q = P.copy()
        Q[:, 0] += g * (P[:, 1] + 0.3)
        draw_bonds(ax, Q, rows, cutoff=1.4, strain_colors=True)
        draw_atoms(ax, Q, ICE)
        load_arrows(ax, (-9, 9, -4.0, 3.5), "shear", strength=g / 0.16)
        caxis(ax, -11.8, -1.5)
        # (b) stress against strain: one straight line, traced up and back down
        f = g / 0.16
        bx.plot([0, 1], [0, 1], color=fs.BLACK, lw=fs.s(0.8))
        bx.plot(f, f, "o", color=fs.RED, mec=fs.BLACK, mew=fs.s(0.5), zorder=5)
        bx.set_xlim(0, 1.1); bx.set_ylim(0, 1.1)
        bx.set_xticks([0, 0.5, 1]); bx.set_yticks([0, 0.5, 1])
        bx.set_xlabel("shear strain / peak strain")
        bx.set_ylabel("shear stress / peak stress")
        fs.grid(bx)

    return v, draw


# -- 2. basal glide ------------------------------------------------------------
@mechanism("basal-glide", 2)
def basal_glide():
    P, rows = hex_lattice(11, 5)
    x_in, x_out = -11.4, 11.4
    planes = [0.5 * H, 2.5 * H, -2.5 * H]
    windows = [(0.10, 0.36), (0.40, 0.62), (0.66, 0.86)]

    v = Video(
        slug="basal-glide",
        title="Basal slip",
        captions=[(0.0, 'Shear stress parallel to the basal planes'),
                  (0.08, 'An edge dislocation nucleates and glides'),
                  (0.37, 'Each dislocation that exits leaves a one-molecule step'),
                  (0.86, 'Many dislocations: the crystal shears like a deck of cards')],
        xlim=(-14.5, 14.5), ylim=(-8.2, 10.7), seconds=16)

    def state(t):
        u = np.zeros_like(P)
        cores = []
        for y0, (a, bnd) in zip(planes, windows):
            s = x_in - 1.6 + (x_out - x_in + 3.2) * ramp(t, a, bnd)
            u += glide_disp(P, y0, s, x_in, x_out)
            if x_in - 0.6 < s < x_out + 0.6:
                cores.append((s, y0))
        return P + u, cores

    def draw(ax, t):
        Q, cores = state(t)
        draw_bonds(ax, Q, rows)
        draw_atoms(ax, Q, core_glow(Q, cores))
        for (x, y) in cores:
            draw_core(ax, x, y - 0.05)
        load_arrows(ax, (-11, 11, -4.6, 4.6), "shear", strength=smooth(t, 0.0, 0.06))
        caxis(ax, -13.6, -1.0)
        # deck-of-cards inset: cumulative slip shown on a block of basal planes
        nslip = sum(ramp(t, a, b) for a, b in windows) / 3
        gx, gy, gw, gh, n = 4.0, 7.0, 6.0, 2.8, 7
        for k in range(n):
            off = 1.6 * smooth(t, 0.86, 1.0) * k / (n - 1) + 0.25 * nslip * k / (n - 1)
            ax.add_patch(Polygon([(gx + off, gy + k * gh / n), (gx + gw + off, gy + k * gh / n),
                                  (gx + gw + off, gy + (k + 0.86) * gh / n), (gx + off, gy + (k + 0.86) * gh / n)],
                                 closed=True, facecolor=ICE, edgecolor=INK, lw=fs.s(0.5), zorder=4))
        data_letter(ax, -13.6, 5.6, "A")
        data_letter(ax, gx - 1.0, gy + gh - 0.2, "B")

    return v, draw


# -- 3. non-basal glide --------------------------------------------------------
@mechanism("nonbasal-glide", 3)
def nonbasal_glide():
    # Left: basal planes horizontal, shear on a basal plane (easy).
    PA, rA = hex_lattice(6, 4)
    # Right: crystal rotated 90 degrees (c-axis horizontal); the same horizontal
    # shear must now glide on a prismatic plane that cuts across the basal planes.
    PB0, rB = hex_lattice(4, 5)
    PB = np.c_[-PB0[:, 1], PB0[:, 0]]
    bB = 2 * H  # shortest horizontal lattice translation in the rotated crystal
    yB = 0.25
    xa, xb = -18.0, 7.0  # centers of the two crystals

    v = Video(
        slug="nonbasal-glide",
        title="Basal and prismatic slip",
        captions=[(0.0, 'Same shear stress, two crystal orientations'),
                  (0.15, '(A) basal slip is easy; (B) prismatic slip is ~60 times harder')],
        xlim=(-26.0, 14.0), ylim=(-12.0, 9.5), seconds=15)

    def draw(ax, t):
        # Left crystal: three quick dislocations.
        uA = np.zeros_like(PA)
        coresA = []
        for k, (a, b) in enumerate([(0.12, 0.34), (0.40, 0.62), (0.68, 0.90)]):
            y0 = (0.5 + 2 * (k - 1)) * H
            s = -7.6 + 15.2 * ramp(t, a, b)
            uA += glide_disp(PA, y0, s, -6.4, 6.4)
            if -6.9 < s < 6.9:
                coresA.append((s, y0))
        QA = PA + uA + (xa, 0)
        draw_bonds(ax, QA, rA)
        draw_atoms(ax, QA, core_glow(QA, [(x + xa, y) for x, y in coresA]))
        for x, y in coresA:
            draw_core(ax, x + xa, y - 0.05)
        # Right crystal: one dislocation crawling in jerks.
        prog = ramp(t, 0.12, 1.0)
        jerky = prog + 0.06 * np.sin(2 * np.pi * 6 * prog) / (2 * np.pi)
        s = -4.0 + 5.0 * np.clip(jerky, 0, 1)
        uB = edge_field(PB, [(-400, yB), (s, yB)], b=bB) * smooth(t, 0.12, 0.2)
        QB = PB + uB + (xb, 0)
        draw_bonds(ax, QB, rB)
        draw_atoms(ax, QB, core_glow(QB, [(s + xb, yB)], width=2.4))
        if t > 0.13:
            draw_core(ax, s + xb, yB, size=1.0)
        on = smooth(t, 0.0, 0.05)
        load_arrows(ax, (xa - 6.5, xa + 6.5, -4.0, 4.0), "shear", strength=on, size=0.22)
        load_arrows(ax, (xb - 5.5, xb + 5.5, -5.5, 5.5), "shear", strength=on, size=0.22)
        caxis(ax, xa - 7.8, -6.4, L=1.6)
        caxis(ax, xb - 3.0, -8.9, L=1.6, angle=0.0)
        data_letter(ax, xa - 7.6, 6.2, "A")
        data_letter(ax, xb - 6.6, 7.6, "B")

    return v, draw


# -- 4. dislocation climb ---------------------------------------------------
@mechanism("dislocation-climb", 4)
def climb():
    P, rows = hex_lattice(11, 5)
    y0, y1 = 0.5 * H, 1.5 * H
    xc = -2.5                       # climb column (a site in row 1)
    absorbed = np.where((rows == 1) & np.isclose(P[:, 0], xc))[0][0]
    obstacle = np.where(((rows == 0) | (rows == 1)) & (P[:, 0] > -1.6) & (P[:, 0] < 1.1))[0]
    x_in, x_out = -11.4, 11.4
    t_glide1, t_vac, t_climb, t_glide2 = (0.06, 0.24), (0.30, 0.58), (0.58, 0.66), (0.70, 0.92)

    # Scripted vacancy walk: a biased random walk on the lattice to the half-plane end.
    rng = np.random.default_rng(3)
    tree = cKDTree(P)
    start = np.where((rows == 4) & np.isclose(P[:, 0], 5.0))[0][0]
    walk = [start]
    while walk[-1] != absorbed:
        here = walk[-1]
        nbrs = [j for j in tree.query_ball_point(P[here], 1.05)
                if j != here and j not in obstacle]
        dist = np.array([np.linalg.norm(P[j] - P[absorbed]) for j in nbrs])
        w = np.exp(-1.6 * (dist - dist.min()))
        walk.append(nbrs[rng.choice(len(nbrs), p=w / w.sum())])

    def lattice_state(t):
        """Positions (with all sites), active cores, and whether the site is gone."""
        if t < t_climb[0]:
            s = x_in - 1.6 + (xc - x_in + 1.6) * ramp(t, *t_glide1)
            u = glide_disp(P, y0, s, x_in, x_out)
            return P + u, [(s, y0)] if s > x_in - 0.6 else [], 0.0
        before = P + edge_field(P, [(-400, y0), (xc, y0)])
        if t < t_glide2[0]:
            f = smooth(t, *t_climb)
            after = P + edge_field(P, [(-400, y0), (xc, y0), (xc, y1)])
            return (1 - f) * before + f * after, [(xc, y0 + f * (y1 - y0))], f
        s = xc + (x_out + 1.6 - xc) * ramp(t, *t_glide2)
        path = [(-400, y0), (xc, y0), (xc, y1), (s, y1)]
        if s < x_out:
            u = edge_field(P, path)
        else:
            w = smooth(s, x_out, x_out + 1.5)
            u = (1 - w) * edge_field(P, path) + w * edge_field(P, [(-400, y0), (xc, y0), (xc, y1), (400, y1)])
        return P + u, [(s, y1)] if s < x_out + 0.6 else [], 1.0

    v = Video(
        slug="dislocation-climb",
        title="Dislocation climb",
        captions=[(0.0, 'A dislocation glides to an obstacle'),
                  (0.3, 'A vacancy diffuses to the core'),
                  (0.56, 'The vacancy is absorbed and the dislocation climbs one plane'),
                  (0.7, 'Glide resumes on the new plane')],
        xlim=(-14.5, 14.5), ylim=(-9.3, 9.6), seconds=16)

    def draw(ax, t):
        Q, cores, gone = lattice_state(t)
        show = np.ones(len(P), bool)
        mover = None
        if t_vac[0] <= t < t_climb[0]:
            hops = len(walk) - 1
            x = ramp(t, t_vac[0], t_vac[1] - 0.02) * hops
            k = min(int(x), hops - 1)
            frac = smooth(x - k, 0.15, 0.85)
            if x >= hops:
                show[walk[-1]] = False
                vac = walk[-1]
            else:
                vac_site, next_site = walk[k], walk[k + 1]
                show[vac_site] = False
                show[next_site] = False
                mover = (1 - frac) * Q[next_site] + frac * Q[vac_site]
                vac = vac_site if frac < 0.5 else next_site
        elif t >= t_climb[0]:
            show[absorbed] = False
            vac = absorbed if gone < 1 else None
        else:
            vac = None

        idx = np.where(show)[0]
        draw_bonds(ax, Q[idx], rows[idx])
        col = core_glow(Q[idx], cores)
        is_obs = np.isin(idx, obstacle)
        col[is_obs] = matplotlib_color("#4b5563")
        draw_atoms(ax, Q[idx], col)
        if mover is not None:
            draw_atoms(ax, mover[None], [matplotlib_color(ACCENT2)], z=5)
        if vac is not None:
            alpha = 1 - gone
            ax.add_patch(plt_circle(Q[vac], 0.30, alpha))
        for (x, y) in cores:
            draw_core(ax, x, y - 0.05)
        load_arrows(ax, (-11, 11, -4.6, 4.6), "shear", strength=smooth(t, 0.0, 0.05))
        caxis(ax, -13.6, -1.0)

    return v, draw


def plt_circle(xy, r, alpha):
    from matplotlib.patches import Circle
    return Circle(xy, r, facecolor="none", edgecolor=ACCENT2, lw=fs.s(1.0), ls="--",
                  alpha=float(alpha), zorder=6)


# -- 5. kinking ----------------------------------------------------------------
@mechanism("kink-band", 5)
def kink_band():
    W, Hc = 16.0, 11.0
    nlines = 22
    X = np.linspace(-W / 2 + 0.35, W / 2 - 0.35, nlines)
    m = np.tan(np.radians(-32))   # band boundaries inclined to the basal planes' normal
    wband = 2.6
    Yc = 0.0

    def mapping(Xm, Ym, delta, bow):
        """Material point -> current point for kink offset delta."""
        s = Ym - (Yc + m * Xm)
        f = np.clip((s + wband / 2) / wband, 0, 1)
        wprime = np.sqrt(max(wband ** 2 - delta ** 2, 1e-6))
        x = Xm + delta * f
        y = np.where(s < -wband / 2, Ym,
                     np.where(s > wband / 2, Ym - (wband - wprime),
                              Yc + m * Xm - wband / 2 + f * wprime))
        # slight elastic bowing before the kink forms
        x = x + bow * np.cos(np.pi * Ym / Hc) * 0.35
        return x, y

    v = Video(
        slug="kink-band",
        title="Kinking",
        captions=[(0.0, 'Compression parallel to the basal planes'),
                  (0.25, 'The planes rotate inside a kink band'),
                  (0.55, 'The band edges are walls of dislocations')],
        xlim=(-15.5, 15.5), ylim=(-10.2, 10.0), seconds=13, orient_cbar=True)

    def draw(ax, t):
        bow = smooth(t, 0.08, 0.25) * (1 - smooth(t, 0.25, 0.5))
        delta = 1.9 * smooth(t, 0.22, 0.85)
        phi = np.arcsin(min(delta / wband, 0.99))
        Ys = np.linspace(-Hc / 2, Hc / 2, 220)
        # outline and band fills
        edge = np.r_[np.c_[np.linspace(-W / 2, W / 2, 60), np.full(60, -Hc / 2)],
                     np.c_[np.full(120, W / 2), np.linspace(-Hc / 2, Hc / 2, 120)],
                     np.c_[np.linspace(W / 2, -W / 2, 60), np.full(60, Hc / 2)],
                     np.c_[np.full(120, -W / 2), np.linspace(Hc / 2, -Hc / 2, 120)]]
        ox, oy = mapping(edge[:, 0], edge[:, 1], delta, bow)
        outline = Polygon(np.c_[ox, oy], closed=True, facecolor=orient_color(0.0), edgecolor=INK, lw=fs.s(0.8), zorder=1)
        ax.add_patch(outline)
        xs = np.linspace(-W / 2, W / 2, 80)
        lo = np.c_[xs, Yc + m * xs - wband / 2 + 1e-3]
        hi = np.c_[xs, Yc + m * xs + wband / 2 - 1e-3]
        inside = lambda p: (np.abs(p[:, 1]) <= Hc / 2)  # noqa: E731
        lo, hi = lo[inside(lo)], hi[inside(hi)]
        if phi > 0.02:
            bx1, by1 = mapping(lo[:, 0], lo[:, 1], delta, bow)
            bx2, by2 = mapping(hi[:, 0], hi[:, 1], delta, bow)
            band = np.r_[np.c_[bx1, by1], np.c_[bx2, by2][::-1]]
            bp = Polygon(band, closed=True, facecolor=orient_color(-phi), edgecolor="none", zorder=1.5)
            ax.add_patch(bp)
            bp.set_clip_path(outline)
            # dislocation walls along band edges
            nwall = int(2 + 7 * delta / 1.9)
            for (bx, by), up in (((bx1, by1), True), ((bx2, by2), False)):
                for k in np.linspace(0.1, 0.9, nwall):
                    i = int(k * (len(bx) - 1))
                    draw_core(ax, bx[i], by[i], size=0.28, up=up, lw=fs.s(1.0), angle=np.pi / 2 - phi)
        segs = []
        for x0 in X:
            x, y = mapping(np.full_like(Ys, x0), Ys, delta, bow)
            segs.append(np.c_[x, y])
        ax.add_collection(LineCollection(segs, colors=INK, linewidths=fs.s(0.6), zorder=3))
        load_arrows(ax, (-W / 2, W / 2, -Hc / 2, Hc / 2), "compress-y", strength=smooth(t, 0, 0.06), size=0.12)
        caxis(ax, -14.6, -1.5, L=1.8, angle=0.0)
        if phi > 0.1:
            readout(ax, 0, -Hc / 2 - 2.6, f"lattice rotation in band {np.degrees(phi):.0f}°")

    return v, draw
