# Lattice vibrations and thermal properties

The previous chapter treated the ice crystal as a fixed arrangement of oxygen atoms with protons distributed over the bonds between them. That static picture is enough to explain why ice is less dense than water and why it has a single soft direction, but it does not describe how ice flows. At any temperature above absolute zero, molecules in the crystal lattice are never still. They oscillate about their lattice sites, the lighter protons swinging through larger excursions than the heavier oxygens, and the collective patterns of this motion are the lattice vibrations of the crystal. These lattice vibrations carry the thermal energy that sets the heat capacity, they transport heat down a temperature gradient and so fix the thermal conductivity, and through the point defects in the mattrix they govern the rate at which ice deforms. This chapter develops the vibrational spectrum and the thermal properties that follow from it. It is also the right place to make temperature itself precise, along with the freezing point, because both ideas are statements about the statistics of molecular vibrations. The chapter therefore opens with the mathematics of these statistics, the behavior of very large numbers.

## Probability and very large numbers

Statistical mechanics rests on a mathematical property of large numbers. The quantities of interest in a glacier are averages over water molecules, and any macroscopic piece of ice contains of order >$10^{23}$ H$_2$O. The claim to be demonstrated is that for numbers of this size the fluctuations about an average are negligible, so that statistical averages may be treated as exact.

One gram of ice contains $N \approx 6.7\times10^{22}$ hydrogen bonds, two per molecule. How many of them are broken at any moment? The number of distinct ways of choosing $m$ broken bonds from among $N$ is $N!/m!(N-m)!$, and each such configuration occurs with probability $p^m(1-p)^{N-m}$, so the probability of finding exactly $m$ broken bonds is

$$
p(m) = \frac{N!}{m!\,(N-m)!}\;p^m\,(1-p)^{N-m},
$$

```{admonition} Derivation
:class: dropdown
Treat the $N$ bonds as independent, each broken with probability $p$ and intact with probability $1-p$. One particular configuration with a specified set of $m$ broken bonds and $N-m$ intact ones occurs, by independence, with probability $p^m(1-p)^{N-m}$. The bonds are indistinguishable as to which are broken, so every assignment that breaks some $m$ of them yields the same probability, and the number of such assignments is the number of ways to choose $m$ bonds out of $N$,

$$
\binom{N}{m} = \frac{N!}{m!\,(N-m)!}.
$$

The probability of finding exactly $m$ broken bonds, regardless of which, is the product of the count and the per-configuration probability, which is the printed expression.
```

the binomial distribution. Its mean and width follow from the independence of the bonds. A single bond contributes 1 with probability $p$ and 0 otherwise, so its mean is $p$ and its variance is $\langle x^2\rangle - \langle x\rangle^2 = p - p^2 = p(1-p)$; for independent contributions both means and variances add, giving

$$
\langle m \rangle = Np, \qquad \sigma^2 = Np(1-p), \qquad
\frac{\sigma}{\langle m \rangle} = \sqrt{\frac{1-p}{Np}} \approx \frac{1}{\sqrt{Np}}.
$$

```{admonition} Derivation
:class: dropdown
Write $m = \sum_{i=1}^{N} x_i$, where $x_i$ is 1 if bond $i$ is broken and 0 otherwise. A single such indicator has mean $\langle x_i\rangle = p\cdot 1 + (1-p)\cdot 0 = p$ and, since $x_i^2 = x_i$, variance $\langle x_i^2\rangle - \langle x_i\rangle^2 = p - p^2 = p(1-p)$. Means add for any sum of random variables, so

$$
\langle m\rangle = \sum_{i=1}^N \langle x_i\rangle = Np.
$$

Variances add for *independent* variables, which the bonds are taken to be, so

$$
\sigma^2 = \sum_{i=1}^N p(1-p) = Np(1-p).
$$

The relative fluctuation is then

$$
\frac{\sigma}{\langle m\rangle} = \frac{\sqrt{Np(1-p)}}{Np} = \sqrt{\frac{1-p}{Np}},
$$

which for small $p$ reduces to $1/\sqrt{Np}$.
```

The mean grows in proportion to $N$ while the width grows only as $\sqrt{N}$, so the *relative* fluctuation falls as the population grows. For the gram of ice, $\langle m \rangle \approx 6.7\times10^{18}$ bonds are broken at any instant, with a standard deviation of $\sigma \approx 2.6\times10^{9}$, and the broken-bond count is therefore fixed to about four parts in $10^{10}$. Every property that depends on this population, the creep rate, the dielectric relaxation, the diffusion of molecules through the lattice, is correspondingly sharp. No measurement resolves fluctuations of one part in a billion, which is why ice, an object governed entirely by molecular statistics, behaves in the laboratory and in the field as a material with definite properties.

