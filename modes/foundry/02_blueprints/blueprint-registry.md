# Blueprint Registry

Blueprints are reusable designs for generating MAOs. Each blueprint provides:
- Pre-defined agent architecture and roles
- Domain-specific dimensions and frameworks
- Learning system (rubrics, eval scenarios, feedback loops)
- Governance and ownership structure
- Example outputs and success metrics

## Available Blueprints

### Domain: Product Management
- **BP-0001:** Industrial Construction PM (Pragmatic-aligned)
  - Domains: Capital projects, construction, industrial sectors
  - Key agents: Chief of Staff, Context Librarian, Strategy, Roadmap, GTM
  - Dimensions: Sector, Persona, Project mode

### Domain: Operations & Reliability
- **BP-0003:** Incident Response (ITIL-aligned)
  - Domains: IT Operations, SRE, Infrastructure
  - Key agents: Alert Monitor, Incident Commander, Triage Analyzer, Knowledge Retriever, Executor
  - Dimensions: Severity, Impact area, Detection source, Complexity
  - Key patterns: Event-Driven + Agentic-Swarm + RL-Loop

- **BP-0005:** Data Operations (Data Reliability Engineering)
  - Domains: Data engineering, data ops, analytics
  - Key agents: Pipeline Monitor, Issue Triage, Auto-Remediation, Analytics Support, Knowledge Manager
  - Dimensions: Data layer, Issue type, Severity, Remediation complexity
  - Key patterns: Event-Driven + 3-Layer + RL-Loop

### Domain: Community & Trust & Safety
- **BP-0004:** Content Moderation (Community T&S)
  - Domains: Community management, content safety, policy enforcement
  - Key agents: Content Intake, Policy Classifier, Review Coordinator, Reviewer Interface, Feedback Processor
  - Dimensions: Content type, Policy category, Confidence, Audience risk
  - Key patterns: Event-Driven + 3-Layer + RL-Loop + Agentic-Swarm

## Quick Selection Guide

| If you're building... | Choose blueprint |
|---|---|
| Product management system | BP-0001 |
| Incident response org | BP-0003 |
| Content moderation at scale | BP-0004 |
| Data pipeline reliability | BP-0005 |
| None of the above | Start with template: `../07_templates/blueprint.template.md` |

## Creating Custom Blueprints

To create a new blueprint:

1. **Copy template:** `../07_templates/blueprint.template.md`
2. **Assign ID:** Next available BP-#### (check registry for gaps)
3. **Define:**
   - Domain and framework alignment
   - Clear objective and success criteria
   - 3-6 dimensions for the domain
   - Near-term (5) and ideal (7+) agent architecture
   - Artifact map with ownership
   - Learning system (rubrics + eval suite)
   - Governance structure

4. **Validate:**
   - Each agent has clear responsibility
   - No agent overlaps
   - Eval scenarios test key dimensions
   - Learning loop is actionable

5. **Contribute:** Open GitHub Issue with `blueprint` label

## Mapping Blueprints to Archetypes

Each blueprint uses agent archetypes (see `../../AGENT_ARCHETYPES.md`):

**BP-0003 (Incident Response):**
- Alert Monitor → Monitor archetype (Event-Driven)
- Incident Commander → Orchestrator archetype (Agentic-Swarm)
- Triage Analyzer → Executor archetype (3-Layer)
- Knowledge Retriever → Learner archetype (RL-Loop)
- Execution Agent → Executor archetype (3-Layer)

**BP-0004 (Content Moderation):**
- Content Intake → Monitor archetype (Event-Driven)
- Policy Classifier → Learner archetype (RL-Loop)
- Review Coordinator → Orchestrator archetype (Agentic-Swarm)
- Reviewer Interface → Executor archetype (3-Layer)
- Feedback Processor → Learner archetype (RL-Loop)

**BP-0005 (Data Operations):**
- Pipeline Monitor → Monitor archetype (Event-Driven)
- Issue Triage → Executor + Learner archetype (3-Layer + RL-Loop)
- Auto-Remediation → Executor archetype (3-Layer)
- Knowledge Manager → Learner archetype (RL-Loop)
- Analytics Support → Orchestrator archetype (Agentic-Swarm)


