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

```{admonition} Derivation
:class: dropdown

The balance condition is a statement of steady-state mass conservation for the perturbed glacier. In the original steady state the balance integrates to zero, so no ice crosses the old terminus at $x = L_0$. Switching on the persistent perturbation $\dot b_1(x)$ adds mass to the glacier at a rate equal to its integral over the glacier, which by definition of the spatial average is

$$
\dot V_{\mathrm{in}} = \int_0^{L_0}\dot b_1(x)\,dx = \langle\dot b_1\rangle\,L_0
$$

per unit width. In the new steady state this surplus must be removed, and the only place it can leave is across the advanced terminus. The glacier extends past the old terminus by a thin wedge of new length $L_1$. Over that wedge the surface lies in the ablation zone, where ice is lost at the terminus ablation rate $\dot a_0$ per unit length of advance, so the additional loss the advance opens up is

$$
\dot V_{\mathrm{out}} = \dot a_0\,L_1.
$$

A new steady state requires the surplus to be exactly consumed, $\dot V_{\mathrm{in}} = \dot V_{\mathrm{out}}$, which is the balance written in the text. Solving for the advance,

$$
\langle\dot b_1\rangle\,L_0 = \dot a_0\,L_1
\qquad\Longrightarrow\qquad
L_1 = \frac{\langle\dot b_1\rangle}{\dot a_0}\,L_0.
$$

The terminus advance is the original length scaled by the ratio of the mean balance perturbation to the terminus ablation rate. Because that ratio is small while $L_0$ is large, a modest persistent balance change moves the terminus a conspicuous distance, the lever-arm amplification discussed in the text.
```

% TODO Illustrator figure: figures/terminus-flux-wedge.svg (label fig-terminus-flux-wedge, width 85%)
% Spec: equilibrium length response. Persistent balance perturbation delivers extra flux
% <b1>L0 to the old terminus; glacier advances by L1 until ablation a0 over the new terminus
% wedge consumes it. After C&P ch. 11.

With a terminus ablation rate of $5\ \mathrm{m\,yr^{-1}}$, a balance increase of only $0.5\ \mathrm{m\,yr^{-1}}$ moves the terminus forward by a tenth of the glacier's length. The terminus is a lever arm, and small persistent changes in climate are amplified into conspicuous changes in length. This is the first reason glacier termini make such legible climate records.

If the glacier drains a wide accumulation basin into a narrow tongue, the same balance perturbation collected over the broad upper glacier must be disposed of along a slim terminus, and the advance grows by the ratio of the mean width $\bar Y$ to the terminus width $Y_t$,

$$
L_1 = \frac{\langle \dot b_1 \rangle}{\dot a_0}\,\frac{\bar Y}{Y_t}\, L_0.
$$

```{admonition} Derivation
:class: dropdown

When the glacier varies in width the mass conservation of the previous derivation must be written in terms of volume rather than length, because a unit advance of a wide section delivers more ice than a unit advance of a narrow one. Let $Y(x)$ be the flowband width and $\bar Y$ its mean over the glacier. The surplus collected over the whole glacier is the perturbation integrated over area,

$$
\dot V_{\mathrm{in}} = \int_0^{L_0}\dot b_1(x)\,Y(x)\,dx = \langle\dot b_1\rangle\,\bar Y\,L_0,
$$

where the last step takes the perturbation and the width to be uncorrelated so that the area integral factors into the mean balance times the mean width times the length. The export, by contrast, occurs only across the terminus, whose width is the terminus value $Y_t$. The advancing wedge of length $L_1$ loses ice at rate $\dot a_0$ over that width,

$$
\dot V_{\mathrm{out}} = \dot a_0\,Y_t\,L_1.
$$

Balancing supply against export, $\langle\dot b_1\rangle\,\bar Y\,L_0 = \dot a_0\,Y_t\,L_1$, and solving,

$$
L_1 = \frac{\langle\dot b_1\rangle}{\dot a_0}\,\frac{\bar Y}{Y_t}\,L_0.
$$

The width ratio $\bar Y/Y_t$ multiplies the uniform-width result. A glacier with a broad accumulation basin and a slim tongue has $\bar Y/Y_t \gg 1$ and advances far, because surplus gathered over a wide area is forced out through a narrow terminus. An unconstrained circular ice cap has the opposite geometry; the terminus circumference exceeds the mean width so that $\bar Y/Y_t = 1/2$, and its fluctuations are damped.
```

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

