# Basal sliding and friction laws

The velocity measured at the surface of a glacier is the sum of two contributions. One is the internal deformation of the ice column governed by the flow law of {doc}`../ice_flow/ice-rheology`. The other is basal motion, the bodily movement of the ice over or with the material at its bed. In the slow interior of an ice sheet, deformation dominates. In the ice streams and outlet glaciers that discharge most of the ice reaching the ocean, basal motion dominates, and it is the largest single source of uncertainty in projections of ice-sheet change. The borehole measurements of Ryser and colleagues in west Greenland, for instance, found basal motion contributing the majority of a surface speed of about 75 metres per year. This chapter develops the laws used to represent that motion. The classical material is in Chapter 7 of {cite}`cuffey2010`; the modern hierarchy of friction laws follows the synthesis of {cite}`hewitt_karthaus`.

## The friction law as a boundary condition

A model of ice flow needs a condition at the bed that relates the basal shear stress the bed exerts on the ice, $\tau_b=|\boldsymbol{\tau}_b|$, to the speed at which the ice slides over it, $u_b=|\mathbf{u}_b|$. Written generally,

$$
\boldsymbol{\tau}_b = f(u_b,\dots)\,\frac{\mathbf{u}_b}{u_b},
$$

where $\boldsymbol{\tau}_b$ is the vector basal shear stress, $u_b=|\mathbf{u}_b|$ the sliding speed, and $f(u_b,\dots)$ a friction function that may depend on the speed and on further variables such as the effective pressure. The scalar $f$ sets the magnitude of the drag, while the unit vector $\mathbf{u}_b/u_b$ fixes its direction, so the stress opposes the sliding and the whole expression is a parameterization of all the small-scale processes near the bed that the model does not resolve. Historically it was thought of as a sliding law giving the speed as a function of stress, $u_b=F(\tau_b)$, but that form can be multivalued, and the modern view writes it as a friction law giving the stress as a function of the speed, $\tau_b=f(u_b,\dots)$, which is single valued and better suited to the way models are posed. The thermal state of the bed, established in {doc}`thermal-structure`, sets the two limiting cases. Where the bed is frozen the ice does not slide, $u_b=0$, and the friction law is a vertical line in the stress-speed plane. Where the ice is afloat the bed exerts no traction, $\tau_b=0$. Everything interesting lies between, and which physics fills that gap depends on whether the bed is hard rock or soft sediment, and on how much water is present.

In the shallow-ice limit of {doc}`../ice_flow/shallow-ice` the basal shear stress is just the driving stress, $\tau_b=-\rho_i g H\,\nabla s$, so the friction law closes the problem by tying that stress to the sliding speed. The chapters that follow build the candidate forms of $f$ from the physics of the bed.

## Hard-bed sliding

Over a bed of hard rock a film of water a few microns thick separates ice from rock, so at the scale of individual grains the ice slips freely. Resistance to sliding is generated instead by the roughness of the bed: the ice must deform to pass over bumps. {cite}`weertman1957` showed that it does so by two mechanisms acting together.

The first is viscous creep. The ice flows around an obstacle by deforming, and a scaling estimate with Glen's law gives a sliding speed

$$
u_v \approx \frac{a A}{2^n}\,\frac{\tau_b^{\,n}}{\nu^{2n}},
$$

where $a$ is the height of a representative bump, $\nu=a/l$ is the bed roughness, the ratio of bump height to bump spacing, and $A$ and $n$ are the flow-law parameters. Because creep depends on a high power of stress, this mechanism is effective at passing the large bumps.

