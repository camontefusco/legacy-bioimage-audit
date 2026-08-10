"""Small helpers for educational multichannel measurement exercises."""

from __future__ import annotations

import numpy as np
from skimage import morphology


def nuclear_perinuclear_summary(
    signal: np.ndarray,
    nuclear_labels: np.ndarray,
    ring_radius: int,
) -> dict[str, float]:
    """Summarize signal in a nuclear mask and an adjacent exterior ring.

    This is an operational measurement, not a validated translocation assay.
    """

    if signal.ndim != 2 or nuclear_labels.ndim != 2:
        raise ValueError("signal and nuclear_labels must both be 2D")
    if signal.shape != nuclear_labels.shape:
        raise ValueError("signal and nuclear_labels must have matching shapes")
    if ring_radius < 1:
        raise ValueError("ring_radius must be at least 1 pixel")

    nuclei = nuclear_labels > 0
    ring = morphology.binary_dilation(nuclei, morphology.disk(ring_radius)) & ~nuclei
    nuclear_mean = float(signal[nuclei].mean()) if nuclei.any() else float("nan")
    ring_mean = float(signal[ring].mean()) if ring.any() else float("nan")
    ratio = nuclear_mean / ring_mean if ring_mean > 0 else float("nan")
    return {
        "nuclear_mean_signal": nuclear_mean,
        "perinuclear_mean_signal": ring_mean,
        "nuclear_to_perinuclear_ratio": ratio,
        "nuclear_fraction": float(nuclei.mean()),
        "perinuclear_fraction": float(ring.mean()),
    }
