"""Every computed figure in the book, in the book's figure style (``figstyle.py``).

Run from the repository root:

    python _dev/make_book_figures.py            # all figures
    python _dev/make_book_figures.py creep-curve glen-law-curves
    python _dev/make_book_figures.py --list

Needs numpy, scipy and matplotlib. Each figure is written as a PNG into its
chapter's ``figures/`` folder, with no embedded timestamp, so regenerating an
unchanged figure leaves git clean. The deformation-mechanism map and videos
live in ``_dev/deformation_mechanisms/``.

The absorption spectrum is drawn through order-of-magnitude anchor values
after Warren & Brandt (2008). To use the exact compilation, download
IOP_2008_ASCIItable.dat from https://atmos.uw.edu/ice_optical_constants/ into
``_dev/`` and rerun; alpha = 4 pi k / lambda is then computed from it.
"""
import argparse
import os
import sys

import numpy as np

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from numpy.polynomial.hermite import hermval  # noqa: E402
from scipy.integrate import cumulative_trapezoid  # noqa: E402
from scipy.interpolate import PchipInterpolator  # noqa: E402
from scipy.special import erf  # noqa: E402

import figstyle as fs  # noqa: E402
from figstyle import BLACK, BLUE, GREEN, GREY, PURPLE, RED  # noqa: E402

fs.apply_rc()
W = fs.WIDTH
FS = fs.FS
FS_NOTE = 13          # annotation text: the tick size, so labels never outshout the data
FIGS = {}


def figure(name, chapter):
    """Register a figure function that returns a Figure; it is saved to the chapter."""
    def deco(fn):
        FIGS[name] = (chapter, fn)
        return fn
    return deco


def out_path(chapter, name):
    return os.path.join(ROOT, "sections", chapter, "figures", f"{name}.png")


def sig(x):
    return 1 / (1 + np.exp(-x))


def leader(ax, text, xy, xytext, **kw):
    """An annotation with a thin grey leader line."""
    ax.annotate(text, xy, xytext, fontsize=kw.pop("fontsize", FS_NOTE),
                arrowprops=dict(arrowstyle="-", lw=0.8, color="0.4"), **kw)


# -- ice flow ----------------------------------------------------------------------
@figure("glen-law-curves", "ice_flow")
def glen_law_curves():
    fig, ax = plt.subplots(figsize=(W, 0.68 * W))
    t = np.linspace(0, 2, 400)
    ax.plot(t, t, color=BLUE, label="$n=1$ (Newtonian)")
    ax.plot(t, t ** 3, color=RED, label="$n=3$ (Glen)")
    ax.plot([1, 1], [0, 8], color=BLACK, ls="--", label=r"perfectly plastic ($n\to\infty$)")
    ax.plot(1, 1, "o", color=BLACK, zorder=5)
    leader(ax, "normalized\nat $\\tau_0\\approx100$ kPa", (1, 1), (1.18, 1.7))
    ax.set_xlim(0, 2); ax.set_ylim(0, 8)
    ax.set_xlabel(r"deviatoric stress $\tau/\tau_0$")
    ax.set_ylabel(r"strain rate $\dot\varepsilon/\dot\varepsilon_0$")
    ax.legend(loc="upper left")
    fs.grid(ax)
    fs.title_box(ax, "Flow laws through a common point")
    return fig


