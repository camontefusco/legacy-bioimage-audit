# JMM manuscript-to-code reconciliation

## Executive finding

The submitted manuscript does not consistently describe the code that produced its numerical results. Its central numbers trace to the Notebook 04 percentile-threshold branch, while the Methods section describes parameters and operations from the later `src.segmentation` Otsu/watershed branch.

This is a substantive reproducibility problem, not merely a wording issue.

## Reconciliation matrix

| Submitted element | What the submitted text says | What generated the reported values | Required correction |
|---|---|---|---|
| Preprocessing | Gaussian sigma 1.0; background radius 30 | Sigma 1.5, background radius 50, followed by another Gaussian sigma 1 pass | Report the actual parameters or rerun a prospectively selected method. |
| Threshold | Otsu | Per-image 90th percentile of the processed green channel | Replace the Methods description if reconstructing the submission. |
| Minimum object size | 12 pixels | 80 pixels | Correct the threshold and justify it through sensitivity analysis or validation. |
| Object separation | Distance transform and watershed | Binary closing followed by connected-component labeling; no watershed in the submitted branch | Remove the watershed claim for the submitted results. |
| “30–84 objects” and area fraction 0.060–0.093 | Presented as outputs of the Otsu/watershed workflow | These values come from the 90th-percentile branch | Tie these values only to the submitted branch. |
| Treated intensity–area R² ≈ 0.01 | Presented as a biological treatment phenotype | Reconstructed value is 0.0089; the later Otsu/watershed branch gives 0.359 | The effect is method-dependent and cannot support a robust biological claim without segmentation validation. |
| Untreated slope ≈ 505 and R² ≈ 0.89 | Presented as a stable quantitative result | Archived table gives slope 505.2/R² 0.890; current code reconstruction gives slope 523.7/R² 0.900 | Preserve the archived value only as historical provenance; regenerate final values from a locked environment and code revision. |
| “Mean object area rose from approximately 243 to 349 pixels” | Described as a change in mean object area | 243.1 and 349.4 are treatment-group **medians of per-image mean object area**, not means | Correct the summary statistic and wording. |
| “Maximum object area from approximately 1639 to 7731 pixels” | Presented as a treatment-group change | 1639.5 is the untreated group median of per-image maxima; 7731 is a single treated image maximum | Do not compare a group median with a single extreme value. Report consistent summaries and all observations. |
| Random forest importance | Used to support morphology ranking | Twelve images; training score 1.0; cross-validation ≈0.42 | Remove from inferential claims. At most retain as a documented failed exploratory analysis. |
| Reproducibility statement | Code would be deposited before acceptance | Code existed but no exact public analysis package was linked | Provide a versioned repository and release DOI only after branch reconciliation and data-sharing review. |

## Statistical-unit problem

Each condition has one screenshot-derived image. Grouping six untreated and six treated images does not create biological replication because cell model and timepoint are simultaneously changing. The Mann–Whitney tests and regressions operate on heterogeneous condition panels and cannot isolate a treatment effect.

## Safe use of the recovered analysis

The recovered material can support:

- transparent reconstruction of what was submitted;
- a portfolio or teaching example about image-analysis provenance;
- planning a validated pipeline for raw microscopy data.

It should not currently support claims that tobramycin causes aggregation, changes bacterial clearance, or biologically decouples GFP intensity from burden.

## Recommended manuscript decision

Do not revise the present paper by merely substituting one segmentation branch for the other. Obtain raw images and replication, validate the segmentation against annotations or a defensible comparator, define the experimental unit, then regenerate all claims. If raw data cannot be obtained, reframe the work as a transparent proof-of-concept with no treatment-effect inference.
