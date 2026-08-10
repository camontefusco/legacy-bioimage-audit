# From qualitative observations to quantitative data

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21876822.svg)](https://doi.org/10.5281/zenodo.21876822)

This repository is an open computational learning module for experimental scientists who want to turn qualitative microscopy observations into defensible quantitative variables. Four executable notebooks use deterministic synthetic images and small, declared samples from public microscopy collections to teach measurement design, sensitivity analysis, experimental hierarchy, quality control, and claim restraint.

## Status

This is a teaching module, not a validated biological pipeline, segmentation benchmark, or evaluation of educational effectiveness. Published-image cases deliberately use small teaching samples so that analytical decisions remain inspectable. Their numerical outputs must not be generalized to the full source datasets.

Start with `EXPERIMENTAL_TO_DATA_SCIENCE_GUIDE.md`, then work through the notebooks in numerical order. `EDUCATIONAL_USE_GUIDE.md` provides the module sequence, and `CLAIM_BOUNDARY.md` defines what the exercises do and do not support.

`PUBLICATION_STRATEGY.md` gives the release route. `paper.md` is a transition guide from qualitative experimental observation to quantitative analysis; it makes no claim of educational effectiveness.

The citation-resolved archival report is available at `output/pdf/qualitative-to-quantitative-transition-guide.pdf`. Rebuild and QA instructions are in `REPORT_BUILD.md`.

The immutable `v0.1.0` archive is available from [Zenodo](https://doi.org/10.5281/zenodo.21876822). The current repository includes additional published-image cases developed after that archive.

The optional small-pilot package under `pilot/` includes invitation text, a facilitator guide, a learner worksheet, anonymous feedback prompts, and a session-level results template. Running a pilot is not required for the technical report or archival release.

The notebooks are:

1. `01_educational_sensitivity_analysis.ipynb` — synthetic threshold and object-splitting sensitivity;
2. `02_bbbc039_published_image_transfer.ipynb` — foreground agreement versus object agreement;
3. `03_bbbc050_3d_projection_transfer.ipynb` — central-plane, mean, and maximum projections;
4. `04_bbbc013_multichannel_roles.ipynb` — channel roles and perinuclear region definitions.

They deliberately omit treatment hypothesis tests and predictive modelling.

The notebook runs out of the box on deterministic synthetic teaching images. Thesis-derived panels are not required and remain excluded pending redistribution permission.

Additional published-image transfer exercises have been feasibility-audited in
[`case_studies/`](case_studies/). They are framed as teaching cases, not as
reproductions or biological validation, and no third-party images are bundled.
The first executable transfer case is
[`notebooks/02_bbbc039_published_image_transfer.ipynb`](notebooks/02_bbbc039_published_image_transfer.ipynb).
The second is a 3D-to-2D operationalization exercise using CC BY 3.0 BBBC050:
[`notebooks/03_bbbc050_3d_projection_transfer.ipynb`](notebooks/03_bbbc050_3d_projection_transfer.ipynb).
The third uses paired GFP and DNA channels from CC BY 3.0 BBBC013:
[`notebooks/04_bbbc013_multichannel_roles.ipynb`](notebooks/04_bbbc013_multichannel_roles.ipynb).

## Data

The 12 thesis-derived screenshots are deliberately excluded from this release candidate pending confirmation that they may be redistributed. Their metadata are provided in `data/metadata/metadata_fig34.csv`.

To run the reconstruction locally, place authorized PNG files under:

```text
data/raw_confocal_images/thesis_screenshots/fig34/
```

The filenames must match the metadata file. Copy `metadata_fig34.csv` into the same directory before execution.

The three public-data notebooks include opt-in download scripts. Downloaded third-party data remain under their source licenses and are excluded from version control.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The desktop viewer is optional and is not required for the notebook:

```bash
pip install -r requirements-optional.txt
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

Software code is licensed under the [MIT License](LICENSE). Original instructional prose, notebook narrative, documentation, and synthetic teaching graphics are licensed under [CC BY 4.0](LICENSE-CONTENT.md), except where otherwise noted.

Thesis-derived images are not included and are not covered by either license. The licenses do not convert synthetic panels into biological evidence or relax the interpretation limits documented in `CLAIM_BOUNDARY.md`.
