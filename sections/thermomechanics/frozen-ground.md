# Permafrost and frozen fringe

The thermal exchange described in {doc}`thermal-structure` describes the energy balance at the bed of a glacier and controls whether the bed is frozen or thawed. In the {doc}`basal-motion` and the {doc}`../cryosphere/erosion` chapters, we learned how the energy balance at the bed controls the basal boundary condition. This chapter examines the partially frozen sediment at the base of an ice sheet and the permafrost that characterizes the ground beyond it. The same heat conduction governs both, but a new piece of physics enters, the freezing of water in the pores of fine sediment, which does not happen all at once at 0 °C. That gradual freezing builds the frozen fringe that entrains the debris a glacier carries, it decides whether subglacial till is rigid or deforming, and it is the basis of the permafrost that underlies a quarter of the Northern Hemisphere's land. The terrestrial side of the subject is treated comprehensively by {cite}`french2017`, and the premelting and frost-heave physics it rests on by {cite}`dash2006`.

## Freezing in porous sediment

Water held in the narrow pores of a fine sediment does not freeze at 0 °C. The premelting introduced in {doc}`../foundations/ice-structure`, the thin film of liquid that survives against a solid surface below the bulk melting point, keeps a fraction of the pore water unfrozen to temperatures well below freezing, and the finer the pores the larger that fraction. The depression of the freezing point follows the same Clausius–Clapeyron physics as the pressure melting of {doc}`thermal-structure`, applied now to the curvature of the ice–water interface threading a granular pack rather than to the pressure of overlying ice. The consequence is that frozen ground is never wholly solid; it carries an unfrozen water content that rises smoothly as the temperature approaches the melting point, and it is this residual liquid, mobile along premelted films, that makes the rest of this chapter possible. A clean sand freezes almost completely a fraction of a degree below zero, while a clay can hold tens of percent of its water liquid at several degrees of frost.

The quantitative statement is the generalized Clapeyron equation. Where ice and water coexist in a pore at a temperature $T$ below the bulk melting point $T_m$, equilibrium fixes the difference between the pressures in the two phases,

$$
p_i - p_w = \rho_i L_f\,\frac{T_m - T}{T_m},
$$

where $p_i$ is the pressure in the pore ice, $p_w$ the pressure in the adjacent unfrozen water, $\rho_i$ the density of ice, $L_f$ the latent heat of fusion, and $T_m-T$ the undercooling below the bulk melting point. The relation says that ice held below $T_m$ must stand at a higher pressure than the water it coexists with, by an amount that grows in proportion to the undercooling.

```{admonition} Derivation
:class: dropdown
The two phases are in equilibrium when their chemical potentials, the Gibbs energies per unit mass, are equal, $\mu_i(p_i,T)=\mu_w(p_w,T)$. At the bulk melting point both phases sit at a common reference pressure $p_0$ with $\mu_i=\mu_w=\mu_0$. Expand each potential to first order about that state with $d\mu = -s\,dT + v\,dp$, where $s$ is the specific entropy and $v=1/\rho$ the specific volume, writing the temperature as $T_m$ minus the undercooling,

$$
\mu_i = \mu_0 + s_i(T_m-T) + v_i(p_i-p_0),\qquad
\mu_w = \mu_0 + s_w(T_m-T) + v_w(p_w-p_0).
$$

Set them equal and take the water at the reference pressure, $p_w=p_0$,

$$
(s_i-s_w)(T_m-T) = -v_i(p_i-p_0).
$$

The entropy difference is the entropy of fusion, $s_w-s_i = L_f/T_m$, and $v_i=1/\rho_i$, so

$$
p_i-p_0 = \rho_i L_f\,\frac{T_m-T}{T_m},
$$

which is the printed relation with $p_w=p_0$.
```

Two effects set the undercooling at which ice can occupy a given pore. Across the curved ice–water interface the Young–Laplace relation makes the pressure jump $p_i-p_w=\gamma_{iw}\kappa$, with $\gamma_{iw}$ the ice–water interfacial energy and $\kappa$ the curvature the interface must take to thread the pore. Combining this with the Clapeyron relation gives the Gibbs–Thomson freezing-point depression,

$$
T_m - T = \frac{\gamma_{iw}\, T_m}{\rho_i L_f}\,\kappa,
$$

in which the undercooling needed to push ice through a constriction is proportional to the curvature it must adopt there. A cylindrical throat of radius $r$, where $\kappa\approx 2/r$, stays liquid until the temperature falls about $2\gamma_{iw}T_m/(\rho_i L_f r)$ below zero, so narrow throats hold their water unfrozen to lower temperatures, the quantitative form of the sand-versus-clay contrast. Because a real sediment holds a distribution of pore sizes, ice invades the largest pores first and the unfrozen water content $\theta_u$ falls off smoothly as the ground cools, the freezing characteristic of the soil, often fit over a wide range by a power law $\theta_u\propto(T_m-T)^{-\beta}$ {cite}`dash2006`.

## The frozen fringe

