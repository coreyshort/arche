# Example: Translating BP-0004 (Content Moderation) to OpenAI Swarm

**Purpose:** Translate arche Multi-Agent Organizations to OpenAI Swarm for deterministic agent coordination and lightweight deployments.

---

## Overview

### What is OpenAI Swarm?

OpenAI Swarm is a lightweight framework for building deterministic, multi-agent systems with predictable routing and hand-off patterns. It emphasizes:
- Simple agent definitions with clear responsibilities
- Explicit hand-offs between agents
- Lightweight execution (single Python process)
- Deterministic behavior
- Easy debugging and testing
- Direct control flow

### Why Translate to Swarm?

**Best for:**
- Deterministic workflows with clear routing
- Lightweight deployments
- Systems where predictability matters
- API-based implementations needing simplicity
- Teams preferring explicit control flow over emergent behavior

**Strengths:**
- ✅ Simple agent model
- ✅ Explicit, predictable hand-offs
- ✅ Lightweight and fast
- ✅ Easy to understand and debug
- ✅ Direct function-based routing
- ✅ Good for production systems with clear logic

**Limitations:**
- ⚠️ Less flexible than graph-based approaches
- ⚠️ No built-in persistence
- ⚠️ Limited to single-process execution
- ⚠️ Requires manual hand-off management

---

## Architecture Mapping

### arche Concepts → OpenAI Swarm

| arche Concept | Swarm Implementation |
|---------------|-------------------|
| **Agent** | `Agent` class with tools and instructions |
| **Directive** | Agent `instructions` (system prompt) |
| **Orchestrator** | Router agent with hand-off logic |
| **Executor** | Agent with `tools` for execution |
| **Coordination** | Hand-off function returning next agent |
| **Tool/Action** | `@tool` decorated function |

### arche Modes → Swarm

| arche Mode | Swarm Pattern |
|-----------|--------------|
| **3-Layer** | Classifier agent → Router → Executor agent |
| **Agentic-Swarm** | Supervisor agent → Sub-agents via hand-offs |
| **Event-Driven** | Input handler → Conditional routing → Processing |
| **RL-Loop** | Manual feedback collection → Human policy updates |

### Agent Archetypes → Swarm Agents

| arche Agent | Swarm Agent Pattern |
|------------|-------------------|
| **Executor** | Agent with tools for execution |
| **Learner** | Agent with feedback processing tools |
| **Orchestrator** | Router agent selecting hand-off |
| **Monitor** | Tracking agent collecting metrics |
| **Validator** | Agent with validation tools |

---

## Translation Process

### Phase 1: Plan Your Agent Structure

#### Step 1: Identify Agent Boundaries

**arche MAO (BP-0004):**
```
Agents:
- Classifier: Analyze content for policy violations
- Analyzer: Understand context and threat level
- Escalation Manager: Route to human if needed
- Feedback Processor: Collect and store feedback
```

**Swarm Structure:**
```python
# Four specialized agents with clear hand-offs
classifier_agent = Agent(...)
analyzer_agent = Agent(...)
escalation_agent = Agent(...)
feedback_agent = Agent(...)

# Hand-off logic determines flow
classifier -> analyzer or escalation -> feedback
```

#### Step 2: Define Hand-Off Logic

**Routing Rules:**
```python
def router_classifier(result):
    """Route from classifier to next agent."""
    if result["confidence"] < ESCALATION_THRESHOLD:
        return escalation_agent
    else:
        return analyzer_agent

def router_analyzer(result):
    """Route from analyzer to feedback."""
    return feedback_agent
```

#### Step 3: Map Tools and Capabilities

**Tools needed:**
```
Classifier:
  - check_policy_violations()
  - classify_content()

Analyzer:
  - analyze_user_history()
  - search_similar_content()

Escalation Manager:
  - queue_for_human_review()
  - notify_team()

Feedback Processor:
  - store_feedback()
  - calculate_metrics()
```

---

### Phase 2: Implement Agents

#### Agent 1: Classifier Agent

**arche Directive:**
```markdown
# Directive: Classify Content

## Input
- content: string (text to analyze)
- policy_version: string (rules to apply)

## Rules
- Check for violence indicators
- Check for harassment patterns
- Check for misinformation
- Return category and confidence

## Output
- classification: string
- confidence: float
- violations: list
```

