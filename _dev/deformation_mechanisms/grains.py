"""Grain-scale mechanisms in a polycrystal.

Grains are Voronoi cells. Each is filled with a color for its c-axis
orientation (a stand-in for the interference colors of a thin section between
crossed polarizers) and ruled with thin lines that trace its basal planes.
"""
import numpy as np
from matplotlib.collections import EllipseCollection, LineCollection
from matplotlib.patches import Circle, Polygon
from scipy.spatial import Voronoi

import figstyle as fs
from common import (ACCENT, ACCENT2, FAINT, FS, FS_TICK, ICE, INK, MUTED, WATER, Video,
                    arrow, data_letter, load_arrows, readout, mechanism, orient_color, ramp, smooth)
from lattice import draw_core


# -- geometry helpers -----------------------------------------------------
def voronoi_cells(seeds, box):
    """Convex Voronoi cells of `seeds`, clipped exactly to box (x0, x1, y0, y1)."""
    x0, x1, y0, y1 = box
    S = np.asarray(seeds)
    mirrored = [S, np.c_[2 * x0 - S[:, 0], S[:, 1]], np.c_[2 * x1 - S[:, 0], S[:, 1]],
                np.c_[S[:, 0], 2 * y0 - S[:, 1]], np.c_[S[:, 0], 2 * y1 - S[:, 1]]]
    vor = Voronoi(np.vstack(mirrored))
    cells = []
    for i in range(len(S)):
        reg = vor.regions[vor.point_region[i]]
        poly = vor.vertices[reg]
        c = poly.mean(axis=0)
        order = np.argsort(np.arctan2(poly[:, 1] - c[1], poly[:, 0] - c[0]))
        cells.append(poly[order])
    return cells, vor


def voronoi_clipped(seeds, halfplanes):
    """Voronoi cells of seeds clipped to a convex region given as [(n, c), ...] with n.x >= c."""
    S = np.asarray(seeds)
    ring = 200 * np.c_[np.cos(np.linspace(0, 2 * np.pi, 48, endpoint=False)),
                       np.sin(np.linspace(0, 2 * np.pi, 48, endpoint=False))]
    vor = Voronoi(np.vstack([S, ring]))
    cells = []
    for i in range(len(S)):
        reg = vor.regions[vor.point_region[i]]
        poly = vor.vertices[reg]
        c = poly.mean(axis=0)
        poly = poly[np.argsort(np.arctan2(poly[:, 1] - c[1], poly[:, 0] - c[0]))]
        for n, cc in halfplanes:
            if poly is None:
                break
            poly = clip_halfplane(poly, np.asarray(n, float), cc)
        cells.append(poly)
    return cells, vor


def random_seeds(n, box, rng, lloyd=3):
    """Roughly equiaxed seeds: random points relaxed a few Lloyd steps."""
    x0, x1, y0, y1 = box
    S = np.c_[rng.uniform(x0, x1, n), rng.uniform(y0, y1, n)]
    for _ in range(lloyd):
        cells, _ = voronoi_cells(S, box)
        S = np.array([centroid(c) for c in cells])
    return S


def centroid(poly):
    x, y = poly[:, 0], poly[:, 1]
    xs, ys = np.roll(x, -1), np.roll(y, -1)
    cross = x * ys - xs * y
    A = cross.sum() / 2
    if abs(A) < 1e-12:
        return poly.mean(axis=0)
    return np.array([((x + xs) * cross).sum(), ((y + ys) * cross).sum()]) / (6 * A)


def densify(poly, step=0.25):
    """Insert points along each edge so a non-affine map can bend boundaries."""
    out = []
    for a, b in zip(poly, np.roll(poly, -1, axis=0)):
        n = max(int(np.ceil(np.linalg.norm(b - a) / step)), 1)
        out.append(a + (b - a) * np.linspace(0, 1, n, endpoint=False)[:, None])
    return np.vstack(out)


def clip_halfplane(poly, n, c):
    """Keep the part of convex `poly` where n . x >= c (Sutherland-Hodgman)."""
    out = []
    m = len(poly)
    for i in range(m):
        p, q = poly[i], poly[(i + 1) % m]
        dp, dq = p @ n - c, q @ n - c
        if dp >= 0:
            out.append(p)
        if dp * dq < 0:
            out.append(p + (q - p) * dp / (dp - dq))
    return np.array(out) if len(out) >= 3 else None


def segment_in_convex(poly, p0, p1):
    """The part of segment p0-p1 inside convex polygon `poly` (or None)."""
    d = p1 - p0
    lo, hi = 0.0, 1.0
    c = poly.mean(axis=0)
    for a, b in zip(poly, np.roll(poly, -1, axis=0)):
        e = b - a
        nrm = np.array([-e[1], e[0]])
        if nrm @ (c - a) < 0:
            nrm = -nrm
        num, den = nrm @ (p0 - a), nrm @ d
        if abs(den) < 1e-12:
            if num < 0:
                return None
            continue
        s = -num / den
        if den > 0:
            lo = max(lo, s)
        else:
            hi = min(hi, s)
    return (p0 + lo * d, p0 + hi * d) if hi > lo else None


