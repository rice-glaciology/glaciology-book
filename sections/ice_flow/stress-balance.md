# Momentum balance and the driving stress

We now have the kinematics ({doc}`stress-and-strain`) and the rheology ({doc}`ice-rheology`). The last physical principle we need is **conservation of momentum** — Newton's second law for a continuum. Combined with the flow law, it determines the velocity field. This chapter writes down the full equations and extracts the single most important quantity in ice dynamics: the **gravitational driving stress**.

## Ice flow is a Stokes flow

Newton's second law for a continuum says that the rate of change of momentum equals the sum of the surface forces (the divergence of stress) and the body force (gravity):

$$
\rho\,\frac{D\bu}{Dt} = \nabla\!\cdot\!\boldsymbol{\sigma} + \rho\,\mathbf{g}.
$$

For ice the inertial term on the left is utterly negligible. Glaciers are enormously viscous and move slowly, so the **Reynolds number** is something like $10^{-13}$ — the flow is as far from turbulent as a fluid can be. Dropping inertia leaves the **Stokes equations**,

$$
\nabla\!\cdot\!\boldsymbol{\sigma} + \rho\,\mathbf{g} = 0,
$$

a statement that the forces on every parcel of ice are in *instantaneous balance*. Together with incompressibility $\nabla\!\cdot\!\bu = 0$ and Glen's flow law relating the deviatoric stress $\boldsymbol{\tau}$ to the strain rate, this is the **complete description of glacier flow**. Everything else in this part of the book is an approximation to it.

Writing $\boldsymbol{\sigma} = \boldsymbol{\tau} - p\,\mathbf{I}$ (deviatoric stress minus pressure) makes the structure explicit:

$$
\nabla\!\cdot\!\boldsymbol{\tau} - \nabla p + \rho\,\mathbf{g} = 0.
$$

## The driving stress

The Stokes equations are a coupled, nonlinear, three-dimensional system — too much to solve in your head. But integrating the *horizontal* momentum balance over the ice thickness reveals the force that actually pushes ice downhill. Carrying out that integration (using the surface boundary condition that stress vanishes at the top, and hydrostatic balance for the pressure) yields the **gravitational driving stress**

$$
\boldsymbol{\tau}_d = -\rho\, g\, H\, \nabla s,
$$

where $H$ is the ice thickness, $s$ is the **surface elevation**, and $\nabla s$ is the surface slope. The driving stress points *down the surface slope*, and it grows with both thickness and steepness. It is, to excellent approximation, the engine of all glacier flow.

```{admonition} It's the surface slope that matters
:class: tip
A common surprise: the driving stress depends on the slope of the **upper surface**, not the bed. Ice flows in the direction the *surface* tilts, even where the bed slopes the other way. This is why, to first order, you can predict the direction of ice-sheet flow from a surface elevation map alone.
```

## Balancing the driving stress

Because the ice is in force balance, the driving stress must be opposed by **resistive stresses**. There are three places resistance can come from:

- **Basal drag** — friction at the bed, where the ice is grounded.
- **Lateral drag** — shear against the valley walls or against slower-moving ice on either side.
- **Longitudinal stress gradients** — the push and pull of ice up- and down-stream (membrane stresses).

Schematically, the depth-integrated balance reads

$$
\underbrace{\boldsymbol{\tau}_d}_{\text{driving}} = \underbrace{\boldsymbol{\tau}_b}_{\text{basal}} + \underbrace{\text{(lateral)}}_{} + \underbrace{\nabla\!\cdot\!(\text{membrane stress})}_{\text{longitudinal}}.
$$

Which of these terms dominates depends on the kind of glacier — and that is exactly the choice that defines the different **flow approximations** of the next two chapters. In the slow interior of an ice sheet, vertical shear and basal drag balance the driving stress; in a fast ice stream or a floating shelf, membrane and lateral stresses do. See {cite}`cuffey2010`, Chapter 8, and {cite}`greve2009` for the full derivations.