```{admonition} Derivation
:class: dropdown
This is a dimensional scaling estimate after {cite}`weertman1957`, not an exact solution of the creep problem. The basal shear stress $\tau_b$ acts over the bed and is concentrated onto the bumps, which occupy a fraction of order $\nu^2 = (a/l)^2$ of the area, so the local deviatoric stress driving creep around an obstacle scales as $\sigma \sim \tau_b/\nu^2$. Glen's flow law gives a strain rate $\dot\varepsilon \sim A\,\sigma^n \sim A\,(\tau_b/\nu^2)^n$. The ice must deform over the length scale of the bump, height $a$, to flow past it, so the sliding velocity that this strain rate produces is of order $u_v \sim a\,\dot\varepsilon$. Collecting the factors,

$$
u_v \sim a\,A\left(\frac{\tau_b}{\nu^2}\right)^{\!n} = a\,A\,\frac{\tau_b^{\,n}}{\nu^{2n}},
$$

which matches the printed scaling up to the order-unity geometric constant $2^{-n}$ that a fuller treatment of the stress concentration supplies. The key dependences are $u_v \propto a$ (larger bumps are passed faster by creep) and the high power $\tau_b^{\,n}$.
```

The second mechanism is regelation. The ice presses harder on the upstream face of a bump than on the downstream face, and since the melting point falls with pressure the upstream face is slightly colder. Ice melts on the high-pressure side, the meltwater flows around the bump, and it refreezes on the low-pressure side, releasing latent heat that conducts back through the bump. Balancing the conductive and latent heat fluxes gives

$$
u_R \approx \frac{k\,\Gamma}{\rho_i L\,a}\,\frac{\tau_b}{\nu^{2}},
$$

where $k$ is the thermal conductivity, $L$ the latent heat of fusion, $\rho_i$ the ice density, $\Gamma$ the slope of the pressure-melting relation, $a$ the bump height, and $\nu$ the bed roughness as before. The group $k\Gamma/\rho_i L a$ measures how readily the heat released by refreezing can conduct back through a bump of height $a$ to drive the melt on its upstream face, and the factor $\tau_b/\nu^2$ is the stress concentrated onto the bump that sets the pressure, and hence the melting-point, contrast across it. Because heat conduction through a small bump is quick, regelation is effective at passing the small bumps.

```{admonition} Derivation
:class: dropdown
This is again a scaling estimate, balancing the latent heat released by refreezing against the heat conducted back through the obstacle. The stress concentrated on a bump, $\sigma \sim \tau_b/\nu^2$, raises the pressure on its upstream face and lowers it on the lee face, a pressure difference $\Delta p \sim \tau_b/\nu^2$ across the obstacle. Through the Clausius-Clapeyron slope $\Gamma = \mathrm{d}T_m/\mathrm{d}p$, this sets a temperature difference $\Delta T \sim \Gamma\,\tau_b/\nu^2$ between the two faces.

That temperature difference drives a conductive heat flux through the bump. Over a bump of height $a$ the temperature gradient between the two faces is of order $\Delta T/a$, so the heat conducted from the warm lee side back to the cold stoss side is $\sim k\,\Delta T/a$ per unit area. This heat melts ice on the upstream face at a rate set by the latent heat $\rho_i L$ per unit volume, and the melt-refreeze cycle advances the ice past the bump at a regelation speed

$$
u_R \sim \frac{k\,\Delta T}{\rho_i L\,a} \sim \frac{k\,\Gamma}{\rho_i L\,a}\,\frac{\tau_b}{\nu^2},
$$

the printed scaling. The contrast with creep is in the bump size: $u_R \propto 1/a$, so regelation passes the small bumps fastest, because conduction through a small obstacle is quick, while creep passes the large ones.
```

The two mechanisms have opposite dependence on bump size, $u_v\propto a$ and $u_R\propto 1/a$, so there is a controlling obstacle size at which they are equally effective and the total resistance is greatest, with $a\propto u_b^{-(n-1)/(n+1)}$. Combining the two mechanisms at that worst-case size eliminates $a$ and yields the Weertman sliding law,

$$
\tau_b = \nu^2 R\,u_b^{\,2/(n+1)},
\qquad
R=\left(\frac{\rho_i L}{2 k\,\Gamma A}\right)^{1/(n+1)} .
$$