# -- drawing ----------------------------------------------------------------
def draw_grain(ax, poly, theta, traces=True, spacing=0.42, fill=None, edge=INK, lw=fs.s(0.6),
               trace_color="0.3", trace_lw=fs.s(0.3), z=1, alpha=1.0):
    """Fill a grain by orientation and rule its basal-plane traces.

    theta is the c-axis angle from the x-axis; basal traces run perpendicular.
    Returns the patch so callers can clip other artists to it.
    """
    patch = Polygon(poly, closed=True, facecolor=orient_color(theta, alpha) if fill is None else fill,
                    edgecolor=edge, lw=lw, zorder=z, joinstyle="round")
    ax.add_patch(patch)
    if traces:
        c = poly.mean(axis=0)
        R = np.max(np.linalg.norm(poly - c, axis=1))
        cv = np.array([np.cos(theta), np.sin(theta)])
        dv = np.array([-cv[1], cv[0]])
        ks = np.arange(-np.ceil(R / spacing), np.ceil(R / spacing) + 1)
        segs = [np.array([c + k * spacing * cv - R * dv, c + k * spacing * cv + R * dv]) for k in ks]
        lc = LineCollection(segs, colors=trace_color, linewidths=trace_lw, zorder=z + 0.1, alpha=alpha)
        ax.add_collection(lc)
        lc.set_clip_path(patch)
    return patch


def draw_dots(ax, pts, color, r=0.12, edge="none", z=5, alpha=1.0, lw=0.0):
    pts = np.atleast_2d(pts)
    if len(pts) == 0:
        return
    n = len(pts)
    cols = np.tile(np.array(_rgba(color)), (n, 1))
    cols[:, 3] = alpha
    ax.add_collection(EllipseCollection(np.full(n, 2 * r), np.full(n, 2 * r), np.zeros(n), units="xy",
                                        offsets=pts, offset_transform=ax.transData, facecolors=cols,
                                        edgecolors=edge, linewidths=lw, zorder=z))


def _rgba(c):
    from matplotlib.colors import to_rgba
    return to_rgba(c)


def strain_label(ax, x, y, text):
    readout(ax, x, y, text)


# -- 6. dislocation creep in a polycrystal -----------------------------------
@mechanism("dislocation-creep", 6)
def dislocation_creep():
    rng = np.random.default_rng(11)
    box = (-7.5, 7.5, -5.0, 5.0)
    seeds = random_seeds(34, box, rng)
    cells, _ = voronoi_cells(seeds, box)
    dense = [densify(c) for c in cells]
    theta0 = rng.uniform(0, np.pi, len(cells))
    soft = np.abs(np.sin(2 * (theta0 - np.pi / 2)))  # Schmid-like factor for vertical compression
    # A smooth softness field so well-oriented grains strain more than hard ones.
    sig = 1.6

    def softness(P):
        w = np.exp(-((P[:, None, :] - seeds[None]) ** 2).sum(-1) / (2 * sig ** 2))
        return (w * (soft - soft.mean())).sum(1) / w.sum(1)

    s_vertices = [softness(d) for d in dense]
    s_grain = softness(seeds)
    EPS = 0.38
    flashes = [(g, rng.uniform(-3, 3), rng.uniform(0, 1), rng.uniform(0.7, 1.4))
               for g in range(len(cells)) for _ in range(3) if soft[g] > 0.45]

    def mapping(P, s, eps):
        e = eps * (1 + 0.9 * s)
        return np.c_[P[:, 0] * np.exp(e), P[:, 1] * np.exp(-e)]

    v = Video(
        slug="dislocation-creep",
        title="Dislocation creep",
        captions=[(0.0, 'Polycrystal; thin lines trace the basal planes'),
                  (0.07, 'Vertical compression; red marks active basal slip'),
                  (0.55, 'Grains flatten and c-axes rotate toward the compression axis')],
        xlim=(-13.5, 13.5), ylim=(-8.8, 8.8), seconds=15, orient_cbar=True)

    def draw(ax, t):
        eps = EPS * smooth(t, 0.06, 0.95)
        for g, d in enumerate(dense):
            poly = mapping(d, s_vertices[g], eps)
            e = eps * (1 + 0.9 * s_grain[g])
            th = np.arctan2(np.tan(theta0[g]) * np.exp(2 * e), 1.0) % np.pi
            if theta0[g] > np.pi / 2:
                th = np.pi - (np.arctan2(np.tan(np.pi - theta0[g]) * np.exp(2 * e), 1.0) % np.pi)
            patch = draw_grain(ax, poly, th)
            # slip flashes in soft grains
            if 0.07 < t < 0.97:
                c = poly.mean(axis=0)
                cv = np.array([np.cos(th), np.sin(th)])
                dv = np.array([-cv[1], cv[0]])
                segs = []
                for gg, off, ph, sp in flashes:
                    if gg != g:
                        continue
                    u = ((t * 9 * sp + ph) % 1.0) * 6 - 3
                    p = c + off * 0.4 * cv + u * dv
                    segs.append([p - 0.5 * dv, p + 0.5 * dv])
                if segs:
                    lc = LineCollection(segs, colors=ACCENT, linewidths=fs.s(1.1), zorder=2, alpha=0.9)
                    ax.add_collection(lc)
                    lc.set_clip_path(patch)
        W, Hh = 7.5 * np.exp(eps), 5.0 * np.exp(-eps)
        load_arrows(ax, (-W, W, -Hh, Hh), "compress-y", strength=smooth(t, 0, 0.06), size=0.13)
        strain_label(ax, 10.0, 7.6, f"shortening {100 * (1 - np.exp(-eps)):.0f}%")

    return v, draw


