# Foundry Vendor Integration: Implementation Guide

**Purpose:** Practical implementation patterns for translating arche MAOs to vendor frameworks.

**Version:** 1.0 (January 2026)
**Status:** Reference guide for developers

---

## Quick Start: Translate an arche MAO to Your Vendor

### Prerequisites
- One arche MAO scaffold (from Foundry)
- Target vendor account/environment
- `foundry-translate` tool (or manual translation steps)

### 5-Minute Translation

```bash
# Step 1: Generate translation
foundry-translate --mao ./my-mao --target claude --output ./claude-mao

# Step 2: Review generated files
ls -la ./claude-mao/
# └── claude-project.json (project metadata)
# └── agents/ (agent definitions)
# └── learning/ (feedback config)
# └── eval/ (test suite)

# Step 3: Deploy to vendor
foundry-deploy --vendor claude --config ./claude-mao --env production

# Step 4: Verify learning loops
foundry-verify --vendor claude --check-logging --check-eval

# Done! Your MAO is running.
```

---

## Deep Dive: Manual Translation Process

If not using the CLI tool, here's the manual process:

### Step 1: Analyze Your arche MAO

**Read these files from your MAO:**

```
my-mao/
├── 00_governance/
│   └── FOUNDRY_CONTRACT.md        ← Overall MAO scope
├── 01_agents/
│   ├── agent-role-1.md            ← Agent definitions
│   ├── agent-role-2.md
│   └── ...
├── 02_blueprints/ (optional)
│   └── blueprint-name.md          ← Architecture
├── 07_templates/
│   ├── agent-manual.template.md   ← Pattern templates
│   └── ...
└── 09_learning/
    ├── feedback-log.md            ← Learning system
    └── eval-scenario-*.md         ← Test cases
```

**Questions to answer:**

1. **How many agents?** (Usually 3-7)
2. **What's the primary mode?** (3-Layer, RL-Loop, Event-Driven, Agentic-Swarm)
3. **What vendor?** (Claude, Copilot, Gemini, Swarm, AutoGen, LangGraph)
4. **What constraints?** (Model size, API rate limits, latency requirements)

---

### Step 2: Create Agent Map

Create a translation reference for each agent:

```markdown
# Agent Translation Map

## Agent 1: Content Classifier
**arche role:** Deterministic policy classifier
**Recommended mode:** 3-Layer
**Vendor implementation:** Claude tool + system prompt

**Translation:**
- arche: "Check against policy categories (hate, misinformation, spam)"
- claude: Custom tool that categorizes content
- Input: text, policy_version
- Output: category, confidence, reasoning

## Agent 2: Review Coordinator  
**arche role:** Multi-agent orchestrator
**Recommended mode:** Agentic-Swarm
**Vendor implementation:** Claude delegation in system prompt

**Translation:**
- arche: "Decide which specialists review this content"
- claude: Agent that uses tools to call other agents
- Interaction: Use "Ask agent X" pattern

[Continue for each agent...]
```

---

### Step 3: Translate by Vendor

#### Claude Projects (Recommended for beginners)

**Process:**

```markdown
1. Create project in Claude
2. Add to "Project Instructions" (top level):
   - Copy FOUNDRY_CONTRACT.md summary
   - Add agent overview
   - Add learning system description

3. Create an Agent in the project for each role:
   - Name: agent-role-name
   - System prompt: Copy from arche agent manual + mode guidance
   - Tools: Add JSON tool definitions
   - Knowledge: Add relevant domain documents

4. Add Tools (Cloud integrations):
   - log_feedback (write to database/file)
   - get_metrics (read weekly analysis)
   - log_decision (for 3-Layer agents)
   - get_learned_policy (for RL-Loop agents)
   - etc.

5. Create test cases in project:
   - Name: evaluation scenario name
   - Input: Copy from eval scenario
   - Expected output: Copy success criteria
   - Run tests

6. Deploy to production:
   - Share project with team
   - Setup logging connector
   - Setup feedback triggers
   - Monitor in Claude activity logs
```

**Example: Claude Content Classifier**

