# Deformation mechanisms of ice

The flow law of {doc}`ice-rheology` compresses an entire microphysics into two numbers, a rate factor $A$ and an exponent $n$. This chapter opens that box. Ice deforms by a family of distinct mechanisms. Some move molecules, some move line defects, some move whole grains, and some rebuild the grains themselves. Each has its own dependence on stress, temperature, and grain size. Which one controls the strain rate depends on where a parcel of ice sits in that space, and that is why a single power law with $n=3$ works well across most glaciers but fails at the extremes.

Each mechanism below comes with a short animation. The animations are schematic: strains are exaggerated, timescales are compressed by many orders of magnitude, and the three-dimensional crystal is reduced to a two-dimensional section. Each is drawn to show the one thing that distinguishes its mechanism from the others. In the grain-scale videos each grain is colored by its c-axis orientation, much as grains look in a thin section viewed between crossed polarizers, and thin lines inside each grain trace its basal planes. The panel at the right of each video collects the rate law, the stress exponent, the grain-size dependence, the activation energy, and where in a glacier the mechanism matters. The code that generates them is in `_dev/deformation_mechanisms/` and can be rerun or modified.

## An overview

The mechanisms sort naturally into four groups. The first is what happens inside a single crystal: elastic stretching of bonds, and the glide, climb, and kinking of dislocations. The second is how a polycrystal accommodates an imposed strain: dislocation creep, grain-boundary sliding, and the two forms of diffusion creep. The third is how the grains themselves evolve during and after deformation, through lattice rotation, polygonization, migration recrystallization, nucleation, and normal grain growth. These processes change the microstructure, and through it the rate factor and the anisotropy. The fourth covers the edges of the ductile regime: premelting near the melting point and brittle fracture at high strain rates.

| Mechanism | What moves | Stress exponent $n$ | Grain-size exponent $p$ | Dominant where |
|---|---|---|---|---|
| Elasticity | bond lengths and angles | (linear, recoverable) | 0 | seismic waves, tides, first instants of loading |
| Basal dislocation glide | dislocations in basal planes | (carrier of most strain) | 0 | all creeping ice |
| Non-basal glide | dislocations on prismatic and pyramidal planes | high | 0 | hard grains only |
| Dislocation creep | glide plus climb in a polycrystal | ~4 | 0 | high stress: shear margins, ice streams, lab tests |
| Grain-boundary sliding | whole grains, accommodated by basal slip | ~1.8 | ~1.4 | low stress, fine grains: ice-sheet interiors |
| Nabarro–Herring creep | molecules through the lattice | 1 | 2 | very fine grains, very low stress |
| Coble creep | molecules along grain boundaries | 1 | 3 | very fine, cold grains |

Here a mechanism's strain rate scales as $\dot\varepsilon \propto \tau^n d^{-p} \exp(-Q/RT)$. The microstructural processes of the third group are not flow laws of their own. They set the grain size $d$ and the fabric that the flow laws above respond to.

{numref}`fig-mechanism-map` shows where the rate-controlling mechanisms dominate at $-10\ \mathrm{^\circ C}$, using the composite law of {cite}`goldsby2001` introduced in {doc}`ice-rheology`. A map of this kind follows the approach of {cite}`frost1982`. Glacier ice, with grains of millimetres and stresses of tens to hundreds of kilopascals, straddles the boundary between grain-boundary sliding and dislocation creep. That is the microphysical reason the effective exponent $n\approx3$ sits between the two.

```{figure} figures/deformation-mechanism-map.png
:name: fig-mechanism-map
:width: 85%

Deformation-mechanism map for ice at $-10\ \mathrm{^\circ C}$, computed from the composite flow law of {cite}`goldsby2001`. Shading marks the mechanism contributing most to the strain rate; dashed lines are contours of total strain rate. In the grain-boundary-sliding field, sliding is the slower, rate-limiting member of the sliding and basal-slip pair. Basal slip would become the limiting member only for grains of a few to tens of microns, where diffusion creep is faster still, so no basal-slip-limited field appears. Diffusion-creep parameters are approximate, so the position of that field is indicative only. Boxes show typical conditions in ice-sheet interiors and in shear margins.
```

