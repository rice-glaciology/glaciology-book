# Chemistry and statistical mechanics

Everyone arrives at this book already knowing the main character. Water is H₂O, two hydrogens on an oxygen, and it freezes at 0 °C. The first part of the book builds glacier physics from that familiar molecule up, and this chapter's job is to make the three everyday ingredients precise enough to carry the weight, the shape and polarity of the molecule itself, what temperature actually measures, and why the freezing point sits where it does. Each section ends where a later chapter begins. A reader comfortable with introductory chemistry and a little statistical thermodynamics can skim and move on; a reader who last saw orbitals long ago should find everything here that the ice chapters assume. The chemical physics of ice is treated comprehensively in {cite}`fletcher1970` and {cite}`petrenko1999`, and the statistical mechanics sketched below descends from the founding arguments of Boltzmann and Gibbs {cite}`boltzmann1877,gibbs1902`.

## Orbitals and the shape of a molecule

An electron bound to a nucleus does not orbit it like a planet. It occupies an orbital, a standing-wave pattern with a characteristic shape and energy, and the shapes matter because they decide the geometry of molecules.

Oxygen brings eight electrons. Two sit deep in the inner shell, leaving six in the outer shell, which mixes its one spherical s orbital and three dumbbell-shaped p orbitals into four equivalent hybrids, the sp³ set, pointing toward the corners of a tetrahedron. Two of the four hold lone pairs of electrons; the other two are half-filled and bond to hydrogen atoms. The result is the familiar bent water molecule, with its two O–H bonds at about 104.5°, slightly pinched from the ideal tetrahedral angle of 109.5° by the bulkier lone pairs. The tetrahedral disposition of two bonds and two lone pairs is the single most consequential geometric fact in this book, because it is what lets each water molecule connect to four neighbors and build the open lattice of {doc}`../foundations/ice-structure`.

```{figure} figures/water-molecule-geometry.png
:name: fig-water-molecule-geometry
:width: 55%

The water molecule, with bond length, bond angle, and the partial charges left by the uneven tug-of-war over the shared electrons. The values shown are from an electronic-structure model and differ slightly from the measured gas-phase geometry (0.958 Å and 104.5°); the bond angle is soft, and {doc}`../foundations/water-molecule` returns to why. Figure from M. Chaplin's *Water Structure and Science*, reproduced from the UW ESS 431 course slides of K. Christianson.
```

## Electronegativity and the polar bond

Atoms do not share electrons evenly. Electronegativity measures how strongly an atom pulls shared electrons toward itself, and oxygen is among the most electronegative of the elements while hydrogen is middling. Each O–H bond is therefore polar covalent, with the shared electrons displaced toward the oxygen, leaving a partial negative charge on the oxygen and partial positive charges on the hydrogens. Because the molecule is bent rather than linear, the bond polarities do not cancel, and the molecule carries a permanent dipole moment. The dipole is why water dissolves salts, why the dielectric constant that {doc}`../radar/em-waves` exploits is so large, and, above all, why water molecules grip one another.

That grip is the hydrogen bond. A hydrogen nucleus, bonded to one oxygen and stripped of most of its electron cloud by it, is attracted to the lone pair of a neighboring molecule's oxygen. The resulting bond is about a tenth as strong as the covalent O–H bond, roughly 20 kJ/mol against nearly 500, strong enough to organize molecules into a tetrahedral network and weak enough to break and re-form readily.

```{figure} figures/hydrogen-bond-network.gif
:name: fig-hydrogen-bond-network
:width: 55%

Hydrogen bonding (dashed) between a water molecule and four neighbors. Each δ+ hydrogen points at a δ− lone pair, so every molecule can donate two bonds and accept two more, and the four-armed motif at the center is the seed of the ice lattice. Reproduced from the UW ESS 431 course slides of K. Christianson.
``` Nearly every anomaly of water and ice, the open low-density crystal, the high melting point for so light a molecule, the proton disorder behind the point defects of {doc}`../foundations/point-defects`, is hydrogen bonding expressing itself, and the details are taken up in {doc}`../foundations/water-molecule`.

## What temperature measures

Much of glacier physics is the statistics of jostling molecules, and the machinery for that statistics deserves more than a formula pulled from the air. The starting point, due to Boltzmann, is a counting argument {cite}`boltzmann1877`. A macroscopic state, a block of ice with a given energy, corresponds to an astronomical number $W$ of microstates, distinct molecular arrangements consistent with what we can measure. The entropy is the logarithm of that count,

