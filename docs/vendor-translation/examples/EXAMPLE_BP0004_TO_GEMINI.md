# Example: Translating BP-0004 (Content Moderation) to Google Gemini

**Purpose:** Translate arche Multi-Agent Organizations to Google Gemini with Agents API for multimodal content moderation at scale.

---

## Overview

### What is Google Gemini with Agents API?

Google Gemini is a frontier AI model available through the Gemini API. The Agents API enables:
- Multimodal reasoning (text, images, audio, video)
- Tool/function calling with Google Cloud integration
- Agentic loops with built-in state management
- Low-latency inference
- Grounding with Google Search
- Structured output support

### Why Translate to Gemini?

**Best for:**
- Multimodal content moderation (images, video, audio)
- Fast inference and low latency
- Google Cloud integration
- Content analysis with visual understanding
- Large-scale deployments
- Real-time moderation pipelines

**Strengths:**
- ✅ Best-in-class multimodal capabilities
- ✅ Fast inference (low latency)
- ✅ Deep Google Cloud integration
- ✅ Built-in grounding with Google Search
- ✅ Structured output support
- ✅ Excellent vision/image analysis
- ✅ Cost-effective at scale

**Limitations:**
- ⚠️ Requires Google Cloud Platform account
- ⚠️ Different API patterns than text-only models
- ⚠️ Multimodal models can be more complex to debug
- ⚠️ Regional availability considerations

---

## Architecture Mapping

### arche Concepts → Gemini with Agents API

| arche Concept | Gemini Implementation |
|---------------|----------------------|
| **Agent** | Tool-enabled Gemini instance with system prompt |
| **Directive** | System instructions + tools definitions |
| **Orchestrator** | Root agent with routing tools |
| **Executor** | Specialized agents with Cloud tools |
| **Coordination** | Tool calls triggering other agents |
| **Multimodal Input** | Images, video, audio as input files |

### arche Modes → Gemini

| arche Mode | Gemini Pattern |
|-----------|--------------|
| **3-Layer** | Tool-based layer separation with structured outputs |
| **Agentic-Swarm** | Sub-agent tools with root agent coordination |
| **Event-Driven** | Webhook triggers → Agent processing → Cloud tasks |
| **RL-Loop** | Cloud Storage feedback → Analytics agent → Policy updates |

### Agent Archetypes → Gemini Tools

| arche Agent | Gemini Tool Pattern |
|------------|-------------------|
| **Executor** | Tool with Cloud API calls (BigQuery, Firestore, etc.) |
| **Learner** | Analytics tool querying feedback data |
| **Orchestrator** | Router tool selecting sub-agent |
| **Monitor** | Metrics tool from Cloud Monitoring |
| **Validator** | Validation tool with structured output |

---

## Translation Process

### Phase 1: Plan Your Gemini Implementation

#### Step 1: Design Multimodal Input Handling

**arche MAO (BP-0004):**
```
Content Types:
- Text (primary)
- Images (secondary)
- Video (future)

Moderation Flow:
1. Classify content
2. Analyze visual elements
3. Escalate if needed
4. Track feedback
```

**Gemini Architecture:**
```
Input Processing:
- Text → Direct model input
- Images → Upload to Cloud Storage → URI reference
- Video → Same as images (if using video models)

Model: Gemini 2.0 Flash (multimodal)
Agents:
- Classifier: Text + image analysis
- Analyzer: Context and similarity
- Escalator: Human routing
- Feedback: Learning loop
```

#### Step 2: Define Tools for Cloud Integration

**Required Tools:**
```
Classifier:
  - analyze_visual_content()
  - classify_text_content()
  - check_policy_violations()

Analyzer:
  - query_moderation_history()
  - search_similar_content()
  - analyze_user_patterns()

Escalator:
  - queue_for_human_review()
  - notify_via_pubsub()

Feedback:
  - store_in_firestore()
  - update_analytics()
  - trigger_retraining()
```

#### Step 3: Set Up Google Cloud Resources

```yaml
Resources Needed:
- Cloud Storage bucket (for images/video)
- Firestore (feedback storage)
- BigQuery (analytics/learning)
- Cloud Tasks (scheduling)
- Cloud Pub/Sub (notifications)
- Cloud Monitoring (metrics)
```

