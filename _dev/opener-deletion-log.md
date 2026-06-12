# Paragraph-opener deletion log — June 12, 2026

Book-wide pass deleting corny paragraph-opening sentences (aphorisms, teasers,
pause/wonder flourishes, empty meta). Rule applied: delete only if the sentence
carried no information beyond mood/announcement (or its content is restated by
the rest of the paragraph) AND the paragraph reads cleanly from its second
sentence. Stitches were limited to pronoun→noun swaps. Every deletion is listed
here for review; `git diff` shows exact context. Notebooks (.ipynb) were not
touched.

## Foundations

- preface.md — "The thermal properties are extravagant."
- preface.md — "One thesis organizes all of it."
- composition.md — "The formula itself is the first thing the electrons explain."
- energy-levels.md — "The simplest case yields the most useful number in this chapter."
- energy-levels.md — "Light connects the rungs."
- energy-levels.md — "The kit is now complete."
- water-molecule.md — "One more feature is important for what follows."
- water-molecule.md — "Natural water is not one molecule but a family."
- water-molecule.md — "These forces are real but secondary."
- water-molecule.md — "It is worth keeping in view how directly these molecular facts shape the ice that glaciologists study."
- ice-structure.md — "There is an important subtlety in the structure."
- ice-structure.md — "The proton arrangement is not frozen for all time."
- ice-structure.md — "The perfect lattice described so far ends somewhere, and where it ends the structure pays a price."
- ice-structure.md — "A surprising amount of glaciology lives in this thin liquid."
- lattice-dynamics.md — "It is worth doing the count once, with numbers small enough to hold in your head."
- lattice-dynamics.md — "The same derivative produces the most important distribution in this book."
- lattice-dynamics.md — "Before moving on, put scales on the counting."
- lattice-dynamics.md — "A feature of this spectrum is decisive for the properties that follow."
- lattice-dynamics.md — "Latent heat itself deserves its moment."
- point-defects.md — "It is worth stepping back to see what the point defects accomplish, because two apparently unrelated bodies of glaciological measurement rest on them."
- optical-properties.md — "One refinement matters for the most powerful radar method."
- snow-to-ice.md — "Where meltwater enters the story, it reorganizes it."

## Getting started, modeling, math

- prognostic-problem.md — "The diffusion analogy carries physical intuition worth keeping."
- prognostic-problem.md — "The prognostic loop can only run if it starts somewhere."
- (intro.md, labs-intro, icepack-intro, running-icepack-docker, icepack-ice-shelf, tensor-algebra, finite-elements — no deletions)

## Ice deformation and flow

- stress-and-strain.md — "Before the tensors, a choice has to be made about coordinates, and it is worth making consciously because glaciology uses both options daily."
- stress-and-strain.md — "It helps to see the tensors in the two simplest deformations."
- ice-rheology.md — "Ice deforms in a way that sets it apart from a metal." [stitch: "It shows" → "Ice shows"]
- ice-rheology.md — "The rate-controlling step, and the one that ties the mechanics of flow back to the molecular structure, is more subtle."
- ice-rheology.md — "Deform the sample further and the truce breaks in the ice's favor."
- ice-rheology.md — "The evidence for the law reaches well beyond the laboratory."
- ice-rheology.md — "The exponent is not universal."
- ice-rheology.md — "The activation energy is not constant."
- ice-rheology.md — "It is worth being clear about the status of Glen's law." [stitch: "It is empirical" → "Glen's law is empirical"]
- ice-fabric.md — "Three archetypes organize the possibilities."
- stress-balance.md — "A point that often surprises newcomers is that the driving stress depends on the slope of the upper surface, not the bed."
- shallow-ice.md — "Glen's law has a revealing limit."
- mass-balance.md — "A glacier is a budget."
- mass-balance.md — "This single equation is why ice flow matters for sea level."

## Bed, basal processes, climate

- thermal-structure.md — "The melting point of ice is not fixed." [stitch: "It decreases" → "The melting point of ice decreases"]
- thermal-structure.md — "The feedback between temperature and flow does more than localize streams." [stitch: pronoun → noun]
- thermal-structure.md — "The surge cycle is easier to believe once you have watched one."
- basal-motion.md — "Not every fast glacier rests on hard rock."
- glacier-variations.md — "A modest perturbation produces a substantial advance."
- glacier-variations.md — "Geometry sets the gain of the lever."
- glacier-variations.md — "The numbers this formula produces are the useful surprise."
- glacier-variations.md — "The difference matters most for exactly the problems this chapter cares about."
- climate-forcing.md — "Before asking how climate forces glaciers, it is worth pausing on a prior question: what kind of object are we actually studying?"
- climate-forcing.md — "That memory is worth making precise, because it shapes everything that follows." [stitch: "statement of it" → "statement of that memory"]
- sea-level.md — "The bookkeeping is the easy part."
- paleoclimate.md — "The connection is still not simple."
- paleoclimate.md — "The forcing itself is worth watching."

## Wider cryosphere

- erosion.md — "A useful orientation is that the products are local."
- erosion.md — "The two processes feed each other."
- ice-sheets.md — "The stakes are easy to state."
- ice-sheets.md — "How to judge significance is part of the science here."
- instabilities.md — "A surge is defined by its rhythm."
- instabilities.md — "The mechanism reads directly out of the observations."
- instabilities.md — "The calving that drives the fast half of the cycle is worth watching once at full violence."
- sea-ice.md — "The brine also drains."
- sea-ice.md — "The modern decline of Arctic sea ice runs through this entire chapter."
- former-glaciers.md — "Most of the ice this book studies is gone."
- former-glaciers.md — "The logic is worth making explicit, because it inverts the rest of the book."
- permafrost.md — "The engineering consequences follow directly."
- permafrost.md — "Permafrost is also not confined to Earth."

## Observing ice, radar

- laser-altimetry.md — "That centimetre precision rests on timing."
- panchromatic-imagery.md — "The reach of optical imagery in time is remarkable."
- cryoseismicity.md — "For all its slow creep, ice is a noisy material."
- cryoseismicity.md — "The method has overturned the picture of how some ice streams move."
- magnetotellurics.md — "The method came of age in glaciology when it was used to look beneath an ice stream."
- apres-lab.md — "The science is in the comparison of profiles taken at different times."
- radiowave-fabric.md — "This relationship is what makes radar a fabric instrument."

## Kept on purpose (borderline, contentful)

"The solid floats on its own liquid." (preface), "Ice sheets are also archives."
(paleoclimate), "The ice sheets are not passive recorders of these cycles; they
are half of the machinery." (paleoclimate), "Swap the laser's light for
microwaves..." (radar-altimetry), "Two satellite missions define the record.",
"The radar window is not perfectly transparent." — punchy but carrying the
paragraph's actual claim, per the delete rule.

Total: 71 deletions across 33 files.
