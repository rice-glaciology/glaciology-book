# The shallow-ice approximation

The full Stokes equations of {doc}`stress-balance` are exact but expensive. The way glaciology has made progress for decades is to exploit a simple geometric fact: ice sheets are thin. An ice sheet may be three kilometres thick and three thousand kilometres across, an aspect ratio of about $\varepsilon\sim10^{-3}$. Scaling the Stokes equations with this small parameter and discarding the smallest terms produces a hierarchy of cheaper, approximate models. The first and simplest is the shallow-ice approximation, and this chapter derives it, the velocity profile it predicts, and the perfect-plastic ice-sheet shape that follows in its rheological limit. The full hierarchy is the subject of {doc}`flow-approximations`. The development follows {cite}`hutter1983` and {cite}`cuffey2010`.

## Scaling analysis

Let $[H]$ be a typical thickness and $[L]$ a typical horizontal length, with $\varepsilon=[H]/[L]\ll1$. When the Stokes equations are written in dimensionless form, each stress term carries a power of $\varepsilon$. Some terms are of order one, some of order $\varepsilon$, some of order $\varepsilon^2$. An approximation is a decision about how many powers of $\varepsilon$ to keep. Keeping only the leading order gives the shallow-ice approximation; keeping more terms gives the higher-order models of the next chapter. This single idea organizes the entire family of ice-flow models {cite}`schoof2010`.

## The reduced stress balance

At leading order two simplifications follow from the thin geometry. In the vertical, the deviatoric terms are negligible and the vertical momentum balance reduces to the hydrostatic relation, so the pressure is cryostatic,

$$
p = \rho_i g\,(s-z).
$$

```{admonition} Derivation
:class: dropdown
At leading order the vertical momentum balance drops the small deviatoric and acceleration terms and reduces to $\partial p/\partial z = -\rho_i g$. Integrating downward from the stress-free surface $z=s$, where $p=0$,

$$
p(z) = -\int_s^z \rho_i g\,dz' = \rho_i g\,(s-z),
$$

which is just the weight per unit area of the ice column standing above the depth $z$.
```

In the horizontal, the balance reduces to a local one between the gradient of this pressure, set by the surface slope, and the vertical gradient of the horizontal shear stress. Integrating that balance downward from the stress-free surface gives the shear stress at depth,

$$
\tau_{xz}(z) = -\rho_i g\,(s-z)\,\frac{\partial s}{\partial x},
$$

```{admonition} Derivation
:class: dropdown
At leading order the horizontal momentum balance keeps only the vertical gradient of the shear stress against the horizontal pressure gradient,

$$
\frac{\partial \tau_{xz}}{\partial z} = \frac{\partial p}{\partial x} = \rho_i g\,\frac{\partial s}{\partial x},
$$

where the second equality uses the cryostatic pressure $p=\rho_i g\,(s-z)$, whose horizontal gradient is $\rho_i g\,\partial s/\partial x$. The right-hand side is independent of $z$, so integrating from a depth $z$ up to the surface, where the ice is stress-free and $\tau_{xz}(s)=0$,

$$
\tau_{xz}(s) - \tau_{xz}(z) = \rho_i g\,\frac{\partial s}{\partial x}\,(s-z),
$$

and setting $\tau_{xz}(s)=0$ gives the result.
```

which grows linearly from zero at the surface to its largest value at the bed. Physically, each layer of ice must support, through shear, the downslope weight of all the ice above it. All membrane stresses, the longitudinal and lateral stresses carried in {doc}`stress-balance`, are dropped at this order.

## The velocity profile

Feeding this shear stress into Glen's flow law, written for simple shear as $\partial u/\partial z = 2A\,|\tau_{xz}|^{\,n-1}\tau_{xz}$, and integrating upward from the bed gives the velocity at each depth,

$$
u(z) = u_b + \frac{2A(\rho_i g)^{n}}{n+1}\,\left[H^{\,n+1}-(s-z)^{\,n+1}\right]\left|\frac{\partial s}{\partial x}\right|^{\,n-1}\left(-\frac{\partial s}{\partial x}\right),
$$

```{admonition} Derivation
:class: dropdown
Write $S=\partial s/\partial x$. Substituting $\tau_{xz}=-\rho_i g\,(s-z)\,S$ into the flow law and separating magnitude from sign, with $s-z\ge 0$,

$$
|\tau_{xz}|^{\,n-1}\tau_{xz} = \big[\rho_i g\,(s-z)\,|S|\big]^{\,n-1}\big(-\rho_i g\,(s-z)\,S\big)
= -(\rho_i g)^{n}\,(s-z)^{n}\,|S|^{\,n-1}S,
$$

so that $\partial u/\partial z = -2A(\rho_i g)^{n}(s-z)^{n}|S|^{\,n-1}S$. Integrate upward from the bed $z=b$, where $u=u_b$ and $s-b=H$, using

$$
\int_b^{z}(s-z')^{n}\,dz' = \frac{H^{\,n+1}-(s-z)^{\,n+1}}{n+1},
$$

which gives the profile quoted, with the deformation written as $|S|^{\,n-1}(-S)$ so that the flow points down the surface slope.
```

