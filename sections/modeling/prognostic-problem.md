# The prognostic problem

The chapters on shallow ice, mass balance, glacier response times, ice sheets, and paleoclimate have all treated the geometry of an ice body as something either fixed or changing in one lumped, averaged sense. Even the full Vialov derivation of {doc}`../ice_flow/mass-balance` asked for the shape a climate *produces*, not for the shape that will *emerge* as a climate changes. That is a diagnostic question, and it has a one-time answer. The prognostic question is different. Given the ice today, given the climate it will experience, what shape will it have tomorrow, next century, next glacial cycle? That is a movie, not a photograph, and making the movie is what this chapter is about.

## The prognostic loop

The diagnostic problem is a snapshot. Given the ice thickness $H(\mathbf{x})$ and bed elevation $b(\mathbf{x})$ everywhere, solve for the velocity $\bar{u}(\mathbf{x})$. The shallow-ice expression from {doc}`../ice_flow/shallow-ice` gives the answer analytically; icepack's variational solvers give it for more complex flow models. The velocity is a function of the current geometry alone, and once it is found the calculation is complete.

The prognostic problem uses that velocity to step the geometry forward. The bridge between the two is the depth-integrated mass-conservation equation derived in {doc}`../ice_flow/mass-balance`,

$$
\frac{\partial H}{\partial t} = \dot a - \nabla\!\cdot\!\left(\bar{u}\,H\right),
$$

where $\dot a(\mathbf{x},t)$ is the net surface and basal mass balance. Given $H$ at time $t$, one diagnostic solve supplies $\bar{u}$, and the right-hand side then tells us how fast each column of ice is thickening or thinning. A small step $\Delta t$ forward gives a new $H$, the geometry has changed, and the diagnostic problem must be solved again for the new geometry. Repeat enough times and the photograph becomes a movie.

The simplest prognostic model is therefore a two-step loop: transport the thickness, then re-solve for the velocity. Everything that follows in this chapter is a discussion of how to do those two steps correctly, how to check that the loop is producing sensible answers, and what it means to start the loop from the right initial condition.

% lab (prognostic, icepack): SIA forward loop — step H, re-solve diagnostic velocity, watch Vialov emerge

## The thickness equation as a nonlinear diffusion

Before writing a single line of code it is worth understanding what kind of equation the thickness evolution is, because its character determines how it must be solved numerically.

In the shallow-ice approximation the depth-averaged flux is

$$
\mathbf{q} = \bar{u}\,H = \left(\frac{2A(\rho_i g)^n}{n+2}\,H^{n+2}\,\left|\frac{\partial s}{\partial x}\right|^{n-1}\right)\left(-\frac{\partial s}{\partial x}\right),
$$

where $s = H + b$ is the surface elevation and $b$ is the (fixed) bed. On a flat bed $s = H$, so $\partial s/\partial x = \partial H/\partial x$, and the flux can be written as $\mathbf{q} = -D\,\nabla H$ where the diffusivity is

$$
D(H,\,\nabla s) = \frac{2A(\rho_i g)^n}{n+2}\,H^{n+2}\,|\nabla s|^{n-1}.
$$

```{admonition} Deriving the SIA diffusivity
:class: dropdown

Start from the depth-averaged shallow-ice velocity (no sliding),

$$
\bar{u} = \frac{2A(\rho_i g)^n}{n+2}\,H^{n+1}\left|\frac{\partial s}{\partial x}\right|^{n-1}\!\left(-\frac{\partial s}{\partial x}\right).
$$

Multiply both sides by $H$ to get the flux $q = \bar{u}H$, then factor out $(-\partial s/\partial x)$:

$$
q = \underbrace{\frac{2A(\rho_i g)^n}{n+2}\,H^{n+2}\,\left|\frac{\partial s}{\partial x}\right|^{n-1}}_{D(H,\,\partial s/\partial x)}\left(-\frac{\partial s}{\partial x}\right).
$$

Because $q = -D\,\partial s/\partial x$ and, on a flat bed, $\partial s/\partial x = \partial H/\partial x$, substituting into $\partial H/\partial t = \dot a - \partial q/\partial x$ gives the nonlinear diffusion form

$$
\frac{\partial H}{\partial t} = \dot a + \frac{\partial}{\partial x}\!\left(D\,\frac{\partial H}{\partial x}\right).
$$

The diffusivity $D \propto H^{n+2}|\nabla s|^{n-1}$ is not constant — it depends on the solution itself, which is what makes the equation nonlinear.
```

