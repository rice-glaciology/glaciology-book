"""Generate the plottable figures mentioned in the text (curves and schematics).

Run from the repo root:  python _dev/make-text-figures.py
Needs numpy, matplotlib, scipy. Writes PNGs into the chapters' figures/ folders.
The remaining TODO figures (roche moutonnee, tidewater cycle, terminus-flux wedge,
Mars/Europa cross-sections) are artistic cartoons left for Illustrator.
"""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid as cumtrapz
plt.rcParams.update({"font.size": 10, "axes.linewidth": 0.8, "figure.dpi": 160})
def clean(ax):
    for s in ("top", "right"): ax.spines[s].set_visible(False)
def sig(x): return 1/(1+np.exp(-x))

IF = "sections/ice_flow/figures/"; CL = "sections/climate/figures/"; CR = "sections/cryosphere/figures/"

# 1. Glen's law curves
fig, ax = plt.subplots(figsize=(5.6, 4.4)); t = np.linspace(0, 2, 400)
ax.plot(t, t, label="$n=1$ (Newtonian)", color="C0", lw=1.8)
ax.plot(t, t**3, label="$n=3$ (Glen)", color="C3", lw=1.8)
ax.plot([1, 1], [0, 8], label=r"perfect plastic ($n\to\infty$)", color="0.4", lw=1.8, ls="--")
ax.plot(1, 1, 'o', color="k", ms=5, zorder=5)
ax.annotate("normalized\nat $\\tau_0\\approx100$ kPa", (1, 1), (1.15, 1.6), fontsize=8.5,
            arrowprops=dict(arrowstyle="-", lw=0.7, color="0.4"))
ax.set_xlim(0, 2); ax.set_ylim(0, 8)
ax.set_xlabel(r"deviatoric stress $\tau/\tau_0$"); ax.set_ylabel(r"strain rate $\dot\varepsilon/\dot\varepsilon_0$")
ax.legend(frameon=False, fontsize=9, loc="upper left"); clean(ax)
fig.tight_layout(); fig.savefig(IF+"glen-law-curves.png"); plt.close(fig)

# 2. Creep curve
eps = np.logspace(-3, -1, 800)
edot = 1.0 + 60*np.exp(-eps/0.0018) + 2.0*sig((eps-0.03)/0.005)
imin = int(np.argmin(edot)); eps = eps*(0.01/eps[imin]); edn = edot/edot[imin]; plateau = edn[-1]
fig, (a1, a2) = plt.subplots(2, 1, figsize=(5.8, 6.4))
t = cumtrapz(1/edot, eps, initial=0); t = t/t.max()*10; ee = 0.0015; strain = ee+eps
a1.plot(t, strain, color="C0", lw=1.9); a1.plot([0, 0], [0, ee], color="C0", lw=1.9)
a1.annotate("elastic step", (0, ee), (0.2, ee*0.5), fontsize=8.5, va="center")
for frac, lab, dy in [(0.05, "primary", 0.0016), (0.45, "secondary", 0.0016), (0.9, "tertiary", -0.0015)]:
    xi = frac*10; yi = ee+np.interp(xi, t, eps); a1.annotate(lab, (xi, yi), (xi, yi+dy), fontsize=8.5, ha="center")
a1.set_xlim(0, 10); a1.set_ylim(0, strain.max()*1.06)
a1.set_xlabel("time"); a1.set_ylabel("strain $\\varepsilon$"); a1.set_title("(a) constant-stress creep test", fontsize=10)
a2.loglog(eps, edn, color="C3", lw=1.9); a2.plot(eps[imin], 1.0, 'o', color="k", ms=5, zorder=5)
a2.annotate("minimum at $\\sim$1% strain", (eps[imin], 1.0), (eps[imin]*1.5, 0.62), fontsize=8.5,
            arrowprops=dict(arrowstyle="-", lw=0.7, color="0.4"))
a2.axhline(plateau, ls=":", color="0.5", lw=0.9)
a2.annotate(r"tertiary plateau $\approx3\times$ minimum", (1.4e-3, plateau), (1.4e-3, plateau*1.15), fontsize=8.5)
a2.annotate("primary", (2e-3, 13), fontsize=8.5)
a2.set_xlim(1e-3, 1e-1); a2.set_ylim(0.55, 30)
a2.set_xlabel("strain $\\varepsilon$"); a2.set_ylabel(r"strain rate $\dot\varepsilon/\dot\varepsilon_{\min}$")
a2.set_title("(b) Glen's law describes the minimum; shear margins ride the plateau", fontsize=9)
clean(a1); clean(a2); fig.tight_layout(); fig.savefig(IF+"creep-curve.png"); plt.close(fig)

