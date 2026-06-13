"""Temperature dependence of radio-band absorption in ice.

Debye relaxation model: alpha(omega) = (d_eps / (n c)) * omega^2 tau / (1 + omega^2 tau^2),
saturating at the plateau d_eps/(n c tau) for omega tau >> 1. Relaxation time is
Arrhenius, anchored at tau(273 K) = 2.2e-5 s with activation energy 0.58 eV
(Auty-Cole-type parameters; see Petrenko & Whitworth ch. 4). Pure ice only;
impurity conduction raises the cold-ice floor.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 10, "axes.linewidth": 0.8})

c = 3.0e8
n = 1.78                  # sqrt(3.2)
d_eps = 100.0 - 3.2       # static minus high-frequency permittivity
E_over_k = 0.58 / 8.617e-5   # activation energy / k_B, in K
tau273 = 2.2e-5

def tau(T):
    return tau273 * np.exp(E_over_k * (1.0/T - 1.0/273.15))

lam = np.logspace(0, 8, 600)          # vacuum wavelength, m
omega = 2 * np.pi * c / lam

fig, ax = plt.subplots(figsize=(7.2, 4.8))
temps = [0, -20, -40, -60]
colors = plt.cm.coolwarm(np.linspace(0.95, 0.1, len(temps)))
for Tc, col in zip(temps, colors):
    t = tau(Tc + 273.15)
    alpha = (d_eps / (n * c)) * omega**2 * t / (1 + (omega * t)**2)
    ax.plot(lam, alpha, color=col, lw=1.7, label=f"{Tc} °C")
    
ax.axvspan(1, 10, color="C2", alpha=0.15)
ax.text(3.2, 4e-2, "radar\nsounding\nband", ha="center", fontsize=8.5)

ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlim(1, 1e8); ax.set_ylim(1e-7, 2e-1)
ax.set_xlabel("wavelength (m)")
ax.set_ylabel("absorption coefficient (m$^{-1}$)")
ax.legend(frameon=False, title="ice temperature", fontsize=9, loc="lower left")

# right axis: dB/km for the radar community
ax2 = ax.secondary_yaxis("right", functions=(lambda a: 4343*a, lambda d: d/4343))
ax2.set_ylabel("attenuation (dB km$^{-1}$)")
ax.spines["top"].set_visible(False)
fig.tight_layout()
out = os.path.join(os.path.dirname(__file__), "..", "sections", "foundations",
                   "figures", "ice-attenuation-temperature.png")
fig.savefig(out, dpi=160)
print("written")
