# Forcing glaciers with climate

## Ice sheets are climate

The popular framing — climate changes, glaciers
respond — makes ice sound passive, a thermometer hanging in the atmosphere. The reality
is more interesting. On timescales beyond a few thousand years, ice sheets are not the
thermometer; they are part of the temperature. They reflect sunlight, elevate their own
surface into thinner and colder air, drive the freshwater fluxes that pace the ocean
overturning circulation, and lock up enough water to shift sea level by a hundred meters
and thereby change the shape of every coastline on Earth. An ice sheet is both
the recorder of past climate — the subject of {doc}`paleoclimate` — and the slowest
dynamical component of the climate system itself, carrying its own integrated history, its own
instabilities, and its own committed trajectories that no weather forecast could reveal.

The one-stage kinematic model of {doc}`glacier-variations` gives the cleanest
statement of that memory. A glacier of length $L$ in a perturbed climate obeys

$$
\frac{dL'}{dt} = -\frac{L'}{\tau} + F'(t),
$$

```{admonition} Derivation
:class: dropdown

The red power spectrum quoted below follows from this equation by Fourier transform. Write the length anomaly and the forcing as superpositions of harmonics, $L'(t) = \int \hat L(\omega)\,e^{i\omega t}\,d\omega$ and $F'(t) = \int \hat F(\omega)\,e^{i\omega t}\,d\omega$. A time derivative becomes multiplication by $i\omega$, so the equation transforms term by term into

$$
i\omega\,\hat L(\omega) = -\frac{\hat L(\omega)}{\tau} + \hat F(\omega),
\qquad
\hat L(\omega) = \frac{\hat F(\omega)}{i\omega + \tau^{-1}}.
$$

The power spectrum is the squared modulus of the transfer function times the forcing spectrum. Using $|i\omega + \tau^{-1}|^2 = \omega^2 + \tau^{-2}$,

$$
S_{LL}(\omega) = |\hat L(\omega)|^2 = \frac{|\hat F(\omega)|^2}{\omega^2 + \tau^{-2}}
= \frac{S_{FF}(\omega)}{\omega^2 + \tau^{-2}}.
$$

For white-noise forcing $S_{FF}$ is flat. At low frequencies, $\omega \ll \tau^{-1}$, the denominator is approximately $\tau^{-2}$ and $S_{LL} \approx \tau^2\,S_{FF}$, the constant low-frequency plateau whose height grows as $\tau^2$. At high frequencies, $\omega \gg \tau^{-1}$, the denominator is approximately $\omega^2$ and $S_{LL} \approx S_{FF}/\omega^2$, the $\omega^{-2}$ red tail. The corner separating the two regimes sits at $\omega = \tau^{-1}$, so the longer the response time the lower the corner frequency and the more of the spectrum is lifted into the plateau. Integrating $S_{LL}$ over all frequencies gives the variance of $L'$, which scales as $\tau\,\sigma_F^2$; a longer response time stores more variance, the formal content of the flywheel analogy.
```

where $\tau = H/\dot a_0$ is the Jóhannesson–Raymond–Waddington response time
{cite}`johannesson1989` and $F'(t)$ is a forcing proportional to the mass-balance
perturbation. Now suppose the climate is not changing at all, but the mass balance
varies randomly from year to year, white noise with variance $\sigma_F^2$.
The length anomaly $L'$ is then an Ornstein–Uhlenbeck process, and its variance
accumulates at low frequencies until the response time cuts it off. Formally, the
power spectrum of $L'$ is red: $S_{LL}(\omega) = S_{FF}(\omega)/(\omega^2 + \tau^{-2})$,
proportional to $\tau^2 \sigma_F^2$ at frequencies $\omega \ll \tau^{-1}$ and falling
off as $\omega^{-2}$ above that corner. A glacier integrates interannual mass-balance
noise into slow, persistent length excursions the same way a heavy flywheel integrates
a sputtering engine into smooth rotation — the larger the flywheel (the longer $\tau$),
the smoother and the larger the stored energy. This is the Hasselmann integration
argument applied to glacier length {cite}`hasselmann1976`, and its consequence is concrete and uncomfortable:
even a glacier in a perfectly stationary climate will wander its terminus by a kilometer
or more on multi-decade timescales. A retreating terminus is not automatically a retreating
climate. The null hypothesis every observed retreat must beat is not zero variability; it
is the red-noise wandering that the climate's own interannual noise produces after passing
through the integrating glacier.

