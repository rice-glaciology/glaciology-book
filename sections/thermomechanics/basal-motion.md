# Basal sliding and friction laws

The velocity measured at the surface of a glacier is the sum of two contributions. One is the internal deformation of the ice column governed by the flow law of {doc}`../ice_flow/ice-rheology`. The other is basal motion, the bodily movement of the ice over or with the material at its bed. In the slow interior of an ice sheet, deformation dominates. In the ice streams and outlet glaciers that discharge most of the ice reaching the ocean, basal motion dominates, and it is the largest single source of uncertainty in projections of ice-sheet change. The borehole measurements of Ryser and colleagues in west Greenland, for instance, found basal motion contributing the majority of a surface speed of about 75 metres per year. This chapter develops the laws used to represent that motion. The classical material is in Chapter 7 of {cite}`cuffey2010`; the modern hierarchy of friction laws follows the synthesis of {cite}`hewitt_karthaus`.

## The friction law as a boundary condition

A model of ice flow needs a condition at the bed that relates the basal shear stress the bed exerts on the ice, $\tau_b=|\boldsymbol{\tau}_b|$, to the speed at which the ice slides over it, $u_b=|\mathbf{u}_b|$. Written generally,

$$
\boldsymbol{\tau}_b = f(u_b,\dots)\,\frac{\mathbf{u}_b}{u_b},
$$

this is a parameterization of all the small-scale processes near the bed that the model does not resolve. Historically it was thought of as a sliding law giving the speed as a function of stress, $u_b=F(\tau_b)$, but that form can be multivalued, and the modern view writes it as a friction law giving the stress as a function of the speed, $\tau_b=f(u_b,\dots)$, which is single valued and better suited to the way models are posed. The thermal state of the bed, established in {doc}`thermal-structure`, sets the two limiting cases. Where the bed is frozen the ice does not slide, $u_b=0$, and the friction law is a vertical line in the stress-speed plane. Where the ice is afloat the bed exerts no traction, $\tau_b=0$. Everything interesting lies between, and which physics fills that gap depends on whether the bed is hard rock or soft sediment, and on how much water is present.

In the shallow-ice limit of {doc}`../ice_flow/shallow-ice` the basal shear stress is just the driving stress, $\tau_b=-\rho_i g H\,\nabla s$, so the friction law closes the problem by tying that stress to the sliding speed. The chapters that follow build the candidate forms of $f$ from the physics of the bed.

## Hard-bed sliding

Over a bed of hard rock a film of water a few microns thick separates ice from rock, so at the scale of individual grains the ice slips freely. Resistance to sliding is generated instead by the roughness of the bed: the ice must deform to pass over bumps. {cite}`weertman1957` showed that it does so by two mechanisms acting together.

The first is viscous creep. The ice flows around an obstacle by deforming, and a scaling estimate with Glen's law gives a sliding speed

$$
u_v \approx \frac{a A}{2^n}\,\frac{\tau_b^{\,n}}{\nu^{2n}},
$$

where $a$ is the height of a representative bump, $\nu=a/l$ is the bed roughness, the ratio of bump height to bump spacing, and $A$ and $n$ are the flow-law parameters. Because creep depends on a high power of stress, this mechanism is effective at passing the large bumps. The second mechanism is regelation. The ice presses harder on the upstream face of a bump than on the downstream face, and since the melting point falls with pressure the upstream face is slightly colder. Ice melts on the high-pressure side, the meltwater flows around the bump, and it refreezes on the low-pressure side, releasing latent heat that conducts back through the bump. Balancing the conductive and latent heat fluxes gives

$$
u_R \approx \frac{k\,\Gamma}{\rho_i L\,a}\,\frac{\tau_b}{\nu^{2}},
$$

where $k$ is the thermal conductivity, $L$ the latent heat, and $\Gamma$ the slope of the pressure-melting relation. Because heat conduction through a small bump is quick, regelation is effective at passing the small bumps.

