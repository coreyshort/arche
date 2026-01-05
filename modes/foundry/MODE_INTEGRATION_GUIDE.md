# Foundry Mode Integration Guide

**Purpose:** Guide Foundry-generated multi-agent organizations (MAOs) to leverage other arche modes (3-Layer, Agentic-Swarm, Event-Driven, RL-Loop) for agent objectives and team structures.

## Overview

Foundry creates **multi-agent organizations**. Each agent in an MAO has:
- **Objective** (what decisions/outputs it owns)
- **Role & responsibilities** (what it does)
- **Interaction patterns** (how it collaborates)

**Each agent can be implemented using an appropriate arche mode** based on its objective and the team context.

---

## Mode-Agent Mapping

### 🚀 **When to Use 3-Layer Mode (Mature)**

**Agent characteristics:**
- ✅ Workflow is well-defined and deterministic
- ✅ Outputs are predictable and testable
- ✅ Clear decision logic (if/then rules, branching)
- ✅ Errors must be caught and handled reliably
- ✅ Team prefers traditional software patterns

**Agent examples in MAOs:**
- **Content Reviewer** — deterministic checks against rubrics
- **Output Validator** — predictable validation logic
- **Report Generator** — templated, structured outputs
- **Request Router** — rule-based request triage
- **Data Processor** — ETL-like transformations
- **API Integrator** — deterministic API call patterns

**Directive structure:**
```
Agent Role: [Content Reviewer]
├─ Input schema
├─ Validation rules (directives)
├─ Output template
├─ Error handling paths
└─ Success criteria
```

**Patch**: If an agent starts deterministic but needs to learn, consider migrating to RL-Loop or adding Event-Driven patterns.

---

### 🚀 **When to Use Agentic-Swarm Mode (Emerging)**

**Agent characteristics:**
- ✅ Agent needs to **coordinate with multiple specialized sub-agents**
- ✅ Problem requires diverse skill domains
- ✅ Emergent problem-solving benefits from collaboration
- ✅ Parallel processing improves outcomes

**Agent examples in MAOs:**
- **Chief Researcher** — coordinates researcher, analyst, synthesizer sub-agents
- **Incident Commander** — orchestrates responders, analyzers, decision-makers
- **Product Strategy Agent** — works with market analyst, engineer liaison, designer liaison
- **Audit Manager** — coordinates multiple auditor roles in parallel

**Swarm structure:**
```
Agent Role: [Chief Researcher]
├─ Sub-agent 1: Literature Researcher (3-Layer)
├─ Sub-agent 2: Data Analyst (3-Layer or RL-Loop)
├─ Sub-agent 3: Synthesizer (Event-Driven or 3-Layer)
└─ Coordination protocol (how sub-agents communicate)
```

**Patch**: Use Agentic-Swarm when agent is complex enough to benefit from delegation to specialized collaborators.

---

### 🚀 **When to Use Event-Driven Mode (Emerging)**

**Agent characteristics:**
- ✅ Agent **reacts to external events** or triggers
- ✅ Works with webhooks, queues, message streams
- ✅ Asynchronous, decoupled processing
- ✅ Real-time responsiveness needed
- ✅ Handles multiple concurrent event streams

**Agent examples in MAOs:**
- **Alert Monitor** — reacts to incoming alerts/anomalies
- **Notification Dispatcher** — triggers based on state changes
- **Event Aggregator** — collects and correlates events
- **Stream Processor** — real-time data transformations
- **Webhook Handler** — processes external system callbacks
- **State Change Responder** — reactive to MAO state transitions

**Event-driven structure:**
```
Agent Role: [Alert Monitor]
├─ Event sources (webhooks, streams, queues)
├─ Event handlers (trigger logic)
├─ Processing pipeline
├─ State updates
└─ Downstream notifications
```

**Patch**: Use Event-Driven when agent's primary role is **reacting to asynchronous triggers**, not orchestrating deterministic workflows.

---

### 🚀 **When to Use RL-Loop Mode (Emerging)**

