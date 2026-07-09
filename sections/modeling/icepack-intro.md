# Modeling ice flow with icepack

The chapters ahead develop the physics of ice flow, conservation of mass, the kinematics of stress and strain, and Glen's flow law. To turn that physics into a prediction of how a real glacier moves, we have to solve the **momentum balance equations** that state the divergence of stresses balance the driving force of gravity. Outside of a few idealized analytic geometries this can only be done numerically using tool like the python package [icepack](https://icepack.github.io/) {cite}`shapero2021`.

## Overview

icepack is a library for modeling the flow of glaciers and ice sheets. It is built on top of the [Firedrake](https://www.firedrakeproject.org/) finite element package, which gives us a variety of elements and function spaces to describe the numerics of our problem. A few features make icepack and firedrake well suited to learning *and* research:

- **Physics by composition.** You choose a flow model — an ice shelf, a grounded ice stream, or a hybrid — and icepack assembles the corresponding equations. The rheology (Glen's law) and the boundary conditions are inputs you control.
- **The action principle.** Rather than discretizing the momentum equations directly, icepack derives the flow from minimizing an **action functional**. The velocity solution is the one that minimizes a balance of viscous and gravitational energy. This makes the formulation compact and the solvers robust.
- **Inverse methods.** Because models are differentiable, icepack can *assimilate data*, for example, using surface velocities to infer the basal friction or the fluidity of an ice stream or an ice shelf.

## Diagnostic and prognostic problems

It helps to distinguish two kinds of question:

- A **diagnostic** solve asks: *given the current geometry (thickness, bed) and material properties (fluidity, friction), what is the velocity?* This is a single nonlinear solve of the momentum balance.
- A **prognostic** solve asks: *how does the geometry evolve in time?* It steps the thickness forward using the mass-conservation equation from {doc}`../ice_flow/mass-balance`, re-solving the diagnostic problem as the geometry changes.

## The flow models and running icepack with Docker

icepack provides several depth-averaged flow models. The simplest is the **ice shelf**, floating ice with no basal drag, where flow is resisted only by horizontal stretching (membrane stresses). Adding basal friction gives the **ice stream** model (the shallow-stream/shelfy-stream approximation of {cite}`macayeal1989`), appropriate for fast-flowing grounded ice. A **hybrid** model adds vertical shearing for thicker, slower interior ice. 

icepack runs on Firedrake, a finite element library that depends on a large stack of compiled scientific software (PETSc, MPI, a mesh generator, and more). Installing all of that by hand is the single biggest hurdle to getting started. The reliable solution is a **container**, a pre-built image that bundles a known-good Firedrake, icepack, and JupyterLab. This book ships one, and the rest of this chapter sets it up so that every lab in the book can be run.

```{admonition} You'll need Docker
:class: note
Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) (macOS/Windows) or Docker Engine (Linux) first. The image is several gigabytes, so the first build takes a while; after that it is cached.
```

The `Dockerfile` at the root of the book repository builds on the official Firedrake image and adds icepack and a Jupyter kernel:

```dockerfile
FROM firedrakeproject/firedrake-vanilla:2025-01
SHELL ["/bin/bash", "-c"]

# System packages Firedrake/icepack need for meshing
RUN sudo apt update && sudo apt install -y patchelf gmsh

# Install icepack into the Firedrake virtualenv and register a Jupyter kernel
RUN source firedrake/bin/activate && \
    git clone https://github.com/icepack/icepack.git && \
    pip install --editable ./icepack && \
    pip install ipykernel jupyterlab && \
    python -m ipykernel install --user --name=firedrake --display-name "Firedrake (icepack)"
```

From the book repository (the folder containing the `Dockerfile`):

```bash
# 1. Build the image (first time only — this is the slow step)
docker build -t glaciology-icepack .

# 2. Run it, mounting your current folder so notebooks you create are saved on your machine
docker run -it --rm -p 8888:8888 -v "$PWD":/home/firedrake/work glaciology-icepack
```

The container starts JupyterLab and prints a URL like `http://127.0.0.1:8888/lab`. Open it in your browser.

```{admonition} Pick the right kernel
:class: tip
When you open or create a notebook, choose the **Firedrake (icepack)** kernel (top-right of the notebook). That kernel has Firedrake and icepack on its path; the default Python kernel does not.
```

## Check that it works

Create a notebook and run:

```python
import firedrake
import icepack

print("Firedrake:", firedrake.__version__)
print("icepack:", icepack.__version__)
```

If that imports without error, you are ready for the modeling labs. Anything you save under `/home/firedrake/work` (the mounted folder) persists on your computer after the container stops.

## One kernel for every lab

The image is built so that every notebook in this book runs in the same kernel. The modeling labs need Firedrake and icepack while the observing labs additionally use obspy for seismic data processing, rasterio and scikit-image to process and interpret satellite imagery, netCDF4, h5py, and xarray for altimetry and gravity files, and earthaccess, icepyx, asf_search, and hyp3_sdk for programmatic data access, all of which are installed in the container. Two practical notes apply to the observing labs. Their download cells need network access from inside the container and, for the NASA archives, a free Earthdata login, which the access libraries will prompt for on first use; and the cells marked as not executed at build are sized so that what they fetch fits comfortably in the mounted work folder, with each lab's text stating the expected volumes before any download begins. A quick way to verify the full stack is to run the import block below in a fresh notebook.

```python
import firedrake, icepack, irksome
import netCDF4, h5py, xarray, rasterio, skimage, obspy
import earthaccess, icepyx, asf_search, hyp3_sdk, geopandas, pyproj
print("all lab dependencies import cleanly")
```
