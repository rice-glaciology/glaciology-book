# Ice rheology: Glen's flow law

A rheology, or constitutive law, relates the stress applied to a material to the deformation that results. For ice the governing relationship comes from the laboratory creep experiments of {cite}`glen1955`, and it is developed in detail in Chapter 3 of {cite}`cuffey2010`. Together with conservation of momentum it closes the system of equations and allows us to predict how ice flows.

## The flow law

Glen measured the rate at which ice samples deformed under a fixed load and found that the strain rate increases as a power of the applied stress rather than in proportion to it. Written as a tensor relation, the strain-rate tensor is parallel to the deviatoric-stress tensor,

$$
\dot\varepsilon_{ij} = A\,\tau_E^{\,n-1}\,\tau_{ij},
$$

where $\boldsymbol{\tau}$ is the deviatoric stress, $\tau_E$ is the effective stress defined in the previous chapter, $n$ is Glen's exponent, and $A$ is the rate factor, sometimes called the fluidity. For the range of stresses found in glaciers and ice sheets, roughly 0.05 to 0.2 MPa, laboratory and borehole data are consistent with a value of $n$ close to 3, though reported values span about 2.5 to 4 depending on stress, temperature, and the type of ice. At much lower stresses the exponent appears to decrease toward 1, where deformation is governed by diffusion rather than the motion of dislocations, but that regime is rarely relevant to glacier flow.

Because the strain rate depends on the cube of the stress, the flow law is strongly nonlinear. Ice that carries twice the deviatoric stress of its surroundings deforms roughly eight times faster. Much of the distinctive behavior of ice flow follows from this nonlinearity, including the tendency of rapid flow to concentrate into narrow streams rather than spreading evenly. The same relation is often written in terms of the second invariants alone, as $\dot\varepsilon_E = A\,\tau_E^{\,n}$.

## The rate factor and temperature

The rate factor changes by more than two orders of magnitude across the range of temperatures found in ice sheets, so its temperature dependence is as important as the flow law itself. The variation follows an Arrhenius relation,

$$
A(T) = A_0 \exp\!\left(-\frac{Q}{R\,T}\right),
$$

in which $T$ is the absolute temperature, $R$ is the gas constant, and $Q$ is the activation energy for creep. Cuffey and Paterson recommend an activation energy near 60 kJ per mole for temperatures below about $-10^{\circ}$C, rising to roughly 115 kJ per mole as the ice approaches its melting point, where liquid water along grain boundaries provides additional ways for the ice to deform. A representative value of the rate factor at the melting point is about $2.4\times10^{-24}$ Pa$^{-3}$ s$^{-1}$, and it falls steeply as the ice cools.

Two consequences are worth drawing out. The warm ice near the bed of an ice sheet deforms much more readily than the cold ice above it, so most of the internal deformation in a vertical column takes place in its lowest part. Temperate ice that holds liquid water is softer still, which helps explain why temperate glaciers and the warm beds of polar ice sheets can move quickly.

The rate factor also responds to properties that temperature alone does not capture, among them grain size, dissolved and particulate impurities, and the orientation of the crystals. As ice deforms, its crystal axes tend to rotate into preferred orientations, and the resulting fabric makes the ice deform more easily in some directions than others. This anisotropy can change the effective softness by a factor of several. In models these effects are commonly absorbed into an enhancement factor that multiplies the rate factor, with values near one for isotropic Holocene ice and larger for the strongly aligned or impurity-rich ice laid down during glacial periods.

## The viscosity form

Glen's law describes a nonlinear viscous fluid, and for numerical work it is usually cast in the same form as an ordinary viscous stress, $\tau_{ij} = 2\eta\,\dot\varepsilon_{ij}$, with an effective viscosity that depends on the strain rate,

$$
\eta = \tfrac{1}{2}\,A^{-1/n}\,\dot\varepsilon_E^{\,(1-n)/n}.
$$

When $n$ exceeds 1 the viscosity decreases as the strain rate increases, so ice becomes softer in places where it is already deforming rapidly. This shear-thinning form is the one that ice-flow models, including icepack, insert into the momentum balance and solve.

With conservation of mass, a description of stress and strain, and a flow law relating the two, the only remaining ingredient is conservation of momentum. The next chapter imposes that balance and identifies the force that drives the flow. Recommended values for $n$, $A$, and $Q$, together with the experimental evidence behind them, are tabulated in Chapter 3 of {cite}`cuffey2010`.
