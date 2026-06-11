# Subglacial hydrology

The friction laws of {doc}`basal-motion` all turned on the effective pressure $N=p_i-p_w$, the difference between the weight of the ice and the pressure of the water beneath it. That single quantity decides how fast a glacier slides, and it is set by the subglacial drainage system: how much water reaches the bed, and how efficiently it is carried away. This chapter develops the hydrology that supplies $N$. It also stands on its own, because the water system produces some of the most dramatic behaviour in glaciology, from the seasonal speed-up of the Greenland margin to the catastrophic floods called jökulhlaups. The treatment follows the lectures of {cite}`hewitt_karthaus`, with the foundational results of {cite}`shreve1972,rothlisberger1972,nye1976`.

## Where the water comes from

Water reaches the bed of a glacier from two sources. The first is melting at the bed itself, driven by the geothermal flux from below, by frictional heating where the ice slides, and by the conduction of heat carried down from the surface. The thermal calculation of {doc}`thermal-structure` decides whether the bed is frozen, at the melting point and producing water, or refreezing. Basal melt rates are small, of order ten millimetres a year, but integrated over an ice sheet they are substantial, around 65 gigatonnes a year for grounded Antarctic ice and 20 for Greenland. The second source is melting at the surface, which is far larger where it operates: tens of centimetres a year in Antarctica but of order a metre a year over the Greenland ablation zone, totalling roughly 150 and 400 gigatonnes a year respectively. Surface meltwater collects in supraglacial streams and lakes and reaches the bed through moulins and water-filled crevasses that can hydrofracture to the base. The contrast matters, because surface melt is strongly seasonal and delivered in concentrated pulses, while basal melt is steady, and the two force the drainage system very differently.

## Pressurised water and the direction of flow

Water at the bed is under pressure, squeezed between the ice and the rock, so it does not simply run downhill. Its flow is governed by the gradient of the hydraulic potential, the sum of the gravitational potential energy and the water pressure,

$$
\phi = \rho_w g Z_b + p_w,
$$

where $Z_b$ is the bed elevation. Writing the water pressure in terms of the effective pressure, $p_w = p_i - N = \rho_i g (Z_s - Z_b) - N$, with $Z_s$ the surface elevation, gives

$$
\phi = \rho_w g Z_b + \rho_i g (Z_s - Z_b) - N .
$$

Water flows down the gradient of $\phi$. Taking the gradient and noting that variations in $N$ are usually small compared with those in the elevations,

$$
-\nabla\phi = \Psi + \nabla N \approx \Psi,
\qquad
\Psi = -\rho_i g\,\nabla Z_s - (\rho_w-\rho_i)\,g\,\nabla Z_b ,
$$

the Shreve potential gradient. The two terms compare the pull of the surface slope with that of the bed slope, and their coefficients differ by the factor $\rho_i/(\rho_w-\rho_i)\approx 11$. The surface slope is therefore about eleven times more effective than the bed slope at driving subglacial water. The consequence is one of the most useful facts in the subject: subglacial water flows down the ice-surface slope, not the bed slope, so it can be routed uphill over bedrock ridges, and the catchments that feed subglacial lakes and outlets can be predicted from surface topography alone.

## A spectrum of drainage systems

How the water is carried, and what effective pressure results, depends on the form the drainage takes, and the forms span a spectrum. At one end the water is distributed across the bed, in a thin film, in cavities in the lee of bumps, or in the pore space of a sediment sheet. At the other end it is concentrated into a few large conduits, either channels melted up into the ice or canals incised down into the sediment. The distributed systems are inefficient, carrying water slowly at high pressure and therefore low effective pressure, while the channelized systems are efficient, carrying water quickly at low pressure and high effective pressure. Broadly, the more water there is to carry, the more the system tends toward channels. The seasonal evolution of a glacier from a distributed winter system to a channelized summer one, and the speed changes that come with it, is a journey along this spectrum.

## The instability of a water film

Why the water organizes itself this way can be seen from the simplest distributed system, a uniform film of thickness $h$ between ice and bed. Laminar flow through the film carries a flux

$$
q = -\frac{h^3}{12\,\eta_w}\,\nabla\phi ,
$$

the Poiseuille law, with $\eta_w$ the viscosity of water. As the water flows it dissipates energy and melts the ice roof above it. A patch of film that is slightly thicker than its surroundings carries more flux, dissipates more heat, melts its roof faster, and grows thicker still. The uniform film is therefore unstable, and the instability drives the water to concentrate into a few localized conduits. The endpoint of the instability depends on what the conduit melts or erodes into, which is what distinguishes the channel and cavity systems below.

## Röthlisberger channels

A channel melted upward into the ice is held open by the heat dissipated in the flowing water and squeezed shut by the creep of the surrounding ice under the effective pressure. {cite}`rothlisberger1972` and {cite}`nye1976` wrote the balance as a set of equations for the channel cross-section $S$ and the discharge $Q$: conservation of mass and of the channel wall,

$$
\frac{\partial S}{\partial t} = \frac{m}{\rho_i} - \tilde A\,S\,N^{\,n},
$$

where $m$ is the melt rate of the wall and the second term is creep closure; a turbulent flow relation,

$$
Q = K_c\,S^{4/3}\left(\Psi + \frac{\partial N}{\partial x}\right)^{1/2};
$$

and local conservation of energy, the heat that melts the wall coming from the potential energy released by the flow,

$$
m L = Q\left(\Psi + \frac{\partial N}{\partial x}\right).
$$