@figure("creep-curve", "ice_flow")
def creep_curve():
    eps = np.logspace(-3, -1, 800)
    edot = 1.0 + 60 * np.exp(-eps / 0.0018) + 2.0 * sig((eps - 0.03) / 0.005)
    imin = int(np.argmin(edot))
    eps = eps * (0.01 / eps[imin])
    edn = edot / edot[imin]
    plateau = edn[-1]
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(W, 1.05 * W))
    t = cumulative_trapezoid(1 / edot, eps, initial=0)
    t = t / t.max() * 10
    ee = 0.0015
    strain = ee + eps
    a1.plot(t, strain, color=RED)
    a1.plot([0, 0], [0, ee], color=RED)
    a1.annotate("elastic step", (0, ee), (0.2, ee * 0.5), fontsize=FS_NOTE, va="center")
    for frac, lab, dy in [(0.05, "primary", 0.0016), (0.45, "secondary", 0.0016), (0.9, "tertiary", -0.0017)]:
        xi = frac * 10
        yi = ee + np.interp(xi, t, eps)
        a1.annotate(lab, (xi, yi), (xi, yi + dy), fontsize=FS_NOTE, ha="center")
    a1.set_xlim(0, 10); a1.set_ylim(0, strain.max() * 1.08)
    a1.set_xlabel("time"); a1.set_ylabel(r"strain $\varepsilon$")
    a2.loglog(eps, edn, color=BLUE)
    a2.plot(eps[imin], 1.0, "o", color=BLACK, zorder=5)
    leader(a2, "minimum at ~1% strain", (eps[imin], 1.0), (eps[imin] * 1.5, 0.66))
    a2.axhline(plateau, ls=":", color=GREY, lw=1.2)
    a2.annotate(r"tertiary plateau $\approx3\times$ minimum", (1.4e-3, plateau), (1.4e-3, plateau * 1.18),
                fontsize=FS_NOTE)
    a2.annotate("primary", (2e-3, 13), fontsize=FS_NOTE)
    a2.set_xlim(1e-3, 1e-1); a2.set_ylim(0.55, 30)
    a2.set_xlabel(r"strain $\varepsilon$"); a2.set_ylabel(r"strain rate $\dot\varepsilon/\dot\varepsilon_{\min}$")
    for ax, letter, title in ((a1, "A", "Constant-stress creep test"), (a2, "B", "Strain rate against strain")):
        fs.grid(ax)
        fs.panel_letter(ax, letter, x=0.035, y=0.88)
        fs.title_box(ax, title)
    fig.tight_layout(h_pad=2.5)
    return fig


# -- climate -----------------------------------------------------------------------
@figure("response-time-curve", "climate")
def response_time_curve():
    fig, ax = plt.subplots(figsize=(W, 0.6 * W))
    x = np.linspace(0, 4, 400)
    ax.plot(x, 1 - np.exp(-x), color=RED)
    for tt, frac in [(1, 0.63), (2, 0.86)]:
        ax.plot([0, tt, tt], [frac, frac, 0], ls="--", color=GREY, lw=1.2)
        ax.plot(tt, frac, "o", color=BLACK, zorder=5)
        ax.annotate(f"{int(frac * 100)}%", (tt, frac), (tt + 0.08, frac - 0.08), fontsize=FS_NOTE)
    ax.set_xlim(0, 4); ax.set_ylim(0, 1.05); ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_xticklabels(["0", "$t_r$", "$2t_r$", "$3t_r$", "$4t_r$"])
    ax.set_xlabel("time"); ax.set_ylabel(r"length response $L'/L'_{\rm eq}$")
    fs.grid(ax)
    fs.title_box(ax, "Response to a step change in balance")
    return fig


@figure("three-stage-response", "climate")
def three_stage_response():
    fig, ax = plt.subplots(figsize=(W, 0.6 * W))
    x = np.linspace(0, 4, 500)
    s = x * np.sqrt(3)
    ax.plot(x, 1 - np.exp(-x), color=BLUE, label="one-stage (exponential)")
    ax.plot(x, 1 - np.exp(-s) * (1 + s + 0.5 * s ** 2), color=RED, label="three-stage (sigmoidal)")
    ax.set_xlim(0, 4); ax.set_ylim(0, 1.05); ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_xticklabels(["0", r"$\tau$", r"$2\tau$", r"$3\tau$", r"$4\tau$"])
    ax.set_xlabel("time"); ax.set_ylabel(r"length response $L'/L'_{\rm eq}$")
    ax.legend(loc="lower right")
    fs.grid(ax)
    fs.title_box(ax, "Same equilibrium and timescale, different onset")
    return fig