## Inside the crystal

### Elastic deformation

Under any load, the first response of ice is elastic. The bonds between water molecules stretch, compress, and bend slightly, and every molecule keeps the same neighbors. The strain is proportional to the stress, with a Young's modulus near 9 GPa, and it vanishes the moment the load is removed. At glacier stresses the elastic strain is only about $10^{-5}$, so it matters only on short timescales: seismic waves, the tidal flexing of ice shelves, and the first instants of any loading. Over hours to days, the Maxwell time of {doc}`ice-rheology`, viscous creep overtakes it. The point of the animation is negative: elasticity alone can never produce flow, because no molecule ever changes neighbors.

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/elastic.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/elastic.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Elastic deformation: bonds stretch and recover; nothing flows.</em></p>
```

### Basal slip by dislocation glide

Permanent deformation of a crystal requires defects that move. The essential one is the dislocation, a line along which the lattice is offset by one Burgers vector $b$ (introduced in {doc}`ice-rheology`). In the animation an edge dislocation, the end of an extra half-plane of molecules, nucleates at one surface of the crystal and glides along a basal plane. Only the bonds at the core are broken and remade at any instant, which is why glide needs far less stress than shearing a whole plane at once. When the dislocation leaves the far surface, the upper half of the crystal has moved one molecular spacing and a step appears on each face. The Orowan relation $\dot\varepsilon=\rho_d b v$ is this picture summed over a dislocation density $\rho_d$ moving at speed $v$. In ice, $v$ is limited by how fast Bjerrum defects can reorder the protons ahead of the core, which sets the activation energy of about 0.6 eV {cite}`fletcher1970`. The result is a crystal that shears like a deck of cards, easily parallel to its basal planes.

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/basal-glide.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/basal-glide.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Basal slip: edge dislocations glide through the crystal, each leaving a one-molecule step.</em></p>
```

### Non-basal slip

The same stress applied to a crystal whose basal planes are perpendicular to the shear has to drive dislocations across the basal planes instead of along them, on prismatic or pyramidal planes. The resolved shear stress needed is roughly sixty times larger. The animation shows the reason in geometric form: relative to the Burgers vector, the non-basal planes are closely spaced, so the dislocation core is wide and the lattice grips it hard. The consequence for a polycrystal is fundamental. A general change of grain shape needs five independent slip systems (the von Mises criterion), and basal slip supplies only two. A grain in an aggregate therefore cannot simply deform the way its neighbors require. Something else must accommodate the mismatch: the hard systems, climb, boundary sliding, or recrystallization. Grains that depend on non-basal slip, such as those with c-axes along the compression axis in a strong fabric, are the hard grains of an aggregate.

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/nonbasal-glide.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/nonbasal-glide.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Basal versus prismatic slip under the same shear stress.</em></p>
```

### Dislocation climb and recovery

A gliding dislocation that meets an obstacle, an impurity or a tangle of other dislocations, stops. An edge dislocation can escape by climbing out of its glide plane, and climb requires diffusion. In the animation a vacancy wanders through the lattice, reaches the edge of the extra half-plane, and absorbs its last molecule. The half-plane is now one molecule shorter, so the dislocation sits on the next basal plane up and glides on past the obstacle. Climb also lets dislocations of opposite sign meet and annihilate. This is recovery, and it is why ice hardly work-hardens: once glide and climb balance, creep proceeds at a steady rate (see {doc}`ice-rheology`). Because climb is fed by lattice self-diffusion ({doc}`../foundations/point-defects`), it is thermally activated and is part of what sets the stress dependence of dislocation creep.

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/dislocation-climb.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/dislocation-climb.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Climb: a vacancy is absorbed, the dislocation steps up one plane and bypasses the obstacle.</em></p>
```

### Kinking