# 3. Response-time curve
fig, ax = plt.subplots(figsize=(5.6, 4.0)); x = np.linspace(0, 4, 400); y = 1-np.exp(-x)
ax.plot(x, y, color="C0", lw=1.9)
for tt, frac in [(1, 0.63), (2, 0.86)]:
    ax.plot([0, tt, tt], [frac, frac, 0], ls="--", color="0.6", lw=0.9); ax.plot(tt, frac, 'o', color="k", ms=5)
    ax.annotate(f"{int(frac*100)}%", (tt, frac), (tt+0.08, frac-0.07), fontsize=9)
ax.set_xlim(0, 4); ax.set_ylim(0, 1.05); ax.set_xticks([0, 1, 2, 3, 4])
ax.set_xticklabels(["0", "$t_r$", "$2t_r$", "$3t_r$", "$4t_r$"])
ax.set_xlabel("time"); ax.set_ylabel(r"length response $L'/L'_{\rm eq}$")
ax.set_title("Exponential approach after a step change in balance", fontsize=9.5); clean(ax)
fig.tight_layout(); fig.savefig(CL+"response-time-curve.png"); plt.close(fig)

# 4. Three-stage response
fig, ax = plt.subplots(figsize=(5.6, 4.0)); x = np.linspace(0, 4, 500); eps3 = 1/np.sqrt(3); s = x/eps3
ax.plot(x, 1-np.exp(-x), color="C0", lw=1.8, label="one-stage (exponential)")
ax.plot(x, 1-np.exp(-s)*(1+s+0.5*s**2), color="C3", lw=1.8, label="three-stage (sigmoidal)")
ax.set_xlim(0, 4); ax.set_ylim(0, 1.05); ax.set_xticks([0, 1, 2, 3, 4])
ax.set_xticklabels(["0", "$\\tau$", "$2\\tau$", "$3\\tau$", "$4\\tau$"])
ax.set_xlabel("time"); ax.set_ylabel(r"length response $L'/L'_{\rm eq}$")
ax.legend(frameon=False, fontsize=9, loc="lower right"); clean(ax)
ax.set_title("Same equilibrium and timescale, different onset", fontsize=9.5)
fig.tight_layout(); fig.savefig(CL+"three-stage-response.png"); plt.close(fig)

# 5. Permafrost trumpet
fig, ax = plt.subplots(figsize=(5.2, 5.8))
z = np.linspace(0, 350, 800); Ts = -10.0; G = 1/30; A0 = 15.0; da = 4.0
mean = Ts+G*z; amp = A0*np.exp(-z/da); winter = mean-amp; summer = mean+amp
zal = z[np.argmax(summer < 0)]; zbase = z[np.argmin(np.abs(mean))]
ax.fill_betweenx(z, winter, summer, color="0.86")
ax.fill_betweenx(z[(z >= zal) & (z <= zbase)], -26, 8, color="C0", alpha=0.05)
ax.plot(winter, z, color="C0", lw=1.4); ax.plot(summer, z, color="C3", lw=1.4); ax.plot(mean, z, color="k", lw=1.1, ls="--")
ax.axvline(0, color="0.4", lw=0.8)
ax.axhline(zal, color="0.45", lw=0.7, ls=":"); ax.axhline(zbase, color="0.45", lw=0.7, ls=":"); ax.axhline(16, color="0.6", lw=0.7, ls=":")
ax.annotate("active layer", (4.5, zal*0.5), fontsize=8.5, va="center", ha="center")
ax.annotate("permafrost top", (4.7, zal+12), fontsize=8.5, ha="center")
ax.annotate("depth of zero\nannual amplitude", (-25, 16), (-25, 40), fontsize=8, va="top")
ax.annotate("base of permafrost ($\\approx$300 m)", (0.5, zbase), (-24, zbase-12), fontsize=8.5)
ax.annotate("winter", (winter[150], z[150]), (winter[150]-6.5, z[150]), color="C0", fontsize=8.5)
ax.annotate("summer", (summer[110], z[110]), (summer[110]+0.8, z[110]), color="C3", fontsize=8.5)
ax.set_xlim(-26, 8); ax.set_ylim(355, -8)
ax.set_xlabel("temperature (°C)"); ax.set_ylabel("depth (m)")
ax.set_title("Trumpet diagram of ground temperature", fontsize=9.5); clean(ax)
fig.tight_layout(); fig.savefig(CR+"permafrost-trumpet.png"); plt.close(fig)

