"""Create the compact BBBC039 published-image transfer notebook."""

from __future__ import annotations

from pathlib import Path

import nbformat as nbf


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "notebooks" / "02_bbbc039_published_image_transfer.ipynb"


def markdown(text: str):
    return nbf.v4.new_markdown_cell(text.strip())


def code(text: str):
    return nbf.v4.new_code_cell(text.strip())


def main() -> None:
    notebook = nbf.v4.new_notebook()
    notebook["metadata"]["kernelspec"] = {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3",
    }
    notebook["metadata"]["language_info"] = {"name": "python", "version": "3"}
    notebook["cells"] = [
        markdown(
            """
# Published-image transfer case: BBBC039 nuclei

This exercise asks whether the **analysis mechanics** from the synthetic module
transfer to a published microscopy dataset. It does not reproduce the source
publication, estimate a drug effect, or validate a biological claim.

BBBC039 contains 200 single-channel, 16-bit fluorescence images of U2OS nuclei
and manually created instance masks. The dataset is CC0. Cite BBBC039 and the
Broad Bioimage Benchmark Collection when using it.

Source: https://bbbc.broadinstitute.org/BBBC039
"""
        ),
        markdown(
            """
## Learning objectives

After this exercise, a learner should be able to:

1. preserve intensity bit depth when loading microscopy images;
2. distinguish foreground-mask agreement from biological validity;
3. show how threshold and object-splitting choices alter measurements; and
4. keep image-level observations separate from treatment-level inference.
"""
        ),
        code(
            """
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

ROOT = Path.cwd()
if ROOT.name == "notebooks":
    ROOT = ROOT.parent
sys.path.insert(0, str(ROOT))

from src.segmentation import decode_color_instance_mask, load_grayscale_image
from src.sensitivity import SensitivityConfig, mask_iou, segment_with_config

DATA = ROOT / "data" / "external" / "BBBC039"
if not (DATA / "images").exists():
    raise FileNotFoundError(
        "BBBC039 is not present. From the repository root run: "
        "python scripts/download_bbbc039.py"
    )
"""
        ),
        markdown(
            """
## Select a small, declared sample

We use the first three filenames in the official **training** split. This is a
teaching sample, not a random sample of treatments and not an experimental
replicate structure. The validation and test splits remain untouched.
"""
        ),
        code(
            """
training_names = [
    line.strip() for line in (DATA / "metadata" / "training.txt").read_text().splitlines()
    if line.strip()
]
selected = training_names[:3]

records = []
for mask_name in selected:
    stem = Path(mask_name).stem
    image = load_grayscale_image(DATA / "images" / f"{stem}.tif")
    mask_rgba = np.asarray(Image.open(DATA / "masks" / mask_name))
    reference_labels = decode_color_instance_mask(mask_rgba)
    records.append({
        "image_id": stem,
        "image": image,
        "reference_labels": reference_labels,
    })

pd.DataFrame([
    {
        "image_id": row["image_id"],
        "shape": str(row["image"].shape),
        "dtype": str(row["image"].dtype),
        "intensity_min": int(row["image"].min()),
        "intensity_max": int(row["image"].max()),
        "derived_reference_objects": int(row["reference_labels"].max()),
    }
    for row in records
])
"""
        ),
        code(
            """
fig, axes = plt.subplots(len(records), 2, figsize=(10, 10))
for row_index, row in enumerate(records):
    axes[row_index, 0].imshow(row["image"], cmap="gray")
    axes[row_index, 0].set_title(f"16-bit image {row_index + 1}")
    axes[row_index, 1].imshow(row["reference_labels"], cmap="nipy_spectral")
    axes[row_index, 1].set_title("Derived reference instances")
    for axis in axes[row_index]:
        axis.axis("off")
plt.tight_layout()
"""
        ),
        markdown(
            """
## Operational comparison

The four configurations deliberately vary thresholding and splitting. Mask IoU
measures overlap with the published foreground mask. It is an **agreement
measure**, not proof that either mask represents biological truth.
"""
        ),
        code(
            """
configs = [
    SensitivityConfig("percentile_90", 1.0, 30, "percentile", 90, 40, 1),
    SensitivityConfig("percentile_95", 1.0, 30, "percentile", 95, 40, 1),
    SensitivityConfig("otsu_components", 1.0, 30, "otsu", None, 40, 1),
    SensitivityConfig("otsu_watershed", 1.0, 30, "otsu", None, 40, 1, "watershed"),
]

results = []
segmentations = {}
for row in records:
    reference_foreground = row["reference_labels"] > 0
    for config in configs:
        corrected, predicted_mask, predicted_labels, threshold = segment_with_config(
            row["image"], config
        )
        key = (row["image_id"], config.name)
        segmentations[key] = predicted_labels
        results.append({
            "image_id": row["image_id"],
            "configuration": config.name,
            "threshold": threshold,
            "mask_iou_agreement": mask_iou(predicted_mask, reference_foreground),
            "derived_reference_objects": int(row["reference_labels"].max()),
            "predicted_objects": int(predicted_labels.max()),
            "object_count_difference": int(predicted_labels.max() - row["reference_labels"].max()),
            "predicted_foreground_fraction": float(predicted_mask.mean()),
            "reference_foreground_fraction": float(reference_foreground.mean()),
        })

results_df = pd.DataFrame(results)
results_df.round(4)
"""
        ),
        code(
            """
summary = (
    results_df.groupby("configuration", as_index=False)
    .agg(
        mean_mask_iou_agreement=("mask_iou_agreement", "mean"),
        mean_object_count_difference=("object_count_difference", "mean"),
        mean_predicted_foreground_fraction=("predicted_foreground_fraction", "mean"),
    )
)
summary.round(4)
"""
        ),
        code(
            """
example = records[0]
fig, axes = plt.subplots(1, 2 + len(configs), figsize=(18, 4))
axes[0].imshow(example["image"], cmap="gray")
axes[0].set_title("Input")
axes[1].imshow(example["reference_labels"], cmap="nipy_spectral")
axes[1].set_title("Derived reference")
for index, config in enumerate(configs, start=2):
    axes[index].imshow(
        segmentations[(example["image_id"], config.name)], cmap="nipy_spectral"
    )
    axes[index].set_title(config.name.replace("_", "\\n"))
for axis in axes:
    axis.axis("off")
plt.tight_layout()
"""
        ),
        markdown(
            """
## Interpretation exercise

Write one sentence for each prompt:

1. Which configuration agrees most closely with the published foreground mask?
2. Does the same configuration also recover a similar object count?
3. Which analytical decision appears most consequential in these examples?
4. What additional evidence would be needed before making a biological claim?

An acceptable conclusion is limited to these images and configurations, for
example: *foreground overlap and object counts changed with threshold and
splitting choices*. Do not infer compound effects, segmentation generalization,
or biological mechanisms from this three-image teaching sample.
"""
        ),
    ]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    nbf.write(notebook, OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    main()
