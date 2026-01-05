# Foundry Vendor Translation: Multi-Agent to Cloud Framework

**Purpose:** Enable Foundry to generate Multi-Agent Organizations that can be deployed to Microsoft Copilot Studio, Anthropic Claude Projects, Google Gemini with Agents, and other emerging vendor frameworks.

**Version:** 1.0 Specification (January 2026)
**Status:** Design phase → Ready for implementation

---

## Overview

Today, Foundry generates **vendor-agnostic MAO scaffolds** (markdown docs + folder structure + learning loops). The next evolution: **Vendor translation targets** that convert those MAOs into native deployments.

```
arche MAO Scaffold
(vendor-agnostic)
        ↓
        ├─→ [Microsoft Copilot] →  .copilot.json + skills + orchestration
        ├─→ [Anthropic Claude]  →  .claude-project.json + tools + workflows  
        ├─→ [Google Gemini]     →  agents.json + function definitions + routing
        ├─→ [OpenAI Swarm]      →  swarm.py + agent definitions + transitions
        ├─→ [AutoGen]           →  agent configs + group_chat orchestration
        └─→ [LangGraph]         →  graph.py + state machines + tools
```

---

## Core Principle: Vendor Abstraction Layer

The arche MAO format is the **source of truth**. Foundry generates vendor-specific deployments via a translation layer:

```
┌─────────────────────────────────────────────────┐
│ arche Framework (Vendor-Agnostic)              │
│ - Agent roles and responsibilities             │
│ - Mode recommendations (3-Layer, RL-Loop, etc.)│
│ - Learning loop specifications                 │
│ - Blueprint definitions                        │
│ - Evaluation scenarios                         │
└──────────────────┬──────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────┐
│ Foundry Vendor Translation Layer               │
│ - Agent template → Vendor format               │
│ - Mode → Vendor implementation                 │
│ - Learning loop → Vendor telemetry/logging     │
│ - Evaluation → Vendor test framework           │
└──────────────────┬──────────────────────────────┘
                   │
        ┌──────────┼──────────┬──────────┬─────────┐
        │          │          │          │         │
    Microsoft   Anthropic   Google    OpenAI   AutoGen
    Copilot     Claude      Gemini    Swarm    
```

---

## Supported Vendors (MVP Phase 1)

### Tier 1: High Priority (Q1 2026)
1. **Microsoft Copilot Studio** — Enterprise adoption, plugin architecture
2. **Anthropic Claude** — Advanced prompt engineering, tool use
3. **Google Gemini with Agents** — Multimodal, growing agent capabilities

### Tier 2: Medium Priority (Q2 2026)
4. **OpenAI Swarm** — Lightweight orchestration for simple MAOs
5. **AutoGen (Microsoft)** — Advanced group chat, already multi-agent

### Tier 3: Specialized (Q3 2026+)
6. **LangGraph (LangChain)** — Graph-based orchestration
7. **LlamaIndex Workflows** — Agentic workflows
8. **Hugging Face Agents** — Open-source, local deployment

---

## Vendor-Specific Format Specifications

### 1. Microsoft Copilot Studio Format

**What it is:** Copilot Studio provides visual + code interfaces for creating conversational agents with skills.

**Target structure:**
```
mao-vendor/
├── copilot-manifest.json          # Copilot declaration
├── skills/
│   ├── agent-role-1/
│   │   ├── skill.json             # Skill definition
│   │   ├── instructions.txt       # Agent directive
│   │   └── schema.json            # Input/output schema
│   ├── agent-role-2/
│   │   └── ...
│   └── orchestration-rules.json   # When to route to which skill
├── connectors/
│   ├── learning-feedback.json     # Logging connector
│   ├── eval-runner.json           # Test connector
│   └── external-apis.json         # Data source connectors
└── deployment/
    ├── qa-environment.json
    ├── production.json
    └── monitoring-config.json
```

**Translation mapping:**
- arche agent role → Copilot skill
- arche mode recommendation → Skill implementation pattern
- arche learning loop → Copilot connector + Activity Tracker
- arche evaluation scenario → Copilot test case

**Key capability:** Copilot Studio's skill-based architecture maps naturally to arche agent archetypes (Executor, Learner, Orchestrator, etc.)

---

### 2. Anthropic Claude Projects Format

**What it is:** Claude Projects offer persistent context, custom instructions, tool definitions, and knowledge bases.