With $n = 3$, the diffusivity scales as $H^5$ and $|\nabla s|^2$. These are steep exponents. Where the ice is thick the equation diffuses rapidly and bumps in the surface spread outward; where the ice is thin, especially at the margins where $H \to 0$, $D \to 0$ and the equation loses its diffusive character entirely. Near divides where $|\nabla s| \to 0$ the diffusivity vanishes for the same reason. Both limits create numerical difficulties. At the margin, the ice front can become numerically smeared unless the thickness is constrained to stay non-negative. At the divide, $D = 0$ means no diffusion acts, yet the slope is genuinely zero and the ice still has to be able to flow outward. Both problems have well-understood remedies, discussed in {cite}`bueler2009` and {cite}`greve2009`.

If accumulation piles up a ridge in the surface, the diffusion term will spread it laterally; a hollow will fill. The rate at which this happens scales nonlinearly with the ridge height and slope. An ice sheet with its broad flat interior and steep margins is not, thermally speaking, in a diffusive equilibrium; it is the shape that a *strongly nonlinear* diffusion reaches under a climate forcing, as the Vialov derivation made precise.

## Time stepping

Given the nonlinear diffusion form, how should the equation be stepped forward in time?

The simplest choice is the **explicit Euler** method. At each step, evaluate the right-hand side from the current thickness field and advance,

$$
H^{k+1} = H^k + \Delta t\left[\dot a - \nabla\!\cdot\!\left(\bar{u}^k\,H^k\right)\right].
$$

The scheme is trivially simple to code and requires only one diagnostic solve per step. Its flaw is the diffusive **CFL condition**, the stability requirement that

$$
\Delta t \lesssim \frac{\Delta x^2}{2D_{\max}}.
$$

Since $D \propto H^5$ in the SIA, a modest doubling of the ice thickness tightens the stability limit by more than thirty times. Near fast-flowing outlet glaciers, where $D$ can be orders of magnitude larger than in the interior, the explicit time step shrinks to years or less even when the century-scale evolution is what we care about. The equation is **stiff** in the numerical sense, meaning the stability constraint is far more demanding than the accuracy needs. The practical consequence is that an explicit scheme is often unusable for whole-ice-sheet simulations at reasonable resolution.

### The staggered-grid update and its stability cost

Writing out the discrete update makes the stability constraint concrete. On a 1-D staggered grid, the thickness $H_i$ lives at cell centers and the flux $q_{i+1/2}$ lives at cell edges (half-integer indices). The diffusivity is interpolated to the same edge locations before computing the flux, so that

$$
q_{i+1/2} = -D_{i+1/2}\,\frac{H_{i+1} - H_i}{\Delta x}, \qquad D_{i+1/2} = \tfrac{1}{2}\!\left(D_i + D_{i+1}\right).
$$

Evaluating everything at time level $k$ and advancing one step gives the fully explicit update for each interior cell,

$$
H_i^{k+1} = H_i^k + \frac{\Delta t}{\Delta x}\!\left(q_{i+1/2}^k - q_{i-1/2}^k\right) + \Delta t\,\dot a_i.
$$

This is the entire time-stepping kernel for the SIA prognostic problem in one dimension. The staggered placement of the diffusivity is not cosmetic. If both $H$ and $D$ shared cell-center locations, the discrete diffusion operator would develop a two-grid instability, decoupling odd and even nodes into independent sub-grids. Staggering suppresses that mode and is the standard practice in finite-difference SIA codes {cite}`bueler2009`.

