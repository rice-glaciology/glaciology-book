# Deformation mechanisms of ice

Ice deforms by a family of distinct mechanisms. Some move molecules, some move defects within the crystal, some move whole grains, and some change the grains themselves. 
Each has its own dependence on macroscopic state variables like stress, temperature, and grain size.

Each mechanism below comes with a figure of its key stages and an animation of the . Both are schematic: strains are exaggerated, timescales are compressed by many orders of magnitude, and the three-dimensional crystal is reduced to a two-dimensional section. Each is drawn to show the one thing that distinguishes its mechanism from the others. In the grain-scale figures and videos each grain is colored by its c-axis orientation, in the bands of the colour bar beside it, and thin lines inside each grain trace its basal planes. Red marks the feature to watch: a dislocation core, active slip, a sliding boundary, or a crack. The rate laws and the conditions under which each mechanism matters are in the text and in the table below. The code that generates them is in `_dev/deformation_mechanisms/` and can be rerun or modified.

## An overview

The mechanisms sort naturally into four groups. The first group describe deformation within a single crystal: elastic stretching of bonds, and dislocation glide, climb, and kinking of dislocations. 
The second group describe deformation accommodated by polycrystalline ice and include dislocation creep, grain-boundary sliding, and two forms of diffusion creep. 
The third group describes how the grains themselves evolve during and after deformation, through lattice rotation, polygonization, migration recrystallization, nucleation, and normal grain growth.
These processes change the microstructure, affect the rate factor and drive fabric development. 
The fourth group describes how premelting near the melting point and brittle fracture at high strain rates affect deformation.

| Mechanism | Deformation | Stress exponent $n$ | Grain-size exponent $p$ | Process |
|---|---|---|---|---|
| Elasticity | bond lengths and angles | (linear, recoverable) | 0 | seismic waves, tides, first instants of loading |
| Basal dislocation glide | dislocations in basal planes | (carrier of most strain) | 0 | all creeping ice |
| Non-basal glide | dislocations on prismatic and pyramidal planes | high | 0 | hard grains only |
| Dislocation creep | glide plus climb in a polycrystal | ~4 | 0 | high stress: shear margins, ice streams, lab tests |
| Grain-boundary sliding | whole grains, accommodated by basal slip | ~1.8 | ~1.4 | low stress, fine grains: ice-sheet interiors |
| Nabarro–Herring creep | molecules through the lattice | 1 | 2 | very fine grains, very low stress |
| Coble creep | molecules along grain boundaries | 1 | 3 | very fine, cold grains |

For each mechanism, the strain rate scales as $\dot\varepsilon \propto \tau^n d^{-p} \exp(-Q/RT)$. Not all deformation mechanisms affect the relationship between strainrate and effective stress that we often link to ice-rheology. For instance, the microstructural processes of the third group set the grain size $d$ and the fabric that the flow laws above respond to.

{numref}`fig-mechanism-map` shows where the rate-controlling mechanisms dominate at $-10\ \mathrm{^\circ C}$, using the composite law of {cite}`goldsby2001` introduced in {doc}`ice-rheology`. A map of this kind follows the approach of {cite}`frost1982`. Glacier ice, with grains of millimetres and stresses of tens to hundreds of kilopascals, straddles the boundary between grain-boundary sliding and dislocation creep. That is the microphysical reason the effective exponent $n\approx3$ sits between the two.

```{figure} figures/deformation-mechanism-map.png
:name: fig-mechanism-map
:width: 85%

Deformation-mechanism map for ice at $-10\ \mathrm{^\circ C}$, computed from the composite flow law of {cite}`goldsby2001`. Shading marks the mechanism contributing most to the strain rate; dashed lines are contours of total strain rate. In the grain-boundary-sliding field, sliding is the slower, rate-limiting member of the sliding and basal-slip pair. Basal slip would become the limiting member only for grains of a few to tens of microns, where diffusion creep is faster still, so no basal-slip-limited field appears. Diffusion-creep parameters are approximate, so the position of that field is indicative only. Boxes show typical conditions in ice-sheet interiors and in shear margins.
```

## Inside the crystal

