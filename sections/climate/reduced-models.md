# Reduced models of glacier and ice-sheet response

The lab preceding this chapter integrated a full stress balance forward in time, and the cost of doing so is part of its lesson; resolving one forcing scenario for one synthetic ice stream takes minutes to hours, and mapping the sensitivity of the response to even a few uncertain parameters multiplies that cost by hundreds. Reduced models compress the same system into a small number of ordinary differential equations by tracking reservoirs of ice and the fluxes between them, and they are the standard tools for understanding sensitivity to climate forcing, for attributing observed change against natural variability, and for locating instabilities before a full model is ever run. This chapter derives the two models used throughout the rest of the book, the three-stage model of Roe and Baker {cite}`roebaker2014` for land-terminating glaciers and the two-stage model of Robel, Roe, and Haseloff {cite}`robel2018` for marine-terminating ice streams, and then examines how the marine model behaves as the bed slope at the grounding line is reversed.

## Interior and grounding-zone fluxes

Both models rest on writing the ice body's mass budget in terms of two kinds of flux, and the fluxes deserve to be set out explicitly before any equations are coupled.

The *interior flux* $Q$ is the rate at which ice is delivered from the accumulation zone toward the margin. Its dependence on geometry follows from the flow physics of the earlier chapters. For an interior deforming by shear, the shallow-ice flux of {doc}`../ice_flow/shallow-ice` scales as $H^{n+2}|\nabla s|^{n}$, and with the surface slope of a reservoir of thickness $H$ and length $L$ scaling as $H/L$, the delivered flux takes the form

$$
Q = \nu\,\frac{H^{\alpha}}{L^{\gamma}},
$$

with $\alpha = 2n+2$ and $\gamma = n$ for deformation-dominated flow, and smaller exponents when sliding dominates; the constant $\nu$ absorbs the rate factor and the geometry. The essential property is that $Q$ increases steeply with interior thickness and decreases with length, so a thickening interior pushes more ice toward the margin and a lengthening one, at fixed thickness, pushes less.

The *grounding-zone flux* $Q_g$ is the rate at which ice is exported across the grounding line, the point where the ice goes afloat. Flotation ties the thickness there to the bed, since ice of density $\rho_i$ floats in water of density $\rho_w$ when its thickness falls below $-\lambda b$, where $b(x)$ is the bed elevation, negative below sea level, and $\lambda = \rho_w/\rho_i \approx 1.1$. The grounding-line thickness is therefore not free but pinned to the local bed,

$$
h_g = -\lambda\, b(L),
$$

and the boundary-layer analysis of the shallow-shelf equations, due to Schoof {cite}`schoof2007` and presented with the ice-sheet material in {doc}`../cryosphere/ice-sheets`, shows that the flux across the grounding line is controlled almost entirely by this one number,

$$
Q_g = \Omega\, h_g^{\beta},
\qquad \beta = \frac{m+n+3}{m+1} \approx 4.75
$$

for Glen exponent $n=3$ and Weertman friction exponent $m=1/3$. The prefactor $\Omega$ collects the rate factor, the friction coefficient, and the buttressing supplied by an ice shelf, and it is the handle through which the ocean grips the system; shelf thinning or grounding-zone melt acts on the ice sheet by raising $\Omega$. The exponent is the important number. With $\beta \approx 5$, a ten percent increase in grounding-line thickness nearly doubles the export, so small migrations of the grounding line across a sloping bed produce large changes in discharge.

A steady state is a geometry in which these fluxes balance the surface input. With accumulation rate $P$ over a reservoir of length $L$, steadiness requires

$$
P\,L = Q = Q_g,
$$

two conditions that, on a given bed, select the equilibrium thickness $\bar H$ and grounding-line position $\bar L$. Everything else in this chapter is the behavior of the system near and far from this balance.

## The three-stage model for land-terminating glaciers

For a mountain glacier the exported flux ends in a terminus wedge rather than a grounding zone, and the one-stage reservoir model of {doc}`glacier-variations` captures the equilibrium response and the basic response time $\tau = H/\dot a_0$. Its flaw is dynamical. A one-stage model passes a mass-balance anomaly to the terminus instantly, whereas a real glacier responds in sequence, the interior thickening first, the thickening driving anomalous flux down-glacier, and the length responding only when that flux arrives. Roe and Baker {cite}`roebaker2014` represented the sequence as three linear reservoirs in series, an interior thickness anomaly $h'$ fed by the balance anomaly $\dot b'$, a terminus flux anomaly $F'$ fed by the available thickness, and a length anomaly $L'$ fed by the flux,

