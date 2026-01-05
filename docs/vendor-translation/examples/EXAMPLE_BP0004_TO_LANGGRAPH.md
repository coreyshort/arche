# Example: Translating BP-0004 (Content Moderation) to LangGraph

**Purpose:** Translate arche Multi-Agent Organizations to LangGraph for Python-first, production-grade agentic systems.

---

## Overview

### What is LangGraph?

LangGraph is a framework for building stateful, multi-actor applications with LLMs. It provides:
- Graph-based agent coordination (nodes, edges, cycles)
- Built-in persistence and checkpointing
- Streaming and real-time capabilities
- Full Python control (no low-code restrictions)
- Integration with LangChain ecosystem
- Human-in-the-loop workflows

### Why Translate to LangGraph?

**Best for:**
- Custom, complex agent workflows
- Production systems requiring full control
- Research and experimentation
- Multi-turn, stateful interactions
- Iterative refinement
- Custom memory and persistence

**Strengths:**
- ✅ Maximum flexibility and control
- ✅ Full Python capabilities
- ✅ Graph-based reasoning about agents
- ✅ Built-in persistence (checkpointing)
- ✅ Streaming and real-time updates
- ✅ Human-in-the-loop out of the box
- ✅ Cycle support (loops within agents)

**Limitations:**
- ⚠️ Requires Python expertise
- ⚠️ More operational overhead than managed services
- ⚠️ Self-hosted deployment needed
- ⚠️ Steeper learning curve

---

## Architecture Mapping

### arche Concepts → LangGraph

| arche Concept | LangGraph Implementation |
|---------------|------------------------|
| **Agent** | Graph node with state management |
| **Directive** | Node implementation + system prompt |
| **Orchestrator** | Conditional routing edges |
| **Executor** | Leaf nodes with tool/API calls |
| **Coordination** | Graph edges + routing logic |
| **Feedback** | Persistence layer + state updates |

### arche Modes → LangGraph

| arche Mode | LangGraph Pattern |
|-----------|------------------|
| **3-Layer** | Nodes (layers) → edges (routing) → cycles (feedback) |
| **Agentic-Swarm** | Sub-graphs for specialized agents + supervisor node |
| **Event-Driven** | Event listeners → conditional edges → state updates |
| **RL-Loop** | State persistence → metrics collection → policy node |

### Agent Archetypes → LangGraph Nodes

| arche Agent | LangGraph Node Pattern |
|------------|----------------------|
| **Executor** | `def execute_node(state) → updated_state` with tools |
| **Learner** | `def learn_node(state) → policy_updates` with analytics |
| **Orchestrator** | Router node with `_route()` function selecting next node |
| **Monitor** | State checkpoint with metrics extraction |
| **Validator** | Precondition checks → conditional routing |

---

## Translation Process

### Phase 1: Plan Your Graph

#### Step 1: Model State Structure

**arche Model (Directives):**
```yaml
# BP-0004: Content Moderation
Inputs:
  - content: string
  - user_id: string
  - policy_version: string
  - escalation_threshold: float

Outputs:
  - decision: string (APPROVE | REJECT | ESCALATE)
  - confidence: float
  - reason: string
  - policy_applied: string
```

**LangGraph State:**
```python
from typing import TypedDict, Literal
from langgraph.graph import MessagesState

class ModerationState(TypedDict):
    # Input
    content: str
    user_id: str
    policy_version: str
    escalation_threshold: float
    
    # Processing
    classification: str
    confidence: float
    context_analysis: dict
    
    # Output
    decision: Literal["APPROVE", "REJECT", "ESCALATE"]
    reason: str
    policy_applied: str
    
    # Learning
    human_review: Optional[str]
    review_feedback: Optional[str]
    
    # Metadata
    attempt_count: int
    messages: list  # For multi-turn
```

#### Step 2: Identify Nodes

**Mapping arche Agents to LangGraph Nodes:**

