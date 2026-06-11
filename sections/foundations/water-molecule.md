# The water molecule

Everyone arrives at this book already knowing the main character. Water is H₂O, two hydrogens on an oxygen, and nearly every property of ice that matters to a glaciologist can be traced to that one small molecule and the way copies of it bond to one another. Ice is among the simplest molecular solids, and its unusual behavior, the open low-density structure, the mechanical and electrical anisotropy of the crystal, the high melting point, all follow from the structure of the molecule. This chapter reviews it in some detail, following the account of {cite}`fletcher1970`, before the next chapter assembles many molecules into the crystal. No chemistry beyond this chapter is assumed anywhere in the book, so a reader who last saw orbitals long ago should find everything here that the later chapters lean on.

## Shape and size

A water molecule is bent. That it is triangular rather than linear was known long before modern spectroscopy, from the specific heat of water vapor: the measured heat capacity near room temperature implies contributions from three rotational degrees of freedom with appreciable moments of inertia, which a linear molecule could not provide. Spectroscopy later fixed the geometry precisely. In its equilibrium configuration the oxygen-hydrogen bond length is 0.958 angstroms and the H-O-H angle is 104 degrees and 27 minutes, close to 104.5 degrees. In the lowest vibrational state, which is the relevant one at glacier temperatures, the values shift slightly, to an angle near 105 degrees. The angle is notably smaller than the 109.5 degrees of a perfect tetrahedron, a point we return to below.

```{figure} ../math/figures/water-molecule-geometry.png
:name: fig-water-molecule-geometry
:width: 55%

The bent molecule, with bond length, bond angle, and the partial charges left by the uneven tug-of-war over the shared electrons. The values shown come from an electronic-structure model and differ slightly from the measured gas-phase geometry quoted in the text; the angle is soft, and the section on vibrations explains why. Figure from M. Chaplin's *Water Structure and Science*.
```

## Electronic structure

An electron bound to a nucleus does not orbit it like a planet. It occupies an orbital, a standing-wave pattern with a characteristic shape and energy, and the shapes matter because they decide the geometry of molecules. The lowest orbitals are spherical, the s orbitals; the next are dumbbell-shaped along three perpendicular axes, the p orbitals; and each holds at most two electrons. Everything in this section is bookkeeping with these shapes.

The oxygen atom has the electron configuration $(1s)^2(2s)^2(2p)^4$, so it is the outer 2p electrons that form bonds. Two of them pair with the 1s electrons of the two hydrogen atoms, forming bonding orbitals concentrated between the nuclei, while the rest remain as non-bonding lone pairs. A first, crude version of this picture, using only the two 2p orbitals for bonding, would predict a right angle between the bonds. The bonds are polar, however, with positive charge on the hydrogen side, so they repel one another, and the oxygen orbitals respond by mixing in some 2s character. This hybridization opens the angle toward the observed value and leaves the oxygen with an approximately tetrahedral arrangement of four orbitals: two bonding pairs pointing toward the hydrogen atoms and two lone pairs pointing away from them.

A more careful treatment classifies the molecular orbitals by the symmetry of the molecule, which belongs to the point group $C_{2v}$: it has a twofold rotation axis bisecting the H-O-H angle and two reflection planes. The orbitals fall into symmetry classes labelled $A_1$, $B_1$, and $B_2$, and the ground-state configuration fills the lowest of them. Two of the filled orbitals are the lone pairs. One, of $A_1$ symmetry, is directed along the symmetry axis away from the hydrogens, and the other, of $B_1$ symmetry, is a nearly pure oxygen 2p orbital sticking out of the plane of the molecule. The calculated orbital energies agree reasonably well with the ionization energies measured by electron impact and by photoelectron spectroscopy, which gives confidence that this picture captures the real electronic structure.

The whole story of the bond angle, from the crude right-angle prediction to the measured 104.5°, can be told with vectors and one orthogonality condition, and it is worth telling yourself once with a pencil.

```{admonition} Exercise — the angle between the hydrogens
:class: tip

The text claims that pure p bonding predicts a 90° angle, that perfect sp³ hybrids predict 109.47°, and that the real molecule sits between. Derive all three.

(a) Four equivalent sp³ hybrids point toward alternating corners of a cube centered on the oxygen. Write unit vectors for two of them, for instance toward $(1,1,1)$ and $(1,-1,-1)$, and compute the angle between them.

(b) Model each O-H bonding orbital as a normalized mixture of the oxygen 2s orbital and a 2p orbital pointing along the bond direction $\hat{\mathbf{b}}_i$,

$$
\psi_i = \frac{s + \lambda\, p_i}{\sqrt{1+\lambda^2}},
$$

where the mixing parameter $\lambda$ measures p character and the p orbitals satisfy $\langle p_1 | p_2 \rangle = \hat{\mathbf{b}}_1 \cdot \hat{\mathbf{b}}_2 = \cos\theta$. Hybrids on the same oxygen must be orthogonal. Show that this requires

$$
\cos\theta = -\frac{1}{\lambda^2},
$$

and check that pure p bonding ($\lambda \to \infty$) and equal sharing among four hybrids ($\lambda^2 = 3$) reproduce the two limits of part (a).

(c) The measured angle is 104.5°. What $\lambda^2$ does that imply for the bonding orbitals? The molecule has one 2s orbital to distribute among four hybrids, so if each bond uses an s fraction $1/(1+\lambda^2)$, what fraction is left for each lone pair, and at what angle do the two lone pairs sit?
```

