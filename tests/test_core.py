from __future__ import annotations

from pathlib import Path
import sys

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.run_submission_reconstruction import segment_submission_branch
from src.metrics import summarize_objects
from src.segmentation import (
    decode_color_instance_mask,
    load_grayscale_image,
    load_tiff_stack,
    project_stack,
)


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


def test_load_grayscale_image_preserves_16_bit_values(tmp_path) -> None:
    source = np.array([[0, 256], [4096, 65535]], dtype=np.uint16)
    path = tmp_path / "single_channel.tif"
    Image.fromarray(source).save(path)

    loaded = load_grayscale_image(path)

    assert loaded.dtype == np.uint16
    assert np.array_equal(loaded, source)


def test_load_grayscale_image_rejects_multichannel_input(tmp_path) -> None:
    path = tmp_path / "rgb.png"
    Image.fromarray(np.zeros((3, 4, 3), dtype=np.uint8)).save(path)

    try:
        load_grayscale_image(path)
    except ValueError as exc:
        assert "Select a channel" in str(exc)
    else:
        raise AssertionError("Expected multichannel input to be rejected")


def test_decode_color_instance_mask_labels_connected_foreground() -> None:
    mask = np.zeros((3, 4, 3), dtype=np.uint8)
    mask[0, :2] = [255, 0, 0]
    mask[2, 2:] = [2, 0, 0]

    labels = decode_color_instance_mask(mask)

    assert labels[1, 1] == 0
    assert labels[0, 0] > 0
    assert labels[2, 3] > 0
    assert labels[0, 0] != labels[2, 3]


def test_load_and_project_3d_tiff_stack(tmp_path) -> None:
    import tifffile

    source = np.arange(3 * 4 * 5, dtype=np.uint16).reshape(3, 4, 5)
    path = tmp_path / "stack.tif"
    tifffile.imwrite(path, source, photometric="minisblack")

    loaded = load_tiff_stack(path)

    assert loaded.dtype == np.uint16
    assert np.array_equal(loaded, source)
    assert np.array_equal(project_stack(loaded, "central"), source[1])
    assert np.array_equal(project_stack(loaded, "maximum"), source.max(axis=0))
    assert np.allclose(project_stack(loaded, "mean"), source.mean(axis=0))