Here $\tau_b$ is the basal shear stress, $u_b$ the sliding speed, $\nu$ the bed roughness, $n$ the flow-law exponent, and $R$ a coefficient collecting the regelation and creep properties, the ice density $\rho_i$, latent heat $L$, thermal conductivity $k$, pressure-melting slope $\Gamma$, and rate factor $A$. The factor $\nu^2$ carries the bed geometry, the coefficient $R$ carries the material physics of the two sliding mechanisms, and the power $u_b^{2/(n+1)}$ is how the resistance grows with sliding speed once the controlling bump size has been chosen. For $n=3$ the exponent is $2/(n+1)=1/2$, so the hard-bed law takes the familiar power-law form $\tau_b=C\,u_b^{m}$ with $m\approx 1/2$, the stress rising with the square root of the sliding speed.

```{admonition} Derivation
:class: dropdown
The two mechanisms act in series on bumps of a given size and add as velocities, $u_b \approx u_v + u_R$, with the scalings

$$
u_v \sim a\,A\,\frac{\tau_b^{\,n}}{\nu^{2n}},
\qquad
u_R \sim \frac{k\,\Gamma}{\rho_i L\,a}\,\frac{\tau_b}{\nu^{2}} .
$$

Weertman's argument is that the bed resists most through the obstacle size at which the two contributions are equal, because larger bumps are passed easily by creep and smaller ones by regelation, leaving the intermediate, controlling size to carry the resistance. Set $u_v = u_R$ to find that size. Equating,

$$
a\,A\,\frac{\tau_b^{\,n}}{\nu^{2n}} \sim \frac{k\,\Gamma}{\rho_i L\,a}\,\frac{\tau_b}{\nu^{2}}
\;\Rightarrow\;
a^2 \sim \frac{k\,\Gamma}{\rho_i L\,A}\,\frac{\nu^{2n-2}}{\tau_b^{\,n-1}} ,
$$

so the controlling size shrinks with sliding stress, $a \propto \tau_b^{-(n-1)/2}$, equivalently $a\propto u_b^{-(n-1)/(n+1)}$ once $\tau_b(u_b)$ is found below.

At that size the sliding speed equals either contribution, so use $u_b \sim u_R \sim u_v$. Multiply the two scalings to eliminate $a$, since $a$ enters $u_v$ as $a^{+1}$ and $u_R$ as $a^{-1}$,

$$
u_b^2 \sim u_v\,u_R
\sim \left(a\,A\,\frac{\tau_b^{\,n}}{\nu^{2n}}\right)\!\left(\frac{k\,\Gamma}{\rho_i L\,a}\,\frac{\tau_b}{\nu^{2}}\right)
= \frac{A\,k\,\Gamma}{\rho_i L}\,\frac{\tau_b^{\,n+1}}{\nu^{2n+2}} ,
$$

the bump height cancelling exactly. Solving for $\tau_b$,

$$
\tau_b^{\,n+1} \sim \frac{\rho_i L}{A\,k\,\Gamma}\,\nu^{2n+2}\,u_b^2
\;\Rightarrow\;
\tau_b \sim \nu^2\left(\frac{\rho_i L}{A\,k\,\Gamma}\right)^{1/(n+1)} u_b^{\,2/(n+1)} .
$$

Collecting the constant into $R = \left(\rho_i L/2k\Gamma A\right)^{1/(n+1)}$, where the factor of two carries the geometric constants suppressed in the scalings, gives the printed Weertman law $\tau_b = \nu^2 R\,u_b^{\,2/(n+1)}$.
```

The roughness enters through $\nu^2$, which is why a smoother bed slides faster for the same stress.

## Sliding with cavitation

The hard-bed law assumes the ice stays in contact with the whole bed. At low effective pressure it does not. Where the water pressure $p_w$ at the bed is high, the pressure on the downstream face of a bump can fall to $p_w$ and the ice separates from the rock, opening a water-filled cavity in the lee of the bump. The friction law then depends not only on the sliding speed but on the effective pressure,

$$
N=p_i-p_w,
$$

the difference between the ice overburden pressure and the water pressure. {cite}`lliboutry1968` and {cite}`iken1981` worked out the consequences. As cavities grow they progressively drown the bed roughness, removing the obstacles that resist sliding, so the bed cannot supply more than a maximum shear stress

