"""Render the proton-disorder and point-defect animations.

Run from the repo root:

    python _dev/ice_defects/make_videos.py                 # all videos
    python _dev/ice_defects/make_videos.py ionic-defects   # one
    python _dev/ice_defects/make_videos.py --preview 0.5 --out /tmp/p   # stills only
    python _dev/ice_defects/make_videos.py --list

Uses the frame, style and writer of ``_dev/deformation_mechanisms/common.py``.
Needs numpy, matplotlib and ffmpeg. Writes MP4s and poster JPEGs to
_static/videos/defects/.
"""
import argparse
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "deformation_mechanisms"))
sys.path.insert(0, HERE)

from common import MECHANISMS, REPO  # noqa: E402
import defects  # noqa: E402,F401  (registers the animations)

VIDEO_DIR = os.path.join(REPO, "_static", "videos", "defects")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("slugs", nargs="*", help="animations to render (default: all)")
    p.add_argument("--preview", type=float, metavar="T",
                   help="write one still at normalized time T instead of a video")
    p.add_argument("--list", action="store_true", help="list animations and exit")
    p.add_argument("--out", default=VIDEO_DIR)
    a = p.parse_args()
    ordered = sorted(MECHANISMS.items(), key=lambda kv: kv[1][0])
    if a.list:
        for slug, (order, _) in ordered:
            print(f"{order:3d}  {slug}")
        return
    unknown = set(a.slugs) - set(MECHANISMS)
    if unknown:
        p.error(f"unknown animation(s): {', '.join(sorted(unknown))}")
    for slug, (order, build) in ordered:
        if a.slugs and slug not in a.slugs:
            continue
        t0 = time.time()
        video, draw = build()
        path = video.render(draw, out_dir=a.out, preview_at=a.preview)
        print(f"{slug:26s} {time.time() - t0:6.1f} s  ->  {os.path.relpath(path)}", flush=True)


if __name__ == "__main__":
    main()
