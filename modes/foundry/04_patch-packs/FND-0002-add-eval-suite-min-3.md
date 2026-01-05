# Patch Pack: FND-0002 Add eval suite (minimum 3 scenarios)

## Applies to
- MAOs missing `09_learning/eval/` or missing scenario suite

## Pre-checks
- `09_learning/` exists; if not, create it with feedback log, issues, CRs, rubrics folder

## Changes (idempotent)
1) Create `09_learning/eval/scenario-suite.md`
2) Create 3 scenario files in `09_learning/eval/scenarios/`
3) Create scorecards in `09_learning/eval/scorecards/`
4) (Optional) Create golden stubs in `09_learning/eval/golden/`

## Validation
- Score at least one artifact against a rubric and log to scorecard
