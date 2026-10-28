"""Fabric development after Alley (1988), "Fabrics in polar ice sheets:
development and prediction", Science 240, 493-495.

Alley's model: in a polycrystal each grain strains in proportion to its
geometric (Schmid) factor S, the resolved shear stress on its basal plane
relative to the applied stress (S = cos(phi) sin(phi) for uniaxial stress at
angle phi to the c-axis), and the strain averaged over all grains equals the
bulk strain. The c-axis of a grain that slips on its basal plane rotates as a
material plane normal, toward compression axes and away from tension axes.
S-bar, the mean of S over the grains, is the "geometric softness" of the
aggregate.

Here that becomes, for each grain and bulk velocity gradient L = D + W,

    L_g = (S_g / S-bar) D + W,      dc/dt = -L_g^T c + (c . L_g^T c) c,

with S_g = |D c - (c.Dc) c| / (sqrt(3/2) |D|), which equals cos(phi) sin(phi)
under uniaxial stress. Two animations:

* ``alley-flow-regimes``: his Fig. 1B-D and Fig. 2, divergent, parallel and
  convergent flow, with the geometric softness against strain.
* ``alley-ice-column``: a parcel descending through a column like Byrd
  Station, linking each depth to the mechanism that controls the fabric there.
"""
import numpy as np
from matplotlib.collections import EllipseCollection
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm, ListedColormap, to_rgba
from matplotlib.patches import Circle, Rectangle

import figstyle as fs
from common import FS, FS_TICK, INK, Video, mechanism, readout, smooth

N_GRAINS = 400
KAPPA = 25.0                   # width of the axial kernel used to contour the nets
MUD_LEVELS = np.arange(0, 11, 1.0)   # multiples of uniform density, 10 bands


# -- the model -------------------------------------------------------------------
def random_axes(n, rng):
    c = rng.normal(size=(n, 3))
    return c / np.linalg.norm(c, axis=1, keepdims=True)


def schmid(c, D):
    """Geometric factor of each grain: resolved basal shear over applied stress
    (cos(phi) sin(phi) under uniaxial stress)."""
    Dc = c @ D.T
    t = Dc - np.sum(c * Dc, axis=1, keepdims=True) * c
    return np.linalg.norm(t, axis=1) / (np.sqrt(1.5) * np.linalg.norm(D))


def _turn(c, e, dphi):
    """Rotate each c-axis by dphi in the plane holding it and axis e (away from e if dphi > 0)."""
    ce = c @ e
    sgn = np.where(ce < 0, -1.0, 1.0)[:, None]
    e2 = sgn * e                                  # the end of the axis nearer each c
    cosp = np.clip(np.abs(ce), 0, 1)
    phi = np.arccos(cosp)
    p = c - cosp[:, None] * e2
    pn = np.linalg.norm(p, axis=1, keepdims=True)
    p = np.where(pn > 1e-12, p / np.maximum(pn, 1e-12), 0.0)
    new = np.clip(phi + dphi, 0, np.pi / 2)
    out = np.cos(new)[:, None] * e2 + np.sin(new)[:, None] * p
    return np.where(pn > 1e-12, out, c)


def uniaxial(c, e, de):
    """Alley's rotation for an increment of uniaxial strain de along axis e:
    compression (de < 0): dphi = de sin^2(phi) / S-bar, toward the axis;
    tension (de > 0): dphi = de cos^2(phi) / (S-bar + S de), away from it."""
    cosp = np.clip(np.abs(c @ e), 0, 1)
    sinp = np.sqrt(1 - cosp ** 2)
    S = cosp * sinp
    Sbar = S.mean()
    if de < 0:
        dphi = de * sinp ** 2 / Sbar
    else:
        dphi = de * cosp ** 2 / (Sbar + S * de)
    return _turn(c, e, dphi)


def rotate(c, parts, spin, dt):
    """One increment. ``parts`` are (axis, rate) uniaxial components (rate < 0 for
    compression); ``spin`` is a rigid-body rotation rate about the y axis."""
    for e, rate in parts:
        c = uniaxial(c, np.asarray(e, float), rate * dt)
    if spin:
        a = spin * dt
        R = np.array([[np.cos(a), 0, np.sin(a)], [0, 1, 0], [-np.sin(a), 0, np.cos(a)]])
        c = c @ R.T
    return c


def integrate(c0, parts, spin, D, total, steps):
    """Fabric and geometric softness S-bar (for stress D) at each of ``steps`` increments."""
    cs, sb = [c0], [schmid(c0, D).mean()]
    c = c0
    for _ in range(steps):
        c = rotate(c, parts, spin, total / steps)
        cs.append(c)
        sb.append(schmid(c, D).mean())
    return np.array(cs), np.array(sb)