```{admonition} Derivation
:class: dropdown

Start from the two expressions for the rate of volume change. The first is the mass budget of the time-dependent advance, supply over the original glacier minus loss over the wedge of current length $L_1(t)$,

$$
\frac{dV}{dt} = \bar Y\,L_0\,\dot b_1 - Y_t\,\dot a_0\,L_1(t).
$$

The second expresses the same volume change geometrically. Away from the terminus the glacier is a slab of fixed thickness $H_0$, so an advance $dL_1$ of the terminus, of width $Y_t$, adds a volume $Y_t H_0\,dL_1$,

$$
\frac{dV}{dt} = Y_t\,H_0\,\frac{dL_1}{dt}.
$$

Equate the two and divide through by $Y_t H_0$,

$$
\frac{dL_1}{dt} = \frac{\bar Y\,L_0\,\dot b_1}{Y_t\,H_0} - \frac{\dot a_0}{H_0}\,L_1.
$$

Moving the $L_1$ term to the left collects it into a relaxation term with coefficient $\dot a_0/H_0$. Identifying the response time $t_r \equiv H_0/\dot a_0$ (written $H/\dot a_0$ in the text) as the reciprocal of that coefficient,

$$
\frac{dL_1}{dt} + \frac{L_1}{t_r} = \dot b_1\,\frac{\bar Y}{Y_t}\,\frac{L_0}{H_0}.
$$

This is a first-order linear ODE. The relaxation timescale $t_r = H/\dot a_0$ emerged purely from the geometry, the slab thickness divided by the terminus ablation rate, with no appeal to the stress balance. Setting $dL_1/dt = 0$ recovers the equilibrium response of the previous section, since $t_r$ on the left and $1/\dot a_0$ inside it combine to give $L_1 = (\dot b_1/\dot a_0)(\bar Y/Y_t)L_0$.
```

The combination $t_r = H/\dot a_0$ is the **glacier response time** of Jóhannesson, Raymond, and Waddington {cite}`johannesson1989`, the ice thickness divided by the ablation rate at the terminus. Everything about the valley, the climate, and the flow has collapsed into these two numbers. For a step change in balance the solution is exponential adjustment toward the equilibrium response we found above,

$$
L_1(t) = \frac{\dot b_1}{\dot a_0}\,\frac{\bar Y}{Y_t}\,L_0 \left[1 - e^{-t/t_r}\right].
$$

```{admonition} Derivation
:class: dropdown

For a step change the right-hand side of the ODE is a constant in time. Denote it $C = \dot b_1\,(\bar Y/Y_t)\,(L_0/H_0)$, so the equation is

$$
\frac{dL_1}{dt} + \frac{L_1}{t_r} = C.
$$

The equilibrium length is the constant solution, found by setting the derivative to zero, $L_{1,\mathrm{eq}} = C\,t_r$. Substituting $C = L_{1,\mathrm{eq}}/t_r$ and writing the deviation from equilibrium as $g(t) = L_1(t) - L_{1,\mathrm{eq}}$ removes the forcing,

$$
\frac{dg}{dt} = \frac{dL_1}{dt} = C - \frac{L_1}{t_r} = -\frac{g}{t_r},
$$

a homogeneous linear equation with the decaying solution $g(t) = g(0)\,e^{-t/t_r}$. The glacier starts at its original length, $L_1(0) = 0$, so $g(0) = -L_{1,\mathrm{eq}}$, and therefore

$$
L_1(t) = L_{1,\mathrm{eq}} + g(t) = L_{1,\mathrm{eq}}\left(1 - e^{-t/t_r}\right).
$$

Inserting the equilibrium length $L_{1,\mathrm{eq}} = C\,t_r = (\dot b_1/\dot a_0)(\bar Y/Y_t)L_0$, in which the $H_0$ in $C$ cancels against the $H_0$ in $t_r$, gives the result quoted in the text. The terminus relaxes exponentially toward the equilibrium response, reaching a fraction $1 - e^{-1} \approx 0.63$ of it after one response time and $1 - e^{-2} \approx 0.86$ after two.
```

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