---

### Phase 2: Implement Gemini Agents

#### Agent 1: Classifier Agent (Multimodal)

**arche Directive:**
```markdown
# Directive: Classify Content

## Input
- content: string (text)
- images: list (file paths or URIs)
- video: optional (file path or URI)
- policy_version: string

## Processing
1. Analyze text content
2. Analyze visual elements
3. Cross-reference policy
4. Return classification

## Output
- classification: string
- confidence: float
- text_violations: list
- visual_issues: list
- reason: string
```

**Gemini Agent Implementation:**
```python
import anthropic
from google.cloud import storage
import base64
import json

def create_classifier_agent():
    """Create Gemini classifier agent with multimodal tools."""
    
    client = anthropic.Anthropic(api_key=GEMINI_API_KEY)
    
    tools = [
        {
            "name": "analyze_text_content",
            "description": "Analyze text for policy violations",
            "input_schema": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"},
                    "policy_version": {"type": "string"}
                },
                "required": ["text", "policy_version"]
            }
        },
        {
            "name": "analyze_visual_content",
            "description": "Analyze images for policy violations",
            "input_schema": {
                "type": "object",
                "properties": {
                    "image_url": {"type": "string"},
                    "policy_version": {"type": "string"}
                },
                "required": ["image_url", "policy_version"]
            }
        },
        {
            "name": "classify_content",
            "description": "Return final classification",
            "input_schema": {
                "type": "object",
                "properties": {
                    "text_analysis": {"type": "object"},
                    "visual_analysis": {"type": "object"}
                },
                "required": ["text_analysis"]
            }
        }
    ]
    
    system_prompt = """You are a content classifier using Gemini's multimodal capabilities.
Analyze both text and images provided. Use the tools to:
1. analyze_text_content for text violations
2. analyze_visual_content for image issues
3. classify_content to return final decision

Return a structured classification with:
{
    "classification": "SAFE|VIOLATION|UNCERTAIN",
    "confidence": 0.0-1.0,
    "text_violations": ["list"],
    "visual_issues": ["list"],
    "reason": "explanation"
}"""
    
    def process_content(content: str, images: list = None, policy_version: str = "v1.2"):
        """Process multimodal content."""
        
        messages = [
            {
                "role": "user",
                "content": f"""Classify this content under policy {policy_version}:

Text: {content}

Images: {len(images) if images else 0} provided

Analyze both text and images, then provide classification."""
            }
        ]
        
        # If images provided, add them to message
        if images:
            for img_path in images:
                # Upload to Cloud Storage and get URL
                img_url = upload_to_cloud_storage(img_path)
                messages[0]["content"] += f"\nImage URL: {img_url}"
        
        # Call Gemini with tools
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",  # Gemini access
            max_tokens=1024,
            system=system_prompt,
            tools=tools,
            messages=messages
        )
        
        return response
    
    return process_content
```

#### Agent 2: Analyzer Agent

**arche Directive:**
```markdown
# Directive: Analyze Context

## Input
- content: string
- classification: string
- user_id: string
- confidence: float

## Analysis
- Query user moderation history
- Find similar content
- Analyze patterns
- Calculate threat level

## Output
- threat_level: string
- pattern: string
- similar_cases: int
- recommendation: string
```

