# Lab: basal melt from ApRES

This lab turns a series of repeat ApRES acquisitions into a record of vertical strain and basal melt, using the group's own `apres` processing package rather than writing the signal processing from scratch. As with the modeling labs, it is not executed when the book is built, so the page shows the code and explains what it produces. Run it where the `apres` package and a folder of ApRES data are available.

```{admonition} Getting the package
:class: note
The `apres` package implements the preprocessing and strain workflow used in the group's ice-shelf melt studies. It currently lives alongside the field-site processing repositories. To use it here it should be installed as a package, for example with `pip install -e path/to/apres`, so that `import apres` works from any notebook. Packaging it into a single installable repository, and adding it to the book's Docker image, is on the to-do list.
```

## Configure a station

Each ApRES deployment is organized by station, with its raw `.DAT` files in a data directory. `ProcessingConfig` collects the paths and the processing parameters, and `validate` checks them.

```python
from pathlib import Path
from apres import ProcessingConfig, preprocess_file, strain_melt_between_profiles
from apres.io import find_dat_files
from apres.plotting import plot_timeseries

station = "GA01"
data_dir = Path("data") / station

cfg = ProcessingConfig(
    station=station,
    data_dir=data_dir,
    figures_dir=Path("figures") / station,
    results_dir=Path("results") / station,
)
cfg.validate()
```

## Preprocess each acquisition into a depth profile

`preprocess_file` reads one raw acquisition and forms a profile of the complex radar return as a function of depth, the step that takes the frequency-modulated signal into a range profile. We do this for every file and sort the resulting profiles in time.

```python
profiles = [preprocess_file(f, cfg) for f in find_dat_files(data_dir)]
profiles = sorted(profiles, key=lambda p: p.timestamp)
print(f"{len(profiles)} acquisitions from {profiles[0].timestamp} to {profiles[-1].timestamp}")
```

## Strain and melt between repeat profiles

The science is in the comparison of profiles taken at different times. `strain_melt_between_profiles` aligns a pair of profiles, first coarsely and then to sub-wavelength precision using the phase, fits the vertical strain implied by the motion of the internal reflectors, and attributes the residual motion of the bed to melting or freezing. It returns the time separation, the vertical strain rate, and the basal melt rate, along with diagnostic arrays.

```python
results = []
for p1, p2 in zip(profiles[:-1], profiles[1:]):
    result, coarse, fine, fit, bed = strain_melt_between_profiles(p1, p2, cfg)
    print(
        f"{p1.timestamp:%Y-%m-%d} to {p2.timestamp:%Y-%m-%d}: "
        f"strain rate {result.vsr_per_year:.2e} /yr, "
        f"basal melt {result.melt_rate_m_per_year:.2f} m/yr"
    )
    results.append(result)
```

## Plot the time series

```python
plot_timeseries(results, cfg.figures_dir / "timeseries.png", cfg, profiles=profiles)
```

The output is a record of how fast the ocean is melting the base of the ice through time, recovered from a single autonomous radar that sat on the ice and recorded the phase of its own echoes.

```{admonition} Try it yourself
:class: seealso
- Process a second station and compare the melt-rate records.
- Change the depth window used to track the bed and see how sensitive the melt rate is to that choice.
- The vertical strain rate from ApRES is an independent measurement of the same englacial deformation that Glen's flow law predicts. Compare an observed strain rate with what the rheology of {doc}`../ice_flow/ice-rheology` would give for the local stress.
```
