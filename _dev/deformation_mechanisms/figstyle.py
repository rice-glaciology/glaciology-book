r"""Figure style for the deformation-mechanism animations and figures.

Follows the group's figure grammar, as defined in ``scripts/figstyle.py`` of
the vertical-velocity paper (github.com/hoffmaao/vertical_velocity), after
Morrow, Ghelichkhan & Kramer (2026):

  * Times text with STIX math, 8.5 pt text, 9 pt axis labels, 7.5 pt ticks;
  * series in a fixed colour order, never cycled: red, blue, black, green, purple;
  * fields in ``N_LEVELS`` discrete colour bands, colour bars likewise;
  * panels carry no headings; panel letters sit in light-grey circles;
  * ``grid(which="both", alpha=0.3)`` under the data;
  * figures written without timestamps.

Sizes are set for a figure drawn at print width ``FULL`` (17.8 cm). A video
frame is wider than that in inches, so ``apply_rc(scale)`` multiplies every
length by the frame's width / ``FULL``: the frame then looks exactly like a
full-width figure enlarged to 1280 pixels.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import BoundaryNorm, LinearSegmentedColormap, ListedColormap
from matplotlib.ticker import MaxNLocator

# -- series (reported.py in Morrow et al.) -----------------------------------
RED, BLUE, BLACK, GREEN, PURPLE = "#d62728", "#3182bd", "#000000", "#2ca02c", "#9467bd"
ORANGE = "#ff7f0e"
GREY = "gray"
LW, MS = 1.1, 4.5

# -- page and type -------------------------------------------------------------
FULL = 17.8 / 2.54                 # inches, Copernicus full width
DPI = 300
FS, FS_LABEL, FS_TICK = 8.5, 9.0, 7.5
N_LEVELS = 10
LETTER_BOX = dict(boxstyle="circle,pad=0.25", facecolor="lightgrey", edgecolor="black", lw=0.6)
MINUS = "\N{MINUS SIGN}"

_scale = 1.0


def s(x):
    """A length in points at the current scale."""
    return x * _scale


def apply_rc(scale=1.0):
    """The paper's rcParams, every length multiplied by ``scale``."""
    global _scale
    _scale = scale
    k = scale
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Times New Roman", "STIXGeneral", "DejaVu Serif"],
        "mathtext.fontset": "stix",
        "font.size": FS * k, "axes.titlesize": FS * k, "axes.labelsize": FS_LABEL * k,
        "xtick.labelsize": FS_TICK * k, "ytick.labelsize": FS_TICK * k, "legend.fontsize": FS * k,
        "axes.linewidth": 0.6 * k, "xtick.major.width": 0.6 * k, "ytick.major.width": 0.6 * k,
        "xtick.minor.width": 0.4 * k, "ytick.minor.width": 0.4 * k,
        "xtick.major.size": 3.0 * k, "ytick.major.size": 3.0 * k,
        "xtick.major.pad": 3.5 * k, "ytick.major.pad": 3.5 * k,
        "axes.labelpad": 4.0 * k,
        "lines.linewidth": LW * k, "lines.markersize": MS * k, "axes.unicode_minus": True,
        "legend.edgecolor": "black", "legend.fancybox": False, "legend.framealpha": 1.0,
        "patch.linewidth": 0.6 * k,
        "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white",
        "text.color": BLACK, "axes.edgecolor": BLACK,
        "axes.spines.top": True, "axes.spines.right": True,
        "figure.dpi": 100, "savefig.dpi": DPI, "pdf.fonttype": 42, "ps.fonttype": 42,
    })


def grid(ax):
    ax.grid(True, which="both", alpha=0.3, zorder=0, lw=s(0.6))
    ax.set_axisbelow(True)


def panel_letter(ax, letter, x=0.04, y=0.94):
    """Grey-circle panel letter at the top left of an axes."""
    box = dict(LETTER_BOX, lw=s(0.6))
    ax.text(x, y, letter, transform=ax.transAxes, ha="center", va="center",
            fontsize=s(FS), zorder=20, bbox=box)


def num(x, spec="g"):
    """A number for figure text with a true minus sign."""
    return format(x, spec).replace("-", MINUS)


# -- c-axis orientation colours -----------------------------------------------
# Orientation is axial (0 and 180 degrees are the same), so the map is cyclic.
# It runs through the series colours, lightened so basal-plane traces drawn on
# top stay legible, in N_LEVELS discrete bands.
_CYCLE = [RED, ORANGE, "#e5c100", GREEN, BLUE, PURPLE, RED]
_ORIENT_SMOOTH = LinearSegmentedColormap.from_list("orient", _CYCLE)
_LIGHTEN = 0.45


def _lighten(rgb, f=_LIGHTEN):
    rgb = np.asarray(rgb, float)
    out = rgb.copy()
    out[..., :3] = (1 - f) * rgb[..., :3] + f
    return out


ORIENT_BANDS = _lighten(np.array([_ORIENT_SMOOTH((i + 0.5) / N_LEVELS) for i in range(N_LEVELS)]))
ORIENT_CMAP = ListedColormap(ORIENT_BANDS, name="orient_bands")


def orient_color(theta, alpha=1.0):
    """Band colour for a c-axis at angle ``theta`` (radians, axial)."""
    u = (np.asarray(theta, float) % np.pi) / np.pi
    k = np.minimum((u * N_LEVELS).astype(int), N_LEVELS - 1)
    c = ORIENT_BANDS[k].copy()
    c[..., 3] = alpha
    return c


def orient_colorbar(fig, cax, label="c-axis angle (°)"):
    """Discrete-band colour bar for c-axis orientation, 0 to 180 degrees."""
    norm = BoundaryNorm(np.linspace(0, 180, N_LEVELS + 1), N_LEVELS)
    sm = plt.cm.ScalarMappable(norm=norm, cmap=ORIENT_CMAP)
    cb = fig.colorbar(sm, cax=cax)
    cb.set_label(label, rotation=90, labelpad=s(4))
    cb.outline.set_linewidth(s(0.6))
    cb.ax.tick_params(width=s(0.5), length=s(2.5), labelsize=s(FS_TICK))
    cb.set_ticks([0, 45, 90, 135, 180])
    return cb


def nice_ticks(ax, axis="both", n=5):
    loc = lambda: MaxNLocator(n, steps=[1, 2, 2.5, 5, 10])  # noqa: E731
    if axis in ("x", "both"):
        ax.xaxis.set_major_locator(loc())
    if axis in ("y", "both"):
        ax.yaxis.set_major_locator(loc())


# -- output ----------------------------------------------------------------------
_PDF_METADATA = {"CreationDate": None, "Producer": None, "Creator": None}
_PNG_METADATA = {"Software": ""}


def save(fig, path, pad_inches=0.04):
    """PNG at 300 dpi and a vector PDF, with no embedded timestamp."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    for ext, meta in (("png", _PNG_METADATA), ("pdf", _PDF_METADATA)):
        fig.savefig(str(path.with_suffix(f".{ext}")), bbox_inches="tight",
                    pad_inches=pad_inches, metadata=dict(meta))
    plt.close(fig)
    print(f"Saved {path.with_suffix('')}.{{png,pdf}}", flush=True)