**Swarm Agent:**
```python
from swarm import Agent
import anthropic

# Initialize client
client = anthropic.Anthropic()

# Define tools
tools = [
    {
        "name": "check_policy_violations",
        "description": "Check content against policy rules",
        "input_schema": {
            "type": "object",
            "properties": {
                "content": {"type": "string"},
                "policy_version": {"type": "string"}
            },
            "required": ["content", "policy_version"]
        }
    },
    {
        "name": "classify_content",
        "description": "Classify content into categories",
        "input_schema": {
            "type": "object",
            "properties": {
                "content": {"type": "string"},
                "violations": {"type": "array"}
            },
            "required": ["content", "violations"]
        }
    }
]

# Classifier agent
classifier_agent = Agent(
    name="Classifier",
    model="gpt-4",
    tools=tools,
    instructions="""You are a content classifier. Analyze the provided content 
for policy violations. Use the check_policy_violations tool to identify issues, 
then classify_content to determine the category.

Return a JSON object with:
{
    "classification": "SAFE|VIOLATION|UNCERTAIN",
    "confidence": 0.0-1.0,
    "violations": ["list of violations"],
    "reason": "explanation"
}"""
)

# Tool implementations (called by framework)
def check_policy_violations(content: str, policy_version: str) -> dict:
    """Check content against policy."""
    # Call policy API or run local rules
    return {
        "violence_score": 0.2,
        "harassment_score": 0.1,
        "misinformation_score": 0.8
    }

def classify_content(content: str, violations: list) -> dict:
    """Classify based on violations."""
    max_score = max(violations.values()) if violations else 0
    if max_score > 0.7:
        return {"classification": "VIOLATION", "confidence": max_score}
    elif max_score > 0.3:
        return {"classification": "UNCERTAIN", "confidence": max_score}
    else:
        return {"classification": "SAFE", "confidence": 1 - max_score}
```

#### Agent 2: Analyzer Agent

**arche Directive:**
```markdown
# Directive: Analyze Context

## Input
- content: string
- user_id: string
- classification: string
- confidence: float

## Analysis
- Look at user history
- Find similar content decisions
- Calculate threat level
- Identify policy gaps

## Output
- threat_level: string (LOW|MEDIUM|HIGH)
- context_summary: string
- policy_gaps: list
```

**Swarm Agent:**
```python
analyzer_agent = Agent(
    name="Analyzer",
    model="gpt-4",
    tools=[
        {
            "name": "analyze_user_history",
            "description": "Get user's moderation history",
            "input_schema": {
                "type": "object",
                "properties": {
                    "user_id": {"type": "string"}
                },
                "required": ["user_id"]
            }
        },
        {
            "name": "search_similar_content",
            "description": "Find similar content decisions",
            "input_schema": {
                "type": "object",
                "properties": {
                    "content": {"type": "string"},
                    "limit": {"type": "integer", "default": 5}
                },
                "required": ["content"]
            }
        }
    ],
    instructions="""You are a context analyzer. Given classified content,
provide deeper analysis considering user history and similar content patterns.

Return a JSON object with:
{
    "threat_level": "LOW|MEDIUM|HIGH",
    "context_summary": "brief explanation",
    "similar_cases": ["list of similar decisions"],
    "policy_gaps": ["identified gaps"],
    "recommendation": "action to take"
}"""
)

def analyze_user_history(user_id: str) -> dict:
    """Get user moderation history."""
    return {
        "violations_count": 2,
        "last_violation": "2025-12-15",
        "pattern": "repeat offender",
        "severity": "escalating"
    }

def search_similar_content(content: str, limit: int = 5) -> dict:
    """Find similar content decisions."""
    return {
        "similar_count": 3,
        "examples": [
            {"content": "similar 1", "decision": "REJECT"},
            {"content": "similar 2", "decision": "REJECT"},
            {"content": "similar 3", "decision": "REJECT"}
        ]
    }
```

#### Agent 3: Escalation Agent

**arche Directive:**
```markdown
# Directive: Escalate to Human

## Input
- content: string
- classification: string
- confidence: float
- threat_level: string

## Escalation
- Queue to moderation team
- Set priority
- Attach full context
- Create escalation ticket

## Output
- escalation_id: string
- queue_position: int
- estimated_review_time: int
```

