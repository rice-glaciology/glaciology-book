# Ice flow, accumulation and ablation

A glacier is a budget. Ice is added in some places and removed in others, and flow carries ice between them. Whether the glacier grows or shrinks depends on whether that budget balances.

## Accumulation and ablation

**Accumulation** is everything that adds mass: mostly snowfall, but also refreezing of meltwater and, on ice shelves, freezing at the base. **Ablation** is everything that removes it: surface and basal melt, sublimation, and — for marine-terminating glaciers — iceberg **calving**. The net of the two, expressed as a rate of ice-equivalent thickness change, is the **surface mass balance** $\dot a$ (positive where accumulation wins, negative where ablation wins).

On a typical mountain glacier or ice sheet, $\dot a$ is positive at high elevation (the *accumulation zone*) and negative at low elevation (the *ablation zone*). The line separating them, where $\dot a = 0$, is the **equilibrium line**. Without flow, the accumulation zone would grow ever thicker and the ablation zone would vanish. Flow prevents this by continuously transporting ice from where it is gained to where it is lost.

## Conservation of mass

Make this precise by conserving mass in a vertical column of ice. Let $H(\bx, t)$ be the ice thickness and let

$$
\mathbf{q} = \bar{\bu}\, H
$$

be the **ice flux**, the depth-integrated horizontal flow, where $\bar{\bu}$ is the depth-averaged horizontal velocity. Balancing the rate of change of thickness against the divergence of flux and the local mass source gives the **depth-integrated mass-conservation equation**,

$$
\frac{\partial H}{\partial t} = \dot a - \nabla\!\cdot\!\mathbf{q}
            = \dot a - \nabla\!\cdot\!\left(\bar{\bu}\, H\right).
$$

Read this physically: the thickness at a point changes because mass is added or removed locally ($\dot a$) and because flow carries mass toward or away from the point ($-\nabla\!\cdot\!\mathbf{q}$). Where the flux *converges* ($\nabla\!\cdot\!\mathbf{q} < 0$) ice piles up; where it *diverges*, ice thins.

```{admonition} Steady state
:class: note
A glacier is in **steady state** when $\partial H/\partial t = 0$ everywhere, so that $\nabla\!\cdot\!(\bar{\bu} H) = \dot a$: flow exactly redistributes the mass that accumulation and ablation add and remove. Real ice sheets are rarely in perfect steady state, and the sign and pattern of $\partial H/\partial t$ — measurable from satellite altimetry — is one of the most important diagnostics of ice-sheet health.
```

This single equation is why ice flow matters for sea level. To predict how an ice sheet's thickness — and therefore its contribution to the ocean — evolves, we need $\bar{\bu}$. Everything that follows is, in one way or another, about how to find it. The remaining ingredient is a physical relationship between the forces in the ice and the velocity they produce, which is the subject of the next two chapters. See {cite}`cuffey2010`, Chapter 8, for a fuller discussion.
