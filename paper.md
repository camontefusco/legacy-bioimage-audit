---
title: 'From qualitative microscopy observations to quantitative data: an open computational learning module for experimental scientists'
tags:
  - data science education
  - bioimage analysis
  - quantitative microscopy
  - measurement
  - reproducibility
author: Carlos Victor Montefusco-Pereira
affiliation: Independent researcher
date: 2026-08-10
bibliography: paper.bib
---

*Affiliation: Independent researcher.*

# Abstract

Experimental scientists often recognize meaningful visual patterns before they can define them numerically. Moving from “this image looks more clustered” to a defensible dataset requires more than learning Python: the analyst must separate description from interpretation, define a construct, operationalize it as a measurement, preserve experimental hierarchy, validate extraction, and restrict conclusions to the available evidence. This open computational learning module teaches that transition through deterministic synthetic images and three published microscopy datasets. Learners examine threshold and object-splitting sensitivity in two-dimensional nuclear images, projection sensitivity in three-dimensional image stacks, and channel-role and region-definition sensitivity in paired fluorescence images. The module includes executable notebooks, source-data retrieval scripts, tests, provenance documentation, and explicit claim boundaries. It teaches measurement reasoning and computational traceability; it is not a validated segmentation method, a biological benchmark, or evidence of educational effectiveness.

# Statement of need

Students moving from experimental work into data science commonly begin with strong domain perception. They can recognize sparse and dense signal, dispersed and clustered patterns, or expected and unusual morphology. Introductory programming instruction can teach them to load images, call segmentation functions, and create tables, but the scientifically difficult step occurs earlier: deciding what a number means.

Quantitative microscopy depends on acquisition, processing, metadata, calibration, and the relationship between images and experimental units [@waters2009; @lee2018; @jonkman2020]. Accessible software such as CellProfiler and scikit-image lowers the technical barrier to measurement [@carpenter2006; @vanderwalt2014], but a reproducible software default does not establish construct validity. A student can therefore produce an orderly spreadsheet while silently changing the scientific question, treating fields as biological replicates, or interpreting fluorescence as abundance without the required controls.

This module addresses that gap. Its contribution is not a new segmentation algorithm. It is a reusable learning sequence connecting qualitative observation, measurement design, computational sensitivity, data hierarchy, and claim restraint. The intended audience is senior undergraduate, postgraduate, or early-career experimental life scientists who have basic Python and microscopy familiarity but limited formal experience in quantitative image analysis. The notebooks can be used for self-study or as a short instructor-led module.

# Learning design

The module uses a worked-example progression. A deterministic synthetic exercise first makes analysis choices visible without biological labels. Three published-image transfer cases then introduce one new source of complexity at a time: reference-mask agreement, three-dimensional reduction, and multichannel region definition. This progression follows a “coding to learn” approach: code is used to expose the consequences of a measurement decision rather than to search for a preferred biological result. It also reflects lessons from reproducible computational instruction: keep examples executable, expose intermediate states, and make learners modify working analyses rather than begin from an empty script [@wilson2014].

The suggested sequence takes approximately three to five hours. Learners need Python 3.10 or later, basic NumPy and pandas familiarity, and an understanding of fluorescence channels and experimental replication. Each notebook states its objectives, declares its teaching sample, displays intermediate images and masks, produces structured measurements, and ends with interpretation prompts. A learner should be able to:

1. separate a qualitative description from a biological interpretation;
2. express a construct as a complete operational definition;
3. identify the independent experimental unit and nested technical observations;
4. test whether preprocessing, segmentation, projection, or region choices materially alter a measurement; and
5. write supported and unsupported claims for the available evidence.

The accompanying transition canvas serves as a formative assessment. Before coding, the learner records the observation, alternative explanations, construct, units, preprocessing, experimental hierarchy, controls, quality-control views, aggregation rule, sensitivity analysis, and stop/go criterion. After each notebook, the learner revises the canvas and explains which decisions changed the result. An instructor can evaluate whether the proposed measurement is reproducible, scientifically interpretable, and matched to the experimental unit; no single numerical answer is treated as universally correct.

# From observation to structured data

The learning workflow begins with a mechanism-neutral description such as “bright regions appear larger” or “signal covers more of the field.” The learner then lists alternative technical and biological explanations. The construct is named—coverage, intensity, size, shape, spatial dispersion, or co-localization—and converted into a calculation with explicit units, preprocessing, threshold, exclusion, and aggregation rules.

The workflow preserves the hierarchy

`experiment → biological sample → well/specimen → field/image → object`.

Objects within an image and fields from one specimen are not automatically independent biological replicates [@lazic2010]. A robust implementation therefore produces linked layers: a file manifest, an image table, an object table when appropriate, and a sample-level table based on a prespecified aggregation rule. Filenames alone are not a sufficient data model. Machine-readable identifiers and provenance also make the educational outputs easier to find, inspect, and reuse [@wilkinson2016].

Extraction is checked before any group comparison. Relevant views include the source image, corrected image, binary mask, labelled objects, overlay, excluded cases, and parameter-sensitivity summaries. Agreement statistics are named carefully. Intersection-over-union with an annotation measures foreground agreement; it does not by itself prove biological accuracy. Reproducibility is necessary but not sufficient for valid inference [@munafò2017manifesto].

