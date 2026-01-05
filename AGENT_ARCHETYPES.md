# Agent Archetype Library

**Purpose:** Pre-built agent patterns that can be used in Foundry-generated MAOs, with recommended implementations and example configurations.

---

## What is an Agent Archetype?

An archetype is a **reusable agent pattern** that solves a common problem across domains:
- **Objective:** What the agent is trying to accomplish
- **Responsibilities:** What it owns
- **Recommended mode:** How to implement it (with alternatives)
- **Template:** Copy-paste starting point for agent manual
- **Examples:** Real-world uses in different domains

Think of archetypes as **agent personas** — just like product design has "user archetypes," agent systems have reusable agent patterns.

---

## Core Archetypes

### 1. The Deterministic Executor

**Purpose:** Reliably execute well-defined workflows with zero tolerance for error

**Responsibilities:**
- Execute step-by-step procedures
- Validate inputs against rules
- Handle errors gracefully
- Log all actions
- Report outcomes

**Recommended mode:** 🟢 3-Layer (Mature)

**Use cases:**
- Data processor (ETL)
- Order fulfiller
- Report generator
- API integrator
- Validator
- Content reviewer

**Implementation template:**
```markdown
# Agent: [Name] (Executor)

## Objective
Execute [procedure] reliably, handling errors gracefully.

## Recommended mode: 3-Layer

## Directives
- `directives/validate-input.md` — Input validation rules
- `directives/process-workflow.md` — Step-by-step procedure
- `directives/handle-errors.md` — Error recovery
- `directives/report-outcome.md` — Reporting format

## Success metrics
- Error rate < 0.1%
- Completion rate > 99.5%
- Audit trail complete
- All errors logged and categorized
```

**Why 3-Layer?**
- Workflow is deterministic
- Errors must be caught and handled reliably
- Easy to test and debug
- Audit trail is critical

**Alternative modes:**
- Event-Driven: If triggered by events instead of scheduled
- 3-Layer with RL-Loop wrapper: If success rate improves from feedback

---

### 2. The Learner

**Purpose:** Improve strategy from outcomes; find optimal approach

**Responsibilities:**
- Maintain action policy
- Execute actions and observe outcomes
- Update policy based on reward signal
- Explore new strategies
- Track learning progress

**Recommended mode:** 🚀 RL-Loop (Emerging)

**Use cases:**
- Recommender engine
- Price optimizer
- Resource allocator
- Skill matcher
- Priority ranker
- Parameter tuner

**Implementation template:**
```markdown
# Agent: [Name] (Learner)

## Objective
Learn optimal [strategy] from [reward signal].

## Recommended mode: RL-Loop

## Learning setup
- **Action space:** [List possible actions/decisions]
- **State space:** [What info informs decisions]
- **Reward signal:** [How to measure success]
- **Learning algorithm:** [Bandit / Q-learning / Policy gradient]
- **Exploration strategy:** [How to discover new actions]

## Success metrics
- Learning curve: [Expected improvement trajectory]
- Convergence: [When to stop updating policy]
- Stability: [Low variance in recent decisions]
- Interpretability: [Can humans understand learned policy?]
```

**Why RL-Loop?**
- Optimal strategy unknown upfront
- Reward signal available from outcomes
- System improves with experience
- Exploration/exploitation tradeoff needed

**Alternative modes:**
- 3-Layer with heuristics: If domain knowledge is strong enough
- RL-Loop + 3-Layer wrapper: If some rules are non-negotiable

---

### 3. The Orchestrator

**Purpose:** Coordinate multiple specialized agents toward shared goal

**Responsibilities:**
- Understand incoming request/goal
- Decompose into sub-tasks
- Assign to appropriate sub-agents
- Collect and synthesize results
- Report outcome

**Recommended mode:** 🚀 Agentic-Swarm (Emerging)

**Use cases:**
- Chief researcher
- Incident commander
- Project manager
- Product strategist
- Audit manager
- Sales coordinator