```{admonition} Derivation
:class: dropdown

Each of the three equations is the same first-order reservoir balance met in the one-stage model, applied to a different state variable, with the output of one reservoir feeding the next. A linear reservoir with state $u$ obeys $\dot u + u/T = S$, where $T$ is its drainage timescale and $S$ its source; the homogeneous part relaxes the reservoir on the timescale $T$ and the source fills it. Roe and Baker split the single relaxation of the one-stage model into three identical stages, each with timescale $\epsilon\tau$.

The first reservoir is the interior thickness anomaly $h'$, sourced directly by the balance anomaly $\dot b'$,

$$
\frac{dh'}{dt} + \frac{h'}{\epsilon\tau} = \dot b'.
$$

The second is the terminus flux anomaly $F'$. The thickness anomaly stored over a glacier of length $L$ drives an extra flux; the source term $L\,h'/(\epsilon\tau)^2$ is constructed so that a static thickness anomaly produces, in steady state, a flux $F' = L\,h'/(\epsilon\tau)$, the extra ice volume per unit time that an anomaly of cross-section $\sim h'$ moving on the reservoir timescale delivers,

$$
\frac{dF'}{dt} + \frac{F'}{\epsilon\tau} = \frac{L\,h'}{(\epsilon\tau)^2}.
$$

The third is the length anomaly $L'$, sourced by the arriving flux divided by the terminus thickness scale $\epsilon H$, since a flux $F'$ delivered to a terminus of thickness $\sim H$ advances the length at rate $F'/H$,

$$
\frac{dL'}{dt} + \frac{L'}{\epsilon\tau} = \frac{F'}{\epsilon H}.
$$

The factor $\epsilon$ is fixed by requiring the chained system to reproduce the one-stage model's behaviour. Three identical stages in series each acting on timescale $\epsilon\tau$ compose into an aggregate relaxation governed by $\tau$ when $\epsilon = 1/\sqrt 3$; this choice makes the third-order operator below reduce to the correct single timescale and preserves the equilibrium response, as the prefactors verify when the chain is collapsed.
```

with $\epsilon = 1/\sqrt{3}$ chosen so that the chain preserves both the equilibrium response and the e-folding behavior of the one-stage model. Each equation is the same mass bookkeeping as the one-stage reservoir, linearized; the left sides drain each reservoir on the timescale $\epsilon\tau$, and the right sides are the fluxes passed down the chain. Eliminating $h'$ and $F'$ gives a single third-order equation,

$$
\left(\frac{d}{dt}+\frac{1}{\epsilon\tau}\right)^{3} L' = \frac{L}{H}\,\frac{\dot b'}{\epsilon\,(\epsilon\tau)^{2}},
$$

```{admonition} Derivation
:class: dropdown

Write $\mathcal D \equiv d/dt + 1/(\epsilon\tau)$ for the common reservoir operator, so each of the three equations reads $\mathcal D\,u = (\text{source})$. The three become

$$
\mathcal D\,h' = \dot b', \qquad
\mathcal D\,F' = \frac{L\,h'}{(\epsilon\tau)^2}, \qquad
\mathcal D\,L' = \frac{F'}{\epsilon H}.
$$

Eliminate the intermediate variables by applying $\mathcal D$ repeatedly. Act with $\mathcal D$ on the third equation and substitute the second,

$$
\mathcal D^2 L' = \frac{\mathcal D F'}{\epsilon H} = \frac{1}{\epsilon H}\,\frac{L\,h'}{(\epsilon\tau)^2}.
$$

Act with $\mathcal D$ once more and substitute the first,

$$
\mathcal D^3 L' = \frac{1}{\epsilon H}\,\frac{L\,\mathcal D h'}{(\epsilon\tau)^2}
= \frac{L}{\epsilon H\,(\epsilon\tau)^2}\,\dot b'.
$$

Restoring the explicit operator, $\mathcal D^3 = (d/dt + 1/\epsilon\tau)^3$,

$$
\left(\frac{d}{dt}+\frac{1}{\epsilon\tau}\right)^3 L' = \frac{L}{H}\,\frac{\dot b'}{\epsilon\,(\epsilon\tau)^2}.
$$

The three reservoirs in series collapse to a single third-order equation with a triply repeated root at $-1/(\epsilon\tau)$. A repeated root is what produces the delayed, sigmoidal onset of the next solution, in contrast to the single root and immediate exponential response of the one-stage model.
```

whose response to a step change in balance is sigmoidal rather than exponential,