# -- 7. fabric development ----------------------------------------------------
@mechanism("fabric-development", 7)
def fabric():
    rng = np.random.default_rng(5)
    box = (-4.2, 4.2, -5.5, 5.5)
    seeds = random_seeds(30, box, rng)
    cells, _ = voronoi_cells(seeds, box)
    n = 500
    c0 = rng.normal(size=(n, 3))
    c0 /= np.linalg.norm(c0, axis=1, keepdims=True)
    cg = rng.normal(size=(len(cells), 3))   # the drawn grains' own c-axes
    cg /= np.linalg.norm(cg, axis=1, keepdims=True)
    EPS = 0.9
    net_c, net_r = np.array([11.8, 0.4]), 4.6

    def rotate(c, eps):
        # Basal-plane normals under uniaxial compression along z: c ∝ F^{-T} c0.
        f = np.array([np.exp(-eps / 2), np.exp(-eps / 2), np.exp(eps)])
        c = c * f
        return c / np.linalg.norm(c, axis=1, keepdims=True)

    v = Video(
        slug="fabric-development",
        title="Fabric development",
        captions=[(0.0, '(A) thin section, (B) c-axes on a Schmidt diagram: a random fabric'),
                  (0.1, 'Vertical compression rotates c-axes toward the vertical'),
                  (0.45, 'A single-maximum fabric develops')],
        xlim=(-8.0, 17.5), ylim=(-8.3, 8.3), seconds=14, orient_cbar=True)

    def draw(ax, t):
        eps = EPS * smooth(t, 0.08, 0.92)
        sx, sy = np.exp(eps / 2), np.exp(-eps)
        cgt = rotate(cg, eps)
        for k, cell in enumerate(cells):
            poly = cell * (sx, sy)
            th = np.arctan2(cgt[k, 2], cgt[k, 0])   # projection on the x-z section
            draw_grain(ax, poly, th, spacing=0.36)
        load_arrows(ax, (-4.2 * sx, 4.2 * sx, -5.5 * sy, 5.5 * sy), "compress-y", strength=smooth(t, 0, 0.06), size=0.10)
        # Schmidt net
        c = rotate(c0, eps)
        c = np.where(c[:, 2:3] > 0, -c, c)
        rho = np.sqrt(np.clip(1 + c[:, 2], 0, 1))
        az = np.arctan2(c[:, 1], c[:, 0])
        pts = net_c + net_r * np.c_[rho * np.cos(az), rho * np.sin(az)]
        ax.add_patch(Circle(net_c, net_r, facecolor="white", edgecolor=INK, lw=fs.s(0.6), zorder=2))
        ax.plot([net_c[0] - net_r, net_c[0] + net_r], [net_c[1]] * 2, color=FAINT, lw=fs.s(0.4), zorder=2)
        ax.plot([net_c[0]] * 2, [net_c[1] - net_r, net_c[1] + net_r], color=FAINT, lw=fs.s(0.4), zorder=2)
        draw_dots(ax, pts, INK, r=0.07, alpha=0.75)
        a1 = np.linalg.eigvalsh(np.einsum("ni,nj->ij", c, c) / len(c)).max()
        data_letter(ax, -7.2, 6.6, "A")
        data_letter(ax, net_c[0] - net_r - 0.2, net_c[1] + net_r - 0.2, "B")
        readout(ax, net_c[0], net_c[1] - net_r - 1.1, f"$a_1$ = {a1:.2f}")
        readout(ax, 0, -7.2, f"vertical strain {100 * (1 - np.exp(-eps)):.0f}%")

    return v, draw


