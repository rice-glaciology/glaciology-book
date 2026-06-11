#!/usr/bin/env bash
# Copies course videos into the book. Embedded videos go to _static/videos/
# and are then compressed to web-friendly .mp4 (see ffmpeg loop in the repo
# notes) and committed; unidentified ones go to _video_review/ at the book
# root (NOT shipped) — watch them, rename, and promote the keepers.
# Run once:  bash copy_movies.sh   (re-running restores originals, so the
# ffmpeg compression pass must be repeated afterward)
set -euo pipefail

SRC="$HOME/Downloads/glaciology-course-uw"
EXT="$SRC/_extracted"
BOOK="$HOME/projects/glaciology-book"

mkdir -p "$BOOK/_static/videos" "$BOOK/_video_review"

# --- embedded in chapters ---
cp "$SRC/paulabreen_surge.m4v"                                  "$BOOK/_static/videos/paulabreen-surge.m4v"
cp "$EXT/W04b_Glacier_Flow/ppt/media/media1.MOV"                "$BOOK/_static/videos/helheim-calving.mov"
cp "$EXT/W05a_IceDynamics_Sliding/ppt/media/media1.mp4"         "$BOOK/_static/videos/outburst-flood-usgs.mp4"
cp "$EXT/W09a_IceAge_Cycles/ppt/media/media1.m4v"               "$BOOK/_static/videos/insolation-cycles.m4v"

# --- content not yet identified; review before embedding ---
cp "$EXT/W05b_IceTemperature/ppt/media/media1.mp4"              "$BOOK/_video_review/w05b-surface-slide24.mp4"
cp "$EXT/W08a_PaleoClimate_IceCores_part1/ppt/media/media1.mp4" "$BOOK/_video_review/w08a-slide4.mp4"
cp "$EXT/W08a_PaleoClimate_IceCores_part1/ppt/media/media2.m4v" "$BOOK/_video_review/w08a-slide8.m4v"
cp "$EXT/W04a_Ablation/ppt/media/media1.mp4"                    "$BOOK/_video_review/w04a-slide4.mp4"
cp "$EXT/W04a_Ablation/ppt/media/media2.mp4"                    "$BOOK/_video_review/w04a-slide5.mp4"
cp "$EXT/W06b_IceSheets/ppt/media/media1.mp4"                   "$BOOK/_video_review/w06b-slide14.mp4"

# clean up the earlier misplaced copy of the surge video, if present
rm -rf "$BOOK/sections/thermomechanics/media"

echo "Videos copied. Embedded: $(ls "$BOOK/_static/videos" | wc -l | tr -d ' '). For review: $(ls "$BOOK/_video_review" | wc -l | tr -d ' ')."
