# A synthetic ice shelf

This chapter builds a complete, if idealized, ice-flow model: a rectangular **floating ice shelf** fed by ice flowing in one side. It is the smallest example that contains real ice physics — Glen's flow law, a momentum balance, and boundary conditions — and it introduces every piece of the icepack workflow that larger models reuse.

```{admonition} Run this in the container
:class: tip
The code below is meant to be run in the Firedrake/icepack environment from {doc}`running-icepack-docker`, with the **Firedrake (icepack)** kernel. It is **not executed** when the book is built, so you won't see output here — copy it into a notebook and run it yourself.
```

## The domain

Every finite element model starts with a **mesh** of the region we want to solve on. Here it is a 20 km × 20 km square, and we define two function spaces on it: a scalar space `Q` for fields like thickness and a vector space `V` for the velocity. Degree-2 (`CG 2`) elements give a smooth, accurate velocity.

```python
import firedrake
import icepack

Lx, Ly = 20e3, 20e3      # domain size (m)
nx, ny = 32, 32          # mesh resolution
mesh = firedrake.RectangleMesh(nx, ny, Lx, Ly)

Q = firedrake.FunctionSpace(mesh, "CG", 2)         # scalars (thickness, fluidity)
V = firedrake.VectorFunctionSpace(mesh, "CG", 2)   # vectors (velocity)

x, y = firedrake.SpatialCoordinate(mesh)
```

`RectangleMesh` labels its four edges with integer **boundary ids**: `1` is the inflow edge at $x=0$, `2` the outflow at $x=L_x$, and `3`, `4` the sides. We'll use those ids to set boundary conditions.

## Geometry and material properties

We prescribe a thickness that **thins downstream**, from 500 m at the inflow to 400 m at the calving front, and an initial guess for the velocity that increases downstream. The flow's fluidity comes from the temperature through the rate factor of {doc}`../ice_flow/ice-rheology`; a uniform $-18^\circ$C ($255$ K) is a reasonable cold-shelf value.

```python
u_in, h_in = 100.0, 500.0     # inflow speed (m/yr) and thickness (m)
dh, du = 100.0, 100.0         # downstream change in thickness and speed

h = firedrake.Function(Q).interpolate(h_in - dh * x / Lx)
u0 = firedrake.Function(V).interpolate(
    firedrake.as_vector((u_in + du * x / Lx, 0.0))
)

T = firedrake.Constant(255.0)        # temperature (K)
A = icepack.rate_factor(T)           # fluidity in Glen's law
```

## The model and the solve

Now we pick the **ice shelf** flow model and create a solver. The only boundary condition we impose on the velocity is at the inflow (`dirichlet_ids=[1]`), where ice enters at the prescribed speed; the other edges are left free, which lets ice spread and accelerate. The **diagnostic solve** then finds the velocity field that balances the membrane (stretching) stresses against the gravitational driving stress — internally, by minimizing icepack's action functional.

```python
model = icepack.models.IceShelf()
solver = icepack.solvers.FlowSolver(model, dirichlet_ids=[1])

u = solver.diagnostic_solve(
    velocity=u0,
    thickness=h,
    fluidity=A,
)
```

## Looking at the result

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots()
axes.set_aspect("equal")
colors = firedrake.tripcolor(u, axes=axes)   # plots speed
fig.colorbar(colors, label="speed (m/yr)")
plt.show()
```

You should see the ice **accelerate from the inflow toward the calving front**, reaching speeds well above the 100 m/yr it entered with. This is the signature of an ice shelf: with no friction at its base, the only thing resisting flow is the ice's own resistance to stretching, so as the shelf thins downstream it speeds up to conserve mass — exactly the flux relationship $\mathbf{q}=\bar{\bu}h$ from {doc}`../ice_flow/mass-balance`.

```{admonition} Try it yourself
:class: seealso
- Lower the temperature `T` (stiffer ice) and re-solve. Does the shelf flow faster or slower?
- Change `dh` so the shelf thins more sharply. How does the speed at the calving front respond?
- Replace the uniform temperature with one that varies in space, `T = firedrake.Function(Q).interpolate(...)`, and pass the resulting fluidity field to the solver.

These are the same moves — change the geometry or rheology, re-solve, compare — that underlie real modeling studies. The next step, beyond this book's first edition, is the **prognostic** problem: stepping the thickness forward in time with the mass-balance equation while re-solving for velocity, so the shelf evolves.
```

For the theory behind the ice-shelf and ice-stream models, see {cite}`macayeal1989`; for icepack itself, {cite}`shapero2021`.