$$
L'(t) = L'_{\mathrm{eq}}\left[1 - e^{-t/\epsilon\tau}\left(1 + \frac{t}{\epsilon\tau} + \frac{1}{2}\left(\frac{t}{\epsilon\tau}\right)^{2}\right)\right].
$$

```{admonition} Derivation
:class: dropdown

For a step change $\dot b'$ is constant for $t>0$, so the forcing on the right of the third-order equation is constant. The equilibrium response $L'_{\mathrm{eq}}$ is the particular solution found by dropping the time derivatives, which leaves $(1/\epsilon\tau)^3 L'_{\mathrm{eq}} = (L/H)\dot b'/[\epsilon(\epsilon\tau)^2]$, that is $L'_{\mathrm{eq}} = (L/H)\,\dot b'\,\tau$, the same equilibrium the one-stage model gives. Write $s = t/(\epsilon\tau)$ for the dimensionless time. The deviation $y = L' - L'_{\mathrm{eq}}$ satisfies the homogeneous equation

$$
\left(\frac{d}{ds}+1\right)^3 y = 0,
$$

whose triply repeated root at $-1$ gives the general solution $y = (c_0 + c_1 s + c_2 s^2)\,e^{-s}$, the polynomial prefactor being the signature of the repeated root.

The constants follow from the initial conditions. Because the forcing enters only the third derivative, a step leaves the length and its first two time derivatives continuous and zero at $t=0$: $L'(0)=0$, $\dot L'(0)=0$, $\ddot L'(0)=0$. These translate to $y(0) = -L'_{\mathrm{eq}}$, $y'(0)=0$, $y''(0)=0$. Evaluating $y$ and its first two derivatives at $s=0$,

$$
y(0)=c_0, \quad
y'(0)=c_1-c_0, \quad
y''(0)=2c_2-2c_1+c_0,
$$

and setting these to $-L'_{\mathrm{eq}}, 0, 0$ gives $c_0 = -L'_{\mathrm{eq}}$, $c_1 = c_0 = -L'_{\mathrm{eq}}$, and $c_2 = (2c_1 - c_0)/2 = -L'_{\mathrm{eq}}/2$. Hence

$$
y(s) = -L'_{\mathrm{eq}}\left(1 + s + \tfrac12 s^2\right)e^{-s},
$$

and $L' = L'_{\mathrm{eq}} + y$ gives the quoted solution after restoring $s = t/(\epsilon\tau)$. Near $t=0$ the bracket cancels to second order, so the terminus barely moves while the flux anomaly is still propagating down the chain; only once the polynomial growth is overtaken by the decaying exponential does the length climb to its equilibrium, producing the sigmoid.
```

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

```{admonition} Derivation
:class: dropdown

The exponents follow from the shallow-ice flux of {doc}`../ice_flow/shallow-ice` evaluated with the reservoir's reduced geometry. The depth-integrated deformational flux scales as

$$
q \sim H^{n+2}\,|\nabla s|^{n},
$$

where $H$ is the thickness, $n$ the Glen exponent, and $\nabla s$ the surface slope; the thickness power $n+2$ comes from integrating the Glen-law shear $\dot\varepsilon \propto \tau^n$ with $\tau \propto H|\nabla s|$ through the depth. In the lumped reservoir the surface slope is not resolved but represented by its mean magnitude, the thickness drop spread over the length, $|\nabla s| \sim H/L$. Substituting,

$$
Q \sim H^{n+2}\left(\frac{H}{L}\right)^n = \frac{H^{2n+2}}{L^n}.
$$

Matching to $Q = \nu\,H^\alpha/L^\gamma$ identifies $\alpha = 2n+2$ and $\gamma = n$ for deformation-dominated flow, with $\nu$ collecting the rate factor and the dimensional constants of the flux integral. When basal sliding rather than internal deformation carries most of the flux the thickness enters less steeply, so both exponents are smaller; the sliding case is bracketed by the same construction with a sliding rather than a deformation flux law. The thickness dependence is strongly superlinear and the length dependence inverse, so a thickening interior drives more flux toward the margin while a lengthening one at fixed thickness drives less.
```

with $\alpha = 2n+2$ and $\gamma = n$ for deformation-dominated flow, and smaller exponents when sliding dominates; the constant $\nu$ absorbs the rate factor and the geometry. The interior flux increases steeply with thickness and decreases with length, so a thickening interior pushes more ice toward the margin and a lengthening one, at fixed thickness, pushes less.