# -- 8. grain-boundary sliding --------------------------------------------------
@mechanism("grain-boundary-sliding", 8)
def gbs():
    a = 2.2
    pts = []
    for j in range(-6, 7):
        for i in range(-8, 9):
            pts.append(((i + 0.5 * (j % 2)) * a, j * a * np.sqrt(3) / 2))
    pts = np.array(pts)
    box0 = (-7.2, 7.2, -7.0, 7.0)
    inside = (pts[:, 0] > box0[0]) & (pts[:, 0] < box0[1]) & (pts[:, 1] > box0[2]) & (pts[:, 1] < box0[3])
    seeds0 = pts[inside]
    rng = np.random.default_rng(2)
    theta = rng.uniform(0, np.pi, len(seeds0))
    cells0, _ = voronoi_cells(seeds0, box0)
    # scribed marker line, cut into one rigid segment per grain
    m0, m1 = np.array([-7.2, -2.6]), np.array([7.2, 3.4])
    marks = [segment_in_convex(c, m0, m1) for c in cells0]
    LAM = np.sqrt(3)

    v = Video(
        slug="grain-boundary-sliding",
        title="Grain-boundary sliding",
        captions=[(0.0, 'Fine-grained ice with a scribed marker line'),
                  (0.06, 'Extension: grains slide (red boundaries) and switch neighbours'),
                  (0.45, 'Grains stay equiaxed; the marker line is offset at boundaries')],
        xlim=(-14.0, 14.0), ylim=(-9.2, 9.2), seconds=15, orient_cbar=True)

    def draw(ax, t):
        f = smooth(t, 0.06, 0.94)
        lam = 1 + (LAM - 1) * f
        lamdot = (LAM - 1)
        S = seeds0 * (lam, 1 / lam)
        box = (box0[0] * lam, box0[1] * lam, box0[2] / lam, box0[3] / lam)
        cells, vor = voronoi_cells(S, box)
        for k, c in enumerate(cells):
            draw_grain(ax, c, theta[k], spacing=0.5, lw=fs.s(0.4), edge=MUTED)
        # boundaries colored by sliding rate (tangential velocity jump)
        L = np.diag([lamdot / lam, -lamdot / lam])
        segs, rates = [], []
        nS = len(S)
        for (p, q), rv in zip(vor.ridge_points, vor.ridge_vertices):
            if p >= nS or q >= nS or -1 in rv:
                continue
            A, B = vor.vertices[rv[0]], vor.vertices[rv[1]]
            tvec = (B - A) / (np.linalg.norm(B - A) + 1e-12)
            dv = L @ (S[p] - S[q])
            segs.append([A, B])
            rates.append(abs(dv @ tvec))
        rates = np.array(rates) / (max(rates) + 1e-9)
        col = np.array([_rgba(INK)] * len(rates))
        hot = np.array(_rgba(ACCENT))
        w = (rates[:, None] * (0.25 < t < 0.97)) if t > 0.06 else 0 * rates[:, None]
        w = 0.8 * w ** 1.5
        col = (1 - w) * col + w * hot
        ax.add_collection(LineCollection(segs, colors=col, linewidths=fs.s(0.6) + fs.s(1.0) * w[:, 0], zorder=3))
        # marker segments ride rigidly with their grain
        msegs = [np.array(mk) - seeds0[k] + S[k] for k, mk in enumerate(marks) if mk is not None]
        ax.add_collection(LineCollection(msegs, colors=ACCENT2, linewidths=fs.s(1.4), zorder=4))
        load_arrows(ax, box, "extend-x", strength=smooth(t, 0, 0.05), size=0.11)
        strain_label(ax, 8.0, 8.4, f"extension {100 * (lam - 1):.0f}%")

    return v, draw


# -- diffusion creep (shared by Nabarro-Herring and Coble) -----------------------
def _diffusion_setup(seed):
    rng = np.random.default_rng(seed)
    box = (-7.0, 7.0, -4.6, 4.6)
    seeds = random_seeds(14, box, rng, lloyd=6)
    cells, _ = voronoi_cells(seeds, box)
    theta = rng.uniform(0, np.pi, len(cells))
    # classify each edge as compressed (normal near vertical) or in tension (near horizontal)
    edges = []
    for g, c in enumerate(cells):
        for a, b in zip(c, np.roll(c, -1, axis=0)):
            e = b - a
            nrm = np.array([-e[1], e[0]]) / (np.linalg.norm(e) + 1e-12)
            on_box = (np.isclose(a[0], b[0]) and abs(abs(a[0]) - 7.0) < 1e-6) or \
                     (np.isclose(a[1], b[1]) and abs(abs(a[1]) - 4.6) < 1e-6)
            edges.append((g, a, b, nrm[1] ** 2, on_box))
    return rng, box, cells, theta, edges


def _pick_edges(edges, g, rng, kind):
    """Random point on an edge of grain g that is compressed ('src') or in tension ('snk')."""
    cand = [(a, b, ny2) for gg, a, b, ny2, _ in edges if gg == g and
            ((ny2 > 0.6) if kind == "src" else (ny2 < 0.4))]
    if not cand:
        return None
    w = np.array([np.linalg.norm(b - a) for a, b, _ in cand])
    a, b, _ = cand[rng.choice(len(cand), p=w / w.sum())]
    return a + rng.uniform(0.15, 0.85) * (b - a)