For mountain glaciers with $\tau$ of decades this means a few kilometers of excursion are
climatically innocent. For the great ice sheets, where $\tau$ can reach millennia, the
implied natural variability is vast — and the ocean-forced marine glaciers, as we will see
below, produce an even slower and larger integration effect. The present shape of the West
Antarctic ice sheet still reflects conditions at the Last Glacial Maximum.
Reading a glacier's terminus position and inferring climate from it requires knowing the
filter, and most of this book is about building and using that filter correctly.

## From simple glaciers to marine ice sheets

The one-stage reservoir model is the right starting point for small mountain glaciers, but
it eventually runs out of physics. For the large marine-terminating systems — the outlet
glaciers of Greenland and the ice streams of West Antarctica — the controlling boundary is
not a thin terminus wedge but a grounding line, and the dynamics feeding that grounding
line are themselves a slow process with their own timescale. The kinematic machine of
{doc}`glacier-variations` can still be run, but it needs a second stage.

That second stage is the two-stage model of Robel, Roe, and Haseloff {cite}`robel2018`, derived in {doc}`glacier-variations`, which tracks the mean interior thickness and the grounding-line position as coupled reservoirs, fed by the interior flux and drained by the steeply thickness-dependent flux across the grounding line. Three of its results bear directly on this chapter's argument. The linearized system has a fast grounding-zone timescale of decades to centuries and a slow interior timescale of millennia, so a marine ice stream responds to forcing quickly in part and completely only after a very long time. Its steady states are stable or unstable according to the sign of a single number set by the bed slope at the grounding line, which makes the marine ice-sheet instability of {doc}`../cryosphere/ice-sheets` a calculable property of the mean state. And driven by the broadband variability of ocean temperature, the system acts as the marine extension of the Hasselmann argument above, integrating noise into grounding-line excursions that are large, slow, and persistent, so that a decade of observed retreat cannot by itself distinguish forcing from natural variability.

% lab (stochastic, icepack): two-stage Robel model driven by white-noise ocean forcing;
% estimate natural grounding-line variability; compare fast and slow eigenmode trajectories

## The surface mass balance function

Everything in {doc}`../modeling/prognostic-problem` is waiting on one piece of
information: the surface mass balance $\dot a(x,t)$ as a function of position and time.
The conservation law of {doc}`../ice_flow/mass-balance` and the flow law of
{doc}`../ice_flow/shallow-ice` are ready; what the prognostic model cannot yet do is
answer the climate. Climate models and weather station networks speak in temperature and
precipitation, in humidity and wind and incoming radiation. They do not speak in meters
of ice-equivalent per year. The sections that follow build the translation layer between
those two languages.

The translation is imperfect, and being honest about its imperfections matters
enormously for ice-sheet projections. Both the reduced two-stage model above and a
full prognostic experiment consume the same two ingredients — the surface mass balance
$\dot a(x,t)$ and an ocean thermal forcing — and the uncertainty in a century-scale
forecast lives mostly in those forcings, not in the ice flow law itself. The basal
friction adds its own uncertainty, as argued in {doc}`../thermomechanics/basal-motion`,
but getting $\dot a(x,t)$ right is where the science is hardest, and where the honest
modeler must be most explicit about what has been approximated.

There is also a structural limit on prognostic experiments that motivates the reduced
models in the first place. A full ice-sheet model is expensive: the diffusive time-step
constraint from the shallow-ice equations pushes computational cost up sharply as
resolution improves, initialization from an imperfect present-day state introduces a
drift that grows over centuries, and the forcing uncertainty compounds with every decade
of integration. Direct prognostic experiments are therefore practically limited to runs
of a hundred to a thousand years. For variability on the multi-centennial and millennial
timescales where the two-stage model predicts the largest signals, reduced models are not
an approximation of convenience but a genuine scientific tool.

## Accumulation

The accumulation part of $\dot a$ is governed by two questions: how much precipitation
falls, and how much of it is solid rather than liquid? Where all precipitation is snow,
the conversion is trivial and the mass balance gains whatever the atmosphere delivers.
Where the atmosphere straddles the freezing point seasonally, the partitioning is the
first nontrivial step.

