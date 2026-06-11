# Ice flow, accumulation, and ablation

A glacier is a budget. Ice is added in some places and removed in others, and flow carries ice between them. Whether the glacier grows or shrinks depends on whether that budget balances. This chapter sets out the budget, the conservation law that expresses it, and the steady ice-sheet shape that a given climate produces, which is the first and cleanest connection between climate and ice flow. The treatment follows Chapter 8 of {cite}`cuffey2010`.

## Accumulation and ablation

Accumulation is everything that adds mass to the ice. It is mostly snowfall, but it also includes the refreezing of meltwater and, beneath ice shelves, freezing of ocean water onto the base. Ablation is everything that removes mass: surface and basal melt, sublimation, and, for glaciers that end in the ocean, the calving of icebergs. The net of the two, expressed as a rate of ice-equivalent thickness change, is the surface mass balance $\dot a$, positive where accumulation wins and negative where ablation wins.

```{figure} figures/penitentes-atacama.jpeg
:name: fig-penitentes
:width: 95%

Ablation is not always gentle melt. Penitentes in the high, dry Andes near the Atacama Desert, metre-scale blades carved where sublimation dominates the surface energy budget; the spikes grow because hollows concentrate reflected light and deepen preferentially. Sublimation costs nearly ten times the latent heat of melting, a price set by the hydrogen bonds of {doc}`../foundations/water-molecule`. Photograph: ESO (eso.org).
```

On a typical mountain glacier or ice sheet the balance is positive at high elevation, in the accumulation zone, and negative at low elevation, in the ablation zone. The line between them, where $\dot a=0$, is the equilibrium line, and its altitude is one of the most sensitive recorders of climate a glacier has. Without flow the accumulation zone would thicken without limit while the ablation zone wasted away. Flow prevents this by carrying ice continuously from where it is gained to where it is lost, and the speed at which it must do so to hold the glacier in balance is set by the budget.

```{figure} figures/blue-glacier-balance-gradient.jpeg
:name: fig-blue-glacier-gradient
:width: 80%

The mass-balance gradient measured. Specific net balance against elevation for seven years on Blue Glacier, Washington, from stake and pit surveys. Each curve crosses zero at that year's equilibrium line, near 1600–2000 m, and the spread between wet and dry years shows how the whole profile, not just the ELA, shifts with climate.
```

## Conservation of mass

To make the budget precise, conserve mass in a vertical column of ice. Let $H(\mathbf{x},t)$ be the ice thickness and let

$$
\mathbf{q} = \bar{u}\,H
$$

be the ice flux, the depth-integrated horizontal flow, with $\bar{u}$ the depth-averaged horizontal velocity of {doc}`shallow-ice`. Balancing the rate of change of thickness against the divergence of this flux and the local mass source gives the depth-integrated mass-conservation equation,

$$
\frac{\partial H}{\partial t} = \dot a - \nabla\!\cdot\!\mathbf{q}
            = \dot a - \nabla\!\cdot\!\left(\bar{u}\,H\right).
$$

Read physically, the thickness at a point changes for two reasons: mass is added or removed locally through $\dot a$, and flow carries mass toward or away from the point through the flux divergence. Where the flux converges the ice piles up, and where it diverges the ice thins. A glacier is in steady state when the thickness holds fixed everywhere, so that $\nabla\!\cdot\!(\bar u H)=\dot a$, and flow exactly redistributes the mass that accumulation and ablation add and remove. Real ice sheets are rarely in perfect balance, and the pattern of $\partial H/\partial t$, now measured directly by satellite altimetry, is among the most important diagnostics of an ice sheet's health.

This single equation is why ice flow matters for sea level. To predict how an ice sheet's thickness, and therefore its contribution to the ocean, evolves, the depth-averaged velocity $\bar u$ is needed, and supplying it is what the rheology and the momentum balance of the earlier chapters are for.

## The shape of an ice sheet in balance

The conservation law and the flow law together fix the shape an ice sheet settles into under a given climate, and the result is worth deriving because it shows exactly how the accumulation rate controls the ice. Take an ice sheet on a flat bed, with no sliding, spreading symmetrically from a central divide at $x=0$ to a margin at $x=L$, fed by a uniform balance rate $\dot b$. In steady state the thickness is fixed, so the conservation equation reduces to a statement that the flux grows linearly away from the divide,

$$
\frac{\partial}{\partial x}\!\left(\bar u H\right)=\dot b
\quad\Longrightarrow\quad
\bar u H = \dot b\,x .
$$

With the bed flat the surface equals the thickness, and the shallow-ice depth-averaged velocity of {doc}`shallow-ice` gives the flux

$$
\bar u H = \frac{2A(\rho_i g)^n}{n+2}\,H^{\,n+2}\left(-\frac{\partial H}{\partial x}\right)^{n}.
$$

Setting the two expressions for the flux equal, taking the $n$th root, recognizing the left side as the derivative of a power of $H$, and integrating inward from the margin where $H(L)=0$, gives the Vialov profile {cite}`vialov1958`,

$$
H(x)=\left[\frac{2(n+2)^{1/n}}{(2A)^{1/n}\rho_i g}\right]^{\!\frac{n}{2(n+1)}}\dot b^{\,\frac{1}{2(n+1)}}\,L^{1/2}
\left[1-\left(\frac{x}{L}\right)^{\!\frac{n+1}{n}}\right]^{\!\frac{n}{2(n+1)}},
\qquad 0<x<L .
$$

The shape is the smooth dome seen in any cross-section of Greenland or East Antarctica, steep at the margin and nearly flat at the divide. Its lesson is in the exponents. The central thickness grows as $L^{1/2}$, so a wider ice sheet is thicker in proportion to the square root of its span, but only as $\dot b^{\,1/2(n+1)}$, an extremely weak dependence on the climate that feeds it. With $n=3$ the thickness scales as the snowfall to the one-eighth power, so doubling the accumulation thickens the ice sheet by under ten percent. An ice sheet's height is set by how far it spreads, not by how much it snows. This is the simplest prognostic statement the book can make, a steady balance between a climate forcing and an ice flow, and it is the seed of the time-dependent coupling between climate and ice-sheet evolution taken up in the chapters that follow.