def _diffusion_video(slug, path_kind):
    rng, box, cells, theta, edges = _diffusion_setup(8)
    EPS = 0.32
    particles = []
    for g, c in enumerate(cells):
        for k in range(26 if path_kind == "lattice" else 12):
            p0, p1 = _pick_edges(edges, g, rng, "src"), _pick_edges(edges, g, rng, "snk")
            if p0 is None or p1 is None:
                continue
            particles.append((g, p0, p1, rng.uniform(0, 1), rng.uniform(0.8, 1.2)))

    def mapf(P, eps):
        return np.asarray(P) * (np.exp(eps), np.exp(-eps))

    def perimeter_path(poly, p0, p1):
        """Shorter way round the boundary of convex poly from p0 to p1."""
        n = len(poly)
        segs = [(poly[i], poly[(i + 1) % n]) for i in range(n)]

        def locate(p):
            best = None
            for i, (a, b) in enumerate(segs):
                e = b - a
                s = np.clip((p - a) @ e / (e @ e), 0, 1)
                d = np.linalg.norm(a + s * e - p)
                if best is None or d < best[0]:
                    best = (d, i, s)
            return best[1], best[2]

        cum = np.r_[0, np.cumsum([np.linalg.norm(b - a) for a, b in segs])]
        P_ = cum[-1]
        i0, s0 = locate(p0)
        i1, s1 = locate(p1)
        L0 = cum[i0] + s0 * (cum[i0 + 1] - cum[i0])
        L1 = cum[i1] + s1 * (cum[i1 + 1] - cum[i1])
        fwd = (L1 - L0) % P_
        return L0, (fwd if fwd <= P_ / 2 else fwd - P_), cum, segs

    def at_arclength(cum, segs, L):
        L = L % cum[-1]
        i = min(np.searchsorted(cum, L, side="right") - 1, len(segs) - 1)
        a, b = segs[i]
        s = (L - cum[i]) / max(cum[i + 1] - cum[i], 1e-12)
        return a + s * (b - a)

    paths = []
    for g, p0, p1, ph, sp in particles:
        if path_kind == "lattice":
            c = centroid(cells[g])
            ctrl = 0.5 * (p0 + p1) + 0.6 * (c - 0.5 * (p0 + p1))
            paths.append(("bez", g, p0, ctrl, p1, ph, sp))
        else:
            paths.append(("per", g, perimeter_path(cells[g], p0, p1), ph, sp))

    nh = path_kind == "lattice"
    v = Video(
        slug=slug,
        title="Nabarro–Herring creep" if nh else "Coble creep",
        captions=([(0.0, 'Compression: red boundaries are squeezed, blue ones are in tension'),
                  (0.08, 'Molecules diffuse through the grain interiors'),
                  (0.6, 'Grains lengthen; their lattices do not rotate')]
                  if nh else
                  [(0.0, 'Compression: red boundaries are squeezed, blue ones are in tension'),
                  (0.08, 'Molecules diffuse along the grain boundaries'),
                  (0.6, 'Same shape change, but rate $\\propto 1/d^{3}$ rather than $1/d^{2}$')]),
        xlim=(-11.0, 11.0), ylim=(-7.2, 7.2), seconds=15, orient_cbar=True)

    def draw(ax, t):
        eps = EPS * smooth(t, 0.06, 0.95)
        for g, c in enumerate(cells):
            draw_grain(ax, mapf(c, eps), theta[g], spacing=0.55)
        # boundary loading colors
        segs, cols, lws = [], [], []
        for g, a, b, ny2, on_box in edges:
            A, B = mapf(a, eps), mapf(b, eps)
            segs.append([A, B])
            if on_box:
                cols.append(_rgba(INK)); lws.append(fs.s(0.8))
            elif ny2 > 0.6:
                cols.append(_rgba(fs.RED)); lws.append(fs.s(1.4))
            elif ny2 < 0.4:
                cols.append(_rgba(fs.BLUE)); lws.append(fs.s(1.4))
            else:
                cols.append(_rgba(INK)); lws.append(fs.s(0.6))
        ax.add_collection(LineCollection(segs, colors=cols, linewidths=lws, zorder=3))
        # moving molecules
        if 0.06 < t < 0.98:
            pos, alph = [], []
            for p in paths:
                ph, sp = p[-2], p[-1]
                s = (t * 7 * sp + ph) % 1.0
                fade = min(1.0, s / 0.12, (1 - s) / 0.12)
                if p[0] == "bez":
                    _, g, p0, ctrl, p1, _, _ = p
                    q = (1 - s) ** 2 * p0 + 2 * s * (1 - s) * ctrl + s ** 2 * p1
                else:
                    _, g, (L0, dL, cum, segs_), _, _ = p
                    q = at_arclength(cum, segs_, L0 + s * dL)
                pos.append(mapf(q, eps))
                alph.append(fade)
            pos = np.array(pos)
            for a_lo in (0.33, 0.66, 1.0):
                m = (np.array(alph) <= a_lo) & (np.array(alph) > a_lo - 0.34)
                draw_dots(ax, pos[m], ACCENT2, r=0.12, alpha=a_lo, z=5)
        W, Hh = 7.0 * np.exp(eps), 4.6 * np.exp(-eps)
        load_arrows(ax, (-W, W, -Hh, Hh), "compress-y", strength=smooth(t, 0, 0.05), size=0.10)

    return v, draw


