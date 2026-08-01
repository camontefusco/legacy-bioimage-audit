"""
visualization.py

Visualization utilities for the bioimage-host-pathogen-analysis project.

This file saves figures that help you inspect:
- raw microscopy images
- separated fluorescence channels
- segmentation masks
- segmentation overlays

Why this matters:
Bioimage analysis should never be only numbers.
You always need visual quality control to check whether the segmentation makes
biological sense.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from skimage import segmentation


def save_rgb_image(
    image: np.ndarray,
    output_path: str | Path,
    title: str = "RGB microscopy image",
) -> None:
    """
    Save an RGB image as a figure.

    Parameters
    ----------
    image:
        RGB image with shape (height, width, 3).

    output_path:
        Where to save the figure.

    title:
        Figure title.
    """

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(6, 6))
    plt.imshow(image)
    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()


def save_channel_figure(
    channel_image: np.ndarray,
    output_path: str | Path,
    title: str = "Single fluorescence channel",
    cmap: str = "gray",
) -> None:
    """
    Save a single-channel fluorescence image.

    Parameters
    ----------
    channel_image:
        2D image, for example the green/GFP channel.

    output_path:
        Where to save the figure.

    title:
        Figure title.

    cmap:
        Matplotlib color map.
        Use "gray" for neutral visualization.
        Use "Greens" for GFP-like visualization.

    Why this matters
    ----------------
    Looking at individual channels helps verify which biological structures are
    represented by each fluorescence signal.
    """

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(6, 6))
    plt.imshow(channel_image, cmap=cmap)
    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()


def save_binary_mask(
    mask: np.ndarray,
    output_path: str | Path,
    title: str = "Binary segmentation mask",
) -> None:
    """
    Save a binary foreground/background mask.

    Parameters
    ----------
    mask:
        Boolean mask.
        True = detected foreground object.
        False = background.

    output_path:
        Where to save the figure.

    title:
        Figure title.

    Biological interpretation
    -------------------------
    In a GFP bacteria channel, the mask shows which pixels are considered
    bacteria-positive or cluster-positive.
    """

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(6, 6))
    plt.imshow(mask, cmap="gray")
    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()


def save_label_image(
    labels: np.ndarray,
    output_path: str | Path,
    title: str = "Labelled segmented objects",
) -> None:
    """
    Save a label image where each segmented object has a different label.

    Parameters
    ----------
    labels:
        Label image from segmentation.
        0 = background.
        1, 2, 3... = objects.

    output_path:
        Where to save the figure.

    title:
        Figure title.

    Why this matters
    ----------------
    The label image helps you see whether objects are separated correctly.
    This is especially important when bacteria or biofilm-like aggregates touch.
    """

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(6, 6))
    plt.imshow(labels, cmap="nipy_spectral")
    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()


def save_segmentation_overlay(
    image: np.ndarray,
    labels: np.ndarray,
    output_path: str | Path,
    title: str = "Segmentation overlay",
) -> None:
    """
    Save an RGB image with segmentation boundaries overlaid.

    Parameters
    ----------
    image:
        Original RGB image.

    labels:
        Label image from segmentation.

    output_path:
        Where to save the figure.

    title:
        Figure title.

    Why this matters
    ----------------
    This is one of the most important quality-control figures.

    It lets you ask:
    - Are the fluorescent bacteria/objects detected?
    - Are background regions falsely detected?
    - Are clusters over-split or under-split?
    """

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    overlay = segmentation.mark_boundaries(
        image,
        labels,
        mode="outer",
    )

    plt.figure(figsize=(6, 6))
    plt.imshow(overlay)
    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()


def save_feature_histogram(
    values: np.ndarray,
    output_path: str | Path,
    title: str,
    xlabel: str,
    bins: int = 30,
) -> None:
    """
    Save a histogram of extracted object features.

    Parameters
    ----------
    values:
        Numeric values to plot.
        Example: object area, intensity, circularity.

    output_path:
        Where to save the figure.

    title:
        Figure title.

    xlabel:
        Label for the x-axis.

    bins:
        Number of histogram bins.

    Biological interpretation
    -------------------------
    Feature histograms can show whether the image contains:
    - many small objects
    - fewer large clusters
    - heterogeneous bacterial aggregates
    - possible biofilm-like phenotypes
    """

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    values = np.asarray(values)

    plt.figure(figsize=(6, 4))
    plt.hist(values, bins=bins)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()