**Agent characteristics:**
- ✅ Agent should **improve its strategy from outcomes**
- ✅ Optimal approach **unknown upfront**
- ✅ Clear **reward/feedback signal** available
- ✅ Historical data or outcomes to learn from
- ✅ Exploration/exploitation tradeoff acceptable

**Agent examples in MAOs:**
- **Recommendation Agent** — learns user preferences over time
- **Resource Optimizer** — learns optimal allocation strategies
- **Priority Ranker** — learns what gets highest completion rate
- **Skill Matcher** — learns to match people to roles effectively
- **Budget Allocator** — learns optimal spend distribution
- **A/B Test Agent** — learns winning variants

**RL-Loop structure:**
```
Agent Role: [Recommendation Agent]
├─ Strategy/policy (learnable)
├─ Action space (recommendations to try)
├─ Reward signal (user acceptance, business outcome)
├─ Learning cycle (collect feedback → update policy)
├─ Exploration (try new recommendations)
└─ Exploitation (use learned best strategies)
```

**Patch**: Use RL-Loop when agent's value increases **the more it runs** and learns from outcomes.

---

## Mode Selection Decision Tree for Agents

```
START: Analyzing an agent role in the MAO

├─ Is the workflow **deterministic and predictable**?
│  └─ YES → Use 3-Layer Mode ✅
│
├─ Does this agent need to **coordinate with multiple sub-agents**?
│  └─ YES → Use Agentic-Swarm Mode 🚀
│
├─ Is this agent **primarily reactive to events/triggers**?
│  └─ YES → Use Event-Driven Mode 🚀
│
├─ Should this agent **improve from outcomes over time**?
│  └─ YES → Use RL-Loop Mode 🚀
│
└─ Multiple modes apply?
   └─ Combine them: see "Hybrid Agents" below
```

---

## Implementation Pattern: Hybrid Agents

Some agent roles require **combining multiple modes**:

### Example 1: Incident Commander
```
Primary: Agentic-Swarm (coordinates responders)
├─ Sub-agent: Alert Monitor (Event-Driven — reacts to alerts)
├─ Sub-agent: Incident Analyzer (3-Layer — deterministic diagnosis)
├─ Sub-agent: Decision-Maker (3-Layer or RL-Loop — learns best escalations)
└─ Coordination: Swarm protocol managing sub-agents
```

### Example 2: Product Recommendation Engine
```
Primary: RL-Loop (learns user preferences)
├─ State: User profile, historical interactions
├─ Reward: Click-through, conversion, satisfaction
├─ Learning: Improve recommendation strategy
└─ Event layer: Triggered by user events (Event-Driven)
```

### Example 3: Data Operations Manager
```
Primary: 3-Layer (manages deterministic workflows)
├─ Sub-workflows: Each pipeline (ETL, validation, reporting)
├─ Learning layer: RL-Loop tracking pipeline performance
├─ Event layer: Reacting to data freshness alerts
└─ Coordination: Deterministic orchestration
```

---

## How Foundry Implements Mode Selection

### Step 1: Blueprint Designer Recommends Modes
When creating a blueprint, the **Blueprint Designer** agent should:

1. **Analyze each agent role** defined in the architecture
2. **Apply the decision tree** (above) to recommend a mode
3. **Document the rationale** in the agent manual

Example agent manual addition:
```markdown
## Agent: Content Reviewer

### Objective
Validate all outputs against quality rubrics before publication.

### Recommended Mode: 3-Layer (Mature)
- Workflow is deterministic: check against rubric → approve/reject
- Inputs: artifact + rubric; Output: approval status + feedback
- Error handling: catch validation failures, log issues
- Team benefit: Easy to test, reliable, traditional development patterns

### Implementation
- Create a directive at `agents/content-reviewer/directives/validation.md`
- Use 3-layer form: [link to 3-layer form template]
```

### Step 2: Scaffold Includes Mode-Specific Structure
The generated MAO scaffold should reflect the chosen modes:

```
generated-mao/
├─ 01_agents/
│  ├─ content-reviewer/        (3-Layer)
│  │  ├─ directives/
│  │  │  ├─ validation.md
│  │  │  └─ rubric-check.md
│  │  └─ agent-manual.md
│  ├─ incident-commander/      (Agentic-Swarm)
│  │  ├─ swarm-protocol.md
│  │  ├─ sub-agents/
│  │  │  ├─ alert-monitor.md   (Event-Driven)
│  │  │  ├─ analyzer.md        (3-Layer)
│  │  │  └─ decision-maker.md  (RL-Loop)
│  │  └─ agent-manual.md
│  └─ recommender/             (RL-Loop)
│     ├─ learning-config.md
│     ├─ reward-signals.md
│     └─ agent-manual.md
└─ 00_governance/
   └─ mode-selection-log.md    (← NEW: documents mode choices)
```

### Step 3: Mode Selection Log
Each MAO should include a **mode-selection-log.md** documenting:

```markdown
# Mode Selection Log

## Summary
- Total agents: 5
- 3-Layer: 3 agents (deterministic roles)
- Agentic-Swarm: 1 agent (orchestrator)
- Event-Driven: 2 agents (reactive)
- RL-Loop: 1 agent (learning-based)

## Per-Agent Decisions

### Agent: Content Reviewer
- **Recommended Mode**: 3-Layer (Mature)
- **Rationale**: Deterministic validation against rubrics
- **Justification**: Error rates must be minimal; workflow is rule-based
- **Form Used**: [link to 3-layer form]
- **Status**: Ready for implementation

### Agent: Incident Commander
- **Recommended Mode**: Agentic-Swarm (Emerging)
- **Rationale**: Coordinates 3 specialized responders
- **Justification**: Benefits from parallel analysis and collaboration
- **Sub-agents**: [list with their modes]
- **Status**: Ready for implementation

...
```

---

## Templates & Forms

### New: Agent Implementation Template
**File:** `modes/foundry/07_templates/agent-implementation.template.md`

```markdown
# Agent Implementation

## Metadata
- Agent name:
- Mode:
- Objective:
- Status: Not Started / In Progress / Ready

## Mode Details
[Include mode-specific structure based on selected mode]

### If 3-Layer:
- Directives: [list]
- Input schema:
- Output schema:

### If Agentic-Swarm:
- Sub-agents: [list]
- Coordination protocol:

### If Event-Driven:
- Event sources:
- Event handlers:

### If RL-Loop:
- Action space:
- Reward signal:
- Learning mechanism:

## Testing & Validation
- [ ] Satisfies agent objective
- [ ] Passes mode-specific tests
- [ ] Integrated with MAO workflow
- [ ] Documented in agent manual
```

### Updated: Agent Manual Template
**File:** `modes/foundry/07_templates/agent-manual.template.md` (UPDATED)

Add section:
```markdown
## Recommended Implementation Mode
- **Mode**: [3-Layer / Agentic-Swarm / Event-Driven / RL-Loop]
- **Rationale**: [Why this mode fits this agent role]
- **Form**: [Link to arche form]
- **Status**: Ready to implement
```

---

## Patch Pack: Add Mode Integration
**File:** `modes/foundry/04_patch-packs/FND-0004-add-mode-integration.md` (NEW)

```markdown
# Patch: Add Mode Integration to Existing MAOs

## Purpose
Add mode selection guidance and scaffold to an existing MAO.

## Changes
1. Create `00_governance/mode-selection-log.md`
2. Update each agent manual with recommended mode
3. Add mode-specific structure (directives, configs, etc.)
4. Link to relevant arche form documentation

## Implementation Steps
[detailed walkthrough]

## Validation
- [ ] Mode selection log exists and is complete
- [ ] Each agent manual documents recommended mode
- [ ] Mode-specific structures are created
- [ ] Links to arche forms are correct
```

---

## Integration with Arche Forms

When Foundry recommends a mode for an agent, it should also suggest the appropriate **form** from that mode:

### 3-Layer Mode Forms
- **api-service** — for API-based agent roles
- **cli-tool** — for command-line driven agent roles
- **library** — for reusable agent logic
- **automation** — for workflow automation agents

### Agentic-Swarm Mode Forms
- Use swarm coordination templates
- Link to agentic-swarm documentation

### Event-Driven Mode Forms
- Event handler templates
- Stream processing guides