The same arithmetic disposes of the extreme cases. The probability that a gram of ice momentarily contains no broken bonds at all is $(1-p)^N = e^{N\ln(1-p)} \approx e^{-Np} = e^{-6.7\times10^{18}}$. For comparison, the age of the universe is of order $10^{17}$ seconds and the visible universe contains of order $10^{80}$ atoms; a probability of $e^{-10^{18}}$ is zero for every physical purpose. Perfect crystalline order does not occur in macroscopic ice, and neither does any other macroscopic fluctuation away from the average.

These conclusions are not special to the binomial distribution. The central limit theorem states that a sum $S = \sum_{i=1}^{N} x_i$ of independent quantities drawn from any distribution with mean $\mu_x$ and standard deviation $\sigma_x$ approaches, for large $N$, the Gaussian distribution

$$
p(S) = \frac{1}{\sigma\sqrt{2\pi}}\,e^{-(S-\mu)^2/2\sigma^2},
\qquad \mu = N\mu_x, \quad \sigma = \sqrt{N}\,\sigma_x,
$$

so that the relative width falls as $1/\sqrt{N}$ whatever the underlying distribution. The energy of a block of ice, the polarization of a dielectric, and the strain accumulated from many molecular rearrangements are all sums of this kind, and all are sharp in the same degree. This is the license for everything in the rest of the chapter. When the next section identifies the most probable division of energy between two systems, that division is not merely the most probable but, for macroscopic systems, the only one ever observed.

## The statistical definition of temperature

Much of glacier physics is the statistics of jostling molecules, and the machinery for that statistics deserves more than a formula pulled from the air. The starting point, due to Boltzmann, is a counting argument {cite}`boltzmann1877`. A macroscopic state, a block of ice with a given energy, corresponds to an astronomical number $W$ of microstates, distinct molecular arrangements consistent with what we can measure. The entropy is the logarithm of that count,

$$
S = k_B \ln W,
$$

with $k_B$ Boltzmann's constant, and an isolated system evolves toward the macrostate with the most microstates simply because that is overwhelmingly where the dice land. The residual entropy of the proton-disordered crystal in {doc}`ice-structure` was this formula at work, with $W$ counted by Pauling.

Energy in a vibrating lattice comes in discrete quanta, so picture two tiny blocks of ice, each just three of the oscillators of this chapter, sharing six quanta between them. The number of ways to arrange $q$ indistinguishable quanta among $N$ oscillators is a standard counting result, $W = \binom{q+N-1}{q}$, and multiplying the counts for the two blocks gives the number of microstates for each way of splitting the energy.

| $q_A$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| $W_A \cdot W_B$ | 28 | 63 | 90 | **100** | 90 | 63 | 28 |

Every one of the 462 microstates is equally likely; nothing prefers the even split. Yet the even split owns more microstates than any other, and if the blocks were real, with $10^{23}$ oscillators rather than three, the peak of this table would sharpen into a needle of relative width $\sim 1/\sqrt{N}$, the scaling established in the preceding section. Energy spreads out, and ice in a warm room ends up at the room's temperature, not because any force pushes it there but because the alternatives are statistically invisible.

The table also says *when* the spreading stops. The most probable split is the one where moving a quantum from block A to block B no longer increases the product $W_A W_B$, that is, where it no longer increases $\ln W_A + \ln W_B$. In the language of entropy, energy flows until

$$
\frac{\partial S_A}{\partial E_A} = \frac{\partial S_B}{\partial E_B},
$$

and this shared quantity is what temperature is. Define $1/T = \partial S/\partial E$, the rate at which a system's entropy buys energy, and the equation above becomes the familiar statement that two bodies in contact come to the same temperature. The definition explains the direction of heat flow rather than assuming it. A cold body is one whose entropy grows steeply with energy, so moving a joule from hot to cold creates more entropy in the receiver than it destroys in the donor, and the joule moves. Temperature is the exchange rate in that trade, and a thermometer lowered down a borehole is reading it; the temperature profiles of {doc}`../thermomechanics/thermal-structure` are maps of $\partial S/\partial E$ through an ice column.

