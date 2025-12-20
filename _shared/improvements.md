# Recommended Improvements

> This file captures suggested enhancements to the agent instruction set based on real-world usage and learnings.

## How to Use This File

**Purpose:** Track learnings from AI interactions to continuously improve agent instructions.

**When to update:**
- After completing a complex multi-step task
- When discovering gaps in current instructions
- When encountering repeated errors or inefficiencies
- After creating new tools or workflows

**Process:**
1. AI discovers an issue or learns something during conversation
2. AI adds a new numbered section below with the improvement suggestion
3. User reviews and approves/rejects suggestions
4. Approved suggestions get implemented into AGENTS.md or INIT_ENV.md
5. Implemented suggestions are marked with status and date

## Template for New Suggestions

```markdown
### [Number]. [Short Title]

**Suggestion:** [What to add/change]

**Rationale:** [Why it's needed - what problem it solves]

**Proposed Addition:** [Actual text/code to add to AGENTS.md or INIT_ENV.md]

**Status:** [Proposed / Approved / Implemented / Rejected]

**Date:** [When added to this file]
```

## Review Checklist

Before implementing any suggestion:
- [ ] Does it solve a real problem encountered in practice?
- [ ] Is it specific enough to be actionable?
- [ ] Does it align with the 3-layer architecture principles?
- [ ] Will it actually improve future AI agent performance?
- [ ] Is it documented clearly enough for an AI to understand?