$$
\tau_b \le \mu N,
$$

the Iken bound, where $\mu$ is a coefficient set by the steepest bedrock slope.

```{admonition} Derivation
:class: dropdown
This bound is a geometric limit on how much traction a cavitated hard bed can supply, derived by {cite}`iken1981`; it is not fitted but follows from a force balance once cavities have drowned all but the steepest faces. Consider the limiting state in which the only ice-rock contact remaining is on the steepest up-glacier-facing bedrock slopes, inclined at the maximum angle whose tangent is $\mu$. Across the cavities the ice exerts only the water pressure $p_w$; on the contact faces it exerts a normal stress $\sigma_n$.

Resolve the force balance on the bed. The vertical balance requires the contact faces plus the cavity water to support the ice overburden $p_i$, while the horizontal drag the bed can return is the down-glacier component of the normal stress on the contact faces. For a face at angle $\theta$ to the horizontal, the ratio of the horizontal (resisting) to the vertical (supporting) component of the contact stress is $\tan\theta$. The drag is largest when the supporting contact is concentrated on the steepest available faces, $\tan\theta = \mu$. Writing the net supporting load as the effective pressure $N = p_i - p_w$, the maximum horizontal traction is

$$
\tau_b \le \mu\,(p_i - p_w) = \mu N .
$$

Once the sliding speed is high enough that cavities reach this configuration, the bed cannot supply more shear stress regardless of how fast the ice slides, because there is no steeper face to push against. The coefficient $\mu$ is therefore a property of the bedrock geometry, the tangent of the steepest slope, not a fitted friction coefficient.
```

The sliding relation therefore rises with speed at first, in the Weertman manner, and then falls back toward the Coulomb ceiling $\mu N$ once cavities dominate, which makes the underlying $u_b(\tau_b)$ relation double valued. Laboratory ring-shear experiments that drag ice over a sinusoidal bed reproduce this rise and fall {cite}`hewitt_karthaus`.

Two friction laws are in common use that capture this behaviour while remaining single valued in $\tau_b(u_b)$. The first keeps the resistance growing with speed without bound, arguing that there is always some larger bump to take up the stress. This is the generalized Weertman, or Budd, law {cite}`budd1979`,

$$
\tau_b = C\,u_b^{\,p}\,N^{\,q},
$$

where $\tau_b$ is the basal shear stress, $u_b$ the sliding speed, $N$ the effective pressure, $C$ a friction coefficient, and $p$ and $q$ positive exponents. The factor $u_b^{\,p}$ is the Weertman-like rise of drag with sliding speed, while the added factor $N^{\,q}$ encodes the effective-pressure dependence and so makes the bed weaker when the water pressure is high and $N$ is small.

```{admonition} Derivation
:class: dropdown
This is a phenomenological generalization rather than a derived result. {cite}`budd1979` took the Weertman power law $\tau_b = C\,u_b^{\,p}$ and appended a factor $N^{\,q}$ to encode the empirical observation that sliding accelerates as the effective pressure falls toward flotation, the behaviour seen in the borehole records of Iken and others. The exponents $p$ and $q$ and the coefficient $C$ are fitted, not predicted; common choices set $p = 1/n$ to recover the Weertman exponent and take $q$ positive so that the bed weakens as $N\to 0$. The form has no built-in ceiling on stress, which is its defining contrast with the regularized Coulomb law below: it assumes there is always a larger obstacle to take up additional stress, so $\tau_b$ grows without bound as the speed rises.
```

The second enforces the Iken ceiling, letting the stress rise monotonically toward $\mu N$. This is the regularized Coulomb law {cite}`schoof2005,gagliardini2007,tsai2015`,

$$
\tau_b = \mu N\left(\frac{u_b}{u_b+\lambda N^{\,n}}\right)^{1/n}.
$$

