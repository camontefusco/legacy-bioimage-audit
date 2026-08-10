"""Educational sensitivity-analysis helpers for rendered microscopy panels.

These functions compare analytical configurations on illustrative panels. They
do not estimate treatment effects or segmentation accuracy.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass

import numpy as np
from scipy import ndimage as ndi
from skimage import filters, measure, morphology, segmentation

from src.metrics import summarize_objects
from src.segmentation import preprocess_channel


@dataclass(frozen=True)
class SensitivityConfig:
    name: str
    gaussian_sigma: float
    background_radius: int
    threshold_method: str
    threshold_value: float | None
    min_size: int
    closing_radius: int
    split_method: str = "connected_components"


def default_educational_configs() -> list[SensitivityConfig]:
    """Return a compact set of deliberately contrasting configurations."""
    return [
        SensitivityConfig("percentile_85", 1.5, 50, "percentile", 85, 80, 2),
        SensitivityConfig("submitted_branch", 1.5, 50, "percentile", 90, 80, 2),
        SensitivityConfig("percentile_95", 1.5, 50, "percentile", 95, 80, 2),
        SensitivityConfig("small_objects_retained", 1.5, 50, "percentile", 90, 12, 2),
        SensitivityConfig("large_objects_only", 1.5, 50, "percentile", 90, 200, 2),
        SensitivityConfig("lighter_smoothing", 0.5, 30, "percentile", 90, 80, 1),
        SensitivityConfig("stronger_smoothing", 2.0, 50, "percentile", 90, 80, 2),
        SensitivityConfig("otsu_components", 1.0, 30, "otsu", None, 12, 1),
        SensitivityConfig("otsu_watershed", 1.0, 30, "otsu", None, 12, 1, "watershed"),
    ]


def segment_with_config(channel: np.ndarray, config: SensitivityConfig):
    corrected = preprocess_channel(
        channel,
        gaussian_sigma=config.gaussian_sigma,
        background_radius=config.background_radius,
    )
    if config.name in {"percentile_85", "submitted_branch", "percentile_95", "small_objects_retained", "large_objects_only", "lighter_smoothing", "stronger_smoothing"}:
        corrected = filters.gaussian(corrected, sigma=1)
    if config.threshold_method == "percentile":
        threshold = float(np.percentile(corrected, config.threshold_value))
    elif config.threshold_method == "otsu":
        threshold = float(filters.threshold_otsu(corrected))
    else:
        raise ValueError(f"Unsupported threshold method: {config.threshold_method}")

    mask = corrected > threshold
    mask = morphology.remove_small_objects(mask, min_size=config.min_size)
    if config.closing_radius > 0:
        mask = morphology.binary_closing(mask, morphology.disk(config.closing_radius))

    if config.split_method == "connected_components":
        labels = measure.label(mask)
    elif config.split_method == "watershed":
        distance = ndi.distance_transform_edt(mask)
        markers = measure.label(morphology.local_maxima(distance))
        labels = segmentation.watershed(-distance, markers, mask=mask)
    else:
        raise ValueError(f"Unsupported split method: {config.split_method}")
    return corrected, mask, labels, threshold


def mask_iou(mask_a: np.ndarray, mask_b: np.ndarray) -> float:
    """Intersection over union; this measures agreement, not accuracy."""
    union = np.logical_or(mask_a, mask_b).sum()
    if union == 0:
        return 1.0
    return float(np.logical_and(mask_a, mask_b).sum() / union)


def summarize_configuration(channel: np.ndarray, config: SensitivityConfig) -> dict:
    _, mask, labels, threshold = segment_with_config(channel, config)
    row = summarize_objects(channel, labels).iloc[0].to_dict()
    row.update(asdict(config))
    row["threshold"] = threshold
    row["foreground_fraction"] = float(mask.mean())
    return row

