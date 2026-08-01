# Analysis branches and manuscript implications

## Submitted-analysis reconstruction

The JMM manuscript's numerical claims come from `04_quantification_backup.ipynb`. That notebook uses:

- green-channel extraction;
- Gaussian smoothing and morphological-opening background correction;
- an additional Gaussian smoothing pass;
- the 90th percentile of each processed image as the threshold;
- removal of objects smaller than 80 pixels;
- binary closing with a radius-2 disk;
- connected-component labeling.

It does **not** use Otsu thresholding or watershed separation for the table underlying the submitted claims. The manuscript methods therefore do not accurately describe the submitted numerical analysis.

The reproducible reconstruction is `scripts/run_submission_reconstruction.py`. It writes new outputs under `results/regenerated_submission/` and preserves all historical files.

## Later batch-pipeline candidate

`05_multi_image_pipeline.ipynb` calls `src.segmentation.segment_objects` with `min_size=8`, `gaussian_sigma=0.8`, and `background_radius=25`. That implementation uses Otsu thresholding and watershed separation.

This branch reproduces its own archived CSVs byte-for-byte, but it does not reproduce the submitted manuscript results. Compared with the submitted branch, it produces substantially different foreground fractions, object counts, morphology metrics, and treated intensity–area regression.

## Consequence

Neither branch should silently replace the other. For provenance:

- use the submitted branch to reconstruct what was reported;
- use the batch branch only as a separately labeled candidate method;
- do not combine tables or claims across branches;
- do not publish the current manuscript methods as a description of the submitted branch.

For a new scientific submission, the segmentation method must be selected through validation against manually annotated raw images or another defensible reference—not because one branch yields a more attractive result.