**Implementation template:**
```markdown
# Agent: [Name] (Orchestrator)

## Objective
Coordinate [sub-agents] to accomplish [goal].

## Recommended mode: Agentic-Swarm

## Sub-agents
- **[Agent 1]** (mode: 3-Layer) — Responsible for [task]
- **[Agent 2]** (mode: 3-Layer) — Responsible for [task]
- **[Agent 3]** (mode: Event-Driven) — Responsible for [task]

## Coordination protocol
1. **Request intake:** Parse incoming goal
2. **Task decomposition:** Break into sub-tasks
3. **Assignment:** Route to appropriate agent
4. **Parallel execution:** Agents work concurrently
5. **Synthesis:** Combine results
6. **Output:** Return synthesized result

## Success metrics
- All sub-tasks completed
- Synthesis quality: [rubric]
- Time-to-completion
- Sub-agent utilization balanced
```

**Why Agentic-Swarm?**
- Multiple specialized agents needed
- Parallel work improves efficiency
- Coordination rules are clear
- Emergent behavior from specialization

**Alternative modes:**
- 3-Layer: If coordination can be fully deterministic
- Agentic-Swarm + RL-Loop: If coordination strategy should learn

---

### 4. The Monitor

**Purpose:** Detect anomalies or state changes; trigger responses

**Responsibilities:**
- Observe system state or streams
- Detect conditions of interest
- Trigger alerts or actions
- Handle escalation
- Learn what triggers matter

**Recommended mode:** 🚀 Event-Driven (Emerging)

**Use cases:**
- Alert monitor
- Anomaly detector
- Health checker
- Inventory watcher
- Notification dispatcher
- State change responder

**Implementation template:**
```markdown
# Agent: [Name] (Monitor)

## Objective
Detect [conditions] and trigger [responses].

## Recommended mode: Event-Driven

## Event sources
- **[Source 1]:** [Description]
- **[Source 2]:** [Description]

## Event handlers
- **On [event type 1]:** [Action]
- **On [event type 2]:** [Action]
- **On [event type 3]:** [Action]

## Escalation rules
- **Level 1:** [Condition] → [Action]
- **Level 2:** [Condition] → [Action]
- **Level 3:** [Condition] → [Action]

## Success metrics
- Detection latency < [time]
- False positive rate < [threshold]
- All escalations logged
- Response time < [time]
```

**Why Event-Driven?**
- Reacts to asynchronous triggers
- Needs to handle multiple concurrent events
- Decoupled from event sources
- Natural fit for streaming data

**Alternative modes:**
- Event-Driven + RL-Loop: If detection rules should learn
- 3-Layer: If events come in known sequence/patterns

---

### 5. The Validator

**Purpose:** Check quality, compliance, or correctness of artifacts

**Responsibilities:**
- Receive artifact to validate
- Apply validation rules
- Score against rubric
- Provide feedback
- Escalate if issues found

**Recommended mode:** 🟢 3-Layer (Mature)

**Use cases:**
- Content reviewer
- Code quality checker
- Compliance auditor
- Data validator
- Test scorer
- Rubric applier

**Implementation template:**
```markdown
# Agent: [Name] (Validator)

## Objective
Validate [artifact type] against [rubric].

## Recommended mode: 3-Layer

## Validation directives
- `directives/apply-rubric.md` — Scoring rules
- `directives/identify-issues.md` — Issue categories
- `directives/provide-feedback.md` — Feedback format
- `directives/escalation-rules.md` — When to escalate

## Rubric reference
- **Rubric:** `09_learning/rubrics/[artifact]-quality.md`
- **Scoring:** [1-5 scale]
- **Pass threshold:** [e.g., >= 3]

## Success metrics
- Validation time < [threshold]
- Consistency: [Inter-rater reliability if human-validated]
- Issue detection rate
- False positive rate
```

