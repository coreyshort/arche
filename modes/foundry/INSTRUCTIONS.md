# Foundry Instructions

Use Foundry to create a self-learning multi-agent scaffold.

## 0) Choose a starting point
- If a blueprint exists for your domain: start in `02_blueprints/`
- Otherwise: start with `07_templates/blueprint.template.md`

## 1) Define the request (copy/paste)
Provide:
- Objective (what decisions/outputs must improve)
- In/Out of scope
- Target users (personas/roles)
- Constraints (tooling, security, cadence)
- Frameworks/standards to align to (optional)
- Key dimensions (pick 3–6; Foundry can propose)
- Desired agent footprint (near-term minimal vs ideal)

## 2) Foundry produces
1) Agent architecture (near-term + ideal) + hierarchy
2) Folder/file scaffold (all .md) + `00_governance/scaffold-spec.md`
3) Templates for recurring outputs
4) Learning system (`09_learning/` rubrics + eval suite + scorecards)
5) Meta contract (`10_meta/` export + upgrade log)

## 3) First-week loop
- Produce 1–2 real artifacts using the new org
- Log feedback in `09_learning/feedback-log.md`
- Triage into `issue-backlog.md`
- Ship 1 change request
- Run 1 eval scenario and record score

## 4) Improve and upgrade
- Add one dimension at a time
- Add eval scenarios before adding lots of new agents
- Apply patch packs for upgrades (`04_patch-packs/`)
