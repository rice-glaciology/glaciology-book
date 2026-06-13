# Phase-sensitive radar (ApRES)

A radar echo from inside an ice column carries more than the location of its reflector; held to sub-wavelength precision, it can watch that reflector move. Radio waves pass through cold ice with little loss and reflect from changes in electrical properties, so a radar records echoes from internal layers and from the bed, and why ice is transparent to radio waves at all, and what sets their speed and attenuation, is the subject of {doc}`em-waves`. Ordinary ice-penetrating radar measures the strength and timing of those echoes to map thickness and internal structure, and the radar texts {cite}`bogorodsky1985` and {cite}`richards2010` cover the underlying theory. This chapter describes the instrument that turns the echo's *phase* into a measurement, the Autonomous phase-sensitive Radio-Echo Sounder, or ApRES, built to measure how ice deforms and melts.

## The phase measurement

ApRES is a frequency-modulated continuous-wave radar, an instrument that transmits a continuous tone swept smoothly upward in frequency so that each reflector's range appears as a beat frequency between the outgoing and returning signals, and it records the full complex return, both amplitude and phase, as a function of depth {cite}`nicholls2015`. The amplitude tells you where the reflectors are. The phase is what makes the instrument powerful. The phase of a reflection advances by a full cycle for every half wavelength of change in the distance to the reflector, and the wavelength in ice is short, so a phase measurement is sensitive to changes in range far smaller than the radar's nominal range resolution. By comparing the phase of the same reflector in two acquisitions separated in time, ApRES can detect vertical displacements of a fraction of a millimetre.

## From displacement to strain and melt

A single ApRES measurement is a depth profile of complex returns. The science comes from repeating the measurement at the same place after an interval of hours, days, or a year, and asking how far each reflector has moved. Internal reflectors move closer together as the ice column thins under vertical strain, so tracking many internal reflectors with depth gives the vertical strain rate. The bed is a special reflector. Its apparent motion relative to the strain field of the overlying ice reveals whether ice is being added or removed at the base. After the contribution of internal strain is removed, the residual motion of the bed gives the basal melt rate, which on an ice shelf is the rate at which the ocean is melting the ice from below.

This is the measurement behind much of what is now known about how ice-shelf basal melt varies in time. Because ApRES instruments can be left to run autonomously through a polar winter, they turn a single radar site into a continuous record of strain and melt, which is difficult to obtain any other way.

Put concretely, a single instrument drawing roughly the power of a car battery over months sits on the snow surface and detects motion of a millimetre or less in a reflector 800 metres below, week after week through a polar winter with no one present. The ice column above the reflector, with all its own slow deformation, is part of what the instrument is measuring and accounting for. The number that comes out at the end is how fast the ocean ate into the bottom of the shelf while the instrument sat in the dark.

---

## Lab: basal melt from ApRES

This lab turns a series of repeat ApRES acquisitions into a record of vertical strain and basal melt, using the open `apres` processing package rather than writing the signal processing from scratch. As with the modeling labs, it is not executed when the book is built, so the page shows the code and explains what it produces. Run it where the `apres` package and a folder of ApRES data are available.

```{admonition} Getting the package
:class: note
The `apres` package implements a standard ApRES preprocessing and strain workflow of the kind used in published ice-shelf melt studies. It currently lives alongside the field-site processing repositories. To use it here it should be installed as a package, for example with `pip install -e path/to/apres`, so that `import apres` works from any notebook. Packaging it into a single installable repository, and adding it to the book's Docker image, is on the to-do list.
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

`strain_melt_between_profiles` aligns a pair of profiles, first coarsely and then to sub-wavelength precision using the phase, fits the vertical strain implied by the motion of the internal reflectors, and attributes the residual motion of the bed to melting or freezing. It returns the time separation, the vertical strain rate, and the basal melt rate, along with diagnostic arrays.

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
