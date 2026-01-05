# Patch Pack: FND-0003 Add scaffold spec

## Applies to
- MAOs missing `00_governance/scaffold-spec.md`

## Pre-checks
- `00_governance/` exists; if not, create it minimally (ownership + naming + decisions)

## Changes (idempotent)
1) Create `00_governance/scaffold-spec.md`
2) Populate with current `.md` file paths (path | owner | stub)
3) Add a note: treat scaffold-spec as canonical for generation

## Validation
- Confirm generator can create missing files without overwriting existing ones