**Why 3-Layer?**
- Rules are deterministic
- Consistent scoring critical
- Easy to test and debug
- Audit trail needed

**Alternative modes:**
- 3-Layer + RL-Loop: If rubric weights should learn from feedback
- Event-Driven: If validation triggered by state changes

---

### 6. The Synthesizer

**Purpose:** Combine inputs from multiple sources into coherent output

**Responsibilities:**
- Receive inputs from multiple sources
- Integrate and reconcile
- Create synthesis
- Handle conflicts
- Report output

**Recommended mode:** 🚀 Agentic-Swarm or 3-Layer (depends on synthesis complexity)

**Use cases:**
- Report synthesizer
- Decision maker
- Proposal writer
- Insight generator
- Strategy formulator
- Recommendation aggregator

**Implementation template:**
```markdown
# Agent: [Name] (Synthesizer)

## Objective
Synthesize [inputs] into [output format].

## Recommended mode: [3-Layer for simple | Agentic-Swarm for complex]

### If 3-Layer:
- `directives/intake-inputs.md` — Input formats
- `directives/integration-rules.md` — How to combine
- `directives/conflict-resolution.md` — How to handle disagreement
- `directives/format-output.md` — Output template

### If Agentic-Swarm:
- **Analyzer sub-agent** (3-Layer) — Parse each input
- **Reconciler sub-agent** (3-Layer) — Resolve conflicts
- **Formatter sub-agent** (3-Layer) — Format output
- **Coordinator** (Agentic-Swarm) — Orchestrate them

## Success metrics
- Synthesis quality: [rubric score]
- Time to synthesize
- Conflict resolution accuracy
- Output consistency
```

**Why 3-Layer for simple, Agentic-Swarm for complex?**
- Simple: Clear rules for combining inputs → 3-Layer
- Complex: Multiple resolution strategies → Agentic-Swarm (sub-agents)

---

### 7. The Router

**Purpose:** Categorize inputs and route to appropriate handlers

**Responsibilities:**
- Receive input
- Extract features / classify
- Route to appropriate next step
- Handle misclassifications
- Log routing decisions

**Recommended mode:** 🟢 3-Layer (Mature) or 🚀 RL-Loop (Emerging)

**Use cases:**
- Request router
- Task classifier
- Priority assigner
- Skill matcher
- Load balancer
- Incident categorizer

**Implementation template (3-Layer):**
```markdown
# Agent: [Name] (Router)

## Objective
Route [input type] to appropriate [handler].

## Recommended mode: 3-Layer

## Routing directives
- `directives/classify-input.md` — Classification rules
- `directives/route-decisions.md` — Routing logic
- `directives/fallback-handler.md` — Unknown input handling
- `directives/log-routes.md` — Decision logging

## Categories and routes
- **[Category 1]** → [Handler 1]
- **[Category 2]** → [Handler 2]
- **[Category 3]** → [Handler 3]
- **Unknown** → [Default/escalate]

## Success metrics
- Classification accuracy > [threshold]
- Routing latency < [time]
- Misclassification rate < [threshold]
```

**Implementation template (RL-Loop):**
```markdown
# Agent: [Name] (Smart Router)

## Objective
Learn optimal routing strategy from handler success rates.

## Recommended mode: RL-Loop

## Action space
- Route to [handler 1]
- Route to [handler 2]
- Route to [handler 3]
- Escalate to human

## Reward signal
- [Handler success] → +10
- [Handler failure] → -5
- [Escalation] → +2

## Learning
- Update routing weights based on outcomes
- Explore new routes occasionally
- Decay old learning over time
```

**Why 3-Layer vs RL-Loop?**
- 3-Layer: Routing rules are stable and well-known
- RL-Loop: Success rates differ; learn which routes work best

---

### 8. The Advisor

**Purpose:** Provide recommendations or guidance; doesn't execute