**Gemini Agent Implementation:**
```python
def create_analyzer_agent():
    """Create Gemini analyzer agent."""
    
    tools = [
        {
            "name": "query_moderation_history",
            "description": "Query user's moderation history from BigQuery",
            "input_schema": {
                "type": "object",
                "properties": {
                    "user_id": {"type": "string"},
                    "days": {"type": "integer", "default": 90}
                },
                "required": ["user_id"]
            }
        },
        {
            "name": "search_similar_content",
            "description": "Search for similar content using embeddings",
            "input_schema": {
                "type": "object",
                "properties": {
                    "content": {"type": "string"},
                    "limit": {"type": "integer", "default": 5}
                },
                "required": ["content"]
            }
        },
        {
            "name": "analyze_patterns",
            "description": "Analyze user behavior patterns",
            "input_schema": {
                "type": "object",
                "properties": {
                    "user_id": {"type": "string"},
                    "metric": {"type": "string"}
                },
                "required": ["user_id"]
            }
        }
    ]
    
    system_prompt = """You are a context analyzer for content moderation.
Use the tools to understand:
1. User's history with similar content
2. Similar cases in the system
3. Behavioral patterns

Return analysis:
{
    "threat_level": "LOW|MEDIUM|HIGH",
    "pattern": "description of pattern",
    "similar_cases": count,
    "recommendation": "action to take"
}"""
    
    def process_analysis(content: str, classification: str, user_id: str):
        """Analyze content context."""
        
        messages = [
            {
                "role": "user",
                "content": f"""Analyze context for this content:

Classification: {classification}
User ID: {user_id}
Content: {content}

Provide detailed context analysis including history, similar cases, and patterns."""
            }
        ]
        
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            system=system_prompt,
            tools=tools,
            messages=messages
        )
        
        return response
    
    return process_analysis
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
- policy_version: string

## Escalation
- Create escalation record in Firestore
- Publish notification via Pub/Sub
- Queue in Cloud Tasks
- Notify moderation team

## Output
- escalation_id: string
- status: string
- estimated_review_time: int
```

**Gemini Agent Implementation:**
```python
def create_escalation_agent():
    """Create Gemini escalation agent."""
    
    from google.cloud import firestore, pubsub_v1, tasks_v2
    
    db = firestore.Client()
    publisher = pubsub_v1.PublisherClient()
    task_client = tasks_v2.CloudTasksClient()
    
    tools = [
        {
            "name": "create_escalation_record",
            "description": "Create escalation record in Firestore",
            "input_schema": {
                "type": "object",
                "properties": {
                    "content": {"type": "string"},
                    "classification": {"type": "string"},
                    "priority": {"type": "string"}
                },
                "required": ["content", "classification", "priority"]
            }
        },
        {
            "name": "publish_notification",
            "description": "Publish escalation notification via Pub/Sub",
            "input_schema": {
                "type": "object",
                "properties": {
                    "escalation_id": {"type": "string"},
                    "priority": {"type": "string"}
                },
                "required": ["escalation_id", "priority"]
            }
        },
        {
            "name": "queue_for_review",
            "description": "Queue in Cloud Tasks for human review",
            "input_schema": {
                "type": "object",
                "properties": {
                    "escalation_id": {"type": "string"}
                },
                "required": ["escalation_id"]
            }
        }
    ]
    
    system_prompt = """You are responsible for escalating uncertain content to humans.
Use the tools to:
1. Create escalation record in Firestore
2. Publish notification to the team
3. Queue for human review

Return escalation details:
{
    "escalation_id": "unique id",
    "status": "queued",
    "priority": "high|normal|low",
    "estimated_review_time_minutes": 5-30
}"""
    
    def process_escalation(content: str, classification: str, confidence: float, threat_level: str):
        """Escalate to human review."""
        
        priority = "high" if threat_level == "HIGH" else "normal"
        
        messages = [
            {
                "role": "user",
                "content": f"""Escalate this content:

Classification: {classification}
Confidence: {confidence}
Threat Level: {threat_level}
Priority: {priority}

Create escalation record, notify team, and queue for review."""
            }
        ]
        
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=512,
            system=system_prompt,
            tools=tools,
            messages=messages
        )
        
        return response
    
    return process_escalation
```

#### Agent 4: Feedback Agent

**arche Directive:**
```markdown
# Directive: Track Feedback

## Input
- original_decision: string
- content: string
- classification: string
- human_decision: optional string
- policy_version: string

## Processing
1. Store in Firestore
2. Update BigQuery analytics
3. Calculate metrics
4. Trigger retraining if needed

## Output
- feedback_id: string
- metrics_updated: boolean
- retraining_triggered: boolean
```

