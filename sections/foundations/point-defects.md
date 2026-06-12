# Point defects

A perfect ice crystal would be a poor conductor of electricity, would not relax in an oscillating field, and, more surprisingly, would barely flow at all. The properties that make ice interesting as a geophysical material come from its imperfections. This chapter collects the point defects of the ice lattice, the small departures from the ideal structure that allow protons to rearrange, molecules to migrate, and dislocations to move. They are the agents that connect the static crystal of {doc}`ice-structure` to the dielectric response sensed by radar and to the creep that lets ice sheets flow. The treatment follows Chapter 7 of {cite}`fletcher1970`, with values updated from {cite}`petrenko1999`.

## Departures from the ice rules

The structure of ice was defined by three conditions: each site holds a water molecule bonded tetrahedrally to its four neighbors, exactly two protons lie close to each oxygen, and exactly one proton sits on each bond. A perfect crystal obeys all three everywhere. At any finite temperature, though, thermal agitation creates a small equilibrium population of sites where one of the rules fails, and each kind of failure is a distinct defect with its own energy of formation and its own consequences. Removing a molecule from its site leaves a vacancy, and forcing one into the open spaces of the lattice makes an interstitial; these violate the first rule and govern how molecules diffuse. Moving a proton from its bond to the far oxygen creates an ionic pair and violates the second rule. Rotating a molecule so that a bond ends up with two protons or none creates an orientational defect and violates the third. The two latter families, the ionic and orientational defects, are peculiar to the hydrogen-bonded structure of ice and are the ones that carry charge and enable flow.

## Ionic defects

An ionic defect appears when a proton jumps from its normal position near one oxygen across the hydrogen bond to the other, converting the two molecules it joins into a hydronium ion $\mathrm{H_3O^+}$ and a hydroxyl ion $\mathrm{OH^-}$. Once a second jump on a neighboring bond separates the two ions, they can drift apart and survive as independent charged defects. They are the carriers of the small direct-current conductivity of ice. Forming a separated pair costs an enthalpy of order one electron volt, appreciably more than in liquid water, because the rigid ice lattice cannot reorganize around the new ions the way mobile liquid molecules can. As a result the equilibrium concentration of ionic defects in ice is some two orders of magnitude smaller than in water at the same temperature, of order $10^{10}$ per cubic centimeter near $-10\ \mathrm{^\circ C}$.

What the ionic defects lack in number they make up in mobility. The positive defect in particular is extraordinarily mobile, because moving it requires only that an excess proton hop from one essentially neutral molecule to the next, a transfer that can proceed by quantum tunneling along the bonds. Its mobility approaches that of electrons in a semiconductor like germanium and far exceeds the mobility of ordinary ions in solids. The negative defect moves more sluggishly, by a factor that ranges from a few to a hundred, because shifting it amounts to moving a proton vacancy through a network of negatively charged units. The barrier to motion is set sensitively by the oxygen-oxygen spacing, and the proton transfer is not a simple classical hop over the barrier but is coupled to the vibrations of the surrounding lattice, another point at which the lattice dynamics of the previous chapter enter.

## Orientational, or Bjerrum, defects

The second native family was proposed by Bjerrum to explain how the molecules of ice can change their orientation at all. If a single molecule rotates by one third of a turn about one of its bond directions, it leaves one bond carrying two protons and another carrying none. The doubly occupied bond is called a D-defect, from the German for doubly, and the empty bond an L-defect. Like the ionic defects they are created in pairs and can then diffuse apart by successive molecular rotations, each rotation handing the defect on to a neighbor.

```{figure} figures/bjerrum-defect-lattice.png
:name: fig-bjerrum-defect
:width: 55%

A patch of proton-disordered lattice with a misbonded molecule (blue) carrying an orientational defect. Each molecular rotation hands the defect to a neighbor, so the blue site wanders through the crystal, and every molecule it visits comes away reoriented.
```

Two facts about the orientational defects make them central to what follows. They are far more numerous than the ionic defects, with a formation energy near $0.68\ \mathrm{eV}$ giving an equilibrium concentration of order $10^{15}$ to $10^{16}$ per cubic centimeter near $-10\ \mathrm{^\circ C}$, a thousand times the ionic population. And they are the only mechanism by which a water molecule can reorient. A molecule cannot simply turn in place without violating the bonding rules with all four of its neighbors; reorientation happens only as a D- or L-defect passes through, rotating each molecule it visits. The migration of these defects is thermally activated, with an energy barrier of a few tenths of an electron volt, and is slower than the motion of the ionic defects despite their greater number. Because they reorient the molecular dipoles, the orientational defects control the dielectric relaxation of ice, and because they rearrange the proton configuration ahead of a moving dislocation, they also control the rate of creep. The same defect therefore links the electrical and mechanical behavior of ice, a connection developed in {doc}`../radar/radiowave-fabric` and {doc}`../ice_flow/ice-rheology`.

## Impurities as dopants

A small amount of chemical impurity changes the defect populations in a way closely analogous to doping a semiconductor. Two impurities are especially instructive because they enter the lattice substitutionally and act as proton donors and acceptors. Ammonia, $\mathrm{NH_3}$, is nearly the same size as a water molecule and carries one proton too few; sitting in the lattice it behaves as a proton acceptor that generates D-defects and negative ionic states while depressing their opposites. Hydrogen fluoride, $\mathrm{HF}$, carries one proton too many and behaves as a proton donor that generates L-defects and positive ionic states. The parallel with electron donors and acceptors in silicon and germanium is exact enough that the same statistical relations describe the defect concentrations, with the dissociated defect concentration rising as the square root of the impurity content. This doping analogy is not a curiosity. It is the basis of a decisive experiment on the mechanism of ice flow, discussed in the rheology chapter, in which a few parts per million of hydrogen fluoride, by supplying L-defects, measurably speeds the creep of single crystals.

