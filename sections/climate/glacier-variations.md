# Glacier variations and response time

In 1905 a survey party photographed Lillian Glacier in the Olympic Mountains as a healthy body of ice filling its cirque. A photograph from the same vantage in 2010 shows bare rock and a few snow patches. Between the two images lies a century of climate, filtered through the dynamics of a small mountain glacier. This chapter builds the simplest theory that connects the two photographs. It asks how far a glacier's terminus moves when its mass balance changes, and how long the move takes. The answers come from the mass balance ideas of {doc}`../ice_flow/mass-balance` applied to a glacier that is allowed to change its length, and they are developed in Chapter 11 of {cite}`cuffey2010`.

The theory in this chapter is deliberately kinematic. We will not solve the stress balance at all. Everything follows from conservation of mass and a little geometry, which is why the results are so portable, and the price of that simplicity is that the dynamics of the flow appear only through a single number, the thickness of the ice. The same reservoir reasoning extends a long way. After the land-terminating glacier we chain reservoirs into the three-stage model of Roe and Baker, and then carry the logic to the ocean, where the two-stage model of Robel, Roe, and Haseloff describes a marine ice stream and produces the marine ice-sheet instability from nothing more than mass conservation and a flux rule. These reduced models are the efficient lens through which the prognostic experiments and the instability chapters that follow are best understood.

## The equilibrium response

Consider a glacier of length $L_0$ in steady state with a specific mass balance profile $\dot b_0(x)$, where $x$ runs down-glacier from the head. Steady state means the balance integrates to zero over the glacier, so no ice passes the terminus. Now perturb the balance by $\dot b_1(x)$, a persistent change rather than a single anomalous year. The glacier as a whole gains extra mass at a rate set by the spatial average of the perturbation,

$$
\int_0^{L_0} \dot b_1(x)\,dx = \langle \dot b_1 \rangle L_0,
$$

and this extra ice has nowhere to go but past the old terminus. The glacier advances until the new ice is consumed, and if the terminus is a thin wedge where ice ablates at the rate $\dot a_0$, the advance $L_1$ required to restore equilibrium follows from setting the flux in equal to the flux out,

$$
\langle \dot b_1 \rangle L_0 = \dot a_0 L_1
\qquad\Longrightarrow\qquad
L_1 = \frac{\langle \dot b_1 \rangle}{\dot a_0} L_0.
$$

% TODO Illustrator figure: figures/terminus-flux-wedge.svg (label fig-terminus-flux-wedge, width 85%)
% Spec: equilibrium length response. Persistent balance perturbation delivers extra flux
% <b1>L0 to the old terminus; glacier advances by L1 until ablation a0 over the new terminus
% wedge consumes it. After C&P ch. 11.

With a terminus ablation rate of $5\ \mathrm{m\,yr^{-1}}$, a balance increase of only $0.5\ \mathrm{m\,yr^{-1}}$ moves the terminus forward by a tenth of the glacier's length. The terminus is a lever arm, and small persistent changes in climate are amplified into conspicuous changes in length. This is the first reason glacier termini make such legible climate records.

If the glacier drains a wide accumulation basin into a narrow tongue, the same balance perturbation collected over the broad upper glacier must be disposed of along a slim terminus, and the advance grows by the ratio of the mean width $\bar Y$ to the terminus width $Y_t$,

$$
L_1 = \frac{\langle \dot b_1 \rangle}{\dot a_0}\,\frac{\bar Y}{Y_t}\, L_0.
$$

Wide-basin, narrow-tongue glaciers are therefore the most excitable. An ice sheet spreading as an unconstrained circle sits at the opposite extreme. There $\bar Y/Y_t = 1/2$, the ablation zone widens as it lengthens, and terminus fluctuations are damped. The mass-balance gradient matters in the same way, since a glacier whose terminus descends into a zone of fierce ablation needs less advance to bury the imbalance than one lying on a gentle slope where the ablation rate barely changes along flow {cite}`oerlemans2008`.

Nothing in this argument says how long the adjustment takes. For that we need to let the length depend on time.

## The response time

Let the balance perturbation $\dot b_1$ switch on at $t=0$ and stay on, and track the glacier volume $V$. Away from the terminus, treat the glacier as a slab of constant thickness $H_0$. The volume grows because the perturbation adds mass over the original glacier, and it shrinks because ablation eats the advancing wedge,