### RL-Loop Mode Forms
- Learning policy templates
- Reward signal design guides

---

## Example: Complete Agent with Mode

### Agent Manual (Updated)

```markdown
# Chief Researcher Agent

## Objective
Synthesize research into actionable insights by coordinating specialized researchers.

## Role
Orchestrates parallel research across domains (literature, data, market analysis).

## Recommended Implementation Mode: Agentic-Swarm (Emerging)

### Rationale
- Coordinates 3+ specialized sub-agents with distinct expertise
- Emerges better insights from collaboration than single agent
- Parallel processing of research domains
- Clear interface contracts between agents

### Form: Agentic-Swarm Mode
- **Entry point**: `modes/agentic-swarm/INSTRUCTIONS.md`
- **Example**: See `modes/agentic-swarm/forms/` for similar coordinator patterns

### Sub-Agents & Their Modes

1. **Literature Researcher**
   - Mode: 3-Layer (deterministic search + synthesis)
   - Form: cli-tool (query construction, scraping)

2. **Data Analyst**
   - Mode: 3-Layer or RL-Loop (learns patterns)
   - Form: library (statistical analysis, visualization)

3. **Market Intelligence Agent**
   - Mode: RL-Loop (improves predictions from feedback)
   - Form: Custom (learns market trends)

### Swarm Protocol
[Coordination rules, handoff protocols, output integration]

## Implementation Checklist
- [ ] Study Agentic-Swarm mode
- [ ] Define sub-agent interfaces
- [ ] Implement each sub-agent with its mode
- [ ] Build coordination layer
- [ ] Test swarm interaction patterns
```

---

## Quick Reference: Mode at a Glance

| Aspect | 3-Layer | Agentic-Swarm | Event-Driven | RL-Loop |
|--------|---------|---------------|--------------|---------|
| **Best for agent role** | Deterministic workflows | Orchestrating sub-agents | Reactive/async | Learning strategies |
| **Implementation ease** | Easy | Moderate | Moderate | Hard |
| **Maturity** | ✅ Mature | 🚀 Emerging | 🚀 Emerging | 🚀 Emerging |
| **Testing** | Easy | Moderate | Hard | Hard |
| **Debugging** | Easy | Challenging | Challenging | Challenging |
| **Typical MAO agent count** | 3-5 | 1-2 (coordinators) | 2-4 (monitors/handlers) | 1-3 (optimizers) |

---

## How to Use This Guide

### For Blueprint Designers
1. Review agent roles defined in the objective
2. Apply decision tree to recommend mode for each
3. Document in agent manuals
4. Create mode-selection-log.md

### For MAO Implementers
1. Read agent manual → see recommended mode
2. Go to that mode's INSTRUCTIONS.md
3. Follow mode-specific form for implementation
4. Reference agent objective in mode-specific directives/config

### For Pattern Librarians
1. Track which mode combinations work well together
2. Identify anti-patterns (modes that clash)
3. Propose new MAO blueprints based on proven mode combinations
4. Share learnings in pattern library

---

## Anti-Patterns

### ❌ Using 3-Layer for Everything
- Problem: Misses opportunities for specialization, learning, reactivity
- Solution: Apply decision tree; use specialized modes for complex agents

### ❌ Using Agentic-Swarm for Single Objective Agents
- Problem: Unnecessary complexity; adds coordination overhead
- Solution: Use 3-Layer for deterministic single-objective agents

### ❌ Ignoring Event-Driven Opportunities
- Problem: Polling or synchronous patterns where async is more natural
- Solution: Identify reactive agents; use Event-Driven mode

### ❌ Not Learning from Outcomes
- Problem: RL-Loop creates complexity; team forgets to use it
- Solution: Explicitly define reward signals; use RL-Loop for optimizable roles

---

## Future Enhancements

- **Mode compatibility matrix**: Which modes work well together in an MAO
- **Migration guide**: Promoting agent from one mode to another (e.g., 3-Layer → RL-Loop)
- **Performance profiles**: Which mode combinations scale best
- **Cost analysis**: Computational cost of each mode in production MAOs