```{admonition} Solution
:class: dropdown

(a) The dot product of $(1,1,1)/\sqrt{3}$ and $(1,-1,-1)/\sqrt{3}$ is $(1-1-1)/3 = -1/3$, so $\theta = \arccos(-1/3) = 109.47°$.

(b) Orthogonality gives $\langle \psi_1 | \psi_2 \rangle = (1 + \lambda^2 \cos\theta)/(1+\lambda^2) = 0$, hence $\cos\theta = -1/\lambda^2$. With $\lambda \to \infty$ the angle goes to $\arccos(0) = 90°$, the pure-p limit, and with $\lambda^2 = 3$ it returns $\arccos(-1/3)$.

(c) $\lambda^2 = -1/\cos(104.5°) \approx 4.0$, so each bonding hybrid is one part s to four parts p, an s fraction of $1/(1+\lambda^2) = 20\%$ rather than the 25% of perfect sp³. The two bonds together use 40% of the s orbital, leaving 30% for each lone pair; setting $1/(1+\mu^2) = 0.3$ gives $\mu^2 = 7/3$ for the lone-pair hybrids, which sit at $\arccos(-3/7) \approx 115°$. Squeezing the bonds together spreads the lone pairs apart, which is the orbital version of the repulsion argument in the text. The bending force constant of the next section is small, so none of these angles is rigid, and the molecule in ice relaxes back toward the tetrahedral 109.5° that the lattice prefers.
```

## Charge distribution and electric moments

Atoms do not share electrons evenly. Electronegativity measures how strongly an atom pulls shared electrons toward itself, and oxygen is among the most electronegative of the elements while hydrogen is middling. Each O-H bond is therefore polar covalent, with the shared electrons displaced toward the oxygen, leaving a partial negative charge on the oxygen and partial positive charges on the hydrogens.

The molecule is electrically neutral, but because the bonds are polar and the lone pairs are offset to one side, it carries a permanent electric dipole moment. In the vapor phase that moment is about 1.84 debye. A useful and somewhat surprising result of detailed calculations is that a large part of the dipole comes from the lone-pair electrons rather than from the polarity of the O-H bonds alone, so much so that the lone-pair contribution can outweigh the bond contribution. The molecule also has nonzero higher electric moments, a quadrupole and an octupole, which are weaker but still matter when molecules approach closely, as they do in the crystal.

The tidy cartoon of two positive arms and two sharp negative lone-pair lobes should be treated with care. When the electron density is calculated directly, the density at the proton is roughly twenty percent greater than in an isolated hydrogen atom, while the lone-pair charge is not concentrated into two neat lobes at all. Instead it forms a diffuse ridge of negative charge spread perpendicular to the plane of the molecule. The tetrahedral picture is a guide to the bonding directions, not a literal map of the charge.

One more feature is important for what follows. The dipole moment of a water molecule is not fixed. Placed in the electric field of its neighbors, the molecule's electron cloud distorts and its dipole grows. The polarizability that governs this response is about $1.5\times10^{-24}$ cubic centimeters, a fairly low value consistent with the molecule's moderately high ionization energy. In the condensed phases, where every molecule sits in the field of several hydrogen-bonded neighbors, this induced enhancement raises the effective dipole well above the vapor value, which in turn strengthens the hydrogen bonds. The bonding in ice is therefore cooperative, and the molecule in the crystal is not quite the same as the molecule in isolation.

## Molecular vibrations

With three nuclei the molecule has three internal vibrational degrees of freedom, and these correspond to three normal modes. The first, $\nu_1$, is a symmetric stretch in which both O-H bonds lengthen and shorten together. The second, $\nu_2$, is a bending of the H-O-H angle. The third, $\nu_3$, is an asymmetric stretch in which one bond lengthens as the other shortens. Their frequencies, expressed as wavenumbers, are about 3652, 1595, and 3756 inverse centimeters respectively, so the two stretching modes lie near a wavelength of three micrometers and the bending mode near six micrometers.

The stiffness of these motions is described by force constants, and they reveal something useful. The constant resisting bond stretching is about $8.5\times10^{5}$ dynes per centimeter, while the constant resisting bending of the angle is only about $0.8\times10^{5}$, roughly an order of magnitude smaller. The H-O-H angle is, in other words, soft. This is why the bond angle is hard to predict from first principles, since a small error in the energy translates into a large change in the computed angle, and it is also why the angle adjusts when the molecule is placed in the differing environments of vapor, liquid, and ice.

