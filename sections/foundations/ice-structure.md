# The structure of ice

The previous chapter ended with the hydrogen bond: each water molecule, with two protons and two lone pairs arranged tetrahedrally, can bond to four neighbors. This chapter follows that bonding rule to its consequence, the crystal structure of ordinary ice, and the proton disorder hidden within it. The treatment again follows {cite}`fletcher1970`.

## Hexagonal ice

At the temperatures and pressures found in glaciers and ice sheets, water freezes into hexagonal ice, known as ice Ih. The structure is the direct expression of the tetrahedral hydrogen bond. Every oxygen atom sits at the center of a tetrahedron formed by four neighboring oxygen atoms, joined to each by a hydrogen bond, with an oxygen-to-oxygen distance of about 2.76 angstroms. These tetrahedra link into puckered hexagonal layers, and the layers stack one above another to fill space.

```{figure} figures/tetrahedral-coordination.png
:name: fig-tetrahedral-coordination
:width: 50%

One molecule and its four hydrogen-bonded neighbors, with the tetrahedron they define shown at upper right. The 0.28 nm spacing is the oxygen-to-oxygen distance of the bond, and the 109.47° angle is the tetrahedral angle derived in the exercise of {doc}`water-molecule`. Repeat this motif through space and the lattice below follows.
```

```{figure} figures/ice-ih-lattice.png
:name: fig-ice-ih-lattice
:width: 65%

The ice Ih lattice, oxygens in red and protons in blue, viewed obliquely so the puckered hexagonal rings and the open channels through them are visible. The emptiness of the structure is the point, since it is why ice floats on its own melt.
```

Because the tetrahedral framework holds the molecules well apart, the structure is open, with a good deal of empty space between the molecules. This is why ice is less dense than the liquid water it forms from, and why ice floats. That single fact, a consequence of the bonding geometry of one molecule, is among the most consequential in Earth science, since it is why ice shelves and sea ice float on the ocean rather than sinking, and why lakes freeze from the top down.

## The c-axis and basal planes

The stack of hexagonal layers gives the crystal one special direction: the axis of hexagonal symmetry, perpendicular to the layers, called the c-axis. The layers themselves are the basal planes. This single axis of symmetry is the source of the crystal's anisotropy, the fact that its properties depend on direction.

```{figure} figures/snow-crystal-libbrecht.jpg
:name: fig-snow-crystal
:width: 55%

The lattice made visible. A snow crystal grows fastest along the six directions the basal plane prefers, so its six-fold symmetry is the hexagonal unit cell expressed at a scale you can see with a hand lens, photographed through a microscope. Photograph by K. Libbrecht (snowcrystals.com).
```

The mechanical consequence is that ice deforms far more easily by gliding along its basal planes than across them, in the way a deck of cards shears. A single ice crystal is therefore strongly directional in its response to stress, and the direction of its c-axis records the direction in which it is stiff. This is the molecular origin of the single-crystal anisotropy behind Glen's flow law in {doc}`../ice_flow/ice-rheology`, and it is why the distribution of c-axis orientations, the crystal fabric of {doc}`../ice_flow/ice-fabric`, exerts so strong a control on how ice sheets flow. The same axis makes the electrical permittivity of ice different along and across the c-axis, the dielectric anisotropy that lets radar sense fabric through birefringence, as shown in {doc}`../radar/radiowave-fabric`.

## Proton disorder

The oxygen atoms occupy a fixed, ordered lattice, but the hydrogen atoms do not. Each hydrogen bond between two oxygens holds a single proton, and that proton sits closer to one of the two oxygens than to the other. Which side it occupies is, to a good approximation, random, subject only to two constraints known as the Bernal-Fowler ice rules: there is exactly one proton on each oxygen-oxygen bond, and exactly two protons lie close to each oxygen, so that every molecule remains a recognizable, intact water molecule.

