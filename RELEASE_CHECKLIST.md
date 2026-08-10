# Public release checklist

## Required decisions

- [x] Confirm the repository owner and final name: `camontefusco/legacy-bioimage-audit`.
- [ ] Confirm authors, contributors, affiliations, and acknowledgements.
- [ ] Confirm ownership of the recovered code and institutional obligations.
- [x] Select an OSI-approved code license: MIT.
- [x] Select an open license for prose and educational graphics: CC BY 4.0.
- [x] Replace `LICENSE_PENDING.md` with the approved license files.
- [x] Update `pyproject.toml` and `CITATION.cff` with the selected license.
- [x] Add a private GitHub reporting form and document it in `SECURITY.md`.

## Technical checks

- [x] Thesis-derived images are excluded.
- [x] Synthetic teaching data are deterministic and included.
- [x] Tests pass locally.
- [x] The teaching notebook runs without private data.
- [x] Repository scan found no credentials or personal filesystem paths.
- [x] Optional GUI dependencies are separated from core installation.
- [x] GitHub Actions passes on Python 3.10 and 3.12 in the public repository.
- [ ] A clean installation is tested on another computer or container.

## JOSE readiness

- [x] Audit current JOSE scope, licensing, paper, and repository requirements.
- [x] Document the 2026-08-10 submission pause in `JOSE_READINESS.md`.
- [ ] Obtain one independent installation or adoption test.
- [ ] Reduce the JOSE submission paper toward the journal's approximately 1,000-word guidance.
- [ ] Confirm final author metadata, funding statement, acknowledgements, and ORCID if applicable.
- [ ] Recheck that JOSE is accepting submissions before filing.

## Archival publication checks

- [x] Pivot `paper.md` to a transition guide from qualitative experimental observation to quantitative data.
- [x] Prepare a data-minimizing 3–5 learner pilot package under `pilot/`.
- [x] Keep current affiliation optional and omit unconfirmed acknowledgements from v0.1.0.
- [x] Complete final citation, credential, personal-path, and public-file audit.
- [x] Create tagged GitHub release `v0.1.0`.
- [x] Archive the release in Zenodo as DOI `10.5281/zenodo.21876822` and add it to `CITATION.cff`.
- [x] Publish the visually verified transition-guide PDF with the archived release.