# -- thermomechanics -------------------------------------------------------------------
@figure("seasonal-wave-periods", "thermomechanics")
def seasonal_wave_periods():
    """Damped surface waves T = A exp(-z/z*) sin(wt - z/z*), z* = sqrt(kappa P / pi)."""
    kappa = 35.0              # m^2/yr, thermal diffusivity of ice (1.1e-6 m^2/s)
    A = 10.0                  # °C, surface amplitude
    z = np.linspace(0, 50, 400)
    fig, axes = plt.subplots(1, 3, figsize=(W * 1.2, 0.62 * W), sharey=True)
    for ax, P, letter in zip(axes, (1, 10, 100), "ABC"):
        zs = np.sqrt(kappa * P / np.pi)
        env = A * np.exp(-z / zs)
        for ph in np.linspace(0, 2 * np.pi, 12, endpoint=False):
            ax.plot(env * np.sin(ph - z / zs), z, color=BLACK, lw=0.8, alpha=0.7)
        ax.plot(env, z, color=RED, ls="--")
        ax.plot(-env, z, color=RED, ls="--")
        ax.set_xlim(-11, 11); ax.set_ylim(50, 0)
        ax.set_xlabel("temperature anomaly (°C)")
        fs.grid(ax)
        fs.panel_letter(ax, letter, x=0.08, y=0.95)
        fs.title_box(ax, f"{P} year" + ("" if P == 1 else "s"))
    axes[0].set_ylabel("depth (m)")
    fig.tight_layout(w_pad=1.0)
    return fig


@figure("divide-temperature-profile", "thermomechanics")
def divide_temperature_profile():
    """Robin (1955) steady profile under a divide, with height z above the bed:
    T(z) = T_s + (G/k) l (sqrt(pi)/2) [erf(H/l) - erf(z/l)], l = sqrt(2 kappa H / a)."""
    H, Ts, G, k = 3000.0, -32.0, 0.042, 2.1        # m, °C, W/m^2, W/m/K
    kappa, a = 35.0, 0.10                           # m^2/yr, m/yr
    l = np.sqrt(2 * kappa * H / a)
    z = np.linspace(0, H, 400)
    T = Ts + (G / k) * l * np.sqrt(np.pi) / 2 * (erf(H / l) - erf(z / l))
    Tpmp = -9.8e-8 * 917 * 9.81 * H                 # Clapeyron, 0.098 K/MPa
    fig, ax = plt.subplots(figsize=(0.8 * W, 0.7 * W))
    ax.plot(T, z, color=RED)
    ax.axvline(Tpmp, color=BLUE, ls="--", lw=1.4)
    ax.annotate("pressure-melting\npoint at the bed", (Tpmp, 2200), (Tpmp - 7.5, 2200), fontsize=FS_NOTE,
                va="center", color=BLUE)
    ax.set_xlim(-35, 0); ax.set_ylim(0, H)
    ax.set_xlabel("temperature (°C)"); ax.set_ylabel("height above bed (m)")
    fs.grid(ax)
    fs.title_box(ax, "Temperature beneath an ice divide")
    return fig


# -- cryosphere --------------------------------------------------------------------------
@figure("permafrost-trumpet", "cryosphere")
def permafrost_trumpet():
    fig, ax = plt.subplots(figsize=(0.85 * W, 0.95 * W))
    z = np.linspace(0, 350, 800)
    Ts, G, A0, da = -10.0, 1 / 30, 15.0, 4.0
    mean = Ts + G * z
    amp = A0 * np.exp(-z / da)
    winter, summer = mean - amp, mean + amp
    zal = z[np.argmax(summer < 0)]
    zbase = z[np.argmin(np.abs(mean))]
    ax.fill_betweenx(z, winter, summer, color="0.88")
    ax.plot(winter, z, color=BLUE); ax.plot(summer, z, color=RED); ax.plot(mean, z, color=BLACK, ls="--")
    ax.axvline(0, color=GREY, lw=1.0)
    for zz in (zal, zbase, 16):
        ax.axhline(zz, color=GREY, lw=0.9, ls=":")
    ax.annotate("active layer", (4.5, zal * 0.5), fontsize=FS_NOTE, va="center", ha="center")
    ax.annotate("permafrost top", (4.6, zal + 14), fontsize=FS_NOTE, ha="center")
    ax.annotate("depth of zero\nannual amplitude", (-25, 16), (-25, 44), fontsize=FS_NOTE, va="top")
    ax.annotate(r"base of permafrost ($\approx$300 m)", (0.5, zbase), (-25, zbase - 12), fontsize=FS_NOTE)
    ax.annotate("winter", (winter[150], z[150]), (winter[150] - 7.5, z[150]), color=BLUE, fontsize=FS_NOTE)
    ax.annotate("summer", (summer[110], z[110]), (summer[110] + 0.8, z[110]), color=RED, fontsize=FS_NOTE)
    ax.set_xlim(-26, 8); ax.set_ylim(355, -8)
    ax.set_xlabel("temperature (°C)"); ax.set_ylabel("depth (m)")
    fs.grid(ax)
    fs.title_box(ax, "Trumpet diagram of ground temperature")
    return fig


