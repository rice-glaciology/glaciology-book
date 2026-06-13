# The finite element method

The equations of glacier flow derived in this book, the Stokes system and the shallow approximations that descend from it, are partial differential equations posed on awkward domains. A real ice sheet has a ragged coastline, a grounding line that migrates, fast streams next to nearly stagnant ice, and a viscosity that depends nonlinearly on the very velocity being solved for. Solving such problems on a computer is the work of the modelling chapters, and the method those chapters use, by way of the icepack library, is the finite element method. This chapter introduces it, framed throughout around the ice-flow equations it will be used to solve. It belongs with the mathematical background because the method is general, but its payoff is the numerical glacier model of {doc}`../modeling/icepack-intro`. Helpful background is in {cite}`greve2009`, and the icepack implementation is described in {cite}`shapero2021`.

## Motivation

The oldest numerical method, finite differences, lays a regular grid over the domain and replaces each derivative by a difference of neighbouring grid values. It is simple and works well on rectangles, but it struggles with exactly the features that matter for ice. A regular grid cannot follow a fjord wall or a grounding line without staircasing it, it wastes resolution on the slow interior to afford resolution at the fast margin, and it makes the traction boundary conditions at a calving front or a sliding bed awkward to impose. The finite element method was built for irregular domains. It covers the domain with an unstructured mesh of small elements, triangles in two dimensions or tetrahedra in three, that can be made fine where the flow is complicated and coarse where it is smooth, and it can conform to any boundary shape. It also handles the nonlinearity of Glen's law and the mixed boundary conditions of ice flow in a natural way, which is why nearly every modern ice-sheet model, icepack among them, is built on it.

## From the strong form to the weak form

The starting point is the differential equation as written in the earlier chapters, called the strong form. For a diagnostic flow model it is the momentum balance of {doc}`../ice_flow/stress-balance`, that the divergence of the stress balances gravity, together with the flow law that relates stress to the velocity. The strong form demands that the equation hold at every point, which requires the solution to be smooth enough to differentiate twice. The finite element method works instead with a weaker statement that asks less of the solution.

The idea is to stop requiring the equation to hold pointwise and require only that it hold on average against every member of a family of test functions. Multiply the momentum balance by an arbitrary test function $\mathbf{w}$, which can be thought of as a virtual velocity, and integrate over the whole ice domain $\Omega$,

$$
\int_\Omega \mathbf{w}\cdot\left(\nabla\!\cdot\!\boldsymbol{\sigma}+\rho_i\mathbf{g}\right)\,\mathrm{d}V = 0 .
$$

Now integrate the stress term by parts, the multidimensional version of moving a derivative from one factor to the other. This lowers the order of the derivative on the stress and raises one onto the test function, and it produces a boundary integral,

$$
-\int_\Omega \nabla\mathbf{w}:\boldsymbol{\sigma}\,\mathrm{d}V
+\int_{\partial\Omega} \mathbf{w}\cdot\boldsymbol{\sigma}\mathbf{n}\,\mathrm{d}S
+\int_\Omega \mathbf{w}\cdot\rho_i\mathbf{g}\,\mathrm{d}V = 0 .
$$

This is the weak, or variational, form. Two things have been gained. The solution now needs only one derivative rather than two, so the piecewise-polynomial approximations introduced below are admissible. And the boundary integral has made the natural boundary conditions explicit: the term $\boldsymbol{\sigma}\mathbf{n}$ is the traction on the ice surface, so a stress-free upper surface, the water pressure at a calving front, and the ocean pressure beneath a shelf all enter here, simply by substituting the known traction. The conditions that prescribe the velocity itself, such as no slip on a frozen bed or a given inflow, are imposed differently, as described below.

## The action principle for ice

For ice flow the weak form has an especially clean origin. Glaciers, being slow viscous flows, settle into the velocity field that minimizes a functional, the rate at which energy is dissipated by viscous deformation minus the rate at which gravity does work. This action functional, for Glen's law with exponent $n$, takes the schematic form

$$
J(\mathbf{u}) = \int_\Omega \left[\frac{2A^{-1/n}}{1+1/n}\,\dot\varepsilon_E^{\,1+1/n} - \rho_i\,\mathbf{g}\cdot\mathbf{u}\right]\mathrm{d}V
+ (\text{boundary terms}),
$$