**Swarm Agent:**
```python
escalation_agent = Agent(
    name="Escalation Manager",
    model="gpt-4",
    tools=[
        {
            "name": "queue_for_human_review",
            "description": "Queue content for human moderation",
            "input_schema": {
                "type": "object",
                "properties": {
                    "content": {"type": "string"},
                    "priority": {"type": "string"},
                    "context": {"type": "object"}
                },
                "required": ["content", "priority"]
            }
        },
        {
            "name": "notify_team",
            "description": "Notify moderation team of escalation",
            "input_schema": {
                "type": "object",
                "properties": {
                    "escalation_id": {"type": "string"},
                    "priority": {"type": "string"}
                },
                "required": ["escalation_id", "priority"]
            }
        }
    ],
    instructions="""You are responsible for escalating uncertain content to humans.
Queue the content, notify the team, and return escalation details.

Return a JSON object with:
{
    "escalation_id": "unique id",
    "status": "queued",
    "priority": "high|normal|low",
    "estimated_review_time_minutes": 5-30
}"""
)

def queue_for_human_review(content: str, priority: str, context: dict) -> dict:
    """Queue content for human review."""
    escalation_id = f"ESC_{datetime.now().timestamp()}"
    return {
        "escalation_id": escalation_id,
        "queued_at": datetime.now().isoformat(),
        "position": get_queue_position(priority)
    }

def notify_team(escalation_id: str, priority: str) -> dict:
    """Notify moderation team."""
    return {
        "notification_sent": True,
        "team": "moderation_team",
        "channel": "teams"
    }
```

#### Agent 4: Feedback Agent

**arche Directive:**
```markdown
# Directive: Track Feedback

## Input
- original_decision: string
- content: string
- human_decision: optional string

## Processing
- Store decision record
- Update metrics
- Identify improvements
- Queue for learning cycle

## Output
- feedback_id: string
- metrics_updated: boolean
```

**Swarm Agent:**
```python
feedback_agent = Agent(
    name="Feedback Processor",
    model="gpt-4",
    tools=[
        {
            "name": "store_feedback",
            "description": "Store moderation decision and feedback",
            "input_schema": {
                "type": "object",
                "properties": {
                    "decision": {"type": "string"},
                    "content": {"type": "string"},
                    "confidence": {"type": "number"},
                    "human_override": {"type": "string"}
                },
                "required": ["decision", "content"]
            }
        },
        {
            "name": "calculate_metrics",
            "description": "Update performance metrics",
            "input_schema": {
                "type": "object",
                "properties": {}
            }
        }
    ],
    instructions="""You are responsible for collecting feedback and updating metrics.
Store the decision record and calculate updated performance metrics.

Return a JSON object with:
{
    "feedback_id": "unique id",
    "stored": true,
    "metrics_updated": true,
    "accuracy": 0.92,
    "false_positive_rate": 0.08
}"""
)

def store_feedback(decision: str, content: str, confidence: float, 
                   human_override: str = None) -> dict:
    """Store feedback record."""
    record = {
        "id": f"FB_{datetime.now().timestamp()}",
        "decision": decision,
        "content_hash": hash(content),
        "confidence": confidence,
        "human_override": human_override,
        "timestamp": datetime.now().isoformat()
    }
    # Store in database
    save_to_db(record)
    return {"feedback_id": record["id"], "stored": True}

def calculate_metrics() -> dict:
    """Calculate current metrics."""
    all_feedback = get_all_feedback()
    return {
        "total_decisions": len(all_feedback),
        "accuracy": calculate_accuracy(all_feedback),
        "false_positive_rate": calculate_fp_rate(all_feedback),
        "false_negative_rate": calculate_fn_rate(all_feedback)
    }
```

---

### Phase 3: Define Hand-Off Functions

#### Hand-Off from Classifier

```python
def classifier_hand_off(classifier_response: str) -> Agent:
    """Route from classifier to next agent."""
    
    # Parse response
    result = parse_json(classifier_response)
    confidence = result.get("confidence", 0)
    
    # Route based on confidence
    if confidence < ESCALATION_THRESHOLD:  # 0.7
        return escalation_agent
    else:
        return analyzer_agent
```

#### Hand-Off from Analyzer

```python
def analyzer_hand_off(analyzer_response: str) -> Agent:
    """Route from analyzer to feedback collection."""
    # Always proceed to feedback after analysis
    return feedback_agent
```

#### Hand-Off from Escalation

```python
def escalation_hand_off(escalation_response: str) -> Agent:
    """Route from escalation to feedback."""
    # Always proceed to feedback
    return feedback_agent
```

---

### Phase 4: Orchestrate with User Interaction

#### Main Orchestration Loop

