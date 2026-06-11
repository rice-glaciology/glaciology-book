# Heat flow and the basal thermal state

The molecular chapters established how a single temperature controls the softness of ice, through the Arrhenius rate factor derived in {doc}`../foundations/point-defects`. This chapter works at the opposite scale. It follows heat through the whole thickness of a glacier to answer the question that governs basal processes: is the bed frozen to the rock beneath it, or is it at the melting point and lubricated by water? A frozen bed holds the ice fast and forces it to move by internal deformation alone. A thawed bed lets it slide, and sliding is what makes ice streams fast. The thermal state of the bed is therefore the boundary condition that the next chapter, {doc}`basal-motion`, builds upon, and reaching it means accounting for the macroscopic flow of heat. The thermal structure of glaciers is treated in Chapter 9 of {cite}`cuffey2010`.

## The heat budget

The temperature of a parcel of ice is set by a competition among several processes. Heat is conducted through the ice from warmer to colder regions. The flowing ice carries its temperature with it, a transport called advection, so cold surface ice can be drawn down into the interior and warm basal ice can be carried toward an outlet. Heat enters from the bed as a geothermal flux from the Earth below, and it is generated within the ice itself wherever the ice deforms, since the work done against viscous resistance is dissipated as heat. Near the surface, the refreezing of meltwater releases latent heat that can warm the firn substantially.

Collecting these terms gives the heat equation for ice,

$$
\rho c \left(\frac{\partial T}{\partial t} + \bu\cdot\nabla T\right) = \nabla\!\cdot\!(k\,\nabla T) + \Phi,
$$

where $\rho$ is density, $c$ is the specific heat capacity, $k$ is the thermal conductivity, and $\Phi$ is the rate of heating by internal deformation. The term with $\bu$ is the advection of heat by the flow, and the divergence term is conduction.

This is a prognostic equation. The time derivative on the left says that the temperature field is not a fixed property of a glacier but something that evolves, carried along and reshaped by the very flow it helps to drive. Strictly, then, heat flow belongs with the prognostic materials of the later part of the book, alongside the thickness evolution it parallels, and a full model steps temperature and geometry forward together. We introduce it here, ahead of that machinery, for one reason: its quasi-steady consequence at the bed. The basal thermal state changes slowly compared with the flow above it, so for the diagnostic question of whether the bed slides it is enough to ask where the temperature profile reaches the melting point. We solve that reduced, near-steady problem now, and return to the full time evolution, coupled to climate and mass balance, with the prognostic modeling.

## Where the coefficients come from

The two material properties in this equation, the specific heat and the thermal conductivity, are not arbitrary constants. They are set by the lattice vibrations of {doc}`../foundations/lattice-dynamics`, and their values and temperature dependence shape the thermal structure in ways worth keeping in view. The specific heat is large because water molecules are light, about $2.1\ \mathrm{kJ\,kg^{-1}\,K^{-1}}$ near the melting point, and it decreases steadily as the ice cools and the stiffer vibrational modes freeze out, falling by roughly a third in the coldest polar ice. The conductivity behaves oppositely. Because heat is carried by phonons that are scattered ever more frequently as the temperature rises, the conductivity grows as the ice cools, from about $2.1\ \mathrm{W\,m^{-1}\,K^{-1}}$ near melting to half again as much in cold interior ice. Cold ice therefore both stores less heat per degree and conducts it better than warm ice.

What the flow actually feels is the combination of the two, the thermal diffusivity $\kappa_T = k/\rho c$, which measures how fast a temperature signal spreads by conduction and is about $1.1\times10^{-6}\ \mathrm{m^2\,s^{-1}}$ for cold ice. The distance a signal diffuses grows only as the square root of time, so over a single year conduction reaches just a few meters into the ice. This is why the seasonal swing of surface temperature is erased within the upper ten to twenty meters, why the temperature at that depth records the mean annual climate, and why advection by the flow, not conduction, carries cold surface ice deep into the interior of a fast-moving ice sheet. The smallness of the diffusivity is the reason the advection term in the heat equation so often dominates.

## Three profiles you can write down

Before turning to numbers and maps, it is worth knowing the three analytical solutions of the heat equation that explain most of what boreholes measure. Each is a different two-term balance, and together they bracket the real profiles.

**The seasonal wave.** Near the surface, advection is negligible and the heat equation reduces to pure diffusion, $\partial T/\partial t = \kappa_T\,\partial^2 T/\partial z^2$. Force the surface with an annual oscillation of amplitude $\Delta T$ and frequency $\omega$ and the solution is a damped, lagged wave,

$$
T(z,t) = T_0 - \Delta T\, e^{-\alpha z}\cos(\omega t - \alpha z),
\qquad \alpha = \sqrt{\frac{\omega}{2\kappa_T}},
$$

