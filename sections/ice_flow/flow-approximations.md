# A hierarchy of flow models

The shallow-ice approximation is the simplest of a family of ice-flow models, and each member of the family is defined by which terms of the Stokes momentum balance it keeps. This chapter derives the momentum balance at each level, starting from the full equations and working down to the cheapest depth-integrated model, so that the assumptions behind each are explicit. Throughout, $x$ and $y$ are horizontal, $z$ points up, the surface is at $z=s$ and the bed at $z=b$, the thickness is $H=s-b$, and the velocity is $\mathbf{u}=(u,v,w)$.

## The Stokes equations

From {doc}`stress-balance`, slow ice flow obeys the Stokes momentum balance, $\nabla\!\cdot\!\boldsymbol{\sigma}+\rho\mathbf{g}=0$, with $\boldsymbol{\sigma}=\boldsymbol{\tau}-p\mathbf{I}$. Written out, the horizontal ($x$) and vertical components are

$$
\frac{\partial \tau_{xx}}{\partial x}+\frac{\partial \tau_{xy}}{\partial y}+\frac{\partial \tau_{xz}}{\partial z}-\frac{\partial p}{\partial x}=0,
$$

$$
\frac{\partial \tau_{xz}}{\partial x}+\frac{\partial \tau_{yz}}{\partial y}+\frac{\partial \tau_{zz}}{\partial z}-\frac{\partial p}{\partial z}-\rho g=0,
$$

where $\tau_{xx}$ is the longitudinal deviatoric stress, $\tau_{xy}$ and $\tau_{xz}$ the horizontal and vertical shear stresses, $\tau_{zz}$ the vertical normal deviatoric stress, $p$ the pressure, $\rho$ the density, and $g$ the gravitational acceleration. In the horizontal equation the three stress-gradient terms are the net forces per unit volume from the gradients of longitudinal stretching, horizontal shear, and vertical shear, and $\partial p/\partial x$ is the horizontal pressure gradient that resists them. In the vertical equation the stress-gradient terms balance the pressure gradient $\partial p/\partial z$ and the weight $\rho g$. This is accompanied by a matching $y$ equation, the incompressibility condition $\nabla\!\cdot\!\mathbf{u}=0$, and Glen's law relating $\boldsymbol{\tau}$ to the strain rate. This is the **full Stokes** system. It keeps every term and is the most accurate and most expensive model, needed near grounding lines, ice divides, and steep terrain.

## The hydrostatic approximation

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

Integrating from $z$ to the surface, where $\tau_{xz}=0$, gives $\tau_{xz}=-\rho g(s-z)\,\partial s/\partial x$, and inserting this into Glen's law and integrating once more in $z$ gives the velocity profile of {doc}`shallow-ice`. The momentum balance is purely local, so the velocity at a point depends only on the thickness and surface slope there, and no stress is transmitted horizontally.

```{admonition} Where on a real ice sheet these assumptions hold
:class: note

The maps of Greenland and Antarctica sort themselves by exactly this approximation. Over the slow interior, where ice is frozen to a hard bed or sliding weakly, deformation is vertical shear and the SIA is excellent; this is most of East Antarctica and the Greenland summit region. The approximation fails where its neglected stresses do the work. Ice streams like those of the Siple Coast slide as plugs over weak marine till, with the driving stress carried not by the bed but by lateral drag at their crevassed shear margins, more than half of it in the measured cases {cite}`echelmeyer1994`, and their locations follow the sedimentary basins beneath them {cite}`studinger2001`. Ice shelves have no basal drag at all. Divides, grounding lines, and steep bedrock relief violate the smallness assumptions in their own ways. The geography of the approximations, slow shear-dominated interior, membrane-stress streams and shelves, is the geography of the two modern ice sheets surveyed in {doc}`../cryosphere/ice-sheets`, and the practical resolution is the hybrid and higher-order models below.
```

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

