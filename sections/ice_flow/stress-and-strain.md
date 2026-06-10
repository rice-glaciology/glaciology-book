# Stress and strain in ice

To describe how ice deforms we need the language of continuum mechanics: **stress** (the internal forces) and **strain rate** (the deformation those forces produce). This chapter introduces both, and the combination — *deviatoric stress* — that actually drives flow.

## The stress tensor

Imagine slicing through the ice with a small plane whose orientation is given by the unit normal $\mathbf{n}$. The material on one side exerts a force per unit area, the **traction** $\mathbf{t}$, on the other. Traction depends on the orientation $\mathbf{n}$, and the linear map between them is the **Cauchy stress tensor** $\boldsymbol{\sigma}$:

$$
\mathbf{t} = \boldsymbol{\sigma}\,\mathbf{n}.
$$

In components, $\sigma_{ij}$ is the $i$-th component of traction on a face whose normal points in the $j$-direction. The diagonal entries $\sigma_{11}, \sigma_{22}, \sigma_{33}$ are **normal stresses** (push/pull perpendicular to a face) and the off-diagonal entries are **shear stresses** (forces parallel to a face). Conservation of angular momentum makes the tensor symmetric, $\sigma_{ij} = \sigma_{ji}$, so it has six independent components.

We adopt the convention that tension is positive. The **pressure** is minus the average of the normal stresses,

$$
p = -\tfrac{1}{3}\,\mathrm{tr}(\boldsymbol{\sigma}) = -\tfrac{1}{3}\left(\sigma_{11}+\sigma_{22}+\sigma_{33}\right).
$$

## The strain-rate tensor

Deformation is described by how the velocity field $\bu(\bx,t)$ varies in space. The symmetric part of the velocity gradient is the **strain-rate tensor**,

$$
\dot{\varepsilon}_{ij} = \tfrac{1}{2}\!\left(\frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i}\right).
$$

Its diagonal entries are rates of stretching or compression along the coordinate axes, and its off-diagonal entries are rates of shearing. (The *antisymmetric* part of the velocity gradient describes rigid rotation, which produces no deformation and so does not appear here.)

Glacier ice is, to excellent approximation, **incompressible**: deformation changes shape but not volume. Incompressibility is the statement that the velocity field is divergence-free,

$$
\mathrm{tr}(\dot{\boldsymbol{\varepsilon}}) = \dot\varepsilon_{11} + \dot\varepsilon_{22} + \dot\varepsilon_{33} = \nabla\!\cdot\!\bu = 0.
$$

## Deviatoric stress: what drives flow

Because ice cannot change volume, a uniform pressure cannot make it deform — it only resists compression. What *does* drive flow is the part of the stress that tries to change shape: the **deviatoric stress**, obtained by removing the pressure (the isotropic part) from the full stress tensor,

$$
\tau_{ij} = \sigma_{ij} + p\,\delta_{ij} = \sigma_{ij} - \tfrac{1}{3}\,\mathrm{tr}(\boldsymbol{\sigma})\,\delta_{ij},
$$

where $\delta_{ij}$ is the Kronecker delta. By construction $\boldsymbol{\tau}$ is trace-free, $\mathrm{tr}(\boldsymbol{\tau}) = 0$. It is the deviatoric stress $\boldsymbol{\tau}$, not the full stress $\boldsymbol{\sigma}$, that the rheology of the next chapter relates to strain rate.

## Invariants

A constitutive law must not depend on how we orient our coordinate axes, so it is built from **invariants** of the tensors. The most important is the **second invariant** (the *effective stress* and *effective strain rate*),

$$
\tau_E = \sqrt{\tfrac{1}{2}\,\tau_{ij}\tau_{ij}}, \qquad
\dot\varepsilon_E = \sqrt{\tfrac{1}{2}\,\dot\varepsilon_{ij}\dot\varepsilon_{ij}},
$$

using the summation convention. These scalars measure the overall magnitude of shape-changing stress and deformation, and they are exactly the quantities that appear in Glen's flow law. For the full development see {cite}`cuffey2010`, Chapter 3, or {cite}`greve2009`.