penetrating to a depth $z_* = \sqrt{\kappa_T P/\pi}$ for a forcing of period $P$, about 0.2 m for the daily cycle and 3 m for the annual one. This is the quantitative version of the statement made earlier that the seasons are erased within the upper ten to twenty meters, and the phase lag $\alpha z$ means midwinter cold arrives at depth months late. The permafrost trumpet diagram of {doc}`../cryosphere/permafrost` is this same solution drawn in soil.

```{figure} figures/seasonal-wave-periods.png
:name: fig-seasonal-wave-periods
:width: 95%

The damped wave solution drawn for surface forcing periods of 1, 10, and 100 years, with snapshots through each cycle. The envelope scales as $\sqrt{P}$ exactly as $z_*$ promises, so the annual wave dies within about 15 m while a century-scale climate oscillation still registers at 50 m, which is why borehole temperatures remember past climate. After B. Hills and co-workers (2018).
```

**The conductive profile.** In ice that is thick, slow, and old enough to ignore advection, the steady balance is conduction alone, and with the geothermal flux $G$ entering the base the profile is linear, $T = T_s + G(H-z)/k$. The bed then reaches the melting point at a critical thickness

$$
H_c = \frac{k\,(T_m - T_s)}{G},
$$

about 1750 m for a surface 50 °C below melting and $G = 60\ \mathrm{mW\,m^{-2}}$. Conduction alone, with no help from friction or strain heating, is enough to thaw the base of sufficiently thick ice, and for thicker ice the excess heat goes to basal melting rather than warming.

**The Robin divide solution.** Beneath an ice divide the flow is straight down, with vertical velocity $w \approx -az/H$ for accumulation rate $a$, and the steady balance of downward advection against conduction, $w\,\partial T/\partial z = \kappa_T\,\partial^2 T/\partial z^2$, integrates to an error-function profile {cite}`robin1955`. Its character is set by a single dimensionless group, the Peclet number

$$
Pe = \frac{aH}{\kappa_T},
$$

the ratio of advective to conductive heat transport. High accumulation (large $Pe$) flushes cold surface ice downward, holding the upper column isothermal at the surface temperature and compressing all the geothermal warming into a thin basal layer; low accumulation lets the profile relax toward the conductive line. The kink seen partway down many interior boreholes, where mid-depth ice is colder than the ice above and below it, is the signature of the third process, horizontal advection of ice from the colder, higher interior, and needs the full equation rather than any of these reduced balances.

```{figure} figures/divide-temperature-profile.png
:name: fig-divide-profile
:width: 75%

A temperature profile beneath an ice divide, plotted as height above the bed. The upper half of the column rides near the surface temperature while the geothermal warming is compressed into the lowest kilometre, the high-Peclet Robin shape, and the bed here stays a few degrees below the melting point.
```

```{figure} figures/jakobshavn-temperature-profiles.png
:name: fig-jakobshavn-profiles
:width: 70%

Measured profiles from the fast-flowing trunk and margins of Jakobshavn Isbræ {cite}`luthi2002`. The mid-depth minimum near −22 °C is cold interior ice advected downstream faster than conduction can erase it, the kink that no one-dimensional balance reproduces, while strain heating drives the basal ice toward the pressure-melting line (dashed) at the bed.
```

In a slow-moving ice sheet far from the margin, the temperature is lowest at the surface, set by the cold air, and generally increases with depth as the geothermal flux warms the ice from below and deformation adds heat near the bed. Whether the base reaches the melting point depends on the surface temperature, the ice thickness, the geothermal flux, and the rate of deformational heating. This question matters because a frozen bed holds the ice fast, while a bed at the melting point allows sliding and the fast flow that comes with it.

The melting point of ice is not fixed. It decreases as pressure increases, by about 0.07 to 0.1 degrees Celsius for every hundred metres of overlying ice, so the base of a three-kilometre-thick ice sheet can be at the melting point even though its temperature is below zero degrees Celsius. This dependence is a direct consequence of the open crystal structure of {doc}`../foundations/ice-structure`: because ice is less dense than the water it melts to, pressure favors the denser liquid, and the Clausius-Clapeyron relation turns that volume change into a falling melting point. The same molecular fact that makes ice float lowers the melting point at the bed. Ice that is everywhere below the melting point is called cold, ice that is at the melting point throughout is called temperate, and ice that contains both is called polythermal. Many of the world's mountain glaciers are temperate or polythermal, while the interiors of the polar ice sheets are cold with beds that may be frozen or thawed depending on local conditions.

## Polythermal glaciers and the temperate basal layer

The division of ice into cold, temperate, and polythermal is not just a label; it describes a layered thermal structure that controls how a glacier flows. In a polythermal glacier the upper ice is cold, held below the melting point by cold winters, while a layer at the base has been warmed to the pressure-melting point by the geothermal flux and, above all, by the strain heating concentrated near the bed where the shear is fiercest. The surface that separates the two, the cold-temperate transition surface, is a genuine internal boundary. Below it the ice can warm no further, because at the melting point any additional heat goes not into raising the temperature but into melting a small fraction of the ice in place, leaving the temperate layer at the melting point with a few percent of interstitial liquid water threaded along its grain boundaries.

