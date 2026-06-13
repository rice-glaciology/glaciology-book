# Glacial erosion

The fjords of Norway, the U-shaped valleys of the Alps, and the hills of Seattle were all cut by the processes in {doc}`../thermomechanics/basal-motion`, run for long enough. A sliding glacier is the most effective agent of erosion on Earth, and this chapter asks how the sliding actually removes rock, what sets the pace, and what the accumulated work does to landscapes and, through the bed, back to the ice. Chapter 13 of {cite}`cuffey2010` and the review by {cite}`hallet1996` anchor the quantitative material.

Around Puget Sound, a kilometer of Cordilleran ice covered the Seattle area as recently as 15,000 years ago, and the drumlins it streamlined are the hills the city is built on. East of the Cascades, the Channeled Scablands record catastrophic outburst floods from ice-dammed Glacial Lake Missoula, the same jökulhlaup physics treated in {doc}`../thermomechanics/hydrology` at a continental scale. Soils, aquifers, and the very shape of the region's waterways are glacial products that people live on without noticing.

## Abrasion and quarrying

Glaciers erode bedrock chiefly by two processes, and the division of labor between them is lopsided.

**Quarrying** removes blocks. Ice flowing over a bedrock bump concentrates normal stress on the up-flow (stoss) face and opens a water-filled cavity in the lee. The rock step between them carries a deviatoric stress set by the difference between ice pressure and cavity water pressure, and cracks in the lee corner grow when that difference is large. The counterintuitive part is the role of water pressure. High, steady water pressure protects the rock; what breaks it is the drop, when the cavity drains, the bridging stress on the step spikes, and cracks jump ahead. Erosion is fastest under glaciers with fast sliding, low effective pressure, and large water-pressure fluctuations, which is to say under big temperate glaciers with lively hydrology. The hypothesis has been tested directly at the Svartisen Subglacial Laboratory beneath Engabreen in Norway, where instruments at the bed under 210 meters of ice recorded bursts of acoustic emission, cracking, accompanying each drop in water pressure {cite}`cohen2006`. Quarrying is the dominant erosional process, faster than abrasion by an order of magnitude or more, and the asymmetry it leaves behind, smooth abraded stoss faces and steep plucked lee faces, is the signature of the roche moutonnée.

**Abrasion** files the surface. Rock fragments entrained in basal ice, frozen in through the frozen fringe of {doc}`../thermomechanics/frozen-ground`, are dragged across bedrock, carving the striations and polish that record flow direction long after the ice is gone. The force pressing a clast against the bed is not the weight of the overlying ice. A clast in regelating, creeping ice feels a contact force set by the viscous drag of ice moving past it, of order the Stokes drag

$$
F = 6\pi\,\eta\,R\,v_n,
$$

```{admonition} Derivation
:class: dropdown

This is the Stokes drag on a sphere moving slowly through a viscous fluid, applied here with the roles reversed: the ice creeps past a nearly stationary clast, and the drag is the contact force pressing the clast toward the bed. The result comes from solving the Stokes equations, the zero-Reynolds-number limit of the Navier–Stokes equations in which inertia is dropped,

$$
\nabla p = \eta\,\nabla^2 \mathbf{u},\qquad \nabla\!\cdot\!\mathbf{u}=0,
$$

for flow past a sphere of radius $R$ with the no-slip condition $\mathbf u = \mathbf 0$ on the sphere surface and uniform flow $\mathbf u \to v_n\,\hat{\mathbf n}$ far away. Integrating the resulting stress (pressure plus viscous) over the sphere surface gives a net force whose two contributions are the pressure drag $2\pi\eta R v_n$ and the viscous skin drag $4\pi\eta R v_n$, summing to

$$
F = 6\pi\,\eta\,R\,v_n.
$$

The linearity in $\eta$, $R$, and $v_n$ is the hallmark of the Stokes regime, where the force scales with the first power of velocity rather than its square. The use of this Newtonian result for ice, which is non-Newtonian, treats the ice in the immediate neighbourhood of the clast as a fluid of effective viscosity $\eta$ {cite}`hallet1979`; the linear scaling is the essential point, and the numerical prefactor follows from the spherical geometry.
```

with $\eta$ the ice viscosity, $R$ the clast radius, and $v_n$ the ice velocity component carrying the clast toward the bed. The numbers are startling. For $\eta \approx 3\times10^{12}$ Pa s, a half-meter boulder, and a modest meter per year of convergence, the contact force is about $10^6$ N, the weight of a hundred tons of rock pressing down a boulder that itself weighs less than one. This is why striations appear on vertical and even overhanging surfaces, where gravity could never press a tool against the rock. The abrasion rate then scales as

$$
\dot A = \alpha\, F_c\, v_p\, C,
$$