```
Graph Structure:
┌─────────────────────────────────────┐
│     classify_content_node           │
│  (Classifier agent)                 │
└────────────────┬────────────────────┘
                 │
    ┌────────────┴────────────┐
    ↓                         ↓
┌──────────────────┐  ┌────────────────────┐
│ analyze_context  │  │  escalate_human    │
│    _node         │  │     _node          │
│ (Analyzer agent) │  │(Escalation Manager)│
└──────────────────┘  └────────────────────┘
    │                         │
    └────────────┬────────────┘
                 ↓
        ┌─────────────────────┐
        │  collect_feedback   │
        │      _node          │
        │(Feedback Processor) │
        └─────────────────────┘
```

#### Step 3: Plan Routing Logic

**Conditional Routing:**
```python
def router(state):
    if state["confidence"] < state["escalation_threshold"]:
        return "escalate_human_node"
    elif state["confidence"] > 0.9:
        return "collect_feedback_node"
    else:
        return "analyze_context_node"
```

---

### Phase 2: Translate Directives to Nodes

#### Pattern 1: Classifier Agent → Node with Tools

**arche Directive:**
```markdown
# Directive: Classify Content

## Input
- content: string (text to classify)
- policy_version: string (which policy rules)

## Rules
- Check for violence indicators
- Check for harassment patterns
- Check for misinformation flags
- Return category and confidence score

## Output
- classification: string
- confidence: float (0-1)
- violations: list of strings
```

**LangGraph Node Implementation:**
```python
from langchain_core.tools import tool
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")

# Define tools
@tool
def check_policy_violations(content: str, policy_version: str) -> dict:
    """Check content against policy rules."""
    # Call policy API or local rules engine
    return {
        "violence_score": 0.2,
        "harassment_score": 0.1,
        "misinformation_score": 0.8
    }

def classify_content_node(state: ModerationState) -> ModerationState:
    """Classify content using Claude + policy tools."""
    
    system_prompt = """You are a content classifier. 
    Analyze content against the policy version provided.
    Return classification, confidence, and violations found."""
    
    tools = [check_policy_violations]
    llm_with_tools = llm.bind_tools(tools)
    
    # Get classification
    response = llm_with_tools.invoke([
        {
            "role": "user",
            "content": f"""Classify this content using policy {state['policy_version']}:
            
{state['content']}"""
        }
    ])
    
    # Process response
    violations = check_policy_violations(
        state["content"],
        state["policy_version"]
    )
    
    max_score = max(violations.values())
    
    # Determine classification
    if max_score > 0.7:
        classification = "VIOLATION"
    elif max_score > 0.3:
        classification = "UNCERTAIN"
    else:
        classification = "SAFE"
    
    return {
        **state,
        "classification": classification,
        "confidence": max_score,
        "context_analysis": violations
    }
```

#### Pattern 2: Orchestrator → Router Node

**arche Directive:**
```markdown
# Directive: Route Decision

## Logic
1. Get classification from Classifier
2. If confidence < threshold → escalate to human
3. Else if confidence > 0.9 → finalize decision
4. Else → get more analysis

## Output
- next_step: string (analyze | escalate | finalize)
```

**LangGraph Router Node:**
```python
def route_decision(state: ModerationState) -> str:
    """Route based on classification confidence."""
    
    confidence = state["confidence"]
    escalation_threshold = state["escalation_threshold"]
    
    if confidence < escalation_threshold:
        return "escalate_human_node"
    elif confidence > 0.9:
        return "collect_feedback_node"
    else:
        return "analyze_context_node"
```

#### Pattern 3: Executor → Node with API Calls

**arche Directive:**
```markdown
# Directive: Escalate to Human

## Input
- content: string
- classification: string
- confidence: float
- context: dict

## Execution
1. Queue to moderation queue
2. Assign priority based on confidence
3. Wait for human decision
4. Store decision + feedback

## Output
- human_decision: string
- human_reasoning: string
- escalation_id: string
```

