# Stress and strain in ice

A deforming glacier has no rigid parts to track, every parcel stretching and shearing along with its neighbors, and describing that kind of motion takes the language of continuum mechanics. Ice is of course made of molecules, but on the scales of glacier flow we treat it as a continuous medium whose state at each point is described by smooth fields: a velocity, a stress, a temperature. This chapter sets out the two tensor fields that the flow law connects, the stress that measures internal force and the strain rate that measures deformation, and the deviatoric stress that links them. The index notation, the symmetric and deviatoric splits, and the eigenvalues and invariants used throughout are collected in {doc}`../math/tensor-algebra`, to which a reader unfamiliar with tensors should turn first. The treatment follows Chapter 3 of {cite}`cuffey2010` and {cite}`greve2009`.

## Eulerian and Lagrangian descriptions

An **Eulerian** description watches fixed points in space and records the fields that stream past them, $T(\mathbf{x},t)$, $\mathbf{u}(\mathbf{x},t)$. A **Lagrangian** description follows material parcels, labeling each by its initial position and tracking it along its trajectory. A weather station bolted to rock is an Eulerian instrument; a stake drilled into the moving ice, resurveyed year after year, is a Lagrangian one. The models in this book are written in Eulerian form, while much of what we measure, stake networks, ice cores, the layers tracked by radar, is Lagrangian, and translating between the two is a constant low-level activity of the subject.

The translation is the **material derivative**. The rate of change experienced by a parcel moving with velocity $\mathbf{u}$ through an Eulerian field $T$ is, by the chain rule,

$$
\frac{DT}{Dt}=\frac{\partial T}{\partial t}+\mathbf{u}\cdot\nabla T,
$$

```{admonition} Derivation
:class: dropdown
A parcel moving with the flow occupies position $\mathbf{x}(t)$, with $\mathrm{d}\mathbf{x}/\mathrm{d}t=\mathbf{u}$. The temperature it experiences is the field evaluated along its path, $T(\mathbf{x}(t),t)$. Differentiate with respect to $t$ by the chain rule, treating $T$ as a function of the four variables $(x_1,x_2,x_3,t)$,

$$
\frac{DT}{Dt}=\frac{\partial T}{\partial t}+\sum_{i}\frac{\partial T}{\partial x_i}\,\frac{\mathrm{d}x_i}{\mathrm{d}t}
=\frac{\partial T}{\partial t}+\frac{\partial T}{\partial x_i}\,u_i .
$$

The sum on $i$ is the dot product $\mathbf{u}\cdot\nabla T$, since $\partial T/\partial x_i$ are the components of $\nabla T$ and $u_i$ the components of $\mathbf{u}$. The first term is the change at a fixed point and the second the change from being carried to a place where the field differs.
```

a local term, the change at a fixed point, plus an advective term, the change from being carried to somewhere different. A skier descending in the evening feels both at once. The air everywhere is cooling as the sun sets, the local term, while the descent carries them into warmer air at lower elevation, the advective term, and the temperature history they experience is the sum. Every conservation law in the chapters ahead, momentum in these chapters and heat in {doc}`../thermomechanics/thermal-structure`, is a statement about $D/Dt$ of something, and the advective term is what couples those budgets to the flow itself.

## Traction and the stress tensor

Imagine cutting through the ice with a small plane whose orientation is given by a unit normal $\mathbf{n}$. The material on one side exerts a force on the material on the other, and dividing that force by the area of the cut gives the traction $\mathbf{t}$, a vector with units of stress. The traction depends on the orientation of the cut, so a full description of the internal force state at a point requires knowing $\mathbf{t}$ for every possible $\mathbf{n}$.

Cauchy showed that this apparently infinite amount of information is contained in a single second-order tensor. Balancing forces on a vanishingly small tetrahedron with three faces along the coordinate planes and one face with normal $\mathbf{n}$, the traction on the slanted face is a linear function of $\mathbf{n}$,

$$
\mathbf{t}=\boldsymbol{\sigma}\,\mathbf{n}, \qquad t_i=\sigma_{ij}n_j,
$$

