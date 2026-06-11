# The structure of ice

The previous chapter ended with the hydrogen bond: each water molecule, with two protons and two lone pairs arranged tetrahedrally, can bond to four neighbors. This chapter follows that bonding rule to its consequence, the crystal structure of ordinary ice, and the proton disorder hidden within it. The treatment again follows {cite}`fletcher1970`.

## Hexagonal ice

At the temperatures and pressures found in glaciers and ice sheets, water freezes into hexagonal ice, known as ice Ih. The structure is the direct expression of the tetrahedral hydrogen bond. Every oxygen atom sits at the center of a tetrahedron formed by four neighboring oxygen atoms, joined to each by a hydrogen bond, with an oxygen-to-oxygen distance of about 2.76 angstroms. These tetrahedra link into puckered hexagonal layers, and the layers stack one above another to fill space.

```{figure} figures/tetrahedral-coordination.png
:name: fig-tetrahedral-coordination
:width: 50%

One molecule and its four hydrogen-bonded neighbors, with the tetrahedron they define shown at upper right. The 0.28 nm spacing is the oxygen-to-oxygen distance of the bond, and the 109.47° angle is the tetrahedral angle derived in the exercise of {doc}`water-molecule`. Repeat this motif through space and the lattice below follows. Reproduced from the UW ESS 431 course slides of K. Christianson.
```

```{figure} figures/ice-ih-lattice.png
:name: fig-ice-ih-lattice
:width: 65%

The ice Ih lattice, oxygens in red and protons in blue, viewed obliquely so the puckered hexagonal rings and the open channels through them are visible. The emptiness of the structure is the point, since it is why ice floats on its own melt. Reproduced from the UW ESS 431 course slides of K. Christianson.
```

Because the tetrahedral framework holds the molecules well apart, the structure is open, with a good deal of empty space between the molecules. This is why ice is less dense than the liquid water it forms from, and why ice floats. That single fact, a consequence of the bonding geometry of one molecule, is among the most consequential in Earth science, since it is why ice shelves and sea ice float on the ocean rather than sinking, and why lakes freeze from the top down.

## The c-axis and basal planes

The stack of hexagonal layers gives the crystal one special direction: the axis of hexagonal symmetry, perpendicular to the layers, called the c-axis. The layers themselves are the basal planes. This single axis of symmetry is the source of the crystal's anisotropy, the fact that its properties depend on direction.

```{figure} figures/snow-crystal-libbrecht.jpg
:name: fig-snow-crystal
:width: 55%

The lattice made visible. A snow crystal grows fastest along the six directions the basal plane prefers, so its six-fold symmetry is the hexagonal unit cell expressed at a scale you can see with a hand lens, photographed through a microscope. Photograph by K. Libbrecht (snowcrystals.com), reproduced from the UW ESS 431 course slides.
```

The mechanical consequence is that ice deforms far more easily by gliding along its basal planes than across them, in the way a deck of cards shears. A single ice crystal is therefore strongly directional in its response to stress, and the direction of its c-axis records the direction in which it is stiff. This is the molecular origin of the single-crystal anisotropy behind Glen's flow law in {doc}`../ice_flow/ice-rheology`, and it is why the distribution of c-axis orientations, the crystal fabric of {doc}`../ice_flow/ice-fabric`, exerts so strong a control on how ice sheets flow. The same axis makes the electrical permittivity of ice different along and across the c-axis, the dielectric anisotropy that lets radar sense fabric through birefringence, as shown in {doc}`../radar/radiowave-fabric`.

## Proton disorder

There is an important subtlety in the structure. The oxygen atoms occupy a fixed, ordered lattice, but the hydrogen atoms do not. Each hydrogen bond between two oxygens holds a single proton, and that proton sits closer to one of the two oxygens than to the other. Which side it occupies is, to a good approximation, random, subject only to two constraints known as the Bernal-Fowler ice rules: there is exactly one proton on each oxygen-oxygen bond, and exactly two protons lie close to each oxygen, so that every molecule remains a recognizable, intact water molecule.

An enormous number of proton arrangements satisfy these rules. As a result the crystal retains a configurational entropy even as its temperature falls toward absolute zero, in apparent tension with the third law of thermodynamics. Pauling estimated this residual entropy by a simple counting argument as $R\ln(3/2)$, about 3.4 joules per mole per kelvin, and calorimetric measurements agree closely. Ordinary ice is, in this precise sense, a disordered crystal: ordered in its oxygen framework, disordered in its protons.

## Why disorder matters

The proton arrangement is not frozen for all time. Protons can move between allowed configurations through point defects in the lattice, the small departures from the ideal structure that let molecules reorient and migrate. It is through these defects that the proton disorder becomes physically active: their slow migration lets the protons rearrange in response to an applied field, which is the origin of the dielectric relaxation and weak electrical conductivity of ice, and it is also what allows a dislocation to advance and the crystal to flow. The defects therefore connect the static structure to both the radar methods used to study ice and the creep that makes it move. Because they carry so much of the story, they are treated on their own in {doc}`point-defects`, after the lattice vibrations that set them in motion.

Ice can take many other crystal structures at high pressure, more than a dozen distinct phases, but within glaciers and ice sheets the pressures are far too low to reach them, and the ice is ice Ih throughout. From the bent water molecule, then, follow the open tetrahedral crystal that floats, the symmetry axis that shapes how ice flows and how fabric forms, and the proton disorder that governs how ice responds both to an electric field and to a shearing stress.
