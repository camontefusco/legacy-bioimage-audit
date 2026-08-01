#!/usr/bin/env python3
"""Reconstruct the analysis branch used for the submitted JMM manuscript.

This intentionally follows Notebook 04: 90th-percentile thresholding, small-object
removal, binary closing, and connected-component labeling. It does not call the
later Otsu/watershed implementation used by Notebook 05.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

import numpy as np
import pandas as pd
from scipy.stats import kruskal, mannwhitneyu
from sklearn.linear_model import LinearRegression
from skimage import filters, measure
from skimage.morphology import closing, disk, remove_small_objects


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.metrics import summarize_objects  # noqa: E402
from src.segmentation import extract_channel, load_image, preprocess_channel  # noqa: E402


RAW_DIR = PROJECT_ROOT / "data" / "raw_confocal_images" / "thesis_screenshots" / "fig34"
OUT_DIR = PROJECT_ROOT / "results" / "regenerated_submission"


def segment_submission_branch(green: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
    preprocessed = preprocess_channel(green, gaussian_sigma=1.5, background_radius=50)
    preprocessed = filters.gaussian(preprocessed, sigma=1)
    threshold = float(np.percentile(preprocessed, 90))
    mask = preprocessed > threshold
    mask = remove_small_objects(mask, min_size=80)
    mask = closing(mask, disk(2))
    labels = measure.label(mask)
    return mask, labels, threshold


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    metadata = pd.read_csv(RAW_DIR / "metadata_fig34.csv")
    rows: list[pd.DataFrame] = []

    for _, record in metadata.iterrows():
        image = load_image(RAW_DIR / record["file_name"])
        green = extract_channel(image, channel="green")
        mask, labels, threshold = segment_submission_branch(green)
        summary = summarize_objects(green, labels)
        for column in metadata.columns:
            summary[column] = record[column]
        summary["threshold"] = threshold
        summary["foreground_fraction"] = float(mask.mean())
        summary["segmentation_method"] = "90th_percentile_threshold"
        rows.append(summary)

    data = pd.concat(rows, ignore_index=True)
    data["normalized_intensity"] = (
        data["total_positive_intensity"] / data["positive_area_px"].replace(0, np.nan)
    )
    data.to_csv(OUT_DIR / "fig34_image_level_quantification.csv", index=False)

    metrics = [
        "positive_area_fraction",
        "total_positive_intensity",
        "normalized_intensity",
        "max_object_area",
        "mean_object_area",
    ]
    mw_rows = []
    for metric in metrics:
        untreated = data.loc[data["treatment"] == "untreated", metric]
        treated = data.loc[data["treatment"] == "tobramycin", metric]
        statistic, p_value = mannwhitneyu(untreated, treated, alternative="two-sided")
        mw_rows.append({"metric": metric, "statistic": statistic, "p_value": p_value})
    pd.DataFrame(mw_rows).to_csv(OUT_DIR / "mann_whitney_tests.csv", index=False)

    kw_rows = []
    for metric in metrics:
        groups = [group[metric].dropna() for _, group in data.groupby("cell_model")]
        statistic, p_value = kruskal(*groups)
        kw_rows.append({"metric": metric, "statistic": statistic, "p_value": p_value})
    pd.DataFrame(kw_rows).to_csv(OUT_DIR / "kruskal_cell_model_tests.csv", index=False)

    regressions = {}
    for treatment, subset in data.groupby("treatment"):
        x = subset[["positive_area_px"]]
        y = subset["total_positive_intensity"]
        model = LinearRegression().fit(x, y)
        regressions[treatment] = {
            "n_images": int(len(subset)),
            "slope": float(model.coef_[0]),
            "r_squared": float(model.score(x, y)),
        }

    claims = {
        "analysis_branch": "submitted_notebook_04_reconstruction",
        "n_images": int(len(data)),
        "area_fraction_min": float(data["positive_area_fraction"].min()),
        "area_fraction_max": float(data["positive_area_fraction"].max()),
        "mean_object_area_overall": float(data["mean_object_area"].mean()),
        "maximum_object_area_overall": float(data["max_object_area"].max()),
        "regressions": regressions,
    }
    (OUT_DIR / "claim_metrics.json").write_text(json.dumps(claims, indent=2) + "\n")
    print(json.dumps(claims, indent=2))


if __name__ == "__main__":
    main()
