# Firedrake + icepack environment for running the modeling chapters.
# Based on the Rice Glaciology firedrake-docker setup.
#
# Build:  docker build -t glaciology-icepack .
# Run:    docker run -it --rm -p 8888:8888 -v "$PWD":/home/firedrake/work glaciology-icepack
# Then open the JupyterLab URL printed in the terminal and pick the "Firedrake (icepack)" kernel.

FROM firedrakeproject/firedrake-vanilla:2025-01
SHELL ["/bin/bash", "-c"]

# System packages Firedrake/icepack need for meshing
RUN sudo apt update && sudo apt install -y patchelf gmsh && sudo rm -rf /var/lib/apt/lists/*

# Install icepack into the Firedrake virtualenv and register a Jupyter kernel
RUN source firedrake/bin/activate && \
    git clone https://github.com/icepack/icepack.git && \
    pip install --editable ./icepack && \
    pip install ipykernel jupyterlab && \
    python -m ipykernel install --user --name=firedrake --display-name "Firedrake (icepack)"

# Time stepping for the phase-change material (Irksome) and the dependencies
# of the observing-part labs, so every notebook in the book runs in this one
# kernel: netCDF/HDF readers (radar altimetry, GRACE, ICESat-2), obspy
# (cryoseismicity), rasterio + scikit-image (imagery, InSAR), earthaccess +
# icepyx + asf_search + hyp3_sdk (programmatic data download), geopandas +
# pyproj (basin masks, polar projections).
RUN source firedrake/bin/activate && \
    pip install irksome && \
    pip install netCDF4 h5py xarray rasterio scikit-image obspy \
                earthaccess icepyx asf_search hyp3_sdk geopandas pyproj

WORKDIR /home/firedrake/work
EXPOSE 8888
CMD source /home/firedrake/firedrake/bin/activate && \
    jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --NotebookApp.token=''
