# The water molecule

To properly understand the behavior of a complex system, an ice sheet or glacier, we must first appreciate the structure and the physical and chemical properties of the elementary units from which it is composed. 

## Shape and size

The water molecule is triangular in shape. The triangular rather than linear structure of the molecule was known long before modern electron microscopy, from the specific heat of water vapor. The heat capacity of water vapour, $C_p$, at 100 °C is 8.65 cal mole$^{-1}$ deg$^{-1}$, very nearly the $4R$ expected for a gas of rigid molecules with three translational and three rotational degrees of freedom; a linear molecule, with only two rotational degrees of freedom carrying appreciable moments of inertia, would fall measurably short of this value. Equipartition assigns each translational and rotational degree of freedom a mean energy $\tfrac{1}{2}k_BT$ and a contribution $\tfrac{1}{2}R$ to the molar heat capacity, with a further $R$ added at constant pressure, so a rigid nonlinear molecule should show $C_p=\left(\tfrac{3}{2}+\tfrac{3}{2}+1\right)R=4R\approx 7.95$ cal mol$^{-1}$ deg$^{-1}$ and a linear one only $\tfrac{7}{2}R\approx 6.95$; the measured 8.65 sits squarely on the nonlinear value, the small excess coming from incipient vibrational excitation and the non-ideality of the vapour. Spectroscopy later fixed the geometry precisely. In its equilibrium configuration the oxygen-hydrogen bond length is 0.958 angstroms and the H-O-H angle is 104 degrees and 27 minutes, close to 104.5 degrees. In the lowest vibrational state, which is the relevant one at glacier temperatures, the values shift slightly, to an angle near 105 degrees. The angle is notably smaller than the 109.5 degrees of a perfect tetrahedron, a point we return to below.

A molecule also has a size, though the concept needs care because the electron cloud has no sharp edge. The working measure is the distance at which two molecules begin to repel strongly, obtained from the transport properties of the vapor and from the spacing of molecules in the condensed phases, and for water it comes out close to 2.8 angstroms between oxygen centers. Two numbers are worth holding side by side. The covalent O-H bond inside the molecule is about 1 angstrom, while the effective diameter of the whole molecule is nearly three times that, so the molecule is, to a fair approximation, a sphere of electron density about 2.8 angstroms across with two small protrusions where the protons sit. The oxygen-oxygen distance of 2.76 angstroms in ice, derived in the next chapter, is essentially two of these spheres in light contact; the hydrogen bond does not pull the molecules into one another so much as it orients spheres that were already nearly touching.

```{figure} ../math/figures/water-molecule-geometry.png
:name: fig-water-molecule-geometry
:width: 55%

The bent molecule, with bond length, bond angle, and the partial charges left by the uneven tug-of-war over the shared electrons. The values shown come from an electronic-structure model and differ slightly from the measured gas-phase geometry quoted in the text; the angle is soft, and the section on vibrations explains why. Figure from M. Chaplin's *Water Structure and Science*.
```

## Electronic structure

The geometry just described is decided by the orbitals introduced in {doc}`energy-levels`, the spherical $s$ orbitals and the three perpendicular two-lobed $p$ orbitals, each holding at most two electrons of opposite spin. Everything in this section is bookkeeping with those shapes.

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

For calculating the energetics of many molecules at once, the full charge distribution is replaced by an effective model, a small set of point charges positioned and sized to reproduce the measured dipole moment and, in the better models, the quadrupole as well. The classic version places four fractional charges, two positive at the protons and two negative along the lone-pair directions, on a tetrahedral frame, charges of a few tenths of an electron charge at distances of about an angstrom from the oxygen. Models of this kind are crude maps of the molecule but useful machines, since the electrostatic energy of an arrangement of many water molecules, the quantity that decides defect energies and proton configurations in the crystal, can be computed by summing the interactions among the point charges. The same idea, refined and recalibrated, sits inside essentially every molecular simulation of water and ice in use today.

The molecule can also lose its integrity altogether. Removing an electron outright costs about 12.6 electron volts, far beyond thermal reach, but a cheaper rearrangement is available in the condensed phases, the transfer of a proton from one molecule to a neighbor to form an ion pair, H$_3$O$^+$ and OH$^-$. The transfer is rare, since it still costs of order an electron volt against the Boltzmann factor's budget of a fortieth of that, and in ice the equilibrium ion concentration is far smaller even than in liquid water. Rare is not the same as unimportant. These ions, mobile along the hydrogen-bond network, are one of the two native defect families of the crystal, and {doc}`point-defects` shows that they carry part of the electrical life of ice.