A grain loaded parallel to its basal planes has no resolved shear stress on them, so it cannot slip at all at first. A small bending of the planes tilts some of them toward easy slip, and the tilt runs away: inside a narrow band the planes rotate sharply and slip, while the rest of the grain barely moves. The kink band's edges are walls of basal edge dislocations of opposite sign, and the lattice inside is rotated by tens of degrees. Kinking lets otherwise hard grains shorten, and the strongly rotated bands become favored sites for new grains during recrystallization.

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/kink-band.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/kink-band.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>A kink band forms in a grain compressed parallel to its basal planes.</em></p>
```

## How a polycrystal flows

### Dislocation creep

In a polycrystal the processes above act together. Grains with basal planes near 45° to the load slip readily, while grains oriented with basal planes near parallel or perpendicular to it barely slip and are squeezed by their neighbors. Climb and recovery keep the dislocation density in balance. The bulk strain rate rises steeply with stress, as $\tau^n$ with $n\approx4$ in the experiments of {cite}`goldsby2001`, and it does not depend on grain size. This is the regime that Glen's law, with $n=3$, approximates. Two signatures distinguish it from the grain-size-sensitive mechanisms below. The grains change shape along with the sample, and their lattices rotate, building up a fabric. Dislocation creep dominates at stresses above about 0.1 MPa: in shear margins, in the fast trunks of ice streams, and in the lower parts of most glaciers. Its activation energy is about 60 kJ/mol below $-10\ \mathrm{^\circ C}$ and roughly three times larger close to the melting point, the same rise that appears in the rate factor of {doc}`ice-rheology`.

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/dislocation-creep.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/dislocation-creep.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Dislocation creep of a polycrystal under vertical compression; flashes mark active slip in soft grains.</em></p>
```

### Grain-boundary sliding

At lower stresses and in finer-grained ice, the grains themselves move as nearly rigid blocks, sliding along their boundaries and exchanging neighbors. The animation follows the Ashby–Verrall grain-switching geometry {cite}`ashby1973`: the sample extends by about seventy percent while every grain keeps its size and roughly equiaxed shape. A line scribed across the sample breaks into offset pieces, the classic experimental evidence for boundary sliding. Sliding cannot proceed alone. The grain corners and boundary ledges it pushes against must be relieved by basal slip near the boundaries, so the two operate in series and the slower one controls the pair. {cite}`goldsby2001` found that in this superplastic regime $n\approx1.8$ and the rate scales with grain size as $d^{-1.4}$, so finer ice is softer. They argued that grain-boundary sliding is the rate-limiting process at the low stresses of ice-sheet interiors. If so, the effective exponent there is below 3 and the viscosity depends on grain size, both of which matter for the age–depth relations of ice cores and for the shape of ice divides.

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/grain-boundary-sliding.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/grain-boundary-sliding.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Grain-boundary sliding and neighbor switching; boundaries brighten where sliding is fastest.</em></p>
```

### Diffusion creep: Nabarro–Herring

At the lowest stresses a polycrystal can deform with no dislocations at all, by moving individual molecules. Boundaries under compression have a slightly higher chemical potential than boundaries under relative tension. Molecules therefore diffuse from the squeezed faces of each grain to its tensile faces, and vacancies diffuse the other way. When the path runs through the grain interiors this is Nabarro–Herring creep. The strain rate is linear in stress ($n=1$, Newtonian) and scales as $D_v/d^2$, where $D_v$ is the lattice self-diffusivity, because a coarser grain means a longer path and a smaller driving gradient. The animation highlights the diagnostic feature: each grain lengthens, but its basal planes do not rotate, so diffusion creep produces no fabric. To keep the grains fitting together, some boundary sliding has to accompany it. Ice grains in glaciers are millimetres across, which makes diffusion creep far slower than the alternatives except in very fine-grained ice at very low stress.

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/nabarro-herring-creep.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/nabarro-herring-creep.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Nabarro–Herring creep: molecules diffuse through the grains from compressed to tensile boundaries.</em></p>
```

