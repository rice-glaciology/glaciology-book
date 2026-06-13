# Ice rheology

A rheology, or constitutive law, relates the stress applied to a material to the deformation that results. For ice it is the equation that closes the system: combined with conservation of momentum, it determines the velocity field. The law in standard use comes from the laboratory creep experiments of {cite}`glen1955,glen1958`, and the physical basis for it is set out in Chapter 3 of {cite}`cuffey2010`. This chapter develops the law, the microphysics behind it, and the parameter values and caveats a modeler needs.

## Grain-scale deformation mechanisms

To understand why ice flows the way it does, begin with a single crystal. Ice Ih deforms overwhelmingly by the glide of dislocations on its basal planes, the planes perpendicular to the c-axis. This basal glide is easy, in the sense that the resolved shear stress needed to drive it is small, while glide on other planes requires stresses roughly sixty times larger. A single crystal is therefore extremely anisotropic and behaves, to a first approximation, like a deck of cards that shears readily in one set of planes and hardly at all in others.

A glacier is not a single crystal but an aggregate of many, with their c-axes initially pointing in all directions. A randomly oriented crystal cannot deform by basal glide alone in an arbitrary imposed strain, because the five independent components of a general strain cannot be produced by glide on a single plane. The grains must therefore deform compatibly, and they accommodate one another through additional processes: glide on harder planes, the climb of dislocations, bending and rotation of the lattice, and sliding and migration of grain boundaries. Which of these accommodation processes controls the overall rate depends on stress, temperature, and grain size, and that is why the bulk flow law is not a simple reflection of single-crystal glide {cite}`duval1983,goldsby2001`.

## Dislocation glide and the molecular origin of the rate

It is worth looking more closely at how basal glide actually proceeds, because the mechanism explains both the form of the flow law and the value of its activation energy. Glide does not happen by sliding whole planes rigidly over one another, which would require breaking every bond across the plane at once. It happens by the motion of dislocations, line defects across which the lattice is offset by one repeat distance, so that only the bonds along the moving line are rearranged at any instant. The dislocations of lowest energy in ice have the smallest possible offset, a Burgers vector of $(a/3)\langle 11\bar20\rangle$ lying in the basal plane, and X-ray topographs show them running predominantly in the basal plane in a screw orientation. Their density in a well-grown crystal is modest, of order $10^5$ per square centimeter, comparable to a semiconductor crystal of moderate quality. The plastic strain rate produced by their motion is

$$
\dot\varepsilon_p = \rho_d\, b\, v,
$$

where $\rho_d$ is the density of mobile dislocations, $b$ the magnitude of the Burgers vector, and $v$ the speed at which they glide. As the crystal deforms the dislocations multiply, so that $\rho_d$ grows with strain, and the glide velocity itself rises with the resolved stress roughly as a power law. Combining the two dependences yields a strain rate that grows faster than linearly with stress, which is the microscopic root of the power-law form of Glen's relation {cite}`fletcher1970`.

Ice shows almost no work hardening: once a single crystal yields it continues to flow at a low and nearly constant stress, rather than stiffening as deformation proceeds. The reason is that dislocations in ice do not obstruct one another the way they do in a metal. When their density grows too high they climb out of their glide planes, a motion fed by the self-diffusion of molecules through vacancies described in {doc}`../foundations/point-defects`, and annihilate in pairs, holding the mobile density roughly steady and allowing creep to reach a steady rate.

A dislocation gliding through the basal plane cannot advance without changing the proton configuration along its path, because the bonds it sweeps across must be reconnected on the far side. If those bonds simply reformed in whatever configuration they happened to meet, roughly half of them would end up as orientational defects, with two protons or none, at a prohibitive energy cost. The dislocation can therefore move only as fast as the proton arrangement ahead of it can be put right, and that ordering is accomplished by the migration of the very Bjerrum defects introduced in {doc}`../foundations/point-defects`. The flow of ice is, at this level, rate-limited by the diffusion of orientational defects. The prediction that follows is quantitative: the activation energy for creep should equal the energy to form and move a Bjerrum defect, about $0.6\ \mathrm{eV}$, and the measured activation energy for the creep of single crystals, near $0.6$ to $0.7\ \mathrm{eV}$, agrees {cite}`fletcher1970`. This same value reappears as the low-temperature branch of the rate factor below.