**LangGraph Node:**
```python
async def escalate_human_node(state: ModerationState) -> ModerationState:
    """Escalate uncertain cases to human review."""
    
    # Queue to human review system
    escalation = await queue_for_human_review({
        "content": state["content"],
        "user_id": state["user_id"],
        "classification": state["classification"],
        "confidence": state["confidence"],
        "priority": calculate_priority(state["confidence"])
    })
    
    # Decision will be added via human-in-the-loop mechanism
    # (See Phase 4: Human Handoff)
    
    return {
        **state,
        "decision": "ESCALATE",
        "reason": f"Confidence {state['confidence']:.2f} below threshold"
    }
```

#### Pattern 4: Learner → Node with Feedback Processing

**arche Directive:**
```markdown
# Directive: Process Feedback

## Input
- original_decision: string
- human_decision: string
- confidence: float
- context: dict

## Learning
1. Compare decisions
2. Calculate metrics (accuracy, etc)
3. Identify policy gaps
4. Store for weekly analysis

## Output
- feedback_stored: boolean
- metrics_updated: boolean
```

**LangGraph Node:**
```python
def collect_feedback_node(state: ModerationState) -> ModerationState:
    """Collect and store feedback for learning."""
    
    # In practice, this would be populated by human review
    # or retrieved from a feedback store
    
    feedback_record = {
        "original_decision": state["decision"],
        "content": state["content"],
        "classification": state["classification"],
        "confidence": state["confidence"],
        "policy_version": state["policy_version"],
        "timestamp": datetime.now(),
        "user_id": state["user_id"]
    }
    
    # Store feedback
    store_feedback(feedback_record)
    
    # Update metrics
    metrics = calculate_metrics()  # Aggregate from feedback store
    
    return {
        **state,
        "attempt_count": state["attempt_count"] + 1
    }
```

---

### Phase 3: Build the Graph

#### Complete Graph Definition

```python
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

# Create graph
workflow = StateGraph(ModerationState)

# Add nodes
workflow.add_node("classify_content", classify_content_node)
workflow.add_node("analyze_context", analyze_context_node)
workflow.add_node("escalate_human", escalate_human_node)
workflow.add_node("collect_feedback", collect_feedback_node)

# Add edges
workflow.add_edge(START, "classify_content")

# Add conditional edges (routing)
workflow.add_conditional_edges(
    "classify_content",
    route_decision,
    {
        "escalate_human_node": "escalate_human",
        "analyze_context_node": "analyze_context",
        "collect_feedback_node": "collect_feedback"
    }
)

# Both analysis and escalation paths lead to feedback
workflow.add_edge("analyze_context", "collect_feedback")
workflow.add_edge("escalate_human", "collect_feedback")

# Feedback leads to end
workflow.add_edge("collect_feedback", END)

# Compile with checkpointing
checkpointer = MemorySaver()
graph = workflow.compile(checkpointer=checkpointer)
```

#### Invocation with State Persistence

```python
# Invoke with thread_id for persistence
initial_state = {
    "content": "This is violent content...",
    "user_id": "user_123",
    "policy_version": "v1.2",
    "escalation_threshold": 0.7,
    "classification": None,
    "confidence": 0.0,
    "context_analysis": {},
    "decision": None,
    "reason": None,
    "policy_applied": None,
    "human_review": None,
    "review_feedback": None,
    "attempt_count": 0,
    "messages": []
}

# Run graph
config = {"configurable": {"thread_id": "user_123_session_1"}}
final_state = graph.invoke(initial_state, config)

# Access checkpointed state
checkpointed_state = graph.get_state(config)
```

---

### Phase 4: Set Up Human-in-the-Loop

LangGraph has native support for human-in-the-loop via breakpoints:

#### Interrupt at Escalation