That basal water has two consequences that feed back on the flow. It softens the ice, because the water content raises the rate factor of {doc}`../ice_flow/ice-rheology`, so the temperate layer deforms faster than cold ice at the same stress. And where the temperate layer reaches the bed it thaws it, permitting the sliding of {doc}`basal-motion`. The polythermal structure is also visible from the surface: the wet temperate ice scatters radio waves, through the dielectric loss of {doc}`../radar/em-waves`, so ice-penetrating radar sees the temperate layer as a diffuse, bright zone and can map the transition surface directly. Many Svalbard and Scandinavian glaciers, and the margins of the polar ice sheets, are polythermal in exactly this way.

## Thermomechanical instability and the surge cycle

The feedback between temperature and flow does more than localize streams. In some glaciers it cannot settle into a steady state at all, and the glacier instead oscillates between slow and fast flow in a cycle called a surge. A surge-type glacier spends most of its life in a long quiescent phase, decades to centuries, flowing slowly and thickening in an upper reservoir zone while its lower tongue thins and stagnates. This quiescence ends abruptly in a short active phase, months to a few years, during which the glacier flows ten to a thousand times faster, transferring a great volume of ice down-glacier into the receiving zone and often advancing the terminus by kilometres. Only a small fraction of the world's glaciers surge, and they cluster in particular regions, which is itself a clue that surging is set by the thermal and hydrological regime of the bed {cite}`meier1969,sevestre2015`.

Two regulating mechanisms are recognized, and the first is a heat-flow instability of exactly the kind this chapter has been building toward. In the thermally regulated surges of Svalbard and other Arctic glaciers, the bed is largely frozen during quiescence, so the glacier flows slowly by internal deformation and thickens. The thickening insulates the bed from the cold surface and, together with the growing strain heating in the thickening ice, warms the base toward the melting point. When the bed reaches the pressure-melting point over a large enough area, it thaws, sliding and till deformation switch on, and the surge begins. The surge rapidly draws down the reservoir and thins the ice; the thinner ice conducts the surface cold to the bed more effectively, the reduced thickness and driving stress cut the strain heating, the bed refreezes, sliding shuts off, and the glacier returns to quiescence to begin the cycle again. This is a thermomechanical relaxation oscillation, the large-amplitude expression of the same coupling that, in milder form, merely localizes ice streams, and its slow thermal timescale sets the decade-to-century period of the cycle.

The second mechanism is hydrological rather than thermal and governs the faster surges of temperate glaciers such as Variegated Glacier in Alaska. There the bed is everywhere at the melting point, and the switch is in the drainage system: an efficient channelized network keeps the water pressure low and the bed strong during quiescence, but when the drainage becomes inefficient and distributed the water pressure rises, the effective pressure of {doc}`hydrology` collapses, and the bed slides fast until an efficient system re-establishes, often abruptly through an outburst flood, and the surge halts {cite}`kamb1985`. The two mechanisms are end members of a single picture in which surging happens wherever the throughput of ice cannot be balanced by a steady thermal and hydrological state of the bed {cite}`sevestre2015`.

The surge cycle is easier to believe once you have watched one. The clip below shows Paulabreen, a polythermal tidewater glacier in Svalbard that surged between about 2003 and 2005, its terminus advancing rapidly during the active phase as ice flushed from the reservoir into the receiving zone, an example of the thermally regulated cluster discussed above.

```{raw} html
<video controls width="85%" preload="metadata" style="max-width: 700px;">
  <source src="https://github.com/rice-glaciology/glaciology-book/releases/download/media-v1/paulabreen-surge.m4v" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>The 2003–2005 surge of Paulabreen, Svalbard.</em></p>
```

## The thermal state of the bed

The single most consequential output of this heat flow is the temperature at the bed. The bookkeeping there is a boundary condition rather than a differential equation. At a frozen bed, the geothermal flux simply continues into the ice, $G = -k\,\partial T/\partial z$. Once the bed reaches the melting point, frictional heating from sliding joins the budget and the surplus goes into melt,

$$
G + \tau_b u_b - mL = -k\,\frac{\partial T}{\partial z},
$$

where $\tau_b u_b$ is the rate of frictional work at the bed, $m$ the basal melt rate (negative for freeze-on), and $L$ the latent heat of fusion. The frictional term makes the condition two-faced. Sliding produces heat, heat produces water, and water promotes sliding, the same feedback loop that drives the thermally regulated surges above and, scaled up to the Laurentide ice sheet, the binge-purge oscillation proposed to explain the Heinrich iceberg discharges in the ice-age record of {doc}`../climate/paleoclimate` {cite}`macayeal1993`. Where the basal temperature reaches the pressure-melting point, the heat that can no longer raise the temperature instead melts ice, and the resulting water lubricates the interface. That is the threshold at which deformation gives way to sliding, and it is where the next chapter begins.
