# Mode Compatibility & Integration Guide

**Purpose:** Document how arche modes work together, when they complement each other, and potential conflicts to avoid.

---

## Overview

Arche modes are not isolated. Multi-agent organizations (MAOs) and complex systems often benefit from **combining modes strategically**. This guide helps architects decide which modes to integrate and how.

### Key Principles

1. **One primary mode per component** — Each agent or subsystem has a dominant mode
2. **Clear boundaries** — Mode interaction points should be explicitly defined
3. **Maturity alignment** — Mixing mature with experimental modes requires careful integration
4. **Cost awareness** — Combining modes increases complexity; benefits must justify it

---

## Mode Compatibility Matrix

### Scoring Legend
- 🟢 **Excellent** — Natural fit, proven patterns exist
- 🟡 **Good** — Works well with clear contracts
- 🟠 **Fair** — Possible but requires careful design
- 🔴 **Poor** — Not recommended without strong justification

### Compatibility Table

|  | 3-Layer | Agentic-Swarm | Event-Driven | RL-Loop | Foundry |
|---|---------|---------------|--------------|---------|---------|
| **3-Layer** | 🟢 N/A | 🟢 Excellent | 🟡 Good | 🟡 Good | 🟢 Excellent |
| **Agentic-Swarm** | 🟢 Excellent | 🟢 N/A | 🟡 Good | 🟡 Good | 🟢 Excellent |
| **Event-Driven** | 🟡 Good | 🟡 Good | 🟢 N/A | 🟢 Excellent | 🟡 Good |
| **RL-Loop** | 🟡 Good | 🟡 Good | 🟢 Excellent | 🟢 N/A | 🟢 Excellent |
| **Foundry** | 🟢 Excellent | 🟢 Excellent | 🟡 Good | 🟢 Excellent | 🟢 N/A |

---

## Detailed Pairing Patterns

### 🟢 3-Layer + Agentic-Swarm (Excellent)

**When to combine:**
- Orchestrator needs reliable decision logic (3-Layer)
- Sub-agents need specialization (Agentic-Swarm)
- Coordination rules are deterministic

**Architecture:**
```
Agentic-Swarm (Orchestrator)
├─ Sub-agent 1: Deterministic validator (3-Layer)
├─ Sub-agent 2: Rule-based router (3-Layer)
└─ Sub-agent 3: Specialized analyzer (3-Layer)
```

**Integration point:** Clear input/output contracts between swarm and each 3-Layer sub-agent

**Example:** Incident Commander (Agentic-Swarm) coordinating Alert Processor, Triage Agent, and Escalation Router (all 3-Layer)

**Risk level:** Low — both modes handle clear contracts well

---

### 🟢 3-Layer + Foundry (Excellent)

**When to combine:**
- Individual agents in MAO use 3-Layer implementation
- Foundry orchestrates their learning and evolution

**Architecture:**
```
Foundry (meta-agent scaffold)
└─ 01_agents/
   ├─ content-reviewer/ (3-Layer directives)
   ├─ data-processor/ (3-Layer execution)
   └─ api-integrator/ (3-Layer directives)
```

**Integration point:** Foundry's agent manuals specify 3-Layer mode; MODE_INTEGRATION_GUIDE provides guidance

**Example:** All agents in a minimal MAO implemented as 3-Layer directives; Foundry manages learning loop and upgrades

**Risk level:** Low — This is Foundry's primary use case

---

### 🟢 Event-Driven + RL-Loop (Excellent)

**When to combine:**
- System reacts to events (Event-Driven)
- Strategy for handling events improves over time (RL-Loop)

**Architecture:**
```
Event-Driven (event ingestion & routing)
└─ Event handler: RL-Loop agent
   ├─ Action space: How to handle event type
   ├─ Reward signal: Success/failure of handling
   └─ Learning: Improve handling strategy over time
```

**Integration point:** Event-Driven routes events to RL-Loop policy; RL-Loop returns action + updates policy

**Example:** Alert Monitor (Event-Driven) feeds alerts to Priority Optimizer (RL-Loop); learns what priority assignments work best

**Risk level:** Low — Natural separation of concerns

---

### 🟢 Agentic-Swarm + Foundry (Excellent)

**When to combine:**
- Multi-agent swarm structure (Agentic-Swarm)
- Foundry manages swarm composition and learning

**Architecture:**
```
Foundry (MAO scaffold for swarm)
└─ 01_agents/
   ├─ orchestrator/ (Agentic-Swarm coordinator)
   │  ├─ sub-agent: researcher (3-Layer or RL-Loop)
   │  ├─ sub-agent: analyzer (3-Layer)
   │  └─ sub-agent: synthesizer (3-Layer or Event-Driven)
   └─ 09_learning/ (learning loop for whole swarm)
```

**Integration point:** Foundry's mode-selection-log.md documents swarm structure; patch packs upgrade swarm composition

**Example:** Research Organization (Foundry) containing Chief Researcher (Agentic-Swarm) coordinating 3+ specialized researchers