```python
from langgraph.graph import StateGraph, START, END

# Mark node as requiring human input
workflow.add_node("escalate_human", escalate_human_node)

# Add breakpoint
def should_continue(state):
    return state["decision"] != "ESCALATE"

workflow.add_edge(
    "analyze_context",
    "escalate_human",
    metadata={"requires_human_input": True}
)

# When escalation is needed, graph pauses
# External system gets interrupted state
# Human provides decision
# Graph resumes with updated state
```

#### Resume After Human Decision

```python
# After human makes decision
updated_state = {
    **checkpointed_state,
    "human_review": "REJECT",
    "review_feedback": "Clear policy violation",
    "decision": "REJECT"
}

# Resume execution
final_state = graph.invoke(
    None,
    config,
    input=updated_state
)
```

---

### Phase 5: Set Up Learning Loops

#### Weekly Analytics Job

```python
from datetime import datetime, timedelta
import pandas as pd

def weekly_learning_job():
    """Run every Friday to analyze feedback and update policies."""
    
    # Collect feedback from past week
    one_week_ago = datetime.now() - timedelta(days=7)
    feedback = get_feedback_since(one_week_ago)
    
    df = pd.DataFrame(feedback)
    
    # Calculate metrics
    metrics = {
        "total_decisions": len(df),
        "escalation_rate": (df["decision"] == "ESCALATE").sum() / len(df),
        "false_positive_rate": calculate_fp_rate(df),
        "false_negative_rate": calculate_fn_rate(df),
        "avg_confidence": df["confidence"].mean(),
        "policy_gaps": identify_policy_gaps(df)
    }
    
    # Log for review
    log_analytics(metrics)
    
    # Generate recommendations
    recommendations = generate_policy_recommendations(metrics)
    
    # Notify team
    notify_team_weekly_report(metrics, recommendations)
    
    return metrics

# Schedule with APScheduler or cron
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.add_job(weekly_learning_job, 'cron', day_of_week=4, hour=10)
scheduler.start()
```

#### Policy Update Pipeline

```python
def update_escalation_threshold(metrics):
    """Update thresholds based on metrics."""
    
    if metrics["false_positive_rate"] > 0.15:
        # Too many false positives, lower threshold (more escalations)
        new_threshold = current_threshold - 0.05
    elif metrics["false_negative_rate"] > 0.1:
        # Too many false negatives, raise threshold (fewer escalations)
        new_threshold = current_threshold + 0.05
    else:
        new_threshold = current_threshold
    
    if new_threshold != current_threshold:
        # Create version
        policy_version = create_policy_version({
            "escalation_threshold": new_threshold,
            "policy_name": "content_moderation",
            "reason": "Quarterly metrics review"
        })
        
        # Test in staging
        test_staging_deployment(policy_version)
        
        # Deploy to production
        deploy_to_production(policy_version)
```

---

## Complete Implementation Example

### Project Structure

```
content-moderation-langgraph/
├── pyproject.toml
├── requirements.txt
├── main.py
├── graph.py
├── nodes/
│   ├── __init__.py
│   ├── classifier.py
│   ├── analyzer.py
│   ├── escalator.py
│   └── feedback.py
├── tools/
│   ├── __init__.py
│   ├── policy_api.py
│   └── queue_manager.py
├── state.py
├── learning/
│   ├── __init__.py
│   ├── metrics.py
│   └── weekly_job.py
└── tests/
    ├── test_graph.py
    ├── test_nodes.py
    └── test_learning.py
```

### Main Application