The two mechanisms have opposite dependence on bump size, $u_v\propto a$ and $u_R\propto 1/a$, so there is a controlling obstacle size at which they are equally effective and the total resistance is greatest, with $a\propto u_b^{-(n-1)/(n+1)}$. Combining the two mechanisms at that worst-case size eliminates $a$ and yields the Weertman sliding law,

$$
\tau_b = \nu^2 R\,u_b^{\,2/(n+1)},
\qquad
R=\left(\frac{\rho_i L}{2 k\,\Gamma A}\right)^{1/(n+1)} .
$$

For $n=3$ the exponent is $2/(n+1)=1/2$, so the hard-bed law takes the familiar power-law form $\tau_b=C\,u_b^{m}$ with $m\approx 1/2$, the stress rising with the square root of the sliding speed. The roughness enters through $\nu^2$, which is why a smoother bed slides faster for the same stress.

## Sliding with cavitation

The hard-bed law assumes the ice stays in contact with the whole bed. At low effective pressure it does not. Where the water pressure $p_w$ at the bed is high, the pressure on the downstream face of a bump can fall to $p_w$ and the ice separates from the rock, opening a water-filled cavity in the lee of the bump. The friction law then depends not only on the sliding speed but on the effective pressure,

$$
N=p_i-p_w,
$$

the difference between the ice overburden pressure and the water pressure. {cite}`lliboutry1968` and {cite}`iken1981` worked out the consequences. As cavities grow they progressively drown the bed roughness, removing the obstacles that resist sliding, so the bed cannot supply more than a maximum shear stress

$$
\tau_b \le \mu N,
$$

the Iken bound, where $\mu$ is a coefficient set by the steepest bedrock slope. The sliding relation therefore rises with speed at first, in the Weertman manner, and then falls back toward the Coulomb ceiling $\mu N$ once cavities dominate, which makes the underlying $u_b(\tau_b)$ relation double valued. Laboratory ring-shear experiments that drag ice over a sinusoidal bed reproduce this rise and fall {cite}`hewitt_karthaus`.

Two friction laws are in common use that capture this behaviour while remaining single valued in $\tau_b(u_b)$. The first keeps the resistance growing with speed without bound, arguing that there is always some larger bump to take up the stress. This is the generalized Weertman, or Budd, law {cite}`budd1979`,

$$
\tau_b = C\,u_b^{\,p}\,N^{\,q},
$$

which adds an effective-pressure dependence to the power law and so makes the bed weaker when the water pressure is high. The second enforces the Iken ceiling, letting the stress rise monotonically toward $\mu N$. This is the regularized Coulomb law {cite}`schoof2005,gagliardini2007,tsai2015`,

$$
\tau_b = \mu N\left(\frac{u_b}{u_b+\lambda N^{\,n}}\right)^{1/n}.
$$

At low speed, $u_b\ll\lambda N^n$, this reduces to a Weertman-like power law $\tau_b\approx\mu(\lambda^{-1}u_b)^{1/n}$ that is nearly independent of $N$, while at high speed, $u_b\gg\lambda N^n$, it saturates at the Coulomb value $\mu N$. The single parameter $\lambda$ sets the transition. This form has become standard for modelling fast flow near grounding lines, because the Coulomb ceiling is exactly what allows a grounding line to thin and accelerate without the bed supplying ever-larger resistance.

## Soft-bed sliding

Not every fast glacier rests on hard rock. Several of the large Antarctic ice streams sit on a layer of weak, water-saturated sediment called till, produced by glacial erosion of the bed. Laboratory shear tests on till samples show that it behaves not as a viscous fluid but as a plastic material with a yield strength {cite}`iverson1998`,

$$
\tau_f = \mu\,\sigma_e, \qquad \sigma_e = p - p_w,
$$

a Coulomb friction law with a coefficient $\mu\approx 0.4$ acting on the effective stress $\sigma_e$, which is again the overburden minus the pore-water pressure. The decisive observation is that once the till yields, the stress it supports is almost independent of the rate of shearing. The till is, to a good approximation, perfectly plastic, so the basal shear stress is simply

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
