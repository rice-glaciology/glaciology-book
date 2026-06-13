# Ice sheets and their stability

A glacier and an ice sheet obey the same physics, but they do not fail the same way. The mountain glaciers of {doc}`../climate/glacier-variations` gain and lose mass through their surfaces and respond to climate on decadal timescales set by $t_r = H/\dot a_0$. The ice sheets of Greenland and Antarctica are thicker by an order of magnitude, their response times stretch to millennia, and most of Antarctica loses mass not by surface melting at all but by calving and by melting into the ocean at the base of floating ice shelves. This chapter asks what sets the character of the two great modern ice sheets, and then turns to the question their geometry forces on us, whether a marine ice sheet resting on a bed below sea level is stable.

The West Antarctic Ice Sheet and the Greenland Ice Sheet each hold about six meters of sea-level equivalent, East Antarctica holds roughly fifty, and at the last glacial maximum enough ice stood on the continents to lower the ocean by about 120 meters. Chapters 8 and 11 of {cite}`cuffey2010` treat much of this material.

## Greenland and Antarctica

Greenland and Antarctica differ in ways that trace back to the rock beneath them. Greenland sits on old, thick, tectonically quiet continental crust. Its bed is a central depression ringed by coastal mountains, and the depression is not original. The interior bedrock has been pushed below sea level by the weight of the modern ice sheet, and if the ice were removed the bed would relax upward over about fifteen thousand years until nearly all of it stood above the sea {cite}`bamber2001`. The mantle is viscous, so this isostatic adjustment lags far behind the ice. Scandinavia is still rising by almost a centimeter per year in response to the loss of the Fennoscandian ice sheet, and flights of raised beaches around Hudson Bay and Coronation Gulf record the same slow rebound in North America. The lithosphere carries the imprint of an ice age long after the ice is gone, a lag that complicates the gravity measurements of {doc}`../observing/gravity-lab`.

Antarctica is two ice sheets wearing one name. East Antarctica rests on ancient cratonic crust, mostly above sea level, and behaves like a vast, slow, cold version of Greenland. West Antarctica occupies young, thin, rifted crust, and its bed lies mostly below sea level, in places more than two kilometers below, with deep basins that slope downward toward the interior. That single fact, the inland-deepening marine bed, organizes the modern concern about the region's future, and it was recognized as a structural vulnerability long before satellites could watch it being tested {cite}`mercer1978`.

```{figure} figures/ice-sheet-bed-topography.png
:name: fig-ice-sheet-beds
:width: 95%

The rock beneath the ice. Bed elevation for Greenland and Antarctica from radar-sounding compilations (BedMachine and Bedmap), blue below sea level and green-brown above. Greenland's interior depression and the deep marine basins of West Antarctica, sloping inland from the Amundsen coast, are the two facts of this section drawn on a map.
```

## Ice streams and outlet glaciers

The interior of an ice sheet creeps by the internal deformation of {doc}`../ice_flow/shallow-ice`, at meters per year. Almost all of the discharge, however, funnels through narrow corridors of fast flow, the ice streams and outlet glaciers, moving hundreds to thousands of meters per year. The velocity maps of {doc}`../observing/insar-lab` show them as bright rivers of ice draining a nearly stagnant interior.

```{figure} figures/ice-sheet-velocity-maps.png
:name: fig-ice-sheet-velocity
:width: 95%

Surface speed of both ice sheets on a logarithmic scale, from satellite radar interferometry and feature tracking (the NASA MEaSUREs compilations of Rignot, Joughin, and colleagues). The interior creeps at meters per year while the red filaments, ice streams and outlet glaciers moving a thousand times faster, carry nearly all of the discharge to the margins.
```

What makes an ice stream is the bed. Where the substrate is hard crystalline rock, the driving stress is consumed by vertical shear within the ice and the flow stays slow. Where the bed is a wet, weak marine sediment, the till fails at small stress, as described in {doc}`../thermomechanics/basal-motion`, the ice slides as a plug, and resistance must be found elsewhere. On the Siple Coast ice streams the bed supplies so little drag that more than half of the driving stress is carried by the lateral shear margins, bands of intense crevassing a few kilometers wide separating ice moving at hundreds of meters per year from ice moving at almost nothing {cite}`echelmeyer1994`. The mapped coincidence of fast flow with sedimentary basins makes the geological control plain {cite}`studinger2001`. Substrate even reaches into the deep past of the glacial cycles. Clark and Pollard proposed that the early Pleistocene Laurentide ice sheet flowed over a soft regolith that kept it thin and quick to melt, and that erosion of the regolith down to hard bedrock allowed thicker, longer-lived ice sheets, switching the world from 41,000-year to 100,000-year glacial cycles {cite}`clark1998`.

```{admonition} Looking under the ice in Seattle
:class: tip

The streamlined hills of Seattle, Green Lake to Magnolia, are drumlins carved beneath the Puget Lobe of the Cordilleran ice sheet about 15,000 years ago. The lidar maps of the region show the same megascale lineations that ice streams leave on the deglaciated Ross Sea floor. We return to landforms as records of former flow in {doc}`former-glaciers`.
```

## The marine ice-sheet instability