The *grounding-zone flux* $Q_g$ is the rate at which ice is exported across the grounding line. Flotation ties the thickness there to the bed, since ice of density $\rho_i$ floats in water of density $\rho_w$ when its thickness falls below $-\lambda b$, where $b(x)$ is the bed elevation, negative below sea level, and $\lambda = \rho_w/\rho_i \approx 1.1$. The grounding-line thickness is therefore not free but pinned to the local bed,

$$
h_g = -\lambda\, b(L),
$$

```{admonition} Derivation
:class: dropdown

The grounding line is the point where the ice is exactly at flotation, neither pressing on the bed nor lifted off it. Flotation is hydrostatic balance: a column of ice of thickness $h$ floats when its weight equals the weight of the water it displaces. If the bed sits at elevation $b$, negative below sea level, the column extends from the bed up to the surface, and the submerged portion has depth $-b$ (the bed depth below sea level). Balancing the weight of the full ice column against the buoyancy of the displaced water,

$$
\rho_i\,g\,h = \rho_w\,g\,(-b),
$$

where $\rho_i$ and $\rho_w$ are the densities of ice and water and $g$ is gravity. Solving for the thickness at flotation,

$$
h_g = \frac{\rho_w}{\rho_i}\,(-b) = -\lambda\,b,
\qquad \lambda \equiv \frac{\rho_w}{\rho_i} \approx 1.1.
$$

Evaluated at the grounding-line position $x = L$, this gives $h_g = -\lambda\,b(L)$. The grounding-line thickness is therefore not a free variable but is pinned to the bed depth there: a grounding line standing in deeper water (more negative $b$) must carry thicker ice. This pinning is what couples grounding-line migration to the bed topography and, through the flux law below, drives the marine instability.
```

and the boundary-layer analysis of the shallow-shelf equations, due to Schoof {cite}`schoof2007` and presented with the ice-sheet material in {doc}`../cryosphere/ice-sheets`, shows that the flux across the grounding line is controlled almost entirely by this one number,

$$
Q_g = \Omega\, h_g^{\beta},
\qquad \beta = \frac{m+n+3}{m+1} \approx 4.75
$$

```{admonition} Derivation
:class: dropdown

This flux law is a cited result, not one derived here. It comes from the boundary-layer analysis of the grounding zone by Schoof {cite}`schoof2007`, presented with the ice-sheet material in {doc}`../cryosphere/ice-sheets`. Its origin and the meaning of the exponent are worth stating without reproducing the asymptotics.

Near the grounding line the ice transitions over a short distance from bed-supported flow, in which basal friction balances the driving stress, to freely floating shelf flow, in which longitudinal stretching balances it. Schoof showed that this transition occupies a thin boundary layer whose internal structure selects a unique flux for a given grounding-line thickness, so that $Q_g$ is not free but is fixed by $h_g$ alone (with the buttressing of any downstream shelf folded into the prefactor). Matching the boundary-layer solution to the interior yields a power law $Q_g = \Omega\,h_g^{\beta}$.

The exponent combines the Glen flow exponent $n$ and the Weertman sliding exponent $m$ from the two stress balances the boundary layer reconciles,

$$
\beta = \frac{m + n + 3}{m + 1}.
$$

For the standard values $n = 3$ and $m = 1/3$ this gives $\beta = (1/3 + 3 + 3)/(1/3 + 1) = (19/3)/(4/3) = 19/4 \approx 4.75$. The prefactor $\Omega$ collects the rate factor, the friction coefficient, and any ice-shelf buttressing, and it is the channel through which ocean forcing acts: shelf thinning or grounding-zone melt raises $\Omega$. The large exponent is the consequential feature. With $\beta \approx 5$ the export is extraordinarily sensitive to grounding-line thickness, so the small thickness changes that accompany grounding-line migration across a sloping bed produce large changes in discharge.
```

for Glen exponent $n=3$ and Weertman friction exponent $m=1/3$. The prefactor $\Omega$ collects the rate factor, the friction coefficient, and the buttressing supplied by an ice shelf, and it is the handle through which the ocean grips the system; shelf thinning or grounding-zone melt acts on the ice sheet by raising $\Omega$. The exponent is the important number. With $\beta \approx 5$, a ten percent increase in grounding-line thickness nearly doubles the export, so small migrations of the grounding line across a sloping bed produce large changes in discharge. A steady state is a geometry in which these fluxes balance the surface input; with accumulation rate $P$ over a reservoir of length $L$, steadiness requires $P\,L = Q = Q_g$, two conditions that on a given bed select the equilibrium thickness $\bar H$ and grounding-line position $\bar L$.

