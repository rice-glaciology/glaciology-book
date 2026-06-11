#!/usr/bin/env bash
# Copies figures selected from the ESS 431 course decks (extracted to
# ~/Downloads/glaciology-course-uw/_extracted) into the book's figure
# directories, with descriptive names matching the {figure} directives.
# Run once:  bash copy_figures.sh
set -euo pipefail

SRC="$HOME/Downloads/glaciology-course-uw/_extracted"
BOOK="$HOME/projects/glaciology-book/sections"

mkdir -p "$BOOK/math/figures" "$BOOK/foundations/figures" \
         "$BOOK/thermomechanics/figures" "$BOOK/thermomechanics/media" \
         "$BOOK/climate/figures" "$BOOK/cryosphere/figures" \
         "$BOOK/ice_flow/figures"

# --- chemistry primer (sections/math) ---
cp "$SRC/W02a_PhysicalProperties/ppt/media/image4.png"  "$BOOK/math/figures/water-molecule-geometry.png"
cp "$SRC/W02a_PhysicalProperties/ppt/media/image5.gif"  "$BOOK/math/figures/hydrogen-bond-network.gif"
cp "$SRC/W02a_PhysicalProperties/ppt/media/image16.png" "$BOOK/math/figures/water-phase-diagram.png"

# --- foundations ---
cp "$SRC/W02a_PhysicalProperties/ppt/media/image6.png"  "$BOOK/foundations/figures/tetrahedral-coordination.png"
cp "$SRC/W02a_PhysicalProperties/ppt/media/image7.png"  "$BOOK/foundations/figures/ice-ih-lattice.png"
cp "$SRC/W02a_PhysicalProperties/ppt/media/image12.jpg" "$BOOK/foundations/figures/snow-crystal-libbrecht.jpg"
cp "$SRC/W02a_PhysicalProperties/ppt/media/image11.png" "$BOOK/foundations/figures/bjerrum-defect-lattice.png"
cp "$SRC/W03b_Accumulation_2/ppt/media/image14.jpeg"    "$BOOK/foundations/figures/lachapelle-metamorphism.jpeg"
cp "$SRC/W04a_Ablation/ppt/media/image32.jpeg"          "$BOOK/foundations/figures/siple-pit-annual-layers.jpeg"
cp "$SRC/W04a_Ablation/ppt/media/image31.jpeg"          "$BOOK/foundations/figures/benson-facies-zones.jpeg"

# --- ice flow ---
cp "$SRC/W04b_Glacier_Flow/ppt/media/image14.jpg"       "$BOOK/ice_flow/figures/mer-de-glace-ogives.jpg"
cp "$SRC/W04b_Glacier_Flow/ppt/media/image20.png"       "$BOOK/ice_flow/figures/athabasca-transverse-velocity.png"
cp "$SRC/W04b_Glacier_Flow/ppt/media/image54.png"       "$BOOK/ice_flow/figures/velocity-profiles-n1-n3.png"
cp "$SRC/W04a_Ablation/ppt/media/image38.jpeg"          "$BOOK/ice_flow/figures/blue-glacier-balance-gradient.jpeg"
cp "$SRC/W04a_Ablation/ppt/media/image17.jpeg"          "$BOOK/ice_flow/figures/penitentes-atacama.jpeg"

# --- thermomechanics ---
cp "$SRC/W05b_IceTemperature/ppt/media/image34.png"     "$BOOK/thermomechanics/figures/seasonal-wave-periods.png"
cp "$SRC/W05b_IceTemperature/ppt/media/image39.png"     "$BOOK/thermomechanics/figures/divide-temperature-profile.png"
cp "$SRC/W05b_IceTemperature/ppt/media/image40.png"     "$BOOK/thermomechanics/figures/jakobshavn-temperature-profiles.png"
cp "$SRC/W05a_IceDynamics_Sliding/ppt/media/image27.png" "$BOOK/thermomechanics/figures/iken-sliding-water-level.png"
cp "$SRC/W05a_IceDynamics_Sliding/ppt/media/image28.png" "$BOOK/thermomechanics/figures/storglaciaren-pressure-speed.png"
cp "$SRC/W05a_IceDynamics_Sliding/ppt/media/image32.png" "$BOOK/thermomechanics/figures/till-deformation-breidamerkurjokull.png"
cp "$HOME/Downloads/glaciology-course-uw/paulabreen_surge.m4v" "$BOOK/thermomechanics/media/paulabreen_surge.m4v"

# --- climate ---
cp "$SRC/W08b_PaleoClimate_IceCores_part2/ppt/media/image10.png"  "$BOOK/climate/figures/vostok-ghg-temperature.png"
cp "$SRC/W08b_PaleoClimate_IceCores_part2/ppt/media/image45.jpeg" "$BOOK/climate/figures/gisp2-abrupt-change-severinghaus.jpeg"
cp "$SRC/W08b_PaleoClimate_IceCores_part2/ppt/media/image20.png"  "$BOOK/climate/figures/wais-sulfate-volcanic-markers.png"
cp "$SRC/W09a_IceAge_Cycles/ppt/media/image24.png"                "$BOOK/climate/figures/specmap-ice-volume-insolation.png"
cp "$SRC/W09a_IceAge_Cycles/ppt/media/image26.png"                "$BOOK/climate/figures/ice-volume-rate-insolation.png"

# --- cryosphere ---
cp "$SRC/W06b_IceSheets/ppt/media/image19.png"          "$BOOK/cryosphere/figures/ice-sheet-velocity-maps.png"
cp "$SRC/W06b_IceSheets/ppt/media/image18.png"          "$BOOK/cryosphere/figures/ice-sheet-bed-topography.png"
cp "$SRC/W07a_RecentChanges/ppt/media/image36.png"      "$BOOK/cryosphere/figures/larsen-b-speedup-wuite.png"
cp "$SRC/W07a_RecentChanges/ppt/media/image46.jpeg"     "$BOOK/cryosphere/figures/jakobshavn-speed-timeseries.jpeg"
cp "$SRC/W10_Sea_Ice/ppt/media/image29.jpeg"            "$BOOK/cryosphere/figures/sea-ice-salinity-thickness.jpeg"
cp "$SRC/ess431_2020_BL_structure+properties_lecture2_slidesonly/ppt/media/image13.png" "$BOOK/cryosphere/figures/brine-inclusions-light.png"
cp "$SRC/W10_Sea_Ice/ppt/media/image52.png"             "$BOOK/cryosphere/figures/arctic-thinning-scicex.png"
cp "$SRC/W11a_Glacier_Erosion/ppt/media/image38.jpeg"   "$BOOK/cryosphere/figures/cross-cutting-striations.jpeg"
cp "$SRC/W11c_Permafrost/ppt/media/image3.jpeg"         "$BOOK/cryosphere/figures/alaska-permafrost-warming.jpeg"

echo "All figures copied. ($(find "$BOOK" -path '*/figures/*' -newer "$0" | wc -l | tr -d ' ') files placed.)"