An enormous number of proton arrangements satisfy these rules. As a result the crystal retains a configurational entropy even as its temperature falls toward absolute zero, in apparent tension with the third law of thermodynamics. Pauling estimated this residual entropy by a simple counting argument as $R\ln(3/2)$, about 3.4 joules per mole per kelvin, and calorimetric measurements agree closely. Ordinary ice is, in this precise sense, a disordered crystal: ordered in its oxygen framework, disordered in its protons.

## Consequences of proton disorder

Protons can move between allowed configurations through point defects in the lattice, the small departures from the ideal structure that let molecules reorient and migrate. It is through these defects that the proton disorder becomes physically active: their slow migration lets the protons rearrange in response to an applied field, which is the origin of the dielectric relaxation and weak electrical conductivity of ice, and it is also what allows a dislocation to advance and the crystal to flow. The defects therefore connect the static structure to both the radar methods used to study ice and the creep that makes it move. Because they carry so much of the story, they are treated on their own in {doc}`point-defects`, after the lattice vibrations that set them in motion.

## Premelting

A molecule at the free surface cannot complete its four hydrogen bonds; it sits in an under-coordinated environment with no counterpart in the bulk crystal. Below but near the melting point, the crystal lowers its total free energy by sacrificing crystalline order in a thin surface layer, trading bulk freezing energy for relief of the surface frustration, and the result is a film of disordered, liquid-like water on ice that is otherwise well below 0 °C. This is premelting, and it is equilibrium thermodynamics rather than a defect or a contamination. The film is detectable tens of degrees below the melting point, is of nanometre scale by around −10 °C, and thickens steeply as the temperature climbs through the final degrees toward 0 °C, with measured thicknesses that depend on technique and on impurities but with the trend itself beyond doubt.

The same logic operates at internal interfaces. A grain boundary in polycrystalline ice is a sheet of geometric frustration between two misoriented lattices, and it premelts for the same reason the surface does; where three grains meet, the liquid collects into veins, and where four meet, into nodes, so that polycrystalline ice near its melting point is threaded by a connected network of microscopic water channels along its grain edges. Impurities amplify all of this, because dissolved ions are nearly insoluble in the lattice itself, are rejected to the boundaries as the ice grows, and depress the freezing point of the boundary liquid they concentrate in. The interior of a glacier close to the pressure-melting point is therefore not a dry solid but a wet composite, crystal grains sheathed in films and stitched together by veins.

The slipperiness of ice under a skate or a boot is the premelted film doing mechanical work. The sintering of snow, by which loose crystals weld into firn in {doc}`snow-to-ice`, runs through liquid and vapor transport at premelted contacts. Regelation, the melt-and-refreeze mechanism by which a glacier slides past small bumps in {doc}`../thermomechanics/basal-motion`, is premelting physics at the bed, and the few percent of liquid water held in temperate ice, which softens the rheology and feeds the drainage system in {doc}`../thermomechanics/thermal-structure` and {doc}`../thermomechanics/hydrology`, occupies exactly the vein network described above. Even the chemistry of ice cores depends on it, since the impurities that {doc}`../climate/paleoclimate` reads as volcanic and climatic signals reside largely in the boundary liquid rather than the lattice, which is also where the electrical conduction that ice-penetrating radar senses takes place. The lattice of this chapter sets the rules, but much of the action in a real glacier happens in the disordered few nanometres where the lattice gives out.

## Summary

Ice can take many other crystal structures at high pressure, more than a dozen distinct phases, but within glaciers and ice sheets the pressures are far too low to reach them, and the ice is ice Ih throughout. From the bent water molecule, then, follow the open tetrahedral crystal that floats, the symmetry axis that shapes how ice flows and how fabric forms, the proton disorder that governs how ice responds both to an electric field and to a shearing stress, and, wherever the lattice meets a surface or a neighbor grain, the premelted liquid that lets a solid well below its melting point behave, in thin and consequential layers, like water.