### Elastic deformation

Under any applied stress, the first response of ice is elastic. The bonds between water molecules stretch, compress, and bend slightly, but every molecule keeps the same neighbors. The strain is proportional to the stress, with a Young's modulus near 9 GPa, and the deformation of the lattice is recoverable. At glacier stresses the elastic strain is only about $10^{-5}$, so it matters only on short timescales: seismic waves, the tidal flexing of ice shelves, and the first instant of any loading. Over hours to days, the Maxwell time of {doc}`ice-rheology`, viscous creep overtakes it. Because no molecules ever change position in the lattices, elasticity alone can never produce flow.

```{figure} figures/mechanism-elastic.png
:name: fig-mechanism-elastic
:width: 100%

Elastic deformation of an ice crystal under shear, with the stress–strain path beside each stage. (A) Unloaded; each row of molecules is a basal plane. (B) Under load every bond stretches (red) or compresses (blue) and the crystal shears uniformly; the strain is exaggerated about ten-thousand-fold. (C) Unloading retraces the same straight line. (D) The crystal recovers its exact shape; no molecule has changed neighbours.
```

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/elastic.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/elastic.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Elastic deformation: bonds stretch and recover; nothing flows.</em></p>
```

### Basal slip by dislocation glide

Permanent deformation of a crystal requires defects to move. The most common defects are dislocations, lines along which the lattice is offset by one Burgers vector $b$ (introduced in {doc}`ice-rheology`). In the animation an edge dislocation, the end of an extra half-plane of molecules, nucleates at one surface of the crystal and glides along a basal plane. Only the bonds adjecent to the dislocation are broken and remade at any instant, which is why dislocation glide requires far less stress than shearing a whole plane at once. When the dislocation leaves the far surface, the upper half of the crystal has moved one molecular spacing and a step appears on each face. In a real ice sample, there are hundreds of dislocations and the total strainrate $\dot\varepsilon=\rho_d b v$ is the sum over a dislocation density $\rho_d$ moving at speed $v$. In ice, $v$ is limited by how fast Bjerrum defects can reorder the protons ahead of the region of a dislocation (which we also call the core). This sets the activation energy of about 0.6 eV {cite}`fletcher1970`. Deformation associated with crystal glide shears like a deck of cards, easily parallel to its basal planes.

```{figure} figures/mechanism-basal-glide.png
:name: fig-mechanism-basal-glide
:width: 100%

Basal slip by dislocation glide. (A) A crystal under shear stress parallel to its basal planes. (B) An edge dislocation (red), the end of an extra half-plane, glides along a basal plane, breaking and remaking only the bonds at its core. (C) When it leaves the crystal, the upper half has moved one molecular spacing and a step appears on each face. (D) After three dislocations the crystal has sheared, like a deck of cards (inset).
```

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/basal-glide.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/basal-glide.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Basal slip: edge dislocations glide through the crystal, each leaving a one-molecule step.</em></p>
```

### Non-basal slip

The same stress applied to a crystal whose basal planes are perpendicular to the shear has to drive dislocations across the basal planes instead of along them, on prismatic or pyramidal planes. The resolved shear stress needed is roughly sixty times larger. The animation shows the reason in geometric form: relative to the Burgers vector, the non-basal planes are closely spaced, so the dislocation core is wide and the lattice grips it hard. The consequence for a polycrystal is fundamental. A general change of grain shape needs five independent slip systems (the von Mises criterion), and basal slip supplies only two. A grain in an aggregate therefore cannot simply deform the way its neighbors require. Something else must accommodate the mismatch: the hard systems, climb, boundary sliding, or recrystallization. Grains that depend on non-basal slip, such as those with c-axes along the compression axis in a strong fabric, are the hard grains of an aggregate.