# Executable cases

## Synthetic sensitivity exercise

The first notebook generates 12 deterministic fluorescence-like panels with sparse signal, dense signal, large regions, and background gradients. Learners vary smoothing, background subtraction, percentile or Otsu thresholding, minimum object size, and connected-component or watershed splitting. The panels are original, redistributable teaching graphics with no biological labels. Their purpose is to show that a qualitative appearance becomes multiple plausible numerical variables depending on the operational definition.

## BBBC039: foreground agreement is not object agreement

The first published-image case uses three declared training images from BBBC039, a CC0 collection of 16-bit U2OS nuclear fluorescence images and annotations [@ljosa2012; @caicedo2019]. The loader preserves bit depth, and reference instances are decoded according to the dataset author's connected-component procedure.

Four configurations compare percentile thresholds, Otsu thresholding, connected components, and watershed. Across the three teaching images, Otsu foreground masks had mean intersection-over-union of 0.908 with the deposited foreground annotation. Connected components differed from the derived reference count by a mean of -5.7 objects, whereas watershed used the same foreground masks but differed by +104.3 objects. These values are descriptive outputs of a three-image exercise, not benchmark estimates. They demonstrate that strong foreground overlap can coexist with a materially different object definition.

## BBBC050: a 2D projection is a measurement decision

The second case uses three CC BY 3.0 three-dimensional TIFF stacks and corresponding annotations from one BBBC050 training embryo [@tokuoka2020]. The files are repeated teaching observations, not independent replicates. Learners compare a central optical plane, mean projection, and maximum projection before applying one illustrative Otsu configuration.

Mean foreground agreement across the three files was 0.578 for the central plane, 0.542 for the mean projection, and 0.574 for the maximum projection. Mean predicted object counts were 6.0, 6.7, and 8.0, respectively. The exercise does not identify a universally preferred projection. Instead, it asks whether the intended construct concerns one plane, any bright voxel across depth, or a true three-dimensional property. Maximum projection can collapse depth and merge objects; mean projection can suppress small bright structures; a central plane omits signal outside one section.

## BBBC013: channel and region roles define the variable

The third case uses paired GFP and DNA images from three wells in the CC BY 3.0 BBBC013 collection [@carpenter2006; @ljosa2012]. DNA defines nuclear objects, while GFP supplies the measured signal. The comparison region is an exterior ring around the nuclear mask. Learners vary the ring radius while holding the images and nuclear segmentation constant.

The resulting nuclear-to-perinuclear GFP ratio changed substantially with the region definition. In one image it increased from 2.91 with a three-pixel ring to 6.69 with a 15-pixel ring; in another it changed from 0.68 to 1.10. These are not treatment or translocation results. They show that assigning channel roles is not enough: the spatial region used as a denominator is part of the construct and needs scientific justification. A validated assay would additionally require an appropriate cell or cytoplasmic boundary, plate-aware quality control, full replicate mapping, and a prespecified statistical analysis.

# Reproducibility and data boundaries

All three source collections are retrieved from their authoritative public repositories by opt-in scripts and remain excluded from version control. The notebooks record citations, licenses, sample selection, channel or dimensional assumptions, and supported claims. Unit tests cover deterministic generation, bit-depth preservation, stack projection, annotation decoding, and multichannel measurement. Continuous integration tests Python 3.10 and 3.12 and reconstructs every notebook.

The project originated from an attempted reconstruction in which the original microscopy acquisitions and reliable labels were unavailable. That history is retained as a boundary case rather than the module's primary evidence. Rendered legacy panels can support provenance documentation and code-lineage recovery, but cannot recreate calibration, acquisition metadata, sample identity, independent replication, or ground truth. When the intended inference exceeds the material, the correct output is an evidence inventory and prospective data plan—not manufactured certainty.

# Limitations

This is an educational module and worked computational demonstration, not an evaluation of learner outcomes, a segmentation benchmark, or a validated biological method. The three published-image notebooks deliberately use small teaching samples to keep decisions inspectable; their numerical summaries should not be generalized to the full datasets. The simple thresholding operations are chosen for transparency rather than state-of-the-art performance. Constructs, controls, and image-processing choices must be adapted to the instrument, modality, specimen, and scientific question.

The module currently focuses on fluorescence microscopy. Its general reasoning may transfer to other qualitative experimental materials, but that broader transfer has not been demonstrated. A future teaching evaluation could examine usability and changes in learners' ability to specify constructs and evidence boundaries, but no educational-effectiveness claim is made here.

# Availability, licensing, and AI assistance

The repository is available at <https://github.com/camontefusco/legacy-bioimage-audit> and archived at <https://doi.org/10.5281/zenodo.21876822>. Software is licensed under MIT. Original teaching text and synthetic graphics are licensed under CC BY 4.0. Third-party images retain their source licenses and are not redistributed.

AI-assisted tools were used in artifact recovery, code and documentation drafting, and language editing. The author reviewed the materials, executed the tests and notebooks, and remains responsible for the content and evidence boundaries.

# References