Let a single molecule, or any small system, exchange energy with a large reservoir, and ask for the probability of finding it in one particular microstate of energy $E$. That probability is proportional to the number of arrangements left to the reservoir, $W_R(E_{tot}-E) = e^{S_R(E_{tot}-E)/k_B}$, and because the system is small the reservoir's entropy can be expanded to first order, $S_R(E_{tot}-E) \approx S_R(E_{tot}) - E\,\partial S_R/\partial E = S_R(E_{tot}) - E/T$. The constant first term drops into the normalization, leaving the Boltzmann factor,

$$
p \propto e^{-E/k_B T}.
$$

```{admonition} Derivation
:class: dropdown
This collects the steps sketched in the surrounding text. A small system in a definite microstate of energy $E$ leaves the reservoir with energy $E_{tot}-E$, and by the equal-a-priori-probability postulate the joint probability is proportional to the number of reservoir microstates, $W_R(E_{tot}-E)$. Writing that count through the entropy, $W_R = e^{S_R/k_B}$,

$$
p \propto W_R(E_{tot}-E) = \exp\!\left[\frac{S_R(E_{tot}-E)}{k_B}\right].
$$

Because the system is small, $E \ll E_{tot}$, expand $S_R$ to first order in $E$,

$$
S_R(E_{tot}-E) \approx S_R(E_{tot}) - E\left.\frac{\partial S_R}{\partial E}\right|_{E_{tot}}
= S_R(E_{tot}) - \frac{E}{T},
$$

using the definition $1/T = \partial S/\partial E$. The leading term $S_R(E_{tot})$ is a constant independent of the system's state and is absorbed into the normalization, leaving

$$
p \propto \exp\!\left(-\frac{E}{k_B T}\right).
$$
```

Nothing here is specific to the system; the exponential is purely the price the reservoir's count pays to lend out energy $E$. The normalization, the sum of Boltzmann factors over all microstates, is the partition function $Z = \sum_i e^{-E_i/k_B T}$, from which every equilibrium property follows by differentiation {cite}`gibbs1902`. The free energy $F = -k_B T \ln Z$ packages the competition that decides phase equilibrium, since minimizing $F$ means trading energy against entropy, and that trade is exactly what the freezing point at the end of this chapter expresses.

At 0 °C the thermal energy $RT$ is about 2.3 kJ/mol, while a hydrogen bond costs roughly 20 kJ/mol to break, so the Boltzmann factor for borrowing a bond's worth of energy is $e^{-20/2.3} \approx 10^{-4}$. That looks prohibitive until you recall that molecules attempt the move at vibrational frequencies near $10^{13}$ Hz, so any given bond still breaks millions of times per second. Ice near the melting point is solid because the great majority of bonds are intact at any instant, and the rare fluctuations that break them are what let it creep, diffuse, and trade molecules with the vapor. The Arrhenius law that turns this exponential into the rate of every slow process in ice is developed with the point defects of {doc}`point-defects`, and it is why the rate factor in Glen's flow law of {doc}`../ice_flow/ice-rheology` makes ice at the melting point deform orders of magnitude faster than the cold ice of the polar plateaus.

## Three families of vibration

Because the water molecule is a rigid, strongly bonded unit held in a much weaker network of hydrogen bonds, its vibrations separate cleanly into three groups that differ by more than an order of magnitude in frequency. The separation is the vibrational expression of the same hierarchy of forces met in the chapter on the molecule: stiff covalent bonds inside each molecule, soft hydrogen bonds between them.

The highest frequencies belong to the intramolecular modes, the internal stretching and bending of the covalent O-H bonds. These are the same three fundamentals that an isolated water molecule has, shifted only slightly by the presence of the neighbors. In ordinary ice the symmetric and antisymmetric stretches merge into a broad band near $3200\ \mathrm{cm^{-1}}$, and the bending mode sits near $1650\ \mathrm{cm^{-1}}$. Substituting deuterium for hydrogen moves the stretching band down to about $2400\ \mathrm{cm^{-1}}$, close to the factor of $2^{1/2}$ expected when the oscillating mass doubles, which confirms that these are motions of the protons against the oxygen. Expressed as a characteristic temperature, $h\nu/k$, the stretching modes correspond to more than $2300\ \mathrm{K}$. They are so stiff that at any glaciological temperature they are frozen in their quantum ground state and contribute essentially nothing to the heat capacity.