```markdown
## System Prompt for Content Classifier

You are a Content Classifier Agent in a moderation MAO.

### Your Role
Review user-submitted content and determine policy compliance.
You are deterministic and consistent.

### Process (3-Layer Mode)
Follow these steps in order:
1. Extract content: Use extract_content_tool
2. Evaluate against policies: Use policy_evaluation_tool
3. Make decision: Return category and confidence
4. Log decision: Use log_decision_tool with outcome
5. Return result to coordinator

### Guidelines
- Always provide reasoning
- Confidence ranges 0-100
- Log all decisions (for learning)
- If confidence < 60%, recommend human review
- Never skip steps

### Tools You Have
- extract_content_tool: Get text and metadata
- policy_evaluation_tool: Check against policies
- log_decision_tool: Record decision for learning

### Learning System
Every decision you make gets logged.
Weekly analysis improves your decision thresholds.
```

**Tool Definition (JSON):**

```json
{
  "name": "policy_evaluation_tool",
  "description": "Evaluate content against moderation policies",
  "input_schema": {
    "type": "object",
    "properties": {
      "text": {
        "type": "string",
        "description": "Content text to evaluate"
      },
      "policies": {
        "type": "array",
        "items": {"type": "string"},
        "description": "Policies to check: hate_speech, misinformation, spam, violence"
      }
    },
    "required": ["text", "policies"]
  }
}
```

#### Copilot Studio (For Enterprise)

**Process:**

```
1. Create Copilot in Copilot Studio
2. Add Copilot Instructions:
   - Copy FOUNDRY_CONTRACT summary
   - Add agent interaction flow
   - Add learning system description

3. Create a Skill for each agent role:
   - Name: agent-role-name
   - Instructions: Copy from arche agent manual
   - Add Inputs/Outputs matching arche interfaces
   - Add error handling

4. Create connectors:
   - Feedback logging (SQL, REST API, etc.)
   - Evaluation runner (webhook to test service)
   - Data sources (for knowledge retrieval)

5. Create orchestration:
   - Use "Conversation topic" routing
   - Map arche agent selection to topic routing
   - Define skill-to-skill hand-offs

6. Test and deploy:
   - Use Copilot Studio testing UI
   - Verify learning logs go to database
   - Deploy to Web, Teams, etc.
```

#### Gemini with Agents (For Multimodal)

**Process:**

```yaml
1. Define agents.yaml:
   - agents: []  # Add one per arche agent role
   
2. For each agent, define:
   - id: agent-role-name
   - model: gemini-pro or gemini-vision
   - instructions: [Copy from arche agent manual]
   - tools:
     - name: tool-name
       function_declarations: [...]
   - rate_limit: [Set from arche requirements]

3. Define routing rules:
   - When to call which agent
   - State management (what persists)
   - Error handling flows

4. Setup logging:
   - Cloud Logging for decision logs
   - Cloud Monitoring for metrics
   - Pub/Sub for event streaming

5. Create evaluation:
   - agent_eval_runner.py
   - Load eval scenarios
   - Execute against deployed agents
   - Report results

6. Deploy:
   - Deploy to Cloud Run or Cloud Functions
   - Setup scaling policies
   - Enable monitoring
```

#### Swarm (For Lightweight Python)

**Process:**

```python
# 1. Define agents.py
from swarm import Swarm

# Copy each arche agent into a class
class ContentClassifier:
    def __init__(self):
        self.name = "content_classifier"
        self.system_message = """
        [Copy from arche agent manual]
        """
    
    def tools(self):
        return [
            # Copy tools from arche
        ]
    
    def evaluate_outcome(self, decision, actual_outcome):
        # Log to feedback system
        pass

# 2. Define orchestration.py
# Copy arche agent routing logic to Python
def route_to_next_agent(current_agent, state):
    if state["needs_review"]:
        return review_coordinator
    else:
        return content_classifier

# 3. Define learning.py
class FeedbackLogger:
    def log(self, agent, decision, outcome):
        # Write to database/file
        pass

# 4. Create main.py
swarm = Swarm(
    agents=[content_classifier, review_coordinator, ...],
    tools=[...],
    orchestration=route_to_next_agent
)

# 5. Deploy
# python main.py --port 8000
# Test with curl
# Monitor with logging
```

---

## Mode-Specific Translation Patterns

### 3-Layer Mode (Deterministic)

**Pattern:** Sequential steps, no branching