The dipole moment of a water molecule is not fixed. Placed in the electric field of its neighbors, the molecule's electron cloud distorts and its dipole grows. The polarizability that governs this response is about $1.5\times10^{-24}$ cubic centimeters, a fairly low value consistent with the molecule's moderately high ionization energy. In the condensed phases, where every molecule sits in the field of several hydrogen-bonded neighbors, this induced enhancement raises the effective dipole well above the vapor value, which in turn strengthens the hydrogen bonds. The bonding in ice is therefore cooperative, and the molecule in the crystal is not quite the same as the molecule in isolation.

## Molecular vibrations

With three nuclei the molecule has three internal vibrational degrees of freedom, and these correspond to three normal modes. The first, $\nu_1$, is a symmetric stretch in which both O-H bonds lengthen and shorten together. The second, $\nu_2$, is a bending of the H-O-H angle. The third, $\nu_3$, is an asymmetric stretch in which one bond lengthens as the other shortens. Their frequencies, expressed as wavenumbers, are about 3652, 1595, and 3756 inverse centimeters respectively, so the two stretching modes lie near a wavelength of three micrometers and the bending mode near six micrometers. Each mode is a quantized oscillator with the level structure $E_v = (v+\tfrac{1}{2})h\nu$ developed in {doc}`energy-levels`, and at terrestrial temperatures each sits in its ground state, since the smallest of the quanta corresponds to a characteristic temperature $h\nu/k_B$ near 2,300 K and the stretches to above 5,200 K.

The stiffness of these motions is described by force constants, and they reveal something useful. The constant resisting bond stretching is about $8.5\times10^{5}$ dynes per centimeter, while the constant resisting bending of the angle is only about $0.8\times10^{5}$, roughly an order of magnitude smaller. Treating each O–H bond as an independent diatomic oscillator, as in {doc}`energy-levels`, reproduces the stretching constant to within about ten percent; the residual difference arises because the two bonds share the oxygen's motion and the modes are not truly independent. The H-O-H angle is, in other words, soft. This is why the bond angle is hard to predict from first principles, since a small error in the energy translates into a large change in the computed angle, and it is also why the angle adjusts when the molecule is placed in the differing environments of vapor, liquid, and ice.

A quantum oscillator cannot be still, and the vibrations therefore endow the molecule with a zero-point energy of $\tfrac{1}{2}h\nu$ per mode even at absolute zero. Summing over the three modes gives roughly 55 kJ/mol, nearly three hydrogen bonds' worth of energy retained even at absolute zero. The zero-point energy matters here for one reason above all. Its magnitude depends on the vibrational frequencies, and the frequencies depend on the nuclear masses, so molecules built from heavier isotopes vibrate more slowly and sit deeper in the same potential well. That mass dependence is the entire physical basis of the isotopic thermometry developed in the climate chapters, and it deserves a section of its own.

## Isotopic varieties

Oxygen occurs as $^{16}$O, $^{17}$O, and $^{18}$O, and hydrogen as ordinary H and as deuterium, D, so ordinary water contains, alongside the dominant H$_2^{16}$O, about one molecule of H$_2^{18}$O per 500 and about one of HDO per 3,200, with rarer species below these. The isotopic varieties are chemically identical, since chemistry is set by the electrons and the nuclear charge, and their geometry is the same to high accuracy. What differs is the mass, and through the mass, the vibrations.

A heavier isotope lowers the vibrational frequencies, in the simplest picture by the factor $\sqrt{m_H/m_D} \approx 1/\sqrt{2}$ for the proton-dominated modes, and a lower frequency means a smaller zero-point energy. A molecule of HDO or H$_2^{18}$O therefore sits deeper in its potential well than ordinary water, and it costs correspondingly more energy to remove it from the liquid or the crystal into the vapor. The consequence is that the heavy varieties are slightly less volatile, so every evaporation enriches the vapor in light water and every condensation enriches the condensate in heavy water. The fractionation at each step is a fraction of a percent, but the atmosphere performs the step thousands of times between a subtropical ocean and a polar snowfall, and the cumulative depletion of heavy isotopes in polar precipitation, tens of per mil, is the signal that {doc}`../climate/paleoclimate` reads as a thermometer. The thermometer's molecular mechanism is nothing more than the mass dependence of zero-point energy.

The pure heavy waters also exist as bulk materials, and their properties calibrate the size of these quantum effects. Heavy water, D$_2$O, melts at 3.82 °C rather than 0 °C, is about 11 percent denser, and forms an ice with the same crystal structure but measurably different lattice dynamics, which is why deuterated ice appears throughout the spectroscopy of {doc}`lattice-dynamics` as a diagnostic, since shifting a band by $\sqrt{2}$ under deuteration identifies the motion as proton-dominated. A nearly four-degree shift of the melting point from a change of nothing but nuclear mass is a standing reminder that ice is, by molecular standards, a strongly quantum solid.

