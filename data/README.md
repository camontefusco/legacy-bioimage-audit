# Data availability

Run `python scripts/generate_synthetic_panels.py` to create 12 deterministic, redistributable fluorescence-like teaching images under `data/synthetic_panels/`. They teach image-analysis mechanics and have no biological interpretation. The educational notebook creates them automatically when needed.

Published-image transfer exercises are scoped in
`case_studies/case_study_manifest.csv`. Third-party images are deliberately not
bundled with this repository; the manifest records authoritative sources,
licenses, scale, and required adapters.

## Restricted historical inputs

`metadata/metadata_fig34.csv` describes the 12 Figure 34 panels used in the historical analysis.

The corresponding PNG files are not included in this release candidate because redistribution permission has not been confirmed. They remain excluded by `.gitignore` even when present locally.

The inputs are cropped, post-processed thesis figure panels—not raw confocal acquisitions. They lack sufficient acquisition metadata for calibrated quantitative fluorescence analysis.
