# A hierarchy of flow models

The shallow-ice approximation is the simplest of a family of ice-flow models, and each member of the family is defined by which terms of the Stokes momentum balance it keeps. This chapter derives the momentum balance at each level, starting from the full equations and working down to the cheapest depth-integrated model, so that the assumptions behind each are explicit. Throughout, $x$ and $y$ are horizontal, $z$ points up, the surface is at $z=s$ and the bed at $z=b$, the thickness is $H=s-b$, and the velocity is $\mathbf{u}=(u,v,w)$.

## The starting point: the Stokes equations

From {doc}`stress-balance`, slow ice flow obeys the Stokes momentum balance, $\nabla\!\cdot\!\boldsymbol{\sigma}+\rho\mathbf{g}=0$, with $\boldsymbol{\sigma}=\boldsymbol{\tau}-p\mathbf{I}$. Written out, the horizontal ($x$) and vertical components are

$$
\frac{\partial \tau_{xx}}{\partial x}+\frac{\partial \tau_{xy}}{\partial y}+\frac{\partial \tau_{xz}}{\partial z}-\frac{\partial p}{\partial x}=0,
$$

$$
\frac{\partial \tau_{xz}}{\partial x}+\frac{\partial \tau_{yz}}{\partial y}+\frac{\partial \tau_{zz}}{\partial z}-\frac{\partial p}{\partial z}-\rho g=0,
$$

with a matching $y$ equation, the incompressibility condition $\nabla\!\cdot\!\mathbf{u}=0$, and Glen's law relating $\boldsymbol{\tau}$ to the strain rate. This is the **full Stokes** system. It keeps every term and is the most accurate and most expensive model, needed near grounding lines, ice divides, and steep terrain.

## The shallow approximations begin with hydrostatic pressure

Ice sheets are thin, with an aspect ratio $\varepsilon = [H]/[L]\ll 1$. Scaling the equations with $\varepsilon$ shows that in the vertical balance the deviatoric terms are small, so to leading order the vertical momentum balance reduces to the hydrostatic relation $\partial p/\partial z = -\rho g$. Integrating downward from the stress-free surface gives the cryostatic pressure

$$
p \approx \rho g (s-z), \qquad \text{so that} \qquad \frac{\partial p}{\partial x}\approx \rho g\,\frac{\partial s}{\partial x}.
$$

The horizontal pressure gradient is the gravitational driving stress. Every reduced model shares this step; they differ only in which resistive terms they keep to balance it.

## The shallow-ice approximation

In the slow interior, flow is dominated by vertical shear and the membrane terms $\partial\tau_{xx}/\partial x$ and $\partial\tau_{xy}/\partial y$ are smaller by $O(\varepsilon^2)$. Dropping them leaves a local balance between the driving stress and the vertical gradient of the shear stress,

$$
\frac{\partial \tau_{xz}}{\partial z}=\rho g\,\frac{\partial s}{\partial x}.
$$

Integrating from $z$ to the surface, where $\tau_{xz}=0$, gives $\tau_{xz}=-\rho g(s-z)\,\partial s/\partial x$, and inserting this into Glen's law and integrating once more in $z$ gives the velocity profile of {doc}`shallow-ice`. The momentum balance is purely local: the velocity at a point depends only on the thickness and surface slope there, and no stress is transmitted horizontally.

## The shallow-shelf approximation

For fast-sliding ice and floating shelves the opposite holds: the ice slides as a plug, so the vertical shear $\tau_{xz}$ does the negligible work and the membrane terms carry the resistance. Take the velocity to be independent of depth and integrate the horizontal momentum balance through the thickness. The shear term integrates to the boundary tractions,

$$
\int_b^s \frac{\partial \tau_{xz}}{\partial z}\,\mathrm{d}z = \tau_{xz}(s)-\tau_{xz}(b) = -\tau_{b,x},
$$

since the surface is stress free and $\tau_{b,x}$ is the basal drag. Carrying out the depth integration of the remaining terms, using the hydrostatic pressure and the incompressibility relation $\tau_{zz}=-(\tau_{xx}+\tau_{yy})$ to eliminate $\tau_{zz}$, yields the **shallow-shelf** (or shelfy-stream) momentum balance,

$$
\frac{\partial}{\partial x}\!\left[2H\bar\eta\left(2\frac{\partial \bar u}{\partial x}+\frac{\partial \bar v}{\partial y}\right)\right]
+\frac{\partial}{\partial y}\!\left[H\bar\eta\left(\frac{\partial \bar u}{\partial y}+\frac{\partial \bar v}{\partial x}\right)\right]
-\tau_{b,x}=\rho g H\,\frac{\partial s}{\partial x},
$$

with a symmetric $y$ equation, where $\bar u,\bar v$ are the depth-averaged velocities and $\bar\eta$ the depth-averaged viscosity {cite}`macayeal1989`. For a floating shelf $\tau_b=0$, and the ice-shelf lab solves exactly this. Unlike the local SIA balance, this is an elliptic problem in which membrane stress couples the flow across the whole domain, which is what lets shelves and streams transmit stress through grounding lines.

## Hybrid models

Real ice sheets shear in their interiors and slide at their margins, so a useful model must contain both balances. **Hybrid** models combine them, for example by writing the velocity as the sum of a depth-varying shearing part from the SIA and a depth-independent sliding part from the SSA, so that the same model relaxes to the local shear balance where sliding is weak and to the membrane balance where it dominates {cite}`bueler2009`. This gives a single set of equations valid across both regimes at a cost only modestly above the SSA, which is why hybrids are the workhorse of continental simulation.

## Higher-order models

A more complete reduction keeps the hydrostatic vertical balance but retains both the membrane and the vertical-shear resistive terms in the horizontal equations, dropping only the horizontal gradients of the vertical shear stresses, the so-called bridging stresses. The result is the **Blatter-Pattyn** or first-order system,

$$
\frac{\partial}{\partial x}\!\left[2\eta\left(2\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}\right)\right]
+\frac{\partial}{\partial y}\!\left[\eta\left(\frac{\partial u}{\partial y}+\frac{\partial v}{\partial x}\right)\right]
+\frac{\partial}{\partial z}\!\left[\eta\,\frac{\partial u}{\partial z}\right]=\rho g\,\frac{\partial s}{\partial x},
$$

with the matching $y$ equation {cite}`pattyn2003`. This is three-dimensional and resolves the depth-varying stress state far more faithfully than the depth-integrated models, at correspondingly higher cost, and is appropriate in grounding zones and other places where the flow is complicated. The asymptotic theory that places all of these models on a single ladder is given by {cite}`schoof2010`.

## The ladder at a glance

| Model | Horizontal balance retained | Dropped | Best for |
|---|---|---|---|
| **SIA** | vertical shear gradient $\partial\tau_{xz}/\partial z$ vs driving stress | all membrane stresses | slow interiors |
| **SSA** | depth-integrated membrane stresses, basal drag | vertical shear | streams, shelves |
| **Hybrid** | shear and membrane, summed | cross-coupling between them | whole ice sheets |
| **Blatter-Pattyn** | membrane and vertical shear in 3-D | bridging stresses | grounding zones |
| **Full Stokes** | everything | nothing | divides, benchmarks |

icepack is organized around this ladder. Its ice-shelf and ice-stream models solve the shallow-shelf balance, and its hybrid model adds the vertical-shear term. Choosing an icepack model is choosing a rung, and the labs build up a model at the shelf and hybrid levels, where the dynamics that matter most for sea level take place.