**Target structure:**
```
mao-vendor/
├── claude-project.json            # Project metadata
├── project-instructions.md        # Overall MAO context
├── agents/
│   ├── agent-role-1/
│   │   ├── system-prompt.md       # Agent directive + context
│   │   ├── tools.json             # Tool/API definitions
│   │   ├── knowledge-base.md      # Domain knowledge
│   │   └── evaluation-rubric.md   # Success criteria
│   ├── agent-role-2/
│   │   └── ...
│   └── agent-coordination.md      # Inter-agent communication patterns
├── learning-system/
│   ├── feedback-capture.json      # How to log outcomes
│   ├── analysis-template.md       # Weekly analysis template
│   └── improvement-workflow.md    # How to propose improvements
└── evaluation/
    ├── test-scenarios.json        # Test cases
    ├── rubrics.json               # Evaluation criteria
    └── metrics-dashboard.md       # KPIs to track
```

**Translation mapping:**
- arche agent role → Project agent (system prompt + tools)
- arche mode → Implementation pattern in system prompt
- arche learning loop → Feedback capture in Claude tool definitions
- arche evaluation → Test scenarios + rubrics

**Key capability:** Claude's tool use and sophisticated prompting maps well to arche's directive-based approach. Rich context windows support detailed system prompts and knowledge bases.

---

### 3. Google Gemini with Agents Format

**What it is:** Google Agents provide structured function calling, tool use, and stateful orchestration.

**Target structure:**
```
mao-vendor/
├── agents-config.yaml             # Gemini agents configuration
├── agents/
│   ├── agent-role-1/
│   │   ├── config.yaml            # Agent configuration
│   │   ├── instructions.txt       # Agent directive
│   │   ├── tools.yaml             # Available functions
│   │   ├── output-schema.json     # Response format
│   │   └── error-handling.yaml    # Failure modes
│   ├── agent-role-2/
│   │   └── ...
│   └── routing-rules.yaml         # Agent selection logic
├── tools/
│   ├── shared-tools.yaml          # Common functions
│   ├── api-clients.yaml           # External integrations
│   └── data-sources.yaml          # Knowledge retrieval
├── learning/
│   ├── logging-config.yaml        # Telemetry setup
│   ├── feedback-schema.yaml       # Outcome tracking
│   └── metrics.yaml               # KPI definitions
└── deployment/
    ├── dev.yaml
    ├── staging.yaml
    └── production.yaml
```

**Translation mapping:**
- arche agent role → Gemini agent with function definitions
- arche mode → Agent loop implementation
- arche learning loop → Gemini logging + Cloud Logging integration
- arche evaluation → Metric definitions in Cloud Monitoring

**Key capability:** Gemini's function calling architecture and stateful execution maps well to arche's step-by-step modes.

---

### 4. OpenAI Swarm Format

**What it is:** Swarm is a lightweight Python framework for managing agent hand-offs and state transitions.

**Target structure:**
```
mao-vendor/
├── swarm_config.py                # Swarm configuration
├── agents/
│   ├── agent_role_1.py           # Agent class definition
│   │   ├── system_message()      # Agent directive
│   │   ├── tools()               # Available functions
│   │   ├── evaluate()            # Outcome evaluation
│   │   └── to_dict()             # Serialization
│   ├── agent_role_2.py
│   │   └── ...
│   └── __init__.py
├── orchestration/
│   ├── routing_rules.py          # Agent selection logic
│   ├── state_machine.py          # Mode transitions
│   └── coordination.py           # Inter-agent messaging
├── learning/
│   ├── feedback_logger.py        # Outcome logging
│   ├── metrics.py                # KPI calculations
│   └── improvement_loop.py       # Weekly analysis
├── tools/
│   ├── api_clients.py
│   ├── data_retrieval.py
│   └── utilities.py
└── evaluation/
    ├── test_scenarios.py
    ├── rubrics.py
    └── runner.py
```

**Translation mapping:**
- arche agent role → Swarm Agent class
- arche mode → Agent loop pattern in Python
- arche learning loop → Feedback logger + metrics
- arche evaluation → Test scenario classes

**Key capability:** Swarm's simplicity makes it ideal for translating arche's clean architectural patterns directly to Python.

---

### 5. AutoGen Format

**What it is:** AutoGen provides group chat, agent definitions, and advanced orchestration patterns.