```{admonition} Derivation
:class: dropdown
Consider a small tetrahedron at a point, with three faces lying in the coordinate planes and a fourth, slanted face of area $A$ and outward unit normal $\mathbf{n}$. The three coordinate faces have outward normals along $-\mathbf{e}_1,-\mathbf{e}_2,-\mathbf{e}_3$, and their areas are the projections of the slanted face, $A_j=n_j A$, since $n_j$ is the cosine between $\mathbf{n}$ and the $j$ axis.

Let $\mathbf{t}^{(\mathbf{n})}$ be the traction on the slanted face and $\mathbf{t}^{(-\mathbf{e}_j)}$ the traction on the coordinate face with normal $-\mathbf{e}_j$. By Newton's third law $\mathbf{t}^{(-\mathbf{e}_j)}=-\mathbf{t}^{(\mathbf{e}_j)}$. Balancing forces on the tetrahedron,

$$
\mathbf{t}^{(\mathbf{n})}A+\sum_j \mathbf{t}^{(-\mathbf{e}_j)}A_j+\rho\,\mathbf{b}\,V=0 ,
$$

where the last term collects body forces and inertia over the volume $V$. Now shrink the tetrahedron about the point. The face areas scale as the square of its linear size $\ell$ while the volume scales as $\ell^3$, so the body-force term vanishes relative to the surface terms as $\ell\to0$. Dividing by $A$ and using $A_j/A=n_j$ leaves

$$
\mathbf{t}^{(\mathbf{n})}=\sum_j \mathbf{t}^{(\mathbf{e}_j)}\,n_j .
$$

Define $\sigma_{ij}$ as the $i$ component of the traction on the face whose normal is $\mathbf{e}_j$, that is $t^{(\mathbf{e}_j)}_i=\sigma_{ij}$. Then $t_i=\sigma_{ij}n_j$, which is the stated relation.
```

where $\boldsymbol{\sigma}$ is the Cauchy stress tensor and the summation convention is used. The component $\sigma_{ij}$ is the $i$ component of traction on a face whose outward normal points in the $j$ direction. The three diagonal components are normal stresses, acting perpendicular to their faces, and the six off-diagonal components are shear stresses, acting in the plane of their faces.

Balancing angular momentum on the same small element shows that the tensor is symmetric, $\sigma_{ij}=\sigma_{ji}$, so only six of its nine components are independent. We adopt the convention that tension is positive, so that a positive normal stress pulls a face outward. Because the tensor is symmetric it has three real eigenvalues, the principal stresses, and three mutually perpendicular eigenvectors, the principal directions, along which the traction is purely normal with no shear. The mean of the three normal stresses defines the pressure,

$$
p=-\tfrac13\,\mathrm{tr}(\boldsymbol{\sigma})=-\tfrac13\left(\sigma_{11}+\sigma_{22}+\sigma_{33}\right),
$$

the minus sign making the pressure positive under compression.

## The strain-rate tensor

Deformation is described not by displacement, as for an elastic solid, but by the rate of deformation, since ice flows. The relevant quantity is the spatial gradient of the velocity field $\mathbf{u}(\mathbf{x},t)$, the tensor $\partial u_i/\partial x_j$. This gradient can be split into a symmetric and an antisymmetric part, and the two parts have distinct physical meanings. The symmetric part is the strain-rate tensor,

$$
\dot\varepsilon_{ij}=\tfrac12\left(\frac{\partial u_i}{\partial x_j}+\frac{\partial u_j}{\partial x_i}\right),
$$

which measures the rate at which the material is stretching and shearing. The antisymmetric part is the spin, or vorticity, tensor, which measures the rate of rigid rotation and produces no deformation. Only the strain rate enters a constitutive law, because a material element that merely rotates feels no internal resistance.

The diagonal components of the strain rate are stretching rates along the coordinate axes, and the off-diagonal components are shearing rates. Like the stress, the strain-rate tensor is symmetric, with three principal strain rates along three principal directions of stretching. Glacier ice is, to a very good approximation, incompressible: deformation changes the shape of a material element but not its volume. Incompressibility is the statement that the velocity field is divergence free,

$$
\mathrm{tr}(\dot{\boldsymbol{\varepsilon}})=\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}+\frac{\partial w}{\partial z}=\nabla\!\cdot\!\mathbf{u}=0,
$$

so the three principal stretching rates always sum to zero, and any extension in one direction is compensated by shortening in another.