@figure("brine-volume", "cryosphere")
def brine_volume():
    fig, ax = plt.subplots(figsize=(W, 0.65 * W))
    T = np.linspace(-20, -0.5, 400)
    mliq, ratio = 0.054, 917 / 950
    for Si, c, lab in [(10, RED, "first-year ice, $S_i=10$‰"), (5, BLUE, "multiyear ice, $S_i=5$‰")]:
        ax.plot(T, 100 * ratio * Si / (-T / mliq), color=c, label=lab)
    ax.set_xlim(-20, 0); ax.set_ylim(0, 30)
    ax.set_xlabel("ice temperature (°C)"); ax.set_ylabel("brine volume fraction (%)")
    ax.legend(loc="upper left")
    leader(ax, "brine fraction diverges\ntoward the freezing point", (-3, 22), (-13, 17))
    fs.grid(ax)
    fs.title_box(ax, "Brine volume from the freezing equilibrium")
    return fig


@figure("misi-flux-stability", "cryosphere")
def misi_flux_stability():
    """Schoof (2007) boundary-layer flux on the MISMIP+ centreline bed (Asay-Davis et al. 2016)."""
    secyr = 3.15e7
    rhoi, rhow, gg = 900., 1000., 9.8
    nG, mW, Cf = 3., 1. / 3., 7.624e6
    Ar = 9.8e-26
    betaS = (mW + nG + 3) / (mW + 1)        # 4.75
    thetaF = 1 - rhoi / rhow
    Omega = (Ar * (rhoi * gg) ** (nG + 1) * thetaF ** nG / (4 ** nG * Cf)) ** (1 / (mW + 1))
    acc = 0.5 / secyr

    def bed(xm):
        X = xm / 300e3
        return np.maximum(-150. - 728.8 * X ** 2 + 343.91 * X ** 4 - 50.57 * X ** 6, -720.)

    xk = np.linspace(150, 640, 2200)
    xm = xk * 1e3
    Bm = bed(xm)
    hgm = (rhow / rhoi) * np.maximum(-Bm, 0.0)
    Qg = Omega * hgm ** betaS
    Qkm, supply = Qg * secyr / 1e6, acc * xm * secyr / 1e6
    gQ, dBdx = np.gradient(Qg, xm), np.gradient(Bm, xm)
    cross = [i for i in np.where(np.diff(np.sign(Qg - acc * xm)))[0] if xk[i] > 180]
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(W, 1.0 * W), sharex=True,
                                 gridspec_kw={"height_ratios": [2, 1]})
    a1.plot(xk, Qkm, color=RED, label=r"grounding-line flux $Q_g=\Omega\,h_{\rm g}^{\beta}$, $\beta\approx5$")
    a1.plot(xk, supply, color=BLACK, label=r"accumulation supply $a\,x_g$")
    for i in cross:
        stable = gQ[i] > acc
        a1.plot(xk[i], supply[i], "o", mfc=(BLACK if stable else "white"), mec=BLACK, zorder=5)
        a1.annotate("stable" if stable else "unstable", (xk[i], supply[i]), (xk[i], supply[i] + 0.085),
                    ha="center", fontsize=FS_NOTE, color=(BLACK if stable else RED))
    a1.set_ylim(0, 0.52); a1.set_ylabel(r"flux per unit width (km$^2$ yr$^{-1}$)")
    a1.legend(loc="upper left", bbox_to_anchor=(0.07, 1.0), fontsize=13)
    a2.plot(xk, Bm, color=BLACK)
    a2.fill_between(xk, Bm, Bm.min() - 120, color="0.88")
    a2.axhline(0, color=BLUE, lw=1.0, ls=":")
    retro = (dBdx > 0) & (Bm > -719.)
    a2.fill_between(xk, Bm.min() - 120, 80, where=retro, color=RED, alpha=0.12, lw=0)
    if retro.any():
        a2.annotate("retrograde", (xk[retro].mean(), -330), ha="center", fontsize=FS_NOTE, color=RED)
    for i in cross:
        for ax in (a1, a2):
            ax.axvline(xk[i], color=GREY, lw=0.8, ls=":")
    a2.set_ylim(Bm.min() - 120, 80)
    a2.set_xlabel(r"grounding-line position $x_g$ (km)"); a2.set_ylabel("bed elevation (m)")
    for ax, letter in ((a1, "A"), (a2, "B")):
        fs.grid(ax)
        fs.panel_letter(ax, letter, x=0.035, y=0.88 if ax is a1 else 0.8)
    fs.title_box(a1, "Grounding-line flux against supply (MISMIP+ bed)")
    fig.tight_layout(h_pad=1.0)
    return fig