The intermediate band is the librations, the hindered rotations of whole molecules rocking within the cage of their four hydrogen bonds. These form a broad peak running from about $500$ to $1050\ \mathrm{cm^{-1}}$, centered near $650\ \mathrm{cm^{-1}}$ in $\mathrm{H_2O}$ ice. Their frequency reflects the strength of the hydrogen bonds that resist the rotation rather than the strength of the covalent bonds, and substituting deuterium shifts them by a factor close to $2^{1/2}$ as expected for a rotational motion. The librations have a characteristic temperature near $860\ \mathrm{K}$, so they begin to take up appreciable thermal energy only as the ice warms toward its melting point.

The lowest frequencies, and the ones that matter most for the thermal behavior of glacier ice, are the translational modes, in which whole molecules oscillate bodily against one another while the hydrogen-bond network stretches and bends. These lie below about $500\ \mathrm{cm^{-1}}$, with prominent features near $65$, $164$, and $229\ \mathrm{cm^{-1}}$. Because their characteristic temperatures range down to only a few tens of kelvin, they are thermally active across the whole range of temperatures found in ice sheets and dominate the heat capacity and the thermal conduction. The measured root-mean-square vibrational amplitudes reflect this division of labor: near the melting point the oxygen atoms swing through about $0.21\ \mathrm{angstroms}$ and the protons through about $0.25$, with the largest contribution at all temperatures coming from the translational oscillation of whole molecules rather than from libration or internal stretching.

## Phonons and the lattice spectrum

The translational modes can be understood in the same language used for any crystalline solid, as phonons, quantized traveling waves of atomic displacement labeled by a wave vector. Because the molecules move as rigid units in these modes, the relevant structure is just the lattice of oxygen sites, and the analysis runs closely parallel to that of the tetrahedrally bonded semiconductors silicon and germanium, which share the same kind of open, four-coordinated framework. With two molecules in the repeating unit, the spectrum splits into an acoustic branch, in which neighboring molecules move in phase, and an optical branch, in which they move in antiphase. Each branch divides further into one longitudinal sub-branch, with motion along the direction of travel, and two transverse sub-branches, with motion across it.

The transverse acoustic branch lies unusually low in frequency, below the longitudinal acoustic branch, because the shear modulus of ice is smaller than its bulk modulus. The crystal resists being sheared more weakly than it resists being compressed, so the waves that shear the lattice are soft. Spectroscopic and theoretical analyses place the transverse acoustic feature near $60\ \mathrm{cm^{-1}}$, the longitudinal acoustic near $164\ \mathrm{cm^{-1}}$, and the optical features near $190$ and $229\ \mathrm{cm^{-1}}$. The density of vibrational states piles up wherever these branches flatten near the edge of the Brillouin zone, which is the wave vector of the shortest wavelength the discrete lattice can carry, and those pile-ups produce the peaks observed in infrared and Raman spectra. At very low frequency the density of states grows as the square of the frequency, the ordinary behavior of an elastic continuum, and this limit fixes the leading term of the low-temperature heat capacity.

## Heat capacity

The heat capacity measures how much thermal energy the crystal absorbs for a given rise in temperature, and it is simply the sum over all the vibrational modes of the energy each can hold. At low temperature only the softest modes are excited, and the heat capacity of an insulating crystal should rise as the cube of the absolute temperature, the Debye law. Ice follows a cubic law only at the lowest temperatures and departs from it well before the melting point, because its spectrum is far from the smooth Debye form assumed in that simple theory. The large concentration of low-frequency translational modes, in particular the soft transverse acoustic modes near $60\ \mathrm{cm^{-1}}$, with a characteristic temperature of only about $86\ \mathrm{K}$, adds heat capacity faster than a Debye solid of the same stiffness would. One way to summarize the departure is to say that the equivalent Debye temperature of ice is not constant but varies with temperature, falling to a minimum near $180\ \mathrm{K}$ around $16\ \mathrm{K}$ and rising again as the librational modes switch on at higher temperatures.

For glaciological work the upshot is a specific heat capacity that is large, because water molecules are light, and that decreases steadily as the ice cools, because the higher modes progressively freeze out. Near the melting point the specific heat is about $2.1\ \mathrm{kJ\,kg^{-1}\,K^{-1}}$, and it falls by roughly a third in the coldest polar ice. This is the coefficient $c$ that appears in the heat equation of {doc}`../thermomechanics/thermal-structure`, and its temperature dependence is one reason the thermal structure of a cold ice sheet differs from that of a temperate glacier.