$$
\frac{dV}{dt} = \bar Y L_0 \dot b_1 - Y_t \dot a_0 L_1(t).
$$

The same volume change is expressed by the advance itself, $dV/dt = Y_t H_0\, dL_1/dt$. Equating the two and dividing through by $Y_t H_0$ gives a first-order linear equation for the length perturbation,

$$
\frac{dL_1}{dt} + \frac{L_1}{t_r} = \dot b_1\,\frac{\bar Y}{Y_t}\,\frac{L_0}{H_0},
\qquad
t_r \equiv \frac{H}{\dot a_0}.
$$

The combination $t_r = H/\dot a_0$ is the **glacier response time** of Jóhannesson, Raymond, and Waddington {cite}`johannesson1989`, the ice thickness divided by the ablation rate at the terminus. Everything about the valley, the climate, and the flow has collapsed into these two numbers. For a step change in balance the solution is exponential adjustment toward the equilibrium response we found above,

$$
L_1(t) = \frac{\dot b_1}{\dot a_0}\,\frac{\bar Y}{Y_t}\,L_0 \left[1 - e^{-t/t_r}\right].
$$

% TODO Illustrator figure: figures/response-time-curve.svg (label fig-response-time-curve, width 80%)
% Spec: length vs time after a step change in balance, exponential approach to new equilibrium;
% mark 63% at one response time t_r = H/a_0 and 86% at two; cite johannesson1989.

A glacier on Mount Rainier with $H = 100$ m and a terminus ablation rate of $10\ \mathrm{m\,yr^{-1}}$ has $t_r = 10$ years. An ice sheet with $H = 1500$ m losing $1\ \mathrm{m\,yr^{-1}}$ at its margin has $t_r = 1500$ years. Mountain glaciers reflect a few decades of climate. Ice sheets reflect millennia, which is why their present shape still carries the imprint of the last glacial period, a thread we pick up again in {doc}`paleoclimate`. Thick glaciers in cold, dry climates respond slowly. Thin glaciers with high terminus ablation, the maritime glaciers of Norway and New Zealand among them, respond within a decade or two.

## Glaciers as filters of climate

The step response is a Green's function in disguise, and once we have it, the response to any climate history follows by superposition. Two consequences deserve emphasis because they shape how length records must be read.

The first is that a glacier converts noisy climate into smooth, persistent length fluctuations. Interannual mass-balance variability is essentially white noise, a few tenths of a meter to a couple of meters water equivalent from year to year with little memory. Run that noise through the first-order equation above and the length performs slow, red-noise wanderings of a kilometer or more over decades, even with no climate trend at all. A wandering terminus is therefore not, by itself, evidence of climate change. The South Cascade Glacier mass-balance record, the longest in North America, looks like noise about a weak trend, while the length record of the same glacier is a smooth monotonic retreat. Both views are honest; the glacier has simply integrated the one into the other.

The second consequence is lag. During a steady warming ramp the terminus adjusts toward an equilibrium that continues to recede ahead of it, and the gap between the actual length and the equilibrium length grows with $t_r$. Stop the warming and the glacier keeps retreating until it closes that gap. This unrealized response is the **committed retreat**, and it can exceed the retreat already observed. For South Cascade Glacier, with $H = 200$ m, a terminus balance rate near $-5.4\ \mathrm{m\,yr^{-1}}$, and $t_r \approx 37$ years, the committed terminus position lies roughly two kilometers behind the present one even with no further warming. The steeper, thinner Nisqually Glacier on Mount Rainier, with $t_r \approx 12$ years, tracks its climate closely and has little retreat left in the bank.

Set against the natural variability envelope, the observed centennial retreat of glaciers worldwide, from Hintereisferner to Franz Josef to Nigardsbreen, lies far outside what red-noise wandering can produce, and Roe, Baker, and Herla turned exactly this comparison into a formal attribution, finding that the retreats of the last century are categorical evidence of regional climate change {cite}`roe2017,leclercq2014`. The humble first-order equation of this chapter is the engine of that argument.