```{figure} figures/mechanism-nonbasal-glide.png
:name: fig-mechanism-nonbasal-glide
:width: 100%

Basal and prismatic slip under the same horizontal shear stress. In each panel the left crystal has its basal planes horizontal and the right crystal has them vertical, so its dislocation must glide on a prismatic plane. (A) Both crystals loaded. (B) The basal dislocation glides freely. (C) A second basal dislocation has crossed while the prismatic one has barely moved. (D) Three basal passes against one partial prismatic pass; prismatic slip needs roughly sixty times the stress.
```

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/nonbasal-glide.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/nonbasal-glide.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Basal versus prismatic slip under the same shear stress.</em></p>
```

### Dislocation climb and recovery

A gliding dislocation that meets an obstacle, an impurity or a tangle of other dislocations, stops. An edge dislocation can escape by climbing out of its glide plane, and climb requires diffusion. In the animation a vacancy wanders through the lattice, reaches the edge of the extra half-plane, and absorbs its last molecule. The half-plane is now one molecule shorter, so the dislocation sits on the next basal plane up and glides on past the obstacle. Climb also lets dislocations of opposite sign meet and annihilate. This is recovery, and it is why ice hardly work-hardens: once glide and climb balance, creep proceeds at a steady rate (see {doc}`ice-rheology`). Because climb is fed by lattice self-diffusion ({doc}`../foundations/point-defects`), it is thermally activated and is part of what sets the stress dependence of dislocation creep.

```{figure} figures/mechanism-dislocation-climb.png
:name: fig-mechanism-dislocation-climb
:width: 100%

Dislocation climb and recovery. (A) A gliding dislocation (red) is held at an obstacle (dark molecules). (B) A vacancy (dashed) diffuses toward it as neighbouring molecules hop into it. (C) The vacancy absorbs the last molecule of the extra half-plane, and the dislocation climbs one basal plane. (D) Free of the obstacle, it glides on.
```

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/dislocation-climb.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/dislocation-climb.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Climb: a vacancy is absorbed, the dislocation steps up one plane and bypasses the obstacle.</em></p>
```

### Kinking

A grain loaded parallel to its basal planes has no resolved shear stress on them, so it cannot slip at all at first. A small bending of the planes tilts some of them toward easy slip, and the tilt runs away: inside a narrow band the planes rotate sharply and slip, while the rest of the grain barely moves. The kink band's edges are walls of basal edge dislocations of opposite sign, and the lattice inside is rotated by tens of degrees. Kinking lets otherwise hard grains shorten, and the strongly rotated bands become favored sites for new grains during recrystallization.

```{figure} figures/mechanism-kink-band.png
:name: fig-mechanism-kink-band
:width: 100%

Kinking of a grain compressed parallel to its basal planes. (A) The basal planes (lines) carry no resolved shear stress. (B) A slight bowing tilts some planes toward easy slip. (C) Inside a band the planes rotate sharply and slip, while the rest of the grain stays put. (D) The rotated band is bounded by walls of edge dislocations of opposite sign; its lattice rotation is given below the grain. Colours show c-axis orientation.
```

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

```{figure} figures/mechanism-dislocation-creep.png
:name: fig-mechanism-dislocation-creep
:width: 100%

Dislocation creep of a polycrystal under vertical compression. Colours show c-axis orientation and thin lines the basal planes. (A) The undeformed aggregate. (B) Grains with basal planes near 45° to the load slip readily (red marks active slip); hard grains barely slip. (C) Grains flatten with the sample and their lattices rotate. (D) After 32% shortening the c-axes have swung toward the compression axis.
```

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/dislocation-creep.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/dislocation-creep.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Dislocation creep of a polycrystal under vertical compression; flashes mark active slip in soft grains.</em></p>
```

### Grain-boundary sliding

At lower stresses and in finer-grained ice, the grains themselves move as nearly rigid blocks, sliding along their boundaries and exchanging neighbors. The animation follows the Ashby–Verrall grain-switching geometry {cite}`ashby1973`: the sample extends by about seventy percent while every grain keeps its size and roughly equiaxed shape. A line scribed across the sample breaks into offset pieces, the classic experimental evidence for boundary sliding. Sliding cannot proceed alone. The grain corners and boundary ledges it pushes against must be relieved by basal slip near the boundaries, so the two operate in series and the slower one controls the pair. {cite}`goldsby2001` found that in this superplastic regime $n\approx1.8$ and the rate scales with grain size as $d^{-1.4}$, so finer ice is softer. They argued that grain-boundary sliding is the rate-limiting process at the low stresses of ice-sheet interiors. If so, the effective exponent there is below 3 and the viscosity depends on grain size, both of which matter for the age–depth relations of ice cores and for the shape of ice divides.

```{figure} figures/mechanism-grain-boundary-sliding.png
:name: fig-mechanism-grain-boundary-sliding
:width: 100%