Where an ice sheet ends in the ocean, the grounded ice goes afloat at the grounding line, and the flotation condition ties the ice thickness there to the bed depth, $h_g = (\rho_w/\rho_i)\,|b|$. The flux of ice through the grounding line increases very strongly with the thickness of ice there; boundary-layer analysis of the stress balance gives discharge growing like $h_g$ raised to a power near five {cite}`weertman1974,schoof2007`. Deeper bed, thicker grounding line, faster discharge. Everything follows from that chain.

Consider a grounding line in steady state, discharging exactly the accumulation it is fed. If the bed slopes seaward, prograde, a small retreat moves the grounding line into shallower water, the discharge falls below the supply, and the ice readvances. The geometry is self-correcting. If the bed deepens inland, retrograde, the same small retreat puts the grounding line in deeper water, discharge rises above supply, and the imbalance drives further retreat into still deeper water. There is no stable resting place on a retrograde slope. This flux argument is the content of the stability diagrams of {cite}`schoof2007`, and we have already met its kinematic skeleton in the two-stage model of {doc}`../climate/glacier-variations`, where the instability appears as a sign change in a single stability parameter {cite}`robel2018`.

% TODO Illustrator figure: figures/misi-flux-stability.svg (label fig-misi-flux-stability, width 90%)
% Spec: two stacked panels. Top, grounding-line flux (blue) vs integrated accumulation supply (gray)
% as functions of grounding-line position, with imbalance arrows at each crossing. Bottom, the bed,
% an overdeepened basin between two sills. Prograde crossings stable, retrograde crossing unstable.
% After the stability diagrams of weertman1974, schoof2007.

Retreat across a real bed is therefore episodic rather than smooth. Model reconstructions of deglaciation through overdeepened troughs show the grounding line pausing on sills for centuries and then sweeping across basins at rates of kilometers per year, a punctuated style of retreat that the geological record of the Antarctic shelf corroborates. The instability does not require a trigger to be catastrophic, only a nudge that moves the grounding line off its sill.

## Ice shelves and buttressing

The flux diagram leaves out the floating ice, and the floating ice is where the modern story is being decided. An ice shelf transmits resistance upstream wherever it runs aground on pinning points or drags along fjord walls, and this buttressing reduces the discharge through the grounding line below its unbuttressed value. Removing the shelf removes the restraint. The Larsen B Ice Shelf disintegrated over a few weeks in March 2002, shattered by meltwater-driven hydrofracture, in which water filling surface crevasses pressurizes them beyond the depth where dry crevasses would arrest. The glaciers feeding the lost shelf promptly accelerated several-fold {cite}`scambos2004`, a controlled experiment, performed by nature, on what buttressing had been doing.

```{figure} figures/larsen-b-speedup-wuite.png
:name: fig-larsen-b-speedup
:width: 95%

The experiment's result {cite}`wuite2015`. Velocity of the Larsen B embayment glaciers before the collapse (left, 1995 InSAR), a decade after (middle, 2008–2012 feature tracking), and the fractional increase (right), with tributaries that lost their shelf flowing up to three times faster. The 1995 grounding line is drawn for reference.
```

The same restraint, removed at a single glacier, shows up as a step change in speed. Jakobshavn Isbræ in West Greenland lost its floating tongue between 2000 and 2003 and roughly doubled its discharge, and its speed has breathed seasonally around the faster state ever since.

```{figure} figures/jakobshavn-speed-timeseries.jpeg
:name: fig-jakobshavn-speed
:width: 95%

Two decades of speed at flux gates along Jakobshavn Isbræ (M6 nearest the terminus), from satellite feature tracking by I. Joughin and colleagues. The acceleration after the floating tongue broke up in 2000–2003, the strong seasonal cycle, and the continued creep upward through 2012 are all visible at a glance.
```

In the Amundsen Sea sector of West Antarctica the restraint is being removed from below. Relatively warm Circumpolar Deep Water crosses the continental shelf and melts the undersides of the Pine Island and Thwaites ice shelves at rates of tens of meters per year, thinning them and unpinning them from their seabed ridges. The grounding lines of both glaciers have retreated tens of kilometers in the satellite era, and beneath Thwaites the bed deepens inland for hundreds of kilometers. Model studies of Thwaites find no nearby stable position once retreat passes the current grounding zone, and conclude that the early stage of a marine ice-sheet collapse may already be under way {cite}`joughin2014,parizek2013`. The timescale, centuries, belongs to the slow mode of the marine response, which is precisely why a process with so much inertia can be both quiet and committed at the same time.

A tabular iceberg calving from a shelf front may be spectacular and dynamically trivial, while a modest thinning concentrated at a pinning point can matter enormously. The question to ask of any change at the margin is what it does to the buttressing, and through the buttressing, to the flux through the grounding line.

## Summary

The mass-balance and firn chapters that follow supply the surface boundary condition that ice-sheet evolution needs, and {doc}`../climate/paleoclimate` reads the long record held in the ice sheets in the other direction, from the ice back to the climate. The prognostic icepack labs put the pieces together, evolving ice sheets through glacial cycles, and the grounding-line physics sketched here is exactly what their marine experiments are testing.
