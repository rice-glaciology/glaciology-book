# The thermal structure of glaciers

The temperature of ice is not a passing detail. Through the rate factor of {doc}`../ice_flow/ice-rheology`, temperature controls how readily ice deforms, and through the pressure-melting point it controls whether the bed is frozen or thawed and therefore whether the ice can slide. Predicting how a glacier flows requires knowing its temperature, and the temperature in turn depends on the flow. The thermal structure of glaciers is treated in Chapter 9 of {cite}`cuffey2010`.

## The heat budget

The temperature of a parcel of ice is set by a competition among several processes. Heat is conducted through the ice from warmer to colder regions. The flowing ice carries its temperature with it, a transport called advection, so cold surface ice can be drawn down into the interior and warm basal ice can be carried toward an outlet. Heat enters from the bed as a geothermal flux from the Earth below, and it is generated within the ice itself wherever the ice deforms, since the work done against viscous resistance is dissipated as heat. Near the surface, the refreezing of meltwater releases latent heat that can warm the firn substantially.

Collecting these terms gives the heat equation for ice,

$$
\rho c \left(\frac{\partial T}{\partial t} + \bu\cdot\nabla T\right) = \nabla\!\cdot\!(k\,\nabla T) + \Phi,
$$

where $\rho$ is density, $c$ is the specific heat capacity, $k$ is the thermal conductivity, and $\Phi$ is the rate of heating by internal deformation. The term with $\bu$ is the advection of heat by the flow, and the divergence term is conduction.

## Where the coefficients come from

The two material properties in this equation, the specific heat and the thermal conductivity, are not arbitrary constants. They are set by the lattice vibrations of {doc}`../foundations/lattice-dynamics`, and their values and temperature dependence shape the thermal structure in ways worth keeping in view. The specific heat is large because water molecules are light, about $2.1\ \mathrm{kJ\,kg^{-1}\,K^{-1}}$ near the melting point, and it decreases steadily as the ice cools and the stiffer vibrational modes freeze out, falling by roughly a third in the coldest polar ice. The conductivity behaves oppositely. Because heat is carried by phonons that are scattered ever more frequently as the temperature rises, the conductivity grows as the ice cools, from about $2.1\ \mathrm{W\,m^{-1}\,K^{-1}}$ near melting to half again as much in cold interior ice. Cold ice therefore both stores less heat per degree and conducts it better than warm ice.

What the flow actually feels is the combination of the two, the thermal diffusivity $\kappa_T = k/\rho c$, which measures how fast a temperature signal spreads by conduction and is about $1.1\times10^{-6}\ \mathrm{m^2\,s^{-1}}$ for cold ice. The distance a signal diffuses grows only as the square root of time, so over a single year conduction reaches just a few meters into the ice. This is why the seasonal swing of surface temperature is erased within the upper ten to twenty meters, why the temperature at that depth records the mean annual climate, and why advection by the flow, not conduction, carries cold surface ice deep into the interior of a fast-moving ice sheet. The smallness of the diffusivity is the reason the advection term in the heat equation so often dominates.

## Temperature profiles and the bed

In a slow-moving ice sheet far from the margin, the temperature is lowest at the surface, set by the cold air, and generally increases with depth as the geothermal flux warms the ice from below and deformation adds heat near the bed. Whether the base reaches the melting point depends on the surface temperature, the ice thickness, the geothermal flux, and the rate of deformational heating. This question matters because a frozen bed holds the ice fast, while a bed at the melting point allows sliding and the fast flow that comes with it.

The melting point of ice is not fixed. It decreases as pressure increases, by about 0.07 to 0.1 degrees Celsius for every hundred metres of overlying ice, so the base of a three-kilometre-thick ice sheet can be at the melting point even though its temperature is below zero degrees Celsius. This dependence is a direct consequence of the open crystal structure of {doc}`../foundations/ice-structure`: because ice is less dense than the water it melts to, pressure favors the denser liquid, and the Clausius-Clapeyron relation turns that volume change into a falling melting point. The same molecular fact that makes ice float lowers the melting point at the bed. Ice that is everywhere below the melting point is called cold, ice that is at the melting point throughout is called temperate, and ice that contains both is called polythermal. Many of the world's mountain glaciers are temperate or polythermal, while the interiors of the polar ice sheets are cold with beds that may be frozen or thawed depending on local conditions.

## Coupling to the flow

Because the rate factor rises steeply with temperature, the thermal structure and the flow are coupled. Warm ice flows faster, faster flow generates more heat, and that heat can warm the ice further and raise the rate of flow again. This feedback, known as thermomechanical coupling, can localize fast flow into streams and can produce slow oscillations in some idealized models. It is also the reason that any serious ice-sheet model must solve for temperature alongside velocity. In the modeling labs we add this coupling to icepack by making the fluidity a function of a computed temperature field rather than a fixed constant. Greve and Blatter give a thorough mathematical treatment {cite}`greve2009`.
