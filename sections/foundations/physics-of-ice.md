# The water molecule and the structure of ice

Almost every property of ice that matters to a glaciologist can be traced to the shape of a single molecule and the way those molecules bond together. Before we treat ice as a flowing continuum, it is worth seeing where its behavior comes from at the molecular scale. This chapter reviews the water molecule and the crystal structure of ordinary ice, following the classic account of {cite}`fletcher1970`.

## The water molecule

A water molecule is one oxygen atom bonded to two hydrogen atoms, and it is bent rather than straight. The two bonds meet at an angle of about 105 degrees, and each oxygen-hydrogen bond is roughly one angstrom long. The bonds form from the overlap of the oxygen atom's outer 2p orbitals with the hydrogen 1s orbitals. A naive version of this picture would put the bonds at right angles, but the two bonds are polar and repel one another, and the oxygen orbitals hybridize in response, which opens the angle and leaves the oxygen with an approximately tetrahedral arrangement of charge.

The useful way to picture the result is as a small tetrahedron centered on the oxygen with four arms pointing toward its corners. Two of the arms are the bonds to the hydrogen atoms, which carry a slight positive charge, and the other two are lone pairs of electrons, which carry a slight negative charge. The molecule as a whole is electrically neutral but strongly polar, with a positive side and a negative side.

## The hydrogen bond

The tetrahedral pattern of two positive and two negative arms is what lets water molecules link together. Each molecule can form four hydrogen bonds with its neighbors: its two hydrogen atoms reach toward the lone pairs of two neighbors, and its two lone pairs accept a hydrogen from two other neighbors. A hydrogen bond, written O-H...O, is weaker than the covalent bond inside the molecule but far stronger than ordinary intermolecular attraction, and it is directional. This combination of four bonds per molecule and a fixed bonding geometry is responsible for the open, rigid framework of ice and for its unusually high melting point.

## The structure of ordinary ice

At the temperatures and pressures found in glaciers, water freezes into hexagonal ice, known as ice Ih. Every oxygen atom sits at the center of a tetrahedron formed by four neighboring oxygens, joined to each by a hydrogen bond, and the oxygens are arranged in puckered hexagonal layers stacked on top of one another. Because the tetrahedral framework is so open, ice is less dense than the liquid it floats on, which is one of the most consequential facts in all of Earth science.

The stack of hexagonal layers gives the crystal a single special direction, the symmetry axis perpendicular to the layers, called the c-axis. The layers themselves are the basal planes. This one axis of symmetry is the source of the crystal's anisotropy. The ice deforms most readily by glide along its basal planes, which is the molecular origin of the strong single-crystal anisotropy behind Glen's flow law in {doc}`../ice_flow/ice-rheology` and the crystal fabric of {doc}`../ice_flow/ice-fabric`. The same axis makes the electrical permittivity of the crystal different along and across the c-axis, which is what allows radar to sense fabric through birefringence, as developed in {doc}`../radar/radiowave-fabric`.

## Proton disorder

There is a subtlety in the structure that has wide consequences. The oxygen atoms occupy a fixed, ordered lattice, but the hydrogen atoms do not. Each hydrogen bond between two oxygens holds a single proton that sits closer to one oxygen than the other, and the choice of which side is, to a good approximation, random. The allowed arrangements follow the Bernal-Fowler ice rules: exactly one hydrogen lies on each oxygen-oxygen bond, and exactly two hydrogens sit close to each oxygen, so that every molecule remains a recognizable water molecule.

An enormous number of proton arrangements satisfy these rules, so the crystal keeps a configurational entropy even as its temperature approaches absolute zero. Pauling estimated this residual entropy as $R\ln(3/2)$, about 3.4 joules per mole per kelvin, and measurements agree. This proton disorder, and the defects that allow protons to move between allowed configurations, govern the dielectric response of ice, including its response to the oscillating electric field of a radar wave. From a single bent molecule, then, follow the anisotropy that shapes ice flow, the low density that floats ice shelves, and the dielectric behavior that lets us see fabric from the air.