Grain-boundary sliding with neighbour switching (after {cite}`ashby1973`) under horizontal extension. (A) Fine-grained ice with a scribed marker line (green). (B) Grains move as nearly rigid blocks; boundaries are red where they slide fastest. (C) Neighbouring rows switch neighbours. (D) After 73% extension every grain keeps its size and shape, and the marker line is offset at the boundaries.
```

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/grain-boundary-sliding.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/grain-boundary-sliding.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Grain-boundary sliding and neighbor switching; boundaries brighten where sliding is fastest.</em></p>
```

### Diffusion creep: Nabarro–Herring

At the lowest stresses a polycrystal can deform with no dislocations at all, by moving individual molecules. Boundaries under compression have a slightly higher chemical potential than boundaries under relative tension. Molecules therefore diffuse from the squeezed faces of each grain to its tensile faces, and vacancies diffuse the other way. When the path runs through the grain interiors this is Nabarro–Herring creep. The strain rate is linear in stress ($n=1$, Newtonian) and scales as $D_v/d^2$, where $D_v$ is the lattice self-diffusivity, because a coarser grain means a longer path and a smaller driving gradient. The animation highlights the diagnostic feature: each grain lengthens, but its basal planes do not rotate, so diffusion creep produces no fabric. To keep the grains fitting together, some boundary sliding has to accompany it. Ice grains in glaciers are millimetres across, which makes diffusion creep far slower than the alternatives except in very fine-grained ice at very low stress.

```{figure} figures/mechanism-nabarro-herring-creep.png
:name: fig-mechanism-nabarro-herring-creep
:width: 100%

Nabarro–Herring creep under vertical compression. Boundaries normal to the load are squeezed (red) and those parallel to it are in relative tension (blue). (A) The loaded grains. (B, C) Molecules (green) diffuse through the grain interiors from squeezed to tensile boundaries, and each grain lengthens. (D) The final shape; the basal-plane traces have not rotated, so no fabric forms.
```

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/nabarro-herring-creep.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/nabarro-herring-creep.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Nabarro–Herring creep: molecules diffuse through the grains from compressed to tensile boundaries.</em></p>
```

### Diffusion creep: Coble

Grain boundaries are disordered layers about a nanometre thick, and molecules diffuse along them much faster than through the lattice. When the boundaries carry the flux, the mechanism is Coble creep. The shape change is the same as before, and the stress dependence is still linear. Because the pathway's cross-section is the boundary width $\delta$ rather than the grain, the rate scales as $\delta D_b/d^3$. Halving the grain size makes Coble creep eight times faster, compared with four times for Nabarro–Herring creep. Coble creep therefore takes over in the finest grains and at the lowest temperatures, where boundary diffusion, with its lower activation energy, gains most on lattice diffusion. In terrestrial ice both diffusion mechanisms are mainly of interest at the grain-size and stress extremes, and in the fine-grained ice shells of icy moons.

```{figure} figures/mechanism-coble-creep.png
:name: fig-mechanism-coble-creep
:width: 100%

Coble creep under vertical compression, drawn as in the Nabarro–Herring figure. (A) The loaded grains. (B, C) Molecules (green) diffuse along the grain boundaries rather than through the grains. (D) The same shape change, with the lattices unrotated; the rate scales as $1/d^3$ instead of $1/d^2$.
```

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

```{figure} figures/mechanism-fabric-development.png
:name: fig-mechanism-fabric-development
:width: 100%