where $u_b$ is any basal sliding velocity supplied by the friction law of {doc}`../thermomechanics/basal-motion`. The deformation is concentrated near the bed, where the shear stress is largest, so the velocity changes most rapidly there and the profile is nearly uniform through the upper ice. This shape, the Lliboutry profile, matches the deformation measured in deep boreholes reasonably well {cite}`cuffey2010`. Averaging through the thickness gives the depth-averaged velocity,

$$
\bar u = u_b + \frac{2A(\rho_i g)^{n}}{n+2}\,H^{\,n+1}\,\left|\frac{\partial s}{\partial x}\right|^{\,n-1}\left(-\frac{\partial s}{\partial x}\right),
$$

```{admonition} Derivation
:class: dropdown
Average the profile over the thickness, $\bar u = \frac1H\int_b^{s} u\,dz$. The constant $u_b$ averages to itself; only the depth-dependent bracket needs integrating,

$$
\int_b^{s}\!\big[H^{\,n+1}-(s-z)^{\,n+1}\big]\,dz = H^{\,n+1}\!\cdot\! H - \frac{H^{\,n+2}}{n+2} = \frac{n+1}{n+2}\,H^{\,n+2}.
$$

Dividing by $H$ leaves $\frac{n+1}{n+2}H^{\,n+1}$, and the factor $n+1$ cancels the $1/(n+1)$ in the prefactor of $u(z)$, replacing it with $1/(n+2)$.
```

the single result that the shallow-ice approximation contributes to the evolution of an ice sheet. The deformational part depends very steeply on the geometry, growing as the thickness to the power $n+1$ and the surface slope to the power $n$. Because $n\approx3$, a small change in thickness or slope produces a large change in speed, and the velocity is controlled almost entirely by the ice thickness and the surface slope.

```{figure} figures/velocity-profiles-n1-n3.png
:name: fig-velocity-profiles-n
:width: 65%

The velocity profile as a rheology experiment. Fractional horizontal displacement against fractional depth for a linear fluid ($n=1$) and for Glen's law ($n=3$); the larger exponent concentrates the shear near the bed and leaves the upper column riding almost rigidly. Borehole deformation surveys fall in the hatched band, which is the field's vote for $n \approx 3$.
```

The same flow law shapes the velocity across a glacier. In a parabolic valley the shear stress grows toward the margins, so the transverse profile of surface speed is blunt in the middle and drops steeply at the walls, and measured transects show exactly this.

```{figure} figures/athabasca-transverse-velocity.png
:name: fig-athabasca-transverse
:width: 80%

Surface velocity measured by stake triangulation across three sections of Athabasca Glacier, Alberta {cite}`raymond1971`. The profile is the transverse cousin of the $u(z)$ result above, nearly flat across the central half of the glacier and falling to almost nothing at the valley walls.
```

```{admonition} Worked problem: from stress to surface speed
:class: note

A check that the machinery is understood. Take a slab 100 m thick on a slope such that the basal shear stress is $\tau_b = 70$ kPa, with $A = 2\times10^{-16}\ \mathrm{Pa^{-3}\,yr^{-1}}$, $n = 3$, and a frozen bed ($u_b = 0$).

Glen's law gives the shear strain rate at the bed, $\dot\epsilon_{xz} = A\tau_b^{3} \approx 0.07\ \mathrm{yr^{-1}}$, so the velocity gradient there is $\partial u/\partial z = 2\dot\epsilon_{xz} \approx 0.14\ \mathrm{yr^{-1}}$. Integrating the profile through the thickness gives the surface speed, which for a uniform slab reduces to $u_s = \tfrac{2A}{n+1}\,\tau_b^{\,3} H = \tfrac{A}{2}\,\tau_b^{3}H \approx 3.4\ \mathrm{m\,yr^{-1}}$.

The same answer can be reached three ways, analytically as above, by summing $\partial u/\partial z$ over layers in a finite-difference table, or graphically as the area under a plot of strain rate against height above the bed. The lab notebook for this chapter does all three, because the finite-difference version is the seed of every numerical ice-flow model in the later chapters.
```

## The thickness equation

The depth-averaged velocity closes the equation that evolves an ice sheet. Conservation of mass, integrated through the thickness, states that the thickness changes when the flux of ice into a column does not balance the net surface and basal mass gain,

$$
\frac{\partial H}{\partial t} + \frac{\partial}{\partial x}\!\left(\bar u\,H\right) = \dot b,
$$