Now substitute real numbers to see the stability cost. Take $H = 1000$ m and a surface slope of $1^\circ$, so $|\nabla s| = \tan 1^\circ \approx 0.0175$. With $A = 2.4\times10^{-24}\ \mathrm{Pa}^{-3}\ \mathrm{s}^{-1}$, $\rho_i = 917\ \mathrm{kg\ m}^{-3}$, $g = 9.81\ \mathrm{m\ s}^{-2}$, and $n = 3$, the diffusivity evaluates to

$$
D = \frac{2A(\rho_i g)^3}{5}\,H^5\,|\nabla s|^2 \approx \frac{2 \times 2.4\times10^{-24} \times (9000)^3}{5}\,(10^3)^5\,(0.0175)^2 \approx 2000\ \mathrm{m}^2\ \mathrm{yr}^{-1}.
$$

At $\Delta x = 1\ \mathrm{km}$ the CFL limit is

$$
\Delta t \lesssim \frac{(10^3)^2}{2 \times 2000} = 250\ \mathrm{yr}.
$$

That looks generous, but coarsening to $\Delta x = 1\ \mathrm{km}$ is already too coarse to capture outlet-glacier dynamics. At $\Delta x = 100\ \mathrm{m}$, a resolution where outlet glaciers are marginally resolved, the same formula gives

$$
\Delta t \lesssim \frac{(100)^2}{2 \times 2000} = 2.5\ \mathrm{yr}.
$$

Halving the grid spacing tightens the stability limit by four. Halving it again tightens by four again. The total work to advance the solution to a fixed end time therefore scales as the number of grid cells times the number of time steps, and because $N \propto 1/\Delta x$ and $\Delta t \propto \Delta x^2$, the number of steps scales as $1/\Delta x^2$. Work per unit of model time scales as $N / \Delta t \propto \Delta x^{-3}$ in 1-D. Concretely, going from $\Delta x = 1\ \mathrm{km}$ to $\Delta x = 100\ \mathrm{m}$ is a factor of ten in resolution and a factor of one thousand in computational cost, just from the stability constraint. In 2-D the scaling is $\Delta x^{-4}$, even worse. This quadratic coupling between grid spacing and time step is the fundamental reason that high-resolution explicit SIA integrations are impractical for multi-century projections.

The standard responses to stiffness are **implicit** and **semi-implicit** methods, which evaluate the diffusion term at the new time level $k+1$, or split between old and new, making the stability unconditional at the cost of a linear or nonlinear system solve per step. **Operator splitting** separates the diffusion from the balance term: one sub-step handles the diffusion implicitly at low accuracy, another handles the accumulation explicitly at higher accuracy, and the errors from the two sub-steps are controlled independently. In practice most operational ice-sheet models use some form of this split, evaluating $D$ at the old time level but centering or semi-implicitly treating the thickness in the diffusion term. The details are honestly messy, and the reader who needs them should go to Chapters 5 and 10 of {cite}`greve2009`.

What icepack's prognostic solver actually does each step is cleaner to describe. It solves the thickness transport equation using a finite-element discretization with a stabilized advection scheme to prevent spurious oscillations at the ice margin. The diagnostic velocity is re-solved after each thickness update using the current geometry. In the examples that follow, the two steps — transport $H$, solve for $\bar{u}$ — will be visible as explicit function calls, so the loop structure of the prognostic problem can be read directly in the code.

% lab (prognostic, icepack): explicit vs semi-implicit stepping; measure blowup time vs Δt for SIA slab

## The practical horizon of prognostic experiments

The stability analysis above carries a practical implication that shapes everything a glaciologist actually does with a prognostic model. It is not just a numerical nuisance; it reflects a real physical boundary on what prognostic experiments are honest to attempt.

