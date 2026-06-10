# Mapping the cryosphere with elevation data

Radar looks inside the ice. Elevation measurements map its surface, and the way that surface changes through time is one of the most powerful observations in glaciology. Surface elevation gives the geometry that flow models need and, through its slope, the driving stress of {doc}`../ice_flow/stress-balance`. Elevation change reveals where ice sheets are thickening or thinning, and over floating ice it can be turned into a basal melt rate. This chapter surveys how surface elevation is measured and what it tells us.

## Measuring surface elevation

Several techniques measure the height of the ice surface, each with its own strengths.

Satellite radar altimeters send a radar pulse from orbit and time its return to the surface. Missions such as ERS, Envisat, and CryoSat-2 have built decades of coverage. Their footprints are large, and over dry snow the radar penetrates below the surface, which complicates the height retrieval, but they observe in all weather and CryoSat-2's interferometric mode improves performance over the steep margins where the ice is changing fastest.

Satellite laser altimeters send a laser pulse instead. ICESat, and since 2018 ICESat-2 with its photon-counting instrument, reflect from the true surface with a small footprint and high precision, giving dense profiles of elevation along the ground track. The laser is blocked by cloud, so coverage is sparser in time. Airborne lidar, flown for example during Operation IceBridge, filled the gap between the two ICESat missions and provides higher-resolution surveys of targeted areas.

Stereo photogrammetry produces elevation in a different way. Two overlapping high-resolution optical images taken from slightly different viewing angles can be matched feature by feature to reconstruct surface height, the same principle as binocular vision. Applied to commercial satellite imagery this yields digital elevation models, or DEMs, at a resolution of a few metres, and continental mosaics such as REMA over Antarctica and ArcticDEM over Greenland and the Arctic now provide a detailed snapshot of the ice surface.

## From elevation to elevation change

Repeating any of these measurements gives the rate of surface elevation change, $\partial h/\partial t$, whether by comparing altimeter passes over the same ground or by differencing DEMs from different dates. Elevation change is the primary signature of an ice sheet that is out of balance. Rapid lowering near the coast marks the dynamic thinning of outlet glaciers that have sped up, while slow changes in the interior reflect long-term shifts in snowfall and flow.

## From elevation change to mass and melt

Turning elevation change into a change in ice mass is not automatic. Part of any height change reflects the low-density firn rather than solid ice, and the firn air content can grow or shrink without any change in mass, so a firn densification model like the one discussed in {doc}`../foundations/snow-to-ice` is needed to separate the two and to assign the right density to the volume gained or lost.

Over floating ice the same data yield something else. Because an ice shelf floats in hydrostatic equilibrium, a measured change in surface height can be converted into a change in ice thickness. Combining that thickness change with the horizontal flow, the strain of the ice, and the surface mass balance isolates the rate at which the ocean is melting the shelf from below. Repeating high-resolution stereo DEMs, co-registering them, and differencing them is how the group maps basal melt across whole ice shelves, a spatial complement to the point measurements that ApRES provides from a single site. The two observations, elevation change from above and phase-sensitive radar from the ice itself, measure the same melt by independent means.
