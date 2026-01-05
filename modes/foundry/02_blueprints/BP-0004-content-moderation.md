# BP-0004: Content Moderation (Quality at Scale)

## Metadata
- Blueprint ID: BP-0004
- Version: v0.1.0
- Domain: Community Management / Content Moderation
- Framework alignment: Community Trust & Safety best practices

## Objective & Success
Create a multi-agent content moderation organization that:
- Scales human judgment across millions of items
- Maintains consistent policy application
- Learns from human reviewer decisions
- Reduces harmful content dwell time
- Minimizes false positives (over-moderation)

## In Scope
- User-generated content review
- Policy violation detection
- Escalation to human reviewers
- Learning from reviewer feedback

## Out of Scope
- Appeals process (handled separately)
- Policy development (policy makers external)
- User communication (handled by separate system)

## Dimensions (Selected 4)
1. **Content type** (Text, Image, Video, Link, Comment)
2. **Policy category** (Hate speech, Violence, Spam, Misinformation, Sexual content)
3. **Confidence level** (High confidence, Medium, Low, Uncertain)
4. **Audience risk** (Public, Vulnerable audience, Minors exposed)

## Agent Architecture

### Near-term (Minimal)
- **Content Intake** (Event-Driven)
  - Receives user-generated content
  - Extracts metadata and context
  - Queues for classification

- **Policy Classifier** (3-Layer + RL-Loop)
  - Applies policy rules deterministically
  - Uses ML model (RL-Loop) for nuanced cases
  - Routes to appropriate reviewer pool

- **Review Coordinator** (Agentic-Swarm orchestrator)
  - Manages human reviewer queue
  - Assigns content based on reviewer expertise
  - Handles priority and escalation

- **Reviewer Interface** (3-Layer)
  - Presents context to reviewer
  - Collects reviewer decision
  - Stores with justification

- **Feedback Processor** (3-Layer + RL-Loop)
  - Captures reviewer feedback
  - Updates policy classifier model
  - Identifies need for policy clarification

### Ideal (Adds)
- **Pattern Detector** (Event-Driven + RL-Loop)
  - Detects emerging policy violation patterns
  - Alerts escalation team
  - Learns temporal patterns (coordinated inauthentic behavior)

- **Reviewer Quality Monitor** (3-Layer + RL-Loop)
  - Tracks reviewer consistency
  - Identifies reviewer drift
  - Suggests retraining

- **Appeal Handler** (3-Layer)
  - Receives and processes appeals
  - Re-reviews with fresh perspective
  - Learns from appeal patterns

## Agent Hierarchy

```
Content Intake (Event-Driven)
    ↓ Routes
Policy Classifier (3-Layer + RL-Loop)
    ↓ Sends for review if needed
Review Coordinator (Agentic-Swarm)
├─ Reviewer Interface (3-Layer)
└─ Feedback Processor (3-Layer + RL-Loop)
```

## Artifact Map

| Artifact | Owner | Output Files | Rubric | Eval Scenario |
|----------|-------|--------------|--------|---------------|
| **Moderation decision** | Policy Classifier | `01_agents/decision-record.md` | Accuracy, justification | SC-0001 |
| **Reviewer assignment** | Review Coordinator | `01_agents/assignment.md` | Fairness, expertise match | SC-0001 |
| **Review outcome** | Reviewer Interface | `01_agents/review-outcome.md` | Reasoning quality, consistency | SC-0002 |
| **Feedback summary** | Feedback Processor | `01_agents/feedback-summary.md` | Learning readiness | SC-0002 |
| **Monthly report** | Coordinator | `09_learning/monthly-moderation-report.md` | Trend clarity, actionability | SC-0003 |

## Learning System

### Rubrics
- **Classification Accuracy** — Did the policy classifier decide correctly?
  - Agreed with human reviewer: 5 pts
  - Disagreed but defensible: 3 pts
  - Clear policy violation missed: 1 pt

- **Review Consistency** — Are reviewers consistent?
  - Same decision across similar items: 5 pts
  - Majority agreement (>75%): 3 pts
  - Low agreement (<50%): 1 pt

- **Appeal Rate** — Are users challenging decisions?
  - <1% appeal rate: 5 pts
  - 1-3% appeal rate: 3 pts
  - >5% appeal rate: 1 pt

### Eval Suite (3 Scenarios)
- **SC-0001: Clear Policy Violation**
  - Simulates obvious hate speech content
  - Tests: Classification accuracy, reviewer assignment
  - Measures: Decision consistency, dwell time

- **SC-0002: Ambiguous Case**
  - Simulates nuanced misinformation (satire? real?)
  - Tests: Escalation to human, reviewer judgment quality
  - Measures: Appeal rate, consensus difficulty

- **SC-0003: Pattern Detection**
  - Simulates coordinated inauthentic behavior
  - Tests: Pattern recognition, escalation triggers
  - Measures: Detection latency, false positive rate

### Learning Feedback Loop
- **Feedback capture:** Each review logs
  - Classifier decision vs reviewer decision
  - Reviewer reasoning
  - Appeal/challenge if any
  - Reviewer expertise level

- **Learning cycles:** Daily updates
  - Retrain classifier on recent reviews
  - Update reviewer expertise profiles
  - Detect review drift

- **Quarterly reviews:**
  - Policy clarity assessments
  - Reviewer retraining needs
  - Classifier model performance

## Governance

### Ownership Map
```
00_governance/
├─ file-ownership.md
│  ├─ Content Intake: Platform data team
│  ├─ Policy Classifier: Trust & Safety ML team
│  ├─ Review Coordinator: Content Ops lead
│  ├─ Reviewer Interface: Product team
│  └─ Feedback Processor: Analytics team

└─ scaffold-spec.md
   ├─ Blueprint alignment: Community Trust & Safety
   ├─ Contract version: FND-CONTRACT v1
   ├─ Dimensions: Content type, Policy, Confidence, Risk
   ├─ Target MAO size: 5 agents (near-term) → 7 agents (ideal)
   └─ SLA: <2 hour dwell time for violent content
```

### Non-negotiables
1. **Transparent reasoning:** All decisions include justification
2. **Appeal path:** Users can challenge decisions
3. **Consistency tracking:** Monitor reviewer agreement
4. **Escalation path:** Difficult cases escalate, not reject
5. **No user identity bias:** Decisions based on content, not user history

## Special Considerations

### False Positive Minimization
- Start conservative (require high confidence for removal)
- Learn from appeals which should have been allowed
- Balance false positives vs false negatives carefully

### Reviewer Well-being
- Monitor reviewer fatigue and psychological impact
- Rotate reviewers through less impactful content
- Track and prevent reviewer drift

### Policy Evolution
- Regular policy reviews with community input
- Version control for policies
- Clear dates for policy changes

## Contract & Upgrades

- **Contract version:** FND-CONTRACT v1
- **Upgrades via patch packs:**
  - FND-0001: Add meta contract
  - FND-0002: Add eval suite
  - FND-0003: Add scaffold spec
  - [Future] FND-0007: Add reviewer quality monitoring
  - [Future] FND-0008: Add pattern detection

---