### Diffusion creep: Coble

Grain boundaries are disordered layers about a nanometre thick, and molecules diffuse along them much faster than through the lattice. When the boundaries carry the flux, the mechanism is Coble creep. The shape change is the same as before, and the stress dependence is still linear. Because the pathway's cross-section is the boundary width $\delta$ rather than the grain, the rate scales as $\delta D_b/d^3$. Halving the grain size makes Coble creep eight times faster, compared with four times for Nabarro–Herring creep. Coble creep therefore takes over in the finest grains and at the lowest temperatures, where boundary diffusion, with its lower activation energy, gains most on lattice diffusion. In terrestrial ice both diffusion mechanisms are mainly of interest at the grain-size and stress extremes, and in the fine-grained ice shells of icy moons.

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/coble-creep.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/coble-creep.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Coble creep: the same shape change, with molecules travelling along the grain boundaries.</em></p>
```

## How the grains evolve

### Lattice rotation and fabric

Slip on a single family of planes cannot leave a grain's orientation unchanged. As each grain shears on its basal planes, its lattice rotates: under compression the c-axes swing toward the compression axis, and under extension they spread away from the extension axis into a girdle. The animation pairs a thin section with a Schmidt diagram, an equal-area projection on which each dot is one c-axis and the center is vertical. Under vertical compression the dots crowd toward the center and the largest eigenvalue of the orientation tensor climbs from one third toward one. This is the fabric development described quantitatively in {doc}`ice-fabric`, and it is the starting point that the recrystallization processes below modify.

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/fabric-development.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/fabric-development.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Lattice rotation builds a single-maximum fabric under vertical compression.</em></p>
```

### Polygonization (rotation recrystallization)

Uneven slip bends grains, and a bent lattice is held in shape by excess dislocations of one sign scattered through it. Those dislocations lower their energy by gliding and climbing into walls, where their stress fields partly cancel. Between the walls the basal planes straighten, and the grain becomes a set of slightly misoriented sub-grains. As deformation feeds more dislocations into the walls, the misorientation across them grows. Beyond roughly 10 to 15° a wall behaves as an ordinary grain boundary and the old grain has become several new ones. Polygonization keeps grains from coarsening indefinitely and gives new grains orientations close to their parents, so it slightly broadens the fabric. It is the characteristic process in the middle depths of polar ice cores, where the mean grain size levels off {cite}`faria2014`.

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/polygonization.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/polygonization.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Polygonization: dislocations gather into walls that divide a bent grain into sub-grains, then new grains.</em></p>
```

### Migration recrystallization

In warm ice, above about $-10\ \mathrm{^\circ C}$, grain boundaries become mobile enough to move in response to differences in stored strain energy. A grain well oriented for basal slip recovers and stays relatively clean. A badly oriented neighbor keeps accumulating dislocations. The boundary between them bulges into the dirtier grain, and every region it sweeps becomes strain-free crystal with the clean grain's orientation. The animation (a Monte Carlo grain model, with darker shading for more stored energy) shows the survivors taking over and the orientation histogram shifting toward the soft orientations. The microstructure that results, large interlocking grains with lobate boundaries and a fabric tuned to the local stress, is typical of the warm basal ice of ice sheets, of temperate glaciers, and of shear margins. It is the main reason that tertiary creep is faster than the secondary minimum described by Glen's law.

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/migration-recrystallization.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/migration-recrystallization.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Strain-induced boundary migration: clean, well-oriented grains consume deformed neighbors.</em></p>
```

### Nucleation of new grains