$$
\frac{dh'}{dt}+\frac{h'}{\epsilon\tau}=\dot b', \qquad
\frac{dF'}{dt}+\frac{F'}{\epsilon\tau}=\frac{L\,h'}{(\epsilon\tau)^{2}}, \qquad
\frac{dL'}{dt}+\frac{L'}{\epsilon\tau}=\frac{F'}{\epsilon H},
$$

with $\epsilon = 1/\sqrt{3}$ chosen so that the chain preserves both the equilibrium response and the e-folding behavior of the one-stage model. Each equation is the same flux bookkeeping as the steady-state balance above, linearized; the left sides drain each reservoir on the timescale $\epsilon\tau$, and the right sides are the fluxes passed down the chain. Eliminating $h'$ and $F'$ gives a single third-order equation,

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

The terminus barely moves for the first fraction of a response time, while the flux anomaly is still in transit, and then catches up to the same equilibrium response the one-stage model predicts. Because the three-stage glacier filters high-frequency forcing more aggressively than a single reservoir, its variance, autocorrelation, and excursion statistics under interannual noise can all be written in closed form, and those expressions are the machinery beneath the formal attribution of observed glacier retreat to climate change {cite}`roe2017` discussed in {doc}`glacier-variations`. The model is linear, so it can also be run backward, turning a length record into an estimate of the mass-balance history that produced it.

## The two-stage model for marine ice streams

For the ice streams of West Antarctica and the outlet glaciers of Greenland the controlling boundary is the grounding line, and the reduced model needs two state variables, the mean interior thickness $H$ and the grounding-line position $L$, with $x$ measured seaward from the divide. The derivation is mass conservation applied twice {cite}`robel2018`.

Applied to the whole reservoir, of volume $V \approx HL$ per unit width, conservation reads

$$
\frac{dV}{dt} = P\,L - Q_g,
$$

since snowfall supplies $PL$ and the only export is across the grounding line. Applied to the grounding zone alone, conservation determines how the grounding line moves. Advancing the grounding line by $dL$ requires filling a column of thickness $h_g$ with ice, and the ice available to fill it is the difference between what the interior delivers and what the grounding line exports, so

$$
\frac{dL}{dt} = \frac{Q - Q_g}{h_g}.
$$

Expanding $dV/dt = H\,dL/dt + L\,dH/dt$ and combining the two statements gives the interior equation,

$$
\frac{dH}{dt} = P - \frac{Q_g}{L} - \frac{H}{h_g L}\left(Q - Q_g\right),
$$

in which the first two terms are accumulation against export and the third is the geometric correction for the moving boundary. Equations for $L$ and $H$, with the flux laws of the first section, close the model; this pair is the two-stage model, and at a steady state it reduces exactly to the flux balance $PL = Q = Q_g$.

Linearized about that steady state, the system has two eigenvalues and therefore two e-folding timescales, and they are far apart. The fast mode, with a timescale of decades to a few centuries, is the grounding zone adjusting toward flux balance at nearly fixed interior thickness; it is fast because the grounding zone is thin, so modest flux imbalances move it quickly. The slow mode, with a timescale of millennia, is the interior thickness relaxing, the marine analog of $\tau = H/\dot a_0$, slow because the interior is thick and the balance fluxes small. A perturbed marine ice stream therefore shows a quick partial response followed by a long completion, and it can sit far from equilibrium for centuries while appearing superficially quiet.

## Sensitivity to climate forcing

The reduced model's value is that the sensitivity of the steady state can now be written down rather than mapped numerically. Climate forcing enters through two parameters, the accumulation rate $P$ for the atmosphere and the grounding-zone coefficient $\Omega$ for the ocean, since melt at the grounding zone and the thinning of a buttressing shelf both act by raising $\Omega$. Differentiating the steady-state balance $\Omega\, h_g(L)^{\beta} = P\,L$ logarithmically gives the response of the grounding line to small changes in either,

$$
\frac{\delta \bar L}{\bar L} = \frac{1}{\Sigma}\left(\frac{\delta P}{P} - \frac{\delta \Omega}{\Omega}\right),
\qquad
\Sigma \equiv \beta\,\frac{\bar L\, h_g'(\bar L)}{\bar h_g} - 1,
$$

where $h_g'(L) = -\lambda\, b_x(L)$ is the rate at which the flotation thickness grows as the grounding line advances, set entirely by the bed slope $b_x = db/dx$. The dimensionless number $\Sigma$ controls everything. On a strongly prograde bed, one that deepens seaward so that $b_x < 0$ and $h_g' > 0$, $\Sigma$ is large and positive, the gain $1/\Sigma$ is small, and the grounding line is stiff against forcing, since any advance is punished by the steeply rising export $\Omega h_g^\beta$. The same number governs stability. The slow mode of the linearized system decays at a rate proportional to $\Sigma$, so steady states with $\Sigma > 0$ are stable and steady states with $\Sigma < 0$ are not.

The stochastic counterpart of this sensitivity matters as much as the deterministic one. Driven by the broadband natural variability of ocean temperature, the two-stage system behaves as the marine extension of the Hasselmann argument made at the opening of {doc}`climate-forcing` {cite}`hasselmann1976`; it integrates the forcing, amplifies it at the slow eigenfrequency, and produces grounding-line excursions that are large, slow, and persistent. A marine ice stream in a statistically steady climate can sustain kilometer-scale grounding-line fluctuations on multi-centennial timescales from noise alone, which is why a decade of observed retreat, by itself, cannot distinguish forced change from natural variability, and why formal attribution requires the noise statistics these models supply.

## Reverse bed slopes and the approach to instability

The asymptotic behavior of the gain $1/\Sigma$ as the bed slope is varied is the cleanest route into the book's instability discussion. Hold the climate fixed and flatten the bed at the grounding line, so that $h_g' \to h_g/(\beta L)$ from above and $\Sigma \to 0^+$. Three things happen together. The sensitivity $1/\Sigma$ of the steady state diverges, so ever-smaller changes in ocean or atmosphere produce ever-larger equilibrium migrations. The slow eigenvalue, proportional to $\Sigma$, goes to zero, so the system takes arbitrarily long to settle, the critical slowing that in observed systems precedes a bifurcation. And the steady state's basin of attraction shrinks, so finite fluctuations of the kind the stochastic forcing supplies become capable of dislodging the system entirely.

When the slope reverses, $b_x > 0$ at the grounding line, the bed deepening inland, the flotation thickness *increases* as the grounding line retreats, $h_g' < 0$, and $\Sigma$ is negative for any $\beta > 0$. No stable steady state exists on such a slope. A retreat into deeper water raises $h_g$, which raises the export $\Omega h_g^\beta$ by more than it raises the supply, which draws the interior down and retreats the grounding line further, and the feedback closes on itself without any new physics. This is the marine ice-sheet instability, obtained here from two mass reservoirs and a flux rule, with no stress balance anywhere in the argument, which is the strongest available evidence that the instability is at root a statement about mass conservation over a bed that deepens inland. A grounding line perturbed off the end of a retrograde reach does not stop until it finds the next prograde slope, which is the origin of the hysteresis and the discrete stable positions explored with the full mechanical story, buttressing, and the observational case for the Amundsen Sea glaciers in {doc}`../cryosphere/ice-sheets`, and of the oscillatory variants in {doc}`../cryosphere/instabilities`. The lab preceding this chapter shows the same asymmetry numerically; the icepack stream on a prograde bed relaxes exponentially to a new steady state when forced, while the same stream forced on the overdeepened bed accelerates away from its initial state and does not return.

The reduced models earn their place in this book because they convert the prognostic problem's most expensive questions, how sensitive, how fast, how close to the edge, into algebra. The full models of {doc}`../modeling/prognostic-problem` remain the instruments of projection, but the two-stage and three-stage systems are how the projections are understood, attributed, and stress-tested, and they are the lens through which {doc}`../cryosphere/ice-sheets` and {doc}`../cryosphere/instabilities` are best read.