```{admonition} Derivation
:class: dropdown

Start from the $x$ momentum balance $\partial\tau_{xx}/\partial x+\partial\tau_{xy}/\partial y+\partial\tau_{xz}/\partial z=\partial p/\partial x$ and integrate term by term from $b$ to $s$. The vertical-shear term integrates to the boundary tractions as shown above, $\int_b^s\partial\tau_{xz}/\partial z\,\mathrm{d}z=-\tau_{b,x}$. The pressure term gives the driving stress, $\int_b^s\partial p/\partial x\,\mathrm{d}z=\rho g H\,\partial s/\partial x$. The two membrane terms remain. Because the ice slides as a plug, the horizontal velocities and hence the deviatoric stresses are nearly independent of depth, so on the left the integrals over $\partial\tau_{xx}/\partial x$ and $\partial\tau_{xy}/\partial y$ act on depth-independent integrands and the order of integration and horizontal differentiation may be exchanged, contributing $\partial(H\tau_{xx})/\partial x$ and $\partial(H\tau_{xy})/\partial y$ up to surface-slope terms that cancel against the basal-traction definition.

Now express the deviatoric stresses through the viscous flow law $\tau_{ij}=2\eta\,\dot\varepsilon_{ij}$. Incompressibility, $\dot\varepsilon_{xx}+\dot\varepsilon_{yy}+\dot\varepsilon_{zz}=0$, lets the vertical normal strain rate be eliminated, $\dot\varepsilon_{zz}=-(\dot\varepsilon_{xx}+\dot\varepsilon_{yy})$, equivalently $\tau_{zz}=-(\tau_{xx}+\tau_{yy})$. The longitudinal normal deviatoric stress is therefore

$$
\tau_{xx}=2\eta\,\dot\varepsilon_{xx}=2\eta\,\frac{\partial u}{\partial x}
=2\eta\left(2\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}\right)-2\eta\!\left(\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}\right),
$$

but the more useful form follows from writing the resistive stress that appears in the momentum balance as the full deviatoric stress plus the eliminated $\tau_{zz}$. Combining $\tau_{xx}-\tau_{zz}=2\tau_{xx}+\tau_{yy}=2\eta(2\dot\varepsilon_{xx}+\dot\varepsilon_{yy})$ gives the effective longitudinal stress $2\eta(2\,\partial u/\partial x+\partial v/\partial y)$, while the shear deviatoric stress is $\tau_{xy}=\eta(\partial u/\partial y+\partial v/\partial x)$. Replacing the depth-varying viscosity and velocity by their depth averages $\bar\eta$, $\bar u$, $\bar v$, and multiplying each by the thickness $H$ from the integration, the membrane terms become

$$
\frac{\partial}{\partial x}\!\left[2H\bar\eta\!\left(2\frac{\partial\bar u}{\partial x}+\frac{\partial\bar v}{\partial y}\right)\right]
+\frac{\partial}{\partial y}\!\left[H\bar\eta\!\left(\frac{\partial\bar u}{\partial y}+\frac{\partial\bar v}{\partial x}\right)\right].
$$

Moving the basal drag to the left and keeping the driving stress on the right gives the printed balance {cite}`macayeal1989`.
```

with a symmetric $y$ equation, where $\bar u,\bar v$ are the depth-averaged horizontal velocities, $\bar\eta$ the depth-averaged viscosity, $H$ the thickness, and $\tau_{b,x}$ the basal drag {cite}`macayeal1989`. The first term is the gradient of the depth-integrated longitudinal stress, the push and pull of stretching and compression along the flow, the second is the gradient of the depth-integrated lateral shear stress, the drag transmitted sideways across the flow, $\tau_{b,x}$ is the friction the bed exerts on the sliding ice, and the right-hand side $\rho g H\,\partial s/\partial x$ is the gravitational driving stress that the membrane and basal terms together oppose. For a floating shelf $\tau_b=0$, and the ice-shelf lab solves exactly this. Unlike the local SIA balance, this is an elliptic problem in which membrane stress couples the flow across the whole domain, which is what lets shelves and streams transmit stress through grounding lines.

## Hybrid models

Real ice sheets shear in their interiors and slide at their margins, so a useful model must contain both balances. **Hybrid** models combine them, for example by writing the velocity as the sum of a depth-varying shearing part from the SIA and a depth-independent sliding part from the SSA, so that the same model relaxes to the local shear balance where sliding is weak and to the membrane balance where it dominates {cite}`bueler2009`. This gives a single set of equations valid across both regimes at a cost only modestly above the SSA, which is why hybrids are the workhorse of continental simulation.

## Higher-order models

A more complete reduction keeps the hydrostatic vertical balance but retains both the membrane and the vertical-shear resistive terms in the horizontal equations, dropping only the horizontal gradients of the vertical shear stresses, the so-called bridging stresses. The result is the **Blatter-Pattyn** or first-order system,