```python
from swarm import Swarm

client = anthropic.Anthropic()
swarm_client = Swarm(client=client)

def moderate_content(content: str, user_id: str, policy_version: str = "v1.2"):
    """Main moderation flow."""
    
    # Prepare initial message
    messages = [
        {
            "role": "user",
            "content": f"""Please moderate this content:

Content: {content}
User ID: {user_id}
Policy Version: {policy_version}

Analyze it using the full workflow:
1. First classify the content
2. Then analyze the context
3. Escalate if needed
4. Track the feedback"""
        }
    ]
    
    # Start with classifier agent
    agent = classifier_agent
    
    # Run swarm
    response = swarm_client.run(
        agent=agent,
        messages=messages
    )
    
    return response

# Usage
result = moderate_content(
    content="This is violent content example",
    user_id="user_123"
)

print(result)
```

---

### Phase 5: Integrate Learning Feedback

#### Capture Human Decisions

```python
def process_human_feedback(escalation_id: str, human_decision: str):
    """Process human review feedback."""
    
    # Get escalation record
    escalation = get_escalation(escalation_id)
    
    # Create feedback message
    messages = [
        {
            "role": "user",
            "content": f"""Process human feedback:

Original Decision: {escalation['original_decision']}
Human Decision: {human_decision}
Content: {escalation['content']}
Reason: Human reviewed and {human_decision}

Please update metrics and store this feedback."""
        }
    ]
    
    # Run feedback agent
    response = swarm_client.run(
        agent=feedback_agent,
        messages=messages
    )
    
    return response
```

#### Weekly Analytics

```python
import schedule
import time

def weekly_analytics_job():
    """Analyze metrics weekly."""
    
    metrics = get_metrics()
    
    print(f"Weekly Moderation Report")
    print(f"Total Decisions: {metrics['total_decisions']}")
    print(f"Accuracy: {metrics['accuracy']:.2%}")
    print(f"False Positive Rate: {metrics['false_positive_rate']:.2%}")
    print(f"False Negative Rate: {metrics['false_negative_rate']:.2%}")
    
    # Generate recommendations
    if metrics['false_positive_rate'] > 0.15:
        print("⚠️  High false positive rate - consider lowering threshold")
    if metrics['false_negative_rate'] > 0.1:
        print("⚠️  High false negative rate - consider raising threshold")
    
    # Notify team
    notify_team_metrics(metrics)

# Schedule
schedule.every().friday.at("10:00").do(weekly_analytics_job)

while True:
    schedule.run_pending()
    time.sleep(60)
```

---

## Complete Implementation Example

### Project Structure

```
content-moderation-swarm/
├── main.py
├── agents.py
├── tools.py
├── hand_offs.py
├── config.py
├── learning.py
├── tests/
│   ├── test_agents.py
│   ├── test_hand_offs.py
│   └── test_integration.py
└── requirements.txt
```

### Main Application

```python
# main.py
from swarm import Swarm
import anthropic
from agents import (
    classifier_agent,
    analyzer_agent,
    escalation_agent,
    feedback_agent
)
from config import ESCALATION_THRESHOLD

client = anthropic.Anthropic()
swarm = Swarm(client=client)

async def moderate_content(
    content: str,
    user_id: str,
    policy_version: str = "v1.2"
) -> dict:
    """Main content moderation endpoint."""
    
    messages = [
        {
            "role": "user",
            "content": f"""Moderate this content using the full workflow:

Content: {content}
User ID: {user_id}
Policy Version: {policy_version}

Steps:
1. Classify the content
2. Analyze context
3. Escalate if needed
4. Track feedback

Return final decision with reasoning."""
        }
    ]
    
    response = swarm.run(
        agent=classifier_agent,
        messages=messages
    )
    
    return {
        "user_id": user_id,
        "decision": extract_decision(response),
        "reasoning": response.messages[-1]["content"]
    }

if __name__ == "__main__":
    import asyncio
    result = asyncio.run(moderate_content(
        "Test content",
        "user_123"
    ))
    print(result)
```

---

## Configuration Checklist

- [ ] Python 3.10+ installed
- [ ] OpenAI Swarm installed (`pip install swarm-py`)
- [ ] Anthropic/OpenAI API keys configured
- [ ] All agent definitions complete
- [ ] All tool implementations done
- [ ] Hand-off functions defined and tested
- [ ] Main orchestration loop working
- [ ] Error handling implemented
- [ ] Logging configured
- [ ] Database for feedback configured
- [ ] Metrics calculation working
- [ ] Weekly job scheduler set up
- [ ] Unit tests passing
- [ ] Integration tests passing
- [ ] Documentation complete
- [ ] Ready for deployment