Here $\mu$ is the friction coefficient, $N$ the effective pressure, $u_b$ the sliding speed, $n$ the flow-law exponent, and $\lambda$ a parameter setting the transition speed. The prefactor $\mu N$ is the Iken Coulomb ceiling the stress cannot exceed, and the bracketed ratio is a throttle that rises from zero toward one as the speed climbs, so the drag interpolates smoothly from a power law at low speed to the ceiling at high speed. At low speed, $u_b\ll\lambda N^n$, this reduces to a Weertman-like power law $\tau_b\approx\mu(\lambda^{-1}u_b)^{1/n}$ that is nearly independent of $N$, while at high speed, $u_b\gg\lambda N^n$, it saturates at the Coulomb value $\mu N$. The single parameter $\lambda$ sets the transition.

```{admonition} Derivation
:class: dropdown
The form itself is a phenomenological interpolation, constructed by {cite}`schoof2005,gagliardini2007,tsai2015` to join the two known limits, a Weertman power law at low speed and the Iken Coulomb ceiling at high speed, in a single expression that is smooth and single-valued. It is not derived from the bed mechanics; rather, it is the simplest function with the required asymptotics, and the two limits can be read off directly.

Take the printed law

$$
\tau_b = \mu N\left(\frac{u_b}{u_b+\lambda N^{\,n}}\right)^{1/n} .
$$

At low speed, $u_b \ll \lambda N^n$, the denominator is dominated by $\lambda N^n$, so

$$
\tau_b \approx \mu N\left(\frac{u_b}{\lambda N^{\,n}}\right)^{1/n}
= \mu N\,\frac{u_b^{\,1/n}}{\lambda^{1/n} N}
= \mu\left(\frac{u_b}{\lambda}\right)^{1/n},
$$

the effective pressure cancelling to leave a Weertman-like power law with exponent $1/n$, nearly independent of $N$. At high speed, $u_b \gg \lambda N^n$, the ratio inside the bracket tends to one, so

$$
\tau_b \to \mu N,
$$

the Iken Coulomb ceiling. The crossover occurs where $u_b \sim \lambda N^n$, so $\lambda$ alone fixes the transition speed.
```

This form has become standard for modelling fast flow near grounding lines, because the Coulomb ceiling is exactly what allows a grounding line to thin and accelerate without the bed supplying ever-larger resistance.

## Soft-bed sliding

Several of the large Antarctic ice streams sit on a layer of weak, water-saturated sediment called till, produced by glacial erosion of the bed. Laboratory shear tests on till samples show that it behaves not as a viscous fluid but as a plastic material with a yield strength {cite}`iverson1998`,

$$
\tau_f = \mu\,\sigma_e, \qquad \sigma_e = p - p_w,
$$

a Coulomb friction law with a coefficient $\mu\approx 0.4$ acting on the effective stress $\sigma_e$, which is again the overburden minus the pore-water pressure.

```{admonition} Derivation
:class: dropdown
This is the Mohr-Coulomb failure criterion of soil mechanics, measured rather than derived. In a granular material the shear strength along a failure plane is set by the frictional contact between grains, which carry only the part of the normal load not borne by the pore water. That load is the effective stress $\sigma_e = p - p_w$, the total overburden $p$ minus the pore-water pressure $p_w$, since water pressure pushes the grains apart and unburdens the contacts. The shear strength is proportional to the load actually pressing the grains together,

$$
\tau_f = c + \mu\,\sigma_e ,
$$

with $\mu = \tan\varphi$ the internal-friction coefficient ($\varphi$ the friction angle) and $c$ a cohesion. For the nearly cohesionless subglacial tills tested by {cite}`iverson1998`, $c\approx 0$ and $\mu\approx 0.4$, giving the printed $\tau_f = \mu\,\sigma_e$. The value of $\mu$ is a laboratory result for the specific sediment, not a quantity predicted from first principles. The decisive experimental finding is that $\tau_f$ depends on $\sigma_e$ but barely on the rate of shearing, so the till is to good approximation perfectly plastic.
```

