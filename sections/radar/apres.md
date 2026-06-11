# Phase-sensitive radar (ApRES)

Radar is one of the main tools glaciologists use to see inside ice. Radio waves pass through cold ice with little loss and reflect from changes in electrical properties, so a radar records echoes from internal layers and from the bed. Why ice is transparent to radio waves at all, and what sets their speed and attenuation, is the subject of {doc}`em-waves`. Ordinary ice-penetrating radar measures the strength and timing of those echoes to map thickness and internal structure, and the radar texts {cite}`bogorodsky1985` and {cite}`richards2010` cover the underlying theory. This chapter describes a particular instrument, the Autonomous phase-sensitive Radio-Echo Sounder, or ApRES, which the group uses to measure how ice deforms and melts.

## Why phase matters

ApRES is a frequency-modulated continuous-wave radar that records the full complex return, both its amplitude and its phase, as a function of depth {cite}`nicholls2015`. The amplitude tells you where the reflectors are. The phase is what makes the instrument powerful. The phase of a reflection advances by a full cycle for every half wavelength of change in the distance to the reflector, and the wavelength in ice is short, so a phase measurement is sensitive to changes in range far smaller than the radar's nominal range resolution. By comparing the phase of the same reflector in two acquisitions separated in time, ApRES can detect vertical displacements of a fraction of a millimetre.

## From displacement to strain and melt

A single ApRES measurement is a depth profile of complex returns. The science comes from repeating the measurement at the same place after an interval of hours, days, or a year, and asking how far each reflector has moved. Internal reflectors move closer together as the ice column thins under vertical strain, so tracking many internal reflectors with depth gives the vertical strain rate. The bed is a special reflector. Its apparent motion relative to the strain field of the overlying ice reveals whether ice is being added or removed at the base. After the contribution of internal strain is removed, the residual motion of the bed gives the basal melt rate, which on an ice shelf is the rate at which the ocean is melting the ice from below.

This is the measurement behind much of the group's work on ice-shelf melt. Because ApRES instruments can be left to run autonomously through a polar winter, they turn a single radar site into a continuous record of strain and melt, which is difficult to obtain any other way.

The next page is a lab that processes real ApRES data with the group's processing library to recover a basal melt-rate time series.
