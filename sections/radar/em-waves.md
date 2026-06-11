# Electromagnetic waves in ice

Most of what is known about the interior of an ice sheet has been learned by sending electromagnetic waves into it and listening to what comes back. Radio waves pass through cold ice for kilometres and reflect from its layers and its bed, visible light passes through the upper few metres and gives glacier ice its blue cast, and between these two windows ice is opaque. All three facts, the radio window, the optical window, and the absorbing band between them, are properties of how the molecules and the lattice of ice respond to an oscillating electric field, and that response is developed, from the molecular physics, in {doc}`../foundations/optical-properties`. This chapter takes that dielectric behaviour as given and shows how it governs the propagation of the waves used to observe the cryosphere. It is the foundation for the radar methods that follow. The standard radioglaciology references are {cite}`bogorodsky1985` and {cite}`petrenko1999`.

## Waves in a dielectric

An electromagnetic wave in a medium with no free charge or current obeys a wave equation that follows from Maxwell's equations,

$$
\nabla\times\nabla\times\mathbf{E} = -\frac{1}{c^2}\,\mu_r\,\epsilon_r\,\frac{\partial^2 \mathbf{E}}{\partial t^2},
$$

in which the relative permittivity $\epsilon_r$ encodes the response of the material. Ice is non-magnetic, so $\mu_r\approx 1$, and the speed at which a wave travels is set entirely by the permittivity,

$$
v=\frac{c}{n},\qquad n=\sqrt{\epsilon_r'},
$$

where $n$ is the refractive index and $\epsilon_r'$ is the real part of the permittivity at the frequency of the wave. The imaginary part, written $\epsilon_r''$, measures absorption, the conversion of wave energy into heat. The permittivity is not a single number but a function of frequency, because the different parts of the molecule and the lattice can follow a slow field but not a fast one. Reading that function from low frequency to high is reading off, in order, which physical response is still able to keep up.

## The two windows

The permittivity of ice and its molecular origins are developed in {doc}`../foundations/optical-properties`; here only its consequences for propagation are needed. Across the radio and microwave range that ice-penetrating radar uses, the dipolar response has relaxed away and the permittivity sits on a low-loss plateau at $\epsilon_r'\approx 3.2$, giving a refractive index $n\approx 1.78$ and a wave speed of about $168$ metres per microsecond, a little more than half the speed in vacuum. This is the radar window, and the near-constancy of the permittivity across it is the single fact that makes radioglaciology possible: a pulse can travel down through kilometres of cold ice and back with enough energy left to record, and one wave speed converts its travel time into distance. At far higher frequencies the lattice vibrations absorb and ice is opaque through the infrared, until in the visible only the electrons respond, the permittivity settles to about $1.72$, and the index is $1.31$. This is the optical window through which we see ice and through which laser altimeters range to its surface. Every electromagnetic method below works in one window or the other.

## Wave speed and depth sounding

Because the radar window has a nearly constant permittivity, the speed of a radio wave in cold ice is nearly constant, and this is what turns a radar into a ruler. A pulse sent downward reflects from the bed and returns after a two-way travel time, and multiplying half that time by the wave speed gives the ice thickness. Radio-echo sounding mapped the beds of Greenland and Antarctica this way, and it remains the primary means of measuring ice thickness. One correction matters near the surface. In the firn of {doc}`../foundations/snow-to-ice` the ice is mixed with air, which lowers the permittivity and raises the wave speed, so the travel time through the firn layer must be corrected for its lower density before the thickness is read.

## Attenuation and the limits of the window

The radar window is not perfectly transparent. The same ionic defects that carry the small electrical conductivity of ice, introduced in {doc}`../foundations/point-defects`, absorb a little of the wave at radio frequencies, and this dielectric loss sets how far a radar can see. The absorption increases with temperature, so warm and temperate ice is far more attenuating than cold polar ice, and it increases with the concentration of dissolved impurities, particularly the acids from past volcanic eruptions. A radar can sound several kilometres of cold ice but is quickly defeated by the wet, warm ice of a temperate glacier. The temperature dependence is strong enough that the attenuation of the returning signal itself carries information about the temperature of the ice column.

## Internal layers and anisotropy

Between the surface and the bed a radar records a series of internal echoes, the englacial layers, and each comes from a contrast in permittivity. Three kinds of contrast produce them. In the firn the contrasts are in density, as the wave crosses layers of differing porosity. Deeper in the ice they are in conductivity, where thin horizons of acidic fallout from volcanic eruptions reflect the wave, and these horizons, being deposited everywhere at once, are surfaces of equal age that can be traced across whole ice sheets to map accumulation and to transfer the chronology of {doc}`../climate/paleoclimate` between cores. The third kind of contrast is in crystal orientation. The permittivity of a single ice crystal differs slightly along and across its c-axis, the dielectric anisotropy noted in {doc}`../foundations/ice-structure`, so a change in fabric reflects the wave and, more importantly, makes the bulk ice birefringent. A radio wave splits into fast and slow polarizations that drift apart with depth, and measuring that splitting recovers the crystal fabric, the subject of {doc}`radiowave-fabric`. With the propagation, the speed, the attenuation, and the reflections all traced back to the response of the molecules and the lattice, the radar instruments of the next chapters can be read as measurements of the ice itself.