**Claude:**
```markdown
## System Prompt Pattern for 3-Layer

Follow these exact steps in order:

1. [First step description]
   Use: [tool name]
   
2. [Second step description]
   Use: [tool name]
   
3. [Third step description]
   Use: [tool name]

Always complete all steps.
Always log decisions.
Do not skip or reorder steps.
```

**Copilot:**
```
Skill Input:
├─ Step 1: Call function-1
├─ Step 2: Call function-2
├─ Step 3: Call function-3
└─ Output: Return result
```

**Swarm:**
```python
def agent_step_1(inputs):
    # Execute step 1
    return step_1_output

def agent_step_2(inputs):
    # Execute step 2
    return step_2_output

# Call sequentially (never branching)
result = agent_step_1(inputs)
result = agent_step_2(result)
```

### RL-Loop Mode (Learning)

**Pattern:** Log outcomes, adjust strategy, improve over time

**Claude:**
```markdown
## System Prompt Pattern for RL-Loop

Your goal is to maximize [metric: e.g., recommendation relevance].

Decision Strategy:
1. Make recommendation based on learned patterns
2. [tool: log_recommendation]
3. Wait for feedback (user interaction)
4. [tool: log_outcome] - Did user engage?
5. Adjust strategy for next time

Learning Mechanism:
- Store successful patterns: [tool: record_successful_pattern]
- Retrieve learned patterns: [tool: get_learned_patterns]
- Adjust weights: Increase probability of successful patterns

Tools available:
- log_recommendation: Record what you recommend
- log_outcome: Record if user engaged
- get_learned_patterns: Retrieve successful patterns
- record_successful_pattern: Save new success
```

**Swarm:**
```python
class LearnerAgent:
    def __init__(self):
        self.learned_patterns = []
    
    def make_decision(self, inputs):
        # Get learned patterns
        patterns = self.get_learned_patterns()
        
        # Make decision favoring successful patterns
        decision = self.strategy(inputs, patterns)
        
        # Log for feedback
        self.log_decision(decision, inputs)
        
        return decision
    
    def receive_feedback(self, outcome):
        # Learn from outcome
        if outcome.success:
            self.learned_patterns.append(outcome.pattern)
```

### Event-Driven Mode (Reactive)

**Pattern:** Listen for events, respond immediately

**Claude:**
```markdown
## System Prompt Pattern for Event-Driven

You respond to events.

Supported events:
- alert_received: [Description]
- threshold_exceeded: [Description]
- deadline_approaching: [Description]

For each event:
1. Receive event data
2. Assess urgency
3. Take action (log, notify, escalate)
4. Return immediately

Response time target: < 2 seconds

Tools:
- parse_event: Extract event details
- assess_urgency: Rate severity
- escalate: Route to escalation agent
- log_event: Record for analysis
```

**Gemini:**
```python
@functions_framework.http
def event_handler(request):
    """Respond to incoming event"""
    event = request.get_json()
    
    # Agent evaluates event
    response = gemini_agent.evaluate(event)
    
    # Return immediately
    return {
        "action": response.action,
        "escalated": response.escalated,
        "latency_ms": time_elapsed_ms
    }
```

### Agentic-Swarm Mode (Multi-Agent)

**Pattern:** Coordinator routes to specialists, combines results

**Claude:**
```markdown
## System Prompt Pattern for Agentic-Swarm (Coordinator)

You coordinate a team of specialists.

Team members:
- Specialist A: [Responsibility]
- Specialist B: [Responsibility]
- Specialist C: [Responsibility]

Coordination process:
1. Receive input
2. Analyze which specialists are needed
3. Ask each specialist: "How would you approach this?"
4. Combine their responses
5. Return coordinated answer

Ask specialists using: [tool: ask_specialist]
```

**AutoGen:**
```python
from autogen import ConversableAgent, GroupChat

# Define specialists (ConversableAgents)
specialist_a = ConversableAgent(name="specialist_a", ...)
specialist_b = ConversableAgent(name="specialist_b", ...)

# Define coordinator
coordinator = ConversableAgent(
    name="coordinator",
    system_message="Coordinate specialist responses"
)

# Create group chat
group_chat = GroupChat(
    agents=[coordinator, specialist_a, specialist_b],
    messages=[],
    max_round=5
)

# Coordinator leads discussion
coordinator.initiate_chat(group_chat, message="How should we handle this?")
```