**Gemini Agent Implementation:**
```python
def create_feedback_agent():
    """Create Gemini feedback agent."""
    
    from google.cloud import firestore, bigquery
    
    db = firestore.Client()
    bq = bigquery.Client()
    
    tools = [
        {
            "name": "store_feedback",
            "description": "Store feedback in Firestore",
            "input_schema": {
                "type": "object",
                "properties": {
                    "decision": {"type": "string"},
                    "content": {"type": "string"},
                    "human_override": {"type": "string"}
                },
                "required": ["decision", "content"]
            }
        },
        {
            "name": "update_analytics",
            "description": "Update BigQuery analytics table",
            "input_schema": {
                "type": "object",
                "properties": {
                    "feedback_id": {"type": "string"}
                },
                "required": ["feedback_id"]
            }
        },
        {
            "name": "check_retraining_threshold",
            "description": "Check if retraining should be triggered",
            "input_schema": {
                "type": "object",
                "properties": {
                    "metric_type": {"type": "string"}
                }
            }
        }
    ]
    
    system_prompt = """You are responsible for collecting feedback and updating metrics.
Use the tools to:
1. Store feedback in Firestore
2. Update BigQuery analytics
3. Check if retraining is needed

Return feedback status:
{
    "feedback_id": "unique id",
    "stored": true,
    "metrics_updated": true,
    "retraining_triggered": false
}"""
    
    def process_feedback(decision: str, content: str, human_override: str = None):
        """Process feedback and update metrics."""
        
        messages = [
            {
                "role": "user",
                "content": f"""Process feedback:

Decision: {decision}
Human Override: {human_override or 'none'}
Content Hash: {hash(content)}

Store feedback and update metrics."""
            }
        ]
        
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=512,
            system=system_prompt,
            tools=tools,
            messages=messages
        )
        
        return response
    
    return process_feedback
```

---

### Phase 3: Orchestrate with Gemini API

#### Complete Orchestration

```python
from google.cloud import firestore
import json

class ContentModerationSystem:
    """Complete moderation system using Gemini."""
    
    def __init__(self):
        self.classifier = create_classifier_agent()
        self.analyzer = create_analyzer_agent()
        self.escalator = create_escalation_agent()
        self.feedback = create_feedback_agent()
        self.db = firestore.Client()
    
    async def moderate(self, content: str, images: list = None, user_id: str = None, 
                       policy_version: str = "v1.2") -> dict:
        """Main moderation flow."""
        
        # Step 1: Classify
        classification = await self.classifier(
            content=content,
            images=images,
            policy_version=policy_version
        )
        
        class_result = parse_response(classification)
        
        # Step 2: Decide routing
        if class_result["confidence"] < 0.7:  # ESCALATION_THRESHOLD
            # Route to escalation
            escalation = await self.escalator(
                content=content,
                classification=class_result["classification"],
                confidence=class_result["confidence"],
                threat_level="MEDIUM"
            )
            result = parse_response(escalation)
        else:
            # Route to analyzer for context
            analysis = await self.analyzer(
                content=content,
                classification=class_result["classification"],
                user_id=user_id or "anonymous"
            )
            result = parse_response(analysis)
        
        # Step 3: Collect feedback
        feedback = await self.feedback(
            decision=result.get("decision", class_result["classification"]),
            content=content
        )
        
        return {
            "classification": class_result,
            "analysis": result,
            "feedback_id": parse_response(feedback).get("feedback_id")
        }
```

---

### Phase 4: Set Up Learning Loops

#### Cloud Tasks for Weekly Analytics

```python
from google.cloud import tasks_v2
from google.protobuf import timestamp_pb2
import datetime

def schedule_weekly_analytics():
    """Schedule weekly analytics job."""
    
    client = tasks_v2.CloudTasksClient()
    project = "my-project"
    queue = "moderation-analytics"
    location = "us-central1"
    
    parent = client.queue_path(project, location, queue)
    
    task = {
        "http_request": {
            "http_method": tasks_v2.HttpMethod.POST,
            "url": "https://example.com/analytics",
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"task": "weekly_analytics"}).encode()
        }
    }
    
    # Schedule for next Friday 10 AM
    d = datetime.datetime.utcnow() + datetime.timedelta(days=5)
    timestamp = timestamp_pb2.Timestamp()
    timestamp.FromDatetime(d.replace(hour=10, minute=0, second=0, microsecond=0))
    task["schedule_time"] = timestamp
    
    response = client.create_task(request={"parent": parent, "task": task})
    return response

async def weekly_analytics_job():
    """Analyze metrics weekly."""
    
    # Query BigQuery
    query = """
    SELECT 
        COUNT(*) as total_decisions,
        COUNTIF(human_override IS NOT NULL) as human_overrides,
        AVG(confidence) as avg_confidence,
        COUNTIF(human_override != auto_decision) as errors
    FROM `project.dataset.moderation_feedback`
    WHERE DATE(timestamp) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
    """
    
    bq = bigquery.Client()
    results = bq.query(query).result()
    
    metrics = dict(results[0])
    
    # Calculate error rates
    metrics["error_rate"] = metrics["errors"] / metrics["total_decisions"]
    
    # Log for team review
    print(f"Weekly Report: {metrics}")
    
    # Publish to Pub/Sub for team notification
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path("project", "moderation-analytics")
    
    publisher.publish(
        topic_path,
        json.dumps(metrics).encode("utf-8")
    )
```