Consider a modeler who wants to run a whole-ice-sheet simulation at outlet-glacier resolution, say $\Delta x = 500\ \mathrm{m}$. The stability constraint forces time steps of order a year or less. Running that model for ten thousand years — a typical glacial-cycle duration — requires ten thousand or more diagnostic velocity solves, each on a fine grid spanning the whole domain. On current hardware this is possible for 2-D flowline models but prohibitive for fully 3-D models without substantial algorithmic effort. The problem is not laziness; it is that the computational cost scales so steeply that the step from a coarse model to a fine one is not incremental but disruptive.

More fundamentally, there is an accuracy argument for staying within a roughly 100-to-1000-year window when making direct prognostic experiments. Three issues converge at that boundary.

The first is the time-step cost already described. At outlet-glacier resolution the model can step forward efficiently over decades to centuries, but running to millennia requires either coarsening the grid — sacrificing the resolution that motivated the exercise — or adopting implicit solvers that themselves demand careful validation.

The second is initialization drift. A model initialized from today's observed geometry is not, as discussed in the next section, in perfect internal balance. The drift from its initialized state toward whatever equilibrium the model prefers happens on a timescale of decades to centuries, set by the ice dynamics. For near-term projections this drift is a manageable nuisance to be quantified and corrected. For runs of many millennia, the accumulated drift can grow to a significant fraction of the total volume change, making it difficult to separate the response to forcing from the model's own internal adjustment.

The third is forcing uncertainty. Climate projections carried ten years forward are plausible, those carried a thousand years forward are scenarios, and those carried ten thousand years forward are thought experiments. The compounding uncertainty in the surface mass balance, ocean forcing, and geothermal heat flux means that a simulation run well beyond a thousand years is shaped more by assumptions about forcing than by the ice dynamics the model was designed to capture.

Together these three constraints mean that direct prognostic ice-sheet experiments live most honestly in the 100-to-1000-year window: short enough that drift is manageable and forcing can be prescribed with some defensibility, long enough to see the committed response work itself out. Longer timescales, where the ice sheet is itself part of the climate system and must be treated as a coupled component rather than a forced boundary, belong to a different class of model entirely — the reduced dynamical models taken up in the next chapter.

## Initialization and spin-up

Choosing the initial condition is not merely a technical detail; it shapes what the model can honestly claim to predict.

The conceptually cleanest initialization is **spin-up to steady state**. The procedure is straightforward to describe: hold the climate forcing fixed, start from a simple initial shape — a thin sheet of ice, or even bare bedrock — and run the model forward until the ice thickness field has stopped changing to within some tolerance. In practice the tolerance is stated as a volume tendency: spin-up is judged complete when the total volume rate of change $\partial V/\partial t$ falls below some fraction of the net surface mass balance, typically a few tenths of a percent. At that point the ice sheet is in approximate equilibrium with the forcing. The Vialov profile of {doc}`../ice_flow/mass-balance` is the analytic version of this; what a spin-up produces numerically for a real three-dimensional domain with real bed topography and a non-uniform accumulation field is the ice-sheet equivalent.

How long does spin-up take? The adjustment timescale is set by the ice dynamics and is roughly the ratio of the mean thickness to the mean accumulation rate — the same volume-balance argument that gives the response time of a simple glacier. For a large ice sheet with $H \sim 2000\ \mathrm{m}$ and $\dot a \sim 0.3\ \mathrm{m\ yr}^{-1}$, the timescale is of order $10^4$ years. In practice spin-up runs are often 50,000 to 100,000 model years, long enough for even the deepest, slowest parts of the thermodynamic state to equilibrate. This is expensive, which is why coarser-resolution models are usually used for spin-up even when the eventual projection experiment runs at higher resolution.