```{admonition} Derivation
:class: dropdown
Integrate incompressibility $\partial u/\partial x + \partial w/\partial z = 0$ through the thickness from the bed $z=b$ to the surface $z=s$,

$$
\int_b^{s}\frac{\partial u}{\partial x}\,dz + \big[w(s)-w(b)\big] = 0 .
$$

Leibniz's rule moves the derivative outside the first integral, $\int_b^{s}\partial u/\partial x\,dz = \frac{\partial}{\partial x}\!\int_b^s u\,dz - u(s)\frac{\partial s}{\partial x} + u(b)\frac{\partial b}{\partial x} = \frac{\partial(\bar u H)}{\partial x} - u(s)\frac{\partial s}{\partial x} + u(b)\frac{\partial b}{\partial x}$. The vertical velocities follow from the kinematic boundary conditions, which state that the surface and bed move with the ice plus their mass exchange, $w(s) = \frac{\partial s}{\partial t} + u(s)\frac{\partial s}{\partial x} - a$ and $w(b) = \frac{\partial b}{\partial t} + u(b)\frac{\partial b}{\partial x} + m$. Substituting, the slope terms cancel in pairs and, for a fixed bed $\partial b/\partial t = 0$ with $H=s-b$, what remains is $\frac{\partial H}{\partial t} + \frac{\partial(\bar u H)}{\partial x} = a - m = \dot b$.
```

where the balance function $\dot b=a-m$ is the net rate of accumulation minus melt, the subject of {doc}`mass-balance`. Substituting the shallow-ice expression for $\bar u$ turns this into a single nonlinear diffusion equation for the surface, cheap enough to integrate over whole glacial cycles, which is why the shallow-ice approximation underlies most paleo-ice-sheet models. Its steady solution forced by a uniform accumulation rate, the Vialov profile, ties the shape of an ice sheet to the climate that feeds it, and is derived alongside the mass balance in {doc}`mass-balance`. One steady shape, however, needs no climate at all, and it follows directly from the rheology.

## The perfect-plastic limit

As the exponent $n$ grows the ice deforms more and more abruptly once the stress reaches a critical value and barely at all below it, and in the limit $n\to\infty$, with $A^{-1/n}\to\tau_i$, the flow law becomes that of a perfectly plastic solid with a yield stress $\tau_i$. This is the oldest idealization of an ice sheet {cite}`nye1952`. If the bed everywhere supports exactly the yield stress, the shallow-ice driving stress equals $\tau_i$,

$$
-\rho_i g\,H\,\frac{\partial s}{\partial x}=\tau_i .
$$

On a flat bed, where $s=H$, the product $H\,\partial H/\partial x$ is half the derivative of $H^2$, so

$$
\frac{\partial}{\partial x}\!\left(H^{2}\right)=-\frac{2\tau_i}{\rho_i g},
\qquad\text{equivalently}\qquad
\left|\nabla\!\left(H^{2}\right)\right|=\frac{2\tau_i}{\rho_i g}.
$$

The square of the thickness falls off linearly from the divide, so integrating inward from a margin at $x=L$, where $H=0$, gives

$$
H(x)=H_0^{1/2}\,(L-x)^{1/2},
\qquad
H_0=\frac{2\tau_i}{\rho_i g}\approx 20\ \mathrm{m}.
$$

```{admonition} Derivation
:class: dropdown
The constant-gradient equation $\partial(H^2)/\partial x = -2\tau_i/\rho_i g$ integrates immediately. Taking the margin at $x=L$ with $H(L)=0$ as the lower limit,

$$
H^2(x) - H^2(L) = -\frac{2\tau_i}{\rho_i g}\,(x-L)
\quad\Longrightarrow\quad
H^2(x) = \frac{2\tau_i}{\rho_i g}\,(L-x),
$$

since $H^2(L)=0$. Writing $H_0 = 2\tau_i/\rho_i g$ and taking the square root gives the parabola. With $\tau_i \approx 100$ kPa and $\rho_i g \approx 9\times10^{3}\ \mathrm{Pa\,m^{-1}}$, $H_0$ is about 20 m, so an ice sheet spanning $L=1000$ km reaches $H=\sqrt{20\times10^{6}}\approx 4500$ m near the divide.
```

This parabolic profile is the shape behind the rule of thumb that an ice sheet a thousand kilometres in span stands a few thousand metres high. Because $H^2$ has a constant gradient, the surface is exactly the shape of a heap of dry sand poured onto a table, which is why a pile of sugar in the outline of Antarctica reproduces the real surface so well. The shape depends only on the yield stress and the span, not on the accumulation, which makes it a quick estimate of the thickness of a former ice sheet whose extent is known from its moraines but whose climate is not. Its one flaw is the cusp at the divide, where the slope is infinite; the viscous Vialov profile rounds it off.

## When the approximation holds

The shallow-ice approximation is excellent in the slow interior of an ice sheet, where the flow really is dominated by vertical shear balanced locally by basal drag, and where stresses are not transmitted far horizontally. It fails exactly where the interesting dynamics happen: ice streams, outlet glaciers, ice shelves, and grounding lines. There the ice slides rapidly, vertical shear is small, and the flow is controlled by the membrane stresses and the long-range stress transmission that the approximation discards. For those regimes a different member of the hierarchy is needed, which is the subject of {doc}`flow-approximations`.
