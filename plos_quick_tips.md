---
title: 'Seven quick tips for turning qualitative microscopy observations into quantitative data'
tags:
  - bioimage analysis
  - quantitative microscopy
  - data science education
  - reproducibility
author: Carlos Victor Montefusco-Pereira
affiliation: Independent researcher
date: 2026-08-12
bibliography: paper.bib
---

*Article type: Education (Quick Tips); section: General.*

*Affiliation: Independent researcher.*

# Abstract

Experimental scientists often recognize important visual patterns before they can define them numerically. Converting “this signal looks more clustered” into a defensible dataset is not simply a programming task. It requires the analyst to distinguish observation from interpretation, define the intended construct, preserve experimental hierarchy, inspect extraction quality, test sensitivity to reasonable analytical choices, and restrict conclusions to the available evidence. These seven tips present a practical workflow for that transition. An open companion resource uses deterministic synthetic images and small, declared samples from three public microscopy collections to demonstrate threshold and object-splitting sensitivity, the consequences of reducing three-dimensional stacks to two-dimensional projections, and the effect of channel and region definitions on intensity ratios. The resource is designed for self-study by experimental life scientists beginning quantitative image analysis. It is not a segmentation benchmark, validated biological method, or evaluation of learner outcomes.

# Introduction

Modern microscopy produces numerical arrays, but that fact does not make every number extracted from an image scientifically meaningful. Software can load an image, apply a threshold, label objects, and export a table long before the analyst has decided what the resulting variable represents. For an experimental scientist moving into data science, the main difficulty is therefore often not syntax. It is operationalization: translating a visual observation into a calculation whose meaning, units, exclusions, aggregation, and limitations are explicit.

Existing guidance maps the interconnected choices required to plan and perform quantitative bioimaging experiments [@senft2023], identifies broad pitfalls in computational medical-image analysis [@chicco2023], and explains good practice when working with numerical data [@schwen2018]. The present tips complement those resources by focusing narrowly on the bridge between one qualitative microscopy statement and one defensible quantitative variable. The associated notebooks use code not to promote a preferred algorithm, but to make measurement decisions inspectable.

The workflow is summarized in Figure 1. It is intended for senior undergraduate, postgraduate, and early-career experimental life scientists with basic Python and fluorescence-microscopy familiarity. Readers can apply the questions without using Python, although the executable examples make the consequences of each choice easier to see.

![Figure 1. Seven-tip workflow from a qualitative observation to a bounded quantitative claim. The process is iterative: quality-control or sensitivity findings may require revising the construct or operational definition. The graphic is original and licensed CC BY 4.0. Alt text: A workflow connects qualitative observation, alternative explanations, construct, operational definition, hierarchy-aware data table, quality control, sensitivity analysis, and bounded claim.](figures/qualitative_to_quantitative_workflow.svg)

# Tip 1: Describe what you see before explaining why it happened

Begin with a mechanism-neutral description. “Bright regions cover more of the field” is an observation; “the treatment increased biofilm formation” is an interpretation requiring experimental support. Other plausible explanations may include illumination differences, background, focus, detector saturation, staining variation, field selection, sample preparation, or a genuine biological effect.

Write the observation before inspecting group labels when possible, then list at least two technical and two biological explanations. Ask: *What can another person verify directly from the image, and what am I adding from prior knowledge?* This separation does not prohibit biological hypotheses. It prevents a favored hypothesis from silently determining the measurement.

In the companion synthetic notebook, panels contain sparse signal, dense signal, large regions, and gradients but have no biological labels. The absence of a biological answer is deliberate: it forces the learner to describe appearance and propose measurements without searching for a treatment effect.

Practical check: Write three sentences beginning with “I observe,” “This could reflect,” and “To distinguish these possibilities, I would need.” If the first sentence contains a treatment, mechanism, or causal verb, rewrite it until it only describes visible structure.

# Tip 2: Define the construct before choosing the software

A construct is the property the measurement is intended to represent: coverage, intensity, object size, shape, dispersion, localization, or co-localization. Terms such as “amount,” “signal,” and “clustering” are incomplete until converted into operational definitions.

Complete this sentence before coding: *For each [unit], I will calculate [variable] in [units] from [region or object], after [preprocessing], using [inclusion and exclusion rules], and aggregate it at the [experimental level].* For example, “coverage” could mean the fraction of valid field pixels above a prespecified threshold after background correction. It does not automatically mean cell number, biomass, viability, or biological abundance.