---

## Comparison: arche vs Swarm

| Aspect | arche MAO | OpenAI Swarm |
|--------|-----------|-------------|
| **Definition** | Markdown directives | Python agents + hand-offs |
| **Agents** | Agent archetypes | Agent class instances |
| **Coordination** | Coordination patterns | Hand-off functions |
| **Execution** | Abstract | Direct Python execution |
| **Tools** | Tool specifications | LangChain tool binding |
| **Hand-Offs** | Implicit | Explicit return next agent |
| **State** | Implicit | Message history |
| **Control Flow** | Declarative | Imperative (explicit routing) |
| **Complexity** | Low (specification) | Medium (implementation) |
| **Predictability** | Medium | High (explicit hand-offs) |

---

## Advantages of Swarm for arche

1. **Simplicity** — Easy to understand agent boundaries
2. **Explicitness** — Clear routing logic in hand-offs
3. **Lightweight** — Single Python process, easy deployment
4. **Deterministic** — Predictable hand-off behavior
5. **Debuggable** — Clear message flow, easy to trace
6. **Testing** — Simple agent testing without graph complexity

---

## When Swarm Might Not Be Ideal

- Complex multi-turn with cycles → Use LangGraph
- Distributed coordination → Use AutoGen
- Enterprise integration → Use Copilot Studio
- Rapid prototyping → Use Claude Projects
- Multimodal → Use Gemini

---

## Troubleshooting

### Agent Not Receiving Context

**Problem:** Hand-off not passing full state to next agent

**Solution:**
```python
def hand_off_with_context(response: str) -> Agent:
    """Pass context through hand-off."""
    # Extract context from response
    context = parse_context(response)
    
    # Pass to next agent via instructions
    agent = next_agent
    agent.instructions += f"\n\nContext from previous step: {context}"
    
    return agent
```

### Tools Not Being Called

**Problem:** Agent not invoking tools defined in agent

**Solution:**
```python
# Ensure tools are properly formatted
agent = Agent(
    name="MyAgent",
    model="gpt-4",
    tools=[
        {
            "name": "my_tool",
            "description": "Clear description of what tool does",
            "input_schema": {
                "type": "object",
                "properties": {...},
                "required": [...]
            }
        }
    ],
    instructions="Use tools to accomplish tasks"  # Prompt to use tools
)
```

### Hand-Off Loop

**Problem:** Agents cycling between each other

**Solution:**
```python
# Add termination conditions
def safe_hand_off(response: str, visited_agents: set) -> Agent:
    next_agent = determine_next(response)
    
    if next_agent.name in visited_agents:
        return None  # Terminate to avoid loop
    
    return next_agent
```

---

## Related Documentation

- [VENDOR_TRANSLATION_SPECIFICATION.md](../VENDOR_TRANSLATION_SPECIFICATION.md) — Architecture specification
- [VENDOR_INTEGRATION_GUIDE.md](../VENDOR_INTEGRATION_GUIDE.md) — Step-by-step integration
- [VENDOR_SELECTION_DECISION_TREE.md](../VENDOR_SELECTION_DECISION_TREE.md) — When to use Swarm
- [../../modes/3-layer/](../../modes/3-layer/) — 3-Layer mode implementation
- [../../blueprints/BP-0004.md](../../blueprints/BP-0004.md) — Content Moderation blueprint

---

## Additional Resources

**OpenAI Swarm Documentation:**
- [GitHub Repository](https://github.com/openai/swarm)
- [Getting Started](https://github.com/openai/swarm#usage)
- [Agent Definition](https://github.com/openai/swarm#agent)
- [Hand-Offs](https://github.com/openai/swarm#hand-offs)

**arche Resources:**
- [CHOOSE_YOUR_PATH.md](../../docs/getting-started/CHOOSE_YOUR_PATH.md) — Learning path guidance
- [AGENT_ARCHETYPES.md](../../docs/frameworks/AGENT_ARCHETYPES.md) — Agent patterns
- [MODE_COMPATIBILITY.md](../../docs/frameworks/MODE_COMPATIBILITY.md) — Mode combinations

---

**Status:** Reference Documentation  
**Last Updated:** January 5, 2026  
**Maintainer:** Community