## Self-diffusion, vacancies, and interstitials

Distinct from the proton-rearranging defects is the bodily migration of whole molecules through the lattice, the process measured by following isotopically labeled water. All the tracers, whether labeled in oxygen or hydrogen, diffuse at essentially the same rate, about $2$ to $3\times10^{-11}\ \mathrm{cm^2\,s^{-1}}$ near $-10\ \mathrm{^\circ C}$ with an activation energy of about $0.6\ \mathrm{eV}$. That they share a common rate shows that self-diffusion proceeds by the motion of complete molecules and not by the proton jumps that dominate the electrical behavior. The most likely carrier is the vacancy: a molecule hops into a neighboring empty site, and the vacancy moves the other way. Forming a vacancy costs about $0.5\ \mathrm{eV}$, roughly the energy to lift a molecule from the interior to a surface step, giving an equilibrium vacancy concentration near $10^{12}$ per cubic centimeter at $-10\ \mathrm{^\circ C}$. Interstitial molecules, which the open structure accommodates more easily than a close-packed crystal would, are present in smaller numbers, of order $10^{10}$ to $10^{11}$ per cubic centimeter. The diffusion is slightly faster along the c-axis than across it, by about ten percent, and where dislocations thread the crystal they offer easy pipes for transport along their disordered cores. Self-diffusion matters for flow because it controls the climb of dislocations, the out-of-plane motion by which dislocations escape obstacles and annihilate one another, and so helps set the steady creep rate discussed next door.

## Rate processes and the Arrhenius law

Every defect process met so far, the dissociation of an ion pair, the jump of a Bjerrum defect, the hop of a vacancy, is a thermally activated process: the system must borrow enough energy from the thermal vibrations of the lattice to surmount an energy barrier before it can pass from one configuration to the next. The temperature dependence of all of them, and through them the temperature dependence of how ice flows, follows from one simple argument. The rate at which a barrier of height $\Delta U$ is crossed is the product of how often the system attempts the crossing and the probability that any one attempt has enough energy,

$$
\text{rate} = \nu_0\,\exp\!\left(-\frac{\Delta U}{k T}\right).
$$

The attempt frequency $\nu_0$ is set by the lattice vibrations of {doc}`lattice-dynamics`, the oscillation that rattles the defect against its barrier, and is of order $10^{12}$ to $10^{13}\ \mathrm{Hz}$. A fuller transition-state treatment replaces $\Delta U$ by an activation free energy and folds an entropy of activation into the prefactor, but the essential content is the exponential Boltzmann factor: warming the crystal multiplies the rate of every activated process, and steeply, because the barrier sits in the exponent.

The activation energy that governs creep is built from the defect energetics already assembled. Two pieces enter. The orientational defects that pace a gliding dislocation must first exist, and because they form in pairs their equilibrium concentration carries half the formation enthalpy,

$$
n_\pm \propto \exp\!\left(-\frac{H_f}{2kT}\right),
$$

since the law of mass action makes $n^2$, not $n$, proportional to $\exp(-H_f/kT)$. Once present, each defect migrates by jumping over its own barrier $H_m$ at the activated rate above. The rate at which the proton configuration is reordered, and therefore the rate at which dislocations glide and the ice deforms, is the product of how many defects there are and how fast each moves,

$$
\dot\varepsilon \;\propto\; n_\pm\,\nu \;\propto\; \exp\!\left(-\frac{H_f/2 + H_m}{kT}\right) \;=\; A_0\,\exp\!\left(-\frac{Q}{RT}\right),
$$

where the last form is written per mole, with $R$ the gas constant, and the activation energy is

$$
Q = \tfrac12 H_f + H_m .
$$

This is the Arrhenius law of ice flow, derived from the chemistry of the lattice rather than fitted to creep data. The numbers close the argument. The Bjerrum pair formation enthalpy is about $0.68\ \mathrm{eV}$ and the migration barrier about $0.24\ \mathrm{eV}$, so $Q \approx 0.34 + 0.24 \approx 0.58\ \mathrm{eV}$, near $56\ \mathrm{kJ\,mol^{-1}}$. The activation energy measured for the creep of cold ice is close to $60\ \mathrm{kJ\,mol^{-1}}$, in agreement {cite}`fletcher1970`. The temperature sensitivity of glacier flow is thus a defect property: the same orientational defects that relax the dielectric response set the exponential by which ice softens as it warms.

The rate factor of {doc}`../ice_flow/ice-rheology` is this Arrhenius law carrying the load. Two glaciological refinements are added there rather than here. Near the melting point additional processes raise the effective activation energy onto a second, steeper Arrhenius branch, and the temperature in the exponent is measured relative to the pressure-melting point, the homologous temperature, so that deep ice under high pressure behaves as though warmer than its absolute temperature. Both are elaborations of the single exponential derived above.

## Electrical and mechanical roles of defects

The orientational defects, by reorienting molecular dipoles, give ice its large static permittivity and its characteristic dielectric relaxation, with a relaxation time of order $10^{-4}\ \mathrm{s}$ and a permittivity that falls from near $100$ at low frequency to about $3.2$ in the microwave range used by radar. That relaxation, and its anisotropy along and across the c-axis, is what lets radio-echo sounding sense the crystal fabric of ice, the subject of {doc}`../radar/radiowave-fabric`. The same orientational defects, by rearranging protons in front of gliding dislocations, set the activation energy for creep and so underlie Glen's flow law. The proton disorder of ice, introduced in the previous chapters as a structural curiosity, turns out to be the feature that makes ice both electrically active and mechanically soft. The ice deformation chapters take up that softness directly.