Two further observations clinch the picture. The first is a doping experiment of exactly the semiconductor kind anticipated in the chapter on defects: adding a few parts per million of hydrogen fluoride, which supplies L-defects, increases the creep rate of single-crystal ice by about a factor of ten at $-70\ \mathrm{^\circ C}$, just as expected if the diffusion of orientational defects sets the dislocation velocity {cite}`fletcher1970`. The second is a comparison across materials. Silicon and germanium share the open, tetrahedrally bonded framework of ice, with easy glide on their close-packed planes, and when deformed near the comparable fraction of their melting temperature they show the same pronounced yield point and the same low stress exponent that ice does. The character of ice flow is, in the end, a property of tetrahedral bonding worked out on a lattice whose protons must be reordered before it can shear {cite}`fletcher1970`.

## The creep curve

Nearly everything this chapter asserts about the flow law was first read off one kind of experiment. Hang a constant load on a sample of polycrystalline ice, hold the temperature fixed, record strain against time for days to months, and the resulting creep curve has a shape so reproducible that its phases have names. The strain rate it implies is anything but constant, and which part of the curve a measurement samples decides what "the viscosity of ice" even means.

The loading itself produces an immediate elastic strain, the stretch of the bonds met again in the Maxwell section below. What follows is **primary creep**, a long deceleration in which the strain rate falls roughly as the inverse two-thirds power of time, the Andrade-like transient familiar from metals. The deceleration is strain hardening at work. Dislocations multiplying on the easy basal planes pile up against grain boundaries and against neighbors whose basal planes face the wrong way, and the back-stress from those pile-ups opposes further glide; part of this transient strain is even recoverable, springing back slowly if the load is removed, which is the delayed elasticity that complicates short-timescale measurements such as tidal flexure. Hardening cannot proceed indefinitely, because the same thermal agitation that drives creep also lets the crystal recover, climbing dislocations out of their tangles and migrating grain boundaries through the worst of the damage.

**Secondary creep** is the truce between the two. The strain rate passes through a minimum where hardening and recovery balance, and the remarkable empirical fact, established across stresses, temperatures, and laboratories, is that the minimum arrives at about one percent strain almost regardless of conditions {cite}`cuffey2010`. This minimum rate is the quantity Glen measured when he established the flow law {cite}`glen1955`, and it is the quantity behind nearly every published value of the rate factor $A$. Secondary creep is therefore not a long-lived steady state but an instant of balance the sample passes through, and treating it as the reference state is a convention of the discipline, honest so long as it is remembered.

In **tertiary creep** the strain rate climbs from the minimum and levels onto a genuinely steady plateau, typically around three times the minimum rate in shear and higher still where the conditions favor it. The acceleration is the microstructure reorganizing under the imposed stress. New, strain-free grains nucleate and grow at the expense of the hardened ones, and the recrystallized grains take up orientations with their basal planes aligned for easy glide, so the sample manufactures exactly the crystal fabric that {doc}`ice-fabric` describes in nature. Tertiary creep, not secondary, is the state of the ice in a shear margin, in the deforming trunk of an ice stream, and in most deep, old, warm ice.

% TODO Illustrator figure: figures/creep-curve.svg (label fig-creep-curve, width 85%)
% Spec: two stacked panels for a constant-stress creep test. Top, strain vs time showing the
% instantaneous elastic step, decelerating primary, near-linear secondary instant, accelerating
% tertiary. Bottom, strain rate vs strain on log axes: primary decay, minimum at ~1% strain
% (marked), rise to tertiary plateau ~3x minimum (marked E~3). Annotate which portion Glen's
% law describes and which portion natural shear-margin ice occupies.