A steady state follows by setting the time derivative to zero and, for a channel along the flow, neglecting $\partial N/\partial x$ against $\Psi$. The energy balance gives $m=Q\Psi/L$, the wall balance becomes $\tilde A S N^n = m/\rho_i = Q\Psi/(\rho_i L)$, and the flow relation gives $S=(Q/K_c\Psi^{1/2})^{3/4}$. Eliminating $S$,

$$
N \approx \left(\frac{K_c^{3/4}}{\rho_i L\,\tilde A}\right)^{1/n}\Psi^{\,11/8n}\,Q^{\,1/4n}.
$$

The exponent of the discharge is positive, so the effective pressure increases with discharge. A channel carrying more water runs at lower water pressure. This is the signature of an efficient, channelized system, and it has a self-organizing consequence: because a larger channel sits at lower pressure, it draws water from its smaller neighbours, which collapse. The drainage collects into a few arborescent trunk channels, exactly the opposite of the distributed film it grew from.

## Jökulhlaups

A celebrated success of the channel theory is the subglacial flood. When a lake is dammed by ice, water leaks into a channel through the dam; the flow melts the channel walls and enlarges them, which lets more water through, which melts the walls faster. Coupling the channel-evolution equation,

$$
\frac{\partial S}{\partial t} = \frac{S^{4/3}\Psi^{3/2}}{\rho_i L} - \tilde A S N^{\,n},
$$

to an equation for the draining lake,

$$
\frac{A_L}{\rho_w g}\frac{\partial N}{\partial t} = m_L - Q,
$$

reproduces the characteristic flood hydrograph, a slow exponential rise to a sharp peak followed by an abrupt collapse when the lake empties and the channel creeps shut. The model of {cite}`nye1976`, refined by later workers, matches recorded jökulhlaup discharges from Iceland closely.

The clip below shows what the sharp end of that hydrograph looks like from the proglacial zone, a glacial outburst flood in full flow.

```{raw} html
<video controls width="85%" preload="metadata" style="max-width: 700px;">
  <source src="../../_static/videos/outburst-flood-usgs.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>A glacial outburst flood. Video courtesy of the U.S. Geological Survey.</em></p>
```

## Linked cavities and canals

The channel theory assumes melt opening, which requires the strong potential gradients of steep glaciers. Under the gentle surface slopes of an ice-sheet interior the water moves too slowly to melt open a channel, and the distributed system survives. Two distributed systems are important. Over hard beds the water occupies cavities in the lee of bumps, linked into a network {cite}`walder1986,kamb1987`. The cavities are opened not by melting but by sliding, the ice being dragged off the downstream side of each bump at a rate proportional to the sliding speed $U_b$ and bump height $h_r$, and closed by creep,

$$
\frac{\partial S}{\partial t} = U_b h_r - \tilde A\,S\,N^{\,n},
\qquad
Q = -K\,S^{\alpha}\,\nabla\phi .
$$

In steady state $S=U_b h_r/(\tilde A N^n)$ and $S=(Q/K\Psi)^{1/\alpha}$, and eliminating $S$,

$$
N \approx \left(\frac{U_b h_r\,K^{1/\alpha}\Psi^{1/\alpha}}{\tilde A}\right)^{1/n}\,Q^{-1/\alpha n}.
$$

Now the exponent of discharge is negative: the effective pressure decreases with discharge. More water raises the water pressure rather than lowering it. This is the opposite of the channel result, and it is what makes the cavity system inefficient and prone to fast sliding when meltwater is delivered faster than it can escape. The two systems are not separate. A cavity network becomes unstable and collapses into channels when the discharge grows large or the sliding slows, and a channel relaxes back into cavities when the discharge drops or the sliding speeds up, so a glacier switches between regimes through the season.

Over soft beds the sediment has too low a hydraulic conductivity to carry much water through its pores, so the water again flows at the interface, either in a patchy film or in canals incised into the till {cite}`walder1994`. A canal is widened by erosion of its sediment floor and by melt, and closed by creep, and its steady state gives an effective pressure that, like the cavities, decreases with discharge, $N\propto\Psi^{-1/3}Q^{-1/3}$. Whether the bed drains through ice-roofed channels or sediment-floored canals turns on whether the effective pressure exceeds a threshold of around 0.8 megapascals, with canals, and the distributed low-pressure state they imply, favoured under the small potential gradients of ice-sheet interiors.

## Why hydrology controls flow

The thread running through this chapter is the sign of the relation between effective pressure and discharge. In channels the effective pressure rises with the water supply, draining the bed and strengthening it; in cavities and canals it falls, flooding the bed and weakening it. A glacier that receives a sudden pulse of surface melt before its channels have developed responds with the cavity behaviour, the water pressure climbs, the effective pressure falls, and through the friction law of {doc}`basal-motion` the ice accelerates. As the melt season proceeds, channels grow, the bed drains, the effective pressure recovers, and the ice slows even as melting continues. This is the explanation for the observed spring speed-up and late-summer slow-down of land-terminating Greenland glaciers, and it is why a faithful prognostic model of ice flow must carry an evolving water system alongside the ice. The coupling of hydrology to sliding, and its role in the response of the ice sheets to a warming climate, returns with the prognostic modelling. It returns sooner than that too, because the water-pressure fluctuations this chapter explained are the hammer that {doc}`../cryosphere/erosion` will show quarrying bedrock, so the chain that began with heat at the bed runs onward from sliding and drainage into the shaping of the landscape itself.
