# Patch Pack: FND-0001 Add 10_meta contract folder

## Applies to
- MAOs missing `10_meta/` or missing contract files

## Pre-checks
- `09_learning/` exists (if not, apply FND-0002 first)
- `00_governance/` exists

## Changes (idempotent)
1) Create `10_meta/FOUNDRY_CONTRACT.md` from Foundry contract template
2) Create `10_meta/feedback-export.md` from feedback export template
3) Create `10_meta/upgrade-log.md` from upgrade log template
4) Add these paths to `00_governance/scaffold-spec.md` (if present)

## Validation
- Run 1 eval scenario (if eval suite exists)
- Record outcome in `10_meta/upgrade-log.md`
