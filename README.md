# Introduction to Glaciology and Ice-Flow Modeling

Source for the Rice Glaciology group's open textbook, built with [Jupyter Book](https://jupyterbook.org/) and deployed to GitHub Pages. It introduces glaciological concepts and ice-flow modeling with [icepack](https://icepack.github.io/).

## Build locally

```bash
pip install -r requirements.txt
jupyter-book build .
# open _build/html/index.html
```

## Run the modeling chapters (icepack)

icepack runs on [Firedrake](https://www.firedrakeproject.org/), which is easiest to use via the included Docker image:

```bash
docker build -t glaciology-icepack .
docker run -it --rm -p 8888:8888 -v "$PWD":/home/firedrake/work glaciology-icepack
```

Open the JupyterLab URL it prints and select the **Firedrake (icepack)** kernel. See the "Running icepack with Docker" chapter for details.

## Deploy

Pushing to `main` triggers `.github/workflows/deploy.yml`, which builds the book and publishes it to GitHub Pages (set **Settings → Pages → Source → GitHub Actions**). It is intended to live at `https://rice-glaciology.github.io/glaciology-book`.

## Editing

Chapters are MyST-Markdown files under `sections/`. The table of contents is `_toc.yml`; site settings are `_config.yml`; references are in `references.bib`.