X, Y, Z = (1, 0, 0), (0, 1, 0), (0, 0, 1)
S2 = 1 / np.sqrt(2)


# -- Schmidt net ----------------------------------------------------------------------
def project(c):
    """Lower-hemisphere equal-area projection, vertical at the centre, x = flow direction."""
    c = np.where(c[:, 2:3] > 0, -c, c)
    r = np.sqrt(np.clip(1 + c[:, 2], 0, 1))
    az = np.arctan2(c[:, 1], c[:, 0])
    return np.c_[r * np.cos(az), r * np.sin(az)]


_G = 70
_gx, _gy = np.meshgrid(np.linspace(-1, 1, _G), np.linspace(-1, 1, _G))
_inside = _gx ** 2 + _gy ** 2 <= 1
_rho = np.sqrt(_gx ** 2 + _gy ** 2)
_az = np.arctan2(_gy, _gx)
_cz = -(1 - np.clip(_rho, 0, 1) ** 2)                 # invert the projection
_sz = np.sqrt(np.clip(1 - _cz ** 2, 0, 1))
GRID_C = np.stack([_sz * np.cos(_az), _sz * np.sin(_az), _cz], -1)[_inside]
_u = random_axes(20000, np.random.default_rng(0))
_UNIFORM = np.mean(np.exp(KAPPA * (_u[:, 2] ** 2 - 1)))   # kernel mean for a uniform fabric


def density(c):
    """Axial-kernel density on the net, in multiples of uniform density."""
    d = np.exp(KAPPA * ((GRID_C @ c.T) ** 2 - 1)).mean(axis=1) / _UNIFORM
    out = np.full(_gx.shape, np.nan)
    out[_inside] = d
    return out


MUD_CMAP = ListedColormap(np.array([plt.get_cmap("Blues")(0.08 + 0.84 * i / 9) for i in range(10)]))
MUD_NORM = BoundaryNorm(MUD_LEVELS, 10)


def draw_net(ax, c, x0=0.0, y0=0.0, R=1.0, highlight=None):
    ax.contourf(x0 + R * _gx, y0 + R * _gy, np.minimum(density(c), MUD_LEVELS[-1] - 1e-6),
                levels=MUD_LEVELS, cmap=MUD_CMAP, norm=MUD_NORM, zorder=1)
    p = project(c)
    n = len(p)
    col = np.tile(np.array(to_rgba(INK)), (n, 1))
    if highlight is not None:
        col[highlight] = to_rgba(fs.RED)
    ax.add_collection(EllipseCollection(np.full(n, 0.022 * R), np.full(n, 0.022 * R), np.zeros(n),
                                        units="xy", offsets=np.c_[x0, y0] + R * p,
                                        offset_transform=ax.transData, facecolors=col, zorder=3))
    ax.add_patch(Circle((x0, y0), R, facecolor="none", edgecolor=INK, lw=1.4, zorder=4))
    for s in (-1, 1):
        ax.plot([x0, x0 + s * R * 0.06], [y0, y0], color=INK, lw=1.0, zorder=4)
        ax.plot([x0, x0], [y0, y0 + s * R * 0.06], color=INK, lw=1.0, zorder=4)


def mud_colorbar(fig, rect):
    cax = fig.add_axes(rect)
    sm = plt.cm.ScalarMappable(norm=MUD_NORM, cmap=MUD_CMAP)
    cb = fig.colorbar(sm, cax=cax)
    cb.set_label("multiples of uniform density", rotation=90, fontsize=fs.FS_LABEL, labelpad=10)
    cb.ax.tick_params(labelsize=fs.FS_CBAR_TICK)
    cb.set_ticks([0, 2, 4, 6, 8, 10])


# -- Fig. 1 and 2: three flow regimes -------------------------------------------------------
REGIMES = [
    # title, sites, uniaxial parts (axis, rate), stress D for S-bar, total strain.
    # x = flow, y = transverse, z = vertical. Pure shear is uniaxial compression
    # plus an equal uniaxial tension on an orthogonal axis (Alley's note 4).
    # Strains as in his Fig. 1: B to unit length 0.5, C to 0.55 by 1.85, D to length 2.
    ("Divergent flow", "Dome C, Byrd, Dye 3", [(Z, -1.0)], np.diag([0.5, 0.5, -1.0]), 0.5),
    ("Parallel flow", "Byrd, Dye 3", [(Z, -0.5), (X, 0.5)], np.diag([1.0, 0.0, -1.0]), 0.9),
    ("Convergent flow", "Mizuho, Vostok", [(X, 1.0)], np.diag([1.0, -0.5, -0.5]), 1.0),
]
STRAIN_LABEL = ["vertical shortening", "vertical shortening", "longitudinal extension"]


