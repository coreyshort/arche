# Autonomous Mode Selection Algorithm

**For AI agents:** Use this algorithm to select the appropriate arche mode without human intervention.

**⚡ Quick reference:** [AI_QUICKSTART.md](AI_QUICKSTART.md) has a simplified 30-second decision tree. Use this document for the full scoring algorithm.

---

This algorithm enables AI agents to select the appropriate arche mode without human intervention.

## Algorithm Overview

```
1. Analyze project requirements
2. Score each mode against requirements
3. Select highest-scoring mature/emerging mode
4. If tied, prefer more mature mode
5. Document decision rationale
```

## Scoring Matrix

For each requirement, assign points to modes that satisfy it:

### Requirement: Predictability & Reliability
**Question:** Must outcomes be deterministic and testable?
- YES → +10 points: 3-layer
- NO → +5 points: agentic-swarm, event-driven, rl-loop

### Requirement: Multi-Agent Coordination
**Question:** Do multiple specialized agents need to collaborate?
- YES → +10 points: agentic-swarm
- NO → +5 points: 3-layer, event-driven, rl-loop

### Requirement: Event-Driven Architecture
**Question:** Does the system primarily react to external events/streams?
- YES → +10 points: event-driven
- NO → +5 points: 3-layer, agentic-swarm, rl-loop

### Requirement: Learning & Adaptation
**Question:** Should the system improve from outcomes over time?
- YES → +10 points: rl-loop
- NO → +5 points: 3-layer, agentic-swarm, event-driven

### Requirement: Defined Workflows
**Question:** Can workflows be specified upfront with clear steps?
- YES → +8 points: 3-layer
- NO → +5 points: agentic-swarm, event-driven, rl-loop

### Requirement: Production Readiness
**Question:** Is immediate production stability critical?
- YES → +10 points: 3-layer (mature)
- MODERATE → +5 points: agentic-swarm, event-driven, rl-loop (emerging)
- NO → +0 points: all modes

### Requirement: Complexity Tolerance
**Question:** Is significant architectural complexity acceptable?
- HIGH → +5 points: agentic-swarm, rl-loop
- MEDIUM → +5 points: event-driven
- LOW → +10 points: 3-layer

### Requirement: Real-Time Reactivity
**Question:** Are sub-second response times critical?
- YES → +8 points: event-driven, 3-layer
- NO → +3 points: agentic-swarm, rl-loop

---

## Decision Algorithm (Pseudocode)

```python
def select_mode(requirements):
    scores = {
        "3-layer": 0,
        "agentic-swarm": 0,
        "event-driven": 0,
        "rl-loop": 0
    }
    
    # Score based on requirements
    if requirements["predictability_critical"]:
        scores["3-layer"] += 10
    else:
        scores["agentic-swarm"] += 5
        scores["event-driven"] += 5
        scores["rl-loop"] += 5
    
    if requirements["multi_agent_needed"]:
        scores["agentic-swarm"] += 10
    else:
        scores["3-layer"] += 5
        scores["event-driven"] += 5
        scores["rl-loop"] += 5
    
    if requirements["event_driven_architecture"]:
        scores["event-driven"] += 10
    else:
        scores["3-layer"] += 5
        scores["agentic-swarm"] += 5
        scores["rl-loop"] += 5
    
    if requirements["learning_required"]:
        scores["rl-loop"] += 10
    else:
        scores["3-layer"] += 5
        scores["agentic-swarm"] += 5
        scores["event-driven"] += 5
    
    if requirements["workflows_definable"]:
        scores["3-layer"] += 8
    else:
        scores["agentic-swarm"] += 5
        scores["event-driven"] += 5
        scores["rl-loop"] += 5
    
    if requirements["production_stability_critical"]:
        scores["3-layer"] += 10  # Mature
    else:
        scores["agentic-swarm"] += 5  # Emerging
        scores["event-driven"] += 5
        scores["rl-loop"] += 5
    
    if requirements["complexity_tolerance"] == "high":
        scores["agentic-swarm"] += 5
        scores["rl-loop"] += 5
    elif requirements["complexity_tolerance"] == "medium":
        scores["event-driven"] += 5
    else:  # low
        scores["3-layer"] += 10
    
    if requirements["realtime_reactivity"]:
        scores["event-driven"] += 8
        scores["3-layer"] += 8
    else:
        scores["agentic-swarm"] += 3
        scores["rl-loop"] += 3
    
    # Get mode with highest score
    selected_mode = max(scores.items(), key=lambda x: x[1])[0]
    
    # If tied, prefer maturity: 3-layer > others
    max_score = max(scores.values())
    tied_modes = [mode for mode, score in scores.items() if score == max_score]
    
    if len(tied_modes) > 1:
        if "3-layer" in tied_modes:
            selected_mode = "3-layer"
        else:
            selected_mode = tied_modes[0]  # Take first emerging mode
    
    return selected_mode, scores
```

---

## Structured Question Set

When analyzing a project, ask these questions to extract requirements:

### 1. Reliability Requirements
**Question:** "How critical is predictable, testable behavior?"
- **CRITICAL** → predictability_critical = True
- **MODERATE/LOW** → predictability_critical = False

### 2. Agent Architecture
**Question:** "Does this project need multiple specialized agents working together?"
- **YES** → multi_agent_needed = True
- **NO** → multi_agent_needed = False

### 3. Architectural Pattern
**Question:** "Is the system primarily event-driven (webhooks, queues, streams)?"
- **YES** → event_driven_architecture = True
- **NO** → event_driven_architecture = False

