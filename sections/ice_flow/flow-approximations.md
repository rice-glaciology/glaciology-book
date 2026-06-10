# A hierarchy of flow models

The shallow-ice approximation is the simplest member of a **family** of ice-flow models, each defined by which terms of the Stokes equations it keeps. Choosing a model is the central modeling decision in glaciology: it trades physical completeness against computational cost. This chapter lays out the ladder, from the cheapest depth-integrated models to the full Stokes equations, and shows where icepack sits on it.

## The shallow-shelf / shelfy-stream approximation (SSA)

The SSA is, in a sense, the **opposite limit** of the SIA. Instead of assuming flow is dominated by vertical shear, it assumes there is essentially **no vertical shear**: the horizontal velocity is uniform with depth, as it is in fast-sliding ice streams and in floating ice shelves. The driving stress is then balanced by **membrane stresses** — depth-integrated longitudinal and lateral stretching — and, for grounded ice, by basal drag {cite}`macayeal1989`.

In one horizontal dimension the SSA is the elegant equation

$$
\frac{\partial}{\partial x}\!\left(2\,\bar\eta\,H\,\frac{\partial \bar u}{\partial x}\right) - \tau_b = \rho\, g\, H\,\frac{\partial s}{\partial x},
$$

where $\bar u$ is the depth-averaged velocity, $\bar\eta$ the depth-averaged viscosity, and $\tau_b$ the basal drag (zero for a floating shelf). Unlike the SIA, the SSA is **non-local**: because of the stretching term, a perturbation anywhere influences the flow everywhere, which is exactly what lets ice streams and shelves transmit stress across grounding lines. The ice-shelf model we built with icepack in {doc}`../modeling/icepack-ice-shelf` is precisely this equation with $\tau_b = 0$.

## Hybrid models

Real ice sheets contain **both** regimes — shearing interiors and sliding margins — and the transition between them. **Hybrid** models combine the SIA and SSA, summing a sheared and a sliding contribution so that the same model behaves like the SIA where shear dominates and like the SSA where sliding dominates {cite}`bueler2009`. They are the workhorse of continental-scale ice-sheet simulation, and icepack provides a hybrid model for this purpose.

## Higher-order and full-Stokes models

Going up the ladder, **higher-order** models (often called Blatter–Pattyn or "first-order") keep more of the membrane and vertical-shear stresses simultaneously, dropping only the smallest "bridging" terms {cite}`pattyn2003`. They resolve the three-dimensional stress state much more faithfully than the depth-integrated models, at substantially higher cost. At the top of the ladder sits the **full Stokes** system itself — no approximation — which is necessary near grounding lines, ice divides, and steep or rapidly varying terrain, and which is the most expensive of all.

## The ladder at a glance

| Model | Keeps | Drops | Best for | Cost |
|---|---|---|---|---|
| **SIA** | vertical shear, local driving stress | all membrane stresses | slow shearing interiors | lowest |
| **SSA** | membrane (longitudinal + lateral) stresses, basal drag | vertical shear | ice streams, ice shelves | low |
| **Hybrid (SIA+SSA)** | shear *and* membrane stresses (summed) | cross-terms between them | whole ice sheets | low–moderate |
| **Higher-order (Blatter–Pattyn)** | most stress components in 3-D | smallest "bridging" terms | grounding zones, complex flow | high |
| **Full Stokes** | everything | nothing | divides, grounding lines, benchmarks | highest |

```{admonition} How this maps onto icepack
:class: seealso
icepack is organized around exactly this hierarchy. Its `IceShelf` and `IceStream` models are the SSA (membrane) level — the right tool for shelves, streams, and outlet glaciers — and its hybrid model adds vertical shear for thicker, slower ice. Choosing an icepack model *is* choosing a rung on this ladder. The rest of the book builds up a model at the SSA/hybrid level, because that is where the dynamics that matter for sea level — fast flow, grounding-line migration, ice-shelf buttressing — actually live.
```

For the asymptotic theory that unifies these models, see {cite}`schoof2010`; for a textbook treatment, {cite}`cuffey2010` (Ch. 8) and {cite}`greve2009`.