## The two-stage model for marine ice streams

With the fluxes in hand the marine model needs two state variables, the mean interior thickness $H$ and the grounding-line position $L$, with $x$ measured seaward from the divide. The derivation is mass conservation applied twice {cite}`robel2018`. Applied to the whole reservoir, of volume $V \approx HL$ per unit width, conservation reads

$$
\frac{dV}{dt} = P\,L - Q_g,
$$

```{admonition} Derivation
:class: dropdown

This is mass conservation for the whole grounded reservoir, integrated over its length. Per unit width the reservoir holds a volume $V \approx H L$, the mean interior thickness times the grounding-line position. Its mass changes only through what the surface adds and what the boundary removes. The surface gains ice at the accumulation rate $P$ over the full length $L$, contributing $P L$ per unit width. The reservoir has no other input, and its only outlet is across the grounding line, where ice is exported at the grounding-zone flux $Q_g$. There is no terminus ablation wedge as in the land-terminating case, because the export is concentrated at the grounding line. Summing input and output,

$$
\frac{dV}{dt} = P\,L - Q_g.
$$

This is the marine counterpart of the volume budget $dV/dt = \bar Y L_0 \dot b_1 - Y_t \dot a_0 L_1$ of the land-terminating model, with distributed accumulation replacing the balance perturbation and a single grounding-line flux replacing the terminus ablation. Combined with the grounding-line equation it yields the interior thickness equation below, and at steady state it reduces to $P L = Q_g$.
```

since snowfall supplies $PL$ and the only export is across the grounding line. Applied to the grounding zone alone, conservation determines how the grounding line moves; advancing it by $dL$ requires filling a column of thickness $h_g$ with ice, and the ice available is the difference between what the interior delivers and what the grounding line exports, so

$$
\frac{dL}{dt} = \frac{Q - Q_g}{h_g}.
$$

```{admonition} Derivation
:class: dropdown

This is mass conservation applied to the grounding zone, the narrow region immediately upstream of the grounding line. Consider the rate at which ice enters and leaves that region. The interior delivers ice into it at the interior flux $Q$, and the grounding line exports ice out of it at the grounding-zone flux $Q_g$, both per unit width. The net rate of mass accumulation in the grounding zone is therefore $Q - Q_g$.

That surplus advances the grounding line. Moving the grounding line seaward by $dL$ requires filling a new ice column at the flotation thickness $h_g$, a volume $h_g\,dL$ per unit width. Equating the volume gained to the net mass supplied,

$$
h_g\,\frac{dL}{dt} = Q - Q_g,
\qquad\Longrightarrow\qquad
\frac{dL}{dt} = \frac{Q - Q_g}{h_g}.
$$

The grounding line advances when the interior delivers more than the grounding line can export ($Q > Q_g$) and retreats when the export outpaces delivery ($Q < Q_g$). Because $h_g$ appears in the denominator and the grounding zone is thin, modest flux imbalances move the grounding line quickly, which is the origin of the fast eigenmode identified after the model is linearized.
```

Expanding $dV/dt = H\,dL/dt + L\,dH/dt$ and combining the two statements gives the interior equation,

$$
\frac{dH}{dt} = P - \frac{Q_g}{L} - \frac{H}{h_g L}\left(Q - Q_g\right),
$$

```{admonition} Derivation
:class: dropdown

Combine the reservoir mass balance with the grounding-line equation. The reservoir volume per unit width is $V = H L$, so by the product rule

$$
\frac{dV}{dt} = H\,\frac{dL}{dt} + L\,\frac{dH}{dt}.
$$

The whole-reservoir balance states $dV/dt = P L - Q_g$. Equating the two expressions for $dV/dt$ and solving for the thickness rate,

$$
L\,\frac{dH}{dt} = P L - Q_g - H\,\frac{dL}{dt}.
$$

Substitute the grounding-line equation $dL/dt = (Q - Q_g)/h_g$,

$$
L\,\frac{dH}{dt} = P L - Q_g - \frac{H}{h_g}\,(Q - Q_g),
$$

and divide through by $L$,

$$
\frac{dH}{dt} = P - \frac{Q_g}{L} - \frac{H}{h_g L}\,(Q - Q_g).
$$

The first term is accumulation, the second the export drawn from the reservoir, and the third a geometric correction: as the grounding line moves it changes the reservoir length over which the fixed volume is spread, thinning or thickening the interior even at constant mass. At a steady state $dL/dt = 0$ forces $Q = Q_g$, the third term vanishes, and $dH/dt = 0$ then requires $P L = Q_g$, recovering the flux balance $P L = Q = Q_g$.
```