with $\dot\varepsilon_E$ the effective strain rate of {doc}`tensor-algebra`. The true velocity is the one that makes this functional stationary, and setting its first variation to zero recovers exactly the weak form above. Because the functional is convex, the minimizer is unique, and the problem is well posed. This variational viewpoint is the one icepack adopts: a flow model is specified by writing down its action functional, and the basal friction law of {doc}`../thermomechanics/basal-motion` enters as a boundary contribution to it.

## Discretization with a mesh and basis functions

To turn the weak form into something a computer can solve, the infinite-dimensional space of possible velocities is replaced by a finite-dimensional one. The domain is divided into a mesh of elements, and on that mesh a set of basis functions $\phi_j$ is defined, each a simple polynomial that equals one at a single mesh node and zero at all the others, so that it is nonzero only on the handful of elements touching that node. The simplest choice, piecewise-linear functions on triangles, gives a velocity that varies linearly across each element; quadratic functions resolve the curved velocity profile of sheared ice more accurately. The approximate velocity is written as a sum over the nodes,

$$
\mathbf{u}_h(\mathbf{x}) = \sum_j \mathbf{U}_j\,\phi_j(\mathbf{x}),
$$

so that the unknowns are now the finite set of nodal values $\mathbf{U}_j$. The Galerkin method completes the recipe by choosing the test functions from the same set of basis functions. Substituting both the trial sum and each basis function as a test function into the weak form turns the single variational statement into one algebraic equation per node.

## The algebraic system and its solution

For a linear problem the result of this substitution is a matrix equation,

$$
\mathbf{K}\,\mathbf{U} = \mathbf{F},
$$

where the stiffness matrix $\mathbf{K}$ collects the interactions between basis functions, the load vector $\mathbf{F}$ holds the gravitational forcing and the traction boundary terms, and $\mathbf{U}$ is the vector of unknown nodal velocities. The matrix is assembled element by element, each element contributing only to the rows and columns of the few nodes it touches, so $\mathbf{K}$ is sparse, and large sparse systems can be solved efficiently. Ice flow is not linear, because the viscosity in Glen's law depends on the strain rate and so on the unknown velocity. The system is therefore nonlinear, $\mathbf{K}(\mathbf{U})\,\mathbf{U}=\mathbf{F}$, and it is solved by iteration. A Newton or Picard scheme makes a guess at the velocity, evaluates the viscosity from it, solves the resulting linear system for a correction, and repeats until the velocity stops changing. Each iteration is one sparse linear solve, and a handful of them usually suffices.

## Boundary conditions

The two kinds of boundary condition enter in two different ways. The essential, or Dirichlet, conditions that prescribe the velocity, a frozen bed where the ice does not slide or a prescribed influx, are imposed by building them into the space of trial functions, fixing the corresponding nodal values rather than solving for them. The natural, or Neumann, conditions that prescribe the traction, the stress-free surface and the water and ocean pressures, are already present in the boundary integral of the weak form and require nothing more than substituting the known stress. The basal friction law sits between these, contributing a traction that depends on the sliding velocity and so appearing as a boundary term that is updated through the nonlinear iteration.

This division is one reason the method suits glaciers so well. The membrane stresses and long-range stress transmission that the shallow-ice approximation of {doc}`../ice_flow/shallow-ice` discarded, and that dominate in ice streams and shelves, are kept naturally in the weak form. Unstructured meshes conform to grounding lines and coastlines and can be refined precisely where the velocity gradients are sharp. The incompressible Stokes problem, which couples velocity and pressure, is handled by choosing compatible element pairs for the two fields. And the whole scheme can be checked against the analytical solutions derived earlier, the Vialov profile and the spreading ice shelf, before it is trusted on real geometry, a verification step the modelling chapters carry out.

## Implementation in icepack

Writing out the stiffness matrix and the assembly loops by hand for a three-dimensional nonlinear ice-flow problem would be a major undertaking, and this is the gap that modern finite element libraries fill. Firedrake, on which icepack is built, lets the modeller write the weak form, or equivalently the action functional, in a high-level notation that reads almost like the mathematics on this page, and then generates and runs the efficient parallel code automatically. The icepack library wraps this in the specific functionals of glacier flow, the shallow-ice, shallow-shelf, and hybrid models, together with the rheology and friction laws of the earlier chapters, so that building a glacier model becomes a matter of supplying a mesh, the geometry and temperature fields, and the boundary conditions, and asking for the velocity. The next chapter puts this to work.