### 4. Learning Requirements
**Question:** "Should the system learn and improve from outcomes over time?"
- **YES** → learning_required = True
- **NO** → learning_required = False

### 5. Workflow Definition
**Question:** "Can the workflows be defined upfront with clear steps?"
- **YES** → workflows_definable = True
- **NO** → workflows_definable = False

### 6. Production Constraints
**Question:** "Is immediate production stability critical?"
- **YES** → production_stability_critical = True
- **NO** → production_stability_critical = False

### 7. Complexity Tolerance
**Question:** "What level of architectural complexity is acceptable?"
- **HIGH** → complexity_tolerance = "high"
- **MEDIUM** → complexity_tolerance = "medium"
- **LOW** → complexity_tolerance = "low"

### 8. Performance Requirements
**Question:** "Are sub-second response times critical?"
- **YES** → realtime_reactivity = True
- **NO** → realtime_reactivity = False

---

## Decision Template

When selecting a mode autonomously, document your decision:

```markdown
## Mode Selection Decision

**Project:** [Project name/description]

**Requirements Analysis:**
- Predictability Critical: [Yes/No]
- Multi-Agent Needed: [Yes/No]
- Event-Driven Architecture: [Yes/No]
- Learning Required: [Yes/No]
- Workflows Definable: [Yes/No]
- Production Stability Critical: [Yes/No]
- Complexity Tolerance: [High/Medium/Low]
- Realtime Reactivity: [Yes/No]

**Scoring:**
- 3-layer: [score]
- agentic-swarm: [score]
- event-driven: [score]
- rl-loop: [score]

**Selected Mode:** [mode name]

**Rationale:** [Why this mode scored highest and fits the requirements]

**Confidence:** [High/Medium/Low]
- High: Clear winner, requirements strongly favor this mode
- Medium: Close scores, multiple modes viable
- Low: Insufficient information, defaulting to 3-layer (mature)

**Fallback:** If selected mode proves unsuitable during development, [alternative mode] is recommended.
```

---

## Default Decision Rules

When requirements are unclear or ambiguous:

1. **Default to 3-layer mode** (mature, proven, lowest risk)
2. **Document assumption:** "Defaulting to 3-layer due to [reason]"
3. **Note re-evaluation trigger:** "Re-evaluate if [condition changes]"

---

## Example Decisions

### Example 1: ETL Pipeline
```
Requirements:
- Predictability: YES (financial data, must be accurate)
- Multi-Agent: NO (single workflow)
- Event-Driven: NO (scheduled batch)
- Learning: NO (deterministic transformations)
- Workflows Definable: YES (clear ETL steps)
- Production Stability: YES (critical system)
- Complexity Tolerance: LOW (traditional team)
- Realtime: NO (batch processing)

Scores:
- 3-layer: 10+5+5+5+8+10+10+3 = 56
- agentic-swarm: 5+5+5+5+5+5+5+3 = 38
- event-driven: 5+5+5+5+5+5+5+3 = 38
- rl-loop: 5+5+5+5+5+5+5+3 = 38

Selected: 3-layer (clear winner)
```

### Example 2: Real-Time Recommendation Engine
```
Requirements:
- Predictability: NO (exploration acceptable)
- Multi-Agent: NO (single recommender)
- Event-Driven: NO (request-response)
- Learning: YES (improve from user interactions)
- Workflows Definable: NO (learning-based)
- Production Stability: MODERATE (can iterate)
- Complexity Tolerance: HIGH (ML team)
- Realtime: YES (user-facing)

Scores:
- 3-layer: 5+5+5+5+5+5+10+8 = 48
- agentic-swarm: 5+5+5+5+5+5+5+3 = 38
- event-driven: 5+5+5+5+5+5+5+8 = 43
- rl-loop: 5+5+5+10+5+5+5+3 = 43

Selected: 3-layer (highest score, but note: rl-loop close second)
Fallback: Consider rl-loop if learning proves critical
```

### Example 3: Multi-Agent Research System
```
Requirements:
- Predictability: NO (emergent solutions)
- Multi-Agent: YES (researcher, analyst, synthesizer)
- Event-Driven: NO (coordinated workflow)
- Learning: NO (rule-based coordination)
- Workflows Definable: NO (dynamic collaboration)
- Production Stability: MODERATE (internal tool)
- Complexity Tolerance: HIGH (R&D project)
- Realtime: NO (batch research)

Scores:
- 3-layer: 5+5+5+5+5+5+10+3 = 43
- agentic-swarm: 5+10+5+5+5+5+5+3 = 43
- event-driven: 5+5+5+5+5+5+5+3 = 38
- rl-loop: 5+5+5+5+5+5+5+3 = 38

Selected: agentic-swarm (tied, but multi-agent requirement is explicit)
```

---

## Implementation Notes

**For AI Agents:**
1. Extract requirements by analyzing project description
2. Answer the 8 structured questions
3. Apply scoring algorithm
4. Select highest-scoring mode
5. Document decision with template
6. Proceed with bootstrap using selected mode

**Confidence Thresholds:**
- High confidence: Winner scores 10+ points above alternatives
- Medium confidence: Winner scores 5-9 points above alternatives
- Low confidence: Winner scores 0-4 points above alternatives (consider defaulting to 3-layer)

**When to seek human input:**
- Multiple modes tied with high scores
- Project requirements are contradictory
- Confidence is low and project is high-risk

**Otherwise: Proceed autonomously with documented decision.**
