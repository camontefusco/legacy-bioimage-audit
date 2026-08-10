# Public release checklist

## Required decisions

- [x] Confirm the repository owner and final name: `camontefusco/legacy-bioimage-audit`.
- [ ] Confirm authors, contributors, affiliations, and acknowledgements.
- [ ] Confirm ownership of the recovered code and institutional obligations.
- [x] Select an OSI-approved code license: MIT.
- [x] Select an open license for prose and educational graphics: CC BY 4.0.
- [x] Replace `LICENSE_PENDING.md` with the approved license files.
- [x] Update `pyproject.toml` and `CITATION.cff` with the selected license.
- [ ] Add a private conduct-reporting email address or form.

## Technical checks

- [x] Thesis-derived images are excluded.
- [x] Synthetic teaching data are deterministic and included.
- [x] Tests pass locally.
- [x] The teaching notebook runs without private data.
- [x] Repository scan found no credentials or personal filesystem paths.
- [x] Optional GUI dependencies are separated from core installation.
- [ ] GitHub Actions passes on the public repository.
- [ ] A clean installation is tested on another computer or container.

## Publication checks

- [ ] Replace placeholder author/affiliation fields in `paper.md`.
- [ ] Complete and document at least one teaching pilot.
- [ ] Revise the module in response to pilot findings.
- [ ] Create a tagged GitHub release.
- [ ] Archive the release in Zenodo and add the DOI to `CITATION.cff`.
- [ ] Submit the archived module and `paper.md` to JOSE.
