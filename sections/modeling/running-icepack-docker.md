# Running icepack with Docker

icepack runs on [Firedrake](https://www.firedrakeproject.org/), a finite element library that depends on a large stack of compiled scientific software (PETSc, MPI, a mesh generator, and more). Installing all of that by hand is the single biggest hurdle to getting started. The reliable solution is a **container**: a pre-built image that bundles a known-good Firedrake, icepack, and JupyterLab. This book ships one.

```{admonition} You'll need Docker
:class: note
Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) (macOS/Windows) or Docker Engine (Linux) first. The image is several gigabytes, so the first build takes a while; after that it is cached.
```

## The image

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

## Build and run

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

If that imports without error, you are ready for the next chapter. Anything you save under `/home/firedrake/work` (the mounted folder) persists on your computer after the container stops.

## One kernel for every lab

The image is built so that every notebook in this book runs in this single kernel, not just the icepack chapters. The modeling labs need Firedrake and icepack; the observing-part labs additionally use obspy for seismic data, rasterio and scikit-image for imagery and interferograms, netCDF4, h5py, and xarray for altimetry and gravity files, and earthaccess, icepyx, asf_search, and hyp3_sdk for programmatic data access, all of which are installed in the container. Two practical notes apply to the observing labs. Their download cells need network access from inside the container and, for the NASA archives, a free Earthdata login, which the access libraries will prompt for on first use; and the cells marked as not executed at build are sized so that what they fetch fits comfortably in the mounted work folder, with each lab's text stating the expected volumes before any download begins. A quick way to verify the full stack is to run the import block below in a fresh notebook.

```python
import firedrake, icepack, irksome
import netCDF4, h5py, xarray, rasterio, skimage, obspy
import earthaccess, icepyx, asf_search, hyp3_sdk, geopandas, pyproj
print("all lab dependencies import cleanly")
```