```python
# main.py
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from state import ModerationState
from nodes import (
    classify_content_node,
    analyze_context_node,
    escalate_human_node,
    collect_feedback_node,
    route_decision
)

def build_graph():
    workflow = StateGraph(ModerationState)
    
    # Add nodes
    workflow.add_node("classify", classify_content_node)
    workflow.add_node("analyze", analyze_context_node)
    workflow.add_node("escalate", escalate_human_node)
    workflow.add_node("feedback", collect_feedback_node)
    
    # Add edges
    workflow.add_edge(START, "classify")
    workflow.add_conditional_edges(
        "classify",
        route_decision,
        {
            "escalate": "escalate",
            "analyze": "analyze",
            "feedback": "feedback"
        }
    )
    workflow.add_edge("analyze", "feedback")
    workflow.add_edge("escalate", "feedback")
    workflow.add_edge("feedback", END)
    
    # Compile
    checkpointer = MemorySaver()
    return workflow.compile(checkpointer=checkpointer)

async def moderate_content(content: str, user_id: str):
    """Main entry point."""
    graph = build_graph()
    
    initial_state = ModerationState(
        content=content,
        user_id=user_id,
        policy_version="v1.2",
        escalation_threshold=0.7,
        classification=None,
        confidence=0.0,
        context_analysis={},
        decision=None,
        reason=None,
        policy_applied=None,
        human_review=None,
        review_feedback=None,
        attempt_count=0,
        messages=[]
    )
    
    config = {"configurable": {"thread_id": f"{user_id}_session"}}
    return await graph.ainvoke(initial_state, config)

if __name__ == "__main__":
    import asyncio
    result = asyncio.run(moderate_content(
        "This is test content",
        "user_123"
    ))
    print(result)
```

---

## Configuration Checklist

- [ ] Python 3.11+ installed
- [ ] LangGraph installed (`pip install langgraph`)
- [ ] LangChain ecosystem set up
- [ ] LLM API keys configured (Claude, OpenAI, etc.)
- [ ] State TypedDict defined
- [ ] All nodes implemented and tested
- [ ] Graph definition complete
- [ ] Routing logic validated
- [ ] Checkpointer configured
- [ ] Human-in-the-loop integrated
- [ ] Learning job scheduled
- [ ] Metrics collection enabled
- [ ] Error handling implemented
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Documentation complete
- [ ] Deployment pipeline ready

---

## Comparison: arche vs LangGraph

| Aspect | arche MAO | LangGraph |
|--------|----------|----------|
| **Definition** | Markdown directives | Python classes + StateGraph |
| **Agents** | Agent archetypes | Graph nodes |
| **Coordination** | Directive specifications | Edges + routing functions |
| **State** | Implicit | Explicit TypedDict |
| **Execution** | Abstract (vendor-dependent) | Python functions |
| **Tools** | Tool definitions | LangChain tool bindings |
| **Human Handoff** | Escalation Manager | Breakpoints + state updates |
| **Learning** | Quarterly cycles | Custom Job scheduling |
| **Persistence** | N/A | Built-in checkpointing |
| **Streaming** | N/A | Supported natively |
| **Testing** | Documentation review | Unit + integration tests |

---

## Testing Strategy

### Unit Tests

```python
# tests/test_nodes.py
import pytest
from nodes import classify_content_node
from state import ModerationState

@pytest.mark.asyncio
async def test_classify_safe_content():
    state = ModerationState(
        content="Hello, how are you?",
        user_id="test_user",
        policy_version="v1.0",
        escalation_threshold=0.7,
        classification=None,
        confidence=0.0,
        context_analysis={},
        decision=None,
        reason=None,
        policy_applied=None,
        human_review=None,
        review_feedback=None,
        attempt_count=0,
        messages=[]
    )
    
    result = await classify_content_node(state)
    
    assert result["classification"] == "SAFE"
    assert result["confidence"] < 0.3
```

### Integration Tests

```python
# tests/test_graph.py
@pytest.mark.asyncio
async def test_full_moderation_flow():
    graph = build_graph()
    
    initial_state = ModerationState(
        content="Violent content...",
        # ... other fields
    )
    
    config = {"configurable": {"thread_id": "test_123"}}
    result = await graph.ainvoke(initial_state, config)
    
    assert result["decision"] in ["APPROVE", "REJECT", "ESCALATE"]
    assert result["reason"] is not None
```

---

## Deployment Considerations

### Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python main.py

# Run tests
pytest tests/
```

### Production

```bash
# Docker deployment
docker build -t content-moderation .
docker run -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY content-moderation