in which the first two terms are accumulation against export and the third is the geometric correction for the moving boundary. These two equations are the two-stage model, and at a steady state they reduce exactly to the flux balance $PL = Q = Q_g$. Linearized about that steady state, the system has two eigenvalues and therefore two e-folding timescales, and they are far apart. The fast mode, decades to a few centuries, is the grounding zone adjusting toward flux balance at nearly fixed interior thickness; it is fast because the grounding zone is thin, so modest flux imbalances move it quickly. The slow mode, of order millennia, is the interior thickness relaxing, the marine analog of $t_r = H/\dot a_0$, slow because the interior is thick and the balance fluxes small. A perturbed marine ice stream therefore shows a quick partial response followed by a long completion, and it can sit far from equilibrium for centuries while appearing superficially quiet.

## Sensitivity to climate forcing

The reduced model's value is that the sensitivity of the steady state can be written down rather than mapped numerically. Climate forcing enters through two parameters, the accumulation rate $P$ for the atmosphere and the grounding-zone coefficient $\Omega$ for the ocean, since melt at the grounding zone and the thinning of a buttressing shelf both act by raising $\Omega$. Differentiating the steady-state balance $\Omega\, h_g(L)^{\beta} = P\,L$ logarithmically gives the response of the grounding line to small changes in either,