---

## Complete Implementation Example

### Project Structure

```
content-moderation-gemini/
├── main.py
├── agents.py
├── cloud_tools.py
├── config.py
├── learning.py
├── requirements.txt
└── tests/
    ├── test_agents.py
    ├── test_multimodal.py
    └── test_learning.py
```

### Main Application with FastAPI

```python
# main.py
from fastapi import FastAPI, UploadFile, File, Form
from google.cloud import storage
import asyncio

app = FastAPI()

moderation_system = ContentModerationSystem()

@app.post("/moderate")
async def moderate_content(
    content: str = Form(...),
    user_id: str = Form(None),
    files: list[UploadFile] = File(None)
):
    """Moderate content with optional images."""
    
    image_paths = []
    
    # Upload images if provided
    if files:
        storage_client = storage.Client()
        bucket = storage_client.bucket("moderation-images")
        
        for file in files:
            blob = bucket.blob(f"{user_id}/{file.filename}")
            blob.upload_from_string(await file.read())
            image_paths.append(f"gs://moderation-images/{user_id}/{file.filename}")
    
    # Run moderation
    result = await moderation_system.moderate(
        content=content,
        images=image_paths,
        user_id=user_id
    )
    
    return result

@app.get("/analytics")
async def get_analytics():
    """Get current analytics."""
    
    query = """
    SELECT 
        DATE(timestamp) as date,
        COUNT(*) as decisions,
        COUNTIF(human_override IS NOT NULL) as escalations,
        AVG(confidence) as avg_confidence
    FROM `project.dataset.moderation_feedback`
    WHERE DATE(timestamp) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
    GROUP BY date
    ORDER BY date DESC
    """
    
    bq = bigquery.Client()
    results = bq.query(query).result()
    
    return [dict(row) for row in results]
```

---

## Configuration Checklist

- [ ] Google Cloud Project created
- [ ] Gemini API enabled
- [ ] Service account credentials configured
- [ ] Cloud Storage bucket created
- [ ] Firestore database initialized
- [ ] BigQuery dataset created
- [ ] Pub/Sub topics created
- [ ] Cloud Tasks queue set up
- [ ] Cloud Monitoring dashboard created
- [ ] All agents implemented
- [ ] Cloud tools integrated
- [ ] Multimodal input handling tested
- [ ] Learning loop scheduled
- [ ] Error handling implemented
- [ ] Unit tests passing
- [ ] Integration tests passing
- [ ] FastAPI application deployed
- [ ] Documentation complete

---

## Comparison: arche vs Gemini

| Aspect | arche MAO | Google Gemini |
|--------|-----------|--------------|
| **Definition** | Markdown directives | Python agents + tools |
| **Agents** | Agent archetypes | Tool-enabled Gemini instances |
| **Multimodal** | Text-primary (future) | Native (text, image, video, audio) |
| **Execution** | Abstract | API calls to Google Cloud |
| **Tools** | Tool specifications | Google Cloud service integrations |
| **Coordination** | Coordination patterns | Tool-based routing |
| **Scalability** | Deployment-dependent | Auto-scaling via Google Cloud |
| **Learning** | Quarterly feedback | Real-time with BigQuery |
| **Latency** | Depends on vendor | Low (optimized) |
| **Cost** | Varies | Pay-per-use (efficient at scale) |

---

## Advantages of Gemini for arche

1. **Multimodal** — Handle images, video, audio natively
2. **Fast** — Low-latency inference
3. **Scalable** — Google Cloud infrastructure
4. **Integrated** — Deep GCP ecosystem integration
5. **Learning** — Real-time feedback with BigQuery
6. **Cost-effective** — Efficient pricing at scale

