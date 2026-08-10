# JOSE submission-readiness audit

Audit date: 2026-08-10

## Current decision

The module is a plausible Journal of Open Source Education (JOSE) learning-module submission, but it should not be submitted while JOSE displays its current notice that submissions are paused pending eligibility changes.

## Requirements already met

- Public Git repository with browsable source, issue tracking, and contribution guidance.
- Original learning content under CC BY 4.0 and code under the OSI-approved MIT license.
- Executable computational learning materials rather than a syllabus or static notes.
- Clear audience, prerequisites, learning objectives, instructional sequence, adoption route, and limitations.
- `paper.md`, `paper.bib`, author and affiliation metadata, key references, and an archive DOI.
- Deterministic synthetic exercise plus opt-in public-data cases; third-party data are not redistributed.
- Automated tests on Python 3.10 and 3.12 and reconstruction checks for all notebooks.
- Explicit AI-assistance disclosure and conservative evidence boundaries.

## Remaining pre-submission items

1. Recheck JOSE's eligibility and submission status before filing.
2. Obtain at least one documented independent installation/adoption test. JOSE asks how a module has been used; the manuscript must continue to state honestly that learner outcomes have not been evaluated.
3. Reduce the paper toward JOSE's current guidance of about 1,000 words while preserving the longer transition guide as project documentation.
4. Confirm the final author name, affiliation, ORCID (if available), funding statement, acknowledgements, and contributor list.
5. Create a new versioned archive only when the post-review or submission-stage repository state is stable. Do not overwrite the existing v0.1.0 archive.

## Evidence boundary for editors and reviewers

The contribution is the instructional design and inspectable computational module. It is not a new segmentation method, a biological validation study, a benchmark, or evidence that the module improves learner outcomes.

## Authoritative references checked

- JOSE scope and current status: https://jose.theoj.org/
- JOSE scope and licensing: https://jose.theoj.org/about
- JOSE author guidance: https://openjournals.readthedocs.io/en/jose/submitting.html