```{admonition} Exercise — the isotope shift
:class: tip
In the gas-phase HDO molecule the O–H stretching frequency is 3707 cm⁻¹ and the O–D stretching frequency is 2727 cm⁻¹.

**(a)** Using $\nu \propto \mu^{-1/2}$ with the appropriate reduced masses ($m_\mathrm{H} = 1.008$ u, $m_\mathrm{D} = 2.014$ u, $m_\mathrm{O} = 15.999$ u), predict the ratio of the two frequencies and compare with the measured value.

**(b)** Compute the difference in zero-point energy between the O–H and O–D stretches, in cm⁻¹ and in kJ mol⁻¹ (1 cm⁻¹ = 11.96 J mol⁻¹).

**(c)** Explain in one or two sentences how a difference of this kind becomes a paleothermometer.
```

```{admonition} Solution
:class: dropdown
**(a)** $\mu_{\mathrm{OH}} = (1.008)(15.999)/17.007 = 0.948$ u and $\mu_{\mathrm{OD}} = (2.014)(15.999)/18.013 = 1.789$ u, so the predicted ratio is $\sqrt{1.789/0.948} = 1.374$. The measured ratio is $3707/2727 = 1.359$, within about one percent; the small discrepancy reflects anharmonicity of the real bond, which the parabolic approximation neglects.

**(b)** $\Delta E_0 = \tfrac{1}{2}(3707 - 2727) = 490$ cm⁻¹ $\approx 5.9$ kJ mol⁻¹, between two and three times $RT$ at the melting point.

**(c)** Because the heavy isotopologue sits lower in its potential well, its effective binding in the condensed phase differs slightly from that of the light molecule, and the difference shifts again when the molecule passes between vapor and condensed phases. The resulting vapor-pressure difference, a fraction of a percent per condensation step, is compounded by repeated distillation as moisture moves poleward, and the isotopic depletion of polar snow becomes a record of condensation temperature ({doc}`../climate/paleoclimate`).
```

## Spectral properties

The energy levels of the molecule produce absorptions across the spectrum, and each region reports on a different aspect of its structure. The largest energy changes are electronic; the lowest electronic excitation lies near 7 eV, in the far ultraviolet, so that pure water and clear ice transmit visible light almost without loss, and the faint blue of thick ice, treated in {doc}`optical-properties`, arises from overtones of the vibrations rather than from electronic absorption. The vibrational modes absorb in the infrared, the bending mode near six micrometers and the two stretches near three, and because each mode changes the dipole moment it produces a strong absorption band. Because the molecule has a permanent dipole it also has a pure rotational spectrum in the far infrared and microwave, where it absorbs by changing its rotational state alone; the rotational constants about the three principal axes are 27.9, 14.5, and 9.3 cm⁻¹, giving quanta of order $10^{-3}$ eV, the finest rungs of the level ladder of {doc}`energy-levels`. Taken together these absorptions make water vapor one of the strongest infrared absorbers in the atmosphere, alongside carbon dioxide and ozone, which is the molecular root of its role in the planet's radiation balance. In the solid the same vibrational and dielectric responses persist, shifted by the hydrogen bonding, so the spectra of ice carry a record of the bonding environment.

## Forces between molecules

Water molecules attract one another in several ways. Setting aside the hydrogen bond for a moment, there are the ordinary van der Waals interactions common to all molecules. Permanent dipoles attract on average even as the molecules rotate, an interaction that falls off as the inverse sixth power of separation and weakens with temperature. A permanent dipole also polarizes its neighbor and is attracted to the dipole it induces, the induction force. And even molecules with no permanent dipole attract through dispersion forces, which arise because the instantaneous dipole of a molecule fluctuates even when its average is zero, and these fluctuations correlate between neighbors. All three of these fall off as the inverse sixth power of distance.

What dominates the behavior of water in the condensed phases is a stronger and more specific interaction between neighbors, the hydrogen bond.

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

## Implications for glaciology

The polar molecule and its lone pairs make the hydrogen bond, which builds the open tetrahedral crystal, which is why ice is less dense than water and floats. The single symmetry axis of that crystal, inherited from the bonding geometry, gives the strong directional anisotropy that underlies Glen's flow law in {doc}`../ice_flow/ice-rheology` and the crystal fabric of {doc}`../ice_flow/ice-fabric`. The polarizability and the dielectric response of the molecule set the permittivity of ice, and its anisotropy along and across the symmetry axis is what lets radar sense fabric through birefringence, as developed in {doc}`../radar/radiowave-fabric`. Even the strength of the hydrogen bond reappears later as the energy scale that sets the melting point and the activation energy for creep.