**Risk level:** Low — Foundry is designed for this

---

### 🟡 3-Layer + Event-Driven (Good)

**When to combine:**
- Deterministic handlers for event types (3-Layer)
- Event stream triggers them asynchronously (Event-Driven)

**Architecture:**
```
Event-Driven (event bus)
└─ Event handlers (3-Layer directives)
   ├─ on_order_received: Process order (directives)
   ├─ on_payment_failed: Retry logic (directives)
   └─ on_inventory_low: Alert user (directives)
```

**Integration point:** Event handler registry maps event types to 3-Layer directives

**Caution:** 3-Layer expects clear inputs; ensure events are well-structured

**Example:** E-commerce webhook handler: Each event type triggers specific 3-Layer directive

**Risk level:** Medium — Requires clean event schema

---

### 🟡 3-Layer + RL-Loop (Good)

**When to combine:**
- Base behavior is deterministic (3-Layer)
- Optimization strategy changes over time (RL-Loop)

**Architecture:**
```
3-Layer base workflow
└─ Decision point: RL-Loop policy
   ├─ If score high: Execute plan A
   ├─ If score medium: Execute plan B
   └─ If score low: Execute plan C
   (Policy improves from outcomes)
```

**Integration point:** 3-Layer calls RL-Loop to select among options; logs outcome for learning

**Example:** Content moderator (3-Layer) uses ML model (RL-Loop) trained on past decisions to weight confidence thresholds

**Risk level:** Medium — Requires outcome tracking and feedback loops

---

### 🟡 Agentic-Swarm + Event-Driven (Good)

**When to combine:**
- Swarm reacts to events (Event-Driven triggers coordination)
- Sub-agents specialize (Agentic-Swarm pattern)

**Architecture:**
```
Event stream
└─ Trigger: Event-Driven
   └─ Coordinate: Agentic-Swarm
      ├─ Responder 1 (3-Layer)
      ├─ Responder 2 (Event-Driven)
      └─ Responder 3 (3-Layer)
```

**Integration point:** Event triggers swarm; swarm coordinates async response

**Example:** Alert fires → Incident Commander (Agentic-Swarm) activates response team; each member may use different mode

**Risk level:** Medium — Coordination complexity increases with async patterns

---

### 🟡 Agentic-Swarm + RL-Loop (Good)

**When to combine:**
- Swarm coordination strategy is learnable (RL-Loop)
- Sub-agents execute specialized tasks

**Architecture:**
```
RL-Loop orchestrator (learns how to coordinate)
└─ Agentic-Swarm (coordination patterns)
   ├─ Specialist 1
   ├─ Specialist 2
   └─ Specialist 3
   (Policy: How to assign tasks, sequence them)
```

**Integration point:** RL-Loop policy decides swarm coordination strategy; learns from outcomes

**Example:** Project Manager (RL-Loop) learns optimal task assignment; coordinates team (Agentic-Swarm)

**Risk level:** Medium — Two learning systems can interact unexpectedly

---

### 🟡 RL-Loop + Foundry (Excellent)

**When to combine:**
- Learning agents inside MAO (RL-Loop)
- Foundry manages learning loop and feedback cycles

**Architecture:**
```
Foundry (MAO with learning agents)
└─ 01_agents/
   ├─ Recommender (RL-Loop)
   ├─ Optimizer (RL-Loop)
   └─ Evaluator (3-Layer)
   └─ 09_learning/ (eval scenarios, rubrics for RLagents)
```

**Integration point:** Foundry eval scenarios test RL-Loop policies; feedback-log tracks learning progress

**Example:** Recommendation MAO where multiple agents learn; Foundry manages eval suite and improvement cycles

**Risk level:** Low — Foundry is designed for this

---

## Anti-Patterns: Avoid These Combinations

### 🔴 Multiple Uncoordinated RL-Loop Agents

**Problem:** Two RL-Loop agents learning simultaneously can:
- Compete for same reward signals
- Create unstable/oscillating behavior
- Make causality hard to trace

**Solution:**
- Use one RL-Loop with multiple action spaces
- Or use Agentic-Swarm to coordinate them
- Or use Foundry's learning loop to manage interaction

---

### 🔴 Event-Driven + Agentic-Swarm Without Clear Boundaries

**Problem:** Events triggering swarm coordination, but unclear handoff:
- Race conditions in coordination
- Event loss during swarm work
- Deadlock between responders

**Solution:**
- Define explicit state machine for swarm lifecycle
- Use 3-Layer orchestrator wrapper
- Or use Foundry to manage state

---

### 🔴 3-Layer + Multiple Event-Driven Systems

**Problem:** Deterministic logic responding to multiple async event sources:
- Race conditions on shared state
- Difficult to reason about event ordering
- Hard to test determinism

**Solution:**
- Add event prioritization/queuing layer
- Use 3-Layer to serialize event processing
- Or route events through single Event-Driven system

---

## Migration Patterns: Evolving Modes

### From 3-Layer → Agentic-Swarm