At the base of a glacier whose bed is at or near the melting point, the transition from temperate ice to frozen ground is not a surface but a layer, the frozen fringe, a few millimetres to centimetres thick in which pore ice and sediment grains coexist with premelted films of unfrozen water {cite}`rempel2008`. Within the fringe the temperature falls below the bulk melting point with height into the ice, the unfrozen water content falls with it, and the films exert a suction, the same thermomolecular force that drives frost heave in a roadbed, that draws liquid water toward the colder side. The water arriving at the freezing front freezes on, so ice accumulates within and above the fringe as segregation ice, lifting the overlying ice and incorporating sediment from below.

The cryosuction can be read straight off the Clapeyron relation. Within the fringe the pore ice is continuous with the basal ice above and carries the ice overburden, so its pressure $p_i$ is set by the load, and the water pressure beneath it follows,

$$
p_w = p_i - \rho_i L_f\,\frac{T_m - T}{T_m}.
$$

Here $p_w$ is the pore-water pressure, $p_i$ the pressure of the load-bearing pore ice, and $\rho_i L_f (T_m-T)/T_m$ the Clapeyron offset, so the water pressure falls further below the overburden the colder the ice. This depressed pressure is the cryosuction, and it pulls liquid up the temperature gradient toward the freezing front. The water travels through the unfrozen films and the still-open throats by Darcy's law,

$$
q = -\frac{k(\theta_u)}{\mu_w}\,\frac{\partial p_w}{\partial z},
$$

where $q$ is the water flux toward the front, $\mu_w$ the viscosity of water, $\partial p_w/\partial z$ the gradient of the cryosuction, and $k(\theta_u)$ the permeability of the partially frozen matrix, which collapses by orders of magnitude as pore ice chokes the throats. The permeability falling toward zero at the cold end of the fringe is what throttles the supply and fixes the depth at which the ice can accumulate.

The load on the fringe is shared among the phases, and that sharing is the poromechanics that decides where an ice lens grows. The overburden $\sigma$ pressing on a horizontal section is carried partly by the pore ice, partly by the pore water, and partly by the grain-to-grain contacts, the effective stress $\sigma'$,

$$
\sigma = \chi\,p_i + (1-\chi)\,p_w + \sigma',
$$

where $\sigma$ is the total overburden, $\chi$ the fraction of the section occupied by ice, $p_i$ and $p_w$ the ice and water pressures, and $\sigma'$ the stress carried at grain contacts. As the temperature rises toward the warm end of the fringe the ice fraction $\chi$ grows, the ice takes up more of the load, and the grain contacts carry less. A new ice lens nucleates at the depth where the effective stress falls to zero, the grains lose contact, and the load passes entirely to the ice; the temperature there, through the Clapeyron relation, sets the maximum overburden the lens can lift, the heave pressure {cite}`rempel2004,rempel2008`.

This is how a glacier picks up its tools. The debris that does the abrasion of {doc}`../cryosphere/erosion` is not, for the most part, scraped loose at a clean ice–rock contact; it is entrained through the frozen fringe, frozen into the basal ice a grain at a time as segregation ice grows, and carried englacially until it is released by melting downstream. The thickness of the debris-rich basal ice layer of many glaciers, and the concentration of sediment within it, are set by the temperature gradient across the fringe and the rate at which water can be supplied to it. The frozen fringe therefore links the thermal state of the bed directly to the erosional and depositional record, since a bed that is everywhere thawed cannot entrain by this mechanism and a bed that is everywhere frozen has no liquid to migrate.

## Frozen and thawed till beneath ice sheets

Where a glacier rests on a thick layer of unconsolidated sediment rather than on rock, the same freezing physics decides whether that till deforms. A thawed till, at the melting point with its pore water at high pressure, is weak and deforms readily, the soft deforming bed that the friction laws of {doc}`basal-motion` and the sliding-laws lab of {doc}`sliding-laws-lab` describe; a frozen till, with its pore water largely ice, is strong and holds the ice above it fast. The boundary between the two is set by the basal thermal state, the competition among geothermal flux, frictional heating, and conduction toward the cold interior that {doc}`thermal-structure` works out, and it can migrate as that balance shifts.

The migration is consequential because it regulates fast flow. Frictional heating from an ice stream's own rapid motion tends to keep its bed thawed and deforming, but if the supply of meltwater fails or the ice thins and conducts heat away faster than friction supplies it, the bed can freeze, the till stiffens, and the ice stream slows or stops. The stagnation of Kamb Ice Stream in West Antarctica a century or two ago is interpreted as exactly this, a thermally driven shutdown in which the bed froze beneath a once-fast stream, and the resulting frozen-thawed mosaic across the bed of an ice sheet is one of the harder boundary conditions to specify in the prognostic models of {doc}`../modeling/prognostic-problem`. A frozen patch is not merely a slow patch; it is a sticky spot that anchors the flow and concentrates stress on its margins.

## Permafrost beyond the ice

Beyond the glacier the same frozen ground stands on its own as permafrost, defined thermally as ground that stays at or below 0 °C for at least two consecutive years, the conduction physics of {doc}`thermal-structure` with the glacier removed and the soil left behind. The annual surface temperature cycle penetrates downward as a damped, lagged wave that dies out within fifteen to twenty metres, the depth of zero annual amplitude, below which the temperature follows the geothermal gradient back toward the melting point.

