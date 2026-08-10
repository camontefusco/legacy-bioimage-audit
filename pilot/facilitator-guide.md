# Facilitator guide

## Before the session

1. Schedule 90 minutes even if the planned exercise is shorter.
2. Recruit 3–5 adult learners.
3. Replace placeholders in `invitation.md`.
4. Record the repository commit in `session-record.md`.
5. On a clean environment, run:

   ```bash
   git clone https://github.com/camontefusco/legacy-bioimage-audit.git
   cd legacy-bioimage-audit
   python -m venv .venv
   source .venv/bin/activate
   pip install -e '.[test]'
   pytest
   jupyter notebook notebooks/01_educational_sensitivity_analysis.ipynb
   ```

6. Prepare a fallback shared environment in case installation consumes the session.
7. Do not distribute or display excluded thesis panels.

## Session schedule

- 0–10 min: explain the purpose, synthetic-data boundary, and voluntary feedback.
- 10–20 min: installation and notebook orientation.
- 20–55 min: independent or paired notebook work.
- 55–70 min: learner worksheet and group discussion.
- 70–80 min: feedback form.
- 80–90 min: buffer and close-out.

## Facilitation rules

- Let learners attempt each task before giving an answer.
- Record where help was needed, not who needed it.
- Do not teach that one segmentation configuration is biologically correct.
- Reinforce that mask overlap measures agreement without providing ground truth.
- Stop any discussion that treats panels as independent biological replicates.
- Do not collect names, email addresses, demographic details, or screen recordings in the pilot record.

## Core observations

Record counts, not identities:

- learners who opened the notebook;
- learners who completed the configuration comparison;
- learners who correctly explained agreement versus accuracy;
- learners who identified the panel as the unit of description;
- learners who named at least one prohibited biological claim;
- installation and execution problems;
- cells, labels, or prompts requiring facilitator explanation.

## After the session

1. Aggregate answers into `session-record.md`.
2. Remove any accidental identifying information.
3. Convert recurring problems into GitHub issues.
4. Make and test revisions.
5. Link revision commits in the session record.
6. Update the `Experience of use` section in `paper.md` descriptively.
