"""Static figures of the deformation mechanisms, for the ice-deformation chapter.

Each figure shows one mechanism at four stages (panels A-D), drawn by the same
code as its animation, in the book's figure style. Run from the repo root:

    python _dev/deformation_mechanisms/make_figures.py            # all
    python _dev/deformation_mechanisms/make_figures.py basal-glide

Writes sections/ice_flow/figures/mechanism-<name>.png.
"""
import argparse
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import FIG_DIR, MECHANISMS  # noqa: E402
import lattice  # noqa: E402,F401
import grains  # noqa: E402,F401
import potts  # noqa: E402,F401

# (t, stage title) for each panel; t is the animation's normalized time.
STAGES = {
    "elastic": [(0.0, "Unloaded"), (0.28, "Loaded in shear"),
                (0.58, "Unloading"), (1.0, "Recovered exactly")],
    "basal-glide": [(0.05, "Shear on the basal planes"), (0.22, "A dislocation glides"),
                    (0.40, "It exits, leaving a step"), (1.0, "Three dislocations later")],
    "nonbasal-glide": [(0.12, "Same stress, two orientations"), (0.24, "Basal slip runs freely"),
                       (0.62, "Prismatic slip lags"), (1.0, "Three basal passes, one partial")],
    "dislocation-climb": [(0.20, "Glide stopped by an obstacle"), (0.42, "A vacancy diffuses in"),
                          (0.66, "Climb by one plane"), (0.84, "Glide resumes")],
    "kink-band": [(0.0, "Load parallel to basal planes"), (0.20, "The planes bow"),
                  (0.50, "A kink band forms"), (1.0, "Rotated band, dislocation walls")],
    "dislocation-creep": [(0.0, "Undeformed polycrystal"), (0.30, "Slip in soft grains"),
                          (0.60, "Grains flatten and rotate"), (1.0, "After 32% shortening")],
    "fabric-development": [(0.0, "Random fabric"), (0.35, "c-axes rotate"),
                           (0.65, "Clustering about vertical"), (1.0, "Single maximum")],
    "grain-boundary-sliding": [(0.0, "Scribed marker line"), (0.30, "Boundaries slide"),
                               (0.55, "Neighbours switch"), (1.0, "Equiaxed grains, offset line")],
    "nabarro-herring-creep": [(0.0, "Loaded grains"), (0.30, "Diffusion through grains"),
                              (0.65, "Grains lengthen"), (1.0, "Lattices unrotated")],
    "coble-creep": [(0.0, "Loaded grains"), (0.30, "Diffusion along boundaries"),
                    (0.65, "Grains lengthen"), (1.0, "Lattices unrotated")],
    "polygonization": [(0.0, "Bent grain"), (0.25, "Dislocations glide and climb"),
                       (0.50, "Sub-grain walls"), (1.0, "New grain boundaries")],
    "migration-recrystallization": [(0.0, "Deformed warm ice"), (0.30, "Boundaries bulge"),
                                    (0.60, "Clean grains grow"), (1.0, "Recrystallized")],
    "nucleation-recrystallization": [(0.0, "Heavily deformed ice"), (0.10, "Nuclei at boundaries"),
                                     (0.30, "A necklace of new grains"), (1.0, "Recrystallized")],
    "grain-growth": [(0.0, "Fine grains"), (0.33, "Small grains shrink"),
                     (0.66, "Coarsening continues"), (1.0, "Grain area linear in time")],
    "premelting": [(0.0, "Cold: dry boundaries"), (0.30, "Water films and veins"),
                   (0.70, "Shear on wet boundaries"), (1.0, "Boundaries have slid")],
    "brittle-fracture": [(0.10, "Rapid compression"), (0.40, "Boundaries crack"),
                         (0.70, "Wing cracks link"), (1.0, "A fault forms")],
}


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("names", nargs="*")
    a = p.parse_args()
    unknown = set(a.names) - set(STAGES)
    if unknown:
        p.error(f"unknown: {', '.join(sorted(unknown))}")
    for slug, stages in STAGES.items():
        if a.names and slug not in a.names:
            continue
        t0 = time.time()
        video, draw = MECHANISMS[slug][1]()
        path = video.still(draw, stages, os.path.join(FIG_DIR, f"mechanism-{slug}.png"))
        print(f"{slug:30s} {time.time() - t0:5.1f} s -> {os.path.relpath(path)}", flush=True)


if __name__ == "__main__":
    main()
