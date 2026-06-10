# Ice rheology: Glen's flow law

A **rheology**, or constitutive law, is the relationship between the stress applied to a material and the deformation that results. For ice, the empirical law that has organized the field for seventy years comes from the laboratory creep experiments of {cite}`glen1955`. It is the equation that closes the system: combined with conservation of momentum, it lets us predict how ice flows.

## Glen's flow law

Glen found that the rate at which ice deforms increases as a **power** of the applied deviatoric stress. In its tensor form, the strain-rate tensor is aligned with the deviatoric-stress tensor,

$$
\dot\varepsilon_{ij} = A\,\tau_E^{\,n-1}\,\tau_{ij},
$$

where $\boldsymbol{\tau}$ is the deviatoric stress, $\tau_E$ is the effective stress from the previous chapter, $n$ is **Glen's exponent**, and $A$ is the **rate factor** (or *fluidity*). For most glacier ice $n \approx 3$, so the strain rate depends on stress *cubed*: doubling the stress makes ice deform roughly eight times faster. This strong nonlinearity is the defining feature of ice flow — it is why fast-flowing regions concentrate into narrow streams and why small changes in driving stress can produce large changes in speed.

Equivalently, the law can be written as an effective relationship between the second invariants,

$$
\dot\varepsilon_E = A\,\tau_E^{\,n}.
$$

## Temperature dependence: the rate factor

The rate factor $A$ is **strongly temperature dependent** — warm ice is far softer than cold ice. Its variation follows an Arrhenius law,

$$
A(T) = A_0\,\exp\!\left(-\frac{Q}{R\,T}\right),
$$

where $T$ is absolute temperature, $Q$ is the **activation energy** for creep, $R$ is the gas constant, and $A_0$ is a constant. Near the melting point $A$ rises sharply (the activation energy itself increases above about $-10^\circ$C), so ice within a few degrees of melting can deform an order of magnitude faster than cold polar ice. Because the deep ice in an ice sheet is generally warmer than the surface, most internal deformation happens near the bed. In practice $A$ also depends on impurities, water content, and crystal-fabric anisotropy, which are folded into an empirical *enhancement factor*.

## Viscosity form

Glen's law is a **nonlinear viscous** rheology, and it is often convenient to write it like a viscous fluid, $\tau_{ij} = 2\,\eta\,\dot\varepsilon_{ij}$, with an effective viscosity that depends on the strain rate,

$$
\eta = \tfrac{1}{2}\,A^{-1/n}\,\dot\varepsilon_E^{\,(1-n)/n}.
$$

For $n>1$ the viscosity *decreases* as the strain rate increases: ice is **shear-thinning**. This viscosity form is exactly what numerical models use, because it casts the flow law as a (nonlinear) viscous stress–strain-rate relationship that can be inserted into a momentum balance and solved.

```{admonition} Where this is heading
:class: tip
We now have all the physics we need: conservation of mass ({doc}`mass-balance`), the kinematics of stress and strain ({doc}`stress-and-strain`), and a rheology relating the two (this chapter). Closing the system requires one more equation — conservation of momentum (force balance) — and then solving it for the velocity field. Doing that analytically is only possible in idealized cases, so in the next part we solve it **numerically** with icepack.
```

See {cite}`cuffey2010`, Chapter 3, for the experimental basis of the flow law and the values of $n$, $A$, and $Q$.