```{admonition} A caveat about what $t_r$ hides
:class: warning

The kinematic model treats the glacier as a reservoir with a single thickness, and its response time is an e-folding scale, not a delay. It says nothing about how thickness anomalies propagate down-glacier, which is the business of kinematic waves, and it fails entirely for glaciers whose termini end in water, where calving opens a mass-loss channel with its own dynamics. Tidewater glaciers can advance and retreat on cycles almost decoupled from climate, the subject we take up with the flow instabilities in {doc}`../cryosphere/instabilities`.
```

## The three-stage model

The one-stage model has a flaw that becomes visible the moment the step change switches on. Its terminus begins to move immediately, at its maximum rate, because the model passes a balance perturbation straight to the terminus with no intervening glacier. A real glacier responds in sequence. The interior thickens first, the extra thickness drives extra flux toward the terminus, and only when that flux arrives does the length begin to change in earnest. Roe and Baker {cite}`roebaker2014` represented this sequence as three linear reservoirs in series, an interior thickness anomaly $h'$ fed by the balance anomaly $\dot b'$, a terminus flux anomaly $F'$ fed by the available thickness, and a length anomaly $L'$ fed by the flux,

$$
\frac{dh'}{dt}+\frac{h'}{\epsilon\tau}=\dot b', \qquad
\frac{dF'}{dt}+\frac{F'}{\epsilon\tau}=\frac{L\,h'}{(\epsilon\tau)^{2}}, \qquad
\frac{dL'}{dt}+\frac{L'}{\epsilon\tau}=\frac{F'}{\epsilon H},
$$

with $\epsilon = 1/\sqrt{3}$ chosen so that the chain preserves both the equilibrium response and the e-folding behavior of the one-stage model. Each equation is the same mass bookkeeping as the one-stage reservoir, linearized; the left sides drain each reservoir on the timescale $\epsilon\tau$, and the right sides are the fluxes passed down the chain. Eliminating $h'$ and $F'$ gives a single third-order equation,

$$
\left(\frac{d}{dt}+\frac{1}{\epsilon\tau}\right)^{3} L' = \frac{L}{H}\,\frac{\dot b'}{\epsilon\,(\epsilon\tau)^{2}},
$$

whose response to a step change in balance is sigmoidal rather than exponential,

$$
L'(t) = L'_{\mathrm{eq}}\left[1 - e^{-t/\epsilon\tau}\left(1 + \frac{t}{\epsilon\tau} + \frac{1}{2}\left(\frac{t}{\epsilon\tau}\right)^{2}\right)\right].
$$

% TODO Illustrator figure: figures/three-stage-response.svg (label fig-three-stage-response, width 80%)
% Spec: step responses of one-stage vs three-stage kinematic models, same equilibrium response and
% timescale tau; three-stage curve sigmoidal (delayed onset, then catches up); cite roebaker2014.

The terminus barely moves for the first fraction of a response time, while the flux anomaly is still in transit, and then catches up to the same equilibrium the one-stage model predicts. Because the three-stage glacier filters high-frequency forcing more aggressively than a single reservoir, its variance, autocorrelation, and excursion statistics under interannual noise can all be written in closed form, and those expressions are the machinery beneath the formal attribution of observed glacier retreat to climate change {cite}`roe2017` discussed above. The model is linear, so it can also be run backward, turning a length record into an estimate of the mass-balance history that produced it. The lab accompanying this chapter builds both the one-stage and the three-stage filters and forces them with steps, noise, and ramps.

## Marine-terminating glaciers: interior and grounding-zone fluxes

For an ice sheet the terminus wedge is the wrong picture. The margins of Antarctica mostly end in the ocean, mass leaves by calving and by basal melting of floating ice shelves, and the controlling boundary is the grounding line, where the ice goes afloat over a bed that often deepens inland. The reservoir logic of this chapter survives the change of setting, worked out by Robel, Roe, and Haseloff {cite}`robel2018`, with one extra state variable and much richer consequences. The construction rests on two kinds of flux, which are worth setting out before the reservoirs are coupled.

The *interior flux* $Q$ is the rate at which ice is delivered from the accumulation zone toward the margin. Its dependence on geometry follows from the flow physics of the earlier chapters. For an interior deforming by shear, the shallow-ice flux of {doc}`../ice_flow/shallow-ice` scales as $H^{n+2}|\nabla s|^{n}$, and with the surface slope of a reservoir of thickness $H$ and length $L$ scaling as $H/L$, the delivered flux takes the form

$$
Q = \nu\,\frac{H^{\alpha}}{L^{\gamma}},
$$

with $\alpha = 2n+2$ and $\gamma = n$ for deformation-dominated flow, and smaller exponents when sliding dominates; the constant $\nu$ absorbs the rate factor and the geometry. The interior flux increases steeply with thickness and decreases with length, so a thickening interior pushes more ice toward the margin and a lengthening one, at fixed thickness, pushes less.

The *grounding-zone flux* $Q_g$ is the rate at which ice is exported across the grounding line. Flotation ties the thickness there to the bed, since ice of density $\rho_i$ floats in water of density $\rho_w$ when its thickness falls below $-\lambda b$, where $b(x)$ is the bed elevation, negative below sea level, and $\lambda = \rho_w/\rho_i \approx 1.1$. The grounding-line thickness is therefore not free but pinned to the local bed,

$$
h_g = -\lambda\, b(L),
$$

and the boundary-layer analysis of the shallow-shelf equations, due to Schoof {cite}`schoof2007` and presented with the ice-sheet material in {doc}`../cryosphere/ice-sheets`, shows that the flux across the grounding line is controlled almost entirely by this one number,

$$
Q_g = \Omega\, h_g^{\beta},
\qquad \beta = \frac{m+n+3}{m+1} \approx 4.75
$$

for Glen exponent $n=3$ and Weertman friction exponent $m=1/3$. The prefactor $\Omega$ collects the rate factor, the friction coefficient, and the buttressing supplied by an ice shelf, and it is the handle through which the ocean grips the system; shelf thinning or grounding-zone melt acts on the ice sheet by raising $\Omega$. The exponent is the important number. With $\beta \approx 5$, a ten percent increase in grounding-line thickness nearly doubles the export, so small migrations of the grounding line across a sloping bed produce large changes in discharge. A steady state is a geometry in which these fluxes balance the surface input; with accumulation rate $P$ over a reservoir of length $L$, steadiness requires $P\,L = Q = Q_g$, two conditions that on a given bed select the equilibrium thickness $\bar H$ and grounding-line position $\bar L$.

## The two-stage model for marine ice streams

With the fluxes in hand the marine model needs two state variables, the mean interior thickness $H$ and the grounding-line position $L$, with $x$ measured seaward from the divide. The derivation is mass conservation applied twice {cite}`robel2018`. Applied to the whole reservoir, of volume $V \approx HL$ per unit width, conservation reads

$$
\frac{dV}{dt} = P\,L - Q_g,
$$

since snowfall supplies $PL$ and the only export is across the grounding line. Applied to the grounding zone alone, conservation determines how the grounding line moves; advancing it by $dL$ requires filling a column of thickness $h_g$ with ice, and the ice available is the difference between what the interior delivers and what the grounding line exports, so

$$
\frac{dL}{dt} = \frac{Q - Q_g}{h_g}.
$$

Expanding $dV/dt = H\,dL/dt + L\,dH/dt$ and combining the two statements gives the interior equation,

$$
\frac{dH}{dt} = P - \frac{Q_g}{L} - \frac{H}{h_g L}\left(Q - Q_g\right),
$$

in which the first two terms are accumulation against export and the third is the geometric correction for the moving boundary. These two equations are the two-stage model, and at a steady state they reduce exactly to the flux balance $PL = Q = Q_g$. Linearized about that steady state, the system has two eigenvalues and therefore two e-folding timescales, and they are far apart. The fast mode, decades to a few centuries, is the grounding zone adjusting toward flux balance at nearly fixed interior thickness; it is fast because the grounding zone is thin, so modest flux imbalances move it quickly. The slow mode, of order millennia, is the interior thickness relaxing, the marine analog of $t_r = H/\dot a_0$, slow because the interior is thick and the balance fluxes small. A perturbed marine ice stream therefore shows a quick partial response followed by a long completion, and it can sit far from equilibrium for centuries while appearing superficially quiet.

## Sensitivity to climate forcing

The reduced model's value is that the sensitivity of the steady state can be written down rather than mapped numerically. Climate forcing enters through two parameters, the accumulation rate $P$ for the atmosphere and the grounding-zone coefficient $\Omega$ for the ocean, since melt at the grounding zone and the thinning of a buttressing shelf both act by raising $\Omega$. Differentiating the steady-state balance $\Omega\, h_g(L)^{\beta} = P\,L$ logarithmically gives the response of the grounding line to small changes in either,

$$
\frac{\delta \bar L}{\bar L} = \frac{1}{\Sigma}\left(\frac{\delta P}{P} - \frac{\delta \Omega}{\Omega}\right),
\qquad
\Sigma \equiv \beta\,\frac{\bar L\, h_g'(\bar L)}{\bar h_g} - 1,
$$

where $h_g'(L) = -\lambda\, b_x(L)$ is the rate at which the flotation thickness grows as the grounding line advances, set entirely by the bed slope $b_x = db/dx$. The dimensionless number $\Sigma$ controls everything. On a strongly prograde bed, one that deepens seaward so that $b_x < 0$ and $h_g' > 0$, $\Sigma$ is large and positive, the gain $1/\Sigma$ is small, and the grounding line is stiff against forcing, since any advance is opposed by the steeply rising export $\Omega h_g^\beta$. The same number governs stability. The slow mode of the linearized system decays at a rate proportional to $\Sigma$, so steady states with $\Sigma > 0$ are stable and steady states with $\Sigma < 0$ are not.

The stochastic counterpart of this sensitivity matters as much as the deterministic one. Driven by the broadband natural variability of ocean temperature, the two-stage system is the marine version of the red-noise filter described above for mountain glaciers; it integrates the forcing, amplifies it at the slow eigenfrequency, and produces grounding-line excursions that are large, slow, and persistent {cite}`hasselmann1976`. A marine ice stream in a statistically steady climate can sustain kilometer-scale grounding-line fluctuations on multi-centennial timescales from noise alone, which is why a decade of observed retreat, by itself, cannot distinguish forced change from natural variability, and why formal attribution requires the noise statistics these models supply.

## Reverse bed slopes and the approach to instability

The asymptotic behavior of the gain $1/\Sigma$ as the bed slope is varied is the cleanest route into the book's instability discussion. Hold the climate fixed and flatten the bed at the grounding line, so that $h_g' \to h_g/(\beta L)$ from above and $\Sigma \to 0^+$. Three things happen together. The sensitivity $1/\Sigma$ of the steady state diverges, so ever-smaller changes in ocean or atmosphere produce ever-larger equilibrium migrations. The slow eigenvalue, proportional to $\Sigma$, goes to zero, so the system takes arbitrarily long to settle, the critical slowing that in observed systems precedes a bifurcation. And the steady state's basin of attraction shrinks, so finite fluctuations of the kind the stochastic forcing supplies become capable of dislodging the system entirely.

When the slope reverses, $b_x > 0$ at the grounding line, the bed deepening inland, the flotation thickness *increases* as the grounding line retreats, $h_g' < 0$, and $\Sigma$ is negative for any $\beta > 0$. No stable steady state exists on such a slope. A retreat into deeper water raises $h_g$, which raises the export $\Omega h_g^\beta$ by more than it raises the supply, which draws the interior down and retreats the grounding line further, and the feedback closes on itself without any new physics. This is the marine ice-sheet instability, obtained here from two mass reservoirs and a flux rule, with no stress balance anywhere in the argument, which is the strongest available evidence that the instability is at root a statement about mass conservation over a bed that deepens inland. A grounding line perturbed off the end of a retrograde reach does not stop until it finds the next prograde slope, the origin of the hysteresis and the discrete stable positions explored, with the full mechanical story, buttressing, and the observational case for the Amundsen Sea glaciers, in {doc}`../cryosphere/ice-sheets`, and of the oscillatory variants in {doc}`../cryosphere/instabilities`. The lab accompanying this chapter exhibits the asymmetry directly, the two-stage model relaxing to a new steady state when forced on a prograde bed and running away when forced on a retrograde one, and the full stress-balance version of the same experiment is carried out in icepack in {doc}`../modeling/ice-stream-vaf-lab`.

These reduced models earn their place in the book because they convert the prognostic problem's most expensive questions, how sensitive, how fast, how close to the edge, into algebra. The full models of {doc}`../modeling/prognostic-problem` remain the instruments of projection, but the one-, two-, and three-stage systems are how the projections are understood, attributed, and stress-tested, and they are the lens through which {doc}`../cryosphere/ice-sheets` and {doc}`../cryosphere/instabilities` are best read.