Lattice rotation and fabric development under vertical compression. Each panel shows a thin section (left; colours are c-axis orientations) and the c-axes of 500 grains on a lower-hemisphere equal-area Schmidt diagram with the vertical at its centre (right). (A) A random fabric, $a_1\approx1/3$. (B, C) Basal slip rotates the c-axes toward the vertical. (D) A single maximum; $a_1$ is the largest eigenvalue of the orientation tensor.
```

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/fabric-development.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/fabric-development.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Lattice rotation builds a single-maximum fabric under vertical compression.</em></p>
```

### Polygonization (rotation recrystallization)

Uneven slip bends grains, and a bent lattice is held in shape by excess dislocations of one sign scattered through it. Those dislocations lower their energy by gliding and climbing into walls, where their stress fields partly cancel. Between the walls the basal planes straighten, and the grain becomes a set of slightly misoriented sub-grains. As deformation feeds more dislocations into the walls, the misorientation across them grows. Beyond roughly 10 to 15° a wall behaves as an ordinary grain boundary and the old grain has become several new ones. Polygonization keeps grains from coarsening indefinitely and gives new grains orientations close to their parents, so it slightly broadens the fabric. It is the characteristic process in the middle depths of polar ice cores, where the mean grain size levels off {cite}`faria2014`.

```{figure} figures/mechanism-polygonization.png
:name: fig-mechanism-polygonization
:width: 100%

Polygonization (rotation recrystallization) of a bent grain. (A) Basal planes curved by excess dislocations of one sign (red). (B) The dislocations glide along and climb across the basal planes. (C) They gather into walls, and between the walls the planes straighten into slightly misoriented sub-grains. (D) More dislocations join the walls until the misorientation passes 10 to 15° and the walls are grain boundaries. Colours exaggerate the small orientation differences.
```

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/polygonization.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/polygonization.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Polygonization: dislocations gather into walls that divide a bent grain into sub-grains, then new grains.</em></p>
```

### Migration recrystallization

In warm ice, above about $-10\ \mathrm{^\circ C}$, grain boundaries become mobile enough to move in response to differences in stored strain energy. A grain well oriented for basal slip recovers and stays relatively clean. A badly oriented neighbor keeps accumulating dislocations. The boundary between them bulges into the dirtier grain, and every region it sweeps becomes strain-free crystal with the clean grain's orientation. The animation (a Monte Carlo grain model, with darker shading for more stored energy) shows the survivors taking over and the orientation histogram shifting toward the soft orientations. The microstructure that results, large interlocking grains with lobate boundaries and a fabric tuned to the local stress, is typical of the warm basal ice of ice sheets, of temperate glaciers, and of shear margins. It is the main reason that tertiary creep is faster than the secondary minimum described by Glen's law.

```{figure} figures/mechanism-migration-recrystallization.png
:name: fig-mechanism-migration-recrystallization
:width: 100%

Migration recrystallization under vertical compression, from a Monte Carlo grain model. Darker grains hold more stored strain energy; the histogram gives the area fraction of each c-axis angle from the compression axis. (A) Deformed warm ice. (B) Clean grains well oriented for basal slip bulge into deformed neighbours. (C) Swept regions become strain-free crystal of the growing grain. (D) The survivors cluster near 45° to the load, the orientation softest for basal slip.
```

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/migration-recrystallization.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/migration-recrystallization.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Strain-induced boundary migration: clean, well-oriented grains consume deformed neighbors.</em></p>
```

### Nucleation of new grains

When stored energy is high enough, entirely new strain-free grains appear at the most deformed sites: along old boundaries, at triple junctions, and in kink bands. Their orientations are typically well suited to basal slip under the current stress rather than inherited from the parent. Driven by the stored energy of the deformed matrix, they grow quickly, first as a necklace outlining the old grains and then consuming them. Nucleation resets the grain size and, because the new grains are soft, weakens the ice. In laboratory tests it drives the acceleration from secondary to tertiary creep shown in the creep curve of {doc}`ice-rheology`.

