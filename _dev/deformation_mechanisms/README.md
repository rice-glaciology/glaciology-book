# Deformation-mechanism animations

Code for the videos and the mechanism map in
`sections/ice_flow/deformation-mechanisms.md`.

```bash
pip install numpy scipy matplotlib        # plus ffmpeg on the PATH
python _dev/deformation_mechanisms/make_videos.py --list          # what exists
python _dev/deformation_mechanisms/make_videos.py                 # render all (~15 min)
python _dev/deformation_mechanisms/make_videos.py basal-glide     # one video
python _dev/deformation_mechanisms/make_videos.py --preview 0.5 --out /tmp/p   # stills
python _dev/deformation_mechanisms/mechanism_map.py               # static figure
```

Videos and poster frames go to `_static/videos/deformation/`.

| File | Contents |
|---|---|
| `figstyle.py` | The Morrow, Ghelichkhan & Kramer (2026) figure framework (github.com/sghelichkhani/morrow2026): Times/STIX at 15/17/13 pt, upper-case panel letters in grey circles, light-yellow title boxes, light-blue readout boxes, fixed series colours, 10-band colour bars |
| `common.py` | Frame layout (panels, caption, orientation colour bar), MP4 writer, registry |
| `lattice.py` | Atomic scale: elasticity, basal and non-basal glide, climb, kinking. Edge dislocations use the linear-elastic displacement field, with the slipped surface following the core's path so climb works. |
| `grains.py` | Voronoi polycrystals: dislocation creep, fabric development, grain-boundary sliding (Ashby–Verrall switching), Nabarro–Herring and Coble creep, polygonization, premelting, brittle failure |
| `potts.py` | Monte Carlo Potts model with stored energy: migration recrystallization, nucleation, normal grain growth |
| `alley1988.py` | Alley (1988) grain-rotation model: Fig. 1/2 flow regimes, and a Byrd-like column linking depth to mechanism |
| `mechanism_map.py` | Goldsby–Kohlstedt (2001) mechanism map at −10 °C |

To add a mechanism, write a function decorated with `@mechanism("slug", order)`
that returns `(Video(...), draw)`, where `draw(ax, t)` redraws the panel for
normalized time `t` in [0, 1] (or `draw(axes, t)` when `Video(panels=[...])`).

The book's other computed figures are made by `_dev/make_book_figures.py`, in the
same style (`figstyle.py` at the repository root).