Choosing software first encourages the available function to define the scientific question. Instead, select the construct, then identify the image features and controls needed to support it. If the construct requires calibrated distance but pixel size is unavailable, the correct result is a missing requirement—not an uncalibrated area presented as physical size.

Practical check: Ask another reader to implement your definition without speaking to you. Any question they must ask—about threshold, channel, region, exclusion, units, or aggregation—reveals a decision that is still implicit.

# Tip 3: Preserve the experimental hierarchy in the data table

Microscopy data are nested. A common hierarchy is

`experiment -> biological sample -> well/specimen -> field/image -> object`.

Objects in one image and fields from one sample are not independent biological replicates [@lazic2010]. Counting thousands of objects can improve the precision of a within-image description without increasing the number of independently treated samples.

Create a file manifest and retain identifiers for every level. Produce an image table and, when needed, an object table linked by stable keys. Define the sample-level aggregation rule before comparing groups. Ask: *At what level was the experimental condition independently applied?* That level, not the largest row count in the exported table, usually determines replication for treatment inference.

Filenames can assist navigation but should not be the only data model. A separate manifest should record source, condition, sample, well, field, channel, stack, calibration, exclusions, and provenance. Machine-readable identifiers make later auditing and reuse easier [@wilkinson2016].

Practical check: Draw the experimental hierarchy as a tree, then mark where randomization or independent treatment occurred. Add one table column for every level needed to reconstruct that tree. If the hierarchy cannot be reconstructed from the table, group statistics are premature.

# Tip 4: Make every image-processing choice part of the measurement definition

Background subtraction, smoothing, projection, thresholding, morphology, minimum object size, and object splitting are not merely implementation details. Each can change the variable being measured. Record parameter values, software versions, channel roles, dimensional reductions, and edge-object rules.

The BBBC050 companion case compares a central plane, mean projection, and maximum projection from three files belonging to one training embryo [@tokuoka2020]. Mean foreground agreement with the deposited annotation was 0.578, 0.542, and 0.574, while mean predicted object counts were 6.0, 6.7, and 8.0. These are small teaching outputs, not benchmark estimates. They demonstrate that a projection answers a scientific question: one plane, average signal through depth, or any bright voxel encountered through depth. A maximum projection can merge structures separated axially; a mean projection can suppress small bright structures; a single plane omits structures outside that section.

Ask: *If I change this setting, am I approximating the same construct more or less well, or have I defined a different construct?*

Practical check: Create a measurement specification beside the code with input channel, bit depth, calibration, correction, projection, segmentation, morphology, edge handling, units, and aggregation. Version this specification with the analysis so a changed default cannot silently alter the variable.

# Tip 5: Inspect masks and intermediate outputs before comparing groups

A tidy spreadsheet is not evidence that extraction succeeded. Before group comparison, inspect the source image, corrected image, binary mask, labelled objects, overlay, excluded regions, and representative failure cases. Quality control should be stratified across batches, plates, conditions, and acquisition times so that a systematic failure is not hidden by a convenient example.

The BBBC039 companion case uses three declared training images and deposited annotations [@ljosa2012; @caicedo2019]. Otsu masks had mean foreground intersection-over-union of 0.908, but connected-component and watershed counts differed from the derived reference counts by means of -5.7 and +104.3 objects, respectively. The same foreground can therefore support materially different object definitions. Foreground overlap should be named as foreground agreement; it does not prove biological validity or correct instance separation.

Ask: *Can I explain why each displayed object exists, why excluded objects were removed, and which failure modes remain?* If not, do not advance to biological comparison.

Practical check: Select examples before viewing the final group result: typical images, extreme intensities, crowded and sparse fields, excluded images, and every acquisition batch. A gallery chosen after seeing the desired result risks becoming illustration rather than quality control.

# Tip 6: Test whether reasonable analytical choices change the result

Reproducibility of one fixed pipeline is necessary but does not show that the result is robust to defensible alternatives [@munafò2017manifesto]. Identify uncertain decisions before examining the desired outcome, choose plausible alternatives, and compare masks and measurements per image rather than only final group summaries.