The limitation of spin-up is that the present-day cryosphere is not in equilibrium. Ice sheets carry the memory of their glacial-maximum extent, of the warming since the last glacial period, and of the recent anthropogenic forcing. A model that has spun up to equilibrium with a modern climate will arrive at a different geometry than the one observed. Driving the model with a full glacial-cycle forcing since 120,000 years ago can reduce this mismatch but requires assuming that the paleoclimate forcing is known, which is its own source of uncertainty.

The alternative is **assimilation-based initialization**, matching the model state directly to observed thickness and velocity at a chosen starting date. This forces the model to begin from a state that looks like today. The cost is that the thickness field produced by assimilation is not in balance with the model's velocity field; the mass budget does not close. When the model is released to run forward, it drifts away from the initialized state as it seeks its own internal equilibrium. This **initialization drift** can be larger than the signal of interest over the first decades of a projection, which is precisely the near-term period that sea-level projections care most about. Quantifying and minimizing initialization drift is an active research problem {cite}`cuffey2010`.

The choice between spin-up and assimilation is not a technical preference but a scientific one. Spin-up produces an internally consistent initial state whose geometry may not match observations; assimilation produces an observationally constrained state whose dynamics are initially inconsistent. Neither is strictly better, and modern practice often combines them — a long spin-up constrained by data assimilation to nudge the resulting geometry toward observations, with the residual drift characterized as part of the projection uncertainty.

Whatever initialization strategy is used, the model inherits a **committed response** even before any future forcing is applied. Just as the one-stage kinematic model of {doc}`../climate/glacier-variations` shows that a glacier can continue retreating for decades after warming stops, a three-dimensional model initialized from the present state will continue to evolve for centuries under fixed modern climate. This committed response is not a model error; it is a real feature of the physical system, and it is the first thing any projection experiment should document before adding future forcing.

% lab (prognostic, icepack): spin-up experiment — run from flat sheet to Vialov; compare to observed central thickness

## A worked example

Before turning to verification in the abstract, it is useful to see exactly what numbers emerge from the simplest possible prognostic experiment. Consider a 1-D synthetic domain: a 100 km flowline on a flat bed, driven by a uniform accumulation rate of $\dot a = 0.3\ \mathrm{m\ yr}^{-1}$, starting from a flat slab of $H = 10\ \mathrm{m}$. The analytic target is the Vialov profile, a dome with central thickness

$$
H_0 = \left(\frac{(n+2)\,\dot a}{2A(\rho_i g)^n}\right)^{1/(n+2)} L^{n/(n+2)} \approx 2800\ \mathrm{m}
$$

for $L = 50\ \mathrm{km}$ (half the domain width) and the standard parameter values.

At $\Delta x = 1\ \mathrm{km}$, the domain has 101 grid points. The diffusivity computed from the initial slab is negligibly small — $H$ is only 10 m, so $D \propto H^5 \approx 10^{10}\ \mathrm{m}^5$ in dimensional terms remains tiny — and the CFL limit is effectively set by how $D$ grows as the dome builds. After the first few hundred years, when the central thickness has grown to a few hundred metres, $D$ at the divide reaches roughly $10\ \mathrm{m}^2\ \mathrm{yr}^{-1}$ and the stable time step is of order 50 years. The model takes perhaps 200 steps to reach year 10,000 and the dome is clearly visible, though still well below its target height. By year 50,000 the central thickness is within a few percent of the Vialov value, and the volume tendency has fallen to less than $10^{-3}$ of the total accumulation flux — a reasonable spin-up criterion.

What does a student see at the command line? In the first thousand years the volume grows nearly linearly because the thin ice barely flows and accumulation dominates. Around year 5,000 the slopes steepen enough that the diffusivity jumps by an order of magnitude and the margins begin advancing rapidly. Between years 10,000 and 50,000 the dome inflates slowly toward its equilibrium shape, with the central tendency decaying roughly exponentially and the half-power of the volume tendency plotting as a nearly straight line on a semi-log axis. This visual — the volume tendency leveling off toward zero — is the diagnostic signature of spin-up converging, and it appears in every real model run of this type. The final geometry matches the Vialov formula to within a few percent at the center, with larger errors near the margin where the exact solution has a slope singularity that any finite-difference code smooths over.