@mechanism("alley-flow-regimes", 17)
def flow_regimes():
    steps = 240
    c0 = random_axes(N_GRAINS, np.random.default_rng(1988))
    runs = [integrate(c0, parts, 0.0, D, tot, steps) for _, _, parts, D, tot in REGIMES]

    panels = [dict(rect=[0.03 + 0.25 * i, 0.47, 0.22, 0.38], kind="field", xlim=(-1.25, 1.25),
                   ylim=(-1.25, 1.25), letter="ABC"[i], letter_at=(0.08, 0.95), title=REGIMES[i][0])
              for i in range(3)]
    panels.append(dict(rect=[0.12, 0.155, 0.62, 0.22], kind="plot", letter="D", letter_at=(0.03, 0.82)))
    v = Video(
        slug="alley-flow-regimes",
        title="Fabrics in polar ice sheets (Alley, 1988)",
        captions=[(0.0, "Random c-axes, one set of grains under three flow patterns"),
                  (0.08, "Basal glide rotates c-axes toward compression and away from extension"),
                  (0.45, "(A) a vertical single maximum; (B) an elongated cluster; (C) a vertical girdle across flow"),
                  (0.75, "(D) geometric softness rises at small strain, then falls as the fabric tightens")],
        panels=panels, seconds=16)

    def draw(axs, t):
        k = int(round(smooth(t, 0.06, 0.94) * steps))
        for i, ax in enumerate(axs[:3]):
            draw_net(ax, runs[i][0][k])
            ax.text(0, -1.2, REGIMES[i][1], ha="center", va="top", fontsize=FS_TICK)
            # tension axes as arrows on the net rim (horizontal x = flow, y = transverse)
            D = REGIMES[i][3]
            for j, (dx, dy) in enumerate(((1, 0), (0, 1))):
                if D[j, j] > 0:
                    for s in (-1, 1):
                        ax.annotate("", (s * 1.2 * dx, s * 1.2 * dy), (s * 1.02 * dx, s * 1.02 * dy),
                                    arrowprops=dict(arrowstyle="-|>", lw=1.6, color=INK))
        bx = axs[3]
        for i, (run, col) in enumerate(zip(runs, fs.SERIES)):
            frac = np.linspace(0, 1, steps + 1)
            bx.plot(frac, run[1], color=col, alpha=0.25)
            bx.plot(frac[:k + 1], run[1][:k + 1], color=col, label=REGIMES[i][0].lower())
            bx.plot(frac[k], run[1][k], fs.MARKERS[i], color=col, mec=INK, zorder=5)
        bx.set_xlim(0, 1); bx.set_ylim(0.2, 0.5)
        bx.set_xlabel("fraction of the strain in (A)–(C)")
        bx.set_ylabel(r"$\bar{S}$")
        bx.legend(loc="center left", bbox_to_anchor=(1.01, 0.5), fontsize=13)
        fs.grid(bx)

    v.extra = lambda fig: mud_colorbar(fig, [0.80, 0.50, 0.012, 0.32])
    return v, draw


# -- a column like Byrd Station ------------------------------------------------------------
H = 2164.0                      # m, Byrd Station
ZONES = [  # top, bottom (m), label, fill
    (0, 150, "firn: random fabric", "#f2f2f2"),
    (150, 1200, "cold ice: rotation by basal glide", "#e3eefa"),
    (1200, 1800, "basal shear: single maximum", "#fbe3e3"),
    (1800, H, "warm ice: recrystallization", "#fff3d6"),
]
MECH = [  # depth, mechanisms (the videos in this chapter)
    (0, "grain growth"),
    (150, "basal glide, lattice rotation"),
    (700, "lattice rotation, polygonization"),
    (1200, "simple shear, lattice rotation"),
    (1800, "migration recrystallization, nucleation"),
]


def column_temperature(z):
    """A smooth profile from -28 °C at the surface to -1.6 °C (melting) at the bed."""
    return -28 + 26.4 * (z / H) ** 3