```{figure} ../cryosphere/figures/permafrost-trumpet.png
:name: fig-permafrost-trumpet
:width: 85%

The trumpet diagram of ground temperature. The seasonal swing at the surface, here $\pm15$ °C about a mean of $-10$ °C, is damped and lagged with depth and dies out by the depth of zero annual amplitude near 15 m. The active layer is the thin zone whose summer maximum rises above 0 °C; below it the permafrost extends to its base near 300 m, where the geothermal gradient carries the mean profile back to the melting point {cite}`french2017`.
```
% Spec: trumpet diagram of ground temperature, mean surface T = -10 C, seasonal amplitude 15 C,
% geothermal gradient 1 C per 30 m; winter/summer envelopes converging at depth of zero annual
% amplitude; mark active layer, permafrost top, permafrost base near 300 m; cite french2017.

The architecture reads off the trumpet diagram of the seasonal temperature envelope. The *active layer* is the zone where the summer maximum rises above 0 °C, the half metre to few metres that thaws each year and the only layer where water moves freely and plants root. The *base of permafrost* lies where the geothermal gradient carries the mean profile back to the melting point, near 300 m beneath a surface averaging −10 °C and deeper still in the coldest ground of Siberia and the Canadian Arctic. Bodies of unfrozen ground called taliks open beneath lakes that do not freeze to their beds, and toward the warm margin of the permafrost zone the same arithmetic thins the frozen ground into the patchy classes of discontinuous and sporadic permafrost.

The seasonal freezing and thawing of the active layer is a moving-boundary problem of the kind that arises wherever ice changes phase. At the freezing front the latent heat given up as water turns to ice must be carried away by conduction, the Stefan condition,

$$
\rho_w L_f \theta\,\frac{dX}{dt} = \left.k_f\frac{\partial T}{\partial z}\right|_{\mathrm{frozen}} - \left.k_t\frac{\partial T}{\partial z}\right|_{\mathrm{thawed}},
$$

where $X(t)$ is the depth of the front, $\theta$ the volumetric water content that changes phase, $\rho_w$ the density of water, $L_f$ the latent heat of fusion, and $k_f$ and $k_t$ the conductivities of the frozen ground above the front and the thawed ground below it. The left side is the latent heat released per unit area as the front advances, and the right side is the difference between the heat conducted away into the frozen ground and the heat arriving from the thawed ground. Balancing the two makes the front penetrate as the square root of time, $X\propto\sqrt{t}$, the same diffusive law that governs the temperature wave itself.

Because the pore water freezes over a range of temperature rather than all at once, it is usually more convenient to fold the latent heat into the heat equation as an apparent heat capacity. Writing the latent heat released as the unfrozen content $\theta_u(T)$ changes with temperature, the conduction equation of {doc}`thermal-structure` becomes

$$
\rho\left(c + L_f\,\frac{\partial \theta_u}{\partial T}\right)\frac{\partial T}{\partial t} = \frac{\partial}{\partial z}\!\left(k\,\frac{\partial T}{\partial z}\right),
$$

where $\rho$ is the bulk density, $c$ the specific heat of the mineral-plus-unfrozen-water solid, $k$ the conductivity, and the bracketed sum is the apparent heat capacity. The added term $L_f\,\partial\theta_u/\partial T$ is large wherever water is actively freezing, so a front passing through ice-rich ground advances slowly and the temperature there lingers near the melting point, the zero curtain seen in autumn permafrost records as the active layer surrenders its latent heat before it can cool any further.

The upper hundred metres of a permafrost borehole is a recording thermometer, since a change in surface temperature diffuses downward slowly and leaves the smoothed history of past climate curved into the profile. Boreholes across northern Alaska bend warm in their upper 100 to 150 m, the diffused signature of about a century of Arctic warming registered in the ground before instrumental records reached the region {cite}`lachenbruch1986`, the same borehole paleothermometry that, applied through an ice sheet, returns in {doc}`../climate/paleoclimate`.

```{figure} ../cryosphere/figures/alaska-permafrost-warming.jpeg
:name: fig-alaska-permafrost
:width: 60%

The recording thermometer read out {cite}`lachenbruch1986`. Temperature profiles from four boreholes across northern Alaska, with permafrost bases from 284 to about 600 m. Each profile bends warm in its upper 100–150 m, away from the straight geothermal gradient below, the diffused signature of about a century of surface warming.
```

Permafrost matters to climate out of proportion to its obscurity because of what it stores. Northern permafrost soils hold on the order of 1,000 Gt of organic carbon, more than the atmosphere now contains, accumulated because frozen ground is where dead plant matter goes to not decompose {cite}`schuur2015`. Thaw restarts the decomposition, releasing carbon dioxide and methane and warming the climate that deepens the thaw, a slow positive feedback with the same logical shape as the ice–albedo feedback of {doc}`../cryosphere/sea-ice`. The frozen ground that this chapter began with at the bed of an ice sheet is, in this wider setting, both a landscape and a reservoir whose stability is now in question.