Glen's law, as used through the rest of this book, describes the secondary minimum. The faster tertiary rate is folded in by multiplying the law by an enhancement factor $E$, which hides the entire physics of recrystallization and fabric inside one number of order unity to ten. This bookkeeping matters in both directions: a model that uses laboratory values of $A$ without enhancement will underestimate the deformation of fabric-softened ice, while a rate factor inverted from observations of a real glacier, as in the modeling chapters, returns the tertiary value with the fabric already priced in, whether or not anyone asked.

## The flow law and its stress dependence

In tensor form the strain-rate tensor is parallel to the deviatoric-stress tensor, and its magnitude grows as a power of the effective stress,

$$
\dot\varepsilon_{ij}=A\,\tau_E^{\,n-1}\,\tau_{ij}, \qquad \dot\varepsilon_E=A\,\tau_E^{\,n},
$$

where $\boldsymbol{\tau}$ is the deviatoric stress, $\tau_E$ the effective stress, $A$ the rate factor, and $n$ Glen's exponent. For the stresses found in glaciers and ice sheets, roughly 0.05 to 0.2 megapascals, the data are consistent with $n$ close to 3. This value is the signature of dislocation creep, in which the density of mobile dislocations itself rises with stress, so that the strain rate increases faster than linearly.

% TODO Illustrator figure: figures/glen-law-curves.svg (label fig-glen-law-curves, width 80%)
% Spec: strain rate vs deviatoric stress for n=1 (Newtonian), n=3 (Glen), and the perfectly
% plastic limit, all normalized through the same point at tau_0 ~ 100 kPa; cite glen1955,cuffey2010.

The closure rate of tunnels bored beneath glaciers, the spreading of floating ice shelves, and the progressive tilt of boreholes all probe natural ice at natural stresses, and all are consistent with a stress exponent near 3 {cite}`nye1953,cuffey2010`. Calibrating against field measurements remains delicate even so, because stress, temperature, and fabric are hard to separate cleanly in any single observation.

At the very low stresses of slow ice-sheet interiors, below about 0.1 megapascals, experiments suggest the exponent falls toward 1 or 2 as grain-size-sensitive mechanisms, grain-boundary sliding and diffusional flow, take over from dislocation creep {cite}`goldsby2001`. Goldsby and Kohlstedt made the composite nature explicit, writing the total strain rate as a sum and series combination of the contributing mechanisms,

$$
\dot\varepsilon \;=\; \dot\varepsilon_{\mathrm{diff}} \;+\; \left(\dot\varepsilon_{\mathrm{basal}}^{-1} + \dot\varepsilon_{\mathrm{gbs}}^{-1}\right)^{-1} \;+\; \dot\varepsilon_{\mathrm{disl}},
$$

with each term a power law $\dot\varepsilon_{(\cdot)} = A_{(\cdot)}\tau^{n_{(\cdot)}}$ of its own exponent, diffusional flow at $n=1$, grain-boundary sliding near $n=1.8$, basal slip near $n=2.4$, and dislocation creep near $n=4$. Basal glide and grain-boundary sliding appear in series because each must wait on the other, and whichever is slower sets the pace. At higher stresses some recent analyses favor $n$ closer to 4. The honest position is that a single power law is an approximation to a composite of mechanisms, each dominant in a different range of stress, temperature, and grain size, and that $n=3$ is a serviceable average across the conditions of most glacier flow rather than a fundamental constant. Because the strain rate depends so steeply on stress, the nonlinearity is responsible for much of the character of ice flow, including the tendency of fast flow to concentrate into narrow streams: a region carrying twice the deviatoric stress of its surroundings deforms about eight times faster.

## The rate factor and its controls

The rate factor $A$ varies by more than two orders of magnitude across the temperatures found in ice sheets, so its dependence on temperature is as important as the flow law itself. The variation follows an Arrhenius relation, derived from the defect rate processes of the lattice in {doc}`../foundations/point-defects`,