# Or as a service (FastAPI wrapper)
pip install fastapi
# (wrap graph in FastAPI endpoints)

# Kubernetes deployment
kubectl apply -f k8s/deployment.yaml
```

### Monitoring

```python
# Add logging and metrics
import logging
from prometheus_client import Counter, Histogram

decision_counter = Counter(
    'moderation_decisions_total',
    'Total moderation decisions',
    ['decision']
)

confidence_histogram = Histogram(
    'moderation_confidence',
    'Confidence scores'
)

def monitoring_wrapper(graph):
    def invoke_with_metrics(state, config):
        result = graph.invoke(state, config)
        decision_counter.labels(result["decision"]).inc()
        confidence_histogram.observe(result["confidence"])
        return result
    return invoke_with_metrics
```

---

## Troubleshooting

### Graph Not Routing Correctly

**Problem:** Router function not being called or returning wrong node

**Solution:**
```python
# Debug routing
def debug_route_decision(state):
    print(f"State: {state}")
    result = route_decision(state)
    print(f"Route result: {result}")
    return result

workflow.add_conditional_edges(
    "classify",
    debug_route_decision,  # Use debug version
    {...}
)
```

### State Not Persisting

**Problem:** Checkpointer not saving state between invocations

**Solution:**
```python
# Verify checkpointer is set up
checkpointer = MemorySaver()
graph = workflow.compile(checkpointer=checkpointer)

# Verify config includes thread_id
config = {"configurable": {"thread_id": "some_id"}}

# Retrieve state
state = graph.get_state(config)
print(state)  # Should show saved state
```

### Human-in-Loop Not Working

**Problem:** Graph not pausing for human input

**Solution:**
```python
# Ensure node is marked for interruption
# When interrupt happens, catch and handle
try:
    result = graph.invoke(state, config)
except GraphInterrupt:
    # Node paused for human input
    # Get current state, wait for user input
    current_state = graph.get_state(config)
    # Let user update state
    updated_state = await get_human_decision(current_state)
    # Resume
    result = graph.invoke(updated_state, config)
```

---

## Related Documentation

- [VENDOR_TRANSLATION_SPECIFICATION.md](../VENDOR_TRANSLATION_SPECIFICATION.md) — Architecture specification
- [VENDOR_INTEGRATION_GUIDE.md](../VENDOR_INTEGRATION_GUIDE.md) — Step-by-step integration
- [VENDOR_SELECTION_DECISION_TREE.md](../VENDOR_SELECTION_DECISION_TREE.md) — When to use LangGraph
- [../../modes/3-layer/](../../modes/3-layer/) — 3-Layer mode implementation
- [../../blueprints/BP-0004.md](../../blueprints/BP-0004.md) — Content Moderation blueprint

---

## Additional Resources

**LangGraph Documentation:**
- [LangGraph Core Concepts](https://langchain-ai.github.io/langgraph/concepts/)
- [Graphs, Nodes, and Edges](https://langchain-ai.github.io/langgraph/concepts/low_level_vs_high_level_interface/)
- [State and Memory](https://langchain-ai.github.io/langgraph/concepts/persistence/)
- [Human-in-the-Loop](https://langchain-ai.github.io/langgraph/how-tos/human-in-the-loop/)
- [Streaming](https://langchain-ai.github.io/langgraph/concepts/streaming/)

**arche Resources:**
- [CHOOSE_YOUR_PATH.md](../../docs/getting-started/CHOOSE_YOUR_PATH.md) — Learning path guidance
- [AGENT_ARCHETYPES.md](../../docs/frameworks/AGENT_ARCHETYPES.md) — Agent patterns
- [MODE_COMPATIBILITY.md](../../docs/frameworks/MODE_COMPATIBILITY.md) — Mode combinations

---

**Status:** Reference Documentation  
**Last Updated:** January 5, 2026  
**Maintainer:** Community
