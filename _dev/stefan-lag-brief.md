# Development brief: phase change via Irksome `lag` for the basal-processes lab

Status: parked (June 2026) pending numerical development, likely in Claude Code with a
working Firedrake + Irksome + icepack environment. This folder does not build into the book.

## What exists

`~/Documents/stefan.ipynb` (Andrew, June 2026). 1-D unit interval, CG1. Temperature runs
−1 to +1 with T_m = 0 inside the domain; conductivity is the discontinuous
`conditional(T <= T_m, k_s, k_l)` with k_s = 2, k_l = 1; the right boundary temperature
oscillates (amplitude 0.25), driving the front back and forth; Robin-type boundary terms
with penalty σ = lag(k)/λ; Irksome BackwardEuler TimeStepper. The point of the demo, in
Andrew's words: lagging the conductivity to the start of each timestep makes this go —
without `lag`, the form is not differentiable w.r.t. T.

## The gap

No latent heat yet. The current front is the T = 0 isotherm of a two-conductivity diffusion
problem, not a phase boundary with energy cost. The full Stefan problem needs the enthalpy
form: apparent heat capacity c_app(T) = c_p + L·(dχ/dT), with χ a (regularized) phase
fraction stepping 0→1 across T_m. The natural move is `lag(c_app)` (or `lag` on χ' alone),
i.e. lag exactly the spike, keep diffusion implicit. Open questions for the development
session:

- Does `lag` handle a regularized delta (width ε in temperature) robustly, and how does the
  front speed converge as ε → 0 and Δt → 0? Verify against the classical Neumann similarity
  solution for the 1-D Stefan problem (front ∝ √t) before anything else.
- Step-lagging vs stage-lagging for higher-order RK methods (does `lag` evaluate at the
  timestep start or per stage, and does it matter for energy conservation?).
- Energy bookkeeping: with lagged c_app, is total enthalpy conserved to acceptable tolerance
  over a forcing cycle? (Track ∫ c_app T dx + L·∫ χ dx per step.)
- Whether the Robin penalty σ = lag(k)/λ is the right basal boundary treatment once the
  basal energy balance G + τ_b·u_b − mL = −k ∂T/∂z replaces the Dirichlet forcing; m falls
  out of the jump condition and should be recoverable as a diagnostic.

## Where it goes in the book

The basal-processes lesson, between `temperature-profile-lab.ipynb` (1-D analytics: seasonal
wave, conductive profile, Robin solution — all verified against the chapter) and
`sliding-laws-lab.ipynb` (Thwaites-like domain, three friction laws). Planned arc for the
combined lab (working name `heat-flow-thwaites-lab.ipynb`):

1. 1-D column with phase change: adapt stefan.ipynb to ice (real k, c, L; seasonal surface
   forcing; geothermal flux below), watch a cold bed thaw and a temperate layer grow; recover
   the basal melt rate m from the jump condition and check it against the chapter's formula.
2. Thwaites domain: take the geometry and diagnostic flow field from sliding-laws-lab,
   advect heat with it (icepack heat transport or a hand-rolled advection-diffusion form in
   Irksome), friction heating τ_b·u_b from the friction laws as a basal source.
3. The payoff: the solver returns the thawed patch of bed; that patch becomes the sliding
   mask the friction comparison inherits, closing the thermomechanical loop that
   thermal-structure.md describes in prose (frozen interior, thawed streaming corridors,
   the surge logic).

## Practicalities

- Irksome is not in the book's Docker image; the Dockerfile and
  `running-icepack-docker.md` need it added when this lab lands.
- The icepack labs use `# verify against your icepack version` flags for API-sensitive
  lines; do the same here for Irksome (`Dt`, `lag`, `TimeStepper` signatures).
- Andrew intends to write up his thoughts on why `lag` beats the alternatives (regularized
  enthalpy with full Newton; explicit operator splitting); fold that write-up into the
  lab's prose when it exists. Drop it in this folder.