---

## When Gemini Might Not Be Ideal

- Text-only, simple logic → Use Claude or Swarm
- Deterministic routing → Use Swarm
- Custom workflows → Use LangGraph
- Enterprise Teams → Use Copilot Studio
- Low-code authoring → Use Copilot Studio

---

## Troubleshooting

### Images Not Processing

**Problem:** Multimodal input failing

**Solution:**
```python
# Ensure images are uploaded to Cloud Storage first
def upload_image_to_gcs(image_path: str) -> str:
    """Upload image and return GCS URI."""
    
    storage_client = storage.Client()
    bucket = storage_client.bucket("moderation-images")
    blob = bucket.blob(f"images/{Path(image_path).name}")
    blob.upload_from_filename(image_path)
    
    return f"gs://moderation-images/images/{blob.name}"

# Use GCS URI in Gemini call
image_url = upload_image_to_gcs("path/to/image.jpg")
```

### BigQuery Queries Slow

**Problem:** Analytics queries timing out

**Solution:**
```python
# Create materialized views for common queries
create_materialized_view_query = """
CREATE MATERIALIZED VIEW `project.dataset.daily_metrics` AS
SELECT 
    DATE(timestamp) as date,
    COUNT(*) as total_decisions,
    COUNTIF(human_override IS NOT NULL) as escalations,
    AVG(confidence) as avg_confidence
FROM `project.dataset.moderation_feedback`
GROUP BY date
"""

# Query materialized view (instant)
query = "SELECT * FROM `project.dataset.daily_metrics` WHERE date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)"
```

### Pub/Sub Messages Not Delivering

**Problem:** Notifications not reaching team

**Solution:**
```python
# Verify subscription exists and has handlers
def create_subscription(topic_name: str, subscription_name: str):
    """Create Pub/Sub subscription."""
    
    publisher = pubsub_v1.PublisherClient()
    subscriber = pubsub_v1.SubscriberClient()
    
    topic_path = publisher.topic_path("project", topic_name)
    subscription_path = subscriber.subscription_path("project", subscription_name)
    
    subscription = subscriber.create_subscription(
        request={"name": subscription_path, "topic": topic_path}
    )
    
    return subscription
```

---

## Related Documentation

- [VENDOR_TRANSLATION_SPECIFICATION.md](../VENDOR_TRANSLATION_SPECIFICATION.md) — Architecture specification
- [VENDOR_INTEGRATION_GUIDE.md](../VENDOR_INTEGRATION_GUIDE.md) — Step-by-step integration
- [VENDOR_SELECTION_DECISION_TREE.md](../VENDOR_SELECTION_DECISION_TREE.md) — When to use Gemini
- [../../modes/3-layer/](../../modes/3-layer/) — 3-Layer mode implementation
- [../../blueprints/BP-0004.md](../../blueprints/BP-0004.md) — Content Moderation blueprint

---

## Additional Resources

**Google Gemini Documentation:**
- [Gemini API Overview](https://ai.google.dev/)
- [Multimodal Capabilities](https://ai.google.dev/tutorials/python_quickstart)
- [Function Calling](https://ai.google.dev/docs/function_calling)
- [Agents API](https://ai.google.dev/docs/agents)

**Google Cloud Resources:**
- [Cloud Storage for Media](https://cloud.google.com/storage/docs)
- [Firestore Documentation](https://firebase.google.com/docs/firestore)
- [BigQuery Guide](https://cloud.google.com/bigquery/docs)
- [Cloud Tasks](https://cloud.google.com/tasks/docs)
- [Pub/Sub Messaging](https://cloud.google.com/pubsub/docs)

**arche Resources:**
- [CHOOSE_YOUR_PATH.md](../../docs/getting-started/CHOOSE_YOUR_PATH.md) — Learning path guidance
- [AGENT_ARCHETYPES.md](../../docs/frameworks/AGENT_ARCHETYPES.md) — Agent patterns
- [MODE_COMPATIBILITY.md](../../docs/frameworks/MODE_COMPATIBILITY.md) — Mode combinations

---

**Status:** Reference Documentation  
**Last Updated:** January 5, 2026  
**Maintainer:** Community