# -- foundations ---------------------------------------------------------------------------
@figure("ice-attenuation-temperature", "foundations")
def ice_attenuation_temperature():
    """Debye relaxation, alpha = (d_eps / (n c)) w^2 tau / (1 + w^2 tau^2), with an
    Arrhenius tau anchored at 2.2e-5 s at 0 °C and activation energy 0.58 eV (after
    Petrenko & Whitworth ch. 4). Pure ice only."""
    c, n, d_eps = 3.0e8, 1.78, 100.0 - 3.2
    E_over_k, tau273 = 0.58 / 8.617e-5, 2.2e-5
    lam = np.logspace(0, 8, 600)
    omega = 2 * np.pi * c / lam
    fig, ax = plt.subplots(figsize=(W, 0.66 * W))
    for Tc, col in zip([0, -20, -40, -60], fs.SERIES):
        t = tau273 * np.exp(E_over_k * (1.0 / (Tc + 273.15) - 1.0 / 273.15))
        ax.plot(lam, (d_eps / (n * c)) * omega ** 2 * t / (1 + (omega * t) ** 2), color=col,
                label=f"{fs.num(Tc, 'd')} °C")
    ax.axvspan(1, 10, color=GREEN, alpha=0.15)
    ax.text(3.2, 3e-2, "radar\nsounding\nband", ha="center", fontsize=FS_NOTE)
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlim(1, 1e8); ax.set_ylim(1e-7, 2e-1)
    ax.set_xlabel("wavelength (m)"); ax.set_ylabel("absorption coefficient (m$^{-1}$)")
    ax.legend(title="ice temperature", loc="lower left")
    ax2 = ax.secondary_yaxis("right", functions=(lambda a: 4343 * a, lambda d: d / 4343))
    ax2.set_ylabel("attenuation (dB km$^{-1}$)")
    fs.grid(ax)
    fs.title_box(ax, "Radio-band absorption of pure ice")
    return fig


