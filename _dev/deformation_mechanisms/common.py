"""Shared frame and video writer for the deformation-mechanism animations.

Every video is a 1280 x 720 frame in the group's figure style (``figstyle``):
one or more panels and a one-line caption for the current stage underneath.
Grain-scale videos add a discrete colour bar for c-axis orientation.

A mechanism module builds a ``Video`` and a ``draw`` function. For a single
panel, ``draw(ax, t)`` redraws it at normalized time t in [0, 1]; with
``panels=[...]`` it is ``draw(axes, t)`` with one axes per panel.
"""
from __future__ import annotations

import os
import sys
import textwrap
from dataclasses import dataclass, field

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.animation import FFMpegWriter  # noqa: E402

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import figstyle as fs  # noqa: E402
from figstyle import orient_color  # noqa: E402,F401  (re-exported for the modules)

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
VIDEO_DIR = os.path.join(REPO, "_static", "videos", "deformation")
FIG_DIR = os.path.join(REPO, "sections", "ice_flow", "figures")

# Frame: 12.8 x 7.2 in at 100 dpi = 1280 x 720 px, the native width of the
# Morrow et al. figures, so their type sizes are used as they are.
FRAME_W, FRAME_H = 12.8, 7.2
fs.apply_rc()

# Roles, all from the paper's series colours.
PAPER = "white"
INK = fs.BLACK
MUTED = "0.35"
FAINT = "0.85"
ICE = "white"          # molecules
WATER = fs.BLUE        # liquid water
ACCENT = fs.RED        # the thing to watch: dislocation cores, active slip, cracks
ACCENT2 = fs.GREEN     # secondary: markers, molecules in transit
STRESS = fs.BLACK      # applied-load arrows
FS = fs.FS
FS_TICK = fs.FS_TICK


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
                arrowprops=dict(arrowstyle="-|>,head_width=0.25,head_length=0.6",
                                color=color, lw=kw.pop("lw", fs.s(1.0)), shrinkA=0, shrinkB=0),
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
    title: str                   # short title, in a light-yellow box at the top
    captions: list               # [(t_start, text), ...] in normalized time
    seconds: float = 14.0
    fps: int = 24
    xlim: tuple = (0, 1)         # data limits of the single field panel
    ylim: tuple = (0, 1)
    hold: float = 0.06           # fraction of the clip frozen at each end
    panels: list = None          # [{rect, kind: "field"|"plot", xlim, ylim, letter, title}, ...]
    orient_cbar: bool = False    # add the c-axis orientation colour bar
    _fig: object = field(default=None, repr=False)

    # -- layout -----------------------------------------------------------
    def _setup(self):
        fig = plt.figure(figsize=(FRAME_W, FRAME_H), dpi=100)
        self._fig = fig
        right = 0.87 if self.orient_cbar else 0.98
        specs = self.panels or [dict(rect=[0.02, 0.10, right - 0.02, 0.78], kind="field",
                                     xlim=self.xlim, ylim=self.ylim)]
        fig.text(0.5, 0.95, self.title, ha="center", va="center", fontsize=fs.FS_TITLE,
                 bbox=fs.TITLE_BOX)
        self._specs = specs
        self.axes = [fig.add_axes(p["rect"]) for p in specs]
        if self.orient_cbar:
            fs.orient_colorbar(fig, fig.add_axes([0.905, 0.22, 0.017, 0.56]))
        self.cap = fig.text(0.5, 0.04, "", fontsize=FS, va="center", ha="center")
        if getattr(self, "extra", None):      # static extras such as a second colour bar
            self.extra(fig)

    def caption_at(self, t):
        txt = ""
        for t0, s in self.captions:
            if t >= t0:
                txt = s
        return "\n".join(textwrap.wrap(txt, 120))

    # -- rendering --------------------------------------------------------
    def render(self, draw, out_dir=VIDEO_DIR, preview_at=None):
        """Render the clip. ``draw`` must fully redraw its panel(s)."""
        os.makedirs(out_dir, exist_ok=True)
        self._setup()
        single = self.panels is None

        def frame(t):
            for ax, p in zip(self.axes, self._specs):
                ax.clear()
                if p.get("kind", "field") == "field":
                    ax.set_xlim(*p["xlim"])
                    ax.set_ylim(*p["ylim"])
                    ax.set_aspect("equal")
                    ax.set_axis_off()
            draw(self.axes[0] if single else self.axes, t)
            for ax, p in zip(self.axes, self._specs):
                if p.get("letter"):
                    fs.panel_letter(ax, p["letter"], *p.get("letter_at", (0.03, 0.95)))
                if p.get("title"):
                    fs.title_box(ax, p["title"])
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
                u = i / (n - 1)
                # Hold the first and last frames briefly so viewers can read them.
                t = np.clip((u - self.hold) / (1 - 2 * self.hold), 0, 1)
                frame(t)
                writer.grab_frame()
        # A poster frame for the <video> tag, taken late in the clip.
        frame(0.8)
        self._fig.savefig(os.path.join(out_dir, f"{self.slug}.jpg"), dpi=50,
                          pil_kwargs={"quality": 85})
        plt.close(self._fig)
        return path


    # -- static figure ------------------------------------------------------
    def still(self, draw, stages, path, ncols=2):
        """A publication figure: the panels drawn at each (t, label) in ``stages``,
        one cell per stage with an upper-case letter and a light-yellow stage title."""
        global STILL
        STILL = True
        Y0, Y1 = 0.075, 0.895                     # the frame's panel region
        n = len(stages)
        nrows = int(np.ceil(n / ncols))
        cw = FRAME_W / 2                          # each cell is a half-size frame
        ch = cw * FRAME_H / FRAME_W * (Y1 - Y0)
        band = 0.62                               # room for the stage title
        margin_r = 1.25 if self.orient_cbar else 0.15
        W = ncols * cw + margin_r
        Ht = nrows * (ch + band) + 0.1
        fig = plt.figure(figsize=(W, Ht))
        single = self.panels is None
        specs = self.panels or [dict(rect=[0.01, Y0, 0.98, Y1 - Y0], kind="field",
                                     xlim=self.xlim, ylim=self.ylim)]
        for k, (t, label) in enumerate(stages):
            r, c = divmod(k, ncols)
            x0 = c * cw / W
            top = 1 - (r * (ch + band) + band) / Ht
            cell_w, cell_h = cw / W, ch / Ht
            axes = []
            for p in specs:
                x, y, w, h = p["rect"]
                ax = fig.add_axes([x0 + x * cell_w, top - cell_h + (y - Y0) / (Y1 - Y0) * cell_h,
                                   w * cell_w, h / (Y1 - Y0) * cell_h])
                if p.get("kind", "field") == "field":
                    ax.set_xlim(*p["xlim"]); ax.set_ylim(*p["ylim"])
                    ax.set_aspect("equal"); ax.set_axis_off()
                axes.append(ax)
            draw(axes[0] if single else axes, t)
            yb = top + 0.5 * band / Ht
            fig.text(x0 + 0.03 * cell_w, yb, "ABCDEFGHIJ"[k], ha="center", va="center",
                     fontsize=FS, bbox=fs.LETTER_BOX)
            fig.text(x0 + 0.5 * cell_w, yb, label, ha="center", va="center",
                     fontsize=fs.FS_TITLE, bbox=fs.TITLE_BOX)
        if self.orient_cbar:
            fs.orient_colorbar(fig, fig.add_axes([(ncols * cw + 0.25) / W, 0.2, 0.17 / W, 0.6]))
        STILL = False
        fs.save(fig, path, pad_inches=0.15)
        plt.close(fig)
        return path


# -- registry -------------------------------------------------------------
# Each mechanism module registers a builder that returns (Video, draw).
MECHANISMS = {}


def mechanism(slug, order):
    def deco(fn):
        MECHANISMS[slug] = (order, fn)
        return fn
    return deco


STILL = False       # True while a static figure is drawn: its letters are the figure's


def data_letter(ax, x, y, letter):
    """A grey-circle panel letter at data coordinates, for sub-panels that share one axes."""
    if STILL:
        return
    ax.text(x, y, letter, ha="center", va="center", fontsize=FS, zorder=20, bbox=fs.LETTER_BOX)


def readout(ax, x, y, text):
    """A progress readout (strain, temperature, angle) in a light-blue box, at data coordinates."""
    fs.time_box(ax, x, y, text, transform=ax.transData)