@mechanism("alley-ice-column", 18)
def ice_column():
    rng = np.random.default_rng(7)
    c0 = random_axes(N_GRAINS, rng)
    # 1. divergent flow (vertical compression) through the cold upper ice
    n1, n2 = 180, 180
    run1, _ = integrate(c0, [(Z, -1.0)], 0.0, np.diag([0.5, 0.5, -1.0]), 0.5, n1)
    # 2. bed-parallel simple shear u_x = g z: a pure shear with compression along
    #    (x - z)/sqrt2 and tension along (x + z)/sqrt2, each of rate g/2, plus a
    #    rigid-body rotation at rate g/2 (Alley's simple shear)
    L = np.zeros((3, 3)); L[0, 2] = 1.0
    D = 0.5 * (L + L.T)
    parts = [((S2, 0, -S2), -0.5), ((S2, 0, S2), 0.5)]
    run2, _ = integrate(run1[-1], parts, 0.5, D, 3.0, n2)
    # 3. migration recrystallization: grains replaced by new ones in a small-circle
    #    girdle about 25-30° from vertical, gathered into a few maxima
    order = rng.permutation(N_GRAINS)
    az0 = rng.uniform(0, 2 * np.pi)
    maxima = az0 + np.arange(4) * np.pi / 2 + rng.normal(0, 0.15, 4)
    colat = np.radians(rng.normal(27, 4, N_GRAINS))
    az = maxima[rng.integers(0, 4, N_GRAINS)] + rng.normal(0, 0.18, N_GRAINS)
    new = np.c_[np.sin(colat) * np.cos(az), np.sin(colat) * np.sin(az), -np.cos(colat)]
    Dshear = D

    def state(z):
        if z < 150:
            return c0, None
        if z < 1200:
            return run1[int(round((z - 150) / 1050 * n1))], None
        if z < 1800:
            return run2[int(round((z - 1200) / 600 * n2))], None
        f = (z - 1800) / (H - 1800)
        m = int(round(0.92 * f * N_GRAINS))
        c = run2[-1].copy()
        c[order[:m]] = new[order[:m]]
        return c, order[:m]

    zs = np.linspace(0, H, 300)
    sbar = np.array([schmid(state(z)[0], Dshear).mean() for z in zs])
    sbar_rel = sbar / schmid(c0, Dshear).mean()

    panels = [dict(rect=[0.08, 0.09, 0.28, 0.79], kind="plot", letter="A", letter_at=(0.92, 0.97)),
              dict(rect=[0.38, 0.28, 0.30, 0.53], kind="field", xlim=(-1.25, 1.25), ylim=(-1.25, 1.25),
                   letter="B", letter_at=(0.06, 0.95)),
              dict(rect=[0.84, 0.17, 0.13, 0.66], kind="plot", letter="C", letter_at=(0.2, 0.97))]
    v = Video(
        slug="alley-ice-column",
        title="Fabric with depth in an ice sheet (after Alley, 1988)",
        captions=[(0.0, "Near the surface the c-axes are randomly oriented"),
                  (0.10, "Cold upper ice: vertical compression rotates c-axes toward the vertical by basal glide"),
                  (0.40, "Grains stop growing as polygonization subdivides them; rotation still controls the fabric"),
                  (0.55, "Near the bed, basal shear exceeds the normal stresses: a tight single maximum forms"),
                  (0.80, "Warm basal ice: migration recrystallization makes coarse grains in a multiple-maximum girdle")],
        panels=panels, seconds=18)

    def draw(axs, t):
        ax, nx, cx = axs
        z = H * smooth(t, 0.05, 0.95)
        # (A) the column
        for top, bot, lab, fill in ZONES:
            ax.add_patch(Rectangle((0, top), 1, bot - top, facecolor=fill, edgecolor=INK, lw=0.8))
            ax.text(0.04, 0.5 * (top + bot), lab, fontsize=FS_TICK - 1, va="center")
        ax.plot([0.94], [z], "o", color=fs.RED, mec=INK, ms=11, zorder=5)
        ax.set_xlim(0, 1); ax.set_ylim(H, 0); ax.set_xticks([])
        ax.set_ylabel("depth (m)")
        # (B) the fabric of the descending parcel
        c, new_idx = state(z)
        draw_net(nx, c, highlight=new_idx)
        mech = [m for d, m in MECH if z >= d][-1]
        readout(nx, 0, 1.42, mech)
        readout(nx, -0.62, -1.48, f"depth {z:,.0f} m")
        readout(nx, 0.72, -1.48, f"$T$ = {fs.num(round(column_temperature(z), 1), '.1f')} °C")
        # (C) geometric softness for bed-parallel shear, relative to random
        k = int(np.searchsorted(zs, z))
        cx.plot(sbar_rel, zs, color=fs.RED, alpha=0.25)
        cx.plot(sbar_rel[:k + 1], zs[:k + 1], color=fs.RED)
        cx.plot(sbar_rel[min(k, len(zs) - 1)], zs[min(k, len(zs) - 1)], "o", color=fs.RED, mec=INK, zorder=5)
        cx.set_ylim(H, 0); cx.set_xlim(0.8, 1.6)
        cx.set_xlabel(r"$\bar S / \bar S_{\rm random}$")
        cx.set_yticklabels([])
        fs.grid(cx)

    v.extra = lambda fig: mud_colorbar(fig, [0.715, 0.30, 0.012, 0.48])
    return v, draw