**Target structure:**
```
mao-vendor/
├── config.json                    # AutoGen configuration
├── agent_definitions/
│   ├── agent_role_1.json         # Agent definition
│   │   ├── system_message       # Agent directive
│   │   ├── functions            # Available tools
│   │   ├── max_consecutive_auto_reply
│   │   └── human_input_mode
│   ├── agent_role_2.json
│   │   └── ...
│   └── agents.py                # Python implementations
├── orchestration/
│   ├── group_chat_manager.py    # Chat orchestration
│   ├── routing_logic.py         # Agent selection
│   └── state_tracking.py        # Conversation state
├── learning_system/
│   ├── conversation_logger.py   # Log interactions
│   ├── outcome_evaluator.py     # Assess results
│   └── improvement_recommender.py
├── tools/
│   ├── functions.py             # Tool definitions
│   └── integrations.py          # External APIs
└── evaluation/
    ├── test_scenarios.py
    ├── metrics.py
    └── benchmark_suite.py
```

**Translation mapping:**
- arche agent role → AutoGen ConversableAgent
- arche mode → Agent behavior pattern
- arche learning loop → Conversation logging + analytics
- arche evaluation → Benchmark suite

**Key capability:** AutoGen's group_chat_manager maps naturally to arche's Agentic-Swarm mode with coordinator patterns.

---

### 6. LangGraph Format

**What it is:** LangGraph uses directed graphs and state machines for agentic workflows.

**Target structure:**
```
mao-vendor/
├── graph.py                       # LangGraph graph definition
│   ├── StateDefinition           # Shared state schema
│   ├── nodes/
│   │   ├── agent_role_1()        # Node implementation
│   │   ├── agent_role_2()
│   │   ├── evaluator()
│   │   └── feedback_logger()
│   ├── edges/
│   │   ├── routing()             # Conditional edges
│   │   ├── error_handling()
│   │   └── transitions()
│   └── compile()                 # Graph compilation
├── agents/
│   ├── role_1_agent.py
│   ├── role_2_agent.py
│   └── base_agent.py
├── tools/
│   ├── api_tools.py
│   ├── data_tools.py
│   └── learning_tools.py
├── learning/
│   ├── feedback_capture.py       # State-based feedback
│   ├── metrics_store.py
│   └── improvement_workflow.py
└── evaluation/
    ├── scenarios.py              # Test scenarios
    ├── executor.py
    └── reporter.py
```

**Translation mapping:**
- arche agent role → LangGraph node
- arche mode → Node implementation pattern
- arche learning loop → Feedback node + state updates
- arche evaluation → Graph test harness

**Key capability:** LangGraph's graph-based approach maps naturally to arche's mode-based flow (event-driven → conditional routing → state updates).

---

## Translation Algorithm: arche → Vendor

### Input
- arche MAO scaffold (agent manuals, blueprints, templates)
- Target vendor (Copilot, Claude, Gemini, Swarm, AutoGen, LangGraph)
- Configuration options (deployment environment, logging, API keys)

### Process

```
1. PARSE arche MAO
   ├─ Read agent manuals (roles, responsibilities, mode recommendations)
   ├─ Read blueprint definitions (agent orchestration, learning loop)
   ├─ Read evaluation scenarios (success criteria, test cases)
   └─ Read feedback specifications (what to log, when)

2. NORMALIZE to intermediate format
   ├─ Create unified agent representation
   ├─ Standardize mode → implementation mapping
   ├─ Normalize learning loop → observability schema
   └─ Standardize evaluation → test framework

3. TRANSLATE to vendor format
   ├─ Agent → Vendor agent class/definition
   ├─ Mode → Vendor implementation pattern
   ├─ Learning loop → Vendor logging/metrics
   ├─ Evaluation → Vendor test format
   └─ Orchestration → Vendor routing/routing logic

4. GENERATE vendor artifacts
   ├─ Vendor config files (JSON, YAML, Python)
   ├─ Agent implementations (system prompts, tools, functions)
   ├─ Orchestration logic (routing, state management)
   ├─ Learning system (feedback capture, metrics)
   └─ Evaluation tests (scenarios, rubrics, runners)

5. VALIDATE translation
   ├─ Check completeness (all agents translated?)
   ├─ Check correctness (logic preserved?)
   ├─ Check feasibility (vendor limits respected?)
   └─ Generate validation report

6. OUTPUT vendor-ready MAO
   ├─ Runnable in target vendor environment
   ├─ Learning loops operational
   ├─ Evaluation tests executable
   └─ With deployment and monitoring config
```

