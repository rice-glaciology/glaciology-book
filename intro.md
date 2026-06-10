# Introduction to Glaciology and Ice-Flow Modeling

Welcome to the Rice Glaciology group's open textbook. It introduces the physics of glaciers and ice sheets and shows how to turn that physics into working numerical models with [icepack](https://icepack.github.io/).

The book is aimed at advanced undergraduates and beginning graduate students who have seen some calculus and a little physics, but who are new to glaciology. We build up the ideas in small steps and keep the mathematics tied to physical intuition. Throughout, the standard reference is *The Physics of Glaciers* {cite}`cuffey2010`; we point to specific chapters there for readers who want to go deeper.

## How the book is organized

The first part develops the core ideas of **ice flow** from the ground up:

- why ice flows at all, and why it matters for sea level;
- how glaciers gain and lose mass, and how flow ties the two together;
- the language of **stress and strain** needed to describe a deforming continuum;
- the **rheology** of ice — Glen's flow law — that closes the system.

The second part turns that theory into computation with **icepack**, a Python package for glacier and ice-sheet flow modeling built on the finite element library [Firedrake](https://www.firedrakeproject.org/) {cite}`shapero2021`. We explain the modeling approach, give you a reproducible environment, and work through a complete example.

## Running the code

The modeling chapters use icepack, which runs on Firedrake. Firedrake can be awkward to install directly, so this book ships a **Docker image** that gives you a ready-to-go environment with Firedrake, icepack, and JupyterLab. See {doc}`sections/modeling/running-icepack-docker`. Because that stack is heavy, the notebooks are **not executed** when the book is built — you run them yourself in the container.

```{note}
This is a living document. Each page has "open issue" and "suggest edit" links in the top-right that point back to the source repository, so corrections and contributions are welcome.
```
