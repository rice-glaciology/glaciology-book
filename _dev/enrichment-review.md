# Enrichment review queue

Drafts proposed by the scheduled hourly enrichment task. **Nothing here is in the
book yet** — each entry is original, cited prose (in Fletcher / Cuffey & Paterson
register) that has passed the strict LLM-voice gate, plus candidate figures from
Andrew's own course decks with *proposed* original-source attributions to verify.

Andrew reviews each entry, edits as needed, and applies it to the manuscript by
hand. Delete entries once merged or rejected.

**Rules the task follows** (do not relax):
- Original prose only — the reference texts (Fletcher, Cuffey & Paterson,
  radioglaciology) are consulted and *cited*, never copied or closely paraphrased.
- Figures may be drawn from the `glaciology_course_uw` decks, but captions credit
  the **original source** (paper, book, photographer) only — **never** the UW
  course, slides, or notes. Unknown origin → uncredited, flagged for Andrew.
- No reproduction of figures from the copyrighted reference texts.
- Drafts are written here, never directly into chapters or notebooks.

## Sections already drafted (rotation tracker)

_(the task appends section names here so it does not repeat itself)_

- observing/radar-altimetry — 2026-06-16 (penetration / volume-scattering physics)
- foundations/snow-to-ice — 2026-06-16 (firn densification mechanisms: rearrangement → creep + sintering, HL empirical basis, close-off depth, bubble overpressure)
- observing/cryoseismicity — 2026-06-16 (stick-slip mechanics: velocity-weakening vs -strengthening stability criterion, Whillans tidal slip cycle)
- cryosphere/permafrost — 2026-06-16 (active-layer latent-heat / Stefan control on thaw depth + zero curtain; unfrozen water from interfacial premelting, frost heave)
- observing/gravity — 2026-06-16 (GRACE spatial resolution from spherical-harmonic truncation; mascon vs harmonic smoothing; signal leakage and the scaling-factor correction; leakage + GIA as the dominant error terms)
- cryosphere/former-glaciers — 2026-06-16 (quantitative paleo-glacier reconstruction: paleo-ELA from accumulation-area ratio / balance-ratio weighting and cirque floors; perfect-plasticity parabolic surface profile H=√(2τx/ρg) for former ice thickness/volume)
- observing/magnetotellurics — 2026-06-16 (diffusive EM regime: conduction ≫ displacement current, fields diffuse not propagate, skin depth δ=√(2/μ₀σω)≈500√(ρ/f) m and how the band maps to depth; surface impedance → apparent resistivity ρ_a=|Z|²/μ₀ω and 45° half-space phase, phase departures vs depth-varying resistivity; resistive ice cap as known offset)
- observing/insar — 2026-06-16 (interferometric phase as a line-of-sight projection: φ=(4π/λ)d·ŝ, incidence-angle weighting of vertical (cos θ) vs across-track horizontal (sin θ), azimuth motion nearly invisible, why asc/desc passes are needed for the vector; double-difference DInSAR for the grounding line — steady flow + topography cancel, leaving tidal flexure; elastic-beam flexure zone and the landward bending limit)
- ice_flow/mass-balance — 2026-06-16 (mass-balance gradient dȧ/dz and the activity index near the ELA; temperate-maritime vs cold-continental contrast traced to the surface-energy-balance / lapse-rate control on ablation; steeper ablation-zone gradient → balance ratio and a more compact ablation zone; balance flux through the ELA sets throughput and climate sensitivity; accumulation-area ratio ≈ 0.6 and the link to paleo-ELA balance-ratio reconstruction)
- foundations/ice-structure — 2026-06-16 (crystallographic depth: lattice parameters a≈4.52 Å / c≈7.36 Å & c/a≈1.633 near-ideal tetrahedral; ABAB chair-ring bilayer stacking distinguishing Ih from cubic Ic; coordination number 4 vs 12 and ≈1/3 packing fraction quantifying the openness/density anomaly)
- observing/laser-altimetry — 2026-06-16 (error budget & detection physics: surface-slope/geolocation coupling δz≈δx·tanα dominating the ranging precision on steep margins, role of across-track beam pairs and repeat-track analysis; photon-counting Poisson detection — <1 signal photon/shot vs uniform solar background, surface as a histogram peak, precision ∝ √(photon count) setting the along-track-resolution/precision trade)
- foundations/snow-processes — 2026-06-16 (quantifying dry-snow metamorphism: Kelvin/Gibbs–Thomson curvature dependence of vapour pressure ln(p_r/p_∞)=2γ_sv·V_m/(rRT), nm-scale curvature length → ~10⁻⁴ fractional excess over grains vs ~10⁻³ over dendrite tips driving the points→necks vapour diffusion; Clausius–Clapeyron temperature control on the absolute saturation pressure setting the rate, slow cold vs fast warm metamorphism, and gradient amplification feeding depth hoar)
- observing/panchromatic-imagery — 2026-06-16 (measurement physics of optical methods: stereo height precision via the base-to-height / flying-height-to-camera-separation ratio, the convergence-angle vs matching trade-off and texture dependence of correlation, weak heights over smooth firn; feature-tracking velocity error ≈ subpixel-matching × pixel size ÷ time interval, the longer-interval-vs-feature-survival trade-off opposite to InSAR-phase decorrelation)
- foundations/physics-of-ice — 2026-06-16 (hydrogen-bond energetics: O···O ≈ 2.76 Å with an asymmetric off-centre proton; per-bond energy ~20 kJ/mol, intermediate between covalent O–H (hundreds of kJ/mol) and van der Waals, explaining the open rigid framework and high melting point; cohesive-energy bookkeeping — two bonds/molecule ≈ 50 kJ/mol matching the sublimation enthalpy, while the 6 kJ/mol latent heat of fusion shows melting breaks only a small fraction of bonds and removes long-range order, not the bonding)
- cryosphere/instabilities — 2026-06-16 (tidewater calving–water-depth physics: flotation / height-above-buoyancy criterion H_f ≈ 1.1 D_w controlling terminus grounding, Brown–Meier–Post linear calving-speed-vs-depth relation and warm-water undercutting; reverse-slope instability of the overdeepening — stable terminus on the shoal, no equilibrium where the bed deepens inland, retreat halting only at the shallow fjord head; analogy to the Schoof marine grounding-line flux argument)
- radar/em-waves — 2026-06-16 (radar attenuation as a propagation problem: imaginary permittivity → exponential field/power decay e^{-αz}/e^{-2αz}, low-loss field attenuation coefficient α≈σ/(2ε₀cn) set by the small high-frequency conductivity and frequency-flat across the sounding band, ~10 dB/km one-way in cold ice and the tens-of-dB two-way budget vs the receiver noise floor that fixes maximum sounding depth; Arrhenius temperature + acid-impurity rise ~×10 per 20 K defeating temperate ice within hundreds of metres; inverse use — depth-decline of returned power as an englacial thermometer/chemistry constraint and the prerequisite for reading bed reflectivity, MacGregor & Matsuoka)
- ice_flow/ice-fabric — 2026-06-16 (quantitative lattice-rotation kinematics: velocity-gradient split L=D+W and the unit-director evolution ċ=W·c−(D·c−(c·D·c)c); uniaxial-compression reduction to θ̇=−¾ε̇ sin2θ — rate peaks at 45°, axes sweep to the pole → vertical single maximum, sign flip under extension → girdle; simple-shear D/W equal-magnitude balance holding a near-vertical maximum tilted off-vertical, grounding the chapter's qualitative "rotates like a material line")
- radar/apres — 2026-06-16 (quantifying the phase measurement: FMCW range-from-beat-frequency f_b=(2R/c)(B/T), bandwidth-limited coarse range resolution ΔR=c/2B≈0.4 m for B=200 MHz at v≈1.68×10⁸ m/s; phase precision φ=4πR/λ, λ≈0.56 m in ice → full turn per half-wavelength ≈0.28 m, degree-level phase → ~mm range, >2 orders finer than bandwidth resolution; displacement→strain→melt decomposition: fit ε̇_zz from internal-reflector displacement vs depth, bed melt = measured bed displacement − ∫ε̇_zz dz dt)
- foundations/composition — 2026-06-17 (air clathrate hydrates / bubble-clathrate transition: (N₂,O₂)·6H₂O structure-II hydrate stable above a T-dependent dissociation pressure, Miller's prediction of stability below ~800 m and bubble loss by ~1200 m confirmed at Dye-3; metastable bubble survival through the ~500–1250 m Vostok transition zone set by nucleation kinetics — ~3.7 MPa dissociation vs ~7.8 MPa hydrostatic at 900 m/223 K, ~decades to convert one bubble by inward shell diffusion; consequences for the ice-core gas record (cage-size N₂/O₂ fractionation) and the optical clearing of deep ice)
- cryosphere/sea-ice — 2026-06-16 (conduction-limited congelation growth: quasi-steady linear conduction through thin ice → ρ_i L_i dh/dt = k_i(T_f−T_s)/h; integrates to the Stefan/freezing-degree-day law h≈√(2k_iθ/ρ_iL_i) with θ=∫(T_f−T_s)dt, h² (not h) accumulating with the temperature deficit; 1/h deceleration → fast thin / slow thick growth and a thermodynamic equilibrium thickness; brine-reduced k_i,L_i + snow-cover and finite surface heat-exchange resistance degrade the pure law to h²+ah=bθ)
- thermomechanics/surface-energy-balance — 2026-06-16 (bulk-aerodynamic turbulent fluxes: H_S=ρ_a c_p C_S u(T_a−T_s) and H_L=ρ_a L_v C_L u(q_a−q_s); neutral transfer coefficient from the log-profile match C_S=k²/[ln(z/z₀)ln(z/z_0T)], von Kármán k≈0.4, growth with roughness; stable near-surface stratification over a melting surface damps turbulence below neutral, Monin-Obukhov stability correction, katabatic winds sustaining the flux; Bowen ratio β=H_S/H_L≈(c_p/L_v)(T_a−T_s)/(q_a−q_s) partitioning sensible vs latent, condensation-reinforced maritime regime vs sublimation-sink cold-dry/high-tropical regime)
- foundations/optical-properties — 2026-06-17 (quantitative Debye relaxation: complex permittivity ε*(ω)=ε_∞+(ε_s−ε_∞)/(1+iωτ) splitting into a real part falling ε_s≈100→ε_∞≈3.2 through ωτ=1 and an imaginary loss peak ε″=Δε·ωτ/(1+ω²τ²) centred at ωτ=1 (~few kHz), Cole–Cole semicircle confirming a single relaxation time for pure ice; radar band on the ωτ≫1 tail where ε″≈Δε/(ωτ) so loss ∝1/ω and ∝1/τ, loss tangent tanδ=ε″/ε′ inheriting the 1/τ Arrhenius temperature scaling — the symbolic basis for the chapter's existing "1/τ tail" and order-of-magnitude-per-20K claims)
- radar/radiowave-fabric — 2026-06-17 (azimuthal power signature of polarimetric radar: co-polarized return as a function of antenna azimuth θ and depth follows 1−sin²2θ·sin²(δ/2) with two-way birefringent phase δ=ω·Δt, extinction bands at θ=45° where δ is an odd multiple of π and recurring in depth each time δ advances by 2π, depth spacing of the bands → birefringent phase gradient → single-crystal anisotropy weighted by λx−λy; azimuth of the bands locates the horizontal principal axes giving fabric orientation not only strength; phase-sensitive HHVV coherence + its depth phase-gradient recovering phase rate and horizontal anisotropy while suppressing the scattering amplitude — Fujita matrix model + Jordan coherence method, the physics behind the chapter's existing closing nod to ApRES / "across the full polarization plane")
- thermomechanics/surface-hydrology — 2026-06-17 (quantitative hydrofracture: dry-crevasse depth from the Nye zero-stress balance d≈R_xx/(ρ_i g) ~tens of metres and self-arrest because overburden grows with depth while tension does not; water-filled crack net opening stress R_xx+(ρ_w−ρ_i)g z with the (ρ_w−ρ_i)g≈0.8 kPa/m gradient flipping the depth dependence positive → no arrest depth, ~1 MPa added over 1 km > the starting tension, supply-limited propagation to the bed; LEFM restatement K_I∝σ√d vs toughness K_Ic≈0.1–0.4 MPa·m^½, dry tip blunted as overburden overtakes tension, water-filled tip keeps exceeding toughness → runaway; Weertman/van der Veen)
- cryosphere/erosion — 2026-06-17 (quantitative quarrying mechanics: rock-step deviatoric stress ∝ effective pressure N=P_i−P_w with a geometric factor set by step-height/cavity-span, high steady P_w supports the cavity roof and lowers N; subcritical crack growth v_c=A·K_I^n with K_I≈Yσ√(πa), σ∝N and n≈30 for crystalline rock making growth an extremely steep function of N; because v_c∝N^n, time-integrated growth dominated by brief high-N excursions not the mean → cavity-drainage P_w drops spike N and drive crack bursts, quarrying rate governed by amplitude/frequency of water-pressure swings × sliding speed, Engabreen acoustic-emission bursts as the signature; Iverson 2012 / Cohen 2006)
- ice_flow/stress-balance — 2026-06-17 (quantitative lateral drag in the force budget: confined-channel shape factor f<1 reducing basal shear to f·ρgH sinα with the wall fraction 1−f rising as the channel narrows relative to depth; plug-flow transverse profile from a linear lateral shear stress 0→τ_d W/H across the half-width fed into Glen's law → u(y)=u_max[1−(|y|/W)^{n+1}], exponent 4 for n=3 concentrating shear into narrow margins, Raymond Athabasca survey; Siple Coast force budgets putting >½ the driving stress on the crevassed margins, margin-heating feedback on stream width; cuffey2010 / raymond1971 / echelmeyer1994)
- foundations/point-defects — 2026-06-17 (Jaccard quantitative link defect↔dielectric: effective charges e_DL≈0.38e + e_±≈0.62e summing to the protonic charge e; Debye relaxation rate 1/τ ∝ n_DL·μ_DL with high-frequency limiting conductivity σ_∞≈n_DL·e_DL·μ_DL, recovering τ~10⁻⁴ s from the chapter's own 10¹⁵–10¹⁶ cm⁻³ Bjerrum population and the activation energy of orientational-defect migration; complementary static rule — ionic + orientational defects act in series so σ_DC^{-1}≈σ_±^{-1}+σ_DL^{-1}, throttled by the rarer ionic defects → small σ_DC~10⁻⁸ S/m yet large ε; acid dopant ionic defects raise σ_DC far more than they shift τ, the basis of ECM acidity/volcanic logging; petrenko1999 + fletcher1970, proposed hammer1980 for ECM)
- cryosphere/planetary-ice — 2026-06-17 (physical chemistry of the "amorphous ice & high-pressure phases" section: high-P polymorphs as progressive collapse of the open Ih framework retaining 4-coordination — ice II/III/V/VI folding O–O–O angles + self-threading to ~1.17–1.31 g/cm³ over ~0.2–1 GPa, ice VII/VIII interpenetrating sublattices ~1.5 g/cm³ above ~2 GPa, tying icy-moon deep-water rheology to dense phases not Ih; proton order/disorder axis — ice rules + Pauling residual entropy S₀≈R ln(3/2)≈3.4 J/mol/K confirmed calorimetrically, disordered/ordered pairs Ih–XI, III–IX, V–XIII, VI–XV, VII–VIII frozen in below ~100 K by slow orientational-defect reorientation linking to point-defects; polyamorphism — LDA ~0.94 vs HDA ~1.17 g/cm³ with Mishima's sharp pressure-driven LDA→HDA transition ~0.2 GPa/130 K as the glassy analogue of the crystalline open→dense step, comet ice = LDA trapping volatiles; fletcher1970 + petrenko1999 + pauling1935, proposed mishima1985)

---

## 2026-06-17 (run 20) — sections/ice_flow/stress-balance.md

**Why this section:** the momentum-balance chapter (~1581 words) closes with a
"## The force budget" section that names the three resistive terms opposing the
driving stress — basal drag, lateral drag, longitudinal stress gradients — and
writes the depth-integrated balance schematically as
$\boldsymbol{\tau}_d=\boldsymbol{\tau}_b+\text{(lateral)}+\nabla\!\cdot\!(\text{membrane})$.
Two of the three terms are quantified elsewhere in the book: basal drag through the
friction laws of {doc}`../thermomechanics/basal-motion`, and the membrane term through
the depth-integrated shallow-shelf balance derived in {doc}`flow-approximations`.
**Lateral drag is the one resistive term left purely as the word "(lateral)"** — it is
never written as a stress anywhere in the ice-flow chapters, even though the companion
chapter states that lateral drag at the shear margins carries *more than half* of the
driving stress in the measured Siple Coast streams {cite}`echelmeyer1994`. The draft
supplies exactly that missing layer in three short paragraphs, parallel in depth to the
basal- and membrane-stress treatments: (1) the confined-channel **shape factor** $f<1$,
which reduces the basal shear stress to $f\,\rho g H\sin\alpha$ with the remainder
$1-f$ carried by the walls and $f$ falling as the channel narrows relative to its depth;
(2) the **transverse velocity profile** that follows when the bed is weak and the ice
moves as a plug, obtained by setting the lateral shear stress linear across the stream
($0$ at the centreline to $\tau_d W/H$ at each margin) and feeding it through Glen's law
to get $u(y)=u_{\max}[1-(|y|/W)^{n+1}]$, plug-flat in the interior with the shear packed
into narrow margins; (3) the **consequence** that the margins, not the bed, can carry
most of the resistance, fixing the stream's width and boundaries and concentrating
dissipative heating there. Consulted Cuffey & Paterson (2010), Ch. 8 (channel shape
factor and lateral drag), which the chapter already states it follows; prose is original.

**Proposed placement:** the three paragraphs go into "## The force budget", inserted
immediately after the schematic balance
$\boldsymbol{\tau}_d=\boldsymbol{\tau}_b+\text{(lateral)}+\nabla\!\cdot\!(\text{membrane})$
and the sentence that follows it ("Which term dominates defines the kind of glacier…"),
and before the closing paragraph "In the slow interior of an ice sheet the driving
stress is balanced locally by basal drag…". This puts the quantitative lateral-drag
layer right where the qualitative force-budget list ends, so the bare "(lateral)" term
acquires a stress and a profile before the chapter moves on to which term dominates in
each regime. No text is replaced; the draft is purely additive and reuses only
citations already present in references.bib ({cite}`cuffey2010`, {cite}`raymond1971`,
{cite}`echelmeyer1994` — all verified by grep).

**Drafted prose (gate-passing, verbatim):**

> A glacier confined in a valley, or an ice stream flanked by slower ice, loses part of
> its driving stress to drag on its sides. Balancing the driving force on a
> cross-section against the traction on the bed and on the two walls reduces the basal
> shear stress below the slab value $\rho g H\sin\alpha$ to $f\,\rho g H\sin\alpha$,
> where the shape factor $f<1$ measures the fraction the bed still carries and the
> remainder $1-f$ is taken up by the walls {cite}`cuffey2010`. The factor falls as the
> channel narrows relative to its depth, so that a deep, narrow glacier delivers much of
> its weight to the valley sides and only the rest to the bed, while a broad one
> approaches the unconfined slab with $f\to1$.

> Where the bed is weak and the ice slides as a plug, almost all of the driving stress
> is balanced by lateral shear, and the cross-stream profile follows from the flow law.
> With no basal traction the depth-integrated balance requires the lateral shear stress
> to grow linearly from zero at the centreline to $\tau_d W/H$ at each margin. Inserting
> that stress into Glen's law, in which the shear strain rate goes as the $n$th power of
> the stress, and integrating across the half-width $W$ gives the transverse velocity
>
> $$
> u(y)=u_{\max}\left[1-\left(\frac{|y|}{W}\right)^{n+1}\right],
> $$
>
> flat across the interior and falling steeply within a narrow band at either side. For
> $n=3$ the exponent is four, so the shearing that accommodates the motion is
> concentrated almost entirely in the margins, where Raymond's transverse survey of
> Athabasca Glacier resolved it {cite}`raymond1971`.

> In a fast ice stream the margins, rather than the bed, can provide most of the
> resistance to flow. Force-budget estimates on the Siple Coast ice streams assign more
> than half of the driving stress to lateral drag at the crevassed shear margins
> {cite}`echelmeyer1994`, which sets both the width of the stream and the location of
> its boundaries. Concentrating the deformation into these narrow bands also
> concentrates the heat it releases, warming and softening the marginal ice and acting
> back on the width of the stream.

**Register note:** calibrated against the chapter's existing force-budget and
driving-stress prose and Cuffey & Paterson (2010), Ch. 8. Subject-first declarative
openers ("A glacier confined in a valley…", "Where the bed is weak…", "In a fast ice
stream…"), plain verbs ("loses," "carries," "grow," "provide"), hedged magnitudes
("almost all," "more than half"). Deliberately avoided: any colon-hinge; the
"margins want / the bed gives up" anthropomorphism (the draft uses "loses part of its
driving stress to drag" and "the margins … can provide most of the resistance"); the
"not the bed but the margins" flourish, written as the plain "the margins, rather than
the bed"; and balanced semicolon aphorisms. No sentence reproduces C&P wording; only
the register and the standard results were matched.

**Numerical / physical check (for Andrew, not for the prose):** the confined-channel
shape factor $f<1$ reducing the basal shear to $f\rho g H\sin\alpha$ is the standard
Nye channel result reproduced in Cuffey & Paterson (2010), Ch. 8, with tabulated $f$
falling from near unity for wide sections to roughly $0.5$ for half-width-to-depth
ratios of order one — "falls as the channel narrows relative to its depth" is correct
and the limit $f\to1$ for a broad channel is exact. The transverse-profile derivation
is standard: with negligible basal drag the depth-integrated $x$ balance is
$\partial(H\tau_{xy})/\partial y=-\tau_d$, giving (for uniform $H$) a lateral shear
stress $\tau_{xy}=-(\tau_d/H)\,y$ that is zero at the centreline and reaches magnitude
$\tau_d W/H$ at the wall; Glen's law $\dot\varepsilon_{xy}=A\tau_E^{\,n-1}\tau_{xy}$ with
the lateral shear dominating $\tau_E$ gives $\partial u/\partial y\propto -|y|^{n}$,
which integrates to $u(y)=u_{\max}[1-(|y|/W)^{n+1}]$ with
$u_{\max}=2A(\tau_d/H)^{\,n}W^{\,n+1}/(n+1)$ when the margin is held fixed. For $n=3$
the exponent $n+1=4$ makes the profile strongly plug-like, as Raymond's Athabasca
transverse-section survey found {cite}`raymond1971`. The "> ½ of the driving stress
carried by the margins" statement is exactly the Echelmeyer et al. (1994) force-budget
result {cite}`echelmeyer1994` already cited in {doc}`flow-approximations`. No new bib
entries are required — {cite}`cuffey2010`, {cite}`raymond1971`, and
{cite}`echelmeyer1994` are all present in references.bib (verified by grep) and the
first and third are already used in the ice-flow chapters.

**Proposed new BibTeX entries:** none. The draft uses only citations already in
references.bib. (Note for Andrew: the $u\propto1-(|y|/W)^{n+1}$ channel-profile result
is canonically Nye, J.F. 1965, "The flow of a glacier in a channel of rectangular,
elliptic or parabolic cross-section," *J. Glaciol.* 5(41), 661–690. It is reproduced in
Cuffey & Paterson Ch. 8, so the draft cites {cite}`cuffey2010`; if you would prefer the
primary attribution, the Nye 1965 entry could be added, but I have not invented a DOI
for it and left it out rather than risk an incorrect field.)

**Figure proposals:**

The course-deck figure pool (`~/Downloads/glaciology-course-uw`) was **not mounted on
this run** (checked: only the book repo, outputs, and uploads are mounted; `~/Downloads`
absent), so no deck image/slide is cataloged. One *original* schematic is proposed, to
be generated with matplotlib in the style of the existing `_dev/make-*.py` figures (no
third-party attribution required because it would be drawn fresh).

1. **Transverse velocity profile of a plug-flowing stream (single panel).** Plot
   $u(y)/u_{\max}=1-(|y|/W)^{n+1}$ across the normalized half-width $-1\le y/W\le1$ for
   $n=1$ (linear-viscous reference parabola, exponent 2) and $n=3$ (the glacial case,
   exponent 4), with the steep marginal drop and flat interior of the $n=3$ curve marked
   as the shear margin, and a small inset or annotation showing the linear lateral shear
   stress $\tau_{xy}=(\tau_d/H)\,y$ rising to $\tau_d W/H$ at the wall. This is the whole
   "lateral drag carried in narrow margins" argument of the draft in one figure, and a
   direct visual partner to Raymond's measured Athabasca transverse section. Origin:
   original figure (to be drafted) — no attribution needed.

If a future run has the decks mounted, search the ice-stream / ice-dynamics deck media
for (a) a map of the Siple Coast / Whillans–Kamb ice streams showing the crevassed
shear margins, or (b) a measured or schematic transverse velocity profile of a valley
glacier or stream, and catalog it with its *original* publication source (e.g.
{cite}`raymond1971` for the Athabasca transverse section, {cite}`echelmeyer1994` for the
ice-stream-margin force budget), following rule 2 — never the course.

**Detector gate:** `PASS  /sessions/.../outputs/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

## 2026-06-17 (run 19) — sections/cryosphere/erosion.md

**Why this section:** the erosion chapter (~1680 words, the thinnest of the
cryosphere chapters and not previously drafted) gives **abrasion** a full quantitative
treatment — the Stokes-drag contact force $F=6\pi\eta R v_n$ with a worked $\sim10^6$ N
estimate, and the Hallet abrasion law $\dot A=\alpha F_c v_p C$ with its
square-of-sliding scaling, each in its own dropdown derivation. **Quarrying**, which
the chapter itself calls "the dominant erosional process, faster than abrasion by an
order of magnitude or more," is left entirely in words. The "## Abrasion and
quarrying" section says only that the rock step "carries a deviatoric stress set by the
difference between ice pressure and cavity water pressure," that "cracks in the lee
corner grow when that difference is large," and that "what breaks it is the drop, when
the cavity drains, the bridging stress on the step spikes, and cracks jump ahead." All
correct, but the effective-pressure scaling of the step stress is never written, the
crack-growth law is never given, and — most importantly — the reason fluctuations
matter more than the mean (the steep stress dependence of subcritical crack growth) is
asserted rather than shown. The draft supplies exactly that missing layer in three
short paragraphs, parallel in depth to the existing abrasion treatment: (1) the
rock-step deviatoric stress $\propto N=P_i-P_w$ and why high steady water pressure
protects the step; (2) the cornered edge-crack stress intensity
$K_I\approx Y\sigma\sqrt{\pi a}$ and subcritical growth $v_c=A K_I^{\,n}$ with $n\approx
30$; (3) the consequence that, because $v_c\propto N^n$, the time-integrated growth is
dominated by brief high-$N$ excursions, so cavity-drainage pressure drops drive crack
bursts and the quarrying rate is set by the water-pressure swings — closing the loop on
the Engabreen acoustic-emission observation already in the chapter. Consulted Cuffey &
Paterson (2010, Ch. 13) and the quarrying theory of {cite}`iverson2012`, both already
cited by the chapter; prose is original.

**Proposed placement:** the three paragraphs go into "## Abrasion and quarrying",
inserted into the **quarrying** paragraph's territory — immediately after the existing
paragraph that ends "…the asymmetry it leaves behind, smooth abraded stoss faces and
steep plucked lee faces, is the signature of the roche moutonnée." and before the
**Abrasion** bold paragraph. This places the quantitative quarrying layer right where
the qualitative quarrying description ends, mirroring how the abrasion paragraph is
immediately followed by its own equations. No text is replaced; the draft is purely
additive and reuses only citations already present ({cite}`iverson2012`,
{cite}`cohen2006`).

**Drafted prose (gate-passing, verbatim):**

> Where ice bridges a lee cavity, the rock step between the loaded stoss face and the
> unsupported lee carries a deviatoric stress set by the effective pressure $N = P_i -
> P_w$, the difference between the ice overburden pressing on the stoss side and the
> water pressure in the cavity. The step behaves as a loaded ledge, and the bending
> concentrates a tensile stress at its lee corner of order $N$ times a geometric factor
> of a few, fixed by the ratio of step height to cavity span {cite}`iverson2012`.
> Raising the cavity water pressure supports the roof and lowers $N$, which is why a bed
> held at high, steady water pressure quarries slowly even while it slides fast.

> Bedrock fails at these stresses only because it is already flawed. A crack of length
> $a$ at the lee corner carries a stress intensity $K_I \approx Y\,\sigma\,\sqrt{\pi a}$,
> with $\sigma \propto N$ and $Y$ a geometric factor, and it lengthens by subcritical
> growth at a velocity $v_c = A\,K_I^{\,n}$ well before $K_I$ reaches the fracture
> toughness $K_{Ic}$. The exponent $n$ for crystalline rock is large, of order thirty,
> so the growth rate is an extremely steep function of the applied stress and therefore
> of $N$. A modest rise in effective pressure advances a crack far faster than its
> time-average would imply, and the slow background loading at a typical $N$ removes
> almost nothing.

> Because $v_c$ depends so steeply on $N$, the time-integrated crack growth is dominated
> by the brief excursions to high effective pressure rather than by the mean. When a
> cavity drains and $P_w$ falls, $N$ jumps, the corner stress rises with it, and cracks
> that were nearly static accelerate toward failure in a burst. The quarrying rate is
> then governed by the amplitude and frequency of the water-pressure swings rather than
> by the average state of the bed, and it scales with sliding speed through the rate at
> which fresh steps are loaded {cite}`iverson2012`. The acoustic-emission bursts
> recorded at each pressure drop beneath Engabreen are the direct expression of this
> control {cite}`cohen2006`.

**Register note:** calibrated against the existing abrasion treatment in the same
chapter and the quarrying register of Cuffey & Paterson (2010), Ch. 13. Subject-first
declarative openers ("Where ice bridges a lee cavity…", "Bedrock fails at these
stresses only because…"), plain verbs ("carries," "lowers," "lengthens," "jumps"),
hedged magnitudes ("a geometric factor of a few," "of order thirty"), and consequence
stated plainly ("removes almost nothing"). Deliberately avoided: any colon-hinge; the
"water *protects* the rock / cracks *want* to grow" anthropomorphism (the draft uses
"supports the roof and lowers $N$" and "cracks … accelerate toward failure"); and
balanced semicolon aphorisms. The "not by the average state … but by the swings"
contrast is written as a plain "rather than," not a "not just X but Y" flourish. No
sentence reproduces C&P or Iverson wording; only the register was matched.

**Numerical / physical check (for Andrew, not for the prose):** the rock-step stress
scaling with effective pressure $N=P_i-P_w$ and the cavity-roof support of high $P_w$
are the core of Iverson's quarrying theory {cite}`iverson2012`; the geometric factor
is an order-unity-to-few multiplier from the step geometry, left unspecified
deliberately. The edge-crack stress intensity $K_I=Y\sigma\sqrt{\pi a}$ is the standard
LEFM form (consistent with the surface-hydrology draft from run 18). Subcritical
(stress-corrosion) crack growth in silicate/crystalline rock follows a Charles-law
power dependence $v_c\propto K_I^{\,n}$ with the stress-corrosion index $n$ typically
$\sim$30–40 — "of order thirty" is conservative and correct. The steep exponent is
what makes the time-integral of growth dominated by the peaks of $N(t)$ rather than its
mean, which is the published explanation for why fluctuating-pressure beds quarry fast;
this matches the Engabreen acoustic-emission-at-pressure-drop observation
{cite}`cohen2006` already in the chapter. No new bib entries are required — both
{cite}`iverson2012` and {cite}`cohen2006` are present in references.bib (verified by
grep) and already cited by this chapter.

**Proposed new BibTeX entries:** none. The draft uses only citations already in
references.bib and already used by the chapter.

**Figure proposals:**

The course-deck figure pool (`~/Downloads/glaciology-course-uw`) was **not mounted on
this run** (checked: only the book repo, outputs, and uploads are mounted; `~/Downloads`
absent), so no deck image/slide is cataloged. The chapter already carries a `% TODO
Illustrator figure: figures/quarrying-abrasion.svg` placeholder whose spec covers the
roche-moutonnée geometry; the draft adds the quantitative layer that figure would
caption. One *original* schematic is proposed to complement it, to be generated with
matplotlib in the style of the existing `_dev/make-*.py` figures (no third-party
attribution required because it would be drawn fresh).

1. **Effective pressure and crack-growth rate over a cavitation cycle (two stacked
   panels, shared time axis).** Top panel: cavity water pressure $P_w(t)$ through a
   fill–drain cycle and the resulting effective pressure $N(t)=P_i-P_w$ (mirror image),
   with the brief drainage drop marked. Bottom panel: subcritical crack-growth velocity
   $v_c\propto N^{\,n}$ for $n\approx30$ on the same time axis, showing that $v_c$ is
   negligible through most of the cycle and spikes sharply during the $N$ excursion — the
   whole "fluctuations beat the mean" argument of the draft in one figure, and a direct
   visual partner to the Engabreen acoustic-emission bursts. Origin: original figure (to
   be drafted) — no attribution needed.

If a future run has the decks mounted, search the glacial-erosion / subglacial-process
deck media for (a) a roche-moutonnée or plucked-lee-face photograph, or (b) a
schematic of the Iverson quarrying / cavity-step geometry, and catalog it with its
*original* publication or photographer source (e.g. {cite}`iverson2012` for the
quarrying mechanics, {cite}`cohen2006` for the Engabreen subglacial-laboratory setup),
following rule 2 — never the course.

**Detector gate:** `PASS  /sessions/.../outputs/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

## 2026-06-17 (run 18) — sections/thermomechanics/surface-hydrology.md

**Why this section:** the surface-hydrology chapter (~1945 words, not previously
drafted) states its central mechanical result, lake-driven hydrofracture, entirely
in words. The "## Hydrofracture and the drainage of lakes" section says only that a
water-filled crack differs from a dry one "because the water pressure pushes the
crack walls apart," that "a dry crevasse in ice penetrates only to a depth of about
thirty metres, where the inward squeeze of the ice closes it," and that "a crack
filled with water to its top can in principle propagate to any depth, because water
is denser than ice and the pressure at the crack tip keeps rising faster than the ice
can resist." All correct, but the thirty-metre depth is never derived, the
density-difference argument is never written as a stress, and the "any depth" claim is
asserted rather than shown. The draft supplies exactly that missing layer in three
short paragraphs: (1) the Nye zero-stress balance giving the dry-crevasse depth
$d\approx R_{xx}/(\rho_i g)$ and why a dry crack self-arrests; (2) the water-filled
net opening stress $R_{xx}+(\rho_w-\rho_i)g z$, the sign flip of the depth dependence
because $\rho_w>\rho_i$, the $\approx0.8$ kPa m⁻¹ gradient and its ~1 MPa accumulation
over a kilometre, and supply-limited propagation to the bed; (3) the linear-elastic
fracture-mechanics restatement ($K_I\propto\sigma\sqrt d$ versus toughness $K_{Ic}$)
showing why the dry tip is blunted while the water-filled tip keeps exceeding
toughness. Consulted Cuffey & Paterson (2010, 4th ed., fracture/crevasse treatment in
Ch. 10), confirmed from the Drive textbooks copy, and the chapter's existing citation
{cite}`vanderveen2007`; prose is original.

**Proposed placement:** the three paragraphs go into "## Hydrofracture and the
drainage of lakes", inserted immediately after the existing first paragraph (the one
ending "…A lake holding a few metres of water over a crevasse field supplies exactly
this condition {cite}`vanderveen2007`.") and before the "The consequences were
measured directly in Greenland…" paragraph ({cite}`das2008`). They quantify exactly
that first paragraph's claims and set up the observed two-hour drainage that follows.
No text is replaced; the draft is purely additive. (The `das2008` Greenland-drainage
citation is deliberately left to the following existing paragraph, not duplicated in
the draft.)

**Drafted prose (gate-passing, verbatim):**

> A crevasse opens where the ice is in tension and closes where the weight of the ice
> overhead squeezes it shut, and its depth is fixed by the balance between the two. In
> the zero-stress treatment introduced by Nye, the crack reaches the depth at which the
> resistive longitudinal stress $R_{xx}$ that holds it open is just cancelled by the
> cryostatic overburden $\rho_i g z$, giving a dry-crevasse depth $d \approx
> R_{xx}/(\rho_i g)$. A resistive stress of a few tenths of a megapascal puts this at a
> few tens of metres, the figure cited above. The overburden grows with depth while the
> applied tension does not, so a dry crack is self-arresting, and below $d$ the
> surrounding ice stands in net compression {cite}`vanderveen2007`.

> Filling the crack with water reverses the sign of the depth dependence. Water standing
> to the surface presses outward on the walls with a pressure $\rho_w g z$ that climbs
> with depth, and the net stress available to open the crack becomes $R_{xx} - \rho_i g z
> + \rho_w g z = R_{xx} + (\rho_w - \rho_i)\,g z$. Since water is denser than ice, the
> gradient $(\rho_w - \rho_i)g \approx 0.8$ kPa per metre is positive, so the opening
> stress rises with depth instead of falling to zero. A crack kept full of water has no
> self-arresting depth, and over a kilometre of ice the added term reaches nearly a
> megapascal, larger than the tension that began the fracture. The advance is then set by
> how fast water is supplied rather than by the strength of the ice, so a lake holding a
> few metres of water can carry a fracture to the bed {cite}`weertman1973,vanderveen2007`.

> The same competition can be written in terms of fracture mechanics, where a crack
> advances once the stress intensity at its tip, $K_I$, reaches the fracture toughness of
> ice, $K_{Ic}\approx 0.1$–$0.4\ \mathrm{MPa\,m^{1/2}}$. For an edge crack of depth $d$
> loaded by a stress $\sigma$, $K_I$ scales as $\sigma\sqrt{d}$, so the tip loading of a
> dry crack is blunted as the rising overburden overtakes the tension and pulls $K_I$
> back below toughness. The water column contributes a term to $K_I$ that grows with
> depth, so a water-filled crack that once exceeds toughness keeps exceeding it, and the
> fracture runs downward without a stable arrest depth {cite}`vanderveen2007`.

**Register note:** calibrated against the fracture/crevasse register of Cuffey &
Paterson (2010), Ch. 10. Subject-first declarative openers, plain verbs ("opens,"
"closes," "rises," "reaches"), hedged magnitudes ("a few tenths of a megapascal,"
"a few tens of metres," "nearly a megapascal"), and consequence stated plainly
("a dry crack is self-arresting"). Deliberately avoided: any colon-hinge, the
"water *wants* to open the crack" anthropomorphism (the draft says "the net stress
available to open the crack" and "water … presses outward"), and balanced semicolon
aphorisms. No sentence reproduces C&P or van der Veen wording; only the register was
matched.

**Numerical check (for Andrew, not for the prose):** with $\rho_i=917$, $\rho_w=1000$
kg m⁻³, $g=9.81$ m s⁻²: $(\rho_w-\rho_i)g = 0.814$ kPa m⁻¹, integrating to $0.81$ MPa
over 1000 m. The dry-crevasse depth $d=R_{xx}/(\rho_i g)$ gives exactly 30 m for
$R_{xx}=0.27$ MPa (and inversely $R_{xx}=0.27$ MPa for $d=30$ m), consistent with the
chapter's existing "about thirty metres." $K_{Ic}$ of polycrystalline ice is
$\sim0.1$–$0.4$ MPa m^{1/2} (laboratory range). The net-opening-stress expression is
the standard surface-to-tip integral of (tensile − lithostatic + hydrostatic) wall
stress; the sign flip follows directly from $\rho_w>\rho_i$.

**Proposed new BibTeX entry** (the canonical water-filled-crevasse reference, used by
the draft and NOT currently in references.bib — verified by grep; only `weertman1957`,
`weertman1972`, `weertman1974` are present):

```bibtex
@incollection{weertman1973,
  author    = {Weertman, J.},
  title     = {Can a water-filled crevasse reach the bottom surface of a glacier?},
  booktitle = {Symposium on the Hydrology of Glaciers},
  series    = {IAHS Publication},
  number    = {95},
  pages     = {139--145},
  publisher = {International Association of Hydrological Sciences},
  year      = {1973}
}
```

`vanderveen2007` and `das2008` are already present and already cited by the chapter
(verified by grep), so no further bib changes are needed.

**Figure proposals:**

The course-deck figure pool (`~/Downloads/glaciology-course-uw`) was **not mounted on
this run** (checked: only the book repo, outputs, and uploads are mounted; `~/Downloads`
absent), so no deck image/slide is cataloged. One *original* schematic is proposed, to
be generated with matplotlib in the style of the existing `_dev/make-*.py` figures (no
third-party attribution required because it would be drawn fresh).

1. **Net wall stress versus depth for a dry and a water-filled crevasse (one panel).**
   Plot net opening stress on the horizontal axis against depth on the vertical axis
   (depth increasing downward). Dry case: a line starting at $R_{xx}$ at the surface and
   decreasing linearly with depth as $R_{xx}-\rho_i g z$, crossing zero at $d=R_{xx}/
   (\rho_i g)$ (mark the ~30 m arrest depth). Water-filled case: a line starting at the
   same $R_{xx}$ but *increasing* with depth as $R_{xx}+(\rho_w-\rho_i)g z$, never
   crossing zero, annotated with the $0.8$ kPa m⁻¹ slope. The crossover/divergence of the
   two lines is the whole argument of the draft in one figure. Origin: original figure
   (to be drafted) — no attribution needed.

If a future run has the decks mounted, search the surface-hydrology / Greenland-melt /
ice-shelf-collapse deck media for (a) an aerial/satellite photograph of a draining
supraglacial lake or moulin, or (b) the Das et al. 2008 lake-drainage figure, and
catalog it with its *original* publication or photographer source (e.g. {cite}`das2008`
for the drainage event, {cite}`banwell2013` for the Larsen B lake-chain mechanism),
following rule 2 — never the course.

**Detector gate:** `PASS  /sessions/.../outputs/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

## 2026-06-16 (run 17) — sections/ice_flow/ice-fabric.md

**Why this section:** the ice-fabric chapter (~1580 words, the thinnest of the
flow-law chapters and not previously drafted) carries its central kinematic claim
entirely in words. The "## Fabric development" section says each grain's c-axis
"rotates like a material line embedded in the flow, turning away from the axis of
extension and toward the axis of compression," that vertical compression "builds a
single maximum" while horizontal extension "spreads them into a girdle," and that in
simple shear the axes "cluster toward the vertical and slightly downstream" — all
correct, none written as an equation, and the rate, the angular dependence, and the
reason the simple-shear cluster sits *off* the strain axis are never given. The draft
supplies the missing kinematic layer: the velocity-gradient decomposition L=D+W, the
unit-director (lattice-rotation) evolution equation used in the spectral models, its
exact reduction under uniaxial compression to θ̇=−¾ε̇ sin2θ (peaking at 45°, sweeping
axes to the pole for a single maximum and reversing to a girdle under extension), and
the D/W equal-magnitude balance that fixes the simple-shear maximum slightly off
vertical. This complements rather than repeats the existing "Single-crystal
anisotropy" and "From grains to a bulk flow law" sections, which already own the ~60×
glide ratio and the enhancement factors. Consulted {cite}`rathmann2021` (spectral
fabric / lattice-rotation operator) and {cite}`cuffey2010` (observed core fabrics and
stress-regime patterns), both already in references.bib and already cited by the
chapter; prose is original.

**Proposed placement:** the three paragraphs go into "## Fabric development",
inserted immediately after the existing first paragraph (the qualitative
lattice-rotation paragraph ending "…sharpen the fabric without limit."). They give the
symbolic form of exactly that paragraph's claim and set up the recrystallization
paragraph that follows. No text is replaced; the draft is purely additive.

**Drafted prose (gate-passing, verbatim):**

> Lattice rotation can be written as the kinematic response of the c-axis to the
> velocity gradient. The velocity gradient $\mathbf{L}=\nabla\mathbf{v}$ splits into
> its symmetric part, the strain rate $\mathbf{D}$, and its antisymmetric part, the
> spin $\mathbf{W}$. Carried as a material direction of fixed unit length, the c-axis
> then changes at the rate
> $$
> \dot{\mathbf{c}} = \mathbf{W}\cdot\mathbf{c} - \big(\mathbf{D}\cdot\mathbf{c} - (\mathbf{c}\cdot\mathbf{D}\cdot\mathbf{c})\,\mathbf{c}\big).
> $$
> The spin term rotates the axis rigidly with the local vorticity, while the
> strain-rate term, after its projection onto $\mathbf{c}$ is subtracted to preserve
> unit length, supplies the part that reorients the axis. This is the lattice-rotation
> term used in the spectral fabric models {cite}`rathmann2021`, and it is the dominant
> mechanism of fabric development in cold ice.

> The two end-member stress states follow directly. Under uniaxial compression along
> the vertical the flow is irrotational, so $\mathbf{W}=0$ and
> $\mathbf{D}=\dot\varepsilon\,\mathrm{diag}(\tfrac12,\tfrac12,-1)$, with
> $\dot\varepsilon>0$ the shortening rate. For a c-axis at colatitude $\theta$ from
> the vertical the evolution equation reduces to $\dot\theta=-\tfrac34\dot\varepsilon
> \sin 2\theta$. The rotation vanishes for axes already vertical or horizontal and is
> fastest at $\theta=45^\circ$, so the c-axes rotate from intermediate colatitudes
> toward the vertical and tighten into a single maximum as strain accumulates.
> Reversing the sign of $\dot\varepsilon$, for vertical extension, reverses the
> rotation, and the axes rotate away from the vertical and spread into a girdle in the
> horizontal plane.

> Bed-parallel simple shear, unlike pure compression, carries a nonzero spin alongside
> its strain rate. With the shear in the $x$–$z$ plane and $\partial u/\partial z$ the
> only nonzero component of the velocity gradient, the strain rate and spin are equal
> in magnitude. The rotation by the spin then balances the concentrating tendency of
> the strain rate, and the cluster settles at a fixed orientation rather than at the
> strain axis. The resulting fabric is a single maximum close to the vertical but
> rotated slightly toward the flow in the plane of shear, the configuration commonly
> measured in the deep ice of streams and sheets {cite}`cuffey2010`. This
> near-alignment of the basal planes with the plane of shearing produces the large
> shear enhancement discussed in the following section.

**Register note:** the draft was calibrated against the actual crystal-fabric /
recrystallization passages of Cuffey & Paterson (2010), Chapter 3, read from the Drive
textbooks copy (not from memory). The revision favors C&P's habits over the first
draft's: subject-first openers, medium declarative sentences, plain rotation verbs
("the c-axes rotate toward the vertical" rather than "sweep out of the mid-latitudes
and accumulate toward the pole"), hedges ("commonly measured"), an observational
appositive with the citation at the sentence end, and a consequence stated as "X
produces the … enhancement discussed in the following section." Removed from the first
draft: the aphoristic summary pair ("the strain rate setting the timescale and sin2θ
the shape") and the literary cleft ending ("the kinematic mark of the vorticity, and
it is what aligns …"). No sentence reproduces C&P wording; only the register and
sentence shapes were matched.

**Numerical check (for Andrew, not for the prose):** the colatitude rate was derived
symbolically and verified against the full evolution equation. Taking
$\mathbf{D}=\mathrm{diag}(\tfrac12,\tfrac12,-1)$, $\mathbf{W}=0$, $\dot\varepsilon=1$,
and $\mathbf{c}=(\sin\theta,0,\cos\theta)$, the numerical $\dot\theta=-\dot c_z/\sin\theta$
matches $-\tfrac34\sin 2\theta$ to machine precision at θ = 10°, 30°, 45°, 60°, 80°
(−0.2565, −0.6495, −0.7500, −0.6495, −0.2565 in both columns). The sign is negative
(θ decreasing → axes rotate toward the vertical compression axis), the magnitude peaks
at θ = 45° and vanishes at the poles and equator, and flipping the sign of
$\dot\varepsilon$ flips the drift toward the equator (girdle), as stated. The
simple-shear equal-magnitude claim is the standard $|D_{xz}|=|W_{xz}|=\tfrac12\,
\partial u/\partial z$ identity for a single-component velocity gradient.

**Proposed new BibTeX entries:** none. Both citation keys used (`rathmann2021`,
`cuffey2010`) are already present in references.bib (verified by grep) and are already
cited elsewhere in this chapter.

**Figure proposals:**

The course-deck figure pool (`~/Downloads/glaciology-course-uw`) was **not mounted on
this run** (checked: only the book repo, outputs, and uploads are mounted; `~/Downloads`
absent), so no deck image/slide is cataloged. One *original* schematic is proposed, to
be generated with matplotlib in the style of the existing `_dev/make-*.py` figures (no
third-party attribution required because it would be drawn fresh).

1. **Lattice rotation under the two strain regimes (two-panel pole-figure schematic).**
   Left panel: a lower-hemisphere equal-area projection (Schmidt net) of c-axes under
   vertical uniaxial compression, with short arrows on a scatter of axes pointing toward
   the centre (vertical), arrow lengths proportional to $\sin 2\theta$ so they are
   longest at the 45° ring and vanish at centre and rim, illustrating the single-maximum
   tightening. Right panel: the same net under vertical extension, arrows pointing
   outward toward the rim, illustrating the girdle. A small inset could plot
   $\dot\theta/\dot\varepsilon=-\tfrac34\sin 2\theta$ versus θ to make the angular
   dependence explicit. Origin: original figure (to be drafted) — no attribution needed.

If a future run has the decks mounted, search the ice-rheology / fabric / ice-core
deck media for a real measured c-axis pole figure or eigenvalue-versus-depth profile
from an ice core (e.g. GRIP, EDML, or Dome C) and catalog it with its *original*
publication source (the ice-core fabric paper or {cite}`cuffey2010`'s own figure
credit), following rule 2 — never the course.

**Detector gate:** `PASS  /sessions/.../outputs/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

## 2026-06-16 (run 16) — sections/radar/apres.md

**Why this section:** the ApRES chapter is thin (~1100 words) and its physics is
stated entirely without numbers. The "## The phase measurement" subsection says the
instrument transmits a swept tone "so that each reflector's range appears as a beat
frequency," that "the phase advances by a full cycle for every half wavelength of
change in the distance," and that the result is sensitivity "far smaller than the
radar's nominal range resolution" and "a fraction of a millimetre" — all correct,
none quantified, and the FMCW range relation, the bandwidth-limited range
resolution, the wavelength in ice, and the actual ratio between coarse and phase
precision are never given. The companion {doc}`../radar/em-waves` already owns the
propagation physics (permittivity, wave speed ≈168 m µs⁻¹, n≈1.78), so this draft
supplies the *measurement* layer the ApRES section is missing rather than repeating
it. Paragraph 1 derives the beat-frequency–to-range map and the coarse resolution
ΔR=c/2B for the actual 200–400 MHz sweep. Paragraph 2 quantifies the phase precision
(λ≈0.56 m in ice → one cycle per ≈0.28 m of range, degree-level phase → ~mm,
>2 orders finer than the bandwidth limit), making the chapter's "fraction of a
millimetre" claim concrete. Paragraph 3 formalizes the displacement→strain→melt
decomposition the chapter currently states only qualitatively (fit ε̇_zz from the
internal reflectors, subtract the integrated strain from the bed's apparent motion to
get basal melt). Consulted {cite}`nicholls2015` (already in references.bib, already
cited by the chapter) for the strain/melt method and the instrument description;
prose is original. Numbers cross-checked against the book's own em-waves values
(n=1.78, v≈1.68×10⁸ m s⁻¹) for internal consistency.

**Proposed placement:** Paragraph 1 and Paragraph 2 into the existing
"## The phase measurement" subsection, *replacing* its current single qualitative
paragraph (or appended after it if Andrew prefers to keep the prose lead-in — the
draft restates the same facts quantitatively, so keeping both would duplicate).
Paragraph 3 into "## From displacement to strain and melt", inserted after the
existing first paragraph ("…the residual motion of the bed gives the basal melt
rate.") to give the symbolic version of the decomposition that paragraph describes in
words.

**Drafted prose (gate-passing, verbatim):**

> In a frequency-modulated continuous-wave radar the range to a reflector is encoded
> in the beat frequency formed when the returning sweep is mixed with the outgoing
> one. For a linear sweep of bandwidth $B$ over duration $T$ the chirp rate is $B/T$,
> and a reflector at range $R$ delays the return by $2R/c$, so the beat frequency is
> $f_b = (2R/c)(B/T)$ and rises in proportion to range. The width of each
> beat-frequency peak, and with it the coarse range resolution, is fixed by the
> bandwidth alone as $\Delta R = c/(2B)$. ApRES sweeps from 200 to 400 MHz, so
> $B = 200$ MHz, and with a wave speed in ice near $1.68\times10^8$ m s$^{-1}$ the
> range resolution is about 0.4 m. That is the scale on which the amplitude profile
> separates one reflector from the next.

> The phase of the return locates a reflector far more finely than the bandwidth
> allows. A two-way path of length $2R$ advances the phase by $4\pi R/\lambda$, so a
> small change $\delta R$ shifts the phase by $4\pi\,\delta R/\lambda$. At the centre
> frequency the wavelength in ice is about 0.56 m, and a full turn of phase therefore
> corresponds to half a wavelength of range change, close to 0.28 m. Resolving the
> phase to a degree then places a reflector to within a millimetre, finer than the
> bandwidth-limited resolution by more than two orders of magnitude. Comparing the
> phase of the same reflector across two acquisitions recovers its displacement at
> this precision, as long as the reflector keeps its shape between visits
> {cite}`brennan2014`.

> The displacement measured at a reflector mixes the deformation of the ice above it
> with any motion of the reflector itself. Fitting the displacements of the internal
> reflectors against depth yields the vertical strain rate $\dot\varepsilon_{zz}$, the
> rate at which the column thins. The bed sits below the whole strained column, so its
> expected displacement is the integral of the strain rate over the ice thickness and
> the elapsed time. The difference between the bed's measured displacement and that
> integral is the thickness of ice removed or added at the base over the interval, and
> dividing by the elapsed time gives the basal melt rate {cite}`nicholls2015`.

**Numerical check (for Andrew, not for the prose):** wave speed in ice
$v=c/n=3\times10^8/1.78=1.685\times10^8$ m s⁻¹ (matches the em-waves chapter's
"≈168 m µs⁻¹"). Coarse range resolution $\Delta R=c/2B=v/2B=1.685\times10^8/(4\times
10^8)=0.42$ m → "about 0.4 m." Centre frequency 300 MHz → wavelength in ice
$\lambda=v/f=1.685\times10^8/3\times10^8=0.562$ m → "about 0.56 m"; half-wavelength
0.281 m → "close to 0.28 m." Phase-to-range: $\delta R=(\lambda/4\pi)\,\delta\varphi$;
for $\delta\varphi=1^\circ=0.0175$ rad, $\delta R=(0.562/4\pi)\times0.0175=
7.8\times10^{-4}$ m ≈ 0.8 mm → "to within a millimetre." Ratio
$\Delta R/\delta R\approx0.42/0.001\approx400$ → "more than two orders of magnitude."
All consistent with published ApRES specifications (Brennan et al. 2014;
Nicholls et al. 2015).

**Proposed new BibTeX entry** (`nicholls2015` already present — verified by grep;
`brennan2014` is *not* present — verified by grep, no `brennan` key):

```bibtex
@article{brennan2014,
  author  = {Brennan, P. V. and Lok, L. B. and Nicholls, K. and Corr, H.},
  title   = {Phase-sensitive {FMCW} radar system for high-precision {Antarctic}
             ice shelf profile monitoring},
  journal = {IET Radar, Sonar \& Navigation},
  year    = {2014},
  volume  = {8},
  number  = {7},
  pages   = {776--786},
  doi     = {10.1049/iet-rsn.2013.0053}
}
```

Note on the key. Brennan et al. (2014) is the primary engineering reference for the
ApRES instrument and its phase-sensitive FMCW design, and is the natural anchor for
paragraph 2's phase-precision claim. If Andrew prefers a lighter citation load,
paragraph 2 reads fine on `nicholls2015` alone (which also describes the instrument),
and the `brennan2014` entry can be dropped.

**Figure proposals:**

The course-deck figure pool (`~/Downloads/glaciology-course-uw`) was **not mounted on
this run** (checked: only the book repo, outputs, and uploads are mounted; `~/Downloads`
absent), so no deck image/slide is cataloged. One *original* schematic is proposed, to
be generated with matplotlib in the style of the existing `_dev/make-*.py` figures (no
third-party attribution required because it would be drawn fresh).

1. **FMCW beat frequency and the phase refinement (two-panel schematic).** Left panel:
   outgoing linear frequency sweep (frequency vs time) and the delayed return, with the
   constant frequency offset $f_b$ between them marked, and an annotation $f_b=(2R/c)
   (B/T)$ tying the offset to range. Right panel: a single reflector's complex return
   drawn as a phasor (or as amplitude with a phase tick), with the coarse range bin
   $\Delta R=c/2B\approx0.4$ m drawn as a wide grey band and the phase-resolved
   position drawn as a ~1 mm tick inside it, to make visual the >2-orders-of-magnitude
   gap between amplitude resolution and phase precision that paragraphs 1–2 derive.
   Origin: original figure (to be drafted) — no attribution needed.

If a future run has the decks mounted, search the radar / radio-echo-sounding / ApRES
deck media for a real ApRES depth-amplitude profile, a strain-rate-vs-depth plot, or a
basal-melt time series, and catalog it with its *original* publication source (e.g.
{cite}`nicholls2015` or a BAS field-study figure with the data provider credited)
following rule 2 — never the course.

**Detector gate:** `PASS  /sessions/.../outputs/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

## 2026-06-16 (run 15) — sections/radar/em-waves.md

**Why this section:** the "Attenuation and the limits of the window" subsection is
the chapter's only wholly qualitative passage. It states that ionic defects "absorb
a little of the wave," that attenuation "increases with temperature" and with acid
impurities, that a radar "can sound several kilometres of cold ice but is quickly
defeated" by temperate ice, and that "the attenuation of the returning signal itself
carries information about the temperature" — all true, none quantified. The
companion {doc}`../foundations/optical-properties` already carries the *molecular*
side (Debye relaxation, Arrhenius relaxation time, the order-of-magnitude-per-20 K
plateau drop, the impurity floor) and even owns the attenuation-temperature figure;
its caption explicitly defers the application to "{doc}`../radar/em-waves` and the
radar chapters that follow." So this section should supply the missing *propagation*
side rather than repeat the molecular origin: how the imaginary permittivity becomes
an exponential decay, what the field attenuation coefficient is in the low-loss
limit, the order of the one-way loss, and the two-way decibel budget against the
receiver noise floor that actually sets sounding depth. Paragraph 1 does that.
Paragraph 2 then quantifies the temperature/impurity dependence (Arrhenius, ~×10 per
20 K, consistent with the optical-properties caption) and turns it into the
attenuation-as-thermometer inversion, with the primary modelling citations the
existing prose lacks. Consulted the radioglaciology reference {cite}`bogorodsky1985`
and {cite}`petrenko1999` (already in references.bib and already cited by the chapter);
prose is original. (The radioglaciology PDF in the Drive textbooks folder is a
~108 MB scanned scan with no extractable text, so the physics was grounded against
the book's own already-vetted optical-properties treatment and standard low-loss
dielectric propagation rather than transcribed from it — no copying risk.)

**Proposed placement:** both paragraphs into the existing "## Attenuation and the
limits of the window" subsection. Paragraph 1 directly after the present opening
sentence "The radar window is not perfectly transparent." (which it quantifies), and
*before* the existing "The absorption increases with temperature…" sentence.
Paragraph 2 then *replaces* the chapter's current two temperature/impurity sentences
("The absorption increases with temperature… the wet, warm ice of a temperate
glacier.") and its final thermometer sentence ("The temperature dependence is strong
enough that the attenuation of the returning signal itself carries information about
the temperature of the ice column."), folding both into a mechanistic, cited
version. If Andrew would rather keep the existing sentences, paragraph 2 can instead
be appended after them, but they would then partly duplicate it.

**Drafted prose (gate-passing, verbatim):**

> The loss is set by the imaginary part of the permittivity, which converts a fixed
> fraction of the wave's power into heat over each metre travelled, so the field
> amplitude decays as $e^{-\alpha z}$ and the power as $e^{-2\alpha z}$ with distance
> $z$ into the ice. In the low-loss radar window the field attenuation coefficient
> reduces to $\alpha \approx \sigma/(2\epsilon_0 c\,n)$, fixed by the small
> high-frequency conductivity $\sigma$ and divided by the refractive index. This
> conductivity changes little across the sounding band, so the loss is nearly flat in
> frequency and a single attenuation rate describes a broadband pulse. In cold polar
> ice the one-way loss is of order ten decibels per kilometre, so a bed echo from
> three kilometres of ice travels six kilometres down and back and is reduced by many
> tens of decibels through absorption alone, before the geometric spreading of the
> beam and the partial reflection at the bed are counted. That total, measured against
> the noise floor of the receiver, fixes the greatest depth the instrument can sound.

> The conductivity that sets the loss is the ionic conduction of
> {doc}`../foundations/point-defects`, and it climbs along an Arrhenius law with
> temperature and with the concentration of acidic impurities. Warming the ice by
> twenty degrees raises the loss by roughly an order of magnitude, so the few
> additional decibels per kilometre in warm or temperate ice exhaust the power budget
> within a few hundred metres, while the same radar sounds several kilometres of cold
> ice. The dependence also works in reverse as a measurement. The attenuation
> accumulated along a ray is the integral of the local loss, so the rate at which the
> returned power from internal layers and the bed falls off with depth constrains the
> temperature and chemistry of the ice it passed through {cite}`macgregor2007`. The
> loss has to be modelled this way before the strength of the bed echo can be read as
> a property of the bed rather than of the ice above it {cite}`matsuoka2011`.

**Numerical check (for Andrew, not for the prose):** low-loss field coefficient
$\alpha=\sigma/(2\epsilon_0 c n)$. With $\sigma\sim 1\times10^{-5}$ S m⁻¹ (cold-ice
high-frequency-limit conductivity), $\epsilon_0=8.854\times10^{-12}$, $c=3\times10^8$,
$n=1.78$: $\alpha\approx1.06\times10^{-3}$ Np m⁻¹. One-way power loss
$=2\alpha\times8.686$ dB ≈ **18 dB/km**; for the colder, cleaner ice deeper in a polar
column ($\sigma\sim5\times10^{-6}$) it is ≈ 9 dB/km — hence "of order ten decibels per
kilometre." A 3 km bed (6 km two-way path) then loses ~50–110 dB to absorption alone,
consistent with the published total radar loss budgets, and temperate ice with
$\sigma\sim10^{-4}$ gives ~180 dB/km one-way, defeating the sounding within a few
hundred metres. (The $\omega$ in $\alpha=(\omega/c)\,\epsilon''/2n$ cancels against
$\sigma=\omega\epsilon_0\epsilon''$, which is why the conduction loss is
frequency-flat across the plateau — the third sentence of paragraph 1.)

**Proposed new BibTeX entries** (`bogorodsky1985`, `petrenko1999` already in
references.bib — verified by grep; the two below are not — verified by grep, no
`macgregor`/`matsuoka` keys present):

```bibtex
@article{macgregor2007,
  author  = {MacGregor, J. A. and Winebrenner, D. P. and Conway, H. and
             Matsuoka, K. and Mayewski, P. A. and Clow, G. D.},
  title   = {Modeling englacial radar attenuation at {Siple} {Dome}, {West}
             {Antarctica}, using ice chemistry and temperature data},
  journal = {Journal of Geophysical Research: Earth Surface},
  year    = {2007},
  volume  = {112},
  number  = {F3},
  pages   = {F03008},
  doi     = {10.1029/2006JF000717}
}

@article{matsuoka2011,
  author  = {Matsuoka, Kenichi},
  title   = {Pitfalls in radar diagnosis of ice-sheet bed conditions: Lessons
             from englacial attenuation models},
  journal = {Geophysical Research Letters},
  year    = {2011},
  volume  = {38},
  number  = {5},
  pages   = {L05505},
  doi     = {10.1029/2010GL046205}
}
```

Notes on the keys. MacGregor et al. (2007) is the standard primary reference for
forward-modelling englacial radar attenuation from a measured temperature-and-
chemistry profile and is the natural anchor for the "thermometer" sentence; the
later MacGregor et al. (2015, *J. Geophys. Res. Earth Surf.* 120, on Greenland
radiostratigraphy and attenuation) is an alternative if Andrew prefers a Greenland
example. Matsuoka (2011) makes paragraph 2's last point — that englacial loss must
be modelled before a bed echo's strength can be attributed to basal conditions — and
is the canonical caution on that inversion. Both are pre-2025 and widely cited. If
Andrew wants a lighter citation load, paragraph 2 reads fine on `macgregor2007`
alone and the final sentence (with `matsuoka2011`) can be dropped, since the bed-
reflectivity caveat is also developed where the chapters reach basal conditions.

**Figure proposals:**

The course-deck figure pool (`~/Downloads/glaciology-course-uw`) was **not mounted on
this run** (checked: `~/Downloads` absent; only the book repo, outputs, and uploads
are mounted), so no deck image/slide is cataloged. One *original* schematic is
proposed, to be generated with matplotlib in the style of the existing
`_dev/make-*.py` figures (no third-party attribution required because it would be
drawn fresh). Note that the *molecular* attenuation-vs-temperature figure already
exists and lives in {doc}`../foundations/optical-properties`
(`figures/ice-attenuation-temperature.png`, from
`_dev/make-ice-attenuation-temperature-figure.py`); the proposal below is the
complementary *propagation/budget* figure that this chapter currently lacks, and it
should be cross-referenced to, not duplicated from, the optical-properties one.

1. **Two-way power budget versus depth (the sounding-depth ceiling).** Returned
   power in decibels on the vertical axis against ice depth on the horizontal, one
   curve combining the linear two-way absorption loss (slope ≈ −2 × one-way dB/km)
   with the geometric-spreading roll-off, drawn for two cases: cold polar ice
   (≈ 9–18 dB/km one-way) reaching several kilometres before crossing the receiver
   noise floor, and warm/temperate ice (≈ 100–180 dB/km one-way) crossing it within a
   few hundred metres. Mark the noise floor as a horizontal line and the
   maximum-sounding-depth where each curve meets it. This makes paragraph 1's budget
   argument and paragraph 2's "defeated by temperate ice" contrast visual in one
   panel. Origin: original figure (to be drafted) — no attribution needed.

If a future run has the decks mounted, search the radar / radio-echo-sounding /
ice-penetrating-radar deck media for a real radargram showing internal layers fading
with depth or a bed echo, or an attenuation-rate map, and catalog it with its
*original* publication source (e.g. {cite}`macgregor2007` or a BAS/CReSIS radargram
with the data provider credited) following rule 2 — never the course.

**Detector gate:** `PASS  /sessions/.../outputs/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

## 2026-06-16 (run 14) — sections/cryosphere/instabilities.md

**Why this section:** the tidewater half of the chapter rests on one quantitative
claim it never explains. The retreat paragraph states that "calving rate increases
sharply with water depth, so retreat begets deeper water and deeper water begets
faster retreat," and the closing "Common structure" section abstracts this to
"mass conservation plus a flux law with the wrong sign of slope somewhere," but
the chapter never says *why* calving scales with depth (the flotation /
height-above-buoyancy control on terminus grounding) nor *why* an overdeepening
has no stable terminus position (the reverse-slope feedback). Two short paragraphs
supply both, the first deepening the water-depth/calving assertion, the second the
overdeepening instability, and they tie the result to the marine grounding-line
flux argument the chapter already invokes by analogy ({cite}`schoof2007`, already
in references.bib). Consulted Cuffey & Paterson Ch. 12 ({cite}`cuffey2010`) on the
tidewater cycle; prose is original.

**Proposed placement:** in "## The tidewater glacier cycle", both paragraphs in the
"The retreat is the fast half of the cycle" discussion. Paragraph 1 belongs *before*
the existing "A modest perturbation…" sentence, establishing the flotation control
on calving so that the depth-feedback sentence that follows reads as a consequence
rather than an assertion; it lets the existing "Calving rate increases sharply with
water depth, so retreat begets deeper water…" sentence be trimmed to a one-line
restatement, or removed, since paragraph 1 now carries it. Paragraph 2 belongs
*after* that sentence (before the Helheim video), making the no-stable-position
claim explicit and setting up the {doc}`ice-sheets` marine-instability cross-link
the "Common structure" section later leans on. Neither paragraph restates the
sediment-shoal advance mechanism, which stays in the existing advancing-phase
paragraph.

**Drafted prose (gate-passing, verbatim):**

> The link between calving and water depth, asserted above, follows from how a
> grounded terminus approaches flotation. Ice ending in the sea thins toward the
> front, and a grounded terminus stays in contact with the bed only while its
> thickness exceeds the flotation value, roughly one and a tenth times the water
> depth. A deeper basin therefore requires a thicker terminus to remain grounded,
> and a small thinning at the front is enough to lift weakly grounded ice off the
> bed, where it breaks away in large blocks. Surveys across many Alaskan tidewater
> glaciers found the calving speed to rise roughly in proportion to the water depth
> at the face {cite}`brown1982`, and the height-above-buoyancy models that followed
> place the terminus where the grounded thickness exceeds the flotation thickness
> by a set margin, so that thinning at the front is answered by retreat into the
> basin {cite}`vanderveen1996`. Warm seawater reaching a deep face adds to the loss,
> melting and undercutting the ice below the waterline and steepening the cliff
> above until it fails under its own weight.

> Set on a bed that deepens toward the fjord head, this dependence has no resting
> point. While the terminus sits on its sediment shoal the water is shallow and
> calving is slow, so the position is stable and the glacier can hold or advance.
> Once a few warm summers thin the terminus enough to retreat it off the shoal, it
> enters the overdeepened basin, where greater depth quickens the calving, which
> thins and retreats the front into still deeper water and quickens the calving
> once more. Each step of retreat raises the loss that caused it, and the terminus
> cannot settle anywhere the bed continues to deepen inland, the same reverse-slope
> condition that destabilises a marine grounding line {cite}`schoof2007`. The
> retreat halts only where the bed rises again toward the head of the fjord, the
> water shallows, and calving falls back into balance with the ice supplied from
> upstream {cite}`pfeffer2007,meier1987`.

**Proposed new BibTeX entries** (`schoof2007`, `pfeffer2007`, `meier1987`,
`cuffey2010` already in references.bib — verified by grep; the two below are not):

```bibtex
@article{brown1982,
  author  = {Brown, C. S. and Meier, M. F. and Post, A.},
  title   = {Calving speed of {Alaska} tidewater glaciers, with application to
             {Columbia} {Glacier}},
  journal = {U.S. Geological Survey Professional Paper},
  year    = {1982},
  volume  = {1258-C},
  pages   = {C1--C13},
  doi     = {10.3133/pp1258C}
}

@article{vanderveen1996,
  author  = {van der Veen, C. J.},
  title   = {Tidewater calving},
  journal = {Journal of Glaciology},
  year    = {1996},
  volume  = {42},
  number  = {141},
  pages   = {375--385},
  doi     = {10.3189/S0022143000004226}
}
```

Notes on the keys. Brown, Meier & Post (1982) is the standard primary reference for
the empirical linear calving-speed-versus-water-depth relation across Alaskan
tidewater glaciers, the result paragraph 1 attributes to "surveys across many
Alaskan tidewater glaciers"; van der Veen (1996) is the canonical height-above-
buoyancy ("flotation") calving model. Both are pre-2025 and widely cited. If Andrew
prefers a lighter citation load, paragraph 1 reads fine on {cite}`vanderveen1996`
alone (the flotation argument), and the empirical relation is also summarised in
{cite}`cuffey2010` Ch. 12 if he would rather not add `brown1982`. A more recent
alternative framing is Benn, Warren & Mottram (2007), *Calving processes and the
dynamics of calving glaciers*, Earth-Science Reviews 82, 143–179 — not added here,
but worth considering if Andrew wants the crevasse-depth / strain-rate calving
criterion alongside the flotation one.

**Figure proposals:**

The course-deck figure pool (`~/Downloads/glaciology-course-uw`) was **not mounted
on this run** (checked: `~/Downloads` absent; only the book repo, outputs, and
uploads are mounted), so no deck image/slide is cataloged. Two *original* schematics
are proposed, to be generated with matplotlib in the style of the existing
`_dev/make-*.py` figures (no third-party attribution required because they would be
drawn fresh):

1. **Flotation / height-above-buoyancy terminus.** A long-section of a tidewater
   terminus: bedrock, a water column of depth D_w, and an ice column of thickness H
   thinning toward the front, with the flotation thickness H_f ≈ 1.1·D_w drawn as a
   reference line. Show one panel grounded (H > H_f, ice gripping the bed) and one
   at the point of calving (H → H_f, terminus lifting free), annotated to make
   paragraph 1's depth dependence visual: deeper water raises H_f, so a deeper basin
   needs thicker ice to stay grounded. Origin: original figure (to be drafted) — no
   attribution needed.
2. **Overdeepening retreat instability.** A fjord long-profile bed with a sediment
   shoal at the mouth, an overdeepened basin behind it, and the bed rising again
   toward the head; beneath it, a curve of calving rate (or water depth) versus
   terminus position showing stable points on the shoal and at the head and an
   unstable run-away through the basin where the bed deepens inland. Mirrors the
   marine-ice-sheet grounding-line schematic so the {doc}`ice-sheets` analogy is
   visible. Illustrates paragraph 2. Origin: original figure (to be drafted) — no
   attribution needed.

If a future run has the decks mounted, search the tidewater / calving / Columbia–
Glacier deck media for a real Columbia Glacier retreat map, a bed long-profile with
the overdeepening, or a calving-front photo, and catalog it here with its *original*
publication or photographer source — e.g. {cite}`berthier2010` or {cite}`pfeffer2007`
for the retreat record, USGS for Columbia bathymetry — following rule 2 (credit the
paper or photographer, never the course).

**Detector gate:** `PASS  /sessions/.../outputs/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

## 2026-06-16 (run 13) — sections/observing/panchromatic-imagery.md

**Why this section:** thin (≈551 words) and almost wholly qualitative. The two
core measurements — stereo elevation and feature-tracking velocity — are
described by analogy (binocular parallax; cross-correlating a patch) but the
*measurement physics* that governs their accuracy is never stated: what sets the
height precision of a stereo pair, why matching fails over the smooth interior,
what sets the velocity error, and why the time interval between images is a
constrained choice. Two short paragraphs supply that physics. Paragraph 1
deepens "Elevation from stereo"; paragraph 2 deepens "Velocity from feature
tracking". Consulted Cuffey & Paterson Ch. 4/5 on remote velocity measurement
({cite}`cuffey2010`) and the SETSM stereo-DEM literature; prose is original.

**Proposed placement:** Paragraph 1 appended to the "## Elevation from stereo"
subsection (after the sentence ending "…how thinning is mapped over the rugged
outlet glaciers that altimeters resolve poorly."). Paragraph 2 appended to the
"## Velocity from feature tracking" subsection (after the sentence introducing
the cross-correlation displacement, before the lab-pointer sentence). Neither
restates the qualitative setup already in those paragraphs.

**Drafted prose (gate-passing, verbatim):**

> The precision of a stereo elevation depends on the geometry of the two views.
> The height of a point is recovered from the parallax between the images, the
> small shift in its image position produced by the difference in viewing angle,
> and a given error in measuring that shift maps to a vertical error that scales
> with the ratio of the flying height to the separation between the two camera
> positions. A wider convergence angle between the views therefore sharpens the
> height, but it also makes the two images less alike in perspective and
> shadowing, which degrades the matching that the parallax is measured from, so
> the geometry is chosen as a compromise. The matching itself fails where the
> surface carries no texture to fix on. Bare ice, crevasse fields, and exposed
> rock yield strong, well-defined heights, whereas smooth dry firn returns a
> weak and noisy correlation, and the resulting elevation models are most
> reliable over rough terrain and degrade over the featureless interior
> {cite}`noh2017`.

> The displacement recovered by cross-correlation is located to a fraction of a
> pixel by fitting the peak of the correlation surface, so the error in the
> measured displacement is roughly fixed in ground units, a fraction of the
> pixel size, however far the surface has moved. The velocity is that
> displacement divided by the time between images, and its fractional error
> therefore falls as the interval lengthens, which favours widely separated
> acquisitions. Working against this is the survival of the tracked features.
> Over a long interval the patches rotate and stretch with the flow, and they
> are eventually buried by snowfall or melted away, and once they no longer
> resemble their earlier form the correlation peak collapses and the measurement
> is lost. The usable interval is set by the balance between these two limits,
> and it is shortest on the fast, heavily crevassed glaciers where the velocity
> is highest and changes most quickly {cite}`scambos1992`.

**Proposed new BibTeX entry** (`scambos1992`, `cuffey2010`, `howat2019` already
in references.bib; verify `noh2017` below):

```bibtex
@article{noh2017,
  author  = {Noh, Myoung-Jong and Howat, Ian M.},
  title   = {The Surface Extraction from {TIN}-based Search-space Minimization
             ({SETSM}) algorithm},
  journal = {ISPRS Journal of Photogrammetry and Remote Sensing},
  year    = {2017},
  volume  = {129},
  pages   = {55--76},
  doi     = {10.1016/j.isprsjprs.2017.04.019}
}
```

Noh & Howat (2017) is the standard primary reference for the fully-automatic
stereo-photogrammetric DEM extraction behind REMA/ArcticDEM, and it explicitly
treats the low-contrast / repeated-texture matching problem over snow and ice —
exactly the texture-dependence point in paragraph 1. An alternative companion is
Noh & Howat (2015), *Automated stereo-photogrammetric DEM generation at high
latitudes: SETSM validation and demonstration over glaciated regions*, GIScience
& Remote Sensing 52(2), 198–217 — not added to avoid an unneeded key.

**Figure proposals:**

The course-deck figure pool (`~/Downloads/glaciology-course-uw`) was **not
mounted on this run** (checked: `~/Downloads` absent; only the book repo,
outputs, and uploads are mounted), so no deck image/slide is cataloged. Rather
than guess a provenance, two *original* schematics are proposed, to be generated
with matplotlib in the style of the existing `_dev/make-*.py` figures (no
third-party attribution required because they would be drawn fresh):

1. **Stereo base-to-height geometry.** A single ground point viewed from two
   satellite positions separated by a base B at flying height H, showing the
   parallax in the image plane and the convergence angle, with a small inset
   illustrating how a fixed image-plane matching error δp maps to a vertical
   error δz ≈ δp·(H/B). Illustrates paragraph 1. Origin: original figure (to be
   drafted) — no attribution needed.
2. **Feature-tracking time-interval trade-off.** Two curves against the
   image-pair time interval Δt: velocity error falling as 1/Δt, and a
   feature-survival / decorrelation term rising with Δt, with their sum showing
   an optimum, annotated for a slow interior site versus a fast crevassed outlet
   glacier. Illustrates paragraph 2. Origin: original figure (to be drafted) —
   no attribution needed.

If a future run has the decks mounted, search the optical / remote-sensing deck
media for a real stereo-geometry diagram or a Landsat/WorldView feature-tracking
velocity map and catalog it here with its *original* source (e.g. the relevant
journal paper or USGS/Maxar imagery credit), following rule 2.

**Detector gate:** `PASS  /sessions/.../outputs/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

## 2026-06-16 — sections/observing/radar-altimetry.md

**Why this section:** thin (≈549 words) and the central physical mechanism it
leans on — that microwaves scatter from *within* the snowpack, biasing the
height — is asserted ("a penetration correction accounts for the part of the
echo that comes from scattering within the snow") but never developed. Two short
paragraphs supply that physics and the trend-contamination it causes. Aligns
with the radioglaciology basis already in {doc}`../radar/em-waves`.

**Proposed placement:** expand the existing "Retracking and the penetration
correction" section. Paragraph 1 follows the sentence introducing the penetration
correction; paragraph 2 closes the subsection and leads into "Glaciological
applications".

**Drafted prose (gate-passing, verbatim):**

> The echo comes from within the snow as well as from its surface, a consequence
> of the dielectric behaviour developed in {doc}`../radar/em-waves`. Dry polar
> firn absorbs microwaves only weakly, so a Ku-band pulse penetrates several
> metres before its energy returns, and the reflection forms throughout a volume
> rather than at a single interface, from the permittivity contrasts between firn
> layers of differing density and from scattering by individual grains. The
> recorded waveform is then the sum of a surface return and a volume return
> integrated over a span of depths, and the effective scattering horizon sits
> below the true surface by an amount that grows as the firn becomes more
> transparent. The penetration is limited by two properties of the snow.
> Absorption, set by the imaginary part of the permittivity, rises steeply with
> temperature and with any trace of liquid water. Volume scattering rises with
> grain size and with frequency, so a higher-frequency Ka-band altimeter scatters
> more strongly in the uppermost snow and penetrates less than a Ku-band one
> {cite}`ridley_partington1988`.

> Because the scattering horizon depends on the state of the snow, anything that
> alters absorption or scattering moves the apparent surface and can be mistaken
> for a change in elevation. A summer of surface melt, or a run of warm years,
> raises absorption and confines the return toward the surface, lifting the
> retracked height. A return to cold, dry conditions lowers it again. Variations
> of this kind, correlated with temperature, can imprint a false signal on an
> elevation record at the centimetre-to-decimetre level, comparable in size to
> the climate trends the altimeter is built to detect. Separating the true height
> change from the migrating scattering horizon is the central difficulty of the
> radar record, and it is approached by retracking the waveform shape, by
> combining frequencies or polarisations that penetrate differently, and by
> cross-calibrating against the laser altimetry of {doc}`laser-altimetry-lab`,
> whose optical pulse reflects at the surface itself {cite}`wingham2006`.

**Proposed new BibTeX entry** (verify; `wingham2006` already in references.bib):

```bibtex
@article{ridley_partington1988,
  author  = {Ridley, J. K. and Partington, K. C.},
  title   = {A model of satellite radar altimeter return from ice sheets},
  journal = {International Journal of Remote Sensing},
  year    = {1988},
  volume  = {9},
  number  = {4},
  pages   = {601--624},
  doi     = {10.1080/01431168808954881}
}
```

The Ridley & Partington (1988) waveform model is the standard primary reference
for the surface-plus-volume return of a radar altimeter over an ice sheet. An
alternative or companion citation worth considering is Davis (1993),
*A surface and volume scattering retracking algorithm for ice sheet satellite
altimetry*, IEEE TGRS 31(4), 811–818 — not added here to avoid proposing keys the
section does not need.

**Figure proposals:**

The course-deck figure pool (`~/Downloads/glaciology-course-uw`) was **not
mounted on this run**, so no deck image/slide is cataloged. Rather than guess a
provenance, two *original* schematics are proposed, to be generated with
matplotlib in the style of the existing `_dev/make-*.py` figures (no third-party
attribution required because they would be drawn fresh):

1. **Return-waveform schematic.** Power-vs-time echo over firn, decomposed into a
   surface return (sharp leading edge) and a broader volume-scattering tail, with
   the retracking point and the apparent vs true surface marked. Illustrates
   paragraph 1. Origin: original figure (to be drafted) — no attribution needed.
2. **Penetration-bias cartoon.** Two snow columns, warm/wet vs cold/dry, showing
   the scattering horizon migrating upward as absorption rises, and the resulting
   spurious elevation change. Illustrates paragraph 2. Origin: original figure
   (to be drafted) — no attribution needed.

If a future run has the decks mounted, search the radar/altimetry deck media for
a real ERS/CryoSat waveform or SARIn-geometry figure and catalog it here with its
*original* source (e.g. ESA mission documentation or Wingham et al. 2006),
following rule 2.

**Detector gate:** `PASS  /tmp/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

## 2026-06-16 (run 2) — sections/foundations/snow-to-ice.md

**Why this section:** the "Densification" section (chapter "Firn densification",
≈685 words) states the Herron–Langway stages — grain rearrangement to ~550, slow
sintering to ~830 and pore close-off, bubble compression to 917 — but never gives
the *mechanism*: what stress drives densification, why the rate slows between
stages, why close-off depth varies, or why deep bubbles are overpressured. Two
short paragraphs supply that physics and tie it to the power-law creep of
{doc}`../ice_flow/ice-rheology`. Consulted Cuffey & Paterson Ch. 2
({cite}`cuffey2010`, Drive id 1SGFrZvQ31aBeHa_OG4d9hofCAtuDs9Gp) and the standard
mechanism literature; prose is original.

**Proposed placement:** in the "## Densification" section, immediately after the
three-stage paragraph (the one ending "…slow compression of the trapped
bubbles."), before the Siple-pit `{figure}`. Both paragraphs deepen the mechanism
that the preceding paragraph describes phenomenologically; they do not restate the
stage boundaries (those stay in the existing paragraph). If Andrew prefers, the
small overlap on stage 1 ("rearrange and pack more tightly" ↔ "sliding past one
another and rotating") can be trimmed from the existing paragraph and owned here.

**Drafted prose (gate-passing, verbatim):**

> The driving stress for densification is the weight of the snow accumulated
> above, which presses the grains together with a load that grows with depth. In
> the first stage the grains respond by sliding past one another and rotating into
> tighter arrangements, a rearrangement that needs little force and proceeds
> quickly until the packing approaches the densest that rounded grains can reach
> without deforming, near 550 kg per cubic metre. Closer packing then requires the
> grains themselves to deform. In the second stage the overburden is carried
> across the contacts between grains, where the local stress is large enough to
> drive the power-law creep of ice described in {doc}`../ice_flow/ice-rheology`,
> while material is also carried into the necks between grains by diffusion along
> the grain boundaries. The densification slows as the firn compacts, because the
> load is spread over a growing area of grain contact and the pore space that
> remains is harder to close {cite}`maeno1983,arnaud2000`.

> The empirical model of {cite}`herron1980` represents this behaviour without
> solving the creep problem directly. It takes the rate of densification to be
> proportional to the remaining pore space and to the overburden load, with
> separate coefficients for the two stages and an Arrhenius dependence on
> temperature, and it is calibrated against firn cores spanning a wide range of
> polar conditions. The same dependence accounts for the wide variation in the
> depth of pore close-off. A colder site densifies more slowly under a given load,
> and a higher accumulation rate buries a layer to a given depth in less time, so
> both a low temperature and a high accumulation rate place close-off deeper. Below
> close-off the air no longer escapes, and further compression raises the pressure
> of the trapped bubbles until it approaches the overburden, so the density rises
> only slowly towards that of bubble-free ice and the gas at depth remains above
> atmospheric pressure {cite}`cuffey2010`.

**Proposed new BibTeX entries** (neither key is in references.bib; `herron1980`,
`cuffey2010` already present — verify the two below):

```bibtex
@article{maeno1983,
  author  = {Maeno, Norikazu and Ebinuma, Takao},
  title   = {Pressure sintering of ice and its implication to the densification
             of snow at polar glaciers and ice sheets},
  journal = {Journal of Physical Chemistry},
  year    = {1983},
  volume  = {87},
  number  = {21},
  pages   = {4103--4110},
  doi     = {10.1021/j100244a023}
}

@incollection{arnaud2000,
  author    = {Arnaud, La{\"u}rent and Barnola, Jean-Marc and Duval, Paul},
  title     = {Physical modeling of the densification of snow/firn and ice in the
               upper part of polar ice sheets},
  booktitle = {Physics of Ice Core Records},
  editor    = {Hondoh, Takeo},
  publisher = {Hokkaido University Press},
  address   = {Sapporo},
  year      = {2000},
  pages     = {285--305}
}
```

Maeno & Ebinuma (1983) is the canonical pressure-sintering treatment of the
stage-2 mechanism; Arnaud, Barnola & Duval (2000) is the standard physical
(as opposed to empirical) densification model distinguishing grain-boundary
sliding in the first stage from creep-plus-sintering in the second. Both are
pre-2025 and widely cited. If Andrew would rather keep the citation load light,
the paragraph reads fine citing only {cite}`maeno1983` at the first-stage/second-
stage hinge, or even only {cite}`cuffey2010,herron1980` (both already in the bib),
since the chapter already attributes the staged description to those two.

**Figure proposals:**

The course-deck pool (`~/Downloads/glaciology-course-uw`) was **not mounted on
this run**, so no deck image/slide is cataloged. One *original* figure is
proposed, to be generated with matplotlib in the style of `_dev/make-text-figures.py`
(no third-party attribution required, drawn fresh):

1. **Densification curve (Herron–Langway).** Relative density (or density, 400 →
   917 kg m⁻³) against depth (or age), drawn for two contrasting sites — a cold,
   low-accumulation interior column (deep close-off) and a warm, high-accumulation
   column (shallow close-off) — using the {cite}`herron1980` two-stage equations.
   Mark the stage-1/stage-2 break near 550 and the close-off density ~830, and
   shade the bubbly-ice stage above 830. Illustrates both drafted paragraphs and
   makes the close-off-depth dependence visual. Origin: original figure (to be
   drafted) — no attribution needed.

If a future run has the decks mounted, search the firn/ice-core deck media for a
real measured firn-density-vs-depth profile (e.g. a polar core such as Siple Dome
or a Greenland/EPICA core) and catalog it here with its *original* publication
source, following rule 2; the existing chapter already carries the Siple-pit photo
(R. Tremblay) and the Benson–Müller facies figure ({cite}`paterson1994`).

**Detector gate:** `PASS  /sessions/.../outputs/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

## 2026-06-16 (run 3) — sections/observing/cryoseismicity.md

**Why this section:** thin (≈641 words) and its central mechanism is asserted but
never explained. The "sources of icequakes" paragraph says basal events come from
"a stick-slip motion in which stress builds while the bed is locked and releases in
an abrupt slip," and the applications section describes the Whillans tidal slips in
detail, but nothing states *why* a bed slips in jerks rather than gliding — i.e. the
mechanical condition that separates steady sliding from stick-slip. The friction-law
chapter {doc}`../thermomechanics/basal-motion` supplies the steady drag–speed
relations (Weertman, Coulomb, plastic till) but never their stability under a small
perturbation. Two short paragraphs close that gap: one gives the velocity-weakening
vs velocity-strengthening criterion and links it to the friction laws already in the
book; one applies it to the Whillans tidal cycle the section already cites
informally. Consulted Cuffey & Paterson Ch. 7 ({cite}`cuffey2010`) on basal motion
and the till-plasticity result of {cite}`zoet2020` already in references.bib; the
Whillans observations are attributed to their primary papers (proposed below).

**Proposed placement:** in "## The sources of icequakes", as a new short subsection
or two paragraphs immediately after the sentence introducing basal stick-slip
("…how that is modulated by the tide and the season."). Paragraph 1 supplies the
general mechanism; paragraph 2 grounds it in Whillans and sets up the existing
"Glaciological applications" discussion of the twice-daily slips, removing the need
to re-explain the mechanism there. The applications paragraph can then simply refer
back rather than restate "stick-slip behaviour invisible to any surface measurement."

**Drafted prose (gate-passing, verbatim):**

> Whether a glacier bed slides steadily or in sudden jerks is set by how its
> resistance changes as the ice begins to move. The friction laws of
> {doc}`../thermomechanics/basal-motion` give the steady relation between basal
> drag and sliding speed, but they also govern the response to a small
> perturbation. Where the drag rises with sliding speed, a patch that begins to
> move meets greater resistance and decelerates, so the motion stays smooth and the
> bed creeps forward at the rate the driving stress demands. Where the drag instead
> falls once slip begins, as it does on a near-plastic till bed or on a frozen patch
> that has just yielded, the resistance drops below the stress the surrounding ice
> imposes, and the elastic strain stored in that ice drives the patch to accelerate.
> It slips by a finite amount in seconds, radiating the seismic wave, until the
> falling driving stress and the recovery of resistance bring it to rest and the
> patch locks again. Stress then rebuilds over hours to days until the threshold is
> reached once more {cite}`cuffey2010,zoet2020`.

> On Whillans Ice Stream the loading that brings the bed to failure includes the
> ocean tide. The stream is held by a few sticky patches on an otherwise weak till
> bed, and the rise and fall of the tide at its grounding line changes the
> back-stress transmitted upstream and the effective pressure on the till, carrying
> the locked patches across their failure threshold roughly twice a day
> {cite}`bindschadler2003,wiens2008`. Each slip moves the whole lower stream about
> half a metre in under half an hour and then arrests, after which the steady
> driving stress and the next tidal cycle reload the bed for the following event.
> The recurrence of the slips, and their timing within the tidal cycle, therefore
> record the strength of the bed and the effective pressure on it, quantities that
> no surface measurement of the mean velocity can supply {cite}`winberry2009`.

**Proposed new BibTeX entries** (none of the three keys is in references.bib;
`cuffey2010` and `zoet2020` already present — verify the three below):

```bibtex
@article{bindschadler2003,
  author  = {Bindschadler, Robert A. and King, Matt A. and Alley, Richard B. and
             Anandakrishnan, Sridhar and Padman, Laurence},
  title   = {Tidally controlled stick-slip discharge of a West Antarctic ice stream},
  journal = {Science},
  year    = {2003},
  volume  = {301},
  number  = {5636},
  pages   = {1087--1089},
  doi     = {10.1126/science.1087231}
}

@article{wiens2008,
  author  = {Wiens, Douglas A. and Anandakrishnan, Sridhar and
             Winberry, J. Paul and King, Matt A.},
  title   = {Simultaneous teleseismic and geodetic observations of the stick-slip
             motion of an Antarctic ice stream},
  journal = {Nature},
  year    = {2008},
  volume  = {453},
  number  = {7196},
  pages   = {770--774},
  doi     = {10.1038/nature06990}
}

@article{winberry2009,
  author  = {Winberry, J. Paul and Anandakrishnan, Sridhar and Alley, Richard B. and
             Bindschadler, Robert A. and King, Matt A.},
  title   = {Basal mechanics of ice streams: Insights from the stick-slip motion of
             {Whillans} {Ice} {Stream}, {West} {Antarctica}},
  journal = {Journal of Geophysical Research: Earth Surface},
  year    = {2009},
  volume  = {114},
  number  = {F1},
  pages   = {F01016},
  doi     = {10.1029/2008JF001035}
}
```

Bindschadler et al. (2003) is the discovery paper for tidally triggered stick-slip
on Whillans; Wiens et al. (2008) ties the teleseismic glacial-earthquake signal to
the geodetically measured slip; Winberry et al. (2009) is the mechanical analysis of
the slip cycle and bed strength. All pre-2025 and widely cited. If Andrew prefers a
lighter citation load, paragraph 2 reads fine citing only {cite}`bindschadler2003`
at the tidal-trigger clause and {cite}`winberry2009` at the close; `podolskiy2016`
and `aster2017` (already cited in the section's opening) also review this material
and could substitute for the primary papers if he would rather not add keys.

**Figure proposals:**

The course-deck pool (`~/Downloads/glaciology-course-uw`) was **not mounted on this
run**, so no deck image/slide is cataloged. One *original* figure is proposed, to be
generated with matplotlib in the style of the existing `_dev/make-*.py` scripts (no
third-party attribution required, drawn fresh):

1. **Stick-slip stability schematic.** A two-panel drag-vs-speed (friction law)
   sketch: left panel velocity-strengthening (drag rises with $u_b$, the operating
   point is stable, arrows return a perturbed patch to equilibrium); right panel
   velocity-weakening / near-plastic (drag flat or falling with $u_b$, the operating
   point is unstable, arrows run away to a slip event). Optionally a small inset of
   bed displacement vs time showing the sawtooth load-up / sudden-slip cycle. Tie the
   two panels to the Weertman (rising) and plastic-till/Coulomb (flat) laws of
   {doc}`../thermomechanics/basal-motion`. Illustrates drafted paragraph 1. Origin:
   original figure (to be drafted) — no attribution needed.

If a future run has the decks mounted, search the seismology / ice-stream deck media
for (a) a real Whillans GPS-displacement-vs-time record showing the twice-daily
sawtooth slips, or (b) a teleseismic waveform of a Greenland glacial earthquake, and
catalog it here with its *original* publication source — e.g. Bindschadler et al.
(2003) or Winberry et al. (2009) for the Whillans displacement record, or Ekström,
Nettles & Tsai (2006, *Science*) / Veitch & Nettles for the glacial-earthquake
waveforms — following rule 2 (credit the paper, never the course).

**Detector gate:** `PASS  /sessions/.../outputs/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

## 2026-06-16 (run 4) — sections/cryosphere/permafrost.md

**Why this section:** the chapter (≈990 words) treats the active layer purely
thermally — "the half meter to few meters that thaws each year" — and never says
what *limits* how deep it thaws. The limiter is latent heat, not temperature: the
descending thaw front is a Stefan problem, so thaw depth goes as the square root
of accumulated thaw-season degree-days, and a wet, ice-rich soil thaws *less*
deeply than a dry one under the same forcing (the same latent buffer that makes
the zero curtain). Separately, the chapter says ground ice fills "the pore space"
but never that a substantial fraction of pore water stays *liquid* below 0 °C, by
interfacial premelting against the mineral grains — the physics that gives frost
heave, ice lensing, and a smeared (rather than sharp) freezing front, and the
direct periglacial application of the surface-premelting physics already in
{doc}`physics-of-ice`. Two short paragraphs supply both. Consulted Cuffey &
Paterson (heat conduction / Stefan, {cite}`cuffey2010`), French *The Periglacial
Environment* ({cite}`french2017`, already cited in the chapter), Fletcher on
surface disorder ({cite}`fletcher1970`), and the premelting / frost-heave work
{cite}`dash2006,rempel2004`; prose is original.

**Proposed placement:** in "## The thermal structure of frozen ground", paragraph 1
(latent-heat / Stefan control of active-layer depth + zero curtain) as a new
paragraph right after the active-layer / permafrost-base definition (before the
taliks sentence). Paragraph 2 (unfrozen water / premelting → frost heave) opens, or
sits at the head of, "## Ground ice and the landforms it builds", supplying the
mechanism behind the ice wedges, lenses, and heave that section then describes
phenomenologically. Both deepen mechanism without restating anything the chapter
already has.

**Drafted prose (gate-passing, verbatim):**

> The depth the active layer reaches each summer is limited less by how warm the
> surface becomes than by how much heat is consumed in melting the ice the ground
> contains. As the thaw front descends it must supply the latent heat of fusion of
> the pore ice before the front can advance, and that heat has to be conducted down
> through the already thawed soil above. The advance of the front therefore follows
> the Stefan problem of {doc}`../thermomechanics/thermal-structure`, in which the
> thawed depth grows with the square root of the heat accumulated at the surface
> over the season, conventionally measured as the sum of degree-days above freezing
> {cite}`cuffey2010`. A wet, ice-rich soil holds more latent heat per unit volume
> than a dry one and so thaws less deeply under the same surface warming, while the
> same latent buffer holds the ground temperature near the melting point through the
> weeks of freeze-up and thaw, the stall recorded in borehole profiles as the zero
> curtain {cite}`french2017`.

> Frozen ground is not simply soil with all of its water turned to ice. A fraction
> of the pore water stays liquid well below 0 degrees Celsius, held in films a few
> molecules thick at the contacts between ice and mineral grains and in the finest
> capillaries, where the curvature of the ice surface and the attraction of the
> mineral lower the freezing point {cite}`dash2006,fletcher1970`. This interfacial
> premelting is the same surface disorder treated for a free ice surface in
> {doc}`physics-of-ice`, now confined against a foreign wall. The unfrozen fraction
> increases as the temperature rises toward the melting point and is larger in
> fine-grained soils such as clay, which carry far more interfacial area per unit
> volume than sand, so the phase change is spread over a range of temperatures
> rather than completed at a single front {cite}`cuffey2010`. The thin films of
> unfrozen water stay connected and mobile, carrying solutes and conducting water
> toward growing ice lenses, and that flow is what drives frost heave, the slow
> lifting of the ground as segregated ice accumulates {cite}`rempel2004`.

**Proposed new BibTeX entries:** none. Every key used — `cuffey2010`, `french2017`,
`fletcher1970`, `dash2006`, `rempel2004` — is already in references.bib (verified).
`dash2006` is the canonical premelting review (Dash, Rempel & Wettlaufer, *Rev.
Mod. Phys.* 2006) and `rempel2004` the continuum frost-heave model; both are exactly
on point for paragraph 2. If Andrew wants the citation load even lighter, paragraph 1
reads fine on `cuffey2010` alone and paragraph 2 on `dash2006` alone.

**Figure proposals:**

The course-deck pool (`~/Downloads/glaciology-course-uw`) was **not mounted on this
run**, so no deck image/slide is cataloged. Two *original* figures are proposed, to
be generated with matplotlib in the style of the existing `_dev/make-*.py` scripts
(no third-party attribution required, drawn fresh):

1. **Active-layer Stefan curve.** Thaw depth versus cumulative thaw degree-days,
   drawn as the square-root law of the Stefan solution for two soils — a dry,
   low-ice column (deeper thaw) and a wet, ice-rich column (shallower thaw) — to
   make paragraph 1's latent-heat limitation visual. Optionally an inset of a
   near-surface temperature trace through a season showing the flat zero-curtain
   stall at 0 °C during freeze-up and thaw. Origin: original figure (to be drafted)
   — no attribution needed. (Distinct from the chapter's existing TODO *trumpet*
   figure, which shows the mean/seasonal envelope, not the latent-heat control.)
2. **Unfrozen-water content curve.** Unfrozen water fraction versus temperature
   below 0 °C, schematic, with separate curves for clay, silt, and sand showing the
   larger unfrozen fraction and gentler freezing in fine-grained soil — illustrating
   paragraph 2's smeared phase change. Drawn as a representative schematic of the
   well-known relation, not traced from any one published dataset, so no attribution
   is required; if Andrew prefers a data-backed version, label it after a specific
   measured soil-freezing characteristic and credit that paper.

If a future run has the decks mounted, search the permafrost / periglacial deck
media for a real measured soil-freezing characteristic curve, an active-layer
thaw-depth time series, or a frost-heave / ice-lens schematic, and catalog it here
with its *original* publication source, following rule 2 (credit the paper or
photographer, never the course).

**Detector gate:** `PASS  /sessions/.../outputs/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

---

## 2026-06-16 (run 5) — sections/observing/gravity.md

**Why this section:** at ≈704 words the gravity chapter is one of the thinner
observing-method sections, and its "Processing and the GIA correction" subsection
names mass-concentration ("mascon") solutions and then develops only the GIA
term, explicitly deferring the rest. Two physical limits that set what a GRACE
mass trend actually means go unmentioned: the few-hundred-kilometre spatial
resolution that follows from truncating the spherical-harmonic series, and the
signal *leakage* across basin boundaries that the smoothing forces, together with
the scaling-factor correction used to undo it. These are, alongside GIA (already
covered), the two terms that set the ice-sheet error budget, so the section reads
as incomplete without them. The reference texts consulted (Cuffey & Paterson,
Ch. 4, on mass-balance methods; {cite}`cuffey2010`) frame the method but do not
treat the harmonic-truncation/leakage machinery, so the specifics below are
stated in original prose and cited to the primary processing literature.

**Proposed placement:** two paragraphs inside "Processing and the GIA correction",
immediately *after* the sentence that introduces representing the field "as a set
of mass concentrations" and *before* the GIA paragraph — so the resolution and
leakage limits are established, then GIA is presented as the third dominant
correction. (Minor knock-on: the existing GIA sentence "One correction dominates
the uncertainty" may want softening to "Two corrections dominate…" once leakage is
added; flagged for Andrew, not changed here.)

**Drafted prose (gate-passing, verbatim):**

> The gravity field recovered from the inter-satellite ranging is expressed as a
> sum of spherical harmonics, and the series is truncated near degree 60 to 96
> because the shorter wavelengths are lost in measurement noise and in the
> north-south striping that the near-polar orbit imprints. Truncation sets a floor
> on spatial resolution of a few hundred kilometres, so a monthly field cannot
> resolve an individual outlet glacier and instead reports the mass of a whole
> drainage basin or a larger region. The coarse resolution also shapes how the
> field is represented. Global spherical-harmonic solutions require explicit
> smoothing to suppress the stripes, while mass-concentration solutions, the
> mascons now in common use, impose a comparable smoothing through a regularization
> tied in advance to the geometry of the ice and bedrock {cite}`watkins2015`.

> Because the recovered field is smooth, mass does not stay confined to the region
> it belongs to. Part of the loss from a shrinking ice sheet appears in the
> surrounding ocean and on neighbouring land, and part of the change on those areas
> appears over the ice, so a plain sum of the field across a basin both sheds some
> of the true signal and absorbs some of its neighbours' {cite}`swenson2002`. The
> correction passes a model of the expected mass distribution through the same
> truncation and smoothing as the data and compares the smoothed model with the
> original, returning a multiplicative scaling factor that restores the lost
> amplitude. Leakage and the glacial isostatic adjustment described above are the
> two terms that dominate the error budget of an ice-sheet mass trend, and
> estimates from independent processing centres are now reconciled to within a few
> tens of gigatonnes per year for Greenland and Antarctica {cite}`shepherd2018`.

**Proposed new BibTeX entries** (verify DOIs/page numbers; `cuffey2010`,
`tapley2004`, `velicogna2006` already in references.bib):

```bibtex
@article{swenson2002,
  author  = {Swenson, S. and Wahr, J.},
  title   = {Methods for inferring regional surface-mass anomalies from {Gravity Recovery and Climate Experiment} ({GRACE}) measurements of time-variable gravity},
  journal = {Journal of Geophysical Research: Solid Earth},
  year    = {2002},
  volume  = {107},
  number  = {B9},
  pages   = {2193},
  doi     = {10.1029/2001JB000576}
}

@article{watkins2015,
  author  = {Watkins, Michael M. and Wiese, David N. and Yuan, Dah-Ning and Boening, Carmen and Landerer, Felix W.},
  title   = {Improved methods for observing {Earth's} time variable mass distribution with {GRACE} using spherical cap mascons},
  journal = {Journal of Geophysical Research: Solid Earth},
  year    = {2015},
  volume  = {120},
  number  = {4},
  pages   = {2648--2671},
  doi     = {10.1002/2014JB011547}
}

@article{shepherd2018,
  author  = {{The IMBIE Team}},
  title   = {Mass balance of the {Antarctic} Ice Sheet from 1992 to 2017},
  journal = {Nature},
  year    = {2018},
  volume  = {558},
  pages   = {219--222},
  doi     = {10.1038/s41586-018-0179-y}
}
```

Notes on the keys. `swenson2002` is the standard primary reference for averaging
kernels and the leakage/restoration scaling factor; Swenson & Wahr (2006),
*Post-processing removal of correlated errors in GRACE data* (GRL 33, L08402,
doi:10.1029/2005GL025285) is the companion destriping reference and could be
substituted or added if Andrew prefers the de-striping emphasis. `watkins2015`
documents the JPL spherical-cap mascon approach; an alternative is Save, Bettadpur
& Tapley (2016), *High-resolution CSR GRACE RL05 mascons* (JGR 121, 7547--7569,
doi:10.1002/2016JB013007). `shepherd2018` is the IMBIE Antarctic reconciliation;
the Greenland companion is IMBIE Team (2020), *Mass balance of the Greenland Ice
Sheet from 1992 to 2018* (Nature 579, 233--239, doi:10.1038/s41586-019-1855-2) --
worth citing alongside if the sentence is to name both ice sheets explicitly.

**Figure proposals:**

The course-deck figure pool (`~/Downloads/glaciology-course-uw`) was **not mounted
on this run** (as in run 1), so no deck image/slide is cataloged. Two *original*
schematics are proposed, to be generated with matplotlib in the style of the
existing `_dev/make-*.py` figures (no third-party attribution required because
they would be drawn fresh):

1. **Resolution / averaging-kernel cartoon.** A sharp true mass-loss pattern
   confined to a drainage basin, beside the same pattern after spherical-harmonic
   truncation and smoothing -- broadened, lower-amplitude, spilling across the
   basin outline -- to show why a monthly field resolves only basin-scale mass and
   why amplitude is suppressed. Illustrates paragraph 1. Origin: original figure
   (to be drafted) -- no attribution needed.
2. **Leakage-and-restoration schematic.** One-dimensional transect across an
   ice/ocean boundary: true mass step, the smoothed (leaked) version that loses
   amplitude over the ice and gains it over the ocean, and the rescaled curve after
   the model-based scaling factor is applied. Illustrates paragraph 2. Origin:
   original figure (to be drafted) -- no attribution needed.

If a future run has the decks mounted, search the GRACE / mass-balance deck media
for a real published mass-trend map (e.g. Velicogna or IMBIE figures) or a
GRACE-FO ranging-geometry diagram, and catalog it here with its *original*
publication source (the paper or the GRACE-FO mission documentation), following
rule 2 -- never the course.

**Detector gate:** `PASS  /sessions/.../outputs/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` -- exit 0.

---

## 2026-06-16 (run 6) — sections/cryosphere/former-glaciers.md

**Why this section:** thin (≈684 words) and almost entirely qualitative. It
asserts two quantitative reconstruction results without giving the method behind
either: that "cirque-floor elevations, clustering near the snowline that fed
them" recover paleo-ELAs, and that "thickness comes from trimlines." Neither the
accumulation-area / balance-ratio logic that turns a reconstructed surface into an
ELA, nor the perfect-plasticity profile that turns a mapped margin into a
thickness and volume, appears anywhere in the chapter. Two short paragraphs supply
both, using citations already in references.bib. Consulted Cuffey & Paterson (Drive
"textbooks" folder) for the ELA/AAR and yield-stress profile material and Benn &
Evans for the reconstruction methods; prose is original.

**Proposed placement:** in the "## Direction, extent, thickness" section, after
the paragraph ending "…the mass-balance gradient does for modern glaciers in
{doc}`../climate/glacier-variations`." Paragraph 1 develops the cirque/ELA claim
made in that paragraph; paragraph 2 develops the trimline-thickness claim and
extends it to whole former ice sheets, leading naturally into the
"Thermal regime and landform preservation" section and the prognostic-model
admonition that closes the chapter. No existing sentence needs deleting; the two
paragraphs deepen claims the section already makes phenomenologically.

**Drafted prose (gate-passing, verbatim):**

> A former equilibrium-line altitude is recovered by exploiting the geometry that
> a glacier in balance satisfies. Over a year of zero net change the area gaining
> mass above the equilibrium line supplies the loss below it, and because
> accumulation and ablation both vary smoothly with elevation, the fraction of the
> glacier lying in the accumulation zone settles near a constant value, close to
> two-thirds for valley glaciers. Reconstructing the former ice surface from its
> moraines and trimlines and finding the contour that places that fraction above
> it returns the equilibrium-line altitude. Weighting each band of area by its
> height above or below the line, a correction for the steeper mass-balance
> gradient in the ablation zone, sharpens the estimate {cite}`benn2010,cuffey2010`.
> Cirque floors give a cruder but more abundant reading, because cirque excavation
> is concentrated near the former snowline, so the floor elevations of many cirques
> in a range scatter about the regional paleo-equilibrium line.

> Where trimlines are sparse, the thickness of a vanished ice mass can be
> estimated from its margin alone by treating ice as a perfectly plastic material
> that deforms once its basal shear stress reaches a yield value {cite}`nye1952`.
> Balancing that yield stress against the driving stress of an ice surface sloping
> under gravity gives a profile that thickens inland as the square root of
> distance, so the height $H$ at distance $x$ from the margin is
> $H=\sqrt{2\tau x/(\rho g)}$, with $\tau$ the yield stress, $\rho$ the ice
> density and $g$ gravity. A yield stress of about one hundred kilopascals,
> typical of modern glaciers, reproduces the parabolic cross sections of
> reconstructed ice sheets and converts a mapped margin into a thickness and a
> volume. The profile is a first approximation, because it omits the lower basal
> stress under wet-based ice streams that flattens real ice sheets, but it brackets
> the former geometry and supplies the starting condition that the prognostic
> models of {doc}`../modeling/prognostic-problem` then refine {cite}`cuffey2010`.

**Proposed new BibTeX entries:** none required. All four keys used
(`benn2010` = Benn & Evans, *Glaciers and Glaciation*; `cuffey2010` = Cuffey &
Paterson; `nye1952` = Nye, *The mechanics of glacier flow* — the perfect-plasticity
paper) are already in references.bib and verified to point to the intended works.

> *Optional primary-method citation for Andrew to consider* (not added, prose does
> not need it): for the balance-ratio / AABR refinement of the simple AAR, the
> standard primary reference is Osmaston (2005), "Estimates of glacier equilibrium
> line altitudes by the Area×Altitude, the Area×Altitude Balance Ratio and the
> Area×Altitude Balance Index methods and their validation," *Quaternary
> International* 138–139, 22–31, doi:10.1016/j.quaint.2005.02.004. Add only if you
> want a primary source beyond the two textbooks.

**Figure proposals:**

The course-deck figure pool (`~/Downloads/glaciology-course-uw`) was **not
mounted on this run**, so no deck image/slide is cataloged. Rather than guess a
provenance, two *original* schematics are proposed, to be generated with
matplotlib in the style of the existing `_dev/make-*.py` figures (no third-party
attribution required because they would be drawn fresh):

1. **Paleo-ELA / accumulation-area-ratio schematic.** A reconstructed glacier
   long-profile (surface from trimlines/moraines over a bed) with the equilibrium
   line drawn where the accumulation-zone area reaches ~two-thirds of the total,
   the accumulation and ablation zones shaded, and a row of cirque floors marked
   scattering about the ELA. Illustrates paragraph 1. Origin: original figure (to
   be drafted) — no attribution needed.
2. **Perfect-plasticity profile.** The parabolic $H=\sqrt{2\tau x/(\rho g)}$
   surface rising inland from a mapped margin for one or two yield-stress values
   (~50 and ~100 kPa), with a flatter "real ice sheet with wet-based ice streams"
   profile overlaid for contrast, and a trimline elevation fixing the surface at
   one point. Illustrates paragraph 2. Origin: original figure (to be drafted) —
   no attribution needed.

If a future run has the decks mounted, search the glacial-geomorphology /
reconstruction deck media for a real LGM ice-sheet reconstruction map, a moraine
sequence photo, or a trimline field photo, and catalog it here with its *original*
publication or photographer source (following rule 2 — never the course).

**Detector gate:** `PASS  /sessions/.../outputs/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

## 2026-06-16 (run 7) — sections/observing/magnetotellurics.md

**Why this section:** thin (≈611 words) and its central physical mechanism is
named but never developed. The chapter leans on "the skin effect: a field of a
given frequency penetrates to a depth that grows as the resistivity rises and as
the frequency falls," yet gives no skin-depth relation, no statement of *why* the
EM fields diffuse rather than propagate (the point that distinguishes this method
from the radar regime of {doc}`../radar/em-waves`, which the chapter explicitly
invokes "at frequencies a million times lower"), and no link from the measured
impedance to apparent resistivity and phase. Two short paragraphs supply the
diffusive-regime physics, the quantitative skin depth, and the impedance →
apparent-resistivity/phase relation that the "From time series to a resistivity
model" section asserts. Consulted the radioglaciology EM background already in the
book's `em-waves` chapter for the displacement-vs-conduction-current distinction,
and standard MT references (Cagniard; Chave & Jones) for the impedance and
apparent-resistivity formulation; prose is original.

**Proposed placement:** in the "## Natural fields as a sounding source" section,
replacing or following the single sentence beginning "The key is the skin
effect…" Paragraph 1 develops that sentence into the diffusive regime and the
skin-depth relation; paragraph 2 belongs at the head of "## From time series to a
resistivity model," ahead of the existing impedance-tensor sentence, supplying the
half-space impedance, apparent resistivity, and phase that the section currently
takes as given. Neither paragraph requires deleting existing prose, though the
chapter's "The key is the skin effect: …" colon-hinge sentence and the aphoristic
"The signal is not loud; what the method exploits is that the Earth itself cannot
stop responding to it" are both house-style tells Andrew may wish to retire when
these paragraphs go in.

**Drafted prose (gate-passing, verbatim):**

> At the frequencies magnetotellurics uses, from roughly a thousandth of a hertz
> to a few hundred, the conduction current in the ground far exceeds the
> displacement current, the reverse of the radar regime of {doc}`../radar/em-waves`.
> Maxwell's equations then reduce to a diffusion equation for the fields rather
> than a wave equation, so a field of angular frequency $\omega$ does not propagate
> downward but spreads and decays, its amplitude falling by a factor $e$ over the
> skin depth $\delta=\sqrt{2/\mu_0\sigma\omega}$, with $\sigma$ the conductivity. In
> practical units this is about $500\sqrt{\rho/f}$ metres, where $\rho=1/\sigma$ is
> the resistivity in ohm-metres and $f$ the frequency in hertz, so penetration
> deepens as the ground becomes more resistive and as the period lengthens. A band
> of periods from seconds to thousands of seconds therefore samples from the
> shallow subsurface down to the deep crust. The ice itself, with a resistivity of
> order $10^5$ ohm-metres, has a skin depth of many kilometres even at the
> high-frequency end of the band, so the fields traverse the column with little
> loss and the sounding responds mainly to the conductive water and sediment
> beneath {cite}`chave_jones2012`.

> What a station records is the surface impedance, the ratio of orthogonal
> horizontal electric and magnetic field components, and over a uniform half-space
> its magnitude is fixed by the resistivity while the phase between the two fields
> is exactly $45^\circ$, the signature of a diffusive response. The apparent
> resistivity $\rho_a=|Z|^2/\mu_0\omega$ returns the true value over uniform ground
> and a frequency-weighted average otherwise, and the phase departs from $45^\circ$
> according to how resistivity varies with depth, rising above it where the ground
> grows more conductive downward and falling below where it grows more resistive
> {cite}`cagniard1953`. Reading the apparent resistivity and the phase together
> across the measured band, rather than either alone, is what fixes whether a
> conductive body lies shallow or deep and how sharply its resistivity contrasts
> with its surroundings. A thick resistive ice layer adds a near-surface offset
> that must be modelled before the structure beneath can be resolved, and Antarctic
> soundings are therefore inverted with the ice column included as a known
> resistive cap.

**Proposed new BibTeX entries** (verify before applying; neither key is currently
in references.bib — confirmed by grep):

```bibtex
@article{cagniard1953,
  title     = {Basic theory of the magneto-telluric method of geophysical prospecting},
  author    = {Cagniard, Louis},
  journal   = {Geophysics},
  volume    = {18},
  number    = {3},
  pages     = {605--635},
  year      = {1953},
  doi       = {10.1190/1.1437915}
}

@book{chave_jones2012,
  title     = {The Magnetotelluric Method: Theory and Practice},
  editor    = {Chave, Alan D. and Jones, Alan G.},
  publisher = {Cambridge University Press},
  address   = {Cambridge},
  year      = {2012},
  doi       = {10.1017/CBO9781139020138}
}
```

**Figure proposals:**

The course-deck figure pool (`~/Downloads/glaciology-course-uw`) was **not mounted
on this run** (as in earlier runs), so no deck image/slide is cataloged. Two
*original* schematics are proposed, to be generated with matplotlib in the style
of the existing `_dev/make-*.py` figures (no third-party attribution required
because they would be drawn fresh):

1. **Skin-depth chart.** Log–log plot of $\delta\approx500\sqrt{\rho/f}$ against
   frequency over the MT band ($10^{-3}$–$10^{2}$ Hz), with one curve each for
   representative resistivities — conductive sediment/brine ($\sim1$–$10$ Ω·m),
   crystalline bedrock ($\sim10^{3}$–$10^{4}$ Ω·m), and cold ice ($\sim10^{5}$ Ω·m)
   — and a right-hand depth axis, to show how the measured band maps to sounding
   depth and why the resistive ice column is nearly transparent. Illustrates
   paragraph 1. Origin: original figure (to be drafted) — no attribution needed.
2. **Layered-model sounding curves.** A simple resistive-ice / thin-bedrock /
   conductive-sediment column beside its forward apparent-resistivity and phase
   curves against period, with the phase rising above $45^\circ$ over the band
   where the apparent-resistivity curve descends toward the deep conductor, to make
   the impedance → apparent-resistivity/phase relation concrete and to motivate the
   Whillans saline-groundwater result already cited in the chapter. Illustrates
   paragraph 2. Origin: original figure (to be drafted) — no attribution needed.

If a future run has the decks mounted, search the geophysics / subglacial-water
deck media for a real published MT resistivity cross-section (e.g. the Whillans
Ice Stream model of Gustafson et al. 2022, *Science*, already in references.bib as
`gustafson2022`) and catalog it here with that paper as its *original* source,
following rule 2 — never the course.

**Detector gate:** `PASS  /sessions/.../outputs/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

## 2026-06-16 (run 8) — sections/observing/insar.md

**Why this section:** thin (≈748 words) and its central quantity, the "line-of-sight
component," is invoked four times across the chapter without ever being defined.
Nothing states the phase–displacement relation φ=(4π/λ) d·ŝ, why a single
interferogram is a one-dimensional projection, why a vertical signal (tidal flexure)
is captured strongly while along-track flow is nearly invisible, or why ascending and
descending passes are needed for the velocity vector. Separately, the grounding-line
application asserts that "differencing interferograms taken at different tidal stages
reveals the grounding line" but never gives the double-difference that makes it work
(cancelling the steady flow and topography) or the elastic-beam flexure that sets the
boundary. Two short paragraphs supply both: one the line-of-sight projection geometry,
one the differential-interferometry (DInSAR) grounding-line method. Draws on the EM
propagation physics already in {doc}`../radar/em-waves`; prose is original.

**Proposed placement:** paragraph 1 in "## From phase to a velocity vector," ahead of
or replacing the existing sentence that asserts "a single interferogram measures only
the one-dimensional projection of the motion onto the line of sight" — the paragraph
makes that projection quantitative and explains the cos θ / sin θ weighting and the
asc/desc requirement the section currently states without justification. Paragraph 2
in "## Glaciological applications," immediately after the sentence "Differencing
interferograms taken at different tidal stages reveals the grounding line…," supplying
the double-difference mechanism and the flexure-zone physics behind that claim. Neither
paragraph restates anything the chapter already has; both deepen claims made
phenomenologically.

**Drafted prose (gate-passing, verbatim):**

> The phase of a single interferogram measures one number at each point, the change in
> range to the ground projected onto the radar line of sight. A round trip doubles the
> path, so a displacement $\mathbf{d}$ advances the phase by
> $\phi = (4\pi/\lambda)\,\mathbf{d}\cdot\hat{\mathbf{s}}$, where $\hat{\mathbf{s}}$ is
> the unit vector from the ground toward the satellite and $\lambda$ the wavelength.
> The satellite views the surface at an incidence angle of twenty to forty-five degrees
> from vertical, so a vertical motion enters the phase weighted by the cosine of that
> angle and a horizontal motion in the across-track direction by its sine, while motion
> along the flight track changes the range very little and is nearly absent from the
> phase. A vertical signal such as tidal flexure is recorded strongly, whereas the
> horizontal flow of the ice is captured only in its across-track projection.
> Recovering the full horizontal velocity vector requires interferograms from passes
> flown in different directions, the ascending and descending orbits, whose differing
> look geometries supply the independent projections {cite}`massonnet_feigl1998`.

> The grounding line is found by stripping the steady flow from the phase and keeping
> only the part the tide controls. Two interferograms of the same area, each spanning a
> short repeat interval, are differenced again to form a double difference. The steady
> horizontal flow, very nearly constant over the days between acquisitions, cancels in
> the second difference, as does the topographic phase, and what remains is the change
> in vertical position between the two tidal states {cite}`rignot2011`. Grounded ice
> shows no such motion, and ice in hydrostatic equilibrium with the ocean rises and
> falls by the full tidal amplitude. Between the two the ice bends as an elastic beam
> over a flexure zone one to a few kilometres wide, and the landward limit of the
> bending, where the surface first begins to move with the tide, marks the grounding
> line. The width of that zone is set by the bending stiffness, and through it by the
> ice thickness, so the same fringes that locate the boundary also constrain the
> geometry of the ice where it goes afloat {cite}`rignot2011`.

**Proposed new BibTeX entries** (neither key is in references.bib — confirmed by grep;
`goldstein1993` and `mouginot2019` already present):

```bibtex
@article{massonnet_feigl1998,
  author  = {Massonnet, Didier and Feigl, Kurt L.},
  title   = {Radar interferometry and its application to changes in the {Earth's} surface},
  journal = {Reviews of Geophysics},
  year    = {1998},
  volume  = {36},
  number  = {4},
  pages   = {441--500},
  doi     = {10.1029/97RG03139}
}

@article{rignot2011,
  author  = {Rignot, E. and Mouginot, J. and Scheuchl, B.},
  title   = {Antarctic grounding line mapping from differential satellite radar interferometry},
  journal = {Geophysical Research Letters},
  year    = {2011},
  volume  = {38},
  number  = {10},
  pages   = {L10504},
  doi     = {10.1029/2011GL047109}
}
```

Notes on the keys. `massonnet_feigl1998` is the standard review of the phase geometry
and the line-of-sight projection (canonical and widely cited). `rignot2011` is the
discovery/standard reference for the differential (double-difference) grounding-line
mapping method on which the chapter's tidal-flexure application rests. Both are
pre-2025. Lighter alternatives if Andrew prefers to add only one key: the glaciological
InSAR review of Joughin, Smith & Abdalati (2010), *Glaciological advances made with
interferometric synthetic aperture radar*, J. Glaciol. 56(200), 1026–1042
(doi:10.3189/002214311796406158), covers both paragraphs at survey level and could
stand in for either primary reference; for the elastic-beam flexure specifically,
Rignot (1996), *Tidal motion, ice velocity and melt rate of Petermann Gletscher,
Greenland*, J. Glaciol. 42(142), 476–485, is the primary flexure-zone source.

**Figure proposals:**

The course-deck figure pool (`~/Downloads/glaciology-course-uw`) was **not mounted on
this run** (only the book repo and outputs were mounted), so no deck image/slide is
cataloged. Two *original* schematics are proposed, to be generated with matplotlib in
the style of the existing `_dev/make-*.py` figures (no third-party attribution required
because they would be drawn fresh):

1. **Line-of-sight projection geometry.** A side-view cartoon of the satellite looking
   down at incidence angle θ, with the line-of-sight unit vector ŝ and a surface
   displacement vector d resolved into vertical (× cos θ) and across-track horizontal
   (× sin θ) components, and the along-track (azimuth) direction marked as carrying
   almost no phase. A small inset showing the same scene from ascending and descending
   geometries, whose two projections combine to recover the horizontal vector.
   Illustrates paragraph 1. Origin: original figure (to be drafted) — no attribution
   needed.
2. **Grounding-line flexure profile.** A transect from fully grounded ice (no tidal
   motion) across the flexure zone to freely floating ice (full hydrostatic tidal
   amplitude), drawn as an elastic-beam bending curve for one or two ice thicknesses to
   show how the zone width scales with stiffness; the landward limit of bending marked
   as the grounding line, with a schematic fringe pattern (double-difference phase)
   overlaid to connect the bending curve to what the interferogram shows. Illustrates
   paragraph 2. Origin: original figure (to be drafted) — no attribution needed.

If a future run has the decks mounted, search the InSAR / ice-velocity deck media for a
real published interferogram (e.g. the Rutford fringe image of Goldstein et al. 1993,
already in references.bib as `goldstein1993`, or a continent-wide velocity map from
Mouginot et al. 2019, `mouginot2019`) or a grounding-line double-difference figure
(Rignot, Mouginot & Scheuchl 2011), and catalog it here with that paper as its
*original* source, following rule 2 — never the course.

**Detector gate:** `PASS  /sessions/.../outputs/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

## 2026-06-16 (run 9) — sections/ice_flow/mass-balance.md

**Why this section:** the "Accumulation and ablation" section calls the
equilibrium-line altitude "one of the most sensitive recorders of climate a
glacier has" and carries a Blue Glacier balance-gradient figure
(`fig-blue-glacier-gradient`), yet the *gradient itself* — the quantity the figure
plots and the thing that actually makes a glacier climate-sensitive — is never
defined or developed in the text. Two short paragraphs supply the mass-balance
gradient and the activity index, the maritime/continental contrast and its
energy-balance origin, the balance-ratio asymmetry, and the throughput /
sensitivity / AAR consequences, tying the existing figure to the conservation law
that follows and cross-linking to `surface-energy-balance` and the paleo-ELA
`former-glaciers` reconstruction already drafted in run 6.

**Proposed placement:** in `sections/ice_flow/mass-balance.md`, inside
"Accumulation and ablation", immediately after the `fig-blue-glacier-gradient`
figure block (line ~23) and before the "Conservation of mass" heading. Both
paragraphs use the section's own notation (specific surface mass balance \(\dot a\),
elevation \(z\)).

**Drafted prose (gate-passing, verbatim):**

> The equilibrium line marks where the balance vanishes, but the rate at which the
> balance changes with altitude carries as much climatic information as the line
> itself. This rate, the mass-balance gradient $\mathrm{d}\dot a/\mathrm{d}z$,
> measures how quickly accumulation gives way to ablation as one descends the
> glacier, and its value near the equilibrium line is the activity index
> {cite}`cuffey2010,benn2010`. Temperate maritime glaciers, fed by heavy snowfall
> and wasting under a warm, energy-rich melt season, have steep gradients of order
> one metre of ice per hundred metres of altitude, while cold continental and
> polar glaciers, with sparse accumulation and feeble summer melt, have gradients
> an order of magnitude smaller. The contrast follows from the surface energy
> balance of {doc}`../thermomechanics/surface-energy-balance`, since ablation is
> driven by melt and melt rises steeply with the air temperature that falls off
> with height at the atmospheric lapse rate, while accumulation varies more gently.
> For the same reason the gradient is usually steeper below the equilibrium line
> than above it, so that the ablation zone of a glacier in balance is more compact
> than its accumulation zone {cite}`benn2010`.

> The gradient fixes how vigorously a glacier moves and how sharply it responds to
> a change in climate. The ice flux that must cross the equilibrium line to hold
> the glacier in balance is the accumulation integrated over the area above it, so
> a steep gradient piles up more accumulation in a given altitude band and a
> maritime glacier carries a far larger throughput than a polar one of the same
> size, and must flow faster to do so. The same steepness sharpens the response to
> climate. A rise in the equilibrium line converts a band of former accumulation
> area into ablation area, and where the gradient is large the resulting loss of
> mass is large. A glacier in steady state distributes its area so that the
> accumulation zone occupies a characteristic fraction of the whole, the
> accumulation-area ratio, near 0.6 for temperate glaciers, which is why a mapped
> snowline fixes the equilibrium altitude and why the balance-ratio weighting of
> {doc}`../cryosphere/former-glaciers` can recover a former climate from a
> reconstructed glacier outline {cite}`cuffey2010,benn2010`.

**Proposed new bib entries:** none. Both citation keys already exist in
`references.bib` (`cuffey2010` = Cuffey & Paterson, *The Physics of Glaciers*, 4th
ed., the section's existing reference and the source for the balance-gradient
treatment; `benn2010` = Benn & Evans, *Glaciers and Glaciation*, 2nd ed., which
names the activity index and treats the AAR and balance ratio). No copying — the
physics is restated in original prose, substantially shorter than either source.

**Figure proposals:**

The course-deck figure pool (`~/Downloads/glaciology-course-uw`) was **not mounted
on this run** (only the book repo, outputs and uploads were mounted), so no deck
image/slide is cataloged. The section already carries a real measured
balance-gradient figure (`fig-blue-glacier-gradient`, Blue Glacier), so the prose
above is written to explain that existing figure rather than to require a new one.
One *original* schematic is proposed, to be generated with matplotlib in the style
of the existing `_dev/make-*.py` figures (no third-party attribution required
because it would be drawn fresh):

1. **Activity-index contrast schematic.** Specific balance $\dot a$ on the x-axis
   against elevation $z$ on the y-axis, with two straight balance-profile lines
   crossing zero at a common equilibrium line: a steep maritime profile (large
   $\mathrm{d}\dot a/\mathrm{d}z$, high turnover) and a shallow continental profile
   (small gradient, low turnover), the steeper line drawn with a kink to a yet
   steeper slope below the ELA to show the balance-ratio asymmetry. Shaded bands
   could mark the accumulation and ablation zones to make the AAR visible.
   Illustrates both paragraphs. Origin: original figure (to be drafted) — no
   attribution needed.

If a future run has the decks mounted, search the mass-balance / glacier-budget
deck media for a real published activity-index or balance-gradient comparison
(e.g. a maritime-vs-continental balance-profile plot, or Meier's classic balance
diagrams) or an accumulation-area-ratio diagram, and catalog it here with its
*original* publication source (the paper or textbook figure), following rule 2 —
never the course.

**Detector gate:** `PASS  /sessions/.../outputs/enrich_draft_massbal.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

## 2026-06-16 — sections/foundations/ice-structure.md

**Why this section:** mature already (hexagonal ice, c-axis/basal glide, proton
disorder, premelting), but it describes the lattice only qualitatively — "puckered
hexagonal layers stack one above another" — and asserts the openness/float result
without a number. Two short paragraphs add the crystallographic specifics and put
the density anomaly on a quantitative footing. Fletcher-aligned.

**Proposed placement:** "Hexagonal ice" section. Paragraph 1 (cell parameters and
stacking) follows the paragraph ending "...stack one above another to fill space."
Paragraph 2 (coordination number / packing fraction) follows the existing
"Because the tetrahedral framework holds the molecules well apart... why ice
floats." paragraph, giving it the numbers.

**Drafted prose (gate-passing, verbatim):**

> The hexagonal cell has edge lengths of about $a = 4.52$ angstroms across the
> basal plane and $c = 7.36$ angstroms along the symmetry axis, so the axial ratio
> $c/a \approx 1.63$ lies close to the value $\sqrt{8/3} \approx 1.633$ expected
> for ideal tetrahedral packing, a measure of how nearly perfect the bonding
> geometry is. Within each layer the oxygen atoms form puckered six-membered rings
> in the chair conformation, and successive layers stack in a sequence that
> repeats every second layer, the stacking that defines hexagonal ice and
> separates it from the cubic ice that forms when the same bilayers stack in a
> three-layer sequence instead. Cubic and stacking-disordered ice occur in the
> atmosphere, but at the temperatures and pressures of glaciers the hexagonal
> stacking is the stable one and the ice is ice Ih throughout {cite}`fletcher1970`.

> Each molecule has only four nearest neighbors, the four hydrogen-bonded oxygens,
> whereas a close-packed solid of the same spheres would have twelve, so the
> tetrahedral framework leaves far more empty space than ordinary packing. Ice
> fills only about a third of its volume with molecules, against roughly
> three-quarters for a close-packed arrangement, and on melting some of that empty
> space collapses as bonds bend and break, so the liquid is the denser phase. The
> density difference is about nine percent at the melting point, the figure quoted
> in the preface, and it follows directly from the coordination number that the
> bonding geometry fixes at four.

**Proposed new BibTeX entry:** none — `fletcher1970` already in references.bib.

**Numbers used (verify):** a ≈ 4.52 Å, c ≈ 7.36 Å (ice Ih, near 0 °C); c/a ≈ 1.63
vs ideal √(8/3) ≈ 1.633; coordination number 4 (vs 12 close-packed); packing
fraction ≈ 0.34 (vs 0.74 close-packed); ice/water density contrast ≈ 9%. All
standard Fletcher / crystallography values.

**Figure proposals:** none this run. The chapter already carries strong structure
figures (tetrahedral-coordination, ice-ih-lattice, snow-crystal). A possible
future addition is an ABAB-vs-ABC stacking schematic (Ih vs Ic) to support
paragraph 1 — would be an *original* diagram, no third-party attribution needed.
Course decks were not mounted this run, so nothing was cataloged from them.

**Detector gate:** `PASS  /tmp/enrich_struct.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

**Manuscript action this session (outside the review queue):** at Andrew's
direction, the unresolved merge conflict in `sections/foundations/preface.md` was
resolved in place — the two "common origin" paragraphs merged into one (origin
first, then a separate "cascading effects" paragraph), "asociated"→"associated"
and "it's"→"its" fixed, and the dielectric line corrected from "about 80 (units)
... about 100 (units) ... at microwave frequencies" to "unusually large static
dielectric constants, about 80 for water and about 100 for ice" (the ~80/~100
values are the static constants; ice is ≈3.2 at radar frequencies).

---

## 2026-06-16 — sections/observing/laser-altimetry.md

**Why this section:** thin (≈712 words) and almost entirely descriptive. It states
the headline facts (centimetre precision, 11 m footprints, photon counting, six
beams in three pairs) without the two pieces of physics that actually govern what
laser altimetry can and cannot do: (i) why the *horizontal* geolocation error, not
the timing precision, sets the height error over an ice sheet, and (ii) how a
surface is recovered at all from a stream of mostly-noise photons. The existing
text even mentions the across-track pairs and the photon cloud but leaves both
mechanisms unexplained. Two short paragraphs supply the slope/geolocation error
budget and the photon-counting detection statistics, in the Cuffey & Paterson
observational register.

**Proposed placement:** "The instruments" section already notes the across-track
pairs and the photon background; the new paragraphs deepen exactly those two
sentences. Paragraph 1 (slope–geolocation coupling) is best placed at the end of
"The instruments" or opening a short "Error budget" subsection, since it explains
why the centimetre ranging precision quoted just above does not equal the
ice-sheet height accuracy. Paragraph 2 (photon-counting detection) follows the
existing paragraph ending "...the surface is pulled out of that noise
statistically across many pulses," which it makes quantitative.

**Drafted prose (gate-passing, verbatim):**

> The dominant uncertainty in an ice-sheet elevation from a laser altimeter comes
> not from timing the pulse but from knowing where on the ground it struck. A
> pointing error that displaces the footprint horizontally by a distance $\delta x$
> becomes a vertical error of $\delta x \tan\alpha$ over a surface sloping at angle
> $\alpha$, so a geolocation error of a few metres translates into a height error
> of tens of centimetres where the margin slopes at several degrees, far exceeding
> the centimetre precision of the ranging itself. The flat interior, sloping only a
> fraction of a degree, is where a small elevation change is easiest to detect, and
> the rough, steep outlet glaciers are where the method is least accurate. The
> across-track beam pairs of ICESat-2 measure the local slope directly, and
> repeat-track analysis compares heights along a fixed reference ground track
> rather than at arbitrary crossovers, both of which hold the horizontal error
> small enough that the slope term does not dominate {cite}`markus2017`.

> The photon-counting design trades the energy of one pulse for the number of
> pulses. Rather than recording the waveform of a single strong return, the
> instrument fires a weak pulse ten thousand times a second and detects on average
> fewer than one returned signal photon per shot, against a background of solar
> photons that arrive at random times. The surface emerges only statistically.
> Signal photons fall in range near the true surface from one shot to the next
> while the background is spread uniformly in time, so photons accumulated over a
> short along-track segment form a histogram in which the surface appears as a
> narrow peak above a flat noise floor. The height precision improves roughly as
> the square root of the number of photons gathered, which sets a trade between
> along-track resolution and vertical precision, since a shorter segment locates
> the surface more finely along the track but pools fewer photons to define it
> {cite}`markus2017`.

**Proposed new bib entries:** none. Both paragraphs cite `markus2017` (Markus et
al., *The Ice, Cloud, and land Elevation Satellite-2 (ICESat-2): Science
requirements, concept, and implementation*), already in `references.bib` and
already the section's reference for the instrument; it documents both the
geolocation/pointing requirement and the micropulse photon-counting concept. No
copying — the physics is restated in original prose.

**Numbers used (verify):** δz ≈ δx·tanα (small-angle, ≈ δx·α in radians);
interior slope ≪ 1° vs outlet-glacier slopes of several degrees; ICESat-2 fires at
10 kHz with sub-one signal photon per shot expected over bright/ sloped ice;
height precision scaling ∝ N_photon^(−1/2). All standard altimetry / Poisson-
counting results consistent with {cite}`markus2017`.

**Figure proposals:**

The course-deck figure pool (`~/Downloads/glaciology-course-uw`) was **not mounted
on this run** (only the book repo, outputs and uploads were mounted), so no deck
image/slide is cataloged. One *original* schematic is proposed, to be generated
with matplotlib in the style of the existing `_dev/make-*.py` figures (no
third-party attribution required because it would be drawn fresh):

1. **Slope–geolocation error schematic.** A ground surface drawn as a line of slope
   $\alpha$, the nominal footprint position and a footprint displaced horizontally
   by $\delta x$, with the resulting vertical offset $\delta z = \delta x\,\tan\alpha$
   marked, plus a small inset plot of $\delta z$ versus surface slope for a fixed
   $\delta x$ (e.g. 3 m) to show how the error grows from millimetres on the flat
   interior to decimetres on a steep margin. Directly illustrates paragraph 1.
   Origin: original figure (to be drafted) — no attribution needed.

If a future run has the decks mounted, search the altimetry / remote-sensing deck
media for a real published ICESat-2 beam-pair geometry diagram or a photon-cloud
(ATL03-style) along-track scatter showing signal photons against solar background,
and catalog it here with its *original* publication source (the paper or agency
figure, e.g. Markus et al. 2017 or a NASA/NSIDC product figure), following rule 2
— never the course.

**Detector gate:** `PASS  /sessions/.../outputs/enrich_laser.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

## 2026-06-16 — sections/foundations/snow-processes.md

**Why this section:** the thinnest undrafted chapter (≈1031 words). Its central
mechanism for dry-snow metamorphism is asserted but never quantified — the text
states "Vapour pressure is higher over a convex, high-curvature surface than over
a flat or concave one" and that "sintering" carries the density toward ~550
kg m⁻³, yet it gives no measure of how large the curvature effect is, why it is
enough to act, or what sets its rate. Two short paragraphs supply the Kelvin
(Gibbs–Thomson) curvature relation that fixes the driving force and the
Clausius–Clapeyron temperature control that fixes the rate, in the Fletcher /
Cuffey & Paterson register.

**Proposed placement:** the "Dry-snow metamorphism" section. Paragraph 1
(curvature/Kelvin) follows the existing sentence "Vapour pressure is higher over a
convex, high-curvature surface than over a flat or concave one, so water vapour
moves from the points of the crystals to the necks…", making that qualitative
statement quantitative before the paragraph turns to sintering. Paragraph 2
(temperature/rate) is best placed just after, before the chapter moves on to the
temperature-gradient (depth-hoar) case, since it explains why metamorphism is fast
near melting and nearly arrested in cold interior snow and sets up the
gradient-amplification argument the existing depth-hoar paragraph then uses.

**Drafted prose (gate-passing, verbatim):**

> The rounding described above can be made quantitative through the curvature
> dependence of the vapour pressure. Over a convex surface of radius $r$ the
> saturation vapour pressure exceeds its value over a flat surface according to the
> Kelvin relation $\ln(p_r/p_\infty)=2\gamma_{sv}V_m/(rRT)$, in which
> $\gamma_{sv}\approx0.11$ J m$^{-2}$ is the ice–vapour surface free energy and
> $V_m$ the molar volume of ice {cite}`fletcher1970`. The grouping
> $2\gamma_{sv}V_m/RT$ carries the dimension of a length and amounts to only a few
> nanometres near $-10$ °C, so the fractional pressure excess over a rounded grain
> of radius tens of micrometres is of order $10^{-4}$, while over a dendritic tip a
> few micrometres across it approaches one part in a thousand. Such differences are
> minute in absolute terms, and yet they impose a steady gradient in vapour
> pressure between the sharp points and the concave necks, so vapour diffuses from
> points to necks and the crystals lose their arms as the bonds thicken.

> The rate of this transport, rather than its direction, is governed mainly by
> temperature. The absolute saturation vapour pressure over ice rises steeply as
> the melting point is approached, following the Clausius–Clapeyron relation with
> the latent heat of sublimation, so the diffusive flux available to move mass
> between grains grows by more than an order of magnitude between the cold of
> midwinter and a snowpack near $0$ °C. Dry metamorphism is therefore slow in cold
> polar snow and rapid in temperate snow close to melting, which is one reason firn
> at a warm, high-accumulation site densifies faster than firn of the same age in
> the cold interior {cite}`colbeck1982`. The temperature gradient through a
> seasonal pack adds to this effect, because the same Clausius–Clapeyron
> sensitivity converts a gradient in temperature into a much larger gradient in
> equilibrium vapour pressure, sustaining the upward vapour flux that builds depth
> hoar.

**Proposed new BibTeX entries:** none. Both citation keys already exist in
references.bib (`fletcher1970` = N. H. Fletcher, *The Chemical Physics of Ice*,
Cambridge UP 1970, for the surface-free-energy/curvature physics; `colbeck1982` =
S. C. Colbeck, "An Overview of Seasonal Snow Metamorphism," *Rev. Geophys.* 20(1),
45–61, for the metamorphism rates and their temperature dependence).

**Numbers (for Andrew to spot-check):** with $\gamma_{sv}\approx0.11$ J m⁻²,
$V_m=M/\rho_{ice}=0.018/917\approx1.96\times10^{-5}$ m³ mol⁻¹, $R=8.314$ J mol⁻¹
K⁻¹, $T=263$ K, the Kelvin length $2\gamma_{sv}V_m/RT\approx2$ nm. Ratio to a
50-µm grain ≈ $4\times10^{-5}$; to a 1-µm dendrite tip ≈ $2\times10^{-3}$. These
support "of order $10^{-4}$" and "approaches one part in a thousand." The
order-of-magnitude rise in saturation vapour pressure over ice between roughly
$-30$ °C (≈38 Pa) and $0$ °C (≈611 Pa) is ~16×, consistent with "more than an
order of magnitude." Values are standard; γ_sv is the least certain (literature
range ≈0.10–0.12 J m⁻²).

**Figure proposals:**

The course-deck figure pool (`~/Downloads/glaciology-course-uw`) was **not mounted
on this run**, so no deck image/slide is cataloged. Rather than guess a provenance,
two *original* schematics are proposed, to be generated with matplotlib in the
style of the existing `_dev/make-*.py` figures (no third-party attribution needed
because they would be drawn fresh). Note the section already carries a grain-scale
metamorphism figure (`figures/lachapelle-metamorphism.jpeg`, credited to
LaChapelle), so these should complement rather than duplicate it.

1. **Kelvin curvature–vapour-pressure curve.** Plot of the fractional saturation
   vapour-pressure excess $p_r/p_\infty-1$ versus surface radius of curvature $r$
   (log–log, $r$ from ~0.1 µm to ~1 mm) at a fixed temperature, with the grain-tip
   and dendrite-tip regimes marked and the few-nm Kelvin length annotated.
   Illustrates paragraph 1. Origin: original figure (to be drafted) — no
   attribution needed.
2. **Saturation-vapour-pressure-over-ice vs temperature.** Clausius–Clapeyron
   curve of $p_\infty$(ice) from about $-40$ °C to $0$ °C on a log axis, annotating
   the >10× rise across the snowpack temperature range to make concrete why the
   metamorphism rate climbs toward melting. Illustrates paragraph 2. Origin:
   original figure (to be drafted) — no attribution needed.

If the deck pool is mounted on a future run, a micrograph or sketch of rounded
equilibrium-form grains versus faceted/depth-hoar crystals would pair well here;
catalog it then with its *original* publication source (paper/book/photographer),
following rule 2 — never the course.

**Detector gate:** `PASS  /sessions/.../outputs/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

## 2026-06-16 (run 14) — sections/foundations/physics-of-ice.md

**Why this section:** one of the thinner foundations chapters (≈755 words) and,
for a chapter whose whole argument is that ice's macroscopic behaviour descends
from a single molecule and its bonds, it stays entirely qualitative about the
bond itself. The "## The hydrogen bond" section says only that the bond is
"weaker than the covalent bond inside the molecule but far stronger than ordinary
intermolecular attraction" — no geometry, no energy scale, and no connection to
the two numbers a glaciologist actually meets (the high melting point, and the
small latent heat of fusion versus the large sublimation enthalpy). Two short
paragraphs supply that quantitative spine: paragraph 1 puts numbers on the bond
geometry and energy and ties them to the open framework and high melting point;
paragraph 2 does the cohesive-energy bookkeeping that shows why melting absorbs so
little energy (it removes order, not most of the bonds), which also motivates the
proton-disorder and premelting material elsewhere in the foundations part.

**Proposed placement:** both paragraphs appended to the "## The hydrogen bond"
subsection, after the existing paragraph ending "…responsible for the open, rigid
framework of ice and for its unusually high melting point." They deepen, and do
not restate, the qualitative four-bonds-per-molecule picture already there. The
fusion/sublimation contrast in paragraph 2 sets up "## Proton disorder" (the
surviving disordered network) and the premelting/interfacial-water discussion in
the permafrost and snow-processes chapters.

**Reference note:** the Fletcher text ({cite}`fletcher1970`) is not present in the
connected Drive "textbooks" folder this run (only Cuffey & Paterson and the
radioglaciology text are), so the bond-energetics numbers were grounded in
standard ice-physics values (O···O ≈ 2.76 Å; per-bond energy ~20 kJ/mol; covalent
O–H several hundred kJ/mol; sublimation enthalpy ≈ 51 kJ/mol; latent heat of
fusion ≈ 6.0 kJ/mol) and the prose is original throughout. Both {cite}`fletcher1970`
and {cite}`petrenko1999` are standard authorities for exactly these facts and are
already in references.bib; Andrew should confirm the per-bond energy he prefers to
quote (~20 vs ~23 kJ/mol are both defensible) and the citation load.

**Drafted prose (gate-passing, verbatim):**

In ice Ih the two oxygen atoms joined by a hydrogen bond lie about 2.76 Å apart, and the shared proton sits close to one of them, roughly 1 Å along the bond, leaving the O-H...O link distinctly asymmetric. Breaking one such bond costs on the order of 20 kJ per mole, more than an order of magnitude less than the several hundred kJ per mole of the covalent O-H bond inside the molecule, but about ten times the weak van der Waals attraction between nonpolar molecules of comparable size. This intermediate strength, together with the directional near-tetrahedral geometry, keeps the framework of ice open and rigid rather than close-packed, and sets the high melting point relative to nonpolar solids of similar molecular mass {cite}`fletcher1970,petrenko1999`.

The cohesive energy of the crystal follows from the bond count. Each molecule donates two hydrogen atoms and accepts two, so on average there are two hydrogen bonds per molecule, and the energy needed to part a molecule from the lattice, near 50 kJ per mole, matches the measured enthalpy of sublimation of ice {cite}`petrenko1999`. Melting absorbs far less, about 6 kJ per mole, well below the energy of even one bond per molecule, so most hydrogen bonds survive the change to liquid water; what melting removes is the long-range order of the framework, not the bonding itself.

**Proposed new bib entries:** none — {cite}`fletcher1970` and {cite}`petrenko1999`
are already in references.bib.

**Figure proposals:**

The course-deck figure pool (`~/Downloads/glaciology-course-uw`) was **not mounted
on this run**, so no deck image/slide is cataloged. One *original* figure is
proposed, to be drawn fresh with matplotlib in the style of the existing
`_dev/make-*.py` figures (no third-party attribution needed). This chapter
currently carries no figures, so it complements rather than duplicates.

1. **Energy-scale ladder for the water/ice bonds.** A simple horizontal bar (log
   axis, kJ per mole) placing four energies side by side to make the paragraph-1
   and paragraph-2 comparisons visual: the covalent O–H bond (several hundred),
   one hydrogen bond (~20), the van der Waals scale (~a few), and — on a second
   per-mole row — the sublimation enthalpy of ice (~51) against the latent heat of
   fusion (~6), with the ratio annotated to show that fusion breaks only a small
   fraction of the bonds. Illustrates both drafted paragraphs. Origin: original
   figure (to be drafted) — no attribution needed.

If the deck pool is mounted on a future run, a ball-and-stick sketch of the ice Ih
tetrahedral framework (oxygens at lattice sites, off-centre protons on the O···O
bonds) would pair well with the existing "## The structure of ordinary ice"
section; catalog it then with its *original* publication source (paper, book,
illustrator), following rule 2 — never the course.

**Detector gate:** `PASS  /sessions/.../outputs/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

## 2026-06-17 (run 18) — sections/foundations/composition.md

**Why this section:** the composition chapter (~1120 words, not previously drafted)
closes its "## The composition of natural ice" section by noting that the firn-sealed
bubbles "at sufficient depth and pressure convert to air-clathrate inclusions" — the
chapter's only mention of clathrate hydrates, carried in a single subordinate clause
with no physics behind it. The transition is one of the better-quantified pieces of
ice physics and bears directly on two things the book already cares about: the
ice-core gas record of {doc}`../climate/paleoclimate` (the same trapped-air archive the
chapter calls "the only direct sample of past atmospheres") and the optical clarity of
deep ice touched on in {doc}`optical-properties`. The draft supplies the missing layer:
the thermodynamic stability condition and Miller's prediction, the kinetic
(nucleation-limited) metastability that smears the conversion across a several-hundred-
metre transition zone rather than a sharp depth, and the two glaciological
consequences. It stays within the chapter's stated remit (impurities and trapped
gases) and does not stray into the lattice/defect material owned by
{doc}`ice-structure` and {doc}`point-defects`.

**Proposed placement:** three paragraphs in "## The composition of natural ice",
inserted immediately after the existing paragraph that ends "…the only direct sample
of past atmospheres." They expand exactly that paragraph's clathrate clause and feed
the chapter's closing sentence about ancient air. No text is replaced; the draft is
purely additive.

**Consulted:** {cite}`cuffey2010` (firn/ice gas-inclusion treatment, already in
references.bib) and the primary air-hydrate literature below; physical numbers
cross-checked against published Vostok transition-zone values. Prose is original.

**Drafted prose (gate-passing, verbatim):**

> The bubbles do not persist to the bed. Air and water combine under pressure into a
> clathrate hydrate, a crystal in which gas molecules sit inside cages built from a
> host framework of water molecules, with the approximate stoichiometry (N₂,O₂)·6H₂O
> and the cubic structure II common to the larger gas hydrates {cite}`shoji1982`. Above
> a temperature-dependent dissociation pressure the hydrate is the stable form and the
> free bubble is not, and Miller predicted from laboratory dissociation measurements
> that air hydrate should be stable below roughly 800 m in the cold Antarctic ice
> sheet, with the bubbles gone by about 1200 m {cite}`miller1969`. The prediction was
> confirmed when hydrate inclusions were observed directly in the Dye-3 core from
> Greenland {cite}`shoji1982`.
>
> Bubbles nonetheless survive well below the depth at which the hydrate becomes the
> stable phase, because forming the first hydrate crystal requires nucleation against a
> free-energy barrier rather than thermodynamic favorability alone. At Vostok the
> hydrostatic pressure reaches the dissociation pressure near 500 m, yet bubbles and
> hydrate crystals coexist through a transition zone extending to about 1250 m
> {cite}`lipenkov2000`. Near the middle of that zone, at 900 m and 223 K, the
> equilibrium dissociation pressure is about 3.7 MPa while the ice carries a
> hydrostatic load near 7.8 MPa, so a bubble can remain uncombined at roughly twice the
> pressure at which the hydrate is already favored {cite}`lipenkov2000`. Once a crystal
> nucleates, conversion of a single bubble takes of order decades as the hydrate shell
> thickens inward by diffusion {cite}`lipenkov2000`.
>
> The transition affects how the trapped air is read. Because conversion is gradual and
> fractionates slightly between the small and large cages of the structure, coexisting
> bubbles and hydrates can hold different N₂/O₂ ratios across the transition zone, a
> depth-dependent bias that ice-core gas analyses correct for {cite}`lipenkov2000`. The
> loss of bubbles also clears the ice optically, since the bubbles rather than the
> dissolved air scatter the light, leaving deep hydrate-bearing ice markedly more
> transparent than the white bubbly ice above it {cite}`cuffey2010`.

**Proposed new BibTeX entries** (verify before adding to references.bib; `cuffey2010`
is already present):

```bibtex
@article{miller1969,
  author  = {Miller, Stanley L.},
  title   = {Clathrate Hydrates of Air in Antarctic Ice},
  journal = {Science},
  volume  = {165},
  number  = {3892},
  pages   = {489--490},
  year    = {1969},
  doi     = {10.1126/science.165.3892.489}
}

@article{shoji1982,
  author  = {Shoji, Hitoshi and Langway, Chester C.},
  title   = {Air hydrate inclusions in fresh ice core},
  journal = {Nature},
  volume  = {298},
  number  = {5874},
  pages   = {548--550},
  year    = {1982},
  doi     = {10.1038/298548a0}
}

@incollection{lipenkov2000,
  author    = {Lipenkov, Vladimir Ya.},
  title     = {Air bubbles and air-hydrate crystals in the Vostok ice core},
  booktitle = {Physics of Ice Core Records},
  editor    = {Hondoh, Takeo},
  publisher = {Hokkaido University Press},
  address   = {Sapporo},
  pages     = {327--358},
  year      = {2000}
}
```

Numbers used and their source, for Andrew to spot-check:
- Stability below ~800 m, bubbles gone by ~1200 m, (N₂,O₂)·6H₂O — Miller (1969).
- First direct observation, structure II, Dye-3 Greenland — Shoji & Langway (1982).
- Vostok transition zone ~500–1250 m; at 900 m / 223 K, dissociation ≈ 3.7 MPa vs
  hydrostatic ≈ 7.8 MPa; ~decadal single-bubble conversion by inward shell growth —
  Vostok transition-zone analyses compiled in Lipenkov (2000); the 900 m pressure
  pair traces to the Salamatin/Uchida Vostok simulation work and should be cited to
  that primary paper if Andrew wants the exact figure attributed precisely.

**Figures:** the course-deck pool (`~/Downloads/glaciology-course-uw`,
`_extracted/<deck>/ppt/media`) was **not mounted on this run** and could not be
requested unattended, so no deck image is cataloged. Figure proposals for this
section, for a future run or for Andrew to source directly — captions must credit the
ORIGINAL source only (rule 2), never the course:

1. **Thin-section / micrograph contrast: bubbly ice vs. clathrate-bearing ice.** A
   two-panel image showing dispersed air bubbles in shallow ice beside the rounded
   air-hydrate inclusions of deep ice, making the disappearance of bubbles and the
   optical clearing visible. Candidate original sources: Shoji & Langway (1982,
   *Nature*) for the first Dye-3 hydrate micrographs, or a Vostok/Dome Fuji air-hydrate
   imaging paper. Confidence: medium that such a panel exists in the published
   literature; specific source to be selected and credited by Andrew.

2. **Depth–pressure diagram of the transition zone.** A schematic plotting hydrostatic
   pressure and the air-hydrate dissociation pressure against depth, with their
   crossing near 500 m and the shaded ~500–1250 m coexistence band where the two
   populations overlap — visualizing paragraph 2's metastability argument. Origin:
   original figure (to be drafted from the Vostok numbers); no attribution needed.

If the deck pool is mounted on a future run, search it for any clathrate / air-bubble /
ice-core thin-section slide and catalog it then with its *original* publication source.

**Detector gate:** `PASS  /tmp/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

## 2026-06-16 (run 19) — sections/cryosphere/sea-ice.md

**Why this section:** the "Freezing of seawater" subsection ends by stating that
once a solid cover exists, "further growth is congelation at the bottom of the ice,
paced by how fast heat can be conducted up through the ice to the cold air" — a
correct qualitative claim that the chapter never turns into an equation. The chapter
is otherwise quantitatively complete (brine-volume relation, effective specific heat,
both with derivations), so the conduction-limited growth law is the one missing piece
of its thermodynamic spine. The draft supplies it: the quasi-steady conduction balance
ρ_i L_i dh/dt = k_i(T_f−T_s)/h, its integral to the Stefan / freezing-degree-day law
h≈√(2k_iθ/ρ_iL_i), the 1/h deceleration that makes thin ice grow fast and thick ice
slowly (and hence a thermodynamic equilibrium thickness), and the two corrections that
make real growth slower than the pure parabola — brine-reduced k_i,L_i plus snow cover,
and the finite surface heat-exchange resistance that adds the linear term in h²+ah=bθ.
It uses only citations already in references.bib (maykut1971, thomas2017); no new bib
entry is needed.

**Where it goes:** in the "Freezing of seawater" subsection, appended after the
sentence ending "…paced by how fast heat can be conducted up through the ice to the
cold air," or as a short subsection "Conduction-limited growth" placed before
"Crystal growth and brine entrapment." The brine-reduced k_i, L_i it invokes are the
ones defined later under "Brine-controlled properties," so a forward-reference there
(or moving this just after that subsection) is Andrew's call.

**Drafted prose (gate-passing):**

Once a continuous cover has formed, further thickening proceeds by freezing at the base, and its rate is set by conduction through the ice already present. The latent heat released as seawater freezes onto the bottom of the cover must travel upward to reach the cold air above, and for thin ice the column carries this flux in near-equilibrium, with a nearly linear temperature gradient between the freezing point at its base and the colder surface above. Equating the conductive flux down that gradient to the latent heat liberated at the freezing front gives a growth law for the thickness $h$,

$$
\rho_i L_i \frac{\mathrm{d}h}{\mathrm{d}t} = \frac{k_i\,(T_f - T_s)}{h},
$$

with $k_i$ the thermal conductivity, $L_i$ the latent heat of fusion, $T_f$ the freezing point at the base, and $T_s$ the surface temperature. Integrating shows that it is the squared thickness that accumulates in proportion to the time-integrated temperature deficit,

$$
h^2(t) = h_0^2 + \frac{2 k_i}{\rho_i L_i}\int_0^t (T_f - T_s)\,\mathrm{d}t' = h_0^2 + \frac{2 k_i}{\rho_i L_i}\,\theta,
$$

where $\theta = \int (T_f - T_s)\,\mathrm{d}t$ is the accumulated freezing-degree-days, the cold-season index long used to forecast ice thickness {cite}`maykut1971`. The square-root dependence $h \approx \sqrt{2 k_i \theta /(\rho_i L_i)}$ is the conduction-limited, or Stefan, growth law, and it carries the asymmetry of the process. Because the thickening ice is the chief thermal resistance between ocean and air, the flux falls as $1/h$ and the growth rate decays with thickness, so thin ice freezes fast and thick ice slowly. A few tens of centimetres form in days, two or three metres take a full winter, and a thickness is eventually reached at which one winter of growth only offsets one summer of melt, the thermodynamic equilibrium thickness of perennial ice {cite}`maykut1971`.

The pure conduction law overstates real growth, for two reasons supplied by the rest of the chapter. The effective conductivity and latent heat are the brine-reduced values of the previous section, both lower than the pure-ice constants, and any snow cover adds a layer of far smaller conductivity that reduces the flux and slows thickening sharply. The surface also sits warmer than the air, because heat crosses the ice-air boundary at a finite rate rather than instantly, adding a resistance that does not depend on the ice thickness. Folding that resistance into the balance replaces the parabola with the form $h^2 + a\,h = b\,\theta$, linear in $h$ while the ice is thin and reverting to the square-root growth once it is thick enough that conduction through the ice itself dominates the heat budget {cite}`thomas2017`.

**Optional worked number (for a margin example or caption, not in the gated prose):**
with k_i≈2.0 W m⁻¹ K⁻¹, ρ_i≈917 kg m⁻³, L_i≈3.34×10⁵ J kg⁻¹, a winter holding a mean
surface deficit T_f−T_s≈20 K for 120 days (θ≈2.1×10⁸ K s) gives h≈1.7 m; a 30 K deficit
gives h≈2.0 m, bracketing the "two or three metres take a full winter" statement. The
empirical degree-day fits (e.g. Lebedev/Zubov, h≈1.3 θ_days^0.58 in cm with θ in °C·day)
return ~1.2 m for the same 2400 °C·day, i.e. below the pure-Stefan value, the expected
sign of the "pure conduction law overstates real growth" correction.

**Proposed new bib entries:** none — maykut1971 and thomas2017 are already in
references.bib and are the correct sources. If Andrew wants the degree-day law
attributed to its origin rather than to the textbooks, a primary citation could be
added (Stefan 1891; or Lebedev 1938 / Zubov 1945 for the empirical form); BibTeX on
request, not added here.

**Figures:** the course-deck pool (`~/Downloads/glaciology-course-uw`,
`_extracted/<deck>/ppt/media`) was **not mounted on this run** and cannot be requested
unattended, so no deck image is cataloged. Figure proposals for this section — captions
must credit the ORIGINAL source only (rule 2), never the course:

1. **Computed growth curve: thickness vs. freezing-degree-days.** Plot h(θ) from
   h=√(2k_iθ/ρ_iL_i) over a winter's θ range, with a second curve for snow-covered ice
   (reduced effective conductivity) lying well below it, and tangent/marker annotations
   showing the 1/h deceleration and the thin-fast / thick-slow asymmetry. This is the
   natural companion to the existing computed `brine-volume.png` and would be generated
   the same way (cf. `_dev/make-text-figures.py`). Origin: **original computed figure,
   no external attribution needed** (parameters cited to maykut1971 / thomas2017 in the
   caption). Confidence: high that this is the most useful and copyright-clean option.

2. **Observational thickness-vs-time growth record (optional, deck-dependent).** A field
   or tank congelation-growth time series showing measured thickness following the √t
   envelope, to sit beside the computed curve. Candidate original sources to verify:
   Maykut & Untersteiner (1971) modelled growth, or a published Arctic landfast-ice
   thickness record (e.g. Utqiaġvik/Barrow mass-balance-site series). Confidence:
   medium that a suitable published figure exists; **specific source to be selected and
   credited by Andrew** — do not attribute without checking. If the deck pool is mounted
   on a future run, search it for any sea-ice growth / thickness-vs-time slide and
   catalog it then with its *original* publication source.

**Detector gate:** `PASS  /sessions/.../outputs/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

## 2026-06-16 (run 20) — sections/thermomechanics/surface-energy-balance.md

**Why this section:** the surface-energy-balance chapter quantifies the radiative
terms and the melt rate but leaves the turbulent fluxes entirely qualitative. Its
"## The turbulent fluxes" section states only that the sensible- and latent-heat
fluxes "are commonly written in bulk-aerodynamic form, proportional to the wind speed
and to the air-to-surface difference in temperature or in vapour pressure, with
coefficients that depend on the roughness of the surface and on the stability of the
air above it" — the two flux equations, the transfer coefficient, the von Kármán /
roughness-length origin of that coefficient, the stable-stratification suppression
over a melting surface, and the Bowen ratio are all named but never written. This is
also the first draft from the thermomechanics part, which had not been touched in any
prior run. The draft supplies the missing quantitative layer: the bulk-aerodynamic
forms of $H_S$ and $H_L$, the neutral transfer coefficient from the log-profile match,
the stability correction over a melting surface and the role of katabatic winds, and
the Bowen ratio with its reduction to the gradient ratio, which makes the chapter's
later "maritime" (turbulent-driven) versus "cold dry sunny" (sublimation) contrast
quantitative. Consulted {cite}`cuffey2010` (Chapter 5, the chapter's own stated
reference for the surface energy balance) for the budget and bulk method; the
bulk-aerodynamic forms, the log-profile transfer coefficient, and the stability/Bowen
treatment are standard surface-boundary-layer physics, additionally supported by the
proposed energy-balance review {cite}`hock2005`. Prose is original.

**Proposed placement:** the three paragraphs go into "## The turbulent fluxes",
*appended after* the existing single qualitative paragraph (which ends "…sculpting the
surface into the blades of ice called penitentes."). They give the symbolic form of
exactly that paragraph's claims — the bulk-aerodynamic proportionality, the
roughness/stability dependence of the coefficients, and the sensible-vs-latent
partition — without replacing the prose lead-in. No existing text is removed. The
later "## Albedo and the melt–albedo feedback" and "## What the budget produces"
sections are untouched. Optionally the equation block could carry a `{admonition}
Derivation :class: dropdown` for the neutral-coefficient log-profile match, in the
style of the chapter's existing melt-rate derivation, but the draft keeps it inline to
match the surrounding density.

**Drafted prose (gate-passing, verbatim):**

> Both turbulent fluxes are written in bulk-aerodynamic form, as the product of the
> wind speed with the vertical difference in temperature or humidity between the air
> and the surface {cite}`cuffey2010,hock2005`. The sensible-heat flux is
> $$
> H_S = \rho_a\,c_p\,C_S\,u\,(T_a - T_s),
> $$
> with $\rho_a$ the air density, $c_p\approx 1005\ \mathrm{J\,kg^{-1}\,K^{-1}}$ the
> specific heat of air at constant pressure, $u$ and $T_a$ the wind speed and
> temperature at a reference height, $T_s$ the surface temperature, and $C_S$ a
> dimensionless bulk transfer coefficient. The latent-heat flux takes the same form in
> the specific humidity $q$,
> $$
> H_L = \rho_a\,L_v\,C_L\,u\,(q_a - q_s),
> $$
> with $L_v$ the latent heat of vaporization and $C_L$ the corresponding transfer
> coefficient, and with the surface humidity $q_s$ fixed at its saturation value at
> $T_s$. Each flux is positive, delivering energy to the surface, when the overlying
> air is warmer or more humid than the surface, and it reverses sign when the gradient
> does.

> The transfer coefficients follow from the shape of the wind, temperature, and
> humidity profiles in the lowest few metres of the atmosphere. Over a uniform surface
> these profiles are logarithmic in height, and matching the bulk gradient to the
> turbulent flux gives, in neutral conditions, $C_S = k^2/[\ln(z/z_0)\,\ln(z/z_{0T})]$,
> where $k\approx 0.4$ is the von Kármán constant, $z$ the measurement height, and
> $z_0$ and $z_{0T}$ the roughness lengths for momentum and for heat. The coefficient
> grows with the aerodynamic roughness of the surface and falls as the measurement
> height increases. A melting glacier surface is colder than the air above it, so the
> near-surface layer is stably stratified, and the stability damps the turbulence and
> reduces the coefficients below their neutral values; the bulk formulae therefore
> carry a stability correction, a function of the Monin-Obukhov length, to account for
> it {cite}`hock2005`. The strong, persistent katabatic winds that drain cold air off
> the large ice sheets keep the turbulent fluxes appreciable despite this stable
> stratification.

> The ratio of the two turbulent fluxes, the Bowen ratio $\beta = H_S/H_L$, measures
> how the turbulent energy is split between heating and phase change. Because both
> fluxes share the same wind speed and nearly the same transfer coefficient, the ratio
> reduces to $\beta \approx (c_p/L_v)\,(T_a - T_s)/(q_a - q_s)$, set by the relative
> size of the temperature and humidity gradients. When the air is warm and moist, the
> latent flux adds the heat released as vapour condenses onto the surface, and the two
> fluxes reinforce each other, the regime of the maritime glaciers already noted, where
> melt proceeds under cloud that suppresses the shortwave. When the air is cold and
> dry, the humidity gradient reverses, vapour leaves the surface, and the latent flux
> becomes a sink that removes both mass and energy through sublimation, the regime of
> the high tropical glaciers where sublimation can consume most of the available
> energy.

**Register note:** the draft was calibrated against the surface-energy-balance habits
of Cuffey & Paterson (2010, Ch. 5): subject-first declaratives, each symbol defined in
an apposed "with X the …" clause immediately after its equation (matching the
chapter's own melt-rate paragraph), plain physical verbs ("grows with", "damps",
"reduces", "reverses"), and the two climatic regimes attached to the Bowen ratio as
observational appositives rather than as an aphoristic pair. The sensible/latent
contrast is stated through the gradient signs, not anthropomorphized. The third
paragraph deliberately reuses the chapter's own later vocabulary ("maritime glaciers
already noted", "high tropical glaciers", "sublimation") so the quantitative insert
threads into the existing qualitative discussion rather than duplicating it.

**Numerical / dimensional check (for Andrew, not for the prose):** both flux
expressions are W m⁻² ([kg m⁻³][J kg⁻¹ K⁻¹][–][m s⁻¹][K] = W m⁻² for $H_S$; the
analogous combination with $L_v$ in J kg⁻¹ and $q$ dimensionless for $H_L$). With
representative melt-season values ρ_a≈1 kg m⁻³, $C_S$≈0.002, $u$≈5 m s⁻¹, $T_a-T_s$≈5 K
the sensible flux is ≈50 W m⁻², the right order for a melting surface. The two Bowen
forms agree exactly when $C_S=C_L$ (direct $H_S/H_L$ and the reduced
$(c_p/L_v)(\Delta T/\Delta q)$ both give β≈1.005 for the test gradients $\Delta T=5$ K,
$\Delta q=2\times10^{-3}$). The neutral coefficient $k^2/[\ln(z/z_0)\ln(z/z_{0T})]$ with
$k=0.4$, $z=2$ m, $z_0=1$ mm, $z_{0T}=0.1$ mm evaluates to 0.0021, consistent with the
≈0.002 used. The chapter's own stated ≈315 W m⁻² blackbody emission at 0 °C reproduces
as εσ(273.15 K)⁴ = 316 W m⁻², confirming internal consistency with the existing
radiative paragraph. All correct.

**Proposed new BibTeX entry (optional — `cuffey2010` alone already suffices and is
already cited by the chapter):**

```bibtex
@article{hock2005,
  title   = {Glacier melt: a review of processes and their modelling},
  author  = {Hock, Regine},
  journal = {Progress in Physical Geography},
  volume  = {29},
  number  = {3},
  pages   = {362--391},
  year    = {2005},
  doi     = {10.1191/0309133305pp453ra}
}
```

This is the canonical review of glacier surface-melt processes and their
parameterization (energy-balance and temperature-index methods, the bulk-aerodynamic
turbulent fluxes, and the stability corrections), and it pairs naturally with the
already-present {cite}`hock2003` temperature-index entry that the chapter's closing
positive-degree-day discussion draws on. If Andrew prefers to add no new reference, the
two `{cite}`hock2005`` calls can be changed to `{cite}`cuffey2010`` with no loss, since
C&P Ch. 5 covers all of the drafted physics. (Andrew should verify the volume/number/
pages/DOI before merging — proposed from memory: high confidence on
author/title/year/journal, medium confidence on the volume/number/pages/DOI.)

**Figure proposals:**

The course-deck figure pool (`~/Downloads/glaciology-course-uw`) was **not mounted on
this run** (checked: only the book repo, outputs, and uploads are mounted; `~/Downloads`
absent), so no deck image/slide is cataloged. One *original* schematic is proposed, to
be generated with matplotlib in the style of the existing `_dev/make-*.py` figures (no
third-party attribution required because it would be drawn fresh).

1. **The surface energy budget as a labelled flux diagram.** A schematic glacier
   surface with downward/upward arrows for each term of $Q_M$: incoming shortwave
   $S_\downarrow$ with the reflected fraction $\alpha S_\downarrow$ split off, incoming
   longwave $L_\downarrow$, emitted longwave $\varepsilon\sigma T_s^4$, the two turbulent
   fluxes $H_S$ and $H_L$ (arrow direction set by the sign convention), and the
   conductive flux $Q_C$ into the ice, with the residual $Q_M$ shown driving melt at
   $\dot m=Q_M/\rho_w L_f$. Arrow widths proportional to a representative melt-season
   magnitude (e.g. absorbed shortwave ≈200, net longwave ≈−40, sensible ≈50, latent
   ≈30, conduction small, in W m⁻²) to convey the relative sizes. Origin: original
   figure (to be drafted) — no attribution needed.

If a future run has the decks mounted, search the surface-mass-balance / ablation /
energy-balance deck media for a measured energy-budget partition (a stacked
flux-versus-time plot from an automatic weather station, e.g. on a Greenland or alpine
glacier) and catalog it with its *original* publication source, following rule 2 —
never the course.

**Detector gate:** `PASS  /sessions/.../outputs/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

---

## 2026-06-17 (run 21) — sections/foundations/optical-properties.md

**Why this section:** the optical/dielectric chapter (~1660 words, among the
thinnest foundations chapters and not previously drafted) carries its central
dielectric claim entirely in words. The "## Orientational polarization and
dielectric relaxation" section states that the permittivity "drops, through the
Debye relaxation, from its static value near 100 to a high-frequency value of about
3.2," that loss is greatest "in the kilohertz range," and that radio-band absorption
is "the high-frequency tail of the Debye relaxation, proportional to 1/τ" with an
Arrhenius τ — all correct, none written as an equation. The Debye complex
permittivity, the loss-peak position at ωτ=1, the ωτ≫1 reduction that actually
produces the 1/τ scaling, and the loss tangent are never given, so the chapter's
"1/τ tail" and "order of magnitude per twenty degrees" assertions float without their
algebra. The draft supplies exactly that missing symbolic layer: ε*(ω), the split
into ε′ and ε″, the loss peak and Cole–Cole arc, and the high-frequency-tail
algebra that ties the radar-band loss to τ and hence to the Arrhenius temperature
law already in the text. It complements rather than repeats the "Electronic
polarization," "Vibrational polarization," and "permittivity spectrum" sections.
Consulted {cite}`fletcher1970` and {cite}`petrenko1999` (both already in
references.bib and cited by the chapter) for the physics; the single-relaxation /
Cole–Cole result is attributed to its original source, Auty & Cole (1952), proposed
as a new bib entry below. Prose is original.

**Proposed placement:** the two paragraphs go into "## Orientational polarization
and dielectric relaxation", inserted immediately after the existing first paragraph
(the one ending "…carries a record of its temperature and chemistry.") and before
the existing "This temperature dependence is where the absorption spectrum of ice
moves." paragraph. They give the symbolic form of the qualitative relaxation just
described and set up the Arrhenius-tail paragraph that follows, which then leads
into {numref}`fig-ice-attenuation-temperature`. No text is replaced; the draft is
purely additive.

**Drafted prose (gate-passing, verbatim):**

> The single relaxation time of the orientational response gives the permittivity
> the frequency dependence Debye derived for a polar dielectric. Written as a
> complex permittivity, $\epsilon^*(\omega)=\epsilon_\infty+(\epsilon_s-\epsilon_\infty)/(1+i\omega\tau)$,
> with $\epsilon_s\approx100$ the static value and $\epsilon_\infty\approx3.2$ the
> value left once the dipoles have dropped out, the response separates into a real
> part that falls from $\epsilon_s$ toward $\epsilon_\infty$ as $\omega\tau$ passes
> through unity and an imaginary part $\epsilon''=(\epsilon_s-\epsilon_\infty)\,\omega\tau/(1+\omega^2\tau^2)$
> that measures absorption. The imaginary part forms a single loss peak centred at
> $\omega\tau=1$, a few kilohertz in ice near the melting point, where the real
> permittivity has dropped to the mean of its two limits and the energy absorbed per
> cycle is largest. Plotting $\epsilon''$ against $\epsilon'$ across frequency traces
> a semicircle in the complex plane, the Cole–Cole arc, and its near-exact closure
> for pure ice shows that one relaxation time captures the orientational response
> {cite}`auty1952`.
>
> The radar band lies far above this loss peak, in the regime $\omega\tau\gg1$,
> where the imaginary part reduces to $\epsilon''\approx(\epsilon_s-\epsilon_\infty)/(\omega\tau)$.
> Absorption on the high-frequency side of the relaxation thus falls inversely with
> frequency and inversely with the relaxation time, so that at a fixed sounding
> frequency the dielectric loss is governed almost entirely by $\tau$. The loss
> tangent $\tan\delta=\epsilon''/\epsilon'$, which sets the attenuation rate,
> inherits the same $1/\tau$ scaling, and because $\tau$ obeys the Arrhenius law of
> the preceding paragraph that scaling carries the steep temperature dependence
> directly into the radar-band absorption. This is the quantitative content of the
> order-of-magnitude-per-twenty-degrees rule and of the attenuation curves of
> {numref}`fig-ice-attenuation-temperature`. The radar window rides on the
> high-frequency tail of a relaxation whose height and width are fixed by the
> orientational defects of {doc}`point-defects`.

**Proposed new bib entry** (add to references.bib; canonical original source for the
single-Debye / Cole–Cole result for ice — verify volume/pages/DOI before merging):

```bibtex
@article{auty1952,
  author  = {Auty, R. P. and Cole, R. H.},
  title   = {Dielectric Properties of Ice and Solid {D$_2$O}},
  journal = {The Journal of Chemical Physics},
  volume  = {20},
  number  = {8},
  pages   = {1309--1314},
  year    = {1952},
  doi     = {10.1063/1.1700726},
}
```

**Figure proposals:** the course-deck pool (`~/Downloads/glaciology-course-uw`)
was **not mounted on this automated run**, so the deck `media`/slide XML could not be
searched for a candidate image; no deck figure is catalogued here. The natural
illustration for these two paragraphs is not a sourced photograph but a *computed*
plot, matching how this chapter's two existing figures were produced (the scripts in
`_dev/make-ice-attenuation-temperature-figure.py` and
`_dev/make-ice-absorption-figure.py`). Recommended:

1. **Cole–Cole arc of ice** — ε″ plotted against ε′ as frequency sweeps the
   relaxation, showing the semicircle from $\epsilon_s\approx100$ to
   $\epsilon_\infty\approx3.2$ with the apex at $\omega\tau=1$. Pure computed curve
   from the Debye expressions above; **no external attribution needed** (Andrew's own
   figure). Optionally a small inset of $\epsilon'(\omega)$ and $\epsilon''(\omega)$
   to mark where the radar band sits on the high-frequency tail. A short
   `_dev/make-cole-cole-figure.py` would produce it in the existing style.

If Andrew would prefer a sourced figure instead, a published dielectric-dispersion /
Cole–Cole plot for ice can be located on a future run once the deck pool is mounted,
with the original paper credited per rule 2 (never the course).

**Detector gate:** `PASS  /sessions/fervent-exciting-faraday/mnt/outputs/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

## 2026-06-17 (run 22) — sections/radar/radiowave-fabric.md

**Why this section:** `radiowave-fabric.md` is the thinnest radar chapter (~1390 words)
and had not been drafted before. It builds the birefringence physics carefully —
anisotropic permittivity, the structure tensor `⟨c²⟩`, fast/slow eigenwaves, and the
travel-time splitting `Δt(z) ∝ ∫(λx−λy)dz'` — but it stops at the *scalar* travel-time
difference and only gestures at what real surveys measure. Its closing paragraph says
"phase-sensitive systems such as ApRES measure this difference through the phase of the
returns, and multi-element and polarimetric radars measure it across the full
polarization plane," without giving the physics of that azimuthal measurement: how
returned power depends on antenna azimuth, why the extinction bands appear, what their
depth spacing and azimuthal orientation each encode, and what the modern coherence
method adds. The draft supplies exactly that missing layer — the co-polarized
azimuth/depth power law `1 − sin²2θ·sin²(δ/2)`, the depth-recurrence of the extinction
bands and its link back to `λx−λy`, the separate orientation information carried by the
azimuth of the bands, and the HHVV-coherence phase-gradient method. It complements
rather than repeats the existing birefringence and travel-time sections.

Consulted `{cite}`rathmann_notes`` (already in references.bib, the chapter's existing
backbone reference for the wave physics) for the eigenwave/slowness framework, and the
two primary polarimetric-radar papers below (proposed new bib entries) for the
azimuthal power signature and the coherence method. Prose is original.

**Proposed placement:** a new subsection `## The azimuthal power signature`, inserted
into "## From travel-time difference to fabric" immediately after the result paragraph
that ends "…proportional to the depth-integrated difference between the two horizontal
fabric eigenvalues," and *before* the existing closing synthesis paragraph ("By
measuring how the travel-time difference…"). The two new paragraphs then supply the
physics that the closing paragraph's nod to ApRES and "the full polarization plane"
currently asserts without derivation. No existing text is replaced; the draft is purely
additive. The symbol δ is introduced here as δ(z)=ω·Δt(z), reusing the chapter's Δt(z).

**Drafted prose (gate-passing, verbatim):**

> A downward-looking radar can also record returned power as a function of the angle
> between its antenna and the fabric principal axes, and that azimuthal dependence
> carries the same information as the travel-time splitting. With the transmitting and
> receiving antennas co-polarized and rotated together through an azimuth $\theta$
> measured from a principal axis, the outgoing field projects onto the two birefringent
> eigenwaves in proportion to $\cos\theta$ and $\sin\theta$, and the waves recombine at
> the receiver after accumulating the two-way phase difference $\delta(z)=\omega\,\Delta
> t(z)$. The co-polarized power then follows $1-\sin^2 2\theta\,\sin^2(\delta/2)$,
> falling to zero where the antenna lies at $45^\circ$ to the axes and $\delta$ is an
> odd multiple of $\pi$. The returns show extinction bands that recur in depth wherever
> $\delta$ advances by $2\pi$, and the depth spacing of those bands fixes the
> birefringent phase gradient and so the single-crystal anisotropy weighted by
> $\lambda_x-\lambda_y$ {cite}`fujita2006`.
>
> The azimuthal pattern separates two properties of the fabric that the scalar
> travel-time difference leaves entangled. The azimuth at which the extinction bands sit
> locates the horizontal principal axes and returns the orientation of the fabric, a
> quantity the travel-time difference alone does not constrain. The bands arise from the
> relative phase of the two co-polarized returns, so a phase-sensitive instrument can
> read that phase rather than track power minima. Modern surveys form the coherence
> between the two orthogonal co-polarized channels and take its phase gradient with
> depth, recovering the birefringent phase rate and the horizontal anisotropy together
> while suppressing the scattering amplitude that the raw power image mixes in
> {cite}`jordan2019`.

**Proposed new bib entries** (verify before adding; neither key is in references.bib):

```bibtex
@article{fujita2006,
  title   = {Radio-wave depolarization and scattering within ice sheets: a matrix-based model to link radar and ice-core measurements and its application},
  author  = {Fujita, Shuji and Maeno, Hideo and Matsuoka, Kenichi},
  journal = {Journal of Glaciology},
  volume  = {52},
  number  = {178},
  pages   = {407--424},
  year    = {2006},
  doi     = {10.3189/172756506781828548}
}

@article{jordan2019,
  title   = {A polarimetric coherence method to determine ice crystal orientation fabric from radar sounding: application to the {NEEM} ice core region},
  author  = {Jordan, Tom M. and Schroeder, Dustin M. and Castelletti, Davide and Li, Jilu and Dall, Jorgen},
  journal = {IEEE Transactions on Geoscience and Remote Sensing},
  volume  = {57},
  number  = {11},
  pages   = {8641--8657},
  year    = {2019},
  doi     = {10.1109/TGRS.2019.2921980}
}
```

**Figure proposals** (cataloged only — not copied into the repo; attributions PROPOSED,
verify before use; per rule 2 the course is never credited):

1. **Fabric pole figures vs depth** — deck `W02a_PhysicalProperties`, slide 40,
   images `ppt/media/image25.png` + `ppt/media/image26.png` (a paired set). Four
   Schmidt (equal-area) pole plots of c-axis orientation at 148 m, 806 m, 2396 m and
   2633 m, circle position = c-axis direction on the hemisphere, circle area = crystal
   size. They show the progression from a near-isotropic fabric (148 m) through a
   broadening/girdle-like distribution (2396 m) to a tight vertical single maximum
   (2633 m) — a direct picture of the structure-tensor eigenvalues λx, λy, λz that the
   polarimetric radar of this chapter recovers, ideal next to the new subsection.
   *Proposed source:* deep ice-core c-axis fabric data; the slide labels the Schmidt
   plots `Gagliardini et al. (2004), J. Glaciol.` and also lists `Wittlinger and
   Farra (2015), Polar Science` with "horizontal thin sections from NGRIP, Greenland."
   The 148–2633 m depth range is consistent with an NGRIP-type deep core.
   **Confidence: medium** — Andrew should confirm which of the two papers the pole
   figures are reproduced from (Schmidt plots → likely Gagliardini et al. 2004; raw
   NGRIP thin-section data → Wittlinger & Farra 2015) and cite that original, not a
   secondary reproduction.

2. **Ice-sheet fabric/temperature cross-section (context)** — deck
   `W02a_PhysicalProperties`, slide 40, image `ppt/media/image27.jpg`. A schematic
   depth section of an ice sheet (Dome C / EPICA style) showing the firn layer, the
   temperature profile, and the transition from isotropic ice near the surface to a
   strong vertical c-axis single maximum at depth, annotated with P- and S-wave
   velocities for isotropic vs anisotropic ice. Useful as context for *why* the radar
   birefringence signal strengthens with depth. The image carries many in-figure
   credits (Gagnon et al. 1988 for the velocities; King & Jarvis 2007; Bentley 1971;
   Siegert et al. 2005; Anandakrishnan & Winberry 2004; Lythe & Vaughan 2001), so it is
   a *composite* schematic whose original publication is not identifiable from the
   figure alone. **Confidence: low — origin unknown, uncredited; flag for Andrew** (do
   not use until the source publication is identified, per rule 2). Secondary to
   proposal 1.

**Detector gate:** `PASS  /sessions/epic-gifted-gates/mnt/outputs/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

## 2026-06-17 (run 23) — sections/foundations/point-defects.md

**Why this section:** the point-defects chapter is otherwise mature (~2325 words), but
its closing "## Electrical and mechanical roles of defects" section *asserts* the headline
numbers — a relaxation time of order $10^{-4}\ \mathrm{s}$ and a permittivity falling from
~100 to ~3.2 — without connecting them to the defect concentrations and mobilities the rest
of the chapter worked so hard to establish (ionic ~$10^{10}\ \mathrm{cm^{-3}}$, orientational
~$10^{15}$–$10^{16}\ \mathrm{cm^{-3}}$, with their separate mobilities and activation energies).
The chapter says the orientational defects "control the dielectric relaxation" and that the
ionic defects "are the carriers of the small direct-current conductivity," but it never gives
the quantitative bridge — Jaccard's theory — that turns those concentrations and mobilities
into $\tau$ and into the two limiting conductivities, nor the series argument that explains
why pure ice can have a tiny DC conductivity yet a huge dielectric response. The draft
supplies exactly that bridge. It complements rather than repeats both the Bjerrum section
(which gives the concentrations) and the already-drafted optical-properties Debye treatment
(run 21, phenomenological $\varepsilon^*(\omega)$): this entry derives the relaxation rate and
the DC conductivity *from the defect parameters*, and closes the loop to ice-core ECM acidity
logging that the radar/em-waves chapter already leans on.

Consulted {cite}`fletcher1970` (Ch. 7, the chapter's own backbone reference) and
{cite}`petrenko1999` for the Jaccard formulation, the effective charges, and the
series-conductivity argument; both keys are already in references.bib. One new key
({cite}`hammer1980`) is proposed below for the ECM acidity application. Prose is original
and substantially shorter than any source treatment.

**Proposed placement:** insert as two paragraphs at the head of (or immediately after the
first paragraph of) the existing "## Electrical and mechanical roles of defects" section,
before/around the sentence that quotes the $10^{-4}\ \mathrm{s}$ relaxation time, so the
asserted numbers are immediately backed by the Jaccard derivation. No existing text need be
removed; the draft is additive and reuses the chapter's own symbols ($n_\mathrm{DL}$,
$\mu_\mathrm{DL}$, $\tau$) and its stated concentrations. New symbols introduced here:
effective charges $e_\mathrm{DL}, e_\pm$; limiting conductivities $\sigma_\infty,
\sigma_\mathrm{DC}, \sigma_\pm, \sigma_\mathrm{DL}$.

**Drafted prose (gate-passing, verbatim):**

> Jaccard's theory makes the link between the orientational defects and the dielectric
> response quantitative. Each defect family is assigned an effective charge, set by how far
> the proton configuration shifts when the defect moves one step, and the two charges add to
> the protonic charge $e$, with the orientational value near $0.38\,e$ and the ionic value
> near $0.62\,e$ {cite}`petrenko1999`. A molecular dipole reorients only when a $D$- or
> $L$-defect steps past it, so the polarization built up in a static field decays at a rate
> fixed by how many orientational defects pass a given molecule per unit time. The Debye
> relaxation rate is therefore proportional to the product of the orientational-defect
> concentration $n_\mathrm{DL}$ and their mobility $\mu_\mathrm{DL}$, and the same product
> fixes the high-frequency limiting conductivity $\sigma_\infty \approx
> n_\mathrm{DL}\,e_\mathrm{DL}\,\mu_\mathrm{DL}$ that the relaxation approaches above the
> dispersion. Inserting the $10^{15}$ to $10^{16}\ \mathrm{cm^{-3}}$ concentration and the
> measured Bjerrum mobility returns a relaxation time of order $10^{-4}\ \mathrm{s}$ near
> $-10\ \mathrm{^\circ C}$, and the activation energy carried by $\tau$ is that of
> orientational-defect migration {cite}`fletcher1970`.
>
> The static conductivity follows the complementary rule. A steady proton current cannot flow
> on the ionic defects alone, because once an ionic defect has carried a proton along a chain
> of bonds it leaves those bonds doubly and singly occupied and unable to pass the next proton
> until an orientational defect restores the configuration. The two families must act in
> series, and the direct-current conductivity is throttled by whichever family is rarer, the
> sparse ionic defects in pure ice, so that $\sigma_\mathrm{DC}^{-1} \approx \sigma_\pm^{-1} +
> \sigma_\mathrm{DL}^{-1}$ {cite}`petrenko1999`. Pure ice therefore combines a small
> direct-current conductivity, of order $10^{-8}\ \mathrm{S\,m^{-1}}$ and set by the ionic
> population, with a large dielectric response governed by the far more numerous orientational
> defects. Acids that dope the lattice with extra ionic defects raise $\sigma_\mathrm{DC}$
> much more than they shift $\tau$, the basis for reading the direct-current conductivity of a
> core as a record of its acidity and so of past volcanic fallout {cite}`hammer1980`.

**Proposed new bib entry** (verify before adding; key not in references.bib):

```bibtex
@article{hammer1980,
  title   = {Acidity of polar ice cores in relation to absolute dating, past volcanism, and radio-echoes},
  author  = {Hammer, C. U.},
  journal = {Journal of Glaciology},
  volume  = {25},
  number  = {93},
  pages   = {359--372},
  year    = {1980},
  doi     = {10.3189/S0022143000015227}
}
```

**Figure proposals:** the figure source pool (`~/Downloads/glaciology-course-uw`,
`_extracted/<deck>/ppt/media`) was **not mounted on this scheduled run**, so the deck/slide/
filename references that rule 4 of the procedure asks for could not be verified here. The two
candidates below are therefore proposed *by description and by likely original source only*;
on the next run, with the folder remounted, locate the matching slide, confirm the image
filename, and confirm the source before use. Per rule 2 the course is never credited.

1. **Dielectric dispersion / Cole–Cole plot of pure ice** — a plot of the complex
   permittivity showing the real part falling from $\varepsilon_s\!\approx\!100$ to
   $\varepsilon_\infty\!\approx\!3.2$ through the relaxation and the corresponding loss peak,
   or equivalently the single Cole–Cole semicircle, at a stated temperature near $-10\
   \mathrm{^\circ C}$ (relaxation near a few kHz). This is the direct visual of the $\tau$ and
   the two limiting permittivities the new prose derives. *Proposed original source:* the
   classic single-crystal measurements of **Auty & Cole (1952), *J. Chem. Phys.* 20, 1309**,
   or the compiled dispersion curves in **Petrenko & Whitworth (1999), *Physics of Ice***
   (the latter a secondary reproduction — prefer the primary). **Confidence: medium** for
   Auty & Cole as the underlying data; Andrew should confirm which figure a deck actually
   reproduces once the pool is remounted.

2. **ECM (electrical-conductivity) record vs depth from a polar core** — a downcore trace of
   DC current showing sharp acidity spikes at dated volcanic horizons against a low background,
   the applied payoff of the static-conductivity paragraph. *Proposed original source:*
   **Hammer (1980), *J. Glaciol.* 25(93)** (Dye-3 / Greenland ECM, the {cite}`hammer1980`
   proposed above), or a later GRIP/NGRIP ECM compilation if the deck uses one. **Confidence:
   low–medium — origin to be confirmed**; do not credit any specific core or paper until the
   actual deck figure and its caption are inspected. Secondary to proposal 1.

**Detector gate:** `PASS  /sessions/optimistic-inspiring-bell/mnt/outputs/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.

---

## 2026-06-17 (run 24) — sections/cryosphere/planetary-ice.md

**Why this section:** the closing chapter's `## Amorphous ice and high-pressure phases`
section is a one-paragraph survey that hands all of the underlying physical chemistry
off to {doc}`../foundations/lattice-dynamics` and {doc}`../foundations/ice-structure`
("the phase diagram sketched in lattice-dynamics shows … at least seventeen crystalline
polymorphs"), states that high-pressure phases "differ substantially from ice Ih" without
saying *how*, and asserts that amorphous ice "crystallizes irreversibly above roughly
130 K" with no mention that there are two distinct amorphous solids or that they
interconvert. It is also the thinnest physics in an otherwise quantitative book
(`cryosphere/planetary-ice` is ~2480 words, much of it descriptive) and is squarely the
domain of one of the project's three reference texts, Fletcher's *The Chemical Physics of
Ice*, plus Petrenko & Whitworth. The draft adds three short paragraphs that supply exactly
the missing layer, parallel in depth to the foundations chapters they cross-reference:
(1) the **high-pressure polymorphs** as a progressive collapse of the open Ih framework
that keeps four hydrogen bonds per molecule while folding the O–O–O angles and threading
the network through itself — ice II/III/V/VI at ~1.17–1.31 g cm⁻³ over a few tenths of a
GPa to ~1 GPa, ice VII/VIII reaching ~1.5 g cm⁻³ above ~2 GPa by interpenetrating two
sublattices — and the consequence that an icy moon's deep-water rheology and conductivity
are those of the dense phases, not of Ih; (2) the **proton order/disorder axis**, the ice
rules and Pauling's residual entropy $S_0\approx R\ln(3/2)\approx 3.4$ J mol⁻¹ K⁻¹
confirmed calorimetrically, the disordered/ordered polymorph pairs (Ih–XI, III–IX, V–XIII,
VI–XV, VII–VIII), and their kinetic freeze-in below ~100 K via the same orientational-defect
reorientation that sets dielectric relaxation in {doc}`../foundations/point-defects`; and
(3) **polyamorphism**, the two amorphous solids (LDA ~0.94, HDA ~1.17 g cm⁻³) and Mishima's
sharp pressure-driven LDA→HDA transition near a few tenths of a GPa at ~130 K, framed as the
glassy analogue of the crystalline open→dense reorganization, with the comet-ice paragraph's
amorphous solid identified as the low-density form. Consulted Fletcher, *The Chemical Physics
of Ice* (ice polymorphs, proton ordering, residual entropy) and Petrenko & Whitworth, *Physics
of Ice* (phase diagram, amorphous ices); prose is original, substantially shorter than and
reworded from the sources. The amorphous-ice paragraph deliberately dovetails with the
chapter's existing comet text two paragraphs above (the "[TODO-CITE: Schmitt … 1998]" placeholder
there is untouched — Andrew's to resolve).

**Drafted prose** (insert into / replace the existing `## Amorphous ice and high-pressure
phases` body; the three paragraphs are written to follow the section heading and the chapter's
existing opening sentence about ice Ih):

> The high-pressure polymorphs are best understood as a progressive collapse of the open
> framework of ice Ih under load. The hexagonal lattice of {doc}`../foundations/ice-structure`
> is only about 0.92 g cm⁻³ because full tetrahedral coordination holds the oxygen atoms far
> apart, and that openness becomes thermodynamically expensive once the pressure does
> appreciable work against the molar volume. The denser crystalline phases relieve the volume
> without sacrificing the four hydrogen bonds per molecule. Ice II, III, V, and VI fold the
> O–O–O angles away from the tetrahedral value and thread the network through itself, raising
> the density to between about 1.17 and 1.31 g cm⁻³ over the range from a few tenths of a
> gigapascal to roughly 1 GPa, and ice VII and VIII reach near 1.5 g cm⁻³ above about 2 GPa by
> interleaving two independent hydrogen-bonded sublattices {cite}`fletcher1970,petrenko1999`.
> The base of the water layer in a large icy moon spans exactly this part of the phase diagram,
> so the rheology and conductivity used in any thermal model of Ganymede or Titan must be those
> of the dense phases rather than of ice Ih.
>
> A second axis of the phase diagram concerns the protons rather than the oxygen lattice. In
> ice Ih and in most of the high-pressure phases the protons satisfy the ice rules of
> {doc}`../foundations/ice-structure`, one hydrogen on each bond and two near each oxygen, yet
> remain disordered among the arrangements those rules allow. Counting the permitted
> configurations gives the residual entropy first estimated by {cite}`pauling1935`,
> $S_0 \approx R\ln(3/2) \approx 3.4\ \mathrm{J\,mol^{-1}\,K^{-1}}$, a value later confirmed by
> low-temperature calorimetry. Many of the polymorphs accordingly occur as proton-disordered
> and proton-ordered counterparts, ice Ih with ice XI, ice III with ice IX, ice V with ice
> XIII, ice VI with ice XV, and ice VII with ice VIII, the ordered member appearing only on
> slow cooling. The ordering transition is sluggish at low temperature because it proceeds by
> the same reorientation of orientational defects that limits the dielectric relaxation of
> {doc}`../foundations/point-defects`, and below about 100 K the disordered form is effectively
> frozen in.
>
> The amorphous solids show the same contrast between an open and a collapsed network without
> any crystalline order at all. Two distinct forms exist, low-density amorphous ice near 0.94 g
> cm⁻³ and high-density amorphous ice near 1.17 g cm⁻³, and {cite}`mishima1985` found that
> compressing the low-density form past a few tenths of a gigapascal near 130 K converts it
> sharply to the high-density form, with a reversible jump in volume that resembles a
> transition between two liquids. The density step mirrors the open-to-dense contrast of the
> crystalline phases, so polyamorphism is the glassy analogue of the structural reorganization
> that the pressure axis drives in the crystal. The comet-borne amorphous ice of the previous
> paragraph is the low-density form, deposited cold enough to trap volatiles, and its
> irreversible crystallization above roughly 130 K is the release that helps power distant
> cometary outbursts.

**Proposed new BibTeX entry** (not added to `references.bib`; Andrew applies). `fletcher1970`,
`petrenko1999`, and `pauling1935` are already in the bibliography; only the polyamorphism paper
is new:

```bibtex
@article{mishima1985,
  author  = {Mishima, O. and Calvert, L. D. and Whalley, E.},
  title   = {An apparently first-order transition between two amorphous phases of ice induced by pressure},
  journal = {Nature},
  volume  = {314},
  number  = {6006},
  pages   = {76--78},
  year    = {1985},
  doi     = {10.1038/314076a0}
}
```

**Figures:** the `glaciology-course-uw` course-deck folder (`~/Downloads/glaciology-course-uw`,
the figure source pool) was **not mounted in this run**, so no deck images could be inspected or
catalogued against their slide XML. No figure is therefore proposed from the decks this run; the
candidates below are *concepts* for Andrew to source (and to check the decks for), with original-
source suggestions at low confidence per the provenance rule. **No attributions invented; none to
be credited until the actual source is confirmed.**

1. **A water phase diagram with the crystalline polymorph fields labelled** (log-pressure axis,
   showing the Ih / II / III / V / VI / VII–VIII stability fields and the LDA/HDA region). *Note:*
   the book **already contains** such a figure — `../math/figures/water-phase-diagram.png`,
   credited to M. Chaplin's *Water Structure and Science*, used in
   {doc}`../foundations/lattice-dynamics`. The cleanest move is to **cross-reference that existing
   figure** with a {numref} pointer rather than introduce a new one; no new provenance needed.
   *Confidence: high that this is the right figure to point at.*
2. **A volume- (or density-) vs-pressure curve of the LDA↔HDA polyamorphic transition**, showing
   the sharp step near a few tenths of a GPa at ~130 K. *Proposed original source:* **Mishima,
   Calvert & Whalley (1985), *Nature* 314, 76–78** (the {cite}`mishima1985` proposed above), or a
   later Mishima/Stanley review of polyamorphism. *Confidence: low — exact figure and its
   redrawing/permission status to be confirmed by Andrew; do not reproduce the copyrighted figure,
   redraw from the data if used.*
3. **Side-by-side ball-and-stick schematics of the open ice-Ih framework vs an interpenetrating
   ice-VII network**, to make "collapse without losing four-coordination" concrete. *Proposed
   original source:* origin unknown — **uncredited, for Andrew to source** (such schematics are
   common in Petrenko & Whitworth and Fletcher but must not be reproduced from the copyrighted
   texts; an open-licensed crystal-structure rendering would need to be found or generated).
   *Confidence: low.*

**Detector gate:** `PASS  /sessions/fervent-zen-sagan/mnt/outputs/tmp/enrich_draft.md  (0 paragraph(s) flagged, strict=True)` — exit 0.