### Output
- Vendor-specific MAO ready to deploy
- Implementation code/config for target vendor
- Deployment guide for that vendor
- Learning loop integration
- Evaluation test suite

---

## Mode-to-Vendor Implementation Mapping

### 3-Layer Mode (Deterministic Execution)

| Vendor | Implementation |
|--------|---|
| **Copilot** | Skill with sequential function calls, no branching |
| **Claude** | System prompt with step-by-step instructions, tools in order |
| **Gemini** | Sequential function calls with validation steps |
| **Swarm** | Agent with deterministic tool sequence |
| **AutoGen** | Agent without human_input_mode, single conversation |
| **LangGraph** | Linear path through graph nodes |

**Example Claude translation of 3-Layer agent:**
```markdown
You are a Content Reviewer agent.

ROLE: Review user-submitted content and determine policy compliance.

PROCESS:
1. Extract content text and metadata
2. Check against policy categories (hate speech, misinformation, spam)
3. Make categorization decision
4. Log decision and reviewer confidence
5. Return categorization with reasoning

CONSTRAINTS:
- Never skip any step
- Always provide reasoning
- Log all decisions for learning
```

### RL-Loop Mode (Learning & Adaptation)

| Vendor | Implementation |
|--------|---|
| **Copilot** | Skill with feedback capture + scheduled retraining |
| **Claude** | Tool for outcome logging + knowledge base updates |
| **Gemini** | Metric tracking + model parameter adjustment |
| **Swarm** | Agent state includes learning metrics, periodic weight updates |
| **AutoGen** | Conversation logging + performance-based agent weighting |
| **LangGraph** | State accumulates rewards, conditional paths adjust probabilities |

**Example Claude translation of RL-Loop agent:**
```markdown
You are a Content Preference Recommender agent.

ROLE: Learn user preferences and recommend content.

LEARNING MECHANISM:
- Log every recommendation and user reaction
- Weekly: Analyze which recommendations get engagement
- Adjust recommendation strategy based on engagement patterns
- Update knowledge base with successful recommendation patterns

TOOLS:
- recommend_content (consider learned preferences)
- log_engagement (track user reactions)
- get_learned_patterns (retrieve successful patterns)
- update_strategy (store new insights)
```

### Event-Driven Mode (Reactive Response)

| Vendor | Implementation |
|--------|---|
| **Copilot** | Skill triggered by webhook/event |
| **Claude** | Tool that listens for events and responds |
| **Gemini** | Event handler function |
| **Swarm** | Agent in permanent listen loop |
| **AutoGen** | Agent with event_input_mode |
| **LangGraph** | Event nodes triggering subgraph execution |

### Agentic-Swarm Mode (Multi-Agent Coordination)

| Vendor | Implementation |
|--------|---|
| **Copilot** | Multiple skills orchestrated by skill router |
| **Claude** | Multiple agents in Tools + delegation system prompt |
| **Gemini** | Multiple agents with function-based routing |
| **Swarm** | swarm.Swarm with hand-offs between agents |
| **AutoGen** | group_chat with multiple ConversableAgents |
| **LangGraph** | Graph with multiple agent nodes + routing logic |

---

## Learning Loop Integration by Vendor

### Feedback Capture (Continuous)

**Copilot:**
```json
{
  "connector": "Application Insights",
  "logs": [
    {"event": "agent_decision", "decision": "...", "outcome": "..."},
    {"event": "evaluation_result", "metric": "...", "value": "..."}
  ]
}
```

**Claude:**
```python
def log_feedback_tool(decision, outcome, confidence):
    """Tool that Claude uses to log feedback"""
    feedback_entry = {
        "timestamp": datetime.now(),
        "decision": decision,
        "outcome": outcome,
        "confidence": confidence
    }
    # Store in database or file
    return "Feedback logged"
```

**Gemini:**
```yaml
logging:
  level: INFO
  destination: cloud-logging
  custom_metrics:
    - agent_decision_outcome
    - evaluation_result
    - learning_metric
```

**Swarm:**
```python
class FeedbackLogger:
    def log_decision(self, agent_name, decision, outcome):
        # Store in feedback database
        self.db.insert({
            "agent": agent_name,
            "decision": decision,
            "outcome": outcome,
            "timestamp": datetime.now()
        })
```