@mechanism("nabarro-herring-creep", 9)
def nabarro_herring():
    return _diffusion_video("nabarro-herring-creep", "lattice")


@mechanism("coble-creep", 10)
def coble():
    return _diffusion_video("coble-creep", "boundary")


# -- 11. polygonization (rotation recrystallization) --------------------------------
@mechanism("polygonization", 11)
def polygonization():
    rng = np.random.default_rng(4)
    W, Hc = 18.0, 11.0
    walls = np.array([-4.5, 0.0, 4.5])
    nplanes = 16
    Y0 = np.linspace(-Hc / 2 + 0.4, Hc / 2 - 0.4, nplanes)
    kappa0 = 0.030   # initial curvature (exaggerated)
    xs = np.linspace(-W / 2, W / 2, 200)
    edges = np.r_[-W / 2, walls, W / 2]

    def line_y(y0, f, k):
        arc = y0 + 0.5 * k * xs ** 2
        knots = np.r_[-W / 2, walls, W / 2]
        poly = np.interp(xs, knots, y0 + 0.5 * k * knots ** 2)
        return (1 - f) * arc + f * poly

    # dislocations: start scattered, glide along their plane to a wall, then climb into a slot
    ndis = 45
    start = np.c_[rng.uniform(-W / 2 + 0.6, W / 2 - 0.6, ndis), rng.uniform(-Hc / 2 + 0.6, Hc / 2 - 0.6, ndis)]
    target_wall = walls[np.argmin(np.abs(start[:, 0][:, None] - walls[None]), axis=1)]
    slots = np.zeros(ndis)
    for w in walls:
        m = target_wall == w
        slots[m] = np.linspace(-Hc / 2 + 0.6, Hc / 2 - 0.6, m.sum())[np.argsort(np.argsort(start[m, 1]))]
    # late arrivals that increase misorientation
    nlate = 39
    late_start = np.c_[np.where(rng.uniform(size=nlate) < 0.5, -W / 2 + 0.2, W / 2 - 0.2), rng.uniform(-Hc / 2 + 0.6, Hc / 2 - 0.6, nlate)]
    late_wall = walls[rng.integers(0, 3, nlate)]
    late_slot = rng.uniform(-Hc / 2 + 0.5, Hc / 2 - 0.5, nlate)

    v = Video(
        slug="polygonization",
        title="Polygonization",
        captions=[(0.0, 'A bent grain with excess dislocations'),
                  (0.08, 'Dislocations glide and climb into walls'),
                  (0.5, 'Walls divide the grain into sub-grains'),
                  (0.62, 'Misorientation grows until the walls are grain boundaries')],
        xlim=(-14.5, 14.5), ylim=(-9.4, 9.6), seconds=16)

    def draw(ax, t):
        f = smooth(t, 0.10, 0.50)
        k = kappa0 * (1 + 1.6 * smooth(t, 0.58, 0.92))
        # sub-grain fills by mean orientation (exaggerated color contrast)
        for i in range(len(edges) - 1):
            xa, xb = edges[i], edges[i + 1]
            xm = 0.5 * (xa + xb)
            slope_arc = k * np.clip(xs[(xs >= xa) & (xs <= xb)], -W / 2, W / 2)
            slope_poly = k * xm * np.ones_like(slope_arc)
            ang = np.mean((1 - f) * slope_arc + f * slope_poly)
            yb = line_y(-Hc / 2, f, k)
            yt = line_y(Hc / 2, f, k)
            m = (xs >= xa - 1e-9) & (xs <= xb + 1e-9)
            poly = np.r_[np.c_[xs[m], yb[m]], np.c_[xs[m][::-1], yt[m][::-1]]]
            col = orient_color(np.pi / 2 + 7 * ang * f + 1.2)
            ax.add_patch(Polygon(poly, closed=True, facecolor=col, edgecolor=col, lw=1.0, zorder=1))
        segs = [np.c_[xs, line_y(y0, f, k)] for y0 in Y0]
        ax.add_collection(LineCollection(segs, colors=INK, linewidths=fs.s(0.6), zorder=2))
        # grain outline
        yb, yt = line_y(-Hc / 2, f, k), line_y(Hc / 2, f, k)
        outline = np.r_[np.c_[xs, yb], np.c_[xs[::-1], yt[::-1]]]
        ax.add_patch(Polygon(outline, closed=True, facecolor="none", edgecolor=INK, lw=fs.s(0.8), zorder=4))
        # walls: dashed (sub-grain) becoming solid (grain boundary)
        mis = np.degrees(k * (walls[1] - walls[0]))
        solid = smooth(mis, 7.0, 12.0)
        for w in walls:
            y_lo = np.interp(w, xs, yb)
            y_hi = np.interp(w, xs, yt)
            if f > 0.35:
                ax.plot([w, w], [y_lo, y_hi], color=INK, lw=fs.s(0.5) + fs.s(1.0) * solid, ls=(0, (4, 3)) if solid < 0.5 else "-",
                        alpha=smooth(f, 0.35, 0.6), zorder=3)
        # dislocations
        g = smooth(t, 0.08, 0.30)
        c = smooth(t, 0.22, 0.46)
        for i in range(ndis):
            x = start[i, 0] + (target_wall[i] - start[i, 0]) * g
            y = start[i, 1] + (slots[i] - start[i, 1]) * c
            yy = y + np.interp(x, xs, line_y(0, f, k))
            ang = np.interp(x, xs, k * xs) * (1 - f) + f * k * x * 0
            draw_core(ax, x, yy, size=0.28, lw=fs.s(0.9), angle=ang)
        for i in range(nlate):
            a0 = 0.58 + 0.30 * i / nlate
            gg = smooth(t, a0, a0 + 0.10)
            if gg <= 0:
                continue
            x = late_start[i, 0] + (late_wall[i] - late_start[i, 0]) * gg
            yy = late_slot[i] + np.interp(x, xs, line_y(0, f, k))
            draw_core(ax, x, yy, size=0.28, lw=fs.s(0.9), color=ACCENT2 if gg < 1 else ACCENT)
        if f > 0.4:
            readout(ax, 0, -Hc / 2 - 2.4, f"misorientation across each wall {mis:.1f}°")

    return v, draw