**Responsibilities:**
- Understand context
- Analyze situation
- Generate recommendations
- Explain reasoning
- Learn from user feedback

**Recommended mode:** 🚀 RL-Loop or 3-Layer with feedback loop

**Use cases:**
- Strategy advisor
- Decision support
- Recommendation engine
- Best practice suggester
- Risk analyzer
- Opportunity identifier

**Implementation template:**
```markdown
# Agent: [Name] (Advisor)

## Objective
Provide [type] recommendations based on [context].

## Recommended mode: RL-Loop (learns what advice is taken) or 3-Layer (static recommendations)

## Analysis dimensions
- **[Dimension 1]:** [Analysis]
- **[Dimension 2]:** [Analysis]
- **[Dimension 3]:** [Analysis]

## Recommendation generation
- [Algorithm or heuristics for recommendations]

## Feedback loop (RL-Loop only)
- **Reward signal:** User acceptance of advice
- **Learning:** Update recommendation weights
- **Exploration:** Try new recommendations occasionally

## Success metrics
- Advice acceptance rate > [threshold]
- User outcome improvement
- Reasoning clarity
```

---

## Archetype Selection Quick Reference

| Problem | Archetype | Mode | Key Traits |
|---------|-----------|------|-----------|
| Execute deterministic workflow | Executor | 3-Layer | Reliable, testable, audit trail |
| Improve from feedback | Learner | RL-Loop | Adaptive, explorative, convergent |
| Coordinate sub-agents | Orchestrator | Agentic-Swarm | Parallel, specialized, emergent |
| React to events | Monitor | Event-Driven | Async, decoupled, low latency |
| Ensure quality | Validator | 3-Layer | Consistent, rule-based, scorable |
| Combine multiple inputs | Synthesizer | 3-Layer or Swarm | Integrative, conflict-resolving |
| Categorize & dispatch | Router | 3-Layer or RL-Loop | Efficient, learnable, scalable |
| Recommend options | Advisor | RL-Loop or 3-Layer | Insightful, explainable, adaptive |

---

## Using Archetypes in Foundry

### Step 1: Identify Agent Roles
From your MAO objective, list all agent roles needed:
- Who detects anomalies? (Monitor)
- Who executes workflows? (Executor)
- Who coordinates? (Orchestrator)
- etc.

### Step 2: Match to Archetypes
For each role, find the closest archetype

### Step 3: Customize Template
- Copy archetype template
- Fill in specifics (what to execute, what to validate, etc.)
- Adjust recommended mode if needed

### Step 4: Implement with Mode
- Go to recommended mode's INSTRUCTIONS.md
- Use mode-specific form
- Reference archetype implementation template

---

## Creating Custom Archetypes

If you discover a new agent pattern:

1. **Name it:** Give it a clear name (e.g., "The Conflict Resolver")
2. **Document purpose:** What problem does it solve?
3. **List responsibilities:** What does it own?
4. **Recommend mode:** Which mode fits best?
5. **Provide template:** Copy-paste starting point
6. **Share example:** Real-world use case
7. **Contribute to arche:** GitHub Issue with `archetype` label

---

## Anti-Patterns

### ❌ Archetype Mismatch
- Using Executor (3-Layer) for something that needs learning (RL-Loop)
- Using Monitor (Event-Driven) for deterministic task (use Executor)

**Fix:** Match archetype to actual need

### ❌ Archetype Overload
- Single agent trying to be Executor + Learner + Orchestrator

**Fix:** Decompose into multiple specialized agents

### ❌ Missing Archetype
- Building bespoke agent for common problem

**Fix:** Check archetype library first; customize existing pattern

---

## Next Steps

1. **Use in your MAO:** Pick agent roles, match to archetypes, implement
2. **Share patterns:** If you create custom archetype, contribute back
3. **Improve templates:** If archetype template could be better, open issue
4. **Discover gaps:** If you need archetype that doesn't exist, suggest it

---