```{admonition} Derivation
:class: dropdown

This is the Hallet abrasion law {cite}`hallet1979`, and it is a dimensional-and-physical argument rather than a derived identity, so its origin is what matters. Consider a single clast pressed against the bed with contact force $F_c$ and dragged across it at speed $v_p$. The wear removed by a hard tool sliding under load is, to leading order, proportional both to how hard it presses and to how far it slides: doubling the load doubles the depth of the groove it cuts, and doubling the sliding distance doubles the length. The volume of rock removed per unit time by one clast is therefore proportional to the product $F_c\,v_p$, with a coefficient $\alpha$ that absorbs the hardness contrast between tool and bed and the geometry of the contact.

Many tools act at once. If $C$ is the number of clasts in contact per unit bed area, the volume removed per unit bed area per unit time, which is the abrasion rate $\dot A$ expressed as a lowering rate, is the single-clast rate times the areal concentration,

$$
\dot A = \alpha\,F_c\,v_p\,C.
$$

The energy reading in the main text follows directly: $\mu F_c$ is the friction force on one clast, $\mu F_c v_p$ is the frictional power it dissipates, and $\mu F_c v_p C$ is the frictional work per unit bed area per unit time, so the abrasion rate is proportional to the rate at which sliding does frictional work against the bed. Both $F_c$ (through the Stokes drag, $F_c\propto v_n$) and $v_p$ grow with sliding speed, which is why abrasion scales roughly as the square of the sliding velocity. The law is constrained against field and laboratory wear data, not deduced from first principles {cite}`hallet1979`.
```

with $F_c$ the contact force, $v_p$ the particle speed, $C$ the concentration of tools on the bed, and $\alpha$ a constant absorbing rock hardness {cite}`hallet1979`. Since both $F_c$ and $v_p$ grow with the sliding speed, abrasion goes roughly as the square of sliding, an energy statement, since $\mu F_c v_p C$ is the frictional work spent per unit bed area.

```{figure} figures/cross-cutting-striations.jpeg
:name: fig-striations
:width: 60%

Glacially polished bedrock with two cross-cutting sets of striations, compass for scale. The earlier set survived the episode that carved the later one, which is the field's quiet testimony that abrasion is slow, removing only millimetres of rock per century even under sliding ice.
```

% TODO Illustrator figure: figures/quarrying-abrasion.svg (label fig-quarrying-abrasion, width 90%)
% Spec: erosion at a roche moutonnee, ice sliding left to right. Stoss side, entrained clasts
% pressed by viscous drag abrade striations/polish; lee side, water-filled cavity, pressure drops
% load the rock step and drive crack growth (quarrying); cite hallet1979,cohen2006,iverson2012.

Quarrying supplies the tools that abrade, and abrasion smooths the bumps whose lee corners quarrying exploits. Subglacial streams then do most of the hauling, evacuating the majority of the sediment to the margin, and sliding by regelation adds a quiet chemical channel, dissolving minerals where ice melts on stoss faces and precipitating them in the lee, which is partly why glaciated bedrock shines.

## Rates and controls

Averaged over basins, glacial erosion rates scale with ice flux. Useful rules of thumb are $E \sim 10^{-4} U$ for sliding speed $U$ and $E \sim 10^{-3} S$ for snowfall input $S$, spanning fractions of a millimeter to centimeters per year, with the fastest rates under the fast, wet, maritime glaciers of regions like coastal Alaska {cite}`hallet1996`. The controls follow from the mechanics: no sliding, no erosion, so cold-based ice frozen to its bed protects the landscape beneath it rather than consuming it. A single ice sheet can therefore archive and erase simultaneously, preserving delicate pre-glacial surfaces under its frozen-bedded interior while gutting fjords beneath its wet-bedded outlets, and the juxtaposition is readable in the field wherever molded, striated rock sits beside ancient weathered surfaces, as on the nunataks of the Transantarctic Mountains.

At the largest scale the climate sets a ceiling on topography. Summit elevations across entire mountain belts track the snowline, the glacial buzzsaw, because rock lifted above the equilibrium-line altitude grows glaciers that cut it back down. Alpine forms reach sea level in the Lofoten Islands while the highest peaks on Earth stand where the ELA is highest, in the subtropics. Erosion also reaches back into ice dynamics on the longest timescales. The stripping of soft regolith from beneath the Laurentide ice sheet, exposing hard bedrock, is the leading explanation for the Mid-Pleistocene Transition in the glacial cycles {cite}`clark1998`, the same coupling of substrate to flow that today sorts ice streams from slow ice in {doc}`ice-sheets`.

The landforms all this work leaves behind are the field evidence from which vanished ice sheets are reconstructed, and reading them is the subject of {doc}`former-glaciers`.