**When:** Single agent becomes too complex; sub-specialization helps

**Steps:**
1. Identify logical sub-tasks in directives
2. Extract each as potential sub-agent
3. Define coordination protocol
4. Test swarm behavior matches original 3-Layer
5. Gradually specialize each sub-agent

**Example:** Content moderator (3-Layer directive) → Chief Moderator (Agentic-Swarm) + 3 specialty validators

---

### From 3-Layer → RL-Loop

**When:** Optimal strategy is not known upfront; learning from outcomes improves results

**Steps:**
1. Identify decision point where learning would help
2. Define action space (options to choose from)
3. Define reward signal (what counts as success)
4. Instrument for outcome tracking
5. Gradually migrate from fixed rules to learned policy

**Example:** Router (3-Layer rules) → Router (RL-Loop policy) learning best routing strategy

---

### From Event-Driven → Event-Driven + RL-Loop

**When:** Handling strategy should improve from handling outcomes

**Steps:**
1. Keep event ingestion/routing as-is (Event-Driven)
2. Wrap handler in RL-Loop agent
3. Define reward from handler success/failure
4. Let policy improve
5. Monitor learning curves

**Example:** Alert handler → Alert handler (RL-Loop) learns best severity assessment

---

### From Agentic-Swarm → Agentic-Swarm + RL-Loop Coordinator

**When:** Swarm coordination strategy should adapt

**Steps:**
1. Keep sub-agents as-is
2. Extract coordinator to RL-Loop agent
3. Define action space (coordination decisions)
4. Define reward (task completion, efficiency)
5. Let coordinator learn best patterns

---

## Integration Checklist

When combining modes, verify:

- [ ] **Clear boundaries** — Each mode owns specific responsibilities
- [ ] **Explicit contracts** — Input/output specs between modes
- [ ] **Error handling** — What happens if one mode fails?
- [ ] **State management** — Who owns shared state?
- [ ] **Monitoring** — Can you observe each mode separately?
- [ ] **Testing** — Can you test each mode in isolation?
- [ ] **Rollback** — Can you revert to single mode if needed?
- [ ] **Documentation** — Architecture diagram + integration guide
- [ ] **Maturity alignment** — ✅ Mature paired with 🚀 Emerging documented
- [ ] **Performance** — Acceptable latency/throughput with both modes?

---

## Examples: Real Combinations

### Example 1: E-Commerce Platform (All 5 Modes)

```
3-Layer:
├─ Order processor (deterministic workflow)
├─ Inventory manager (rule-based updates)
└─ Payment handler (reliable transactions)

Event-Driven:
├─ Order webhook listener
├─ Inventory alert monitor
└─ Payment callback handler

RL-Loop:
├─ Product recommender (learns preferences)
└─ Price optimizer (learns demand elasticity)

Agentic-Swarm:
└─ Fulfillment coordinator
   ├─ Picker (3-Layer)
   ├─ Packer (3-Layer)
   └─ Shipper (Event-Driven trigger)

Foundry:
└─ (Future) Meta-organization managing all agents
```

**Integration:**
- 3-Layer handles core workflows
- Event-Driven handles webhooks/async
- RL-Loop learns user behavior
- Agentic-Swarm coordinates fulfillment
- All could feed into Foundry learning loop

---

### Example 2: Incident Response (4 Modes)

```
Foundry (Meta-organization):
└─ 01_agents/
   ├─ Alert Monitor (Event-Driven)
   │  └─ Triggers on: Infrastructure alerts
   │
   ├─ Incident Commander (Agentic-Swarm)
   │  ├─ Analyzer (3-Layer diagnosis)
   │  ├─ Responder (3-Layer executor)
   │  └─ Communicator (3-Layer notifications)
   │
   ├─ Learning Agent (RL-Loop)
   │  └─ Policy: Learn incident severity classification
   │
   └─ 09_learning/ (Foundry learning loop)
      ├─ Eval: Did we detect this incident quickly?
      ├─ Rubric: Incident classification accuracy
      └─ Feedback: Time-to-detection, false positives
```

**Integration:**
- Alert Monitor (Event-Driven) detects incidents
- Routes to Commander (Agentic-Swarm)
- Commander uses Analyzer (3-Layer) to diagnose
- Learning Agent (RL-Loop) improves classifications
- Foundry tracks all improvements, manages upgrades

---

## Next Steps

1. **For your project:** Identify which modes you're combining; check this guide
2. **For Foundry:** Use MODE_INTEGRATION_GUIDE + Compatibility Matrix to recommend mode combos
3. **For community:** Share patterns via GitHub Issues when you discover good combos
4. **For arche:** Over time, add proven patterns as "blessed combinations"

---

## Questions to Ask

- **"Do these modes compete for the same resources?"** → If yes, add coordination layer
- **"Can I test each mode independently?"** → If no, rethink boundaries
- **"What happens if one mode fails?"** → If unclear, add explicit error handling
- **"Does this combination reduce overall complexity?"** → If no, stick with single mode

---

