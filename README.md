# Host–pathogen microscopy analysis: submission reconstruction

This repository candidate reconstructs the image-analysis branch used to generate numerical results for the manuscript submitted as JMM `MIMET-D-26-00638`. Its intended future use is as a historical reconstruction and educational case study based on 12 rendered thesis panels.

## Status

This is a provenance and methods-recovery package. It is **not** a validated biological treatment-effect pipeline. The original analysis used 12 cropped thesis figure panels, one per experimental condition, without independent biological replication or raw acquisition metadata.

The thesis caption states that the underlying experiment included two images per sample from three independent experiments. Those original Leica SP8 acquisitions and their sample mapping have not yet been recovered. Depending on how the caption's sampling statement applies across the 12 conditions, the complete collection may contain up to 72 acquisitions; that is a recovery hypothesis, not a confirmed sample count.

The repository intentionally separates:

- the submitted 90th-percentile connected-component analysis;
- a later Otsu/watershed batch pipeline that produced materially different results.

See `ANALYSIS_BRANCHES.md` and `MANUSCRIPT_CODE_RECONCILIATION.md` before interpreting any output.

Also read `DATA_PROVENANCE.md` for the exact data boundary and `LICENSE_PENDING.md` before copying or distributing the package.

For teaching use, start with `EDUCATIONAL_USE_GUIDE.md`. `CLAIM_BOUNDARY.md` defines the statements that the available evidence does and does not support.

`PUBLICATION_STRATEGY.md` gives the release and journal-submission route. `paper.md` is a JOSE-oriented manuscript skeleton; it deliberately identifies the missing teaching pilot instead of claiming educational effectiveness prematurely.

The executable teaching notebook is `notebooks/01_educational_sensitivity_analysis.ipynb`. It compares analysis configurations panel by panel and deliberately omits treatment hypothesis tests and predictive modeling.

The notebook runs out of the box on deterministic synthetic teaching images. Thesis-derived panels are not required and remain excluded pending redistribution permission.

## Data

The 12 thesis-derived screenshots are deliberately excluded from this release candidate pending confirmation that they may be redistributed. Their metadata are provided in `data/metadata/metadata_fig34.csv`.

To run the reconstruction locally, place authorized PNG files under:

```text
data/raw_confocal_images/thesis_screenshots/fig34/
```

The filenames must match the metadata file. Copy `metadata_fig34.csv` into the same directory before execution.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Reconstruct the submitted branch

```bash
python scripts/run_submission_reconstruction.py
```

New outputs are written to `results/regenerated_submission/`. Historical submission files are not overwritten.

## Tests

```bash
pytest -q
```

## Interpretation boundary

This code can document what was done and help design a future validated study. It cannot turn screenshot panels into biological replicates, recover missing acquisition controls, establish bacterial viability or clearance, or validate segmentation accuracy.

## Licensing

No license has yet been selected. This private release candidate is currently all rights reserved. Do not publish it until code licensing, image redistribution, contributor attribution, and data-use terms have been confirmed.