## Spectral properties

The energy levels of the molecule produce absorptions across the spectrum, and each region reports on a different aspect of its structure. The largest energy changes are electronic and appear in the ultraviolet. The vibrational modes absorb in the infrared, the bending mode near six micrometers and the two stretches near three, and because each mode changes the dipole moment it produces a strong absorption band. Because the molecule has a permanent dipole it also has a pure rotational spectrum in the far infrared, where it absorbs by changing its rotational state alone. Taken together these absorptions make water vapor one of the strongest infrared absorbers in the atmosphere, alongside carbon dioxide and ozone, which is the molecular root of its role in the planet's radiation balance. In the solid the same vibrational and dielectric responses persist, shifted by the hydrogen bonding, so the spectra of ice carry a record of the bonding environment.

## Forces between molecules

Water molecules attract one another in several ways. Setting aside the hydrogen bond for a moment, there are the ordinary van der Waals interactions common to all molecules. Permanent dipoles attract on average even as the molecules rotate, an interaction that falls off as the inverse sixth power of separation and weakens with temperature. A permanent dipole also polarizes its neighbor and is attracted to the dipole it induces, the induction force. And even molecules with no permanent dipole attract through dispersion forces, which arise because the instantaneous dipole of a molecule fluctuates even when its average is zero, and these fluctuations correlate between neighbors. All three of these fall off as the inverse sixth power of distance.

These forces are real but secondary. What dominates the behavior of water in the condensed phases is a stronger and more specific interaction between neighbors, the hydrogen bond.

## The hydrogen bond and bonding to neighbors

When two water molecules approach so that a hydrogen of one points toward a lone pair of the other, they form a hydrogen bond, written O-H...O. The hydrogen already carries a partial positive charge, because its electron has been drawn toward the oxygen it is covalently bound to, and it is attracted to the concentration of negative charge on the lone pair of its neighbor. The bond is therefore largely electrostatic. It is not only electrostatic, however. There is also a small amount of charge transfer and orbital overlap between the two molecules, a partial covalency, and this contribution is what gives the hydrogen bond its strong preference for a straight, linear O-H...O geometry rather than a bent one.

In strength the hydrogen bond sits between the weak van der Waals forces and the strong covalent bond inside the molecule. A single hydrogen bond in ice is worth a few kilocalories per mole, roughly a quarter of an electron volt. That is perhaps twenty times a typical van der Waals attraction but about an order of magnitude weaker than the covalent O-H bond, whose dissociation energy is several electron volts. This intermediate strength is the source of water's peculiarities. The bonds are strong enough to impose a definite structure and to give water its high melting and boiling points and its large latent heats, yet weak enough to break and reform continually, which is in turn why ice can deform under stress and why its protons can rearrange.

The geometry of the molecule fixes how many neighbors it bonds to. Each molecule carries two hydrogens that can donate bonds and two lone pairs that can accept them, and these four arms point toward the corners of a tetrahedron. A molecule therefore bonds to four neighbors, donating to two of them and accepting from the other two, and because the bonds prefer to be straight, those four neighbors sit at roughly tetrahedral angles. This fourfold tetrahedral coordination, repeated through space, is what builds the crystal of the next chapter, and the openness of the arrangement, with a large empty volume between molecules, is the reason ice is less dense than the water it freezes from.

```{figure} ../math/figures/hydrogen-bond-network.gif
:name: fig-hydrogen-bond-network
:width: 55%

The four-armed motif. Each δ+ hydrogen points at a δ− lone pair of a neighbor (dashed bonds), so the central molecule donates two hydrogen bonds and accepts two more.
```

The bonding is also cooperative. A molecule placed in the field of its hydrogen-bonded neighbors has its electron cloud distorted and its dipole moment enhanced, from about 1.84 debye in isolation to roughly 2.6 debye in ice. A larger dipole makes a stronger hydrogen bond, which polarizes the next molecule a little more, so the bonds reinforce one another and the network is more than a collection of independent pairs. This cooperativity is part of why a hydrogen bond in bulk ice is stronger than one measured between an isolated pair of molecules in the vapor, and it is what makes the tetrahedral network of the next chapter so stable.

## Why this matters for glaciology

It is worth keeping in view how directly these molecular facts shape the ice that glaciologists study. The polar molecule and its lone pairs make the hydrogen bond, which builds the open tetrahedral crystal, which is why ice is less dense than water and floats. The single symmetry axis of that crystal, inherited from the bonding geometry, gives the strong directional anisotropy that underlies Glen's flow law in {doc}`../ice_flow/ice-rheology` and the crystal fabric of {doc}`../ice_flow/ice-fabric`. The polarizability and the dielectric response of the molecule set the permittivity of ice, and its anisotropy along and across the symmetry axis is what lets radar sense fabric through birefringence, as developed in {doc}`../radar/radiowave-fabric`. Even the strength of the hydrogen bond reappears later as the energy scale that sets the melting point and the activation energy for creep.
