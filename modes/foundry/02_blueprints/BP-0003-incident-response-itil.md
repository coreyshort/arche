# BP-0003: Incident Response (ITIL-aligned)

## Metadata
- Blueprint ID: BP-0003
- Version: v0.1.0
- Domain: IT Operations / Incident Management
- Framework alignment: ITIL v3/v4 (Incident Management lifecycle)

## Objective & Success
Create a multi-agent incident response organization that:
- Detects incidents and escalates appropriately
- Coordinates response across technical and business teams
- Learns from incidents to improve detection and resolution
- Maintains audit trail for compliance
- Reduces MTTR (Mean Time To Resolution)

## In Scope
- Incident detection and triage
- Response coordination
- Knowledge capture and learning
- Escalation to humans when needed

## Out of Scope
- Problem management (root cause analysis beyond incident resolution)
- Change management (post-incident changes handled separately)
- Security incidents (separate SOC process)

## Dimensions (Selected 4)
1. **Severity level** (P1 Critical, P2 Major, P3 Minor, P4 Planning)
2. **Impact area** (Infrastructure, Application, Database, Network, Business)
3. **Detection source** (Automated monitor, Escalated ticket, Human report)
4. **Resolution complexity** (Simple restart, Configuration change, Code deploy, Human intervention)

## Agent Architecture

### Near-term (Minimal)
- **Alert Monitor** (Event-Driven)
  - Ingests infrastructure & application alerts
  - Detects patterns and clusters
  - Routes to incident commander

- **Incident Commander** (Agentic-Swarm orchestrator)
  - Receives alert/ticket
  - Assesses severity and impact
  - Coordinates response team
  - Manages escalation

- **Triage Analyzer** (3-Layer deterministic)
  - Applies diagnostic rules
  - Queries monitoring systems
  - Classifies incident type
  - Suggests resolution paths

- **Knowledge Retriever** (3-Layer + RL-Loop)
  - Searches past incidents for similar issues
  - Learns what resolution patterns work for each type
  - Suggests known fixes

- **Execution Agent** (3-Layer)
  - Executes mitigation procedures
  - Applies known fixes
  - Handles rollback if needed
  - Logs all actions

### Ideal (Adds)
- **Escalation Manager** (3-Layer + RL-Loop)
  - Learns when and how to escalate
  - Selects appropriate human responder
  - Briefs them with context

- **Post-Incident Learner** (RL-Loop)
  - Analyzes incident after resolution
  - Updates detection thresholds
  - Identifies process improvements

- **Alert Optimizer** (RL-Loop)
  - Learns which alerts are actionable vs noise
  - Reduces alert fatigue
  - Improves alert signal-to-noise ratio

## Agent Hierarchy

```
Alert Monitor (Event-Driven)
    ↓ Triggers
Incident Commander (Agentic-Swarm)
├─ Triage Analyzer (3-Layer)
├─ Knowledge Retriever (3-Layer + RL-Loop)
├─ Execution Agent (3-Layer)
└─ [Future] Escalation Manager (3-Layer + RL-Loop)
```

## Artifact Map

| Artifact | Owner | Output Files | Rubric | Eval Scenario |
|----------|-------|--------------|--------|---------------|
| **Incident ticket** | Incident Commander | `01_agents/incident-record.md` | Completeness, accuracy | SC-0001 |
| **Diagnostic report** | Triage Analyzer | `01_agents/diagnostic.md` | Accuracy of classification | SC-0001 |
| **Resolution plan** | Knowledge Retriever | `01_agents/resolution-plan.md` | Appropriateness to incident | SC-0002 |
| **Execution log** | Execution Agent | `01_agents/execution-log.md` | Completeness, audit trail | SC-0002 |
| **Resolution summary** | Incident Commander | `09_learning/incident-summary.md` | Clarity, actionability | SC-0003 |

## Learning System

### Rubrics
- **Incident Detection Quality** — Did we catch this quickly?
  - Detection latency < 5 min: 5 pts
  - Detection latency < 15 min: 3 pts
  - Manual escalation required: 1 pt

- **Classification Accuracy** — Did we classify correctly?
  - Correct on first attempt: 5 pts
  - Correct after 1 adjustment: 3 pts
  - Required human reclassification: 1 pt

- **Resolution Effectiveness** — Did we fix it?
  - Resolved without escalation: 5 pts
  - Escalated to human, resolved quickly: 3 pts
  - Recurring incident: 1 pt

### Eval Suite (3 Scenarios)
- **SC-0001: Infrastructure Alert Triage**
  - Simulates CPU spike alert
  - Tests: Detection, classification, escalation
  - Measures: Detection latency, classification accuracy

- **SC-0002: Multi-Component Failure**
  - Simulates cascading failures (DB → App → Web)
  - Tests: Correlation, prioritization, coordination
  - Measures: Root cause identification, MTTR

- **SC-0003: Alert Fatigue**
  - Simulates high-volume alerts including noise
  - Tests: Signal vs noise, prioritization
  - Measures: Alert fatigue score, action effectiveness

### Learning Feedback Loop
- **Feedback capture:** Each incident automatically logs
  - Detection latency
  - Classification accuracy
  - Resolution effectiveness
  - Escalations required

- **Learning cycles:** Weekly review
  - Update alert thresholds based on false positive rate
  - Improve knowledge base with new incident patterns
  - Adjust escalation criteria

## Governance

### Ownership Map
```
00_governance/
├─ file-ownership.md
│  ├─ Alert Monitor: Alert Monitor agent owner
│  ├─ Incident Commander: Oncall lead
│  ├─ Triage Analyzer: Senior SRE
│  ├─ Knowledge Retriever: Documentation team
│  └─ Execution Agent: SRE automation team

└─ scaffold-spec.md
   ├─ Blueprint alignment: ITIL Incident Management
   ├─ Contract version: FND-CONTRACT v1
   ├─ Dimensions: Severity, Impact, Source, Complexity
   └─ Target MAO size: 5 agents (near-term) → 8 agents (ideal)
```

### Non-negotiables
1. **Audit trail:** All incident actions logged and immutable
2. **Escalation path:** Clear escalation rules with human override
3. **Knowledge capture:** Each incident improves system
4. **No silent failures:** All failures escalate or alert

## Contract & Upgrades

- **Contract version:** FND-CONTRACT v1
- **Upgrades via patch packs:**
  - FND-0001: Add meta contract
  - FND-0002: Add eval suite
  - FND-0003: Add scaffold spec
  - [Future] FND-0005: Add alert optimization (RL-Loop)
  - [Future] FND-0006: Add post-incident automation

---