The decisive observation is that once the till yields, the stress it supports is almost independent of the rate of shearing. The till is, to a good approximation, perfectly plastic, so the basal shear stress is simply

$$
\tau_b = \mu N,
$$

independent of sliding speed. Ring-shear experiments confirm this plateau and show how it arises: at low effective pressure or low speed the ice slips along the ice-till interface, while at higher stress the larger clasts plough through a deforming layer of till, with the depth of deforming sediment varying non-monotonically with effective pressure {cite}`zoet2020`. The practical consequence is that a till bed has no reserve of strength. If it is asked to support more than $\mu N$ it cannot, and the extra driving stress must be transmitted elsewhere, to the lateral margins or across the grounding line. Because the regularized Coulomb law of the previous section also saturates at $\mu N$, it is often used to represent both hard beds with cavities and soft till beds within a single expression.

The field evidence that till actually deforms came first from Iceland, where markers inserted through the ice into the bed of Breiðamerkurjökull were found displaced down-glacier days later, with nearly all the motion taken up in the upper half metre of sediment.

```{figure} figures/till-deformation-breidamerkurjokull.png
:name: fig-till-deformation
:width: 95%

Marker columns in the till beneath Breiðamerkurjökull, Iceland, shown at three stages over ten days of flow. The upper till (A) shears pervasively while the lower till (B) barely moves, so the glacier rides on a deforming carpet of sediment rather than slipping on a discrete surface. After Boulton and Hindmarsh, as redrawn in {cite}`benn2010`.
```

## The controlling role of water

Every law beyond the simplest hard-bed power law depends on the effective pressure $N$, and through it on the subglacial water system. When the water pressure rises toward the ice overburden, $N$ falls, the bed is partly floated, and the glacier slides faster; when the water drains and $N$ recovers, the bed strengthens. This is why the same glacier can speed up and slow down within a single melt season. Field measurements bear out the coupling but also show its complexity. Some records, such as those of Iken and Bindschadler, show ice speed tracking borehole water pressure closely, while others show no consistent relation. In west Greenland the diurnal swings of ice speed correlate with water pressure in moulins yet run out of phase with pressure in nearby boreholes, a sign that the bed is drained by more than one kind of pathway at once {cite}`hewitt_karthaus`. What sets $N$, and why the drainage system can be efficient at one moment and inefficient the next, is the subject of {doc}`hydrology`. The friction law and the hydrology are two halves of one problem.

```{figure} figures/iken-sliding-water-level.png
:name: fig-iken-sliding
:width: 55%

Sliding speed against borehole water level (depth below the surface, so pressure increases to the right) at Findelengletscher in the early 1980s, from A. Iken's borehole campaigns. Speed climbs steeply as the water level approaches flotation, the empirical backbone of every $N$-dependent friction law in this chapter.
```

```{figure} figures/storglaciaren-pressure-speed.png
:name: fig-storglaciaren-speed
:width: 75%

A month of borehole water pressure (dashed) and surface speed (solid) at Storglaciären, Sweden, in July 1993 {cite}`hanson1998`. The glacier accelerates within hours of each pressure rise and settles as the bed drains, the friction law and the hydrology trading control on a daily clock.
```

## Friction laws in models

In a numerical ice-sheet model the friction law is rarely used with its physical coefficients. Instead the coefficient $C$ in a law such as $\boldsymbol{\tau}_b=C\,|\mathbf{u}_b|^{m-1}\mathbf{u}_b$ is treated as a spatially varying field and chosen, by an inverse method, so that the modelled surface velocity matches the observed one. The inferred coefficient then encodes everything about the bed that the model cannot resolve, and maps of it across Antarctica and Greenland reveal the slippery beds beneath the ice streams as bands of low friction. Two cautions come with this practice. The bed properties the coefficient stands for can change in time, for example as the water system evolves, so a coefficient fitted to one snapshot need not hold for another. And because the friction law represents unresolved processes, both the appropriate form of the law and the value of its coefficients depend on the resolution of the model. The inversion is taken up again in the modelling chapters, where the cost function that defines it is written out.