```{figure} figures/mechanism-nucleation-recrystallization.png
:name: fig-mechanism-nucleation-recrystallization
:width: 100%

Nucleation of new grains (discontinuous recrystallization), drawn as in the migration figure. (A) Heavily deformed ice. (B) Strain-free nuclei form along the old boundaries. (C) A necklace of new grains outlines the old ones. (D) The new grains, mostly oriented for easy basal slip, have consumed the deformed matrix.
```

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/nucleation-recrystallization.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/nucleation-recrystallization.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Discontinuous recrystallization: strain-free nuclei appear at old boundaries and grow.</em></p>
```

### Normal grain growth

Even without deformation, a polycrystal is not at equilibrium, because grain boundaries carry energy. Curved boundaries migrate toward their centers of curvature. Small grains with few neighbors shrink and vanish, and their neighbors absorb the area. The mean grain area grows in proportion to time, $d^2-d_0^2=Kt$, with $K$ thermally activated. This is the slow coarsening seen in firn and in the upper few hundred metres of polar ice sheets, where grain size increases steadily with age until polygonization caps it. Because it is slow and temperature dependent, grain size in the upper part of an ice core is a rough record of both age and past temperature. Normal grain growth is not itself a deformation mechanism. Through the grain-size dependence of sliding and diffusion creep, however, it controls how soft the ice is in exactly the low-stress regime where those mechanisms matter.

```{figure} figures/mechanism-grain-growth.png
:name: fig-mechanism-grain-growth
:width: 100%

Normal grain growth driven by grain-boundary energy alone, from a Monte Carlo grain model. (A) A fine-grained aggregate. (B, C) Curved boundaries migrate toward their centres of curvature; small grains shrink and vanish. (D) The mean grain area (right) grows linearly with time, $d^2-d_0^2=Kt$.
```

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

```{figure} figures/mechanism-premelting.png
:name: fig-mechanism-premelting
:width: 100%

Premelting and intergranular water near the melting point. (A) Cold ice with dry boundaries. (B) On warming, liquid films (blue) thicken along the boundaries and veins open at three-grain junctions. (C) Under shear the wet boundaries slide easily, and the marker line (green) breaks at the boundaries. (D) The aggregate has sheared by sliding on its wet boundaries; the readouts give the temperature and the strain rate relative to dry ice.
```

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/premelting.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/premelting.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Liquid films and veins develop as ice warms toward its melting point, easing boundary sliding.</em></p>
```

### Brittle failure

Every mechanism above relaxes stress by flow. If the load rises faster than creep can relax it, stress concentrates at grain boundaries and the ice cracks instead. In compression, boundaries inclined to the load slide frictionally and open. Wing cracks grow from their tips parallel to the compression, and the cracks interact and link into a fault. The ductile-to-brittle transition in laboratory ice at $-10\ \mathrm{^\circ C}$ lies near strain rates of $10^{-7}\ \mathrm{s^{-1}}$ in tension and about $10^{-4}$ to $10^{-3}\ \mathrm{s^{-1}}$ in compression, and it shifts with grain size, temperature, and confinement. The tensile strength is about 1 MPa and the fracture toughness about $0.1\ \mathrm{MPa\,m^{1/2}}$ {cite}`schulson2001`. Glaciers mostly creep, but crevasses, rifts, calving, hydrofracture, and icequakes are all this mechanism at work.

