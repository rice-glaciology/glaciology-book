# Proton-disorder and point-defect animations

Code for the videos in `sections/foundations/ice-structure.md` (proton disorder)
and `sections/foundations/point-defects.md`.

```bash
pip install numpy matplotlib              # plus ffmpeg on the PATH
python _dev/ice_defects/make_videos.py --list            # what exists
python _dev/ice_defects/make_videos.py                   # render all (~5 min)
python _dev/ice_defects/make_videos.py ionic-defects     # one video
python _dev/ice_defects/make_videos.py --preview 0.5 --out /tmp/p   # stills
```

Videos and poster frames go to `_static/videos/defects/`. The frame, writer and
figure style are shared with `_dev/deformation_mechanisms/common.py` and
`figstyle.py` at the repository root.

| File | Contents |
|---|---|
| `squareice.py` | Two-dimensional square ice: oxygens on a periodic square lattice, one proton per bond, and the Bernal–Fowler ice rules. Proton transfers move ionic defects (H₃O⁺, OH⁻), molecular rotations move Bjerrum defects (D, L), and flipping every proton around a closed loop gives a new rule-obeying arrangement. `Script` plays a sequence of these moves back over time. |
| `defects.py` | The eight animations: proton disorder and Pauling's entropy; ionic defects; Bjerrum defects; HF doping; self-diffusion by vacancies and interstitials (a honeycomb basal plane); thermally activated jumps (Langevin dynamics in a periodic potential, with the measured Arrhenius plot); the Jaccard conduction cycle; dielectric relaxation (Metropolis Monte Carlo of Bjerrum defects in a field) |
| `make_videos.py` | Command-line driver |

Square ice is the standard textbook stand-in for ice Ih (Fletcher 1970, ch. 7;
Petrenko & Whitworth 1999, ch. 4 and 6): it obeys the same ice rules and has the
same defects, but is easy to draw. The random walks in the ionic, Bjerrum and
HF clips are chosen as the clearest of several random tries, and none of the
defects revisits a molecule or bond.
