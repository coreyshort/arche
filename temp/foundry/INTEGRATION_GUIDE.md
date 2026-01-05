# Foundry Mode Seed (v0.2) — Integration Guide (for arche)

**Purpose:** Add Foundry as a new mode under `modes/foundry/` in the `arche` repo.

## What this zip contains
- `modes/foundry/` — Foundry mode scaffold (docs, blueprints, pattern library, patch packs, templates, examples)
- `SNIPPETS/` — paste-in snippets for arche root docs and issue/label plumbing (if needed)
- `IMPORT_PROMPT.md` — a ready prompt for your coding assistant

## Quick install
1) From your `arche` repo root, unzip this archive so it creates:
   - `modes/foundry/**`

2) Add Foundry to arche’s mode registry docs (copy from `SNIPPETS/`):
   - `MODE_SELECTION.md`
   - `AUTONOMOUS_MODE_SELECTION.md`
   - `MODE_MATURITY.md`
   - (optional) `AI_QUICKSTART.md`
   - (optional) root `README.md`

3) If your arche issue template constrains `mode` values:
   - update `.github/ISSUE_TEMPLATE/improvement.yml` to include `foundry`
   - ensure your label workflow (if any) includes `mode:foundry` and/or `area:foundry`

## Mirror-ready later
The mode is self-contained under `modes/foundry/` so you can later subtree-split/publish it as a standalone `foundry` repo.

## Seed date
- 2026-01-04
