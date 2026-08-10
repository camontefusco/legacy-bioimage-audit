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

## Archival publication checks

- [x] Pivot `paper.md` to a technical report that does not claim educational effectiveness.
- [x] Prepare a data-minimizing 3–5 learner pilot package under `pilot/`.
- [ ] Confirm acknowledgements and optional current affiliation.
- [ ] Complete final citation and public-file audit.
- [ ] Create a tagged GitHub release.
- [ ] Archive the release in Zenodo and add the DOI to `CITATION.cff`.
- [ ] Publish the technical report with the archived release.