---

## Learning Loop Translation

### Step 1: Feedback Capture → Vendor Logging

**arche feedback-log.md:**
```markdown
| Date | Agent | Decision | Outcome | Notes |
|------|-------|----------|---------|-------|
| 2026-01-05 | Classifier | Category: Spam | Correct ✓ | ... |
| 2026-01-05 | Classifier | Category: News | Wrong ✗ | ... |
```

**Claude translation:**
```python
def log_feedback_tool(decision: str, outcome: str, notes: str):
    """Tool that Claude uses to log feedback"""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "decision": decision,
        "outcome": outcome,  # "correct" or "wrong"
        "notes": notes
    }
    # Store in database
    db.insert("feedback_log", entry)
    return f"Logged: {outcome}"
```

**Copilot translation:**
```json
{
  "connector": "Azure Application Insights",
  "event": "agent_feedback",
  "properties": {
    "timestamp": "2026-01-05T...",
    "agent_name": "classifier",
    "decision": "category: spam",
    "outcome": "correct",
    "confidence": 0.95
  }
}
```

**Gemini translation:**
```python
# In Cloud Logging
logging.info(
    "agent_feedback",
    extra={
        "json_fields": {
            "agent": "classifier",
            "decision": "category: spam",
            "outcome": "correct",
            "confidence": 0.95
        }
    }
)
```

### Step 2: Weekly Analysis → Vendor Reports

**arche process:**
```markdown
# Weekly Review (manual, every Monday)
1. Read 09_learning/feedback-log.md
2. Analyze patterns (accuracy, errors, etc.)
3. Write findings to 09_learning/issue-backlog.md
4. Create change requests if improvements found
```

**Claude translation:**
```python
# Claude Project Tool for Analysis
def weekly_analysis_tool():
    """Run weekly analysis on feedback"""
    # Query feedback database
    logs = db.query("feedback_log", 
                     where=week_filter,
                     order_by="timestamp")
    
    # Analyze
    accuracy = sum(1 for l in logs if l.outcome=="correct") / len(logs)
    common_errors = find_patterns(logs)
    
    # Generate report
    report = {
        "accuracy": accuracy,
        "common_errors": common_errors,
        "recommendations": generate_recommendations(common_errors)
    }
    
    return report
```

**Automation with scheduler:**
```python
# Every Monday at 9 AM
from schedule import every, run_pending

@every().monday.do(run_weekly_analysis)
def run_weekly_analysis():
    report = claude.call_tool("weekly_analysis_tool")
    save_report(report)
    send_notification(report)

while True:
    run_pending()
```

### Step 3: Improvements → Deployed Updates

**Process:**

```
Weekly analysis → Identifies improvement → Creates change request
                 ↓
arche MAO team decides to implement
                 ↓
Updates agent manual or learning system
                 ↓
Re-translates to vendor format
                 ↓
Deploys updated version
                 ↓
Evaluation scenarios test improvement
                 ↓
Feedback loop continues with improved agent
```

**Example:**

```markdown
## Change Request: Improve Classifier Accuracy

### Finding
Weekly analysis showed classifier at 89% accuracy, target 92%.
Most errors: False positives in "news" category (misclassified as "misinformation")

### Change
Update 3-Layer classifier step 1:
OLD: "Check if content makes factual claims"
NEW: "Check if content makes factual claims. 
      If news source (reputable publication), apply lower threshold for misinformation."

### Implementation
1. Update arche agent manual
2. Re-translate to Claude: New system prompt
3. Deploy to staging
4. Run eval-scenario-ambiguous-case.md
5. If accuracy improves, deploy to production
6. Monitor results in feedback loop

### Validation
- Eval scenario accuracy: +4% (91% → 95%)
- False positive rate: -2%
- Ready to deploy ✓
```

---

## Vendor-Specific Deployment Guides

### Claude Projects Deployment