$$
\frac{\delta \bar L}{\bar L} = \frac{1}{\Sigma}\left(\frac{\delta P}{P} - \frac{\delta \Omega}{\Omega}\right),
\qquad
\Sigma \equiv \beta\,\frac{\bar L\, h_g'(\bar L)}{\bar h_g} - 1,
$$

```{admonition} Derivation
:class: dropdown

Start from the steady-state flux balance, in which the grounding-line export equals the total accumulation delivered over the reservoir,

$$
\Omega\,h_g(L)^{\beta} = P\,L,
$$

with $h_g(L) = -\lambda\,b(L)$ a known function of the grounding-line position through the bed. Take the logarithm of both sides,

$$
\ln\Omega + \beta\,\ln h_g(L) = \ln P + \ln L,
$$

and differentiate, allowing small changes in the forcings $P$ and $\Omega$ and the resulting small change $\delta L$ in the equilibrium grounding-line position. Using $d(\ln\Omega) = \delta\Omega/\Omega$, $d(\ln P) = \delta P/P$, $d(\ln L) = \delta L/L$, and $d(\ln h_g) = (h_g'/h_g)\,\delta L$ where $h_g'(L) = dh_g/dL$,

$$
\frac{\delta\Omega}{\Omega} + \beta\,\frac{h_g'}{h_g}\,\delta L
= \frac{\delta P}{P} + \frac{\delta L}{L}.
$$

Collect the $\delta L$ terms on one side and divide by $\bar L$ to make them fractional, evaluating at the steady state (overbars),

$$
\left(\beta\,\frac{\bar L\,h_g'(\bar L)}{\bar h_g} - 1\right)\frac{\delta\bar L}{\bar L}
= \frac{\delta P}{P} - \frac{\delta\Omega}{\Omega}.
$$

The bracket is precisely the stability number $\Sigma$. Dividing through by it gives the quoted sensitivity,

$$
\frac{\delta\bar L}{\bar L} = \frac{1}{\Sigma}\left(\frac{\delta P}{P} - \frac{\delta\Omega}{\Omega}\right).
$$

The signs are physical. More accumulation ($\delta P > 0$) advances the grounding line; a larger export coefficient ($\delta\Omega > 0$), from shelf thinning or grounding-zone melt, retreats it. The gain $1/\Sigma$ sets the amplification. On a strongly prograde bed $h_g'(\bar L) > 0$ is large, $\Sigma$ is large and positive, the gain is small, and the grounding line is stiff, because any advance is opposed by the steeply rising export $\Omega h_g^\beta$. As the bed flattens at the grounding line $h_g' \to \bar h_g/(\beta\bar L)$ from above, the bracket tends to zero, $\Sigma \to 0^+$, and the sensitivity diverges; when the slope reverses $h_g' < 0$, $\Sigma < 0$, and no stable equilibrium exists, the marine ice-sheet instability.
```

where $h_g'(L) = -\lambda\, b_x(L)$ is the rate at which the flotation thickness grows as the grounding line advances, set entirely by the bed slope $b_x = db/dx$. The dimensionless number $\Sigma$ controls everything. On a strongly prograde bed, one that deepens seaward so that $b_x < 0$ and $h_g' > 0$, $\Sigma$ is large and positive, the gain $1/\Sigma$ is small, and the grounding line is stiff against forcing, since any advance is opposed by the steeply rising export $\Omega h_g^\beta$. The same number governs stability. The slow mode of the linearized system decays at a rate proportional to $\Sigma$, so steady states with $\Sigma > 0$ are stable and steady states with $\Sigma < 0$ are not.

The stochastic counterpart of this sensitivity matters as much as the deterministic one. Driven by the broadband natural variability of ocean temperature, the two-stage system is the marine version of the red-noise filter described above for mountain glaciers; it integrates the forcing, amplifies it at the slow eigenfrequency, and produces grounding-line excursions that are large, slow, and persistent {cite}`hasselmann1976`. A marine ice stream in a statistically steady climate can sustain kilometer-scale grounding-line fluctuations on multi-centennial timescales from noise alone, which is why a decade of observed retreat, by itself, cannot distinguish forced change from natural variability, and why formal attribution requires the noise statistics these models supply.

## Reverse bed slopes and the approach to instability

The asymptotic behavior of the gain $1/\Sigma$ as the bed slope is varied is the cleanest route into the book's instability discussion. Hold the climate fixed and flatten the bed at the grounding line, so that $h_g' \to h_g/(\beta L)$ from above and $\Sigma \to 0^+$. Three things happen together. The sensitivity $1/\Sigma$ of the steady state diverges, so ever-smaller changes in ocean or atmosphere produce ever-larger equilibrium migrations. The slow eigenvalue, proportional to $\Sigma$, goes to zero, so the system takes arbitrarily long to settle, the critical slowing that in observed systems precedes a bifurcation. And the steady state's basin of attraction shrinks, so finite fluctuations of the kind the stochastic forcing supplies become capable of dislodging the system entirely.

When the slope reverses, $b_x > 0$ at the grounding line, the bed deepening inland, the flotation thickness *increases* as the grounding line retreats, $h_g' < 0$, and $\Sigma$ is negative for any $\beta > 0$. No stable steady state exists on such a slope. A retreat into deeper water raises $h_g$, which raises the export $\Omega h_g^\beta$ by more than it raises the supply, which draws the interior down and retreats the grounding line further, and the feedback closes on itself without any new physics. This is the marine ice-sheet instability, obtained here from two mass reservoirs and a flux rule, with no stress balance anywhere in the argument, which is the strongest available evidence that the instability is at root a statement about mass conservation over a bed that deepens inland. A grounding line perturbed off the end of a retrograde reach does not stop until it finds the next prograde slope, the origin of the hysteresis and the discrete stable positions explored, with the full mechanical story, buttressing, and the observational case for the Amundsen Sea glaciers, in {doc}`../cryosphere/ice-sheets`, and of the oscillatory variants in {doc}`../cryosphere/instabilities`. The lab accompanying this chapter exhibits the asymmetry directly, the two-stage model relaxing to a new steady state when forced on a prograde bed and running away when forced on a retrograde one, and the full stress-balance version of the same experiment is carried out in icepack in {doc}`../modeling/ice-stream-vaf-lab`.

These reduced models earn their place in the book because they convert the prognostic problem's most expensive questions, how sensitive, how fast, how close to the edge, into algebra. The full models of {doc}`../modeling/prognostic-problem` remain the instruments of projection, but the one-, two-, and three-stage systems are how the projections are understood, attributed, and stress-tested, and they are the lens through which {doc}`../cryosphere/ice-sheets` and {doc}`../cryosphere/instabilities` are best read.
