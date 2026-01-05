# Patch: Add Mode Integration to Existing MAOs

**Patch ID**: FND-0004
**Status**: Ready
**Applies to**: All MAOs (any contract version)

## Purpose

Add mode selection guidance and arche mode recommendations to an existing MAO that was generated before mode integration support.

**Result:** Each agent in the MAO will have a documented recommended arche mode, with implementation guidance linked from agent manuals.

## What Gets Added

1. **Governance document**: `00_governance/mode-selection-log.md`
   - Summary table of modes used
   - Per-agent mode recommendations with rationale
   - Links to arche mode documentation

2. **Updated agent manuals**: Each `01_agents/<agent-id>/agent-manual.md`
   - New section: "Recommended Implementation Mode"
   - Mode name, rationale, form link
   - Reference to MODE_INTEGRATION_GUIDE.md

3. **Reference guide**: Link to `MODE_INTEGRATION_GUIDE.md` in main README

## Prerequisites

- MAO exists with agent architecture defined
- Agent manuals exist (or can be auto-generated if missing)

## Implementation Steps

### Step 1: Generate Mode Selection Log

Create `00_governance/mode-selection-log.md`:

```markdown
# Mode Selection Log

Generated: [DATE]
MAO Objective: [from scaffold-spec.md]

## Summary

| Mode | Count | Agents |
|------|-------|--------|
| 3-Layer | ? | [list] |
| Agentic-Swarm | ? | [list] |
| Event-Driven | ? | [list] |
| RL-Loop | ? | [list] |

## Decision Methodology

Each agent was analyzed using the decision tree in `../../../modes/foundry/MODE_INTEGRATION_GUIDE.md`.

## Per-Agent Mode Recommendations

### Agent: [Agent Name]
- **Objective**: [from agent manual]
- **Recommended Mode**: [mode name]
- **Maturity**: [✅ Mature / 🚀 Emerging]
- **Rationale**: [2-3 sentences: why this mode fits]
- **Form**: [Link to arche mode form if available]
- **Implementation Status**: Not Started / In Progress / Ready / Active
- **Owner**: [Agent owner]

[Repeat for each agent]

## Mode Combinations in This MAO

If this MAO uses multiple modes working together (hybrid implementation):

- **Primary orchestrator**: [Mode]
- **Sub-agents**: [Mode breakdown]
- **Coordination pattern**: [How modes interact]

## Next Steps

1. Review mode recommendations with team
2. For each agent, follow linked arche mode's INSTRUCTIONS.md
3. Implement agent using mode-specific forms/directives
4. Update implementation status in this log as agents are built

## Questions?

Refer to:
- Decision tree: `../../../modes/foundry/MODE_INTEGRATION_GUIDE.md`
- Arche modes: `../../../modes/3-layer/`, `../../../modes/agentic-swarm/`, etc.
- Mode-specific forms: Each mode has `forms/` directory with templates
```

### Step 2: Update Each Agent Manual

For each agent at `01_agents/<agent-id>/agent-manual.md`:

Add this section after "Mission":

```markdown
## Recommended Implementation Mode

**Mode**: [3-Layer / Agentic-Swarm / Event-Driven / RL-Loop]

**Rationale**: [1-2 sentences explaining why]

**Arche Form**: [Link to appropriate form, e.g., `../../../modes/3-layer/forms/api-service/`]

**Learn more**: `../../../MODE_INTEGRATION_GUIDE.md` — decision tree and detailed mode selection criteria
```

**Example for a deterministic reviewer agent:**

```markdown
## Recommended Implementation Mode

**Mode**: 3-Layer (Mature)

**Rationale**: This agent validates artifacts against rubrics—a deterministic workflow with rule-based logic. 3-Layer mode's directive-based approach provides reliable testing and debugging.

**Arche Form**: `../../../modes/3-layer/forms/automation/` (directive-based workflow)

**Learn more**: `../../../MODE_INTEGRATION_GUIDE.md`
```

### Step 3: Update Main README

Add to MAO's main README (if it exists at `README.md`):

```markdown
## Implementation Modes

This MAO uses arche's multi-mode architecture. Each agent has a recommended implementation mode:

- See `00_governance/mode-selection-log.md` for mode assignments
- See each agent manual (e.g., `01_agents/<agent-name>/agent-manual.md`) for rationale
- Refer to `modes/foundry/MODE_INTEGRATION_GUIDE.md` for mode selection criteria

**Modes used in this MAO:**
[List from mode-selection-log.md summary table]

When implementing an agent:
1. Check its recommended mode in `00_governance/mode-selection-log.md`
2. Read the agent manual (see "Recommended Implementation Mode" section)
3. Go to that mode's INSTRUCTIONS.md (e.g., `modes/3-layer/INSTRUCTIONS.md`)
4. Follow the mode's form templates
```

## Validation Checklist

- [ ] `00_governance/mode-selection-log.md` exists and is complete
- [ ] All agents have recommended modes assigned
- [ ] Each agent manual includes "Recommended Implementation Mode" section
- [ ] All links to arche modes are correct (test locally or on GitHub)
- [ ] Main README mentions mode integration strategy
- [ ] Team has reviewed mode recommendations
- [ ] At least one agent has been implemented following its recommended mode

## Rollback

If mode integration causes confusion:
- Delete `00_governance/mode-selection-log.md`
- Remove "Recommended Implementation Mode" sections from agent manuals
- Remove mode mention from README

## Notes

- This patch is **idempotent**: running it multiple times is safe
- Agent mode recommendations can be updated if team disagrees
- Some agents may require **hybrid modes** (e.g., Agentic-Swarm using 3-Layer sub-agents)—document in mode-selection-log.md