$$
S = k_B \ln W,
$$

with $k_B$ Boltzmann's constant, and an isolated system evolves toward the macrostate with the most microstates simply because that is overwhelmingly where the dice land.

It is worth doing the count once, with numbers small enough to hold in your head. Energy in a vibrating lattice comes in discrete quanta, so picture two tiny blocks of ice, each just three oscillators, sharing six quanta between them. The number of ways to arrange $q$ indistinguishable quanta among $N$ oscillators is a standard counting result, $W = \binom{q+N-1}{q}$, and multiplying the counts for the two blocks gives the number of microstates for each way of splitting the energy.

| $q_A$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| $W_A \cdot W_B$ | 28 | 63 | 90 | **100** | 90 | 63 | 28 |

Every one of the 462 microstates is equally likely; nothing prefers the even split. Yet the even split owns more microstates than any other, and if the blocks were real, with $10^{23}$ oscillators rather than three, the peak of this table would sharpen into a needle of relative width $\sim 1/\sqrt{N}$. Energy spreads out, and ice in a warm room ends up at the room's temperature, not because any force pushes it there but because the alternatives are statistically invisible.

The table also says *when* the spreading stops. The most probable split is the one where moving a quantum from block A to block B no longer increases the product $W_A W_B$, that is, where it no longer increases $\ln W_A + \ln W_B$. In the language of entropy, energy flows until

$$
\frac{\partial S_A}{\partial E_A} = \frac{\partial S_B}{\partial E_B},
$$

and this shared quantity is what temperature is. Define $1/T = \partial S/\partial E$, the rate at which a system's entropy buys energy, and the equation above becomes the familiar statement that two bodies in contact come to the same temperature. The definition explains the direction of heat flow rather than assuming it. A cold body is one whose entropy grows steeply with energy, so moving a joule from hot to cold creates more entropy in the receiver than it destroys in the donor, and the joule moves. Temperature is the exchange rate in that trade, and a thermometer lowered down a borehole is reading it; the temperature profiles of {doc}`../thermomechanics/thermal-structure` are maps of $\partial S/\partial E$ through an ice column.

The same derivative produces the most important distribution in this book. Let a single molecule, or any small system, exchange energy with a large reservoir, and ask for the probability of finding it in one particular microstate of energy $E$. That probability is proportional to the number of arrangements left to the reservoir, $W_R(E_{tot}-E) = e^{S_R(E_{tot}-E)/k_B}$, and because the system is small the reservoir's entropy can be expanded to first order, $S_R(E_{tot}-E) \approx S_R(E_{tot}) - E\,\partial S_R/\partial E = S_R(E_{tot}) - E/T$. The constant first term drops into the normalization, leaving the Boltzmann factor,

$$
p \propto e^{-E/k_B T}.
$$

Nothing here is specific to the system; the exponential is purely the price the reservoir's count pays to lend out energy $E$. The normalization, the sum of Boltzmann factors over all microstates, is the partition function $Z = \sum_i e^{-E_i/k_B T}$, from which every equilibrium property follows by differentiation {cite}`gibbs1902`. The free energy $F = -k_B T \ln Z$ packages the competition that decides phase equilibrium, since minimizing $F$ means trading energy against entropy, and that trade is exactly what the freezing point of the next section expresses.

Before leaving the counting, put scales on it. At 0 °C the thermal energy $RT$ is about 2.3 kJ/mol, while a hydrogen bond costs roughly 20 kJ/mol to break, so the Boltzmann factor for borrowing a bond's worth of energy is $e^{-20/2.3} \approx 10^{-4}$. That looks prohibitive until you recall that molecules attempt the move at vibrational frequencies near $10^{13}$ Hz, so any given bond still breaks millions of times per second. Ice near the melting point is solid by majority vote, not unanimity, and the rare fluctuations that win are what let it creep, diffuse, and trade molecules with the vapor.

Ice repays the statistical view almost immediately. The hydrogen atoms in the lattice of {doc}`../foundations/ice-structure` have many distinct arrangements obeying the local bonding rules, so ice retains a residual entropy even at absolute zero. Pauling counted the arrangements, $W \approx (3/2)^{N}$ for $N$ molecules, and his predicted residual entropy matched the calorimetric measurements, one of the early triumphs of the counting view of entropy and the cleanest evidence for the proton disorder behind the point defects of {doc}`../foundations/point-defects` {cite}`pauling1935`.

