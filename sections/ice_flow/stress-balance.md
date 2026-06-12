# Momentum balance and the driving stress

We now have the kinematics of stress and strain and the rheology that links them. The last physical principle is conservation of momentum, Newton's second law written for a continuum. Combined with the flow law it determines the velocity, and from it we extract the single most important quantity in ice dynamics, the gravitational driving stress, and the resistive stresses that oppose it. The development follows Chapter 8 of {cite}`cuffey2010` and {cite}`greve2009`.

## Cauchy's equation of motion

Apply Newton's second law to an arbitrary volume of ice. The forces on it are the body force of gravity, acting throughout the volume, and the surface tractions, acting on its boundary. Writing the surface term as an integral of the traction $\boldsymbol{\sigma}\mathbf{n}$ over the boundary and converting it to a volume integral with the divergence theorem, the balance of momentum for every volume implies a local equation at every point,

$$
\rho\,\frac{D\mathbf{u}}{Dt}=\nabla\!\cdot\!\boldsymbol{\sigma}+\rho\,\mathbf{g},
$$

where $D/Dt$ is the material derivative following the flow. This is Cauchy's equation of motion, the continuum form of $\mathbf{F}=m\mathbf{a}$. The divergence of the stress tensor is the net surface force per unit volume, and $\rho\mathbf{g}$ is the gravitational body force.

## Ice flow is a Stokes flow

The term on the left is the inertia, and for ice it is utterly negligible. A scale estimate makes this concrete. The ratio of inertial to viscous forces is the Reynolds number, $Re=\rho U L/\eta$. Taking a density of about $900$ kilograms per cubic meter, a speed of a hundred meters per year, a length of a kilometer, and an effective viscosity of order $10^{13}$ to $10^{14}$ pascal seconds, the Reynolds number comes out around $10^{-13}$. The flow is as far from turbulent as a fluid can be, and the acceleration term can be dropped entirely. What remains is the Stokes balance,

$$
\nabla\!\cdot\!\boldsymbol{\sigma}+\rho\,\mathbf{g}=0,
$$

a statement that the forces on every parcel of ice are in instantaneous balance at all times. Writing $\boldsymbol{\sigma}=\boldsymbol{\tau}-p\mathbf{I}$ separates the shape-changing deviatoric stress from the pressure,

$$
\nabla\!\cdot\!\boldsymbol{\tau}-\nabla p+\rho\,\mathbf{g}=0.
$$

Together with incompressibility, $\nabla\!\cdot\!\mathbf{u}=0$, and Glen's law relating $\boldsymbol{\tau}$ to the strain rate, this is a closed system: four scalar equations, the three components of the momentum balance and the incompressibility condition, for the three velocity components and the pressure, with the deviatoric stresses eliminated through the flow law. It is the complete description of glacier flow, and everything in the following chapters is an approximation to it.

## Boundary conditions

The equations are solved subject to conditions on the surfaces of the ice, and the conditions come in two kinds. **Dynamic** conditions constrain the traction. The upper surface is free, in contact only with the atmosphere, so the traction there vanishes. At the bed the condition depends on the situation. Where the ice is frozen to the bed the velocity is zero; where it slides, the basal shear traction is related to the sliding velocity through a friction law, the subject of {doc}`../thermomechanics/basal-motion`. At a calving front or the vertical face of an ice shelf the traction balances the pressure of the water and the atmosphere outside. Beneath a floating shelf the traction balances the pressure of the ocean. These conditions are not incidental; the buttressing that an ice shelf provides, and the way a grounding line responds to thinning, are encoded entirely in them.

**Kinematic** conditions constrain the motion of the boundaries themselves. The upper surface $z=s(x,y,t)$ is a material surface fed by snowfall, so a parcel on it stays on it except as mass is added or removed. Requiring $D(z-s)/Dt$ to equal the accumulation gives the surface evolution equation,

$$
\frac{\partial s}{\partial t}+u\,\frac{\partial s}{\partial x}+v\,\frac{\partial s}{\partial y}=w+a,
$$

with $a$ the surface mass balance, and its counterpart at the bed, $u\,b_x+v\,b_y=w$ for a rigid bed without melting or freezing. The surface condition is where time enters the problem. The Stokes balance itself is instantaneous, the diagnostic problem of the introduction, and it is this kinematic condition, depth-integrated into the thickness equation of {doc}`shallow-ice`, that carries the geometry forward in time and makes the prognostic problem.

## The driving stress

The full system is three-dimensional and nonlinear, but integrating the horizontal momentum balance through the thickness reveals the force that actually moves the ice. Two simplifications make the integration transparent and are accurate for the thin geometry of ice sheets. First, in the vertical balance the deviatoric terms are small, so the vertical momentum equation reduces to the hydrostatic relation $\partial p/\partial z=-\rho g$. Integrating downward from the stress-free surface at $z=s$ gives the cryostatic pressure $p=\rho g(s-z)$. Second, the horizontal gradient of this pressure is

$$
\frac{\partial p}{\partial x}=\rho g\,\frac{\partial s}{\partial x},
$$

the horizontal pressure gradient set by the slope of the upper surface. Integrating the horizontal momentum balance through the thickness then identifies the depth-integrated forward force, the gravitational driving stress,

$$
\boldsymbol{\tau}_d=-\rho\,g\,H\,\nabla s,
$$

where $H$ is the thickness and $\nabla s$ is the surface slope. The driving stress points down the surface slope and grows with both thickness and steepness. For typical ice-sheet values, a thickness of a kilometer or two and a surface slope of a few parts per thousand, it is of order 50 to 150 kilopascals, and this narrow range is one of the most robust facts in glaciology, since thicker ice tends to sit on gentler slopes and thinner ice on steeper ones.

Ice flows in the direction the surface tilts, even where the bed slopes the other way, which is why the direction of ice-sheet flow can be read to first order from a map of surface elevation alone.

## The force budget

Because the ice is in force balance, the driving stress must be opposed by resistive stresses, and there are only three places they can come from. Basal drag is the friction at the bed where the ice is grounded. Lateral drag is the shear against valley walls or against slower ice on either side of a stream. Longitudinal stress gradients are the push and pull transmitted from up and down the flow line through membrane stresses. Schematically the depth-integrated balance reads

$$
\underbrace{\boldsymbol{\tau}_d}_{\text{driving}}=\underbrace{\boldsymbol{\tau}_b}_{\text{basal}}+\underbrace{\text{(lateral)}}_{}+\underbrace{\nabla\!\cdot\!(\text{membrane})}_{\text{longitudinal}}.
$$

Which term dominates defines the kind of glacier and, with it, the appropriate flow approximation. In the slow interior of an ice sheet the driving stress is balanced locally by basal drag through vertical shear, the regime of the shallow-ice approximation. In a fast ice stream or a floating shelf it is balanced instead by membrane and lateral stresses, the regime of the shallow-shelf approximation. The next two chapters derive these limits and the models between them from the equations written here.
