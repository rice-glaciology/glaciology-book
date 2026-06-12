# Modeling ice flow with icepack

The chapters ahead develop the physics of ice flow, conservation of mass, the kinematics of stress and strain, and Glen's flow law. To turn that physics into a prediction of how a real glacier moves, we have to solve the **momentum balance** — the statement that the divergence of stress balances the driving force of gravity — together with the flow law, on a real domain. Outside of a few idealized geometries this can only be done numerically. [icepack](https://icepack.github.io/) is a Python package built for exactly this purpose {cite}`shapero2021`.

## Overview

icepack is a library for modeling the flow of glaciers and ice sheets. It is built on top of the [Firedrake](https://www.firedrakeproject.org/) finite element system, which means models are expressed in terms of the underlying variational (weak) form of the equations and discretized automatically. A few features make it well suited to learning and to research:

- **Physics by composition.** You choose a flow model — an ice shelf, a grounded ice stream, or a hybrid — and icepack assembles the corresponding equations. The rheology (Glen's law) and the boundary conditions are inputs you control.
- **The action principle.** Rather than discretizing the momentum equations directly, icepack derives the flow from minimizing an **action functional**. The velocity that a glacier takes is the one that minimizes a balance of viscous and gravitational energy. This makes the formulation compact and the solvers robust.
- **Inverse methods.** Because models are differentiable, icepack can *assimilate data* — for example, inferring the basal friction or ice fluidity that makes a modeled velocity field match satellite observations.

## Diagnostic and prognostic problems

It helps to distinguish two kinds of question:

- A **diagnostic** solve asks: *given the current geometry (thickness, bed) and material properties (fluidity, friction), what is the velocity?* This is a single nonlinear solve of the momentum balance.
- A **prognostic** solve asks: *how does the geometry evolve in time?* It steps the thickness forward using the mass-conservation equation from {doc}`../ice_flow/mass-balance`, re-solving the diagnostic problem as the geometry changes.

In this book we focus on the diagnostic problem, which is the natural first model and the building block for everything else.

## The flow models

icepack provides several depth-averaged flow models. The simplest is the **ice shelf**, floating ice with no basal drag, where flow is resisted only by horizontal stretching (membrane stresses). Adding basal friction gives the **ice stream** model (the shallow-stream/shelfy-stream approximation of {cite}`macayeal1989`), appropriate for fast-flowing grounded ice. A **hybrid** model adds vertical shearing for thicker, slower interior ice. We start with the ice shelf because it isolates the membrane physics with the fewest moving parts.

The next chapter sets up the computing environment, and the one after works through a complete ice-shelf model.
