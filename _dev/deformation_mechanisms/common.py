"""Shared layout, colors and video writer for the deformation-mechanism animations.

Every video has the same frame (1280 x 720):

    +--------------------------------------+------------------+
    |  title                               |  fact sheet      |
    |                                      |  (rate law, n,   |
    |  main panel: what the crystals do    |   grain size, Q, |
    |                                      |   where it acts) |
    |  caption for the current stage       |                  |
    +--------------------------------------+------------------+

A mechanism module builds a `Video`, then calls `video.render(draw)`, where
`draw(ax, t)` redraws the main panel for normalized time t in [0, 1].
"""
from __future__ import annotations

import os
import textwrap
from dataclasses import dataclass, field

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.animation import FFMpegWriter  # noqa: E402

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
VIDEO_DIR = os.path.join(REPO, "_static", "videos", "deformation")
FIG_DIR = os.path.join(REPO, "sections", "ice_flow", "figures")

# Palette: warm paper background, dark ink, one accent per role.
PAPER = "#fbfaf6"
INK = "#1f2933"
MUTED = "#6b7280"
FAINT = "#d6d3cb"
ICE = "#cfe6f2"        # plain ice fill
WATER = "#2b7bb9"      # liquid water, vacancies flowing
ACCENT = "#c2410c"     # the thing to watch (dislocation core, crack, ...)
ACCENT2 = "#047857"    # secondary highlight (new grains, atoms in transit)
STRESS = "#7c3aed"     # applied-load arrows

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12,
    "figure.facecolor": PAPER,
    "axes.facecolor": PAPER,
    "savefig.facecolor": PAPER,
    "text.color": INK,
    "axes.edgecolor": INK,
})

ORIENT_CMAP = plt.get_cmap("hsv")


def orient_color(theta, alpha=1.0):
    """Color for a c-axis at angle theta (radians, axial so theta and theta+pi match).

    A cyclic map stands in for the interference colors of a thin section
    viewed between crossed polarizers: grains with similar c-axes look alike.
    """
    u = (np.asarray(theta) % np.pi) / np.pi
    c = np.array(ORIENT_CMAP(u))
    # Pastel version so ink drawn on top stays readable.
    c[..., :3] = 0.30 * c[..., :3] + 0.70
    c[..., 3] = alpha
    return c


def smooth(t, a=0.0, b=1.0):
    """Smoothstep from 0 (t <= a) to 1 (t >= b)."""
    if b <= a:
        return float(t >= a)
    x = np.clip((t - a) / (b - a), 0.0, 1.0)
    return x * x * (3 - 2 * x)


def ramp(t, a=0.0, b=1.0):
    """Linear ramp from 0 (t <= a) to 1 (t >= b)."""
    return float(np.clip((t - a) / (b - a), 0.0, 1.0)) if b > a else float(t >= a)


def arrow(ax, x, y, dx, dy, color=STRESS, width=0.012, **kw):
    ax.annotate("", (x + dx, y + dy), (x, y),
                arrowprops=dict(arrowstyle="-|>,head_width=0.4,head_length=0.8",
                                color=color, lw=kw.pop("lw", 3.0), shrinkA=0, shrinkB=0),
                annotation_clip=False, **kw)


def load_arrows(ax, box, mode, strength=1.0, color=STRESS, gap=0.06, size=0.16):
    """Draw applied-load arrows around a box (x0, x1, y0, y1) in data units.

    mode: 'compress-y' (vertical squeeze), 'extend-x', 'shear' (top right,
    bottom left) or 'compress-y-extend-x' (pure shear, both pairs).
    """
    if strength <= 0:
        return
    x0, x1, y0, y1 = box
    W, H = x1 - x0, y1 - y0
    L = size * max(W, H) * strength
    g = gap * max(W, H)
    xs = np.linspace(x0 + 0.25 * W, x1 - 0.25 * W, 3)
    ys = np.linspace(y0 + 0.25 * H, y1 - 0.25 * H, 3)
    if mode in ("compress-y", "compress-y-extend-x"):
        for x in xs:
            arrow(ax, x, y1 + g + L, 0, -L, color)
            arrow(ax, x, y0 - g - L, 0, L, color)
    if mode in ("extend-x", "compress-y-extend-x"):
        for y in ys:
            arrow(ax, x1 + g, y, L, 0, color)
            arrow(ax, x0 - g, y, -L, 0, color)
    if mode == "shear":
        for x in xs:
            arrow(ax, x - L / 2, y1 + g, L, 0, color)
            arrow(ax, x + L / 2, y0 - g, -L, 0, color)


