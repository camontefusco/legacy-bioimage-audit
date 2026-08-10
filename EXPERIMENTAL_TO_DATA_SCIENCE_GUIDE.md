# From qualitative observations to quantitative data

## Who this is for

This guide is for experimental students and researchers who can recognize meaningful patterns in images, notes, gels, plates, traces, or instrument displays but are beginning to translate those observations into structured data and reproducible analysis.

The central idea is simple: **quantification begins with a scientific definition, not with software**.

## The transition

An experimental description often sounds like:

> “This image looks more clustered.”

A quantitative analysis requires a chain of explicit decisions:

> “Clustered” → measurable visual property → operational definition → unit of measurement → extraction procedure → quality control → sample-level summary → statistical question.

Every arrow can change the meaning of the result. Code makes those decisions repeatable; it does not make them scientifically correct automatically.

## Seven-step workflow

### 1. Start with the observation

Write what you see without interpreting mechanism or cause. Separate visual description from explanation.

- Description: “Bright regions appear larger and less dispersed.”
- Interpretation: “Treatment induced aggregation.”

Only the first statement is directly available from the image. The second requires experimental evidence.

### 2. Define the construct

Name the concept you want to measure: coverage, intensity, count, size, shape, spatial dispersion, co-localization, or change over time. Ask what biological or physical quantity the construct is supposed to represent and what else could produce the same appearance.

### 3. Choose an operational measurement

Turn the construct into a computable definition. For example:

- coverage → fraction of pixels assigned to foreground;
- brightness → background-corrected intensity within a defined region;
- object size → area of each connected segmented region;
- clustering → a pre-specified spatial statistic, not merely large objects;
- co-localization → a statistic chosen for the image formation process and controls.

Record units, transformations, thresholds, exclusions, and aggregation rules before comparing groups.

### 4. Preserve the experimental hierarchy

Create one row per observation at the correct level and retain identifiers for:

`experiment → biological sample → well/specimen → field/image → object`

Objects and fields are usually nested technical observations, not independent biological replicates. Decide which level answers the scientific question before choosing a statistical test.

### 5. Build a tidy measurement table

Keep three connected layers:

1. **manifest:** file identity, sample mapping, condition, replicate, acquisition metadata;
2. **object table:** one row per segmented object, with image and sample identifiers;
3. **sample summary:** pre-specified aggregation at the independent experimental-unit level.

Never rely on filenames alone to carry the experimental design.

### 6. Validate the measurement process

Inspect overlays and failure cases. Test sensitivity to defensible parameter changes. Use negative, positive, single-channel, calibration, or expert-annotation controls as appropriate. Mask agreement between algorithms is not accuracy unless a defensible reference exists.

### 7. Match claims to evidence

Use descriptive language when calibration, ground truth, sample mapping, or replication is absent. Statistical modeling should begin only after the measurement and experimental unit are defensible.

## A practical translation canvas

Complete this before coding:

- Qualitative observation:
- Proposed construct:
- Alternative explanations:
- Operational definition:
- Measurement unit and physical unit:
- Independent experimental unit:
- Technical observations nested within it:
- Required metadata:
- Required controls:
- QC visualization:
- Sensitivity analysis:
- Sample-level aggregation rule:
- Supported claim:
- Claim that remains unsupported:
- Stop/go decision:

## What the notebook demonstrates

The included notebook uses synthetic fluorescence-like panels to show that several reasonable segmentation choices can produce different masks, object counts, areas, and size summaries. The exercise teaches measurement construction and sensitivity; it does not identify a biologically correct segmentation.

## When only qualitative legacy material remains

Rendered figures or unlabelled images may still support code practice, provenance reconstruction, and method-sensitivity demonstrations. They usually cannot recover experimental identity, calibration, ground truth, or biological replication. In that situation, document the boundary and use the audit to design the next experiment rather than forcing a treatment conclusion.
