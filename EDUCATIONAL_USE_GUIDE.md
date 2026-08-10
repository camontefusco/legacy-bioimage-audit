# Educational use guide

## Purpose

This repository is a small-data teaching resource for bioimage-analysis provenance, sensitivity, and study design. Its public exercise uses 12 deterministic synthetic panels. The thesis panels are optional historical material and must not be distributed without permission.

It is not a biological treatment-effect dataset, a segmentation benchmark, or a validated clinical or microbiological method.

## Intended learners

- Students beginning Python-based bioimage analysis.
- Researchers inheriting legacy microscopy figures without complete raw data.
- Analysts learning to distinguish technical fields, samples, wells, and biological replicates.
- Authors preparing code and data for reproducible publication.

## Learning objectives

After working through the material, a learner should be able to:

1. Trace a reported number back to the exact code branch that generated it.
2. Distinguish preprocessing, segmentation, object measurement, and statistical inference.
3. Explain why rendered figure panels are not equivalent to raw microscopy data.
4. Identify pseudoreplication and define the correct experimental unit.
5. Compare how reasonable analysis choices change masks and derived measurements.
6. Separate descriptive observations from biological conclusions.
7. Design a data manifest and validation plan before analysing a larger dataset.
8. Recognize when an analysis should stop because calibration, controls, or replication are missing.

## What the 12 synthetic panels may be used for

- Demonstrating image loading, channel extraction, filtering, thresholding, morphology, labeling, and region measurements.
- Reconstructing historical outputs.
- Comparing analytical branches on the same illustrative cases.
- Exploring parameter sensitivity.
- Practising quality-control visualization.
- Teaching provenance, documentation, testing, and version control.
- Planning the transition from a pilot dataset to a confirmatory study.

## What the 12 panels may not be used for

- Estimating a treatment effect.
- Treating six treated and six untreated panels as biological replicates.
- Inferring bacterial viability, clearance, persistence, tolerance, biofilm formation, or macrophage effects.
- Reporting calibrated object sizes or areas.
- Claiming performance relative to modern segmentation methods without ground-truth annotations and suitable raw images.
- Training or validating a predictive biological model.

## Suggested teaching sequence

### Module 1 — Data provenance

Inspect the metadata and reconstruct where each panel came from. Identify which information is known, inferred, unknown, or irrecoverable.

Deliverable: a provenance table and a list of prohibited claims.

### Module 2 — Historical reconstruction

Run the submitted percentile/connected-component branch. Compare regenerated values with the archived reference metrics.

Deliverable: a reproducibility report explaining exact matches and any version-dependent differences.

### Module 3 — Analysis-choice sensitivity

Compare the submitted branch with the later Otsu/watershed branch. Vary preprocessing scale, background radius, threshold rule, minimum object size, and closing radius over documented ranges.

Deliverable: mask-overlap plots and per-panel metric trajectories. The unit of description remains the panel.

### Module 4 — Quality control

Review raw rendered panels, masks, label maps, overlays, and failure cases. Record whether labels, scale bars, compression, uneven background, or channel bleed-through could affect the output.

Deliverable: a structured QC sheet. Do not label a mask “correct” without external ground truth.

### Module 5 — Statistical-unit audit

Draw the intended hierarchy: experiment → well/sample → field → object. Compare it with the available hierarchy: selected montage panel → segmented region.

Deliverable: a short explanation of why object counts and fields cannot replace independent experiments.

### Module 6 — Design the next study

Use the manifest template to specify the raw files, controls, annotations, sample mapping, and acquisition metadata needed for a validated study.

Deliverable: a preregistered analysis outline and go/no-go criteria.

## Responsible language

Prefer:

- “In this rendered panel...”
- “Under this analysis configuration...”
- “The derived measurement changed when...”
- “This result illustrates analytical sensitivity...”
- “Biological interpretation requires raw, replicated data...”

Avoid:

- “Tobramycin caused...”
- “Macrophages increased...”
- “Bacteria were cleared...”
- “Biofilm formation was detected...”
- “The method proved...”
- “The groups differed...”

## Upgrade path when more data become available

### Stage 0 — Current public educational dataset

Twelve synthetic fluorescence-like panels. Use only for method sensitivity, quality-control, and study-design instruction. They carry no biological meaning.

### Stage 1 — Additional unlabelled exports

More images may improve the variety of examples, but they do not restore biological inference unless their experiment, sample/well, field, and condition identities are recovered. Treat unlabelled files as an image collection, not experimental observations.

### Stage 2 — Labelled raw acquisitions

Original channels/stacks plus experiment and sample mapping permit calibrated preprocessing, field aggregation, and acquisition QC. Biological inference still requires adequate independent experiments and controls.

### Stage 3 — Validation dataset

Blinded annotations, negative/single-colour controls, defined inclusion rules, and appropriate comparator methods permit segmentation-performance claims.

### Stage 4 — Confirmatory biological study

Prospectively collected, independently replicated experiments with matched CFU or viability endpoints permit treatment-effect and host-context questions.

## Publication positioning

The safest current outputs are:

- an open educational resource;
- a reproducible teaching case;
- a workshop/tutorial on legacy bioimage-analysis auditing; or
- a short perspective or technical note about analytical provenance, provided the venue accepts case-based educational work.

The repository should not be marketed as a new bacterial segmentation method or as evidence of a biological phenotype.