# 6. Brine volume
fig, ax = plt.subplots(figsize=(5.4, 4.2)); T = np.linspace(-20, -0.5, 400); mliq = 0.054; ratio = 917/950
for Si, c, lab in [(10, "C0", "first-year ice, $S_i=10$‰"), (5, "C3", "multiyear ice, $S_i=5$‰")]:
    ax.plot(T, 100*ratio*Si/(-T/mliq), color=c, lw=1.8, label=lab)
ax.set_xlim(-20, 0); ax.set_ylim(0, 30)
ax.set_xlabel("ice temperature (°C)"); ax.set_ylabel("brine volume fraction (%)")
ax.legend(frameon=False, fontsize=9); clean(ax)
ax.annotate("brine fraction diverges\ntoward the freezing point", (-3, 22), (-14, 24), fontsize=8.5,
            arrowprops=dict(arrowstyle="-", lw=0.7, color="0.4"))
ax.set_title("Brine volume from the freezing equilibrium", fontsize=9.5)
fig.tight_layout(); fig.savefig(CR+"brine-volume.png"); plt.close(fig)

# 7. MISI flux-stability on the MISMIP+ overdeepened bed (Schoof 2007 boundary-layer flux)
secyr = 3.15e7; rhoi, rhow, gg = 900., 1000., 9.8; nG, mW, Cf = 3., 1./3., 7.624e6
Ar = 9.8e-26; betaS = (mW+nG+3)/(mW+1); thetaF = 1 - rhoi/rhow     # betaS = 4.75
Omega = (Ar*(rhoi*gg)**(nG+1)*thetaF**nG/(4**nG*Cf))**(1/(mW+1)); acc = 0.5/secyr
def mismipplus_bed(xm):                                            # Asay-Davis et al. 2016 centreline
    X = xm/300e3
    return np.maximum(-150. - 728.8*X**2 + 343.91*X**4 - 50.57*X**6, -720.)
fig, (a1, a2) = plt.subplots(2, 1, figsize=(5.9, 6.2), sharex=True, gridspec_kw={"height_ratios": [2, 1]})
xk = np.linspace(150, 640, 2200); xm = xk*1e3
Bm = mismipplus_bed(xm); hgm = (rhow/rhoi)*np.maximum(-Bm, 0.0)    # flotation thickness
Qg = Omega*hgm**betaS                                              # m^2/s per unit width
Qkm = Qg*secyr/1e6; supply = acc*xm*secyr/1e6                      # km^2/yr
gQ = np.gradient(Qg, xm); dBdx = np.gradient(Bm, xm)
cross = [i for i in np.where(np.diff(np.sign(Qg-acc*xm)))[0] if xk[i] > 180]
a1.plot(xk, Qkm, color="C0", lw=1.9, label=r"grounding-line flux  $Q_g=\Omega\,h_{\rm g}^{\beta}$,  $\beta\approx5$")
a1.plot(xk, supply, color="0.5", lw=1.7, label=r"accumulation supply  $a\,x_g$")
for i in cross:
    stable = gQ[i] > acc
    a1.plot(xk[i], supply[i], 'o', ms=7, mfc=("k" if stable else "white"), mec="k", zorder=5)
    a1.annotate("stable" if stable else "unstable", (xk[i], supply[i]),
                (xk[i], supply[i]+0.085), ha="center", fontsize=8, color=("k" if stable else "C3"))
a1.set_ylim(0, 0.52); a1.set_ylabel(r"flux per unit width (km$^2$ yr$^{-1}$)")
a1.legend(frameon=False, fontsize=8.3, loc="upper left")
a1.set_title("Grounding-line flux against supply (MISMIP+ bed)", fontsize=9.5)
a2.plot(xk, Bm, color="0.3", lw=1.6); a2.fill_between(xk, Bm, Bm.min()-120, color="0.86")
a2.axhline(0, color="C0", lw=0.8, ls=":")
retro = (dBdx > 0) & (Bm > -719.)                                 # genuine retrograde reach (exclude flat cap)
a2.fill_between(xk, Bm.min()-120, 80, where=retro, color="C3", alpha=0.10, lw=0)
xr = xk[retro]
if len(xr): a2.annotate("retrograde", (xr.mean(), -300), ha="center", fontsize=8, color="C3")
for i in cross:
    a1.axvline(xk[i], color="0.8", lw=0.6, ls=":"); a2.axvline(xk[i], color="0.8", lw=0.6, ls=":")
a2.set_ylim(Bm.min()-120, 80); a2.set_xlabel(r"grounding-line position $x_g$ (km)")
a2.set_ylabel("bed elevation (m)")
clean(a1); clean(a2); fig.tight_layout(); fig.savefig(CR+"misi-flux-stability.png"); plt.close(fig)

print("7 text figures written")