# -- 15. premelting and liquid veins ---------------------------------------------
@mechanism("premelting", 15)
def premelting():
    rng = np.random.default_rng(21)
    box0 = (-7.0, 7.0, -5.0, 5.0)
    seeds0 = random_seeds(30, box0, rng)
    theta = rng.uniform(0, np.pi, len(seeds0))
    cells0, _ = voronoi_cells(seeds0, box0)
    m0, m1 = np.array([-7.0, -4.0]), np.array([7.0, 4.2])
    marks = [segment_in_convex(c, m0, m1) for c in cells0]

    v = Video(
        slug="premelting",
        title="Premelting and intergranular water",
        captions=[(0.0, 'Cold ice: dry grain boundaries'),
                  (0.08, 'Warming: water films and veins form'),
                  (0.45, 'Shear: the wet boundaries slide easily')],
        xlim=(-12.5, 12.5), ylim=(-8.2, 8.2), seconds=15, orient_cbar=True)

    def draw(ax, t):
        T = -25 + 24.9 * smooth(t, 0.06, 0.42)
        wet = smooth(t, 0.06, 0.44)
        gam = 0.65 * smooth(t, 0.46, 0.97)
        S = seeds0 + np.c_[gam * seeds0[:, 1], np.zeros(len(seeds0))]
        x0, x1, y0, y1 = box0
        # sheared sample is a parallelogram; grains ride rigidly with their seeds and
        # the boundaries re-form between them, so neighbors can switch
        k_ = 1 / np.hypot(1, gam)
        region = [((0, 1), y0), ((0, -1), -y1), ((k_, -gam * k_), x0 * k_), ((-k_, gam * k_), -x1 * k_)]
        cells, vor = voronoi_clipped(S, region)
        edge_col = tuple(np.array(_rgba(INK)) * (1 - wet) + np.array(_rgba(WATER)) * wet)
        for k, c in enumerate(cells):
            if c is not None:
                draw_grain(ax, c, theta[k], spacing=0.45, lw=fs.s(0.5) + fs.s(1.6) * wet, edge=edge_col)
        # veins at triple junctions
        if wet > 0.25:
            V = vor.vertices
            ok = np.ones(len(V), bool)
            for n, cc in region:
                ok &= (V @ np.asarray(n, float)) > cc + 0.15
            r = 0.24 * smooth(wet, 0.25, 1.0)
            ang = np.pi / 2 + 2 * np.pi * np.arange(3) / 3
            for p in V[ok]:
                tri = p + r * np.c_[np.cos(ang), np.sin(ang)]
                ax.add_patch(Polygon(tri, closed=True, facecolor=WATER, edgecolor="none", zorder=4))
        # rigid marker pieces ride with their grains
        msegs = [np.array(mk) + (gam * seeds0[k, 1], 0) for k, mk in enumerate(marks) if mk is not None]
        if t > 0.40:
            ax.add_collection(LineCollection(msegs, colors=ACCENT2, linewidths=fs.s(1.4), zorder=5,
                                             alpha=smooth(t, 0.40, 0.46)))
        load_arrows(ax, (x0, x1, y0, y1), "shear", strength=smooth(t, 0.44, 0.50), size=0.12)
        readout(ax, x0 - 2.0, y1 + 2.2, f"$T$ = {fs.num(round(T, 1), '.1f')} °C")
        if t > 0.5:
            readout(ax, x1 + 1.5, y1 + 2.2, f"strain rate ×{1 + 2 * smooth(t, 0.5, 0.75):.1f} vs dry ice")

    return v, draw


