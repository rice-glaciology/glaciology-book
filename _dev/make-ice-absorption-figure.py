"""Absorption spectrum of ice Ih vs wavelength.

Currently drawn through order-of-magnitude anchor values after Warren & Brandt
(2008). To upgrade to the exact compilation: download IOP_2008_ASCIItable.dat
from https://atmos.uw.edu/ice_optical_constants/, place it next to this script,
and the loader below will use it (alpha = 4*pi*k/lambda).
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator

plt.rcParams.update({"font.size": 10, "axes.linewidth": 0.8})

DAT = os.path.join(os.path.dirname(__file__), "IOP_2008_ASCIItable.dat")
if os.path.exists(DAT):
    d = np.loadtxt(DAT)
    lam_um, k = d[:, 0], d[:, 2]
    lx = np.log10(lam_um)
    ly = np.log10(4 * np.pi * k / (lam_um * 1e-6))
    schematic = False
else:
    anchors = [
        (0.12, 1e7), (0.17, 1e6), (0.25, 1e-2), (0.32, 2e-3), (0.40, 6e-4),
        (0.50, 2e-3), (0.60, 6e-2), (0.70, 0.6), (0.80, 2.0), (0.90, 7.0),
        (1.0, 20.0), (1.2, 1e2), (1.5, 2e3), (2.0, 1e4), (2.6, 5e4),
        (3.08, 2e6), (3.6, 3e4), (4.5, 5e4), (6.1, 3e5), (8.0, 8e4),
        (12.0, 3e5), (20.0, 1.2e5), (45.0, 3e5), (100.0, 4e4), (300.0, 2e3),
        (1e3, 60.0), (1e4, 1.5), (1e5, 4e-2), (1e6, 4e-3), (1e7, 1.5e-3),
    ]
    lam = np.array([a[0] for a in anchors]); alp = np.array([a[1] for a in anchors])
    f = PchipInterpolator(np.log10(lam), np.log10(alp))
    lx = np.linspace(np.log10(lam[0]), np.log10(lam[-1]), 800)
    ly = f(lx)
    schematic = True

fig, ax = plt.subplots(figsize=(7.6, 5.0))
ax.plot(10**lx, 10**ly, color="k", lw=1.6)
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlim(1e-1, 1e7); ax.set_ylim(1e-4, 2e8)
ax.set_xlabel("wavelength (µm)")
ax.set_ylabel("absorption coefficient (m$^{-1}$)")

ax.axvspan(0.4, 0.7, color="C0", alpha=0.15)
ax.text(0.53, 4e-1, "visible\nwindow", ha="center", fontsize=8.5)
ax.axvspan(3e5, 1e7, color="C2", alpha=0.15)
ax.text(1.7e6, 1e5, "radar\nwindow", ha="center", fontsize=8.5)

top = 4e7
for label, xpk, ypk, xt in [
    ("O–H stretch\n3.1 µm", 3.08, 2.6e6, 1.1),
    ("bend\n6 µm", 6.1, 4e5, 4.6),
    ("libration", 12.0, 4e5, 26.0),
    ("lattice\nmodes", 45.0, 4e5, 70.0),
]:
    ax.annotate(label, xy=(xpk, ypk), xytext=(xt, top), fontsize=8.5,
                ha="center", va="bottom",
                arrowprops=dict(arrowstyle="-", lw=0.7, color="0.4"))
ax.annotate("electronic\nabsorption (UV)", xy=(0.155, 1e5), xytext=(0.105, 6e1),
            fontsize=8.5, arrowprops=dict(arrowstyle="-", lw=0.7, color="0.4"))
ax.annotate("blue minimum", xy=(0.40, 6e-4), xytext=(1.6, 2e-4), fontsize=8.5,
            arrowprops=dict(arrowstyle="-", lw=0.7, color="0.4"))

ax2 = ax.secondary_yaxis("right", functions=(lambda a: 1/np.maximum(a, 1e-30),
                                             lambda d: 1/np.maximum(d, 1e-30)))
ax2.set_ylabel("penetration depth $1/\\alpha$ (m)")
ax.spines["top"].set_visible(False)
fig.tight_layout()
out = os.path.join(os.path.dirname(__file__), "..", "sections", "foundations",
                   "figures", "ice-absorption-spectrum.png")
fig.savefig(out, dpi=160)
print("written", "(schematic)" if schematic else "(Warren & Brandt data)")
