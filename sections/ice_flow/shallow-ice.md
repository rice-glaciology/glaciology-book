# The shallow-ice approximation

The full Stokes equations are exact but expensive. The way glaciology has made progress for decades is to exploit a simple geometric fact: **ice sheets are thin**. An ice sheet may be 3 km thick but 3000 km across — an aspect ratio of $\varepsilon \sim 10^{-3}$. Scaling the Stokes equations with this small parameter and discarding the smallest terms produces a hierarchy of cheaper, approximate models. The first and simplest is the **shallow-ice approximation** (SIA).

## The scaling idea

Let $[H]$ be a typical thickness and $[L]$ a typical horizontal length, with $\varepsilon = [H]/[L] \ll 1$. When the Stokes equations are non-dimensionalized, each stress term carries a power of $\varepsilon$. Some terms are order 1, some order $\varepsilon$, some order $\varepsilon^2$. An approximation is just a decision about **how many powers of $\varepsilon$ to keep**. Keeping only the leading order gives the SIA; keeping more terms gives the higher-order models of the next chapter. This single idea organizes the entire family of ice-flow models {cite}`schoof2010`.

## What the SIA keeps

At leading order, the horizontal momentum balance reduces to a local balance between the **driving stress** and the **vertical gradient of horizontal shear stress**. All membrane (longitudinal and lateral) stresses are dropped. The shear stress at depth is then simply

$$
\tau_{xz}(z) = -\rho\, g\, (s - z)\, \frac{\partial s}{\partial x},
$$

which grows linearly from zero at the surface to its maximum at the bed. Physically: each layer of ice must support the weight of all the ice above it, sliding over the layer below.

## The velocity profile

Feeding this shear stress into Glen's flow law and integrating from the bed upward gives the classic **SIA velocity–depth profile**. For flow with no basal sliding,

$$
u(z) = u_b + \frac{2A}{n+1}\,(\rho g)^n\,\left|\frac{\partial s}{\partial x}\right|^{\,n-1}\frac{\partial s}{\partial x}\left[\,H^{\,n+1} - (s-z)^{\,n+1}\right],
$$

where $u_b$ is any basal sliding velocity. The surface velocity therefore scales as

$$
u_s \;\propto\; A\,(\rho g)^n\,|\nabla s|^{\,n}\,H^{\,n+1}.
$$

This compact result captures a great deal of intuition: flow is faster where the ice is **thicker** (the $H^{n+1}$ factor), where the surface is **steeper**, and where the ice is **softer/warmer** (larger $A$). Because $n\approx 3$, the dependence on thickness and slope is steep — small geometric changes produce large changes in speed. The shape of the profile — most of the deformation concentrated near the warm bed — is the **Lliboutry profile**, and it matches deformation measured in deep boreholes reasonably well {cite}`cuffey2010`.

## When the SIA is good — and when it fails

The SIA is excellent in the **slow interior** of an ice sheet, where flow really is dominated by vertical shear and basal drag and where stresses are not transmitted far horizontally. It is cheap enough to run for whole ice sheets over glacial cycles, which is why it underlies many paleo-ice-sheet models.

It **fails** exactly where the interesting dynamics happen: ice streams, outlet glaciers, ice shelves, and grounding lines. There, ice slides rapidly, vertical shear is small, and the flow is controlled by membrane stresses and by stresses transmitted over long distances — all of which the SIA throws away. For those regimes we need a different member of the hierarchy, which is the subject of the next chapter.
