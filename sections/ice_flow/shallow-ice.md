# The shallow-ice approximation

The full Stokes equations of {doc}`stress-balance` are exact but expensive. The way glaciology has made progress for decades is to exploit a simple geometric fact: ice sheets are thin. An ice sheet may be three kilometres thick and three thousand kilometres across, an aspect ratio of about $\varepsilon\sim10^{-3}$. Scaling the Stokes equations with this small parameter and discarding the smallest terms produces a hierarchy of cheaper, approximate models. The first and simplest is the shallow-ice approximation, and this chapter derives it and the velocity profile it predicts. The full hierarchy is the subject of {doc}`flow-approximations`, and the analytical ice-sheet shapes that the shallow-ice approximation makes possible are derived in {doc}`analytical-solutions`. The development follows {cite}`hutter1983` and {cite}`cuffey2010`.

## The scaling idea

Let $[H]$ be a typical thickness and $[L]$ a typical horizontal length, with $\varepsilon=[H]/[L]\ll1$. When the Stokes equations are written in dimensionless form, each stress term carries a power of $\varepsilon$. Some terms are of order one, some of order $\varepsilon$, some of order $\varepsilon^2$. An approximation is a decision about how many powers of $\varepsilon$ to keep. Keeping only the leading order gives the shallow-ice approximation; keeping more terms gives the higher-order models of the next chapter. This single idea organizes the entire family of ice-flow models {cite}`schoof2010`.

## What the approximation keeps

At leading order two simplifications follow from the thin geometry. In the vertical, the deviatoric terms are negligible and the vertical momentum balance reduces to the hydrostatic relation, so the pressure is cryostatic,

$$
p = \rho_i g\,(s-z).
$$

In the horizontal, the balance reduces to a local one between the gradient of this pressure, set by the surface slope, and the vertical gradient of the horizontal shear stress. Integrating that balance downward from the stress-free surface gives the shear stress at depth,

$$
\tau_{xz}(z) = -\rho_i g\,(s-z)\,\frac{\partial s}{\partial x},
$$

which grows linearly from zero at the surface to its largest value at the bed. Physically, each layer of ice must support, through shear, the downslope weight of all the ice above it. All membrane stresses, the longitudinal and lateral stresses carried in {doc}`stress-balance`, are dropped at this order.

## The velocity profile

Feeding this shear stress into Glen's flow law, written for simple shear as $\partial u/\partial z = 2A\,|\tau_{xz}|^{\,n-1}\tau_{xz}$, and integrating upward from the bed gives the velocity at each depth,

$$
u(z) = u_b + \frac{2A(\rho_i g)^{n}}{n+1}\,\left[H^{\,n+1}-(s-z)^{\,n+1}\right]\left|\frac{\partial s}{\partial x}\right|^{\,n-1}\left(-\frac{\partial s}{\partial x}\right),
$$

where $u_b$ is any basal sliding velocity supplied by the friction law of {doc}`../thermomechanics/basal-motion`. The deformation is concentrated near the bed, where the shear stress is largest, so the velocity changes most rapidly there and the profile is nearly uniform through the upper ice. This shape, the Lliboutry profile, matches the deformation measured in deep boreholes reasonably well {cite}`cuffey2010`. Averaging through the thickness gives the depth-averaged velocity,

$$
\bar u = u_b + \frac{2A(\rho_i g)^{n}}{n+2}\,H^{\,n+1}\,\left|\frac{\partial s}{\partial x}\right|^{\,n-1}\left(-\frac{\partial s}{\partial x}\right),
$$

the single result that the shallow-ice approximation contributes to the evolution of an ice sheet. The deformational part depends very steeply on the geometry, growing as the thickness to the power $n+1$ and the surface slope to the power $n$. Because $n\approx3$, a small change in thickness or slope produces a large change in speed, and the velocity is controlled almost entirely by the ice thickness and the surface slope.

## The thickness equation

The depth-averaged velocity closes the equation that evolves an ice sheet. Conservation of mass, integrated through the thickness, states that the thickness changes when the flux of ice into a column does not balance the net surface and basal mass gain,

$$
\frac{\partial H}{\partial t} + \frac{\partial}{\partial x}\!\left(\bar u\,H\right) = \dot b,
$$

where the balance function $\dot b=a-m$ is the net rate of accumulation minus melt, the subject of {doc}`mass-balance`. Substituting the shallow-ice expression for $\bar u$ turns this into a single nonlinear diffusion equation for the surface, cheap enough to integrate over whole glacial cycles, which is why the shallow-ice approximation underlies most paleo-ice-sheet models. Its steady solutions, the classic analytical ice-sheet profiles, are derived in {doc}`analytical-solutions`.

## When the approximation holds

The shallow-ice approximation is excellent in the slow interior of an ice sheet, where the flow really is dominated by vertical shear balanced locally by basal drag, and where stresses are not transmitted far horizontally. It fails exactly where the interesting dynamics happen: ice streams, outlet glaciers, ice shelves, and grounding lines. There the ice slides rapidly, vertical shear is small, and the flow is controlled by the membrane stresses and the long-range stress transmission that the approximation discards. For those regimes a different member of the hierarchy is needed, which is the subject of {doc}`flow-approximations`.
