# Contributing

Contributions that improve reproducibility, accessibility, teaching clarity, tests, or documentation are welcome after the repository is publicly licensed.

## Before proposing a change

- Do not add patient, participant, confidential, or unpublished laboratory data.
- Do not add thesis-derived or third-party images without documented redistribution permission.
- Do not introduce biological performance or treatment-effect claims that the available evidence cannot support.
- Use synthetic or clearly licensed examples for new exercises.

## Development check

```bash
python -m pip install -e '.[test]'
pytest
python scripts/generate_synthetic_panels.py
python scripts/create_educational_sensitivity_notebook.py
```

Describe the educational purpose of the change, the checks performed, and any effect on the claim boundary. For changes based on teaching experience, summarize the relevant pilot observation without identifying learners.