```markdown
## Deploy arche MAO to Claude Projects

### Prerequisites
- Claude project created in claude.ai
- Agents and tools defined
- Feedback logging tool ready

### Deployment Checklist
- [ ] System prompts use arche agent manuals
- [ ] Tools defined for all operations
- [ ] Knowledge base populated with domain docs
- [ ] Evaluation scenarios loaded as test cases
- [ ] Feedback logging configured
- [ ] Weekly analysis automation set up
- [ ] Team members invited to project

### Monitoring
- Use Claude Activity view to see agent responses
- Check feedback database for logging
- Run weekly analysis to track improvement
- Create GitHub issues for improvement ideas

### Scaling
- Add more specialized agents if needed
- Update routing based on usage patterns
- Retrain on feedback quarterly
```

### Copilot Studio Deployment

```markdown
## Deploy arche MAO to Copilot Studio

### Prerequisites
- Copilot created in Copilot Studio
- Skills defined for each agent role
- Connectors set up for external systems

### Deployment Checklist
- [ ] Copilot Instructions describe MAO scope
- [ ] Each skill has proper instructions and schema
- [ ] Skills tested individually
- [ ] Orchestration routing configured
- [ ] Connectors working (logging, APIs, etc.)
- [ ] Error handling defined
- [ ] Escalation paths clear
- [ ] Published to channel (Web, Teams, etc.)

### Monitoring
- Use Analytics view to see skill usage
- Check connector logs for data flow
- Monitor escalation patterns
- Track user satisfaction

### Scaling
- Add new skills as needed
- Optimize skill latency
- Deploy to additional channels
- Add human handoff if needed
```

---

## Troubleshooting

### "Agent not learning - feedback isn't captured"

**Diagnosis:**
1. Check: Is feedback logging tool being called?
2. Check: Is database/file receiving logs?
3. Check: Does log format match expected schema?

**Solution:**
- Add explicit logging in agent system prompt
- Verify tool definitions include feedback logging
- Test tool directly before integration
- Add error handling for logging failures

### "Evaluation scenario fails but agent seems to work"

**Diagnosis:**
1. Eval scenario expectations may be too strict
2. Agent may be behaving differently in real vs. test
3. Vendor environment may have limitations

**Solution:**
- Review eval scenario success criteria
- Test agent directly with scenario input
- Check if scenario is realistic
- Adjust timeout/latency expectations

### "Learning improvements aren't being deployed"

**Diagnosis:**
1. Process for deploying updates may be unclear
2. Manual steps (re-translation) may be forgotten
3. Vendor may not support live updates

**Solution:**
- Create deployment automation (CI/CD)
- Use foundry-translate to auto-regenerate
- Set up auto-deploy pipeline
- Document deployment process clearly

---

## Best Practices

✅ **DO:**
- Keep arche MAO as source of truth
- Regenerate vendor format when MAO changes
- Test all evaluation scenarios after deployment
- Log all agent decisions for learning
- Review feedback weekly
- Update arche MAO based on learnings
- Maintain vendor-agnostic design

❌ **DON'T:**
- Edit vendor format directly (changes get lost)
- Skip evaluation testing
- Ignore feedback logs
- Let manual processes break learning loop
- Lock yourself into one vendor
- Create vendor-specific hardcoding

---

## Summary: From arche to Production

```
arche MAO scaffold (vendor-agnostic)
         ↓
foundry-translate --target [vendor]
         ↓
vendor-specific MAO (ready to deploy)
         ↓
Deploy to vendor environment
         ↓
Setup learning feedback capture
         ↓
Run evaluation scenarios
         ↓
Monitor and improve weekly
         ↓
Share learnings back to arche ecosystem
```

**Time from arche to production:** 1-2 weeks (including testing and learning loop setup)

---

## See Also

- [VENDOR_SELECTION_DECISION_TREE.md](VENDOR_SELECTION_DECISION_TREE.md) — Choose your deployment vendor
- [VENDOR_TRANSLATION_SPECIFICATION.md](VENDOR_TRANSLATION_SPECIFICATION.md) — Complete architecture and vendor specs
- [../frameworks/MODE_COMPATIBILITY.md](../frameworks/MODE_COMPATIBILITY.md) — Mode patterns for vendor deployment
- [../learning/FRAMEWORK_LEARNING_LOOP.md](../learning/FRAMEWORK_LEARNING_LOOP.md) — Feedback loops for production
- [examples/](examples/) — Worked examples of vendor translations
- [../README.md](../README.md) — Vendor translation overview

---

