# Introduction to ice flow

One of the most surprising facts about ice is that, in large enough quantities, it **flows under its own weight**. This is not some exotic phase of ice — it is ordinary water ice, the same material you keep in your freezer. Hit it hard and it shatters; slip on it and it bruises like concrete. And yet, when enough of it piles up, gravity drives it to creep downhill like an extraordinarily slow, stiff fluid. A continental ice sheet kilometers thick can spread outward and discharge ice to the ocean at speeds ranging from centimeters to kilometers per year.

```{figure} figures/mer-de-glace-ogives.jpg
:name: fig-mer-de-glace
:width: 85%

Flow you can see. The Mer de Glace in the Mont Blanc massif, with two tributaries merging into a single trunk. The dark arcs sweeping across the glacier are ogives, surface bands that left the icefall as straight lines and were bent into parabolas because the center moves faster than the margins, a pattern derived quantitatively in {doc}`shallow-ice`. Imagery © Google Earth / DigitalGlobe.
```

The creep of ice is the process that controls how glaciers and ice sheets **grow, shrink, and deliver ice to the sea**, and it therefore sits at the heart of the connection between glaciers and sea level. Roughly two-thirds of the world's fresh water is locked in the Greenland and Antarctic ice sheets; if they were to melt or flow into the ocean entirely, global sea level would rise by tens of meters. Understanding how fast ice flows — and how that flow responds to a warming climate — is one of the central problems of modern glaciology.

## Controls on ice flow

At the largest scale, the story is simple: gravity pulls ice downhill, and the ice resists through internal deformation and through friction at its base. The interplay of these effects sets the speed. To make this quantitative we need four ingredients, and the next chapters introduce them in turn:

1. **Mass balance** — how ice is added (snowfall) and removed (melt, calving), and how flow connects the two so that an ice sheet can be in or out of balance ({doc}`mass-balance`).
2. **Stress and strain** — the language for describing the forces inside a deforming continuum and the deformation they produce ({doc}`stress-and-strain`).
3. **Rheology** — the constitutive law, *Glen's flow law*, that tells us how fast ice deforms under a given stress ({doc}`ice-rheology`).
4. **A flow model** — combining force balance with rheology to predict velocity. In the chapters ahead we build such a model numerically with icepack.

```{admonition} A note on scales
:class: tip
Glacier flow spans an enormous range of scales — from the deformation of individual ice crystals (millimeters) to the discharge of entire drainage basins (thousands of kilometers). Most of this book works at the *continuum* scale, treating ice as a deforming fluid whose local behavior is captured by a constitutive law. That is the scale at which ice-sheet models operate.
```

For a thorough treatment of everything in these chapters, see {cite}`cuffey2010`; {cite}`greve2009` gives a more mathematical companion.