The BBBC013 companion case holds paired GFP and DNA images constant while changing the exterior ring used as a perinuclear comparison region [@carpenter2006; @ljosa2012]. A nuclear-to-perinuclear GFP ratio changed from 2.91 with a three-pixel ring to 6.69 with a 15-pixel ring in one image, and from 0.68 to 1.10 in another. These are not translocation or treatment results. They show that the denominator region is part of the construct.

Prespecify a response to sensitivity. If all plausible choices support the same descriptive conclusion, report that stability. If the sign, ranking, or practical interpretation changes, report the dependence and revise the operational definition or gather validation data. Do not select the configuration that produces the preferred story.

Practical check: Make a small decision table containing the uncertain choice, plausible alternatives, expected failure mode, diagnostic view, and action if conclusions change. Sensitivity analysis is most informative when the response to instability is decided in advance.

# Worked cases and reproducibility

The companion resource turns Tips 4–6 into three small, inspectable cases. Each case uses a fixed, declared set of images, deterministic code, and a parameter change chosen before the output is interpreted. The examples are teaching demonstrations, not representative samples, performance benchmarks, or biological experiments.

In the BBBC050 case, three alternative reductions of a small three-dimensional stack are compared: a central plane, a mean projection, and a maximum projection. The resulting foreground agreement and object counts differ, showing why dimensional reduction must be recorded as part of the measurement definition. In the BBBC039 case, the same thresholded foreground is passed to connected components and watershed splitting. Foreground overlap remains high while object counts diverge, separating pixel agreement from instance-definition validity. In the BBBC013 case, paired channels are held constant while the width of an exterior ring is changed; the intensity ratio changes, demonstrating that the comparison region is part of the construct.

The repository provides the notebooks, environment information, tests, retrieval scripts, manifests, and rendered outputs needed to reproduce these demonstrations. Public images are retrieved from their authoritative collections rather than redistributed, and synthetic images are generated deterministically. The exact outputs and file-level provenance are archived with the release. Because the cases are intentionally small and fixed, they support inspection of analytical consequences but do not support estimates of biological variability, method ranking, or learner effectiveness.

# Tip 7: Stop the claim where the evidence stops

Match each statement to the strongest evidence actually available. A rendered figure can support a statement about visible appearance. A mask can support a statement about pixels selected under a declared rule. Reference annotations can support a named agreement statistic. Biological treatment claims additionally require sample identity, appropriate controls, independent replication, and a prespecified analysis.

The project that motivated the companion resource lacked recoverable raw acquisitions and reliable sample labels. No image-analysis refinement could recreate calibration, experimental hierarchy, controls, or ground truth. In that situation, the responsible output is an evidence inventory, a reproducible account of what can still be computed, and a prospective plan for collecting what is missing.

Use two columns when writing results: *supported statements* and *unsupported statements*. Ask: *What additional evidence would be required to move this sentence into the supported column?* Stopping is not analytical failure. It is a valid scientific conclusion when the intended inference exceeds the material.

Practical check: Underline every noun and verb in the proposed conclusion. For each one, identify its evidential source. Words such as “caused,” “increased,” “viable,” “cell,” or “replicate” often require more evidence than a thresholded image provides.

# Conclusion

The transition from experimental observation to defensible quantitative image data is not achieved when an image becomes a table. It is achieved when the analyst can explain what every value means, which experimental unit it describes, how processing choices affect it, how extraction was checked, and which claims remain outside the evidence. The seven tips provide a repeatable path through those decisions. The open companion notebooks are deliberately transparent and small so learners can inspect the consequences of each choice rather than treat a sophisticated pipeline as an oracle.

# Data and software availability

The companion resource, notebooks, tests, synthetic graphics, and retrieval scripts are available at <https://github.com/camontefusco/legacy-bioimage-audit>. The current archive is <https://doi.org/10.5281/zenodo.21876822>; a version-specific archive containing the complete submitted companion resource will be created before journal submission. Code is licensed under MIT, and original teaching text and synthetic graphics are licensed under CC BY 4.0. Third-party images remain under their source licenses and are retrieved from authoritative repositories rather than redistributed.

# AI-use disclosure

OpenAI ChatGPT and Codex were used for artifact recovery, code and documentation drafting, literature-discovery support, and language editing. The author checked cited sources against the original publications, reviewed and revised the manuscript and code, executed the tests and notebooks, and remains responsible for accuracy, attribution, and all claims.

# References
