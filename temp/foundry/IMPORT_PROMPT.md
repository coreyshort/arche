# Import Prompt (for an AI coding assistant)

You are helping me integrate a new mode called "foundry" into the existing `arche` GitHub repository.

Tasks:
1) In the `arche` repo root, add the folder `modes/foundry/` by copying the contents of this zip's `modes/foundry/` directory.
2) Ensure no files outside `modes/foundry/` are required for Foundry to run (links are ok, dependencies are not).
3) Update arche mode registry docs to mention Foundry:
   - MODE_SELECTION.md
   - AUTONOMOUS_MODE_SELECTION.md
   - MODE_MATURITY.md
   - (optional) AI_QUICKSTART.md and README.md
   Use the snippet in `SNIPPETS/mode-registry-snippet.md`.
4) If `.github/ISSUE_TEMPLATE/improvement.yml` has a constrained dropdown for mode, add `foundry`.
5) If there is an automated label-management workflow, ensure `mode:foundry` and/or `area:foundry` labels exist.
6) Create a PR branch named `feature/foundry-mode` and commit changes with message: "Add Foundry mode scaffold (v0.2)".
7) Provide a brief PR description summarizing what Foundry is and how to start (`modes/foundry/INSTRUCTIONS.md`).
