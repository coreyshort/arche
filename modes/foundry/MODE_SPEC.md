# Foundry Mode Spec

## Purpose
Foundry creates and evolves **multi-agent organizations (MAOs)** for a given objective.

## Non-negotiables (every generated MAO)
1) Mode integration: `00_governance/mode-selection-log.md` documents recommended arche mode for each agent.
2) Learning loop: `09_learning/` with feedback log, issue backlog, CRs, rubrics, eval scenarios, scorecards.
3) Meta contract: `10_meta/` with `FOUNDRY_CONTRACT.md`, `feedback-export.md`, `upgrade-log.md`.
4) Ownership + scaffold spec: `00_governance/file-ownership.md` and `00_governance/scaffold-spec.md`.
5) Every primary artifact type has a rubric.
6) Eval suite minimum: 3 scenarios representing top intersections of the selected dimensions.

## Inputs (structured but flexible)
A) Objective & outcomes
B) Scope boundaries
C) Stakeholders/personas
D) Standards/frameworks (optional)
E) Dimensions (Foundry proposes; user selects 3–6)
F) Desired footprint (near-term vs ideal)

## Outputs (always)
- Scaffold + seed content (all .md)
- Agent manuals (roles + ownership)
- Templates for recurring outputs
- Learning system (rubrics + eval suite + scorecards)
- Upgrade mechanism (patch packs) + contract folder

## Compatibility
- Contract version stored in each MAO at `10_meta/FOUNDRY_CONTRACT.md`
- Upgrades are idempotent and logged in `10_meta/upgrade-log.md`
