# Quality and publication-venue review

Review date: 2026-08-11

## Overall assessment

The project is credible as an open, unevaluated self-study resource. Its strongest contribution is not a new image-analysis algorithm; it is an inspectable sequence that teaches experimental scientists to move from qualitative observation to operational definition, measurement, sensitivity analysis, experimental hierarchy, and restrained claims.

The repository is technically stronger than a typical static tutorial: it contains four executable notebooks, deterministic synthetic material, opt-in retrieval of licensed public data, automated tests, notebook-reconstruction checks, provenance and licensing documentation, and explicit evidence boundaries. Eleven tests pass locally, the Python wheel builds without network access, and continuous integration covers Python 3.10 and 3.12.

## Strengths

- The intended learner and prerequisite knowledge are explicit.
- Learning objectives are observable actions rather than vague promises.
- The synthetic case and three public-image cases isolate distinct measurement decisions.
- Numerical examples are labelled as small teaching outputs, not benchmarks.
- The experimental-unit and pseudoreplication discussion is unusually strong for an introductory image-analysis resource.
- Code, original teaching content, and third-party data are separated by license.
- AI assistance and missing legacy-data boundaries are disclosed.

## Quality risks and responses

### 1. Overlap with existing bioimaging guidance

Senft et al. (2023) already provide a broad guide to planning quantitative bioimaging experiments, and Chicco and Shiradkar (2023) provide general tips for computational medical-image analysis. The present resource must not claim that no such guidance exists. Its defensible distinction is narrower and practical: translating one qualitative observation into a complete operational definition, then using executable sensitivity cases to show how plausible choices change the resulting variable. The manuscript now cites and positions itself relative to the Senft et al. guide.

### 2. No learner or usability evaluation

No independent evaluator or learner study is planned. This is acceptable for dissemination as a tutorial or Quick Tips resource if stated plainly, but it makes education-research formats that require assessment results poor targets. The inactive feedback templates are optional and must not be described as completed or planned evaluation.

### 3. Current archive is older than the repository

Zenodo v0.1.0 predates the three published-image notebooks. The DOI is valid for the original archive, but it is not yet an immutable archive of the full current module. A v0.2.0 archive should be created only after the target manuscript and metadata are stable.

### 4. Manuscript format is between genres

At roughly 1,700 words, `paper.md` is too long for current JOSE guidance and not yet organized as PLOS Quick Tips. It is nevertheless close to PLOS Computational Biology's 2,000-2,500-word Education guidance. The long-form transition guide should be preserved; a venue-specific manuscript can be maintained separately.

### 5. Ease of first use

The synthetic notebook is immediately usable, while three notebooks require explicit third-party downloads. This is ethically and legally correct, but it adds friction. The README should continue to distinguish the zero-download synthetic path from the opt-in published-data path. A Binder/Colab route would improve access but is optional and should not be promised until tested.

## Ranked journal options

### 1. PLOS Computational Biology — Education / Quick Tips

**Best active target.** Quick Tips teach specific computational or data-analysis skills, normally run about 2,000-2,500 words, accept 7-15 logically ordered tips, and recommend a summary figure or table. Unsolicited Education submissions are considered at the Education Editor's discretion. PLOS states that Education/Quick Tips front matter has no article-processing charge.

Recommended angle: **“Quick tips for turning qualitative microscopy observations into quantitative data.”** The tips should follow the existing workflow: describe before interpreting; define the construct; preserve experimental hierarchy; make processing choices explicit; inspect masks and intermediate states; test sensitivity; stop claims at the evidence boundary. The notebooks become the worked companion resource rather than purported validation.

Main risk: topical overlap. The manuscript should explicitly distinguish the module from broad quantitative-bioimaging planning guidance and from general medical-image-analysis tips. PLOS currently states that it no longer accepts presubmission enquiries, so this positioning must be strong enough for direct full-manuscript submission.

### 2. Journal of Open Source Education (JOSE) — learning module

**Best structural fit, currently unavailable.** JOSE is designed for open computational learning modules, has no publication fee, and values reusable source materials. The repository meets most openness and technical requirements. However, JOSE currently displays a submission pause, and its paper guidance is around 1,000 words. Keep this route as a fallback only if submissions reopen and the eligibility rules still accept an honestly unevaluated self-study module.

### 3. Journal of Microscopy — Short Review

**Possible microscopy-community route.** A Short Review is approximately 3,000 words, topical, accessible, limited to about ten key references, and authors are advised to contact the General Editor before an unsolicited submission. This route would publish the conceptual guide, not the repository as an educational intervention. It would require a more literature-centred manuscript and fewer references; the executable notebooks would be supplementary resources.

Main risk: the journal prioritizes microscopy techniques and state-of-the-art applications, so editorial interest should be tested before rewriting.

### 4. F1000Research — Opinion Article or Case Study

**Format-compatible but conditional and costly.** Opinion Articles can present an evidence-backed perspective without new research; a Case Study can include an imagined teaching exercise. Current listed charges are US$1,758 for an Opinion Article and US$1,003 for a Case Study, plus applicable tax. F1000Research also states that at least one author must be an active qualified researcher, scholar, or clinician and describes recognized-institution eligibility. This should not be pursued without confirming author eligibility and willingness to pay.

### 5. Journal of Computational Science Education (JOCSE)

**Thematic but weaker fit.** JOCSE publishes computational instructional materials as well as efficacy studies. Its public framing emphasizes successful classroom materials and projects. With no planned implementation evidence, the resource may be screened as premature. An editorial enquiry would be necessary before format conversion.

## Routes not recommended

- **Frontiers in Education, Curriculum, Instruction, and Pedagogy:** the format explicitly asks for results-to-date or assessment processes and is fee-bearing; it creates pressure toward an evaluation claim this project does not have.
- **PLOS Computational Biology Methods or Software:** these require methodological innovation, validation, broad utility, or adoption that the project does not claim.
- **JOSS or Journal of Open Research Software:** the repository is primarily a learning module rather than a significant research-software contribution.
- **Bioimage-analysis method journals:** there is no new validated segmentation or biological method.

## Recommended decision

Prepare and submit a complete PLOS Computational Biology Education manuscript containing seven tip headings, explicit novelty positioning, a summary workflow figure, the repository and archive links, and the statement that no learner-outcomes claim is made. Select article type `Education` and section `General`. Keep JOSE as the no-fee fallback if it reopens.

## Authoritative venue pages checked

- https://journals.plos.org/ploscompbiol/s/other-article-types
- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011689
- https://jose.theoj.org/
- https://openjournals.readthedocs.io/en/jose/submitting.html
- https://onlinelibrary.wiley.com/page/journal/13652818/homepage/forauthors.html
- https://f1000research.com/for-authors/article-guidelines
- https://f1000research.com/for-authors/article-processing-charges
- https://jocse.org/