**AutoGen:**
```python
# In group_chat callback
def log_conversation(messages):
    for msg in messages:
        if msg.get("role") == "assistant":
            feedback_store.append({
                "agent": msg.get("name"),
                "response": msg.get("content"),
                "turn": current_turn
            })
```

**LangGraph:**
```python
# In state reducer
def update_feedback(state):
    state["feedback_log"].append({
        "node": current_node,
        "outcome": state.get("evaluation_result"),
        "timestamp": datetime.now()
    })
    return state
```

### Weekly Analysis (Batch)

All vendors generate a weekly analysis artifact:
```markdown
# Weekly Learning Report: Week of Jan 5, 2026

## Metrics
- Decisions made: 1,247
- Accuracy: 94.2% (target: >92%)
- Learning improvement: +2.3% vs. previous week

## Patterns
- Most common error type: X (14% of errors)
- Successful pattern: Y (enables 8% more correct decisions)
- Bottleneck: Z (slows decisions by 0.3s average)

## Recommendations
1. Adjust parameter A to reduce error type X
2. Amplify pattern Y in decision logic
3. Optimize Z for performance

## Next steps
- Implement recommendations as change requests
- Deploy and evaluate
- Report results next week
```

---

## Evaluation Translation

arche evaluation scenarios → Vendor test suites

**Example: Incident Response Blueprint Scenario**

**arche format:**
```markdown
# SC-0001: Infrastructure Sanity Check

**Objective:** Verify alert monitor detects basic infrastructure issues

**Setup:**
1. Simulate high CPU usage alert
2. Simulate disk space alert

**Expected outcomes:**
- Severity: HIGH (CPU >90%)
- Severity: MEDIUM (Disk >80%)
- Escalation: To incident commander

**Success criteria:**
- Correct severity assignments ✓
- Escalation to coordinator within 2s ✓
```

**Claude Projects translation:**
```python
def test_infrastructure_sanity():
    """Test alert monitor on infrastructure scenarios"""
    
    # Setup
    alerts = [
        {"type": "cpu", "value": 95},
        {"type": "disk", "value": 85}
    ]
    
    # Execute
    results = alert_monitor.assess(alerts)
    
    # Verify
    assert results[0]["severity"] == "HIGH"
    assert results[1]["severity"] == "MEDIUM"
    assert results[1]["escalated_to"] == "incident_commander"
    assert results[1]["latency_ms"] < 2000
```

**Gemini translation:**
```python
# In agents-config.yaml
test_scenarios:
  - name: "infrastructure_sanity_check"
    setup:
      - alert: {type: "cpu", value: 95}
      - alert: {type: "disk", value: 85}
    expected_outcomes:
      - severity: HIGH
      - severity: MEDIUM
      - escalated: true
    assertions:
      - metric: "decision_latency_ms"
        must_be: "<2000"
      - metric: "severity_accuracy"
        must_be: "100%"
```

---

## Implementation Roadmap

### Phase 1: Foundation (Weeks 1-2)
- [ ] Create vendor translation specifications (THIS DOCUMENT)
- [ ] Build intermediate representation format
- [ ] Create translation validator
- [ ] Document mode→vendor mappings
- [ ] Establish test suite structure

### Phase 2: Tier 1 Vendors (Weeks 3-6)
- [ ] Microsoft Copilot Studio translator
- [ ] Anthropic Claude translator
- [ ] Google Gemini translator
- [ ] Test with 1 sample MAO each
- [ ] Document vendor-specific guidance

### Phase 3: Tier 2 Vendors (Weeks 7-10)
- [ ] OpenAI Swarm translator
- [ ] AutoGen translator
- [ ] Integration testing
- [ ] Performance benchmarking

### Phase 4: Tools & Automation (Weeks 11-14)
- [ ] Create `foundry-translate` CLI tool
- [ ] Support config-driven translation
- [ ] Add vendor deployment guides
- [ ] Create vendor-specific examples

### Phase 5: Documentation & Rollout (Weeks 15-16)
- [ ] Comprehensive guides for each vendor
- [ ] Migration guide from arche → vendor
- [ ] Feedback loop integration docs
- [ ] Community examples

---

## Example: Translate BP-0004 to Claude

**Input:** BP-0004 Content Moderation blueprint

**Output: Claude Projects format**