This same experiment, run at $\Delta x = 100\ \mathrm{m}$, would require roughly $100\times$ more grid points and $100\times$ more time steps for the same 50,000-year integration — four orders of magnitude more work in total, from the $\Delta x^{-3}$ scaling derived earlier — and the answer would be essentially identical in the interior. This is why the verification problem is run at coarse resolution.

% lab (prognostic, icepack): 100 km Vialov spin-up; plot volume tendency decay and compare final profile to analytic

## Verification

A prognostic model is not trustworthy until it has been tested against cases with known answers. Glaciology offers a short but demanding list.

**The Vialov steady state** is the first and cleanest target. A flat-bed, no-sliding model fed a uniform accumulation rate must, given enough time, produce a symmetric dome whose central thickness and profile match the Vialov formula derived in {doc}`../ice_flow/mass-balance`. This is not a trivial test: it requires the spatial discretization, the time integration, and the boundary treatment at the margin all to be correct simultaneously. Bueler and colleagues formalized this into a family of manufactured solutions that test the full nonlinear SIA time-evolution code against exact analytic results {cite}`bueler2005`; if the prognostic loop passes this test, the numerics are correct where the shallow-ice approximation itself is valid.

**Response times** are a dynamical check. The kinematic models of {doc}`../climate/glacier-variations` predict that a glacier subjected to a step change in mass balance adjusts its length with an e-folding time $t_r = H/\dot{a}_0$. A numerical model of a simple synthetic glacier should reproduce this timescale when subjected to the same step perturbation. If the model's equilibration time differs systematically, the time-stepping or the thickness update is wrong. This is also a check on the balance between diffusion and advection in the numerical scheme: too much numerical diffusion will smooth out the glacier response and produce an erroneously fast equilibration.

**MISI hysteresis** is the hardest test. The marine ice-sheet instability of {doc}`../cryosphere/ice-sheets` predicts that a marine glacier resting on a retrograde bed has no stable grounding-line position on the uphill slope. A prognostic model must reproduce this hysteresis loop: advancing the grounding line over a retrograde bed should lead to runaway advance, and retreating it past the crest should lead to runaway retreat, and the two paths should not coincide. Schoof's boundary-layer theory {cite}`schoof2007` provides the analytic flux condition at the grounding line that a model must satisfy to capture this correctly. Models that represent the grounding line as a coarse-grid feature, without sub-grid treatment, systematically fail to reproduce the correct hysteresis width and can miss the instability entirely. Passing the MISI test distinguishes models whose grounding-line physics can be trusted for projections from those that cannot.

% lab (prognostic, icepack): MISI hysteresis on a synthetic retrograde bed; compare grounding-line advance and retreat

## The role of the forcing

Once the numerical loop is verified, the model is ready to be forced. The mass balance $\dot a(\mathbf{x}, t)$ appears in the thickness equation at every time step, and the projection it produces reflects the quality of that forcing as much as anything about the ice dynamics. A systematic bias in the modeled ablation at the margin, an incorrect accumulation trend, a misrepresented ocean warming at the grounding line — any of these errors accumulate step by step and produce a projection that drifts away from reality even if the ice dynamics are perfect.

This is not a criticism of prognostic modeling; it is its central organizing fact. The ice-dynamics problem and the climate-forcing problem are coupled, and solving one without the other is only half an answer. The next chapter, {doc}`../climate/climate-forcing`, opens from the opposite direction: it treats ice sheets not as passive objects being forced by a prescribed climate but as active participants in the climate system, capable of shifting the circulation, the albedo, and the sea level that feed back on their own mass balance. There it develops the reduced dynamical models best suited to the longer timescales — the millennia to glacial cycles — where direct prognostic experiments reach their honest limits.
