# Introduction to Glaciology and Ice-Flow Modeling

Welcome to the Rice Glaciology group's open textbook. It introduces the physics of glaciers and ice sheets and shows how to turn that physics into working numerical models with [icepack](https://icepack.github.io/).

The book is aimed at advanced undergraduates and beginning graduate students who have seen some calculus and a little physics, but who are new to glaciology. We build up the ideas in small steps and keep the mathematics tied to physical intuition. Throughout, the standard reference is *The Physics of Glaciers* {cite}`cuffey2010`; we point to specific chapters there for readers who want to go deeper.

## How the book is organized

The order of the chapters follows a single pedagogical choice: the book is built around the distinction between the diagnostic and the prognostic problems of ice flow. The diagnostic problem is to find the velocity of a glacier whose shape is known at one instant. The prognostic problem is to evolve that shape forward in time. The first needs the physics of how ice resists stress; the second adds the physics of how ice gains and loses mass. We teach them in that order, and the structure of the book reflects it.

The opening chapters assemble everything the diagnostic problem requires, working from the molecule outward. We begin with the **physics of ice** itself: the water molecule and its bonding, the open crystal that results, the lattice vibrations that carry heat, and the point defects hidden in the proton disorder. This is more chemistry than a flow modeler strictly needs, but it pays off, because the deformation of ice turns out to be a defect-mediated process and Glen's flow law is most honestly understood from the bottom up. From there we develop **deformation and flow**: the language of stress and strain, the **rheology** that closes the system, the momentum balance, and the hierarchy of approximations that follow from it. Two further ingredients complete the diagnostic picture, the **thermal structure** that sets how soft the ice is and the **bed** that sets how freely it slides, followed by the **observations** that supply a real geometry to model. Only then do we turn to computation with **icepack**, a Python package for glacier and ice-sheet flow modeling built on the finite element library [Firedrake](https://www.firedrakeproject.org/) {cite}`shapero2021`, and solve the diagnostic problem on real ice.

The later chapters take up the prognostic problem. Here we introduce **mass balance**, the accumulation and ablation that force changes in thickness, and only here do we treat **firn**, the slow transformation of snow into ice. Firn is deliberately held back rather than placed with the physics of ice at the front. It belongs to the surface and to climate: it records past atmospheres in ice cores, it complicates the conversion of satellite elevation change into mass change, and it is a piece of the prognostic story rather than something the diagnostic solve needs. Grouping it with mass balance and climate keeps the front of the book focused on the single question of what makes ice flow, and lets the connections to past and future climate come together in one place once the machinery to model them is in hand.

## Running the code

The modeling chapters use icepack, which runs on Firedrake. Firedrake can be awkward to install directly, so this book ships a **Docker image** that gives you a ready-to-go environment with Firedrake, icepack, and JupyterLab. See {doc}`sections/modeling/running-icepack-docker`. Because that stack is heavy, the notebooks are **not executed** when the book is built — you run them yourself in the container.

```{note}
This is a living document. Each page has "open issue" and "suggest edit" links in the top-right that point back to the source repository, so corrections and contributions are welcome.
```
