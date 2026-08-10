import numpy as np

from src.sensitivity import SensitivityConfig, mask_iou, segment_with_config


def test_mask_iou_identity_and_disjoint():
    a = np.array([[True, False], [False, True]])
    b = np.array([[False, True], [True, False]])
    assert mask_iou(a, a) == 1.0
    assert mask_iou(a, b) == 0.0


def test_segment_with_config_returns_consistent_shapes():
    image = np.zeros((64, 64), dtype=float)
    image[20:40, 20:40] = 1.0
    config = SensitivityConfig("test", 1.0, 5, "percentile", 90, 5, 1)
    corrected, mask, labels, threshold = segment_with_config(image, config)
    assert corrected.shape == image.shape
    assert mask.shape == image.shape
    assert labels.shape == image.shape
    assert np.isfinite(threshold)