# -- 16. brittle fracture ----------------------------------------------------------
@mechanism("brittle-fracture", 16)
def brittle():
    rng = np.random.default_rng(9)
    box = (-6.0, 6.0, -5.0, 5.0)
    seeds = random_seeds(46, box, rng)
    cells, vor = voronoi_cells(seeds, box)
    theta = rng.uniform(0, np.pi, len(cells))
    nS = len(seeds)
    cracks = []
    for (p, q), rv in zip(vor.ridge_points, vor.ridge_vertices):
        if p >= nS or q >= nS or -1 in rv:
            continue
        A, B = vor.vertices[rv[0]], vor.vertices[rv[1]]
        if not (np.all(np.abs(A) < [5.8, 4.8]) and np.all(np.abs(B) < [5.8, 4.8])):
            continue
        ang = np.degrees(np.arctan2(*(B - A)[::-1])) % 180
        if 20 < ang < 70 or 110 < ang < 160:
            cracks.append((A, B, ang))
    # cracks closer to the eventual fault line appear first
    fault_n = np.array([-np.sin(np.radians(58)), np.cos(np.radians(58))])
    dist = np.array([abs((0.5 * (A + B)) @ fault_n) for A, B, _ in cracks])
    order = np.argsort(dist + rng.uniform(0, 2.5, len(cracks)))
    cracks = [cracks[i] for i in order[:24]]
    birth = np.sort(rng.uniform(0.18, 0.72, len(cracks)))
    fault_dir = np.array([np.cos(np.radians(58)), np.sin(np.radians(58))])

    v = Video(
        slug="brittle-fracture",
        title="Brittle failure",
        captions=[(0.0, 'Rapid compression'),
                  (0.16, 'Inclined boundaries crack'),
                  (0.36, 'Wing cracks grow parallel to the load'),
                  (0.8, 'Cracks link into a fault')],
        xlim=(-12.5, 12.5), ylim=(-8.2, 8.2), seconds=14, orient_cbar=True)

    def above(P):
        return (np.atleast_2d(P) @ fault_n) > 0

    def draw(ax, t):
        slip = 1.4 * smooth(t, 0.80, 0.98)
        shift = slip * fault_dir
        sq = 0.03 * smooth(t, 0.05, 0.78)
        scale = np.array([1 + 0.5 * sq, 1 - sq])
        for k, c in enumerate(cells):
            for sgn in (+1, -1):
                piece = clip_halfplane(c, sgn * fault_n, 0.0)
                if piece is None:
                    continue
                P = piece * scale + (shift if sgn > 0 else 0)
                draw_grain(ax, P, theta[k], spacing=0.42, lw=fs.s(0.4), edge=MUTED)
        for (A, B, ang), tb in zip(cracks, birth):
            g = smooth(t, tb, tb + 0.05)
            if g <= 0:
                continue
            mid = 0.5 * (A + B)
            off = shift if above(mid)[0] else 0
            a = mid + (A - mid) * g
            b = mid + (B - mid) * g
            ax.plot(*np.c_[a, b] * scale[:, None] + np.array(off).reshape(-1, 1) * 1, color=INK, lw=fs.s(1.4),
                    zorder=4, solid_capstyle="round")
            # wing cracks curve toward the compression axis from both tips
            w = 1.2 * smooth(t, tb + 0.05, tb + 0.28)
            if w > 0:
                for tip in (A, B):
                    sgn = 1 if tip[1] > mid[1] else -1
                    s = np.linspace(0, 1, 12)
                    pts = tip + np.c_[0.25 * w * s * np.sign(tip[0] - mid[0]), sgn * w * s ** 0.8]
                    pts = pts * scale + (shift if above(tip)[0] else 0)
                    ax.plot(pts[:, 0], pts[:, 1], color=INK, lw=fs.s(0.8), zorder=4)
        if t > 0.74:
            rect = np.array([[-6, -5.0], [6, -5.0], [6, 5.0], [-6, 5.0]]) * scale
            seg = segment_in_convex(rect, -12 * fault_dir, 12 * fault_dir)
            if seg is not None:
                for off in (0, shift):
                    fl = np.array(seg) + off
                    ax.plot(fl[:, 0], fl[:, 1], color=ACCENT, lw=fs.s(1.4) * smooth(t, 0.74, 0.82), zorder=5)
        load_arrows(ax, (-6, 6, -5.0, 5.0), "compress-y", strength=smooth(t, 0, 0.05), size=0.10)

    return v, draw