When stored energy is high enough, entirely new strain-free grains appear at the most deformed sites: along old boundaries, at triple junctions, and in kink bands. Their orientations are typically well suited to basal slip under the current stress rather than inherited from the parent. Driven by the stored energy of the deformed matrix, they grow quickly, first as a necklace outlining the old grains and then consuming them. Nucleation resets the grain size and, because the new grains are soft, weakens the ice. In laboratory tests it drives the acceleration from secondary to tertiary creep shown in the creep curve of {doc}`ice-rheology`.

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/nucleation-recrystallization.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/nucleation-recrystallization.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Discontinuous recrystallization: strain-free nuclei appear at old boundaries and grow.</em></p>
```

### Normal grain growth

Even without deformation, a polycrystal is not at equilibrium, because grain boundaries carry energy. Curved boundaries migrate toward their centers of curvature. Small grains with few neighbors shrink and vanish, and their neighbors absorb the area. The mean grain area grows in proportion to time, $d^2-d_0^2=Kt$, with $K$ thermally activated. This is the slow coarsening seen in firn and in the upper few hundred metres of polar ice sheets, where grain size increases steadily with age until polygonization caps it. Because it is slow and temperature dependent, grain size in the upper part of an ice core is a rough record of both age and past temperature. Normal grain growth is not itself a deformation mechanism. Through the grain-size dependence of sliding and diffusion creep, however, it controls how soft the ice is in exactly the low-stress regime where those mechanisms matter.

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/grain-growth.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/grain-growth.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Normal grain growth driven by boundary energy alone; mean grain area grows linearly in time.</em></p>
```

## At the edges of the ductile regime

### Premelting and intergranular water

Within a degree or so of the melting point, grain boundaries do not stay dry. Interfacial premelting and dissolved impurities stabilize thin liquid films along the boundaries, and veins of water open where three grains meet, forming a connected network through temperate ice {cite}`nye1973,dash2006`. Wet boundaries slide more easily, and molecules diffuse much faster through the liquid. The rate factor responds strongly: {cite}`duval1977` found that the creep rate roughly triples as the water content rises from zero to about one percent. Together with the rise in activation energy above $-10\ \mathrm{^\circ C}$, this is why temperate ice and the warm basal layers of polar ice sheets are much softer than ice only a few degrees colder, and why shear concentrates near the bed.

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/premelting.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/premelting.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Liquid films and veins develop as ice warms toward its melting point, easing boundary sliding.</em></p>
```

### Brittle failure

Every mechanism above relaxes stress by flow. If the load rises faster than creep can relax it, stress concentrates at grain boundaries and the ice cracks instead. In compression, boundaries inclined to the load slide frictionally and open. Wing cracks grow from their tips parallel to the compression, and the cracks interact and link into a fault. The ductile-to-brittle transition in laboratory ice at $-10\ \mathrm{^\circ C}$ lies near strain rates of $10^{-7}\ \mathrm{s^{-1}}$ in tension and about $10^{-4}$ to $10^{-3}\ \mathrm{s^{-1}}$ in compression, and it shifts with grain size, temperature, and confinement. The tensile strength is about 1 MPa and the fracture toughness about $0.1\ \mathrm{MPa\,m^{1/2}}$ {cite}`schulson2001`. Glaciers mostly creep, but crevasses, rifts, calving, hydrofracture, and icequakes are all this mechanism at work.

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/brittle-fracture.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/brittle-fracture.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Brittle failure in compression: boundary cracks, wing cracks, and a through-going fault.</em></p>
```

## From mechanisms to a flow law

The mechanisms are not alternatives that a glacier chooses between. They operate together, in parallel and in series, as the composite law of {doc}`ice-rheology` expresses: independent mechanisms add their strain rates, and coupled ones, such as basal slip and boundary sliding, are limited by the slower partner. Microstructure ties them together over time. Lattice rotation and migration recrystallization build the fabrics of {doc}`ice-fabric`. Polygonization, nucleation, and normal grain growth set the grain size, which decides how fast boundary sliding and diffusion can go. Premelting softens everything near the melting point. Glen's law with $n=3$ and a temperature-dependent $A$, multiplied by an enhancement factor, is a practical average over this machinery. Knowing the machinery tells a modeler when that average can be trusted and in which direction it fails: toward $n<3$ and grain-size dependence at low stress, toward strong anisotropy where fabrics are well developed, and toward fracture where the ice is loaded quickly.
