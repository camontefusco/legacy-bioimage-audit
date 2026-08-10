# Publication strategy

## Recommended route

### 1. Release the learning module on GitHub and Zenodo

Publish a versioned GitHub release, then archive that release in Zenodo to obtain a DOI. This creates a stable, citable research object but is not peer review.

Release only after ownership, contributor attribution, and licensing are agreed. The public release should contain the synthetic panels, notebook, tests, guide, and claim boundary. Thesis-derived images should remain excluded unless redistribution permission is documented.

### 2. Submit to the Journal of Open Source Education (JOSE)

JOSE is the strongest fit because the contribution is an open computational learning module, not a newly validated biological method. Position it as a case-based lesson in analytical provenance, parameter sensitivity, experimental units, and responsible stopping rules for legacy bioimage analysis.

Before submission:

1. Choose an OSI-approved code license and a compatible open license for text and graphics.
2. Complete a small teaching pilot, ideally with 3–5 learners or one workshop.
3. Revise the module from observed completion times and points of confusion.
4. Add installation checks or an environment lock file.
5. Finish `paper.md` and `paper.bib`, keeping the paper focused on educational need and design.
6. Make a tagged release and archive it before or during review as requested by the journal.

Suggested title: **Auditing legacy bioimage analyses: a computational learning module on provenance, sensitivity, and limits of inference**.

## Secondary possibilities

- **PLOS Computational Biology, Education/Quick Tips:** a stretch option after broadening the lesson beyond this case and contacting the Education editors. The article should teach a general audit workflow rather than report the original biological results.
- **F1000Research Method Article or Software Tool Article:** not the first choice. A Method Article ordinarily needs validation and data, while a Software Tool paper needs a clearer novel-tool claim. Both would invite claims the current evidence cannot support.
- **NEUBIAS and the Centre for Open Bioimage Analysis training collections:** useful community dissemination after release, but not substitutes for peer review.

## Explicitly unsuitable positioning

Do not submit this as a bacterial-segmentation benchmark, treatment-effect study, reanalysis of the thesis biology, or validated microscopy method. No public component should imply that synthetic masks establish biological truth.

## Go/no-go checklist

Proceed to public release only if all are **yes**:

- [ ] Contributors and affiliations are confirmed.
- [ ] Code and educational-content licenses are approved by the relevant owners.
- [ ] No thesis-derived or third-party image is included without permission.
- [ ] A fresh install can run the notebook on the synthetic data.
- [ ] Tests pass.
- [ ] The README and paper state that the panels are synthetic and non-biological.

Proceed to JOSE submission only if the release checklist is complete and at least one teaching pilot has been documented.
