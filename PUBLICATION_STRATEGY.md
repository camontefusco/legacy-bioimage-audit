# Publication strategy

## Current route: technical report and software release

The immediate output is a versioned GitHub release archived in Zenodo with a DOI. The accompanying report, `paper.md`, is a self-contained technical tutorial on responsible legacy bioimage-analysis auditing. It makes no claim of educational effectiveness and does not require a teaching cohort.

Before archival release:

1. Confirm acknowledgements and whether a current affiliation should be listed.
2. Perform one final public-file and citation audit.
3. Create release `v0.1.0` and archive it through Zenodo.
4. Add the DOI to `CITATION.cff` and the report.

## Possible later journal route

An expanded, literature-grounded **Opinion Article** may be considered for F1000Research if publication charges and scope are acceptable. The paper would argue for explicit stopping rules and claim boundaries when raw bioimage data are lost. It should not present the synthetic demonstration as new biological research.

## Routes not recommended now

- **JOSE:** no longer the target because we are not claiming or evaluating a learning intervention. The pilot package remains optional.
- **JOSS:** premature. Current screening emphasizes sustained open development, research use or impact, and community evidence. A newly public single-case reconstruction should not be stretched to meet those criteria.
- **Method or segmentation journals:** unsuitable without raw data, ground truth, independent replication, and method validation.

## Dissemination after DOI release

Share the citable resource with bioimage-analysis training and reproducibility communities such as NEUBIAS and the Centre for Open Bioimage Analysis. Describe it as a technical tutorial and recovery case, not a validated segmentation method.