```markdown
# Claude Project: Content Moderation MAO

## Project Instructions
You are managing a content moderation team. Five agents work together:
1. Content Intake Agent - receives submissions
2. Policy Classifier - categorizes against policies
3. Review Coordinator - decides if human review needed
4. Reviewer Interface - human reviewer support
5. Feedback Processor - learns from appeals

## Agents

### Agent 1: Content Intake
**System prompt:**
```
You receive content submissions and extract metadata.
Always extract: text, source, timestamp, submitter_id
Log the submission to feedback system.
Pass to Policy Classifier.
```

### Agent 2: Policy Classifier
**System prompt:**
```
You classify content against policies: hate speech, misinformation, spam, violence.
Use these tools: policy_check, confidence_assessment, escalation_log
Log your decision and confidence to feedback system.
If confidence < 60%, escalate to human review.
Otherwise, return classification.
```

**Tools:**
```json
{
  "policy_check": {
    "description": "Check content against policy",
    "input_schema": {"text": "string", "policy": "string"}
  },
  "confidence_assessment": {
    "description": "Calculate decision confidence",
    "input_schema": {"classification": "string"}
  }
}
```

... [continue for each agent]

## Learning System
- **Feedback capture:** Each review decision logged with outcome
- **Weekly analysis:** Analyze appeal patterns
- **Improvement:** Adjust classifier based on appeals
- **Testing:** Run eval scenarios weekly

## Evaluation Scenarios
### Scenario 1: Clear Violation
- Input: Obvious hate speech content
- Expected: Immediate rejection, high confidence
- Success: Decision made in <2s, confidence >90%

### Scenario 2: Ambiguous Case
- Input: Satire that might be misunderstood
- Expected: Human review escalation
- Success: Correctly identified as needing human judgment

### Scenario 3: Pattern Detection
- Input: Coordinated spam campaign
- Expected: Detection of spam network
- Success: 80%+ detection rate of coordinated posts
```

---

## Key Design Principles

### 1. Vendor Abstraction
- arche format is source of truth
- Translations are deterministic and reproducible
- Can regenerate vendor format from arche MAO anytime

### 2. Feature Parity
- All arche capabilities map to all vendors (where technically possible)
- Vendor limitations documented explicitly
- Fallbacks defined for unsupported features

### 3. Learning Loop Preservation
- Learning loops work in all vendor environments
- Feedback capture is native to each vendor
- Weekly analysis possible from all vendors

### 4. Evaluation Integrity
- Test scenarios translate to each vendor's testing framework
- Success criteria are equivalent across vendors
- Results are comparable

### 5. Portability
- MAO deployable to multiple vendors simultaneously
- Easy migration between vendors
- Vendor lock-in prevented by maintaining arche source

---

## Benefits

### For arche Users
✅ Deploy to any vendor (not locked in)
✅ Compare vendor capabilities side-by-side
✅ Migrate MAOs between vendors easily
✅ Use best-of-breed tools for different parts
✅ Maintain vendor-agnostic architecture internally

### For Vendors
✅ Integration with arche ecosystem
✅ Access to arche blueprints and patterns
✅ Demonstration of advanced capabilities
✅ Partnership opportunities

### For Community
✅ Vendor flexibility becomes standard
✅ Best practices shared across platforms
✅ Reduced vendor lock-in risk
✅ Focus on what matters (agent design) not infrastructure

---

## Next Steps

1. **Validate specification** — Review with vendor partners
2. **Build intermediate format** — Design canonical representation
3. **Implement Tier 1 translators** — Start with Claude, Copilot, Gemini
4. **Test with real MAOs** — Validate with BP-0003, BP-0004, BP-0005
5. **Build CLI tool** — Make translation easy for users
6. **Document thoroughly** — Guides for each vendor
7. **Release and iterate** — Community feedback shapes improvements

---

## See Also

- [VENDOR_SELECTION_DECISION_TREE.md](VENDOR_SELECTION_DECISION_TREE.md) — Choose your deployment vendor
- [VENDOR_INTEGRATION_GUIDE.md](VENDOR_INTEGRATION_GUIDE.md) — Step-by-step translation guide
- [../frameworks/MODE_COMPATIBILITY.md](../frameworks/MODE_COMPATIBILITY.md) — Mode patterns and compatibility
- [../learning/FRAMEWORK_LEARNING_LOOP.md](../learning/FRAMEWORK_LEARNING_LOOP.md) — Learning loop implementation
- [../../blueprints/](../../blueprints/) — Real-world MAO examples
- [../README.md](../README.md) — Vendor translation overview

---

