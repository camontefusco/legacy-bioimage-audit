from __future__ import annotations

from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.run_submission_reconstruction import segment_submission_branch
from src.metrics import summarize_objects


def test_metadata_describes_twelve_panels() -> None:
    import pandas as pd

    metadata = pd.read_csv(ROOT / "data" / "metadata" / "metadata_fig34.csv")
    assert metadata["panel"].tolist() == list("ABCDEFGHIJKL")
    assert metadata["file_name"].is_unique


def test_submission_segmentation_is_deterministic_on_synthetic_image() -> None:
    y, x = np.ogrid[:256, :256]
    image = np.zeros((256, 256), dtype=float)
    image[(x - 80) ** 2 + (y - 100) ** 2 < 18**2] = 0.8
    image[(x - 175) ** 2 + (y - 150) ** 2 < 25**2] = 1.0

    mask_1, labels_1, threshold_1 = segment_submission_branch(image)
    mask_2, labels_2, threshold_2 = segment_submission_branch(image)

    assert np.array_equal(mask_1, mask_2)
    assert np.array_equal(labels_1, labels_2)
    assert threshold_1 == threshold_2


def test_summary_geometry_is_internally_consistent() -> None:
    labels = np.zeros((20, 20), dtype=int)
    labels[2:7, 2:7] = 1
    labels[10:18, 11:16] = 2
    channel = np.ones((20, 20), dtype=float)
    summary = summarize_objects(channel, labels).iloc[0]

    assert summary["n_objects"] == 2
    assert summary["positive_area_px"] == 65
    assert summary["positive_area_fraction"] == 65 / 400
    assert summary["total_positive_intensity"] == 65
