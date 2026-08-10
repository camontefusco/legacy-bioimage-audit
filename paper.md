---
title: 'From qualitative observations to quantitative data: a transition guide for experimental scientists'
tags:
  - data science
  - bioimage analysis
  - quantitative microscopy
  - reproducibility
  - experimental design
author: Carlos Victor Montefusco-Pereira
date: 2026-08-10
bibliography: paper.bib
---

# Abstract

Experimental scientists routinely recognize meaningful visual patterns before those patterns have formal numerical definitions. Moving from “this sample looks more clustered” to a defensible dataset requires more than learning Python: the analyst must define the construct, operationalize it as a measurement, preserve the experimental hierarchy, validate extraction, and restrict conclusions to what the data support. This transition guide presents a practical workflow for converting qualitative microscopy observations into reproducible quantitative information. A companion notebook uses deterministic synthetic fluorescence-like panels to demonstrate how preprocessing and segmentation choices alter masks and derived measurements. A legacy-analysis case illustrates what remains possible when raw data or labels are lost. The resource teaches measurement reasoning and computational traceability; it is not a validated segmentation method or a source of biological treatment-effect evidence.

# The difficult part is defining the measurement

Students moving from experimental work into data science often begin with strong domain perception. They can distinguish sparse from dense signal, dispersed from clustered patterns, or expected from unusual morphology. The challenge is that such observations mix description, interpretation, and mechanism.

Consider the statement “the treated image looks more clustered.” At least four questions are hidden inside it:

1. What visual property is being called clustering?
2. Which numerical quantity will represent that property?
3. At what experimental level will values be compared?
4. What evidence would support a treatment interpretation rather than a technical explanation?

Quantitative microscopy depends on acquisition, processing, metadata, and the relationship between images and experimental units [@jonkman2020]. Writing code before answering these questions can make an ambiguous concept reproducible without making it valid.

# A workflow from observation to dataset

## 1. Separate description from interpretation

Begin with a mechanism-neutral statement: “bright regions appear larger,” “signal covers more of the field,” or “objects appear less dispersed.” Then list possible explanations, including illumination, focus, exposure, background, cropping, segmentation, staining, or sampling. This prevents the proposed biological mechanism from becoming the measurement definition.

## 2. Define the construct

The construct is the property the analysis intends to represent: coverage, abundance, intensity, size, shape, spatial dispersion, or co-localization. Each construct needs an explicit link to the scientific question. Fluorescence intensity, for example, may reflect abundance, reporter expression, exposure, bleaching, detector response, or background. It should not be called “cell number” without evidence connecting the two.

## 3. Operationalize the construct

An operational definition turns the construct into a repeatable calculation:

- coverage as foreground pixels divided by analysable pixels;
- brightness as background-corrected intensity inside a defined region;
- object size as the area of a connected segmented region;
- shape as a specified descriptor such as solidity or eccentricity; or
- spatial organization as a pre-selected spatial statistic.

The definition must include units, preprocessing, thresholds, exclusions, aggregation, and how failed images are handled. Open tools such as scikit-image make implementation accessible [@vanderwalt2014], but software defaults do not substitute for scientific justification.

## 4. Preserve experimental hierarchy

A useful data model retains the nesting:

`experiment → biological sample → well/specimen → field/image → object`

Objects within an image and fields within one sample are generally technical observations. Treating them as independent biological replicates inflates apparent sample size and changes the question being answered. The independent experimental unit should be defined before hypothesis testing, and lower-level measurements should be aggregated or modeled according to the study design.

## 5. Build linked data layers

A robust workflow produces at least three related tables:

1. a **manifest** connecting files to samples, conditions, replicates, and acquisition metadata;
2. an **object table** containing measurements and identifiers for each detected region; and
3. a **sample-level table** containing pre-specified summaries at the independent-unit level.

This structure lets an analyst trace a plotted value back to an object, image, sample, file, and analysis configuration. Filenames alone are not a sufficient data model.

## 6. Validate extraction before comparing groups

Quality control should include source images, masks, labeled objects, overlays, excluded cases, and parameter-sensitivity views. Controls depend on the measurement and may include negative or positive samples, single-channel controls, calibration standards, repeated acquisitions, or blinded expert annotations.

The companion notebook compares reasonable preprocessing and segmentation configurations on synthetic panels. It reports foreground area, object count, size summaries, and intersection-over-union. Intersection-over-union measures agreement between masks, not accuracy, unless an appropriate reference annotation exists.

## 7. Match analysis and claims to evidence

Only after the measurement process and experimental unit are defensible should group comparisons or models begin. A reproducible result is not automatically a valid biological result [@munafò2017manifesto]. If calibration, controls, ground truth, sample mapping, or independent replication are missing, the output should remain descriptive and the missing evidence should become a requirement for the next experiment.

# A worked sensitivity demonstration

The repository supplies 12 deterministic synthetic fluorescence-like panels representing sparse signal, dense signal, large regions, and background gradients. Their purpose is to make measurement construction visible. Learners can observe that changing smoothing, background subtraction, thresholding, morphology, or minimum object size alters both the binary mask and the quantities derived from it.

The panels have no biological labels or treatment meaning. They cannot validate bacterial segmentation, microscopy performance, or biological conclusions. This restriction is a feature of the exercise: it forces attention onto how a qualitative appearance becomes a computational variable.

# The legacy-data boundary

The project originated from an attempt to reconstruct an analysis when original microscopy acquisitions and reliable labels were unavailable. That case now serves as a boundary example. Rendered panels can support code recovery, provenance documentation, and sensitivity analysis, but they cannot recreate acquisition metadata, physical calibration, sample identity, independent replication, or segmentation ground truth.

When qualitative material cannot support the intended inference, the analyst should stop rather than manufacture certainty. The useful outputs are then an evidence inventory, reconstructed code lineage, claim boundary, and prospective plan for better data collection.

# A transition canvas for students

Before coding, students should complete a one-page specification containing:

- qualitative observation and alternative explanations;
- proposed construct and operational definition;
- measurement and physical units;
- independent experimental unit and nested technical observations;
- required manifest fields and controls;
- QC visualization and sensitivity analysis;
- aggregation rule;
- supported and unsupported claims; and
- an explicit stop/go decision.

This changes the role of code. Instead of searching for any number that separates conditions, the student implements a documented measurement whose meaning, limitations, and provenance are visible.

# Limitations

This is a transition guide and worked computational demonstration, not an evaluation of student outcomes, a segmentation benchmark, or a validated biological method. The synthetic panels are not designed to reproduce a particular microscopy distribution. Constructs and controls must be adapted to the instrument, modality, sample, and scientific question.

# Availability, licensing, and AI assistance

The repository is available at <https://github.com/camontefusco/legacy-bioimage-audit>. Software is licensed under MIT. Original instructional prose and synthetic graphics are licensed under CC BY 4.0. Thesis-derived images are excluded.

AI-assisted tools were used in artifact recovery, code and documentation drafting, and language editing. The author reviewed the materials, ran the tests and notebook, and remains responsible for the content and stated evidence boundaries.

# References
