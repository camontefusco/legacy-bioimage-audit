---
title: 'When raw microscopy data are gone: a responsible workflow for auditing legacy bioimage analyses'
tags:
  - bioimage analysis
  - reproducibility
  - research integrity
  - image segmentation
  - legacy data
authors:
  - name: Carlos Victor Montefusco-Pereira
date: 2026-08-10
bibliography: paper.bib
---

# Abstract

Legacy bioimage-analysis projects sometimes survive only as rendered figures, partial metadata, divergent scripts, and reported measurements. Re-executing recovered code can establish computational provenance, but it cannot recreate raw acquisitions, independent biological replication, calibration, controls, or segmentation ground truth. This technical tutorial presents a conservative workflow for auditing such projects. It separates historical reconstruction from validation, uses deterministic synthetic fluorescence-like panels to demonstrate parameter sensitivity, and defines stopping rules that prevent descriptive image behavior from becoming unsupported biological inference. The accompanying open repository contains code, tests, synthetic examples, provenance records, and claim boundaries. It is a worked framework for research recovery and training, not a validated biological method.

# The recovery problem

Quantitative microscopy depends on acquisition settings, preprocessing choices, metadata, and the relationship between images and experimental units [@jonkman2020]. When only a figure panel remains, pixel values may already reflect cropping, contrast adjustment, compositing, rescaling, compression, or annotation. The panel can still document what a particular program does to that rendered input, but it is not interchangeable with the original microscopy data.

Three questions must therefore remain separate:

1. **Provenance:** Which code and parameters produced a reported value?
2. **Analytical behavior:** How sensitive are masks and derived measurements to reasonable choices?
3. **Scientific validity:** Do the measurements accurately represent a biological quantity and support inference across independent experiments?

Exact recovery of the first does not establish the third. This distinction is consistent with broader reproducibility guidance: rerunning an analysis is valuable, but reproducibility alone does not establish inferential validity [@munafò2017manifesto].

# A responsible audit workflow

## 1. Inventory evidence before analysing

Record every surviving artifact: manuscripts, figure captions, screenshots, tables, notebooks, scripts, environments, emails, and file manifests. Classify each fact as directly documented, inferred, unknown, or irrecoverable. Search for original acquisitions and sample mappings, but record the search boundary and negative result rather than describing missing files as recovered data.

## 2. Reconstruct code branches separately

Legacy projects often contain a submitted branch, a later rewrite, and fragments that combine both. Preserve each branch and compare parameters, algorithms, and outputs. A manuscript may describe Otsu thresholding and watershed segmentation while submitted numbers originate from percentile thresholding and connected components. The audit should report the mismatch rather than silently selecting the branch that best supports the narrative.

## 3. Reproduce numbers without rehabilitating claims

An exact match between recovered code and an archived table demonstrates numerical lineage. It does not show that the input was appropriate, that the mask was accurate, or that image fields were independent replicates. Reconstruction results should therefore be labeled historical or descriptive.

## 4. Test analytical sensitivity

The accompanying notebook uses open scientific Python tools, including scikit-image [@vanderwalt2014], to compare plausible preprocessing, thresholding, morphology, and minimum-object-size choices. It reports foreground area, object count, object-size summaries, and mask intersection-over-union. These comparisons reveal whether conclusions depend heavily on configuration.

Mask overlap is deliberately described as **agreement**, not accuracy. Without blinded expert annotations or another defensible reference, two masks may agree while both are biologically wrong.

## 5. Audit the experimental unit

The intended hierarchy may be experiment → well or sample → field → segmented object. A rendered montage panel does not restore that hierarchy. Objects within one image and multiple fields from one well cannot automatically replace independent experiments. When sample mapping is missing, the safest unit of description is the individual surviving panel.

## 6. Apply a stopping rule

Stop before treatment hypothesis tests, predictive modeling, or biological-performance claims when one or more of the following are unavailable:

- raw or suitably documented source images;
- mapping from images to independent experiments and samples;
- acquisition metadata and calibration required by the measurement;
- appropriate controls;
- ground-truth annotations for accuracy claims; or
- sufficient independent replication for the proposed inference.

Stopping is a positive analytical result: it identifies exactly what evidence is required next.

# Why synthetic panels are used

The public exercise contains 12 deterministic fluorescence-like panels with varied density, object size, and background structure. They make the code immediately executable without redistributing thesis-derived material. They also prevent experimental labels from inviting accidental biological interpretation.

Synthetic examples can demonstrate software behavior, edge cases, and sensitivity. They cannot validate performance on bacteria, microscopy instruments, host cells, or treatment conditions. The repository states this boundary in the data documentation, notebook, and claim guide.

# Outputs of an audit

A useful legacy-analysis audit should produce:

- an artifact and provenance inventory;
- a code-branch reconciliation;
- reproducible reference outputs;
- parameter-sensitivity and quality-control views;
- an experimental-unit diagram;
- a list of supported and prohibited claims; and
- a prospective manifest for any future data collection.

These outputs can preserve methodological history, teach responsible analysis, and guide a new study even when the original biological question can no longer be answered.

# Limitations

This report is based on one recovery case and a synthetic demonstration. It does not estimate how often manuscripts and code diverge, assess learner outcomes, benchmark segmentation algorithms, or establish a new biological method. The synthetic panels are not intended to resemble a validated microscopy distribution. The framework should be adapted to the acquisition modality, biological hierarchy, and governance requirements of each project.

# Availability, licensing, and AI assistance

The repository is available at <https://github.com/camontefusco/legacy-bioimage-audit>. Software is licensed under MIT. Original instructional prose and synthetic graphics are licensed under CC BY 4.0. Thesis-derived images are excluded.

AI-assisted tools were used to help recover and compare project artifacts, draft code and documentation, and edit this report. The author reviewed the repository, executed the tests and notebooks, checked claim boundaries, and remains responsible for the content. The limitations of the surviving evidence, including contradictions between manuscript language and recovered code, are reported rather than resolved by assumption.

# Acknowledgements

The historical microscopy work originated during doctoral research. Acknowledgements for the present technical report will be finalized before archival release and will distinguish historical scientific contributions from authorship of the current software and report.

# References