The simplest partition rule says precipitation falls as snow whenever the air temperature
at the surface is below some threshold, typically $0\,^\circ\mathrm{C}$ or a slightly
positive value that accounts for the wet-bulb depression. In practice a smoothed
transition works better than a sharp cutoff, and a common choice is a linear ramp between
two temperature thresholds, say $-1\,^\circ\mathrm{C}$ and $+2\,^\circ\mathrm{C}$,
with the solid fraction falling linearly from one to zero across the interval. The exact
thresholds are tunable, and different catchments prefer different values.

Bringing a coarse climate field, from a global model or a reanalysis, down to the glacier
surface requires two corrections. The first is a lapse rate. Temperature decreases with
elevation at roughly $6$ to $9\,^\circ\mathrm{C}$ per kilometer in the free troposphere,
and a standard environmental lapse rate of $6.5\,^\circ\mathrm{C}$ per kilometer is often
used to adjust a valley-floor temperature to the elevation of the glacier surface. The
lapse rate matters not only for the temperature-dependent melt discussed below but also
for the phase partition, since a few hundred meters of elevation can swing the accumulation
from all-rain to all-snow.

The second correction is orographic enhancement. When moist air encounters a mountain
barrier, uplift cools it and wrings out precipitation on the windward slopes, leaving the
leeward side in a rain shadow. Precipitation on a major ice field can be two to five times
what a lowland station twenty kilometers away records {cite}`cuffey2010`, and any
mass-balance model that ignores this will be embarrassingly wrong on the accumulation side.
For small mountain glaciers a simple linear scaling with the local elevation anomaly often
captures the main effect. For large ice sheets the orographic field must come from an
atmospheric model explicitly resolving the barrier.

## Temperature-index melt models

Ablation is harder, and two strategies, one cheap and one honest, have divided the field.

The cheap strategy is the positive-degree-day model. Its central insight is that the
temperature of the air near the glacier surface is a surprisingly good proxy for the
entire surface energy budget, because most of the terms in that budget correlate with
temperature. Longwave emission from the atmosphere, the flux of sensible heat to the
surface, and the vapor pressure driving turbulent exchange all rise together with air
temperature. Rather than computing each term explicitly, the positive-degree-day method
integrates the temperature excess above freezing and multiplies by a melt factor,

$$
M = \mathrm{DDF} \times \mathrm{PDD},
$$

```{admonition} Derivation
:class: dropdown

This relation is an empirical regression rather than a result derived from first principles, but its form has a physical rationale worth stating. Melt at a surface already at the melting point is set by the energy surplus $Q_M$ of the surface energy balance treated in {doc}`../thermomechanics/surface-energy-balance`, converted to mass through the latent heat of fusion $L_f$, $M = Q_M/(\rho_w L_f)$. The temperature-index method rests on the observation that several of the dominant terms in $Q_M$ scale roughly linearly with the near-surface air temperature $T$. Incoming longwave radiation rises with atmospheric temperature, the sensible-heat flux is proportional to the air–surface temperature difference, and the saturation vapour pressure that drives the turbulent latent-heat flux climbs with temperature as well. Writing the net melt energy as approximately proportional to the temperature excess above freezing, $Q_M \approx c\,\max(T,0)$ with $c$ an effective heat-transfer coefficient, and integrating over the ablation season,

$$
M = \frac{1}{\rho_w L_f}\int Q_M\,dt \approx \frac{c}{\rho_w L_f}\int \max(T,0)\,dt
= \mathrm{DDF}\times\mathrm{PDD},
$$

where the time integral of the positive temperature excess is by definition the positive-degree-day sum $\mathrm{PDD}$ and the lumped constant $\mathrm{DDF} = c/(\rho_w L_f)$ is the degree-day factor. The factor is not computed from $c$ but calibrated against measured melt, which is why it absorbs the surface-specific physics, most importantly the albedo, and takes different values for snow and bare ice {cite}`cuffey2010`. The approximation fails wherever the energy-balance terms stop covarying with temperature, the cases catalogued in the energy-balance section below.
```

where $M$ is the total melt in water equivalent, $\mathrm{DDF}$ is the degree-day factor
in $\mathrm{mm\,w.e.\,d^{-1}\,{}^\circ C^{-1}}$, and PDD is the sum of positive daily
mean temperatures in $\mathrm{{}^\circ C\cdot d}$ over the ablation season. The
degree-day factor is empirically calibrated and differs substantially between snow and ice.
For snow, typical values fall in the range $3$–$5\ \mathrm{mm\,w.e.\,d^{-1}\,{}^\circ C^{-1}}$;
for bare glacier ice the values are roughly twice as large, around
$6$–$10\ \mathrm{mm\,w.e.\,d^{-1}\,{}^\circ C^{-1}}$ {cite}`cuffey2010`. The contrast
is almost entirely an albedo effect. Fresh snow reflects seventy to ninety percent of
incoming shortwave radiation, leaving very little to drive melt; bare ice, blue-grey and
contaminated with dust, reflects only twenty to forty percent and absorbs the rest.
The albedo differences underlying the DDF contrast are the same optical physics treated
in {doc}`../foundations/optical-properties`, and they are what makes the snow-to-ice
transition mid-season such an important threshold.