## Deviatoric stress

Because ice cannot change volume, a uniform pressure cannot deform it; it can only resist compression elastically. What drives flow is the part of the stress that acts to change shape. Removing the isotropic pressure from the full stress leaves the deviatoric stress,

$$
\tau_{ij}=\sigma_{ij}+p\,\delta_{ij}=\sigma_{ij}-\tfrac13\,\mathrm{tr}(\boldsymbol{\sigma})\,\delta_{ij},
$$

which is trace free by construction, $\mathrm{tr}(\boldsymbol{\tau})=0$. It is the deviatoric stress, not the full stress, that the flow law relates to strain rate. This is why an ice shelf, which floats in a state of high pressure, still spreads: the spreading is driven by the deviatoric stresses associated with the imbalance between the weight of the ice and the pressure of the water, not by the pressure itself.

## Invariants and the effective quantities

A constitutive law must give the same prediction regardless of how the coordinate axes are oriented, so it can depend on the tensors only through their invariants, the combinations that do not change under rotation. For a trace-free tensor the first invariant vanishes, and the most important remaining one is the second invariant. For stress and strain rate these define the effective stress and effective strain rate,

$$
\tau_E=\sqrt{\tfrac12\,\tau_{ij}\tau_{ij}}, \qquad \dot\varepsilon_E=\sqrt{\tfrac12\,\dot\varepsilon_{ij}\dot\varepsilon_{ij}},
$$

```{admonition} Derivation
:class: dropdown
The contraction $\tau_{ij}\tau_{ij}$ is a sum of squares over all nine components and so is invariant under rotation, like any full contraction of a tensor with itself. For a trace-free symmetric tensor it equals twice the negative of the second principal invariant, which is why it is the natural quantity to build a scalar measure from. The factor $\tfrac12$ is a convention fixed so that the effective stress reduces to the familiar value in simple cases.

Take uniaxial deviatoric stress with principal values $(\tau,-\tfrac12\tau,-\tfrac12\tau)$, the deviatoric part of a pull along one axis. Then

$$
\tau_{ij}\tau_{ij}=\tau^2+\tfrac14\tau^2+\tfrac14\tau^2=\tfrac32\,\tau^2,
\qquad
\tau_E=\sqrt{\tfrac12\cdot\tfrac32\,\tau^2}=\sqrt{\tfrac34}\,\tau ,
$$

while for a single shear stress with $\tau_{xz}=\tau_{zx}=\tau$ and all else zero,

$$
\tau_{ij}\tau_{ij}=\tau^2+\tau^2=2\tau^2,
\qquad
\tau_E=\sqrt{\tfrac12\cdot 2\tau^2}=\tau ,
$$

so the convention makes $\tau_E$ coincide with the applied shear stress in simple shear. The strain-rate measure $\dot\varepsilon_E$ is defined by the identical contraction.
```

scalar measures of the overall magnitude of shape-changing stress and deformation. These are exactly the quantities that appear in Glen's flow law, which states that the strain-rate tensor is aligned with the deviatoric-stress tensor with a magnitude set by $\tau_E$.

## Two canonical deformations

In pure shear, an element is stretched along one axis and compressed equally along another, with velocity field $u=\dot\varepsilon x$, $v=-\dot\varepsilon y$. The strain-rate tensor is diagonal, $\dot\varepsilon_{xx}=\dot\varepsilon$ and $\dot\varepsilon_{yy}=-\dot\varepsilon$, the spin is zero, and the effective strain rate is $\dot\varepsilon$. This is the deformation of ice spreading under its own weight near a divide.

In simple shear, layers slide over one another, with velocity field $u=\dot\gamma\,z$ and no other component. The velocity gradient now has a single nonzero entry, which splits equally into a shearing strain rate $\dot\varepsilon_{xz}=\tfrac12\dot\gamma$ and an equal rotation. Half of simple shear is therefore deformation and half is rigid rotation, a distinction that matters when interpreting the strain measured in a borehole or by repeat radar. Simple shear is the deformation of the deep ice in an ice sheet, sheared over its bed, and of the ice in the margins of a fast-flowing stream. These two patterns, extension near divides and shear near beds and margins, organize where in an ice sheet each part of the flow law does its work, which is the subject of the chapters that follow.
