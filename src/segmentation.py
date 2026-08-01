"""
segmentation.py

Core image loading, channel extraction, preprocessing, and segmentation functions.

This file is intentionally simple and commented because it is the foundation of the
bioimage-host-pathogen-analysis project.

Biological idea:
- In your thesis-like workflow, fluorescent bacteria may be visible in the green/GFP channel.
- We extract that channel.
- We remove background/noise.
- We segment fluorescent objects using thresholding + watershed.
"""

from pathlib import Path
from typing import Literal, Tuple

import numpy as np
from PIL import Image
from scipy import ndimage as ndi
from skimage import filters, measure, morphology, segmentation, util


# Restrict allowed channel names.
# This prevents typos like "gren" instead of "green".
ChannelName = Literal["red", "green", "blue"]


def load_image(path: str | Path) -> np.ndarray:
    """
    Load an image file as an RGB NumPy array.

    Parameters
    ----------
    path:
        Path to the microscopy image.

    Returns
    -------
    np.ndarray
        RGB image with shape:
        (height, width, 3)

    Notes
    -----
    For now, this starter project assumes RGB images such as PNG or JPG.
    Later, this can be extended to microscopy formats such as TIFF or CZI.
    """

    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Image not found: {path}")

    image = Image.open(path).convert("RGB")
    return np.asarray(image)


def extract_channel(image: np.ndarray, channel: ChannelName = "green") -> np.ndarray:
    """
    Extract one fluorescence channel from an RGB image.

    Parameters
    ----------
    image:
        RGB image with shape (height, width, 3).

    channel:
        Channel to extract:
        - "red"   = channel 0
        - "green" = channel 1
        - "blue"  = channel 2

    Returns
    -------
    np.ndarray
        Single-channel grayscale image with shape (height, width).

    Biological interpretation
    -------------------------
    For a GFP-labelled bacteria experiment, the green channel can be used
    as a proxy for bacterial burden or bacterial clustering.
    """

    if image.ndim != 3 or image.shape[2] != 3:
        raise ValueError(
            "Expected an RGB image with shape (height, width, 3). "
            f"Received shape: {image.shape}"
        )

    channel_map = {
        "red": 0,
        "green": 1,
        "blue": 2,
    }

    return image[..., channel_map[channel]]


def preprocess_channel(
    channel_image: np.ndarray,
    gaussian_sigma: float = 1.0,
    background_radius: int = 30,
) -> np.ndarray:
    """
    Denoise and background-correct a single-channel microscopy image.

    Parameters
    ----------
    channel_image:
        Single-channel image, for example the green/GFP channel.

    gaussian_sigma:
        Strength of Gaussian smoothing.
        Higher values reduce noise more, but may blur small bacteria.

    background_radius:
        Radius used for morphological background estimation.
        Larger values estimate broader background variation.

    Returns
    -------
    np.ndarray
        Background-corrected image normalized between 0 and 1.

    Why this matters
    ----------------
    Microscopy images often contain:
    - uneven illumination
    - autofluorescence
    - camera noise
    - background signal

    If we segment without correction, we may count background as bacteria.
    """

    if channel_image.ndim != 2:
        raise ValueError(
            "Expected a 2D single-channel image. "
            f"Received shape: {channel_image.shape}"
        )

    # Convert image to float in the range 0 to 1.
    channel_float = util.img_as_float(channel_image)

    # Smooth small pixel-level noise.
    smoothed = filters.gaussian(channel_float, sigma=gaussian_sigma)

    # Estimate slow-varying background using morphological opening.
    # This behaves somewhat like a simple rolling-ball background correction.
    background = morphology.opening(
        smoothed,
        morphology.disk(background_radius),
    )

    # Subtract background and avoid negative values.
    corrected = smoothed - background
    corrected = np.clip(corrected, 0, None)

    # Normalize to 0-1 so thresholds are easier to interpret.
    if corrected.max() > 0:
        corrected = corrected / corrected.max()

    return corrected


def segment_objects(
    channel_image: np.ndarray,
    min_size: int = 12,
    gaussian_sigma: float = 1.0,
    background_radius: int = 30,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Segment fluorescent objects using thresholding and watershed.

    Parameters
    ----------
    channel_image:
        Single-channel fluorescence image.

    min_size:
        Minimum object size in pixels.
        Smaller detected objects are removed as likely noise.

    gaussian_sigma:
        Smoothing parameter passed to preprocessing.

    background_radius:
        Background correction parameter passed to preprocessing.

    Returns
    -------
    mask:
        Binary foreground mask.
        True = likely fluorescent object.

    labels:
        Label image where each object has a unique integer:
        0 = background
        1, 2, 3... = individual segmented objects

    Biological interpretation
    -------------------------
    In a GFP bacteria image, each labelled object may represent:
    - a single bacterium
    - a bacterial aggregate
    - a biofilm-like cluster

    This depends on image resolution and segmentation settings.
    """

    corrected = preprocess_channel(
        channel_image,
        gaussian_sigma=gaussian_sigma,
        background_radius=background_radius,
    )

    # Otsu automatically chooses a threshold separating foreground/background.
    threshold = filters.threshold_otsu(corrected)
    mask = corrected > threshold

    # Remove tiny speckles that are unlikely to be real objects.
    mask = morphology.remove_small_objects(mask, min_size=min_size)

    # Close small gaps inside objects.
    mask = morphology.binary_closing(mask, morphology.disk(1))

    # Distance transform helps separate touching objects.
    distance = ndi.distance_transform_edt(mask)

    # Find approximate object centers.
    local_maxima = morphology.local_maxima(distance)
    markers = measure.label(local_maxima)

    # Watershed separates connected objects based on distance peaks.
    labels = segmentation.watershed(
        -distance,
        markers,
        mask=mask,
    )

    return mask, labels
