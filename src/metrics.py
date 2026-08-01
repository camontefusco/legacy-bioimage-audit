"""
metrics.py

Feature extraction and quantification utilities.

This file turns segmented microscopy objects into structured data tables.

Main idea:
image -> segmentation labels -> object-level features -> image-level summary

Why this matters:
These tables can later be used for:
- statistical analysis
- treatment comparison
- predictive modeling
- infection severity classification
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from skimage import measure


def object_features(
    channel_image: np.ndarray,
    labels: np.ndarray,
) -> pd.DataFrame:
    """
    Extract one row of features per segmented object.

    Parameters
    ----------
    channel_image:
        Single-channel image used for intensity measurements.
        Example: green/GFP bacteria channel.

    labels:
        Label image from segmentation.
        0 = background
        1, 2, 3... = segmented objects.

    Returns
    -------
    pd.DataFrame
        Table where each row is one segmented object.

    Biological interpretation
    -------------------------
    Each object may correspond to:
    - one bacterium
    - one bacterial cluster
    - one biofilm-like aggregate

    depending on image resolution and segmentation settings.
    """

    if channel_image.ndim != 2:
        raise ValueError(
            "Expected channel_image to be 2D. "
            f"Received shape: {channel_image.shape}"
        )

    if labels.ndim != 2:
        raise ValueError(
            "Expected labels to be 2D. "
            f"Received shape: {labels.shape}"
        )

    if channel_image.shape != labels.shape:
        raise ValueError(
            "channel_image and labels must have the same height and width. "
            f"Received {channel_image.shape} and {labels.shape}"
        )

    props = measure.regionprops_table(
        labels,
        intensity_image=channel_image,
        properties=[
            "label",
            "area",
            "bbox",
            "centroid",
            "eccentricity",
            "equivalent_diameter",
            "mean_intensity",
            "max_intensity",
            "min_intensity",
            "perimeter",
            "solidity",
        ],
    )

    df = pd.DataFrame(props)

    if df.empty:
        return df

    # Circularity close to 1 = round object.
    # Lower circularity = elongated or irregular object.
    df["circularity"] = (
        4 * np.pi * df["area"] / np.maximum(df["perimeter"] ** 2, 1e-8)
    )

    # A simple proxy for total fluorescence signal per object.
    # For GFP bacteria, this may approximate bacterial fluorescence burden.
    df["integrated_intensity"] = df["area"] * df["mean_intensity"]

    return df


def summarize_objects(
    channel_image: np.ndarray,
    labels: np.ndarray,
) -> pd.DataFrame:
    """
    Create image-level summary metrics from segmented objects.

    Parameters
    ----------
    channel_image:
        Single-channel image, for example the green/GFP channel.

    labels:
        Label image from segmentation.

    Returns
    -------
    pd.DataFrame
        One-row table summarizing the whole image.

    Example outputs
    ---------------
    - number of objects
    - total positive area
    - positive area fraction
    - mean object area
    - mean fluorescence intensity
    - mean circularity

    Biological interpretation
    -------------------------
    These metrics can become approximate readouts for:
    - bacterial burden
    - bacterial clustering
    - biofilm-like coverage
    - infection intensity
    """

    features = object_features(channel_image, labels)
    positive_pixels = labels > 0

    summary = {
        "n_objects": int(features.shape[0]),
        "positive_area_px": int(positive_pixels.sum()),
        "positive_area_fraction": float(positive_pixels.mean()),
    }

    if positive_pixels.any():
        summary["total_positive_intensity"] = float(channel_image[positive_pixels].sum())
        summary["mean_positive_intensity"] = float(channel_image[positive_pixels].mean())
        summary["max_positive_intensity"] = float(channel_image[positive_pixels].max())
    else:
        summary["total_positive_intensity"] = 0.0
        summary["mean_positive_intensity"] = 0.0
        summary["max_positive_intensity"] = 0.0

    if not features.empty:
        summary["mean_object_area"] = float(features["area"].mean())
        summary["median_object_area"] = float(features["area"].median())
        summary["max_object_area"] = float(features["area"].max())
        summary["mean_circularity"] = float(features["circularity"].mean())
        summary["mean_solidity"] = float(features["solidity"].mean())
        summary["mean_integrated_intensity"] = float(
            features["integrated_intensity"].mean()
        )
        summary["total_integrated_intensity"] = float(
            features["integrated_intensity"].sum()
        )
    else:
        summary["mean_object_area"] = 0.0
        summary["median_object_area"] = 0.0
        summary["max_object_area"] = 0.0
        summary["mean_circularity"] = 0.0
        summary["mean_solidity"] = 0.0
        summary["mean_integrated_intensity"] = 0.0
        summary["total_integrated_intensity"] = 0.0

    return pd.DataFrame([summary])


def add_image_metadata(
    summary_df: pd.DataFrame,
    image_id: str,
    condition: str | None = None,
    treatment: str | None = None,
    timepoint: str | None = None,
) -> pd.DataFrame:
    """
    Add experimental metadata to an image-level summary table.

    Parameters
    ----------
    summary_df:
        One-row summary table from summarize_objects().

    image_id:
        Name or ID of the image.

    condition:
        Experimental condition.
        Example: "infected", "uninfected", "co_culture".

    treatment:
        Treatment condition.
        Example: "untreated", "tobramycin".

    timepoint:
        Experimental timepoint.
        Example: "3h", "6h".

    Returns
    -------
    pd.DataFrame
        Summary table with metadata columns added first.

    Why this matters
    ----------------
    Predictive modeling needs both:
    - features: image-derived numeric measurements
    - labels/metadata: condition, treatment, timepoint, etc.
    """

    df = summary_df.copy()

    df.insert(0, "image_id", image_id)

    if condition is not None:
        df.insert(1, "condition", condition)

    if treatment is not None:
        insert_position = min(2, len(df.columns))
        df.insert(insert_position, "treatment", treatment)

    if timepoint is not None:
        insert_position = min(3, len(df.columns))
        df.insert(insert_position, "timepoint", timepoint)

    return df
