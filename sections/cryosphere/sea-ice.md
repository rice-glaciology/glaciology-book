# Sea ice

Everything to this point in the book has been freshwater ice, the distilled precipitate of the atmosphere; the ice in this chapter grows instead from a salty, turbulent ocean, and the salt rewrites nearly every property the earlier chapters derived. The ice that floats on the polar oceans is a different material, a composite of pure ice, liquid brine, and gas whose properties change drastically with temperature, and it covers an area comparable to a continent in each hemisphere, growing and shrinking by tens of millions of square kilometers with the seasons. Sea ice makes up about two thirds of the cryosphere's surface area while holding a tenth of a percent of its ice volume, and that disproportion is exactly why it matters to climate. A thin, vast, bright lid on a dark ocean is the most leveraged piece of ice on the planet. The standard reference for this material is the sea ice literature gathered in {cite}`thomas2017`, and the thermodynamic framework descends from {cite}`maykut1971`.

## Why the ocean freezes differently

A freshwater lake freezes promptly once autumn arrives, and the reason is a quirk of the water molecule we met in {doc}`../foundations/water-molecule`. Fresh water is densest at 4 °C, so once the surface cools past that point it floats on the warmer water below, the convection shuts down, and only a thin surface layer needs to reach the freezing point before ice forms.

Dissolved salt removes the density maximum. For salinities above 24.7‰, seawater gets denser all the way down to its freezing point, near −1.8 °C at a salinity of 32‰, so cooling surface water keeps sinking and the ocean must typically chill its upper 100 to 150 meters to the freezing point before ice can persist. Sea ice therefore forms late, and it forms in the open, turbulent ocean rather than on a still pond. Freezing begins as frazil, small needles and platelets nucleating throughout the stirred surface layer and floating up as slush. In calm water the slush congeals into a thin elastic sheet called nilas; in waves it forms pancakes, rounded cakes with raised rims that eventually weld together. Once a solid cover exists, further growth is congelation at the bottom of the ice, paced by how fast heat can be conducted up through the ice to the cold air.

## A crystal, a film of brine, and the skeletal layer

Salt does not fit in the ice lattice of {doc}`../foundations/ice-structure`, so the growing interface rejects it. The rejected salt accumulates in a thin boundary layer ahead of the interface, and because salt diffuses far more slowly than heat, a zone of constitutional supercooling develops just below the growing ice. A flat interface is unstable in that situation. Any protrusion reaches into more supercooled water and grows faster, so the interface organizes itself into parallel blades of pure ice, the skeletal layer, with brine concentrated in the grooves between them. As growth continues, ice bridges trap the grooves into vertical strings of brine inclusions. Freshwater ice has no skeletal layer; the salt makes the microstructure.

The same competition selects the crystal fabric. After ten or twenty centimeters of congelation growth, geometric selection leaves only crystals whose c-axes lie horizontal, because growth along the basal plane is faster, and the ice becomes a columnar tissue of horizontally oriented crystals, a fabric story parallel to the one told for glacier ice in {doc}`../ice_flow/ice-fabric`.

The trapped brine cannot freeze solid, because a brine pocket must sit at the freezing point of its own salinity. Cool the ice and the pocket walls freeze inward, concentrating the brine until its depressed freezing point matches the new temperature; warm the ice and the walls melt back. Sea ice consequently has no single melting point, only a temperature-dependent liquid fraction. The brine volume fraction follows from this freezing equilibrium as

$$
\nu_b \;\cong\; \frac{\rho_i S_i}{\rho_b S_b} \;\cong\; -\frac{m\,\rho_i\,S_i}{\rho_b\,T_i},
$$

with $S_i$ the bulk ice salinity, $S_b$ the brine salinity, $\rho_i, \rho_b$ the densities, $T_i$ the temperature in Celsius, and $m$ the liquidus slope. Fast-grown young ice traps more salt, with salinity decreasing as the ice thickens and ages, from roughly 10‰ in thin first-year ice toward 5‰ or less in multiyear ice that has flushed its brine.

% TODO Illustrator figure: figures/brine-volume.svg (label fig-brine-volume, width 80%)
% Spec: brine volume fraction vs temperature for first-year (S_i = 10 permil) and multiyear
% (S_i = 5 permil) ice from the freezing-equilibrium relation; liquid fraction diverging toward
% the freezing point; cite thomas2017.

## Properties ruled by the brine