```{figure} figures/mechanism-brittle-fracture.png
:name: fig-mechanism-brittle-fracture
:width: 100%

Brittle failure of rapidly compressed ice. (A) Loading faster than creep can relax the stress. (B) Boundaries inclined to the load slide and crack open (black). (C) Wing cracks grow from their tips parallel to the compression and link up. (D) A through-going fault (red) forms and the two halves slide apart.
```

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/brittle-fracture.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/brittle-fracture.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Brittle failure in compression: boundary cracks, wing cracks, and a through-going fault.</em></p>
```

## Fabrics in polar ice sheets: putting the mechanisms in place

{cite}`alley1988` combined these mechanisms into a single prediction of the c-axis fabric anywhere in an ice sheet. His model treats basal glide as the carrier of strain. Each grain strains in proportion to its geometric factor $S=\cos\phi\sin\phi$, where $\phi$ is the angle between its c-axis and the stress axis, and the grain strains average to the bulk strain. A grain that slips on its basal plane must rotate, toward a compression axis and away from a tension axis, at a rate that follows from $S$. For an increment of uniaxial strain $\Delta\varepsilon$ (negative in compression),

$$
\Delta\phi = \frac{\Delta\varepsilon\,\sin^2\phi}{\bar S}\quad\text{(compression)},\qquad
\Delta\phi = \frac{\Delta\varepsilon\,\cos^2\phi}{\bar S + S\,\Delta\varepsilon}\quad\text{(tension)},
$$

where $\bar S$, the mean of $S$ over the grains, is the geometric softness of the aggregate. Pure shear is a uniaxial compression superposed on an equal uniaxial tension, and simple shear adds a rigid-body rotation. With these rules the fabric records the cumulative strain and the stress state.

The first animation repeats his Figs. 1 and 2 with the model written in `_dev/deformation_mechanisms/alley1988.py`. Divergent flow, in which transverse extension makes the flow a uniaxial vertical compression, clusters the c-axes about the vertical, passing through a small-circle girdle at intermediate strain. This is the fabric of Dome C, Byrd Station, Camp Century, and Dye 3. Parallel flow, a pure shear, gives an elongated cluster. Convergent flow, a uniaxial longitudinal extension, gathers the c-axes into a vertical plane transverse to the flow, as at Mizuho and Vostok. The geometric softness first rises, because the median c-axis of a random fabric lies at 60° and rotates toward the 45° of maximum resolved shear, and then falls as the fabric tightens beyond it.

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/alley-flow-regimes.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/alley-flow-regimes.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>Alley's rotation model under the three flow patterns of an ice sheet, with the geometric softness against strain.</em></p>
```

Which mechanism controls the fabric changes with depth, and the second animation follows a parcel down a column like that at Byrd Station to show where each mechanism of this chapter takes over. In the cold upper ice, below about $-10\ \mathrm{^\circ C}$ and dominated by normal stresses, rotation by basal glide controls the fabric: the c-axes close in on the vertical while grains first grow and then stop growing as polygonization subdivides them. Near the bed, basal shear exceeds the normal stresses, and simple shear builds a strong single maximum in fine-grained ice with undulose extinction and kink bands. Where the basal ice is warmer than about $-10\ \mathrm{^\circ C}$ and strain rates are high, migration recrystallization and nucleation replace the rotation fabric with coarse, interlocking grains whose c-axes form a multiple-maximum small-circle girdle 25 to 30° from the vertical. Recrystallization is more rapid under normal stresses than under simple shear, because the mismatch between neighbouring grains and the hardening of the aggregate store more strain energy there, so the rotation predictions hold only where recrystallization has not yet taken over {cite}`alley1988`.

```{raw} html
<video controls width="100%" preload="metadata" poster="../../_static/videos/deformation/alley-ice-column.jpg" style="max-width: 860px;">
  <source src="../../_static/videos/deformation/alley-ice-column.mp4" type="video/mp4">
  Your browser does not support embedded video.
</video>
<p><em>A parcel descending through a Byrd-like column: (A) the depth zones, (B) its c-axis fabric, with recrystallized grains in red, and (C) its geometric softness for bed-parallel shear.</em></p>
```

The depths, temperatures, and strain path in the column are illustrative, chosen to resemble Byrd Station rather than fitted to it.

## From mechanisms to a flow law

The mechanisms are not alternatives that a glacier chooses between. They operate together, in parallel and in series, as the composite law of {doc}`ice-rheology` expresses: independent mechanisms add their strain rates, and coupled ones, such as basal slip and boundary sliding, are limited by the slower partner. Microstructure ties them together over time. Lattice rotation and migration recrystallization build the fabrics of {doc}`ice-fabric`. Polygonization, nucleation, and normal grain growth set the grain size, which decides how fast boundary sliding and diffusion can go. Premelting softens everything near the melting point. Glen's law with $n=3$ and a temperature-dependent $A$, multiplied by an enhancement factor, is a practical average over this machinery. Knowing the machinery tells a modeler when that average can be trusted and in which direction it fails: toward $n<3$ and grain-size dependence at low stress, toward strong anisotropy where fabrics are well developed, and toward fracture where the ice is loaded quickly.
