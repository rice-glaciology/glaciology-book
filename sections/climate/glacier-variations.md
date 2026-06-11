# Glacier variations and response time

In 1905 a survey party photographed Lillian Glacier in the Olympic Mountains as a healthy body of ice filling its cirque. A photograph from the same vantage in 2010 shows bare rock and a few snow patches. Between the two images lies a century of climate, filtered through the dynamics of a small mountain glacier. This chapter builds the simplest theory that connects the two photographs. It asks how far a glacier's terminus moves when its mass balance changes, and how long the move takes. The answers come from the mass balance ideas of {doc}`../ice_flow/mass-balance` applied to a glacier that is allowed to change its length, and they are developed in Chapter 11 of {cite}`cuffey2010`.

The theory in this chapter is deliberately kinematic. We will not solve the stress balance at all. Everything follows from conservation of mass and a little geometry, which is why the results are so portable, and the price of that simplicity is that the dynamics of the flow appear only through a single number, the thickness of the ice.

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

```{figure} figures/terminus-flux-wedge.svg
:name: fig-terminus-flux-wedge
:width: 85%

The equilibrium length response. A persistent mass-balance perturbation delivers an extra flux $\langle \dot b_1 \rangle L_0$ to the old terminus, and the glacier advances by $L_1$ until ablation at the rate $\dot a_0$ over the new wedge consumes it. Redrawn after Chapter 11 of {cite}`cuffey2010`.
```

A modest perturbation produces a substantial advance. With a terminus ablation rate of $5\ \mathrm{m\,yr^{-1}}$, a balance increase of only $0.5\ \mathrm{m\,yr^{-1}}$ moves the terminus forward by a tenth of the glacier's length. The terminus is a lever arm, and small persistent changes in climate are amplified into conspicuous changes in length. This is the first reason glacier termini make such legible climate records.

Geometry sets the gain of the lever. If the glacier drains a wide accumulation basin into a narrow tongue, the same balance perturbation collected over the broad upper glacier must be disposed of along a slim terminus, and the advance grows by the ratio of the mean width $\bar Y$ to the terminus width $Y_t$,

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

```{figure} figures/response-time-curve.svg
:name: fig-response-time-curve
:width: 80%

Length adjustment after a step change in mass balance. The terminus approaches its new equilibrium exponentially, 63% of the way there after one response time $t_r = H/\dot a_0$ and 86% after two {cite}`johannesson1989`.
```

The numbers this formula produces are the useful surprise. A glacier on Mount Rainier with $H = 100$ m and a terminus ablation rate of $10\ \mathrm{m\,yr^{-1}}$ has $t_r = 10$ years. An ice sheet with $H = 1500$ m losing $1\ \mathrm{m\,yr^{-1}}$ at its margin has $t_r = 1500$ years. Mountain glaciers remember a few decades of climate. Ice sheets remember millennia, which is why their present shape still carries the imprint of the last glacial period, a thread we pick up again in {doc}`paleoclimate`. Thick glaciers in cold, dry climates respond slowly. Thin glaciers with high terminus ablation, the maritime glaciers of Norway and New Zealand among them, respond within a decade or two.

## Glaciers as filters of climate

The step response is a Green's function in disguise, and once we have it, the response to any climate history follows by superposition. Two consequences deserve emphasis because they shape how length records must be read.

The first is that a glacier converts noisy climate into smooth, persistent length fluctuations. Interannual mass-balance variability is essentially white noise, a few tenths of a meter to a couple of meters water equivalent from year to year with little memory. Run that noise through the first-order equation above and the length performs slow, red-noise wanderings of a kilometer or more over decades, even with no climate trend at all. A wandering terminus is therefore not, by itself, evidence of climate change. The South Cascade Glacier mass-balance record, the longest in North America, looks like noise about a weak trend, while the length record of the same glacier is a smooth monotonic retreat. Both views are honest; the glacier has simply integrated the one into the other.

The second consequence is lag. During a steady warming ramp the terminus chases an equilibrium that keeps receding ahead of it, and the gap between the actual length and the equilibrium length grows with $t_r$. Stop the warming and the glacier keeps retreating until it closes that gap. This unrealized response is the **committed retreat**, and it can exceed the retreat already observed. For South Cascade Glacier, with $H = 200$ m, a terminus balance rate near $-5.4\ \mathrm{m\,yr^{-1}}$, and $t_r \approx 37$ years, the committed terminus position lies roughly two kilometers behind the present one even with no further warming. The steeper, thinner Nisqually Glacier on Mount Rainier, with $t_r \approx 12$ years, tracks its climate closely and has little retreat left in the bank.

Set against the natural variability envelope, the observed centennial retreat of glaciers worldwide, from Hintereisferner to Franz Josef to Nigardsbreen, lies far outside what red-noise wandering can produce, and Roe, Baker, and Herla turned exactly this comparison into a formal attribution, finding that the retreats of the last century are categorical evidence of regional climate change {cite}`roe2017,leclercq2014`. The humble first-order equation of this chapter is the engine of that argument.

```{admonition} A caveat about what $t_r$ hides
:class: warning

The kinematic model treats the glacier as a reservoir with a single thickness, and its response time is an e-folding scale, not a delay. It says nothing about how thickness anomalies propagate down-glacier, which is the business of kinematic waves, and it fails entirely for glaciers whose termini end in water, where calving opens a mass-loss channel with its own dynamics. Tidewater glaciers can advance and retreat on cycles almost decoupled from climate, the subject we take up with the flow instabilities in {doc}`../cryosphere/instabilities`.
```

## From mountain glaciers to ice sheets

For an ice sheet the terminus wedge of this chapter is the wrong picture. The margins of Antarctica mostly end in the ocean, mass leaves by calving and by melting at the base of floating ice shelves, and the stability question is governed by the geometry of the bed at the grounding line rather than by surface ablation at a terminus. The response-time logic survives, but the mechanism changes, and the change is consequential enough to deserve its own chapter, {doc}`../cryosphere/ice-sheets`.
