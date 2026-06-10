# Ice rheology: Glen's flow law

A rheology, or constitutive law, relates the stress applied to a material to the deformation that results. For ice it is the equation that closes the system: combined with conservation of momentum, it determines the velocity field. The law in standard use comes from the laboratory creep experiments of {cite}`glen1955,glen1958`, and the physical basis for it is set out in Chapter 3 of {cite}`cuffey2010`. This chapter develops the law, the microphysics behind it, and the parameter values and caveats a modeler needs.

## How ice deforms at the grain scale

To understand why ice flows the way it does, begin with a single crystal. Ice Ih deforms overwhelmingly by the glide of dislocations on its basal planes, the planes perpendicular to the c-axis. This basal glide is easy, in the sense that the resolved shear stress needed to drive it is small, while glide on other planes requires stresses roughly sixty times larger. A single crystal is therefore extremely anisotropic and behaves, to a first approximation, like a deck of cards that shears readily in one set of planes and hardly at all in others.

A glacier is not a single crystal but an aggregate of many, with their c-axes initially pointing in all directions. A randomly oriented crystal cannot deform by basal glide alone in an arbitrary imposed strain, because the five independent components of a general strain cannot be produced by glide on a single plane. The grains must therefore deform compatibly, and they accommodate one another through additional processes: glide on harder planes, the climb of dislocations, bending and rotation of the lattice, and sliding and migration of grain boundaries. Which of these accommodation processes controls the overall rate depends on stress, temperature, and grain size, and that is why the bulk flow law is not a simple reflection of single-crystal glide {cite}`duval1983,goldsby2001`.

## The creep curve

If a sample of ice is held under a constant stress and its strain is recorded, the strain rate is not constant. It begins high and falls during a phase of primary, or transient, creep as the internal dislocation structure adjusts and the grains harden against one another. It then passes through a minimum during secondary creep, where hardening and recovery are in balance. Finally, in tertiary creep, the strain rate rises again and levels off at a steady value several times larger than the secondary minimum, because the ice recrystallizes under the imposed stress and develops a crystal fabric that is favorably oriented for glide.

Glen's law describes the secondary, minimum strain rate. The faster tertiary rate, which is what fully developed, recrystallized ice actually attains in nature, is usually represented by multiplying the secondary-creep law by an enhancement factor. This distinction matters: laboratory measurements of the minimum rate underpin the published values of the rate factor, but the ice in a shear margin or a deep ice stream is in tertiary creep and flows faster than those values alone would imply.

## The flow law and its stress dependence

In tensor form the strain-rate tensor is parallel to the deviatoric-stress tensor, and its magnitude grows as a power of the effective stress,

$$
\dot\varepsilon_{ij}=A\,\tau_E^{\,n-1}\,\tau_{ij}, \qquad \dot\varepsilon_E=A\,\tau_E^{\,n},
$$

where $\boldsymbol{\tau}$ is the deviatoric stress, $\tau_E$ the effective stress, $A$ the rate factor, and $n$ Glen's exponent. For the stresses found in glaciers and ice sheets, roughly 0.05 to 0.2 megapascals, the data are consistent with $n$ close to 3. This value is the signature of dislocation creep, in which the density of mobile dislocations itself rises with stress, so that the strain rate increases faster than linearly.

The exponent is not universal. At the very low stresses of slow ice-sheet interiors, below about 0.1 megapascals, experiments suggest the exponent falls toward 1 or 2 as grain-size-sensitive mechanisms, grain-boundary sliding and diffusional flow, take over from dislocation creep {cite}`goldsby2001`. At higher stresses some recent analyses favor $n$ closer to 4. The honest position is that a single power law is an approximation to a composite of mechanisms, each dominant in a different range of stress, temperature, and grain size, and that $n=3$ is a serviceable average across the conditions of most glacier flow rather than a fundamental constant. Because the strain rate depends so steeply on stress, the nonlinearity is responsible for much of the character of ice flow, including the tendency of fast flow to concentrate into narrow streams: a region carrying twice the deviatoric stress of its surroundings deforms about eight times faster.

## The rate factor and its controls

The rate factor $A$ varies by more than two orders of magnitude across the temperatures found in ice sheets, so its dependence on temperature is as important as the flow law itself. The variation follows an Arrhenius relation,

$$
A(T)=A_0\exp\!\left(-\frac{Q}{R\,T'}\right),
$$

in which $T'$ is the temperature measured relative to the pressure-melting point, the homologous temperature, $R$ is the gas constant, and $Q$ is the activation energy for creep. Using the homologous temperature matters at depth, where the high pressure lowers the melting point by a few tenths of a degree per hundred meters and makes the deep ice effectively warmer than its absolute temperature suggests.

The activation energy is not constant. Below about minus ten degrees Celsius, $Q$ is close to 60 kilojoules per mole. Above that temperature it rises to roughly 115 to 140 kilojoules per mole, because additional processes, including premelting and enhanced grain-boundary mobility near the melting point, accelerate the creep. The published recommendation is to use two Arrhenius branches with a switch near minus ten degrees, and Chapter 3 of {cite}`cuffey2010` tabulates recommended values, with the rate factor reaching about $2.4\times10^{-24}$ inverse pascals cubed per second at the melting point and falling by more than a hundredfold in the coldest polar ice.

Two further controls are important in practice. Temperate ice that contains liquid water at its grain boundaries is softer than dry ice at the same temperature, and the rate factor increases by roughly a factor of three as the liquid water content rises through the first percent {cite}`duval1983`. And impurities, grain size, and crystal fabric all modify the softness. These effects are gathered into an empirical enhancement factor $E$ that multiplies the rate factor, with $E$ near one for isotropic Holocene ice, around three for the fine-grained, impurity-rich ice deposited during glacial periods, and as large as ten in the directions favored by a strongly aligned fabric, as discussed in {doc}`ice-fabric`.

## The viscosity form and its regularization

Glen's law describes a nonlinear viscous fluid, and for numerical work it is written in the form of an ordinary viscous stress, $\tau_{ij}=2\eta\,\dot\varepsilon_{ij}$, with an effective viscosity that depends on the strain rate,

$$
\eta=\tfrac12\,A^{-1/n}\,\dot\varepsilon_E^{\,(1-n)/n}.
$$

Because $n>1$, the viscosity falls as the strain rate rises, so ice is shear thinning and softens where it already flows fast. This form has a practical difficulty: as the strain rate approaches zero, the viscosity diverges. Numerical models avoid the singularity by adding a small critical strain rate $\dot\varepsilon_0$ under the root, replacing $\dot\varepsilon_E$ with $\sqrt{\dot\varepsilon_E^2+\dot\varepsilon_0^2}$, which caps the viscosity in nearly stagnant ice without affecting the answer where the ice is deforming appreciably. This regularized viscosity is exactly what icepack assembles and inserts into the momentum balance.

## What the law leaves out

It is worth being clear about the status of Glen's law. It is empirical, a fit to the minimum creep rate of laboratory samples, extended to natural ice by a single enhancement factor and a single exponent. It does not, on its own, represent the evolution of grain size and fabric that accompanies real flow, the transition between deformation mechanisms across the range of conditions in an ice sheet, or the anisotropy that develops in shear. Models that need those effects add them separately, through fabric evolution schemes or composite flow laws. For most purposes, though, the power law with $n=3$ and a temperature-dependent, enhancement-adjusted rate factor captures the leading behavior, and it is the relationship that the rest of this book builds on. Recommended values and the experimental evidence behind them are collected in Chapter 3 of {cite}`cuffey2010`.