$$
\frac{\partial}{\partial x}\!\left[2\eta\left(2\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}\right)\right]
+\frac{\partial}{\partial y}\!\left[\eta\left(\frac{\partial u}{\partial y}+\frac{\partial v}{\partial x}\right)\right]
+\frac{\partial}{\partial z}\!\left[\eta\,\frac{\partial u}{\partial z}\right]=\rho g\,\frac{\partial s}{\partial x},
$$

```{admonition} Derivation
:class: dropdown

Begin from the full $x$ momentum balance with the hydrostatic pressure already substituted, so the right side is the driving stress $\rho g\,\partial s/\partial x$. The first-order approximation retains the leading-order deviatoric stresses but drops the two horizontal gradients of the vertical shear stress, $\partial\tau_{xz}/\partial x$ relative to its vertical gradient and the analogous bridging term, which scaling shows to be smaller by $O(\varepsilon^2)$. What remains on the left are the membrane terms $\partial\tau_{xx}/\partial x+\partial\tau_{xy}/\partial y$ and the vertical-shear term $\partial\tau_{xz}/\partial z$.

Express each through the viscous flow law $\tau_{ij}=2\eta\dot\varepsilon_{ij}$ and eliminate $\tau_{zz}$ by incompressibility exactly as in the shallow-shelf reduction. The longitudinal resistive stress becomes $\tau_{xx}-\tau_{zz}=2\eta(2\,\partial u/\partial x+\partial v/\partial y)$, the in-plane shear $\tau_{xy}=\eta(\partial u/\partial y+\partial v/\partial x)$, and the vertical shear $\tau_{xz}=\eta\,\partial u/\partial z$, where the term $\partial w/\partial x$ in $\dot\varepsilon_{xz}$ is dropped at this order. Substituting,

$$
\frac{\partial}{\partial x}\!\left[2\eta\!\left(2\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}\right)\right]
+\frac{\partial}{\partial y}\!\left[\eta\!\left(\frac{\partial u}{\partial y}+\frac{\partial v}{\partial x}\right)\right]
+\frac{\partial}{\partial z}\!\left[\eta\,\frac{\partial u}{\partial z}\right]
=\rho g\,\frac{\partial s}{\partial x},
$$

the printed system {cite}`pattyn2003`. Unlike the shallow-shelf balance the equation is not integrated through the thickness, so it retains the depth-varying shear and is three-dimensional.
```

with the matching $y$ equation {cite}`pattyn2003`, where $u,v$ are the horizontal velocities, $\eta$ the effective viscosity, $\rho$ the density, $g$ gravity, and $s$ the surface elevation. The first two terms are the horizontal gradients of the longitudinal and lateral membrane stresses, as in the shallow-shelf balance but now retained at every depth rather than depth-averaged, the third term $\partial(\eta\,\partial u/\partial z)/\partial z$ is the vertical gradient of the vertical-shear stress, the resistance that the shallow-shelf balance drops, and the right-hand side is the driving stress. Keeping both the membrane and the vertical-shear terms is what places this model between the two depth-integrated limits. This is three-dimensional and resolves the depth-varying stress state far more faithfully than the depth-integrated models, at correspondingly higher cost, and is appropriate in grounding zones and other places where the flow is complicated. The asymptotic theory that places all of these models on a single ladder is given by {cite}`schoof2010`.

## Summary of the hierarchy

| Model | Horizontal balance retained | Dropped | Best for |
|---|---|---|---|
| **SIA** | vertical shear gradient $\partial\tau_{xz}/\partial z$ vs driving stress | all membrane stresses | slow interiors |
| **SSA** | depth-integrated membrane stresses, basal drag | vertical shear | streams, shelves |
| **Hybrid** | shear and membrane, summed | cross-coupling between them | whole ice sheets |
| **Blatter-Pattyn** | membrane and vertical shear in 3-D | bridging stresses | grounding zones |
| **Full Stokes** | everything | nothing | divides, benchmarks |

icepack is organized around this ladder. Its ice-shelf and ice-stream models solve the shallow-shelf balance, and its hybrid model adds the vertical-shear term. Choosing an icepack model is choosing a rung, and the labs build up a model at the shelf and hybrid levels, where the dynamics that matter most for sea level take place.