The model also captures, at least crudely, the **elevation feedback** that is one of the
more consequential amplifiers in ice-sheet dynamics. Thinning lowers the glacier surface
into warmer air. The warmer air increases melt, which causes further thinning, which lowers
the surface further still. This is a positive feedback that, once triggered on a marine ice
sheet resting on a retrograde bed, has the same flavor as the marine ice-sheet instability
discussed in {doc}`../cryosphere/instabilities`: a committed response that exceeds the
initial perturbation. In a positive-degree-day framework the feedback enters naturally
through the lapse-rate correction, since the same temperature field applied at a lower
elevation returns a higher temperature and therefore more melt.

```{admonition} Why PDD integrates the noisy temperature distribution
:class: dropdown

The positive-degree-day sum is not simply the number of degrees above zero, because daily
mean temperature has day-to-day variability that is large compared with the seasonal mean.
On a day when the mean temperature is $-2\,^\circ\mathrm{C}$ the positive part of the
diurnal cycle can still melt several centimeters of snow. Reeh {cite}`reeh1991` showed that this is
handled correctly by modeling daily mean temperature as a normally distributed random
variable with standard deviation $\sigma$ around the monthly mean $T_\mathrm{m}$, and
integrating the positive part analytically,

$$
\mathrm{PDD}_\mathrm{day} = \int_0^\infty T \cdot \frac{1}{\sigma\sqrt{2\pi}}\exp\!\left[-\frac{(T - T_\mathrm{m})^2}{2\sigma^2}\right] dT
= \frac{\sigma}{\sqrt{2\pi}}\exp\!\left[-\frac{T_\mathrm{m}^2}{2\sigma^2}\right]
+ \frac{T_\mathrm{m}}{2}\left[1 + \mathrm{erf}\!\left(\frac{T_\mathrm{m}}{\sigma\sqrt{2}}\right)\right].
$$

This expression is larger than $\max(T_\mathrm{m},0)$ whenever $T_\mathrm{m}$ is negative
but within a few sigma of zero — exactly the spring and autumn shoulder seasons that
contribute most of the melt at the margins of large ice sheets. The $\sigma$-dependence
is not a nuisance to be minimized; it means that an increase in temperature variability,
even with no change in the mean, increases melt. Climate warming is accompanied by changes
in variability as well as the mean, and both enter the PDD through this expression. A
typical value for Greenland is $\sigma \approx 4.5\,^\circ\mathrm{C}$ for the summer
months, giving a non-negligible melt contribution even on days with negative mean
temperature.
```

% lab (prognostic, icepack): PDD forcing of a flowline glacier; elevation feedback; step and ramp scenarios

## Energy-balance melt models

The positive-degree-day approach earns its keep in large-scale and long-timescale
applications, but it is an approximation, and there are surfaces where it fails
qualitatively. A full accounting requires the surface energy balance, the budget
$Q_M = (1-\alpha)S_\downarrow + L_\downarrow - \varepsilon\sigma T_s^4 + H_S + H_L + Q_C$
developed in {doc}`../thermomechanics/surface-energy-balance`, whose terms are the
radiative, turbulent, and conductive fluxes meeting at the surface and whose positive
residual at a melting surface is the melt. The reason temperature-index methods work at
all is that most of these terms covary with air temperature; the reason they sometimes
fail is that not all of them do. The latent-heat flux is the usual culprit, dominating
the variability in maritime settings where warm, humid air drives melt under cloud that
suppresses the shortwave, and reversing its sign on cold, dry, sunny surfaces where the
much larger latent heat of sublimation, $2830\ \mathrm{kJ\,kg^{-1}}$ against
$334\ \mathrm{kJ\,kg^{-1}}$ for melting, lets ablation proceed by sublimation at nearly a
tenth the mass loss per unit energy.

