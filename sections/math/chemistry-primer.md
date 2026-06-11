# A chemistry primer

The first part of this book builds glacier physics from the molecule up, and that construction leans on a handful of ideas from chemistry, the shapes of electron orbitals, the polarity of bonds, the energetics of thermally activated processes, and the equilibrium between phases. This chapter collects them in one place, in the same spirit as the mathematical chapters beside it. A reader comfortable with introductory chemistry can skim it and move on; a reader who last saw orbitals long ago should find everything here that the ice chapters assume. The chemical physics of ice itself is treated comprehensively in {cite}`fletcher1970` and {cite}`petrenko1999`.

## Orbitals and the shape of a molecule

An electron bound to a nucleus does not orbit it like a planet. It occupies an orbital, a standing-wave pattern with a characteristic shape and energy, and the shapes matter because they decide the geometry of molecules. The lowest orbitals are spherical (the s orbitals), the next are dumbbell-shaped along three perpendicular axes (the p orbitals), and each holds at most two electrons.

Oxygen brings eight electrons. Two sit deep in the inner shell, leaving six in the outer shell, which mixes its one s and three p orbitals into four equivalent hybrid orbitals, the sp³ set, pointing toward the corners of a tetrahedron. Two of the four hold lone pairs of electrons; the other two are half-filled and bond to hydrogen atoms. The result is the familiar bent water molecule, with its two O–H bonds at about 104.5°, slightly pinched from the ideal tetrahedral angle of 109.5° by the bulkier lone pairs. The tetrahedral disposition of two bonds and two lone pairs is the single most consequential geometric fact in this book, because it is what lets each water molecule connect to four neighbors and build the open lattice of {doc}`../foundations/ice-structure`.

## Electronegativity and the polar bond

Atoms do not share electrons evenly. Electronegativity measures how strongly an atom pulls shared electrons toward itself, and oxygen is among the most electronegative of the elements while hydrogen is middling. Each O–H bond is therefore polar covalent, with the shared electrons displaced toward the oxygen, leaving a partial negative charge on the oxygen and partial positive charges on the hydrogens. Because the molecule is bent rather than linear, the bond polarities do not cancel, and the molecule carries a permanent dipole moment. The dipole is why water dissolves salts, why the dielectric constant that {doc}`../radar/em-waves` exploits is so large, and, above all, why water molecules grip one another.

That grip is the hydrogen bond. A hydrogen nucleus, bonded to one oxygen and stripped of most of its electron cloud by it, is attracted to the lone pair of a neighboring molecule's oxygen. The resulting bond is about a tenth as strong as the covalent O–H bond, roughly 20 kJ/mol against nearly 500, strong enough to organize molecules into a tetrahedral network and weak enough to break and re-form readily. Nearly every anomaly of water and ice, the open low-density crystal, the high melting point for so light a molecule, the proton disorder behind the point defects of {doc}`../foundations/point-defects`, is hydrogen bonding expressing itself, and the details are taken up in {doc}`../foundations/water-molecule`.

## Boltzmann, activation energy, and Arrhenius

Much of glacier physics is the statistics of jostling molecules, and one formula carries most of it. At temperature $T$, the probability that a molecule finds itself with energy $E$ above the typical thermal energy is proportional to the Boltzmann factor

$$
p \propto e^{-E/k_B T},
$$

where $k_B$ is Boltzmann's constant. Processes that require a rare, energetic fluctuation, breaking a bond, hopping into a vacancy, rotating a molecule against its neighbors, therefore proceed at rates that depend exponentially on temperature. Writing the required energy per mole as the activation energy $Q$ gives the Arrhenius law for the rate of any thermally activated process,

$$
\mathrm{rate} \propto e^{-Q/RT},
$$

with $R$ the gas constant. The exponential is brutal. For an activation energy typical of deformation in ice, the rate roughly doubles for every five degrees of warming near the melting point, which is why the rate factor $A$ in Glen's flow law, derived from the defect physics in {doc}`../foundations/point-defects` and used everywhere from {doc}`../ice_flow/ice-rheology` onward, makes ice at the melting point deform orders of magnitude faster than the cold ice of the polar plateaus. Whenever a chapter says "thermally activated," it means this equation.

## Phases in equilibrium

Ice, liquid water, and vapor are phases of one substance, and which phase wins at given temperature and pressure is settled by a competition between energy and entropy. Two phases coexist where their free energies match, and the coexistence lines in the pressure-temperature plane make up the phase diagram, with the melting line, the vapor-pressure curve, and the triple point where all three phases meet.

The slope of a coexistence line follows from the Clausius-Clapeyron relation,

$$
\frac{dP}{dT} = \frac{L}{T\,\Delta v},
$$

where $L$ is the latent heat of the transition and $\Delta v$ the volume change per unit mass. Two of its consequences run through this book. Along the melting line, ice is anomalous, since melting *shrinks* water ($\Delta v < 0$), the slope is negative and pressure lowers the melting point, the fact that puts the bed of a thick ice sheet at its pressure-melting point in {doc}`../thermomechanics/thermal-structure`. Along the vapor curve, the saturation vapor pressure falls near-exponentially as air cools, which is why cooling air sheds moisture, why snow falls at all, and why the Rayleigh distillation of {doc}`../climate/paleoclimate` turns the isotopic composition of snow into a thermometer.

Latent heat itself deserves its moment. Melting ice absorbs 334 kJ/kg without warming at all, and sublimation absorbs nearly ten times that, energies that dominate the heat budgets of melting surfaces, refreezing firn, and the brine pockets of {doc}`../cryosphere/sea-ice`. Where a later chapter balances an energy budget, the largest entries are usually latent.

## What to carry forward

Four ideas, then, underwrite the molecular chapters that follow. The tetrahedral sp³ geometry of the water molecule sets the architecture of the ice crystal. The polarity of the O–H bond gives the hydrogen bond, which holds the crystal together and leaves it disordered. The Boltzmann factor makes every rate in ice exponentially temperature-dependent through the Arrhenius law. And phase equilibrium, through Clausius-Clapeyron, ties melting and evaporation to pressure and temperature. None of this is specific to glaciology, and all of it is load-bearing.