@figure("ice-absorption-spectrum", "foundations")
def ice_absorption_spectrum():
    dat = os.path.join(os.path.dirname(__file__), "IOP_2008_ASCIItable.dat")
    if os.path.exists(dat):
        d = np.loadtxt(dat)
        lam_um, k = d[:, 0], d[:, 2]
        lx, ly = np.log10(lam_um), np.log10(4 * np.pi * k / (lam_um * 1e-6))
    else:
        anchors = [
            (0.12, 1e7), (0.17, 1e6), (0.25, 1e-2), (0.32, 2e-3), (0.40, 6e-4),
            (0.50, 2e-3), (0.60, 6e-2), (0.70, 0.6), (0.80, 2.0), (0.90, 7.0),
            (1.0, 20.0), (1.2, 1e2), (1.5, 2e3), (2.0, 1e4), (2.6, 5e4),
            (3.08, 2e6), (3.6, 3e4), (4.5, 5e4), (6.1, 3e5), (8.0, 8e4),
            (12.0, 3e5), (20.0, 1.2e5), (45.0, 3e5), (100.0, 4e4), (300.0, 2e3),
            (1e3, 60.0), (1e4, 1.5), (1e5, 4e-2), (1e6, 4e-3), (1e7, 1.5e-3),
        ]
        lam, alp = np.array(anchors).T
        f = PchipInterpolator(np.log10(lam), np.log10(alp))
        lx = np.linspace(np.log10(lam[0]), np.log10(lam[-1]), 800)
        ly = f(lx)
    fig, ax = plt.subplots(figsize=(W * 1.05, 0.7 * W))
    ax.plot(10 ** lx, 10 ** ly, color=BLACK)
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlim(1e-1, 1e7); ax.set_ylim(1e-4, 2e8)
    ax.set_xlabel("wavelength (µm)"); ax.set_ylabel("absorption coefficient (m$^{-1}$)")
    ax.axvspan(0.4, 0.7, color=BLUE, alpha=0.15)
    ax.text(0.53, 4e-1, "visible\nwindow", ha="center", fontsize=FS_NOTE)
    ax.axvspan(3e5, 1e7, color=GREEN, alpha=0.15)
    ax.text(1.7e6, 1e5, "radar\nwindow", ha="center", fontsize=FS_NOTE)
    hi, lo = 5e7, 6e6
    for label, xpk, ypk, xt, yt in [("O–H stretch\n3.1 µm", 3.08, 2.6e6, 1.0, hi),
                                    ("bend\n6 µm", 6.1, 4e5, 6.5, lo),
                                    ("libration", 14.0, 4e5, 16.0, hi),
                                    ("lattice\nmodes", 45.0, 4e5, 90.0, lo)]:
        leader(ax, label, (xpk, ypk), (xt, yt), ha="center", va="bottom")
    leader(ax, "electronic\nabsorption (UV)", (0.155, 1e5), (0.105, 6e1))
    leader(ax, "blue minimum", (0.40, 6e-4), (1.6, 2e-4))
    ax2 = ax.secondary_yaxis("right", functions=(lambda a: 1 / np.maximum(a, 1e-30),
                                                 lambda d: 1 / np.maximum(d, 1e-30)))
    ax2.set_ylabel(r"penetration depth $1/\alpha$ (m)")
    fs.grid(ax)
    fs.title_box(ax, "Absorption by pure ice, ultraviolet to radio")
    return fig


@figure("particle-in-a-box-levels", "foundations")
def particle_in_a_box_levels():
    fig, ax = plt.subplots(figsize=(W, 0.85 * W))
    x = np.linspace(0, 1, 400)
    scale = 2.2
    for n in range(1, 5):
        E = n ** 2
        p = scale * np.sin(n * np.pi * x) ** 2
        ax.axhline(E, color=GREY, lw=0.9, ls="--", zorder=1)
        ax.fill_between(x, E, E + p, color=BLUE, alpha=0.3, lw=0)
        ax.plot(x, E + p, color=BLUE)
        ax.text(1.04, E, f"$n={n}$", va="center", fontsize=FS)
    ax.plot([0, 0], [0, 19], color=BLACK, lw=4)
    ax.plot([1, 1], [0, 19], color=BLACK, lw=4)
    ax.plot([-0.08, 1.2], [0, 0], color=BLACK, lw=1.5)
    ax.annotate("", (0.08, 1), (0.08, 0), arrowprops=dict(arrowstyle="<->", lw=1.0))
    ax.text(0.11, 0.45, "zero-point energy $E_1$", fontsize=FS_NOTE, va="center")
    ax.set_xlim(-0.08, 1.2); ax.set_ylim(-0.5, 19)
    ax.set_xticks([0, 1]); ax.set_xticklabels(["0", "$L$"])
    ax.set_yticks([0, 1, 4, 9, 16]); ax.set_yticklabels(["0", "$E_1$", "$4E_1$", "$9E_1$", "$16E_1$"])
    ax.set_xlabel("position"); ax.set_ylabel("energy")
    fs.title_box(ax, "Particle in a box")
    return fig