This is exactly why temperature-index methods fail on high-altitude, cold, dry glacier
surfaces dominated by sublimation. The penitentes of the high Andes and the Atacama
plateau, mentioned in {doc}`../ice_flow/mass-balance`, form precisely because the net
radiation is enormous but the air is too cold and dry for melting; sublimation carves the
surface into a forest of ice blades. A degree-day model applied there would predict melt
that never happens. Debris-covered glaciers present a different failure mode: a thick
insulating mantle of rock fragments decouples the ice surface from the air temperature,
suppressing melt far below what the temperature record suggests and introducing a spatial
patchwork of ablation rates that no simple temperature proxy can resolve. Wind scour is
a third case, redistributing snow from exposed ridges to sheltered basins in patterns
controlled by topography rather than temperature.

For the prognostic modeling that the following labs undertake, the positive-degree-day
model is sufficient on the clean glaciers of Greenland's margins and on the ice sheets
of the last glacial maximum. The energy-balance formulation is needed for present-day
process studies, for debris-covered glaciers, and for any surface where sublimation
carries a significant fraction of the ablation budget.

## Simple parameterizations for whole-glacier experiments

For prognostic experiments where the goal is understanding how a glacier responds to a
warming climate rather than matching a particular observed record, it is useful to replace
the full spatial and temporal structure of $\dot a(x,t)$ with a simple parameterization.

The most common is the linear ELA form, which says that the mass balance is a linear
function of elevation measured from the equilibrium line altitude $z_\mathrm{ELA}$,

$$
\dot a(z) = \gamma\,(z - z_\mathrm{ELA}),
$$

where $\gamma$ is the mass-balance gradient in $\mathrm{m\,w.e.\,yr^{-1}\,m^{-1}}$ and
is typically of order $0.005$–$0.01\ \mathrm{yr^{-1}}$ for temperate mountain glaciers.
The profile is capped at some maximum accumulation rate above, because no glacier
accumulates without limit at its summit, and the cap prevents unphysical behavior in the
prognostic model at high elevation. The entire influence of climate on the glacier enters
through a single number, $z_\mathrm{ELA}$; a warming climate raises the ELA, reduces the
accumulation area, and shifts the integrated balance negative.

Climate scenarios for prognostic experiments come in three standard flavors. A step change
switches the ELA from one value to another at $t=0$ and holds it there; this is the
idealized scenario that produces the exponential response time worked out in
{doc}`glacier-variations`, and it is the right experiment for testing whether a model
recovers the correct equilibrium and responds on the correct timescale. A ramp change
raises the ELA linearly in time, mimicking a sustained warming trend; this is the
appropriate scenario for committed-retreat calculations and for asking how far behind
equilibrium the glacier falls during a century of warming. Periodic forcing overlays
a seasonal or multi-decadal cycle on the mean state, and it reveals how the glacier's
response time filters different frequencies — slow glaciers suppressing the interannual
noise and passing only centennial trends, fast maritime glaciers following the
interannual signal closely.

At the grandest scale, the Milankovitch forcing of {doc}`paleoclimate` is a periodic
scenario with periods of twenty-three thousand, forty-one thousand, and one hundred
thousand years, superimposed on continental-scale ELA shifts of hundreds of meters.
Running a prognostic ice-sheet model through even one glacial cycle requires $10^4$–$10^5$
years of integration, and the climate forcing must be simplified drastically. Temperature
is typically scaled from an ice-core record, the accumulation scaled with a
temperature-dependent parameterization, and the result fed into the mass-balance gradient
at each time step. The match between model and the paleoclimate record discussed in
{doc}`paleoclimate` is the hardest and most important test a prognostic model can pass.

% lab (prognostic, icepack): ELA step and ramp on a flowline; committed retreat; compare t_r = H/a0

## Ocean forcing

Climate forcing of the large ice sheets arrives not only from above but also from below.
The margins of Antarctica and the fast-flowing outlet glaciers of Greenland terminate in
the ocean, and warm Atlantic Water circulates at depth beneath their floating ice shelves
and at the fronts of tidewater glaciers. Where that water makes contact with ice, it melts
it. The parameterization most commonly used in large-scale models writes the basal melt
rate beneath a floating ice shelf as proportional to the thermal forcing, the temperature
excess of the ocean water above the pressure-dependent melting point at the ice-ocean
interface,

$$
\dot m_b = \Omega\,\Delta T^2,
$$

