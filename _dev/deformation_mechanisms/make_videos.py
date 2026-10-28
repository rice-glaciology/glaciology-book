"""Render the deformation-mechanism videos for the ice-deformation chapter.

Run from the repo root:

    python _dev/deformation_mechanisms/make_videos.py            # all videos
    python _dev/deformation_mechanisms/make_videos.py basal-glide climb
    python _dev/deformation_mechanisms/make_videos.py --preview 0.5   # stills only
    python _dev/deformation_mechanisms/make_videos.py --list

Needs numpy, scipy, matplotlib and ffmpeg on the PATH. Writes MP4s and poster
JPEGs to _static/videos/deformation/.
"""
import argparse
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import MECHANISMS, VIDEO_DIR  # noqa: E402
import lattice  # noqa: E402,F401  (registers mechanisms)
import grains  # noqa: E402,F401
import potts  # noqa: E402,F401
import alley1988  # noqa: E402,F401


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("slugs", nargs="*", help="mechanisms to render (default: all)")
    p.add_argument("--preview", type=float, metavar="T",
                   help="write one still at normalized time T instead of a video")
    p.add_argument("--list", action="store_true", help="list mechanisms and exit")
    p.add_argument("--out", default=VIDEO_DIR)
    a = p.parse_args()
    ordered = sorted(MECHANISMS.items(), key=lambda kv: kv[1][0])
    if a.list:
        for slug, (order, _) in ordered:
            print(f"{order:3d}  {slug}")
        return
    unknown = set(a.slugs) - set(MECHANISMS)
    if unknown:
        p.error(f"unknown mechanism(s): {', '.join(sorted(unknown))}")
    for slug, (order, build) in ordered:
        if a.slugs and slug not in a.slugs:
            continue
        t0 = time.time()
        video, draw = build()
        path = video.render(draw, out_dir=a.out, preview_at=a.preview)
        print(f"{slug:28s} {time.time() - t0:6.1f} s  ->  {os.path.relpath(path)}", flush=True)


if __name__ == "__main__":
    main()