@figure("oscillator-levels-isotope", "foundations")
def oscillator_levels_isotope():
    from math import factorial
    x = np.linspace(-4.5, 4.5, 600)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(W * 1.25, 0.6 * W))
    a1.plot(x, 0.5 * x ** 2, color=BLACK)
    for v in range(5):
        c = np.zeros(v + 1); c[v] = 1
        psi = hermval(x, c) * np.exp(-x ** 2 / 2) / np.sqrt(2 ** v * factorial(v) * np.sqrt(np.pi))
        E = v + 0.5
        a1.fill_between(x, E, E + 0.75 * psi ** 2 / 0.56, color=BLUE, alpha=0.3, lw=0)
        a1.plot(x, E + 0.75 * psi ** 2 / 0.56, color=BLUE, lw=1.2)
        a1.text(4.0, E + 0.05, f"$v={v}$", fontsize=FS_NOTE, va="bottom")
    a1.annotate("", (-3.4, 1.5), (-3.4, 0.5), arrowprops=dict(arrowstyle="<->", lw=1.0))
    a1.text(-3.3, 1.0, r"$h\nu$", fontsize=FS, va="center")
    a1.annotate("", (-2.6, 0.5), (-2.6, 0.0), arrowprops=dict(arrowstyle="<->", lw=1.0))
    a1.text(-2.5, 0.22, r"$\frac{1}{2}h\nu$", fontsize=FS_NOTE, va="center")
    a1.set_ylim(0, 5.6); a1.set_xlim(-4.5, 4.5)
    a1.set_xlabel("displacement"); a1.set_ylabel(r"energy / $h\nu$")
    ratio = 1 / 1.37
    a2.plot(x, 0.5 * x ** 2, color=BLACK)
    for v in (0, 1):
        for E, col, ls in (((v + 0.5), BLUE, "-"), ((v + 0.5) * ratio, RED, "--")):
            w = np.sqrt(2 * E)
            a2.plot([-w, w], [E, E], color=col, ls=ls)
    a2.text(-4.2, 0.62, "O–H", color=BLUE, fontsize=FS)
    a2.text(-4.2, 0.30, "O–D", color=RED, fontsize=FS)
    a2.annotate("", (2.6, 0.5), (2.6, 0.5 * ratio), arrowprops=dict(arrowstyle="<->", lw=1.0))
    a2.text(2.75, 0.43, r"$\Delta E_0$", fontsize=FS, va="center")
    a2.set_ylim(0, 2.1); a2.set_xlim(-4.5, 4.5)
    a2.set_xlabel("displacement"); a2.set_ylabel(r"energy / $h\nu_{\rm OH}$")
    for ax, letter, title in ((a1, "A", "Levels and probability"), (a2, "B", "One well, two masses")):
        fs.grid(ax)
        fs.panel_letter(ax, letter, x=0.06, y=0.93)
        fs.title_box(ax, title)
    fig.tight_layout(w_pad=2.0)
    return fig


@figure("molecular-energy-ladder", "foundations")
def molecular_energy_ladder():
    fig, ax = plt.subplots(figsize=(0.85 * W, 0.95 * W))
    bands = [("electronic", 7.0, 10.0, PURPLE), ("vibrational", 0.2, 0.45, BLUE),
             ("rotational", 1.2e-3, 7e-3, GREEN), ("radar photons", 4.1e-7, 4.1e-6, GREY)]
    for lab, lo, hi, col in bands:
        ax.fill_between([0.25, 0.75], lo, hi, color=col, alpha=0.45, lw=1.0, edgecolor=col)
        ax.text(0.79, np.sqrt(lo * hi), lab, va="center", fontsize=FS)
    kT = 8.617e-5 * 273.15
    ax.axhline(kT, color=RED, lw=2.0)
    ax.text(0.79, kT * 1.6, r"$k_BT$ at 0 °C", color=RED, fontsize=FS, va="bottom")
    ax.text(0.12, 1.0, "frozen out", rotation=90, va="center", ha="center", fontsize=FS_NOTE)
    ax.text(0.12, 3e-3, "classical", rotation=90, va="center", ha="center", fontsize=FS_NOTE)
    ax.set_yscale("log"); ax.set_ylim(1e-7, 30); ax.set_xlim(0, 1.25)
    ax.set_xticks([])
    ax.set_ylabel("energy quantum (eV)")
    ax.grid(True, axis="y", which="major", alpha=0.3)
    fs.title_box(ax, "Energy levels of the water molecule")
    return fig


# -- driver ----------------------------------------------------------------------------------
def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("names", nargs="*", help="figures to make (default: all)")
    p.add_argument("--list", action="store_true")
    a = p.parse_args()
    if a.list:
        for name, (chapter, _) in FIGS.items():
            print(f"{name:32s} sections/{chapter}/figures/")
        return
    unknown = set(a.names) - set(FIGS)
    if unknown:
        p.error(f"unknown figure(s): {', '.join(sorted(unknown))}")
    for name, (chapter, fn) in FIGS.items():
        if a.names and name not in a.names:
            continue
        fs.save(fn(), out_path(chapter, name))


if __name__ == "__main__":
    main()
