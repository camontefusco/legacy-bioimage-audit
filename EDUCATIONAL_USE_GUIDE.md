# Educational use guide

## Purpose

This repository is a transition resource for experimental scientists learning to turn qualitative microscopy observations into quantitative measurements and analysis-ready data. Its public exercise uses 12 deterministic synthetic panels. The thesis case is optional historical material and must not be distributed without permission.

It is not a biological treatment-effect dataset, a segmentation benchmark, or a validated clinical or microbiological method.

## Intended learners

- Experimental students beginning Python-based image analysis or data science.
- Researchers who have qualitative observations but need operational definitions and structured measurement tables.
- Researchers inheriting legacy microscopy figures without complete raw data.
- Analysts learning to distinguish technical fields, samples, wells, and biological replicates.
- Authors preparing code and data for reproducible publication.

## Learning objectives

After working through the material, a learner should be able to:

1. Separate visual description, scientific interpretation, and proposed mechanism.
2. Translate a qualitative construct into an operational measurement.
3. Distinguish preprocessing, segmentation, measurement, aggregation, and inference.
4. Create linked manifest, object-level, and sample-level tables.
5. Identify pseudoreplication and define the correct experimental unit.
6. Compare how reasonable analysis choices change masks and derived measurements.
7. Design controls and a validation plan before group comparison.
8. Recognize when an analysis should stop because calibration, controls, ground truth, or replication are missing.

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

### Module 1 — Observation and construct

Write mechanism-neutral observations about the panels. Choose one construct—such as coverage, size, shape, or dispersion—and list alternative explanations for its appearance.

Deliverable: a completed observation-to-measurement canvas.

### Module 2 — Operational definition and data model

Define the processing, segmentation, measurement, and aggregation rules. Draw the experimental hierarchy and design manifest, object, and sample tables.

Deliverable: a measurement specification and table schema.

### Module 3 — Analysis-choice sensitivity

Compare the submitted branch with the later Otsu/watershed branch. Vary preprocessing scale, background radius, threshold rule, minimum object size, and closing radius over documented ranges.

Deliverable: mask-overlap plots and per-panel metric trajectories. The unit of description remains the panel.

### Module 4 — Quality control

Review raw rendered panels, masks, label maps, overlays, and failure cases. Record whether labels, scale bars, compression, uneven background, or channel bleed-through could affect the output.

Deliverable: a structured QC sheet. Do not label a mask “correct” without external ground truth.

### Module 5 — Experimental-unit audit

Draw the intended hierarchy: experiment → well/sample → field → object. Compare it with the available hierarchy: selected montage panel → segmented region.

Deliverable: a short explanation of why object counts and fields cannot replace independent experiments.

### Module 6 — Design the next study

Use the manifest template to specify the raw files, controls, annotations, sample mapping, and acquisition metadata needed for a validated study.

Deliverable: a preregistered analysis outline and go/no-go criteria.

### Optional case — Legacy reconstruction

Inspect the recovered historical branches and trace how one reported number arose. Use the mismatch between code and manuscript language to discuss why computational reproducibility, measurement validity, and biological inference are different questions.

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
