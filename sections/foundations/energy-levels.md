# Energy levels in atoms and molecules

The bond energies and shell capacities quoted in the previous chapter are the result of quantum-mechanical theory. This chapter develops several quantum-mechanical results: the origin of discrete energy levels, the hydrogen atom and the shell structure that follows from it, the harmonic oscillator and rigid rotor that describe molecular vibration and rotation, and the comparison of level spacing with $k_B T$. The standard results are quoted without formal solution of the wave equation, but each is derived or verified and applied directly to the water molecule.

## Standing waves and discrete energies

Matter on the atomic scale has wave properties, with a wavelength related to momentum by the de Broglie relation $\lambda = h/p$, where $h$ is Planck's constant. Because $h$ is small, the wavelength of any macroscopic object is negligible compared with atomic dimensions, and classical mechanics is an excellent approximation even at the bulk crystal scale. For an electron with a kinetic energy of a few electron volts, however, the wavelength is about 6 Å, comparable with the size of a molecule, and the wave character of the electron cannot be neglected. An electron in a molecule must be treated as a wave occupying the whole of the available volume.

A confined wave can assume only certain forms, and the simplest confinement can be worked out completely. Consider a particle of mass $m$ restricted to a line segment of length $L$, the one-dimensional "particle in a box." Like a string fixed at both ends, the particle's wave must vanish at the walls, so it must consist of a whole number of half-wavelengths,

$$
\lambda_n = \frac{2L}{n}, \qquad n = 1, 2, 3, \ldots
$$

Each allowed wavelength implies a momentum $p_n = h/\lambda_n = nh/2L$ through the de Broglie relation, and hence a kinetic energy

$$
E_n = \frac{p_n^2}{2m} = \frac{n^2 h^2}{8 m L^2}.
$$

Two features of this result hold for confined quantum systems generally. The energy can take only discrete values, with the spacing between levels set by $h^2/8mL^2$, so that discreteness is a property of any confined wave. And the lowest state is not at rest; the $n=1$ level retains the energy $h^2/8mL^2$, the zero-point energy met in the {doc}`preface`, because a wave of infinite wavelength cannot fit between the walls. The state with quantum number $n$ has $n-1$ interior nodes, points where the wave vanishes, and the energy rises with the number of nodes, a pattern that recurs in the orbitals below.

The magnitudes are the point. For an electron confined to $L = 3$ Å, the size of a water molecule, the ground-state energy is about 4 eV, which is the scale of chemical bond energies; the electron-volt scale of chemistry follows directly from the values of $h$, the electron mass, and molecular dimensions. The $1/mL^2$ dependence shows that level spacings shrink as the confining region grows and as the particle mass increases. A proton confined to the same region has levels closer together by a factor of 1836, and a macroscopic body has levels spaced so finely that its energy is continuous for all practical purposes. This single scaling rule locates the boundary between quantum and classical behavior throughout the book.

## The hydrogen atom

An electron bound to a proton is confined by the Coulomb attraction $-e^2/4\pi\epsilon_0 r$. Confining the electron within a radius $L$ costs a kinetic energy of order $h^2/8mL^2$, which grows as the atom shrinks, while the Coulomb attraction supplies an energy of order $-e^2/4\pi\epsilon_0 L$, which increases as the atom shrinks but only as $1/L$. The total has a minimum at a finite radius, and evaluating the sum of the competing processes gives a size of order an angstrom and a binding energy of order an electron volt. The atom does not collapse because compressing the electron wave raises its kinetic energy faster than the Coulomb term can pay for it.

This gives rise to the energy levels for a hydrogen atom:

$$
E_n = -\frac{m e^4}{8\,\epsilon_0^2 h^2}\,\frac{1}{n^2} = -\frac{13.6\ \mathrm{eV}}{n^2},
\qquad n = 1, 2, 3, \ldots
$$

and a ground-state radius, the Bohr radius, $a_0 = \epsilon_0 h^2/\pi m e^2 = 0.529$ Å. The ionization energy of hydrogen is 13.6 eV; the ionization energy of the water molecule, 12.6 eV ({doc}`water-molecule`), is of the same order because the same physics binds its outer electrons. Atomic sizes of an angstrom, bond energies of electron volts, and the $10^{15}$ Hz frequencies of ultraviolet spectra are all expressions of the constants in the Bohr formula.

The hydrogen-atom levels also carry a degeneracy that becomes the periodic table. The level $E_n$ comprises $n^2$ distinct standing-wave patterns, one pattern for $n=1$, four for $n=2$, and so on. With two electrons permitted per pattern, as the next section explains, the first shell holds two electrons and the second holds eight, which are the capacities that fixed the formula H₂O in {doc}`composition`.

