---
title: 'Auditing legacy bioimage analyses: a computational learning module on provenance, sensitivity, and limits of inference'
tags:
  - bioimage analysis
  - reproducibility
  - research integrity
  - image segmentation
  - computational education
authors:
  - name: TO BE CONFIRMED
    affiliation: 1
affiliations:
  - name: TO BE CONFIRMED
    index: 1
date: 2026-08-10
bibliography: paper.bib
---

# Summary

Bioimage-analysis training often begins with a clean dataset and a well-defined task. Research practice can be less orderly: an analyst may inherit rendered figures, incomplete metadata, divergent code branches, and numerical results whose provenance is uncertain. This learning module uses deterministic synthetic fluorescence-like panels and a documented legacy-analysis scenario to teach how to audit such material without converting reconstruction into unsupported biological inference.

Learners trace measurements through preprocessing, thresholding, morphology, connected-component labeling, and object measurement. They then compare plausible configurations, quantify mask agreement, inspect quality-control overlays, and distinguish agreement from accuracy. The lesson closes with an experimental-unit audit and a stopping rule: where raw acquisitions, ground truth, calibration, or independent replication are absent, an analyst can document computational behavior but cannot infer treatment effects or validate segmentation performance.

# Statement of need

Reproducibility instruction frequently emphasizes rerunning code, yet numerical reproducibility alone does not establish data suitability, inferential validity, or methodological accuracy. A pipeline may exactly reproduce an archived number while operating on selected figure panels rather than independent samples. Similarly, two segmentation configurations may agree with one another while both remain unvalidated against expert annotations.

The module addresses this gap through a compact case that can be completed on an ordinary laptop. Its public dataset is generated deterministically and carries no biological labels or intended biological interpretation. This removes redistribution barriers and makes the exercise immediately reusable, while the accompanying claim boundary prevents the synthetic exercise from being represented as validation. Researchers with authorized legacy images may optionally substitute them for local study, but those images are not required or distributed.

# Learning objectives and instructional design

After completing the module, learners should be able to:

1. connect a reported measurement to a specific computational branch;
2. distinguish preprocessing, segmentation, measurement, and inference;
3. test the sensitivity of masks and measurements to reasonable analytical choices;
4. explain why mask overlap measures agreement rather than accuracy;
5. identify the experimental unit and recognize pseudoreplication;
6. formulate evidence-based limits on interpretation; and
7. specify the metadata, controls, annotations, and replication needed for a future validated study.

The notebook follows a predict–run–inspect–reflect sequence. Learners first inspect provenance and configuration tables, then execute multiple segmentation branches, review visual overlays and metric trajectories, and answer structured interpretation prompts. Automated tests cover core measurements, sensitivity summaries, and deterministic generation of the teaching panels. Deliberately excluded activities include group hypothesis tests, predictive modeling, and claims of biological performance.

# Experience of use

Formal pilot results will be added after the first documented teaching session. The repository includes a structured pilot template that records learner background, completion time, recurrent installation problems, misconceptions, and resulting revisions. Until that pilot is complete, this manuscript is a submission skeleton rather than a submission-ready claim of educational effectiveness.

# Availability and limitations

The module is designed for a versioned public repository and archival DOI release. Licensing, authorship, and repository URL must be confirmed before submission. The synthetic panels are pedagogical inputs, not a microscopy benchmark. No conclusion about bacteria, treatment, viability, host response, or segmentation accuracy can be drawn from them. Historical thesis-derived panels are excluded unless explicit redistribution permission is obtained.

# Acknowledgements

To be completed after contributor and institutional review.

# References