### Activation energy and the Arrhenius law

The Boltzmann factor also sets the pace of every slow process in ice. Processes that require a rare, energetic fluctuation, breaking a bond, hopping into a vacancy, rotating a molecule against its neighbors, proceed at rates proportional to the probability of borrowing the necessary energy from thermal fluctuations. Writing the required energy per mole as the activation energy $Q$ gives the Arrhenius law for the rate of any thermally activated process,

$$
\mathrm{rate} \propto e^{-Q/RT},
$$

with $R$ the gas constant. The exponential is brutal. For an activation energy typical of deformation in ice, the rate roughly doubles for every five degrees of warming near the melting point, which is why the rate factor $A$ in Glen's flow law, derived from the defect physics in {doc}`../foundations/point-defects` and used everywhere from {doc}`../ice_flow/ice-rheology` onward, makes ice at the melting point deform orders of magnitude faster than the cold ice of the polar plateaus. Whenever a chapter says "thermally activated," it means this equation, and behind it, the Boltzmann counting above.

## The freezing point

Ice, liquid water, and vapor are phases of one substance, and which phase wins at given temperature and pressure is settled by a competition between energy and entropy. The familiar 0 °C is nothing more than the temperature at which the free energies of ice and liquid water cross at atmospheric pressure; below it the crystal's lower energy wins, above it the liquid's greater entropy does, and a thermometer in an ice bath is reading the location of that crossing. Two phases coexist wherever their free energies match, and the coexistence lines in the pressure-temperature plane make up the phase diagram, with the melting line, the vapor-pressure curve, and the triple point where all three phases meet.

```{figure} figures/water-phase-diagram.png
:name: fig-water-phase-diagram
:width: 90%

The phase diagram of water across fourteen decades of pressure, with the many crystalline polymorphs of ice labelled by Roman numeral. Glaciology lives in a thin horizontal band around 1 bar, where the only players are vapor, liquid, and ordinary hexagonal ice Ih, but the wider view explains what is special about our corner, the nearly vertical melting line that tilts slightly *backward*, so that pressure favors the liquid. Figure from M. Chaplin's *Water Structure and Science*, reproduced from the UW ESS 431 course slides of K. Christianson.
```

The slope of a coexistence line follows from the Clausius-Clapeyron relation,

$$
\frac{dP}{dT} = \frac{L}{T\,\Delta v},
$$

where $L$ is the latent heat of the transition and $\Delta v$ the volume change per unit mass. Two of its consequences run through this book. Along the melting line, ice is anomalous, since melting *shrinks* water ($\Delta v < 0$), the slope is negative and pressure lowers the melting point, the fact that puts the bed of a thick ice sheet at its pressure-melting point in {doc}`../thermomechanics/thermal-structure` and makes the homologous temperature, measured relative to that local melting point, the natural argument of the flow law in {doc}`../ice_flow/ice-rheology`. Along the vapor curve, the saturation vapor pressure falls near-exponentially as air cools, which is why cooling air sheds moisture, why snow falls at all, and why the Rayleigh distillation of {doc}`../climate/paleoclimate` turns the isotopic composition of snow into a thermometer.

Latent heat itself deserves its moment. Melting ice absorbs 334 kJ/kg without warming at all, and sublimation absorbs nearly ten times that, energies that dominate the heat budgets of melting surfaces, refreezing firn, and the brine pockets of {doc}`../cryosphere/sea-ice`. Where a later chapter balances an energy budget, the largest entries are usually latent.

## What to carry forward

The molecule, temperature, and the freezing point, then, are all this chapter really contains. The tetrahedral sp³ geometry of H₂O sets the architecture of the ice crystal, and the polarity of its O–H bonds gives the hydrogen bond, which holds that crystal together and leaves it proton-disordered. Entropy counts microstates, temperature is the rate at which entropy buys energy, and the Boltzmann factor that follows makes every rate in ice exponentially temperature-dependent through the Arrhenius law. And the freezing point is a free-energy crossing, movable by pressure through Clausius-Clapeyron, which is what ties the beds of thick ice sheets, falling snow, and the isotope thermometer of the climate chapters to the same diagram. None of this is specific to glaciology, and all of it is load-bearing.