## Orbitals and the exclusion principle

The standing-wave patterns of an electron in the field of a nucleus are called orbitals. An orbital is a stationary distribution of electron density with a definite energy. The lowest orbitals, designated $s$, are spherically symmetric; the next, designated $p$, have two lobes and occur in sets of three directed along perpendicular axes; orbitals of higher type are not needed for the atoms of ice. Electrons also possess an intrinsic angular momentum, or spin, with two possible orientations, and the Pauli exclusion principle states that no two electrons may occupy the same quantum state, so that each orbital accommodates at most two electrons of opposite spin. The first shell, comprising the single $1s$ orbital, therefore holds two electrons, and the second, comprising $2s$ and the three $2p$ orbitals, holds eight.

Covalent bonding has the same wave-mechanical origin. When two atoms approach, an electron wave can extend over both nuclei at once, and since the energy of a confined wave decreases as the confining region grows, this delocalization lowers the electron's energy. The energy released is the bond energy, about 460 kJ mol⁻¹ for the O–H bond, and the shared electron pair of the previous chapter is two electrons of opposite spin occupying one such molecule-spanning orbital. The particular orbitals formed in water, the hybridization of the oxygen orbitals, and the disposition of the lone pairs are treated in the next chapter, where they determine the geometry of the molecule.

## Electronic, vibrational, and rotational energies

A molecule possesses internal energy levels of three kinds, with characteristic magnitudes separated by roughly two orders of magnitude at each step {cite}`herzberg1945`. Electronic excitations, rearrangements of the electron distribution itself, cost several electron volts, as the hydrogen-atom scale would suggest, and lie in the ultraviolet. This section develops the general results for the other two kinds, vibration and rotation; their application to the measured spectrum of the water molecule is made in {doc}`water-molecule`.

Vibrational levels are described by the harmonic oscillator, the second exactly solvable problem the book needs. Near the bottom of any potential well the potential is approximately parabolic, $V \approx \tfrac{1}{2}k x^2$ with $k$ the curvature or force constant, and a mass $\mu$ oscillating in such a well has the energy levels

$$
E_v = \left(v + \tfrac{1}{2}\right) h\nu, \qquad
\nu = \frac{1}{2\pi}\sqrt{\frac{k}{\mu}}, \qquad v = 0, 1, 2, \ldots
$$

The levels are uniformly spaced by $h\nu$, and the ground state retains the zero-point energy $\tfrac{1}{2}h\nu$. For the vibration of two bonded atoms, $\mu$ is the reduced mass $m_1 m_2/(m_1+m_2)$, which for O–H is 0.948 u, close to the proton mass because the oxygen barely moves. The measured O–H stretching frequency, about 3660 cm⁻¹, then implies a force constant $k = \mu\,(2\pi c\tilde\nu)^2 \approx 750$ N m⁻¹, an estimate of the stiffness of the covalent bond. Two consequences of the formula run through the book. The frequency, and with it the zero-point energy, falls as the square root of the mass increases, which is the origin of the isotope effects developed in {doc}`water-molecule`; and vibrational quanta of this size correspond to characteristic temperatures $h\nu/k_B$ of thousands of kelvin, which is why molecular vibrations are frozen out at terrestrial temperatures.

Rotational levels complete the ladder. A molecule with moment of inertia $I$ rotating freely has the energy levels

$$
E_J = B\,J(J+1), \qquad B = \frac{\hbar^2}{2I}, \qquad J = 0, 1, 2, \ldots
$$

Because molecules are small, their moments of inertia are small and their rotational quanta, of order $10^{-3}$ eV for a light molecule like water, are the finest of the three families, lying in the far infrared and microwave. Thermal energy at the melting point, 190 cm⁻¹ in spectroscopic units, spans many of these levels, so a vapor molecule tumbles freely among its rotational states. In the crystal, free rotation is suppressed by the four hydrogen bonds and is replaced by hindered rocking motions, the librations taken up in {doc}`lattice-dynamics`; the measured rotational constants of the water molecule are given with its spectrum in {doc}`water-molecule`.

Radiation couples to all of these levels through the photon energy $h\nu$, and absorption requires a transition of matching energy, which is why every substance has a characteristic absorption spectrum. At radio frequencies the photon energy lies several orders of magnitude below even the rotational quanta, so cold ice presents no transition to absorb radar energy and is transparent to depths of kilometers, the property on which the radar methods of the observing chapters depend. The weak absorption that remains is due not to quantum transitions but to the slow reorientation of molecular dipoles by way of the lattice defects of {doc}`point-defects`, and its dependence on temperature and impurity content is what radar attenuation measures.