The brine is not hypothetical; under a microscope it is the texture of the material.

```{figure} figures/brine-inclusions-light.png
:name: fig-brine-inclusions
:width: 50%

Brine inclusions in first-year Arctic sea ice under transmitted light, in vertical section {cite}`light2003`. The dark vertical tubes and pockets are liquid brine threaded along the crystal boundaries of the columnar ice; their connectivity, and with it the ice's permeability, switches on as the ice warms.
```

Almost every bulk property of sea ice is the pure-ice value corrected by the brine volume, which makes the brine-volume curve the master curve of the subject. The effective latent heat of fusion is reduced, $L_i = L_0(1-\nu_b)$, since the brine fraction is already liquid; new ice can require only 60% of the energy that pure ice would to melt. The thermal conductivity is dragged down from $2.4\ \mathrm{W\,m^{-1}\,K^{-1}}$ for pure ice toward the brine value of $0.6$, so salty warm ice insulates the ocean and slows its own growth. The effective specific heat,

$$
c_i = c_0 + a\,T_i + \frac{b\,S_i}{T_i^{2}},
$$

includes the latent heat of the internal melting and freezing that any temperature change forces in the brine pockets, and near the melting point it exceeds the pure-ice value by up to two orders of magnitude. Mechanical strength collapses as the brine volume grows, which is the practical limit on travel over spring ice. The thermal physics here is the heat equation of {doc}`../thermomechanics/thermal-structure` again, with coefficients that depend savagely on temperature.

The brine also drains. Gravity drainage and flushing expel salt as the ice ages, so bulk salinity falls with thickness and age, rapidly in the first half metre of growth and slowly thereafter, which is why multiyear ice is fresher, stronger, and a poorer conductor than the first-year ice that now dominates the Arctic.

```{figure} figures/sea-ice-salinity-thickness.jpeg
:name: fig-salinity-thickness
:width: 80%

Bulk salinity against ice thickness for cold first-year sea ice, compiled from four field datasets (legend), with piecewise fits. Thin new ice starts near 15‰ and desalinates quickly to the slowly declining trend beyond about half a metre, the drainage history that the brine-volume curve inherits.
```

## Motion, deformation, and decline

Glacier ice creeps at meters per year; the sea-ice pack travels at the pace of the weather driving it. Pushed by wind and ocean stress, the Arctic pack circulates at kilometers per day, clockwise around the Beaufort Gyre and across the pole in the Transpolar Drift, exporting roughly a tenth of the basin's ice through Fram Strait each year. Where floes diverge they open leads, windows of dark ocean that lose heat furiously in winter and absorb sunlight in summer. Where they converge they raft and ridge, stacking ice into keels tens of meters deep. The thickness of the pack is therefore as much a record of deformation as of freezing.

The modern decline of Arctic sea ice runs through this entire chapter. September extent has fallen by roughly 13% per decade over the satellite record, submarine sonar shows the mean draft thinner by more than a meter since the 1960s, and the old multiyear ice has largely been replaced by first-year ice, which is saltier, weaker, and more easily melted. The amplifier is the ice–albedo feedback. Sea ice reflects 60 to 90% of incoming sunlight while open water reflects under 10%, so a little melting exposes dark ocean, which absorbs more heat, which melts more ice. Melt ponds push the summer ice albedo down toward 0.45 even before the ice is gone. The feedback operates on the same radiative physics introduced in {doc}`../foundations/optical-properties`, and it is the leading reason the Arctic warms at twice the global rate. Sea ice extent and thickness are monitored by the passive microwave, laser, and radar altimetry methods of {doc}`../observing/elevation`, which is where the observational thread of this chapter continues.

```{figure} figures/arctic-thinning-scicex.png
:name: fig-scicex-thinning
:width: 80%

The submarine evidence {cite}`rothrock1999`. Change in mean ice draft, in metres, between sonar surveys of the 1960s–70s and the 1990s SCICEX cruises, by region. Every region thinned, the central basins by more than a metre, an early and unambiguous measurement of the pack's decline.
```

Sea ice is the fastest-changing member of the cryosphere and the one whose physics this book's machinery captures at the smallest scale, brine pockets standing in for the defects and inclusions of the early chapters, the heat equation running with coefficients that a few degrees can change by an order of magnitude. It is also the cryosphere most people will never see, which is worth holding alongside the next chapter, about ice that no one can see anymore because it is gone, surviving only in the shapes it left behind.