$$
A(T)=A_0\exp\!\left(-\frac{Q}{R\,T'}\right),
$$

in which $T'$ is the temperature measured relative to the pressure-melting point, the homologous temperature, $R$ is the gas constant, and $Q$ is the activation energy for creep. Using the homologous temperature matters at depth, where the high pressure lowers the melting point by a few tenths of a degree per hundred meters and makes the deep ice effectively warmer than its absolute temperature suggests.

Below about minus ten degrees Celsius, $Q$ is close to 60 kilojoules per mole, which is essentially the energy to form and move the orientational defects that gate dislocation glide, the mechanism set out above. Above that temperature it rises to roughly 115 to 140 kilojoules per mole, because additional processes, including premelting and enhanced grain-boundary mobility near the melting point, accelerate the creep. The published recommendation is to use two Arrhenius branches with a switch near minus ten degrees, and Chapter 3 of {cite}`cuffey2010` tabulates recommended values, with the rate factor reaching about $2.4\times10^{-24}$ inverse pascals cubed per second at the melting point and falling by more than a hundredfold in the coldest polar ice.

Two further controls are important in practice. Temperate ice that contains liquid water at its grain boundaries is softer than dry ice at the same temperature, and the rate factor increases by roughly a factor of three as the liquid water content rises through the first percent {cite}`duval1983`. And impurities, grain size, and crystal fabric all modify the softness. These effects are gathered into an empirical enhancement factor $E$ that multiplies the rate factor, with $E$ near one for isotropic Holocene ice, around three for the fine-grained, impurity-rich ice deposited during glacial periods, and as large as ten in the directions favored by a strongly aligned fabric, as discussed in {doc}`ice-fabric`.

## The viscosity form and its regularization

Glen's law describes a nonlinear viscous fluid, and for numerical work it is written in the form of an ordinary viscous stress, $\tau_{ij}=2\eta\,\dot\varepsilon_{ij}$, with an effective viscosity that depends on the strain rate,

$$
\eta=\tfrac12\,A^{-1/n}\,\dot\varepsilon_E^{\,(1-n)/n}.
$$

Because $n>1$, the viscosity falls as the strain rate rises, so ice is shear thinning and softens where it already flows fast. This form has a practical difficulty: as the strain rate approaches zero, the viscosity diverges. Numerical models avoid the singularity by adding a small critical strain rate $\dot\varepsilon_0$ under the root, replacing $\dot\varepsilon_E$ with $\sqrt{\dot\varepsilon_E^2+\dot\varepsilon_0^2}$, which caps the viscosity in nearly stagnant ice without affecting the answer where the ice is deforming appreciably. This regularized viscosity is exactly what icepack assembles and inserts into the momentum balance.

## Elasticity and the Maxwell time

Glen's law treats ice as a fluid, and the treatment is right only on long enough timescales. Loaded suddenly, ice responds elastically, with a Young's modulus near 10 GPa and a Poisson ratio near 0.3, the stiffness probed by the seismic waves of {doc}`../observing/cryoseismicity-lab`. The crossover between the two behaviors is the Maxwell time, the ratio of viscosity to elastic modulus, $t_M \sim \eta/E$, which for ice at glacial stresses is on the order of a day. Stresses that fluctuate faster than that, ocean tides flexing an ice shelf, a calving impact, a passing seismic wave, are answered elastically; stresses held longer are relaxed by creep. A Maxwell viscoelastic model, an elastic spring and a Glen-law dashpot in series, spans the two limits and is the standard tool for tidal flexure studies at grounding zones, where the daily bending of the ice is used to map exactly where the ice goes afloat. For the slow flow that occupies the rest of this book, the elastic transient is over before it matters, and the fluid description stands.

## Limitations of the flow law

Glen's law is empirical, a fit to the minimum creep rate of laboratory samples, extended to natural ice by a single enhancement factor and a single exponent. It does not, on its own, represent the evolution of grain size and fabric that accompanies real flow, the transition between deformation mechanisms across the range of conditions in an ice sheet, or the anisotropy that develops in shear. Models that need those effects add them separately, through fabric evolution schemes or composite flow laws. For most purposes, though, the power law with $n=3$ and a temperature-dependent, enhancement-adjusted rate factor captures the leading behavior, and it is the relationship that the rest of this book builds on. Recommended values and the experimental evidence behind them are collected in Chapter 3 of {cite}`cuffey2010`.