## Thermal expansion

When a crystal is heated it usually expands, and the expansion is a direct consequence of the anharmonicity of the bonds, the fact that it costs less energy to pull two atoms apart than to push them together by the same amount. As the vibrational amplitude grows with temperature the average spacing therefore increases. Ice expands in this ordinary way near the melting point, but at low temperature it does something unusual: below about $65\ \mathrm{K}$ its thermal expansion coefficient is negative, so that warming the crystal makes it shrink. The cause lies in the soft transverse modes. When the lattice is compressed these modes stiffen so strongly, and their frequencies rise so much, that exciting them favors a smaller volume rather than a larger one. In the language of the Grüneisen relation, which ties the expansion coefficient to the heat capacity through $\beta = 3\alpha = \gamma C_V \chi / V$, these modes carry a negative Grüneisen parameter $\gamma$ that outweighs the positive contribution of the rest of the spectrum at low temperature. This negative expansion is not a peculiarity of ice but a shared trait of open, tetrahedrally bonded structures, seen also in silicon, germanium, diamond, and fused silica. It is a clear signal that the same soft shear modes responsible for the heat capacity anomaly are at work, and that the bonding geometry, not the chemistry, is what controls the low-temperature behavior.

## Thermal conductivity

Heat flows through ice by the diffusion of phonons down the temperature gradient, the warmer regions launching more lattice waves than the colder ones. Treating the phonons as a gas gives the kinetic estimate

$$
k = \tfrac13\,C_V\,\bar v\,\Lambda,
$$

```{admonition} Derivation
:class: dropdown
This is the elementary kinetic-theory estimate, carried over from the transport of a gas to the phonon gas, with the factor of one-third arising from averaging over directions. Consider a plane normal to a temperature gradient $dT/dx$. Phonons crossing it last scattered, on average, one mean free path $\Lambda$ away, so a phonon arriving from the warmer side carries an excess energy $\sim c\,\Lambda\,(dT/dx)$ relative to one arriving from the colder side, where $c$ is the heat capacity carried by one phonon. The net energy flux is the carrier density times speed times this energy difference. Collecting the per-volume heat capacity $C_V$ and the carrier speed $\bar v$, and averaging the velocity component normal to the plane over all directions, which contributes the factor $\tfrac13$ in three dimensions, gives the flux

$$
q = -\tfrac13\,C_V\,\bar v\,\Lambda\,\frac{dT}{dx}.
$$

Comparison with Fourier's law $q = -k\,dT/dx$ identifies the conductivity as $k = \tfrac13 C_V \bar v \Lambda$. The expression is an order-of-magnitude estimate; $\Lambda$ near the melting point is inferred by inverting it against the measured $k$.
```

where $C_V$ is the heat capacity per unit volume, $\bar v$ is the mean phonon speed, close to the speed of sound in ice, and $\Lambda$ is the mean free path between scattering events. Near the melting point the mean free path inferred this way is only about $15\ \mathrm{angstroms}$, a few molecular spacings, so the phonons scatter almost as soon as they are launched. What limits the mean free path at the temperatures of glacier ice is phonon-phonon scattering through the anharmonicity of the bonds, specifically the umklapp processes in which two phonons combine to produce a third whose wave vector has been folded back into the Brillouin zone. Because the number of phonons available for umklapp scattering grows in proportion to temperature while the heat capacity is nearly constant in this range, the conductivity falls roughly as the inverse of the absolute temperature. Cold ice therefore conducts heat better than warm ice, the opposite of the trend for the heat capacity, and near the melting point the conductivity is about $2.1\ \mathrm{W\,m^{-1}\,K^{-1}}$, rising as the ice cools. The conductivity is also weakly anisotropic, larger by a few percent along the c-axis than across it, a faint mechanical echo of the crystal symmetry. This coefficient $k$ closes the conduction term in the heat equation, and its inverse temperature dependence means that the cold upper layers of an ice sheet are also its most conductive.

## The freezing point

The free energy $F = -k_BT\ln Z$ defined above earns its keep the moment two phases compete. Ice, liquid water, and vapor are phases of one substance, and which phase wins at given temperature and pressure is settled by the competition between energy and entropy that $F$ packages. The familiar 0 °C is nothing more than the temperature at which the free energies of ice and liquid water cross at atmospheric pressure; below it the crystal's lower energy wins, above it the liquid's greater entropy does, and a thermometer in an ice bath is reading the location of that crossing. Two phases coexist wherever their free energies match, and the coexistence lines in the pressure-temperature plane make up the phase diagram, with the melting line, the vapor-pressure curve, and the triple point where all three phases meet.