```{admonition} Derivation
:class: dropdown

The quadratic form is a scaling argument rather than an exact result, but it follows from coupling two effects that each scale linearly with the thermal forcing $\Delta T$, the temperature of the ambient ocean water above the in-situ freezing point. The melt rate at the ice base is proportional to the turbulent heat flux delivered to the interface, which in a standard three-equation parameterization is proportional to both the friction velocity $u_*$ of the boundary-layer flow and the thermal forcing,

$$
\dot m_b \propto u_*\,\Delta T.
$$

For melt-driven convection beneath a shelf the circulation is not externally imposed but generated by the buoyancy of the meltwater itself. A warmer ocean melts faster, the fresher, lighter plume ascends the shelf base more vigorously, and the boundary-layer velocity strengthens. To leading order the buoyancy forcing of the plume is proportional to the melt rate, which is itself proportional to $\Delta T$, so the velocity scale inherits a linear dependence, $u_* \propto \Delta T$. Substituting,

$$
\dot m_b \propto \Delta T \cdot \Delta T = \Delta T^2,
$$

with the constant of proportionality $\Omega$ absorbing the geometry, the mixing efficiency, and the thermal expansion and haline contraction coefficients that set the plume buoyancy. One power of $\Delta T$ is the heat available per unit of circulation; the second is the strengthening of the circulation that the same warming drives. The coefficient $\Omega$ is poorly constrained because each of these factors is, which is why it is a leading source of projection uncertainty {cite}`joughin2014,parizek2013`.
```

where the quadratic dependence enters because a warmer ocean both advects more heat toward
the interface and drives a stronger melt-driven overturning circulation beneath the shelf
that brings yet more heat into contact with the ice. The coefficient $\Omega$ depends on
the geometry and mixing efficiency and is poorly constrained; it is one of the leading
sources of projection uncertainty in West Antarctica. The Amundsen Sea embayment, where
Pine Island and Thwaites glaciers drain through deep marine basins into a bowl of
Circumpolar Deep Water that sits several degrees above freezing, is the clearest
present-day example of this mechanism at work {cite}`joughin2014,parizek2013`. Frontal
melt at calving fronts follows a simpler formulation driven by the depth of warm water
contact, but it too amplifies the sensitivity of marine glaciers to ocean temperature
beyond what atmospheric forcing alone produces. The full dynamics of ice shelves and
grounding lines, buttressed against ocean forcing, are the subject of
{doc}`../cryosphere/ice-sheets`.

The ocean forcing also enters the two-stage Robel model through the grounding-zone flux
term $Q_g$. Because that flux scales as $h_g^\beta$ with $\beta \approx 5$, a small
increase in sub-shelf melt that thins the ice at the grounding line is amplified five-fold
into a flux perturbation. This is why stochastic ocean forcing through the two-stage filter
produces grounding-line variability that looks large and dramatic even when the forcing
itself is modest: the filter does not attenuate the forcing, it amplifies it at low
frequencies. The poorly constrained $\Omega$ is therefore not merely an error bar in a
basal melt formula; it is the amplitude of the forcing that drives the slow, committed
retreat behavior the model predicts.

## Closing the loop

The Icepack labs that follow this chapter build prognostic models of glacier and ice-sheet
evolution. Each lab begins by constructing a $\dot a(x,t)$ from one of the parameterizations
above, usually the linear ELA form for idealized experiments and a temperature-index scheme
for scenario-forced runs. The model then integrates the conservation law forward in time,
and the output is the evolving thickness and flow that can be compared against observations.

Projection uncertainty in those runs lives in a predictable hierarchy. The flow law itself,
Glen's $n=3$ with a rate factor $A$ varying tenfold across the temperature range of an
ice sheet, is actually among the better-constrained parts of the problem. The mass balance,
with its cloud of uncertainties in precipitation phase, lapse-rate corrections, degree-day
factors, and ocean thermal forcing, is far less well constrained. The basal friction, as
argued in {doc}`../thermomechanics/basal-motion`, is least constrained of all.

The two-stage model adds one more lesson to this hierarchy. The filter it describes
amplifies forcing uncertainty at precisely the timescales we care about for sea-level
projections. An uncertainty in $\dot a$ or in the ocean thermal forcing parameter $\Omega$
that looks small in a year-by-year budget becomes large when integrated through a slow
eigenmode with a millennial timescale. Knowing the hierarchy of uncertainty sources does
not make the projections more accurate, but it does say clearly where improved observations
would reduce it most rapidly — not in the ice, but at the surface above, the ocean below,
and the bed in between.