## Classical and quantum degrees of freedom

Whether a degree of freedom behaves classically is determined by the ratio of its level spacing to $k_B T$, which at the melting point is about 1/40 eV. When the spacing is small compared with $k_B T$, the levels are effectively continuous, the motion is classical, and equipartition applies; the rotations of the free molecule, with quanta of order $10^{-3}$ eV, are in this regime, and could accordingly be counted classically in the $4R$ heat capacity of the {doc}`preface`. When the spacing is large compared with $k_B T$, excitation is suppressed by the Boltzmann factor and the degree of freedom contributes nothing to the heat capacity; the molecular vibrations, with quanta of five to twenty times $k_B T$, are in this regime, which is why they are absent from the $4R$ count. Electronic excitation is suppressed more strongly still, so that the molecules of a glacier are all in their electronic ground states. This last point has a useful consequence, since it means the interaction between molecules can be described by a single potential-energy function, the one mapped in the next two chapters. The same comparison of $h\nu$ with $k_B T$, applied mode by mode to the vibrations of the crystal, yields the heat capacity of ice in {doc}`lattice-dynamics`.

A quantum particle also has a finite probability of penetrating a potential barrier higher than its own energy. Inside the barrier the wave does not oscillate but decays, with a decay constant

$$
\kappa = \frac{\sqrt{2m(V - E)}}{\hbar},
$$

so that the transmission probability through a barrier of width $a$ falls off as $e^{-2\kappa a}$, exponentially in the width and in the square root of the particle mass. This is tunneling, and the mass dependence makes it most important for light particles; electrons tunnel readily, protons measurably, deuterons less so. For a proton facing a barrier a few tenths of an electron volt high and a few tenths of an angstrom wide, dimensions typical of proton exchange along a hydrogen bond, the exponent $2\kappa a$ is of order ten, so tunneling is rare for any single attempt but not negligible against the $10^{13}$ attempts per second that lattice vibrations supply. Proton tunneling has accordingly been invoked in the motion of protons along and between hydrogen bonds in ice, and the question recurs with the defect processes of {doc}`point-defects`.

```{admonition} Exercise — confinement energies
:class: tip
The lowest energy of a particle of mass $m$ confined to a region of size $L$ is approximately $E_1 = h^2/8mL^2$.

**(a)** Evaluate $E_1$ for an electron confined to $L = 0.30$ nm, the size of a water molecule, and compare it with the O–H bond energy of about 4.8 eV.

**(b)** Evaluate $E_1$ for a proton in the same region and compare it with $k_B T$ at the melting point, about $1/40$ eV. What does the comparison imply about how classically the molecule's nuclei behave?

**(c)** The measured quantum of the O–H stretching vibration is about 0.45 eV. What confinement size $L$ would give a proton this energy, and what does the answer indicate about how tightly the covalent bond constrains its proton?
```

```{admonition} Solution
:class: dropdown
**(a)** $E_1 = h^2/8m_eL^2 = (6.63\times10^{-34})^2 / (8 \times 9.11\times10^{-31} \times (3.0\times10^{-10})^2) \approx 6.7\times10^{-19}$ J $\approx 4.2$ eV, in agreement with the scale of chemical bond energies. Bond energies are confinement energies.

**(b)** The proton is $1836$ times heavier, so $E_1 \approx 4.2\ \mathrm{eV}/1836 \approx 2.3$ meV, about a tenth of $k_B T$. Confinement at the scale of the molecule costs a proton less than thermal energy, so the nuclei move nearly classically on the potential-energy surface that the electrons establish; quantum mechanics is essential for the electrons and marginal for the nuclei.

**(c)** Solving $E_1 = 0.45$ eV for $L$ with the proton mass gives $L \approx 0.02$ nm. The covalent bond confines its proton to a region roughly a tenth the size of the molecule, which is why the vibrational quanta are large enough to freeze out despite the proton's mass.
```

In sum, energies come in discrete levels because confined waves admit only discrete patterns; the hydrogen atom sets the angstrom and electron-volt scales of atomic physics and supplies, through its degeneracies and the exclusion principle, the shell capacities of chemistry; the harmonic oscillator and rigid rotor describe molecular vibration and rotation and give quantitative meaning to the zero-point energy and the isotope shift; and the comparison of level spacing with $k_B T$ separates the classical degrees of freedom from the frozen ones. The next chapter applies these results to the water molecule itself.