```{figure} ../math/figures/water-phase-diagram.png
:name: fig-water-phase-diagram
:width: 90%

The phase diagram of water across fourteen decades of pressure, with the many crystalline polymorphs of ice labelled by Roman numeral. Glaciology lives in a thin horizontal band around 1 bar, where the only players are vapor, liquid, and ordinary hexagonal ice Ih, but the wider view explains what is special about our corner, the nearly vertical melting line that tilts slightly *backward*, so that pressure favors the liquid. Figure from M. Chaplin's *Water Structure and Science*.
```

The slope of a coexistence line follows from the Clausius-Clapeyron relation,

$$
\frac{dP}{dT} = \frac{L}{T\,\Delta v},
$$

```{admonition} Derivation
:class: dropdown
Two phases coexist where their molar (or specific) Gibbs free energies are equal, $g_1(T,P) = g_2(T,P)$. Moving along the coexistence line by $dT$ and $dP$, equality must be preserved, so the changes in the two free energies match,

$$
dg_1 = dg_2.
$$

For a single component the Gibbs free energy obeys $dg = -s\,dT + v\,dP$, with $s$ the entropy and $v$ the volume per unit mass. Writing this for each phase and equating,

$$
-s_1\,dT + v_1\,dP = -s_2\,dT + v_2\,dP,
$$

and collecting terms,

$$
(v_2 - v_1)\,dP = (s_2 - s_1)\,dT
\qquad\Rightarrow\qquad
\frac{dP}{dT} = \frac{\Delta s}{\Delta v}.
$$

The transition is isothermal and reversible, so the entropy change is the latent heat divided by the temperature, $\Delta s = L/T$. Substituting gives

$$
\frac{dP}{dT} = \frac{L}{T\,\Delta v}.
$$

For melting, $\Delta v < 0$ in water makes the slope negative, the backward tilt of the melting line.
```

where $L$ is the latent heat of the transition and $\Delta v$ the volume change per unit mass. Two of its consequences run through this book. Along the melting line, ice is anomalous, since melting *shrinks* water ($\Delta v < 0$), the slope is negative and pressure lowers the melting point, the fact that puts the bed of a thick ice sheet at its pressure-melting point in {doc}`../thermomechanics/thermal-structure` and makes the homologous temperature, measured relative to that local melting point, the natural argument of the flow law in {doc}`../ice_flow/ice-rheology`. Along the vapor curve, the saturation vapor pressure falls near-exponentially as air cools, which is why cooling air sheds moisture, why snow falls at all, and why the Rayleigh distillation of {doc}`../climate/paleoclimate` turns the isotopic composition of snow into a thermometer.

Melting ice absorbs 334 kJ/kg without warming at all, and sublimation absorbs nearly ten times that, energies that dominate the heat budgets of melting surfaces, refreezing firn, and the brine pockets of {doc}`../cryosphere/sea-ice`. Where a later chapter balances an energy budget, the largest entries are usually latent.

## Implications for ice flow

It would be possible to treat the heat capacity and conductivity as tabulated numbers and proceed, but the vibrational spectrum earns a chapter of its own because it is the hinge between the molecular structure and the flow of ice. Two connections run forward from here. The first is thermal. The coefficients $c$ and $k$ derived above, together with the pressure dependence of the melting point, set the temperature field of a glacier, and temperature in turn controls the rate factor in Glen's flow law so strongly that warm ice can deform a hundred times faster than cold ice. The thermal properties of the lattice and the mechanics of flow are therefore coupled, the subject of {doc}`../thermomechanics/thermal-structure`.

The second connection is more direct and less obvious. The same anharmonic, thermally agitated lattice that conducts heat is also the medium in which point defects form and migrate. A dislocation gliding on a basal plane cannot advance without rearranging the proton configuration in its path, and that rearrangement is accomplished by the migration of orientational defects, whose creation and motion are thermally activated lattice processes. The activation energy for ice to creep turns out to match the energy to form and move these defects, so the deformation of ice is, at bottom, a defect-mediated process running on the vibrating lattice. The next chapter follows the point defects themselves, and the rheology chapter, {doc}`../ice_flow/ice-rheology`, shows how they set the rate at which ice flows.