@dataclass
class Video:
    slug: str                    # file name stem, e.g. "basal-glide"
    title: str                   # headline at the top of the frame
    scale: str                   # e.g. "atomic scale (~1 nm)"
    facts: list                  # [(label, value), ...] for the fact sheet
    where: str                   # one paragraph: where it matters in glaciers
    captions: list               # [(t_start, text), ...] in normalized time
    seconds: float = 14.0
    fps: int = 24
    xlim: tuple = (0, 1)
    ylim: tuple = (0, 1)
    hold: float = 0.06           # fraction of the clip frozen at each end
    _fig: object = field(default=None, repr=False)

    # -- layout -----------------------------------------------------------
    def _setup(self):
        fig = plt.figure(figsize=(12.8, 7.2), dpi=100)
        self._fig = fig
        fig.text(0.025, 0.945, self.title, fontsize=22, weight="bold", va="center")
        fig.text(0.025, 0.895, self.scale, fontsize=12.5, color=MUTED, va="center")
        self.ax = fig.add_axes([0.025, 0.14, 0.62, 0.72])
        self.cap = fig.text(0.025, 0.07, "", fontsize=13.5, va="center", ha="left",
                            linespacing=1.35)
        self._side(fig)
        fig.text(0.975, 0.02, "Introduction to Glaciology · Rice Glaciology",
                 fontsize=8.5, color=MUTED, ha="right")

    def _side(self, fig):
        side = fig.add_axes([0.675, 0.06, 0.30, 0.86])
        side.set_axis_off()
        side.add_patch(plt.Rectangle((0, 0), 1, 1, transform=side.transAxes,
                                     facecolor="#f2efe7", edgecolor=FAINT, lw=1))
        # Shrink the type until the fact sheet fits in the panel.
        for k in np.linspace(1.0, 0.7, 13):
            if self._side_text(side, k, dry=True) > 0.02:
                break
        self._side_text(side, k)

    def _side_text(self, side, k, dry=False):
        def put(y, s, **kw):
            if not dry:
                side.text(0.06, y, s, transform=side.transAxes, va="top", **kw)

        y = 0.955
        for label, value in self.facts:
            put(y, label.upper(), fontsize=9 * k, color=MUTED, weight="bold")
            y -= 0.04 * k
            lines = [value] if value.startswith("$") else textwrap.wrap(value, int(34 / k))
            for ln in lines:
                put(y, ln, fontsize=13 * k)
                y -= 0.048 * k
            y -= 0.022 * k
        put(y, "WHERE IT MATTERS", fontsize=9 * k, color=MUTED, weight="bold")
        y -= 0.04 * k
        for ln in textwrap.wrap(self.where, int(38 / k)):
            put(y, ln, fontsize=11.5 * k)
            y -= 0.042 * k
        return y

    def caption_at(self, t):
        txt = ""
        for t0, s in self.captions:
            if t >= t0:
                txt = s
        return "\n".join(textwrap.wrap(txt, 84))

    # -- rendering --------------------------------------------------------
    def render(self, draw, out_dir=VIDEO_DIR, preview_at=None):
        """Render the clip. `draw(ax, t)` must fully redraw the main axes."""
        os.makedirs(out_dir, exist_ok=True)
        self._setup()
        ax = self.ax

        def frame(t):
            ax.clear()
            ax.set_xlim(*self.xlim)
            ax.set_ylim(*self.ylim)
            ax.set_aspect("equal")
            ax.set_axis_off()
            draw(ax, t)
            self.cap.set_text(self.caption_at(t))

        if preview_at is not None:  # one still for quick checks
            frame(preview_at)
            path = os.path.join(out_dir, f"{self.slug}-preview.png")
            self._fig.savefig(path, dpi=80)
            plt.close(self._fig)
            return path

        n = int(round(self.seconds * self.fps))
        writer = FFMpegWriter(fps=self.fps, codec="libx264", bitrate=-1,
                              extra_args=["-pix_fmt", "yuv420p", "-crf", "27",
                                          "-preset", "slow", "-movflags", "+faststart"])
        path = os.path.join(out_dir, f"{self.slug}.mp4")
        with writer.saving(self._fig, path, dpi=100):
            for i in range(n):
                s = i / (n - 1)
                # Hold the first and last frames briefly so viewers can read them.
                t = np.clip((s - self.hold) / (1 - 2 * self.hold), 0, 1)
                frame(t)
                writer.grab_frame()
        # A poster frame for the <video> tag, taken late in the clip.
        frame(0.8)
        self._fig.savefig(os.path.join(out_dir, f"{self.slug}.jpg"), dpi=50,
                          pil_kwargs={"quality": 80})
        plt.close(self._fig)
        return path


# -- registry -------------------------------------------------------------
# Each mechanism module registers a builder that returns (Video, draw).
MECHANISMS = {}


def mechanism(slug, order):
    def deco(fn):
        MECHANISMS[slug] = (order, fn)
        return fn
    return deco
