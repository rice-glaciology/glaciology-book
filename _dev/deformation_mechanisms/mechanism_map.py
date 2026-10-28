"""Deformation-mechanism map for ice from the Goldsby and Kohlstedt (2001) composite law.

Run from the repo root:  python _dev/deformation_mechanisms/mechanism_map.py
Writes sections/ice_flow/figures/deformation-mechanism-map.png.

For each stress and grain size the total strain rate is

    e = e_diff + (1/e_basal + 1/e_gbs)^-1 + e_disl

and the field is labelled by the largest contribution (for the bracketed
series pair, by the slower, rate-limiting member). Dislocation-creep, basal-
slip and GBS parameters are those tabulated by Goldsby and Kohlstedt (2001).
Diffusion-creep parameters are approximate (lattice and boundary
self-diffusion of ice as compiled by Frost and Ashby, 1982), so the position
of the diffusion field is indicative only.
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import ACCENT, FIG_DIR, INK, MUTED, PAPER  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.colors import ListedColormap  # noqa: E402

R = 8.314


def rates(sig_mpa, d_m, T):
    """Strain rates (1/s) of each mechanism at stress (MPa), grain size (m), temperature (K)."""
    if T < 258:
        disl = 4.0e5 * sig_mpa ** 4.0 * np.exp(-60e3 / (R * T))
    else:
        disl = 6.0e28 * sig_mpa ** 4.0 * np.exp(-181e3 / (R * T))
    basal = 5.5e7 * sig_mpa ** 2.4 * np.exp(-60e3 / (R * T))
    if T < 255:
        gbs = 3.9e-3 * sig_mpa ** 1.8 * d_m ** -1.4 * np.exp(-49e3 / (R * T))
    else:
        gbs = 3.0e26 * sig_mpa ** 1.8 * d_m ** -1.4 * np.exp(-192e3 / (R * T))
    Vm = 1.97e-5                                   # molar volume, m^3/mol
    Dv = 9.1e-4 * np.exp(-59.4e3 / (R * T))        # lattice diffusivity, m^2/s
    dDb = 5.8e-13 * np.exp(-49e3 / (R * T))        # boundary width x diffusivity, m^3/s
    diff = 42 * Vm * (sig_mpa * 1e6) / (R * T * d_m ** 2) * (Dv + np.pi * dDb / d_m)
    return dict(diff=diff, basal=basal, gbs=gbs, disl=disl)


def main(T=263.15):
    s = np.logspace(-3, 1, 400)       # MPa
    d = np.logspace(-5, -1, 400)      # m
    S, D = np.meshgrid(s, d, indexing="xy")
    r = rates(S, D, T)
    series = 1 / (1 / r["basal"] + 1 / r["gbs"])
    total = r["diff"] + series + r["disl"]
    # 0 diffusion, 1 GBS-limited, 2 basal-slip-limited, 3 dislocation creep
    stack = np.stack([r["diff"], series, r["disl"]])
    dom = np.argmax(stack, axis=0)
    field = np.where(dom == 0, 0, np.where(dom == 2, 3, np.where(r["gbs"] < r["basal"], 1, 2)))

    fig, ax = plt.subplots(figsize=(7.2, 5.4), dpi=160)
    fig.patch.set_facecolor(PAPER)
    cmap = ListedColormap(["#dbeafe", "#dcfce7", "#fef9c3", "#fde2e2"])  # diff, GBS, basal, disl
    ax.pcolormesh(d * 1e3, s, field.T, cmap=cmap, vmin=-0.5, vmax=3.5, shading="auto", rasterized=True)
    ax.contour(d * 1e3, s, field.T, levels=[0.5, 1.5, 2.5], colors=INK, linewidths=1.3)
    cs = ax.contour(d * 1e3, s, np.log10(total.T), levels=np.arange(-14, -2, 2), colors=MUTED,
                    linewidths=0.7, linestyles="--")
    ax.clabel(cs, fmt=lambda v: f"$10^{{{int(v)}}}$ s$^{{-1}}$", fontsize=7.5)
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlabel("grain size (mm)"); ax.set_ylabel("differential stress (MPa)")
    # (Basal slip limits the series pair only for grains of ~2-15 microns, where diffusion
    # creep is faster still, so no basal-slip-limited field shows at -10 C.)
    labels = [(0.025, 0.0025, "diffusion creep\n($n=1$)"),
              (0.25, 0.06, "grain-boundary sliding,\nGBS-limited ($n\\approx1.8$)"),
              (12, 2.5, "dislocation creep\n($n\\approx4$)")]
    for x, y, lab in labels:
        ax.text(x, y, lab, ha="center", va="center", fontsize=9.5)
    # where natural ice sits
    for (x0, x1, y0, y1, lab) in [(1, 5, 0.01, 0.1, "ice-sheet\ninteriors"), (2, 20, 0.1, 0.3, "shear\nmargins")]:
        ax.add_patch(plt.Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False, ec=ACCENT, lw=1.6))
        ax.text(x1 * 1.1, np.sqrt(y0 * y1) * (1 if y1 > 0.2 else 0.6), lab, color=ACCENT, fontsize=8.5, va="center")
    ax.set_title(f"Deformation mechanisms of ice at {T - 273.15:.0f} °C", fontsize=11)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    fig.tight_layout()
    out = os.path.join(FIG_DIR, "deformation-mechanism-map.png")
    fig.savefig(out)
    print(out)


if __name__ == "__main__":
    main()
