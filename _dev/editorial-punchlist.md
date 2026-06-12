# Editorial punch list

Findings from the whole-book cohesion audit (June 2026), minus everything already
fixed (openers, headings, transitions marked done). Organized for an editing pass.
This folder does not build into the book. Delete items as they are resolved.

## Duplications to consolidate (pick one owner)

- Tensor invariants are derived twice: tensor-algebra.md (Invariants) and
  stress-and-strain.md (Invariants and the effective quantities). Suggest
  tensor-algebra owns the mathematics; stress-and-strain cites it and keeps only
  the effective-stress/strain-rate definitions.
- The action/variational principle appears in both finite-elements.md and
  icepack-intro.md. Suggest finite-elements owns the derivation; icepack-intro
  keeps one sentence and a {doc} pointer.
- Grounding-line flux exponents: glacier-variations.md (two-stage model, beta = 4.75),
  ice-sheets.md (flux ~ h_g^5 boundary-layer result), and sliding-laws-lab use
  related but differently-stated exponents. One chapter (ice-sheets) should own the
  Schoof result and the others should reference it with consistent notation.

## Candidates for optional asides (dropdown admonitions)

- glacier-variations.md: the three-stage ODE algebra block (keep the result and
  the sigmoid in main text; derivation to a dropdown).
- paleoclimate.md: the Rayleigh distillation integration (keep calibration
  discussion in main text; the d(ln R) integral to a dropdown — the isotope lab
  re-derives it anyway).
- water-molecule.md: the C2v / A1-B1-B2 symmetry-classification paragraph
  (interesting, never used downstream).
- prognostic-problem.md: the mid-sentence bolds (**explicit Euler**, **CFL
  condition**, **stiff**) should be unbolded or italicized; the Vialov/Response/
  MISI lead-bolds in Verification are consistent with house style and can stay.

## Stark openers flagged but not yet rewritten (judgment calls)

- panchromatic-imagery.md: "A photograph of an ice sheet seems the most ordinary..."
  (setup-then-reveal; could open with the declassified 1960s imagery instead).
- insar.md opener (definition-sentence structure; the 1993 Rutford first could lead).
- magnetotellurics.md opener (chain of antecedents; the Whillans groundwater
  discovery could lead).
- optical-properties.md opener (buries the lead; flip observation methods first).
- flow-approximations.md opener (announces rather than opens).
- hydrology.md opener (restates the previous chapter before advancing).
- former-glaciers.md: "Most of the ice this book studies is gone." (borderline;
  the second sentence is the stronger opener).
- running-icepack-docker.md opener (fine for a how-to page; lowest priority).

## Cross-references to re-aim after the restructure

- mass-balance.md mentions "now measured directly by satellite altimetry" — the
  observing part now comes AFTER this chapter; phrase as a forward pointer.
- ice-sheets.md references {doc}`../observing/insar` and {doc}`../observing/gravity`
  — also now forward; fine as explicit pointers, but the prose should not assume
  the reader has seen them.
- thermal-structure.md surge section still pre-empts hydrology.md's drainage-switch
  results in mechanistic detail; trim to a pointer and let hydrology pay it off.

## Running example opportunity

The Amundsen Sea sector appears independently in laser-altimetry, insar, gravity,
ice-sheets, sliding-laws-lab, and sea-level. Cross-linking these as one running
example (each chapter adding an instrument or a process to the same place) would
be the single highest-value cohesion move in the observing part.

## Loose ends

- TODO-CITE markers remain in planetary-ice.md (Nimmo & Manga; McKinnon 2016;
  Schmitt et al. 1998), magnetotellurics-lab (wait1954/tikhonov1950, vozoff1972,
  egbert1997, archie1942), gravity-lab (Whitehouse GIA review, IMBIE 2018/2020,
  Watkins 2015), sliding-laws-lab (Thwaites thinning/velocity obs), laser/radar
  labs (none outstanding). All are plain text and build-safe; resolve at leisure.
- deuterium excess is mentioned in paleoclimate.md but never used; either connect
  it (moisture-source discussion pairs with the isotope lab's Task 5) or cut.
- _video_review/ holds six unidentified course clips worth a watch.
- The creep-curve figure (figures/creep-curve.svg) and the nine other Illustrator
  TODO specs are embedded as % comments at their insertion points; grep
  "TODO Illustrator" for the full list.
