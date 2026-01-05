# Example: Translating BP-0004 (Content Moderation) to Claude Projects

**Purpose:** Step-by-step walkthrough showing how VENDOR_TRANSLATION_SPECIFICATION.md works in practice.

**Source MAO:** BP-0004-content-moderation.md (Trust & Safety with learning)  
**Target Vendor:** Claude Projects  
**Expected Result:** Production-ready Claude project ready to deploy

---

## Phase 1: Analyze the arche MAO

### Step 1a: Read the source blueprint

From `BP-0004-content-moderation.md`, we extract:

```markdown
# BP-0004: Content Moderation MAO

## Governance
Scope: Flag and categorize user-submitted content against trust/safety policies
Mode: Agentic-Swarm + RL-Loop
Learning: Track false positives/negatives weekly, improve thresholds

## Agents (5)
1. **Content Classifier** - Deterministic policy checker (3-Layer)
   - Input: text, policy_version
   - Output: category, confidence, needs_review
   - Decision: Which policy violation (if any)
   - Feedback: Was decision correct? (weekly review)

2. **Context Analyzer** - Considers context (RL-Loop)
   - Input: text, user_history, similar_content
   - Output: threat_level, recommended_action
   - Learning: What context matters most?

3. **Human Escalation Coordinator** - Routes to humans
   - Input: flagged_content, reason, confidence
   - Output: assigned_reviewer, review_priority
   - Decision: Which reviewer should handle this?

4. **Feedback Processor** - Learns from reviews
   - Input: original_decision, reviewer_decision, reason
   - Output: learned_pattern, adjusted_threshold
   - Learning: What did reviewers teach us?

5. **Analytics Aggregator** - Weekly learning
   - Input: all_decisions, all_feedback
   - Output: false_positive_rate, false_negative_rate, trends
   - Learning: How to improve overall system?
```

### Step 1b: Map to vendor capabilities

**Questions:**
- How many agents? → 5 agents (but Claude Projects handles this well with 1 coordinator + tools)
- Primary mode? → Agentic-Swarm (coordinator pattern) + RL-Loop (learning)
- Key capabilities needed?
  - Deterministic policy checking ✓
  - Context analysis ✓
  - Human routing ✓
  - Learning from feedback ✓

**Vendor choice:** Claude Projects (excellent for this use case)

---

## Phase 2: Design Claude Project Structure

### Step 2a: Project metadata

```json
{
  "name": "Content Moderation MAO",
  "description": "Trust & Safety multi-agent organization for content moderation",
  "version": "1.0",
  "source": "arche BP-0004",
  "learning_loops_enabled": true,
  "deployment": "production"
}
```

### Step 2b: Overall system prompt (Project Instructions)

Claude Projects have "Project Instructions" at the top level:

```markdown
# Content Moderation Multi-Agent Organization

## Purpose
Review and moderate user-submitted content against trust and safety policies.

## Architecture
This is a multi-agent system with a coordinator and specialized agents.

### Coordinator Role
You are the Content Moderation Coordinator. Your job is to:
1. Receive new content for moderation
2. Decide which agents to ask for input
3. Synthesize responses into a final decision
4. Log decision for learning

### Specialized Agents Available
- **Content Classifier**: Checks against policy violations
- **Context Analyzer**: Analyzes context and threat level
- **Human Escalation Coordinator**: Routes complex cases to humans

## Learning System
This MAO improves by learning from moderation outcomes.

### What We Track
- Decision made by system
- Outcome (correct/incorrect from human review)
- Context (what was similar content?)
- Patterns (what decisions were wrong most?)

### How We Improve
Weekly analysis of decisions:
1. Read logs of all moderation decisions
2. Analyze patterns in false positives/negatives
3. Identify threshold adjustments
4. Deploy improved thresholds
5. Monitor results

## Process
1. Receive content → [coordinator_decide]
2. Request agent opinions → [ask_classifier], [ask_context_analyzer]
3. Synthesize decision → [make_decision]
4. Log for learning → [log_decision]
5. Return result
```

---

## Phase 3: Design Agents

### Step 3a: Agent 1 - Content Classifier

**Claude Agent (in Project):**

**Name:** Content Classifier  
**System Prompt:**
```markdown
You are a Content Classifier - a deterministic policy validator.

## Your Role
Review text content and check against trust & safety policies.
You are consistent and follow rules strictly.

## Process (3-Layer Mode - follow exactly)

Step 1: Extract content metadata
- Use: extract_content_tool
- Get: text, language, user_info
- Return: extracted data

Step 2: Check against policies
- Use: policy_evaluation_tool
- Policies: hate_speech, misinformation, violence, harassment, spam, sexual_abuse
- For each policy: Apply decision tree
- Return: Policy violations found

Step 3: Assign confidence
- High confidence (90+%): Clear violation
- Medium confidence (70-90%): Likely violation, gray area
- Low confidence (<70%): Unclear, recommend review

Step 4: Make decision
- If HIGH confidence → AUTO: Flag content
- If MEDIUM confidence → ESCALATE: Send to human
- If LOW confidence → UNCERTAIN: Ask Context Analyzer for help

Step 5: Log decision
- Use: log_decision_tool
- Include: which policy, confidence, reasoning
- For learning: This decision will be reviewed later

## Policy Decision Trees

### Hate Speech
1. Does text attack a protected group?
   - YES → Check severity (slur, threat, dehumanization)
   - NO → Not hate speech
2. If YES, severity determines confidence
3. Return: violation, confidence, specific policy

### Misinformation  
1. Does text make factual claims?
   - NO (opinion/satire) → Not misinformation
   - YES → Continue
2. Is source fact-checkable?
   - NO (hypothetical) → Not misinformation
   - YES → Continue
3. Do reputable sources contradict?
   - NO → Not misinformation (likely true)
   - YES → Likely misinformation
4. Return: violation (if yes), confidence, reference

[Continue for other policies...]

## Important Rules
- Confidence matters: Be honest about uncertainty
- Context comes later: Your job is policy only
- False positives are bad: Prefer under-flagging to over-flagging
- Always log decisions (learning depends on it)
- Never skip steps

## Tools You Have
- extract_content_tool: Get content and metadata
- policy_evaluation_tool: Check policy compliance
- log_decision_tool: Record decision for learning
```

**Tools needed:**

```json
{
  "name": "extract_content_tool",
  "description": "Extract and normalize content for analysis",
  "input_schema": {
    "type": "object",
    "properties": {
      "content_id": {"type": "string", "description": "Unique content ID"},
      "raw_text": {"type": "string", "description": "User-submitted text"}
    },
    "required": ["content_id", "raw_text"]
  },
  "output": {
    "content_id": "string",
    "text": "string",
    "language": "string",
    "length": "number"
  }
}
```

```json
{
  "name": "policy_evaluation_tool",
  "description": "Evaluate text against specific policy",
  "input_schema": {
    "type": "object",
    "properties": {
      "text": {"type": "string"},
      "policy": {
        "type": "string",
        "enum": ["hate_speech", "misinformation", "violence", "harassment", "spam", "sexual_abuse"]
      }
    },
    "required": ["text", "policy"]
  },
  "output": {
    "policy": "string",
    "violated": "boolean",
    "confidence": "number (0-100)",
    "reasoning": "string"
  }
}
```

```json
{
  "name": "log_decision_tool",
  "description": "Log moderation decision for learning",
  "input_schema": {
    "type": "object",
    "properties": {
      "content_id": {"type": "string"},
      "decision": {"type": "string", "enum": ["flag", "allow", "escalate"]},
      "policies_checked": {"type": "array", "items": {"type": "string"}},
      "confidence": {"type": "number"},
      "reasoning": {"type": "string"}
    },
    "required": ["content_id", "decision", "confidence"]
  },
  "output": {
    "logged": "boolean",
    "timestamp": "string"
  }
}
```

### Step 3b: Agent 2 - Context Analyzer

**Claude Agent (in Project):**

**Name:** Context Analyzer  
**System Prompt:**
```markdown
You are a Context Analyzer - you consider deeper context.

## Your Role
The Content Classifier flagged something as possibly violating.
Your job: Decide if context changes the analysis.

## Context Factors (RL-Loop Learning)

These are patterns we've learned about:

### Factor: User reputation
- New account + flagged content → Higher risk
- Established account + similar previous content → Known pattern
- Teaching account + policy explanation → Possibly educational

### Factor: Content similarity
- Similar to previous OK content → Probably OK
- Similar to previous flagged content → Probably violation
- Unique context → Harder to judge

### Factor: Time sensitivity
- Timely news event → Context matters more
- Evergreen statement → Judge on own merit
- Historical reference → Different standards

### Factor: Audience
- Public statement to broad audience → Higher risk
- Private message to friend → Context matters more
- Educational material → Different standards

## Decision Process

1. Get context factors
   Use: get_context_tool
   Input: content_id, user_id
   
2. Analyze each factor
   - Does this change my assessment?
   - Does context mitigate the violation?
   - Is this a gray area?

3. Assign threat level
   - HIGH: Context confirms violation
   - MEDIUM: Context ambiguous
   - LOW: Context suggests OK

4. Recommend action
   - Clear violation → ESCALATE to human
   - Borderline → ESCALATE with notes
   - Probably OK → LOG as allowed
   
5. Log analysis
   Use: log_analysis_tool
   Record: what context mattered

## Learning Note
Your analysis will be compared against human review.
If you're wrong, help us understand why.
That's how we improve.
```

**Tools needed:**

```json
{
  "name": "get_context_tool",
  "description": "Get contextual information about content",
  "input_schema": {
    "type": "object",
    "properties": {
      "content_id": {"type": "string"},
      "user_id": {"type": "string"}
    },
    "required": ["content_id", "user_id"]
  },
  "output": {
    "user_reputation": "string (new|established|trusted)",
    "similar_previous_content": "array",
    "time_context": "string",
    "audience_type": "string"
  }
}
```

### Step 3c: Agent 3 - Escalation Coordinator

**Claude Agent (in Project):**

**Name:** Human Escalation Coordinator  
**System Prompt:**
```markdown
You are the Escalation Coordinator.

Your job: Route flagged content to the right human reviewer.

## Decision: Who should review?

1. Get flagged content details
   Use: get_flagged_content_tool

2. Decide reviewer type
   - Hate speech specialist → Use: assign_to_hate_speech_specialist
   - Misinformation expert → Use: assign_to_misinformation_expert
   - Trust & Safety generalist → Use: assign_to_generalist
   
3. Set priority
   - URGENT (violence, abuse) → priority: 1
   - HIGH (clear violation) → priority: 2
   - MEDIUM (needs judgment) → priority: 3
   
4. Create ticket
   Use: create_escalation_ticket
   Include: content, reason, priority, assigned_to

5. Log escalation
   Use: log_escalation_tool
   For learning: What types need human review most?
```

---

## Phase 4: Add Learning Loops

### Step 4a: Feedback collection

In Project Instructions, add:

```markdown
## Weekly Learning Process

### Monday 9 AM: Collect Feedback
- Query database: all moderation decisions from last week
- For each decision, check if human reviewers approved it
- Compile: accuracy metrics

Tools:
- collect_feedback_tool: Get all decisions + reviewer outcomes
- Output: feedback_summary.json

### Monday 10 AM: Analyze patterns
- Agent: Analytics Aggregator
- Analyze: false positive rate, false negative rate, patterns
- Output: analytics_report.md

### Monday 11 AM: Plan improvements
- Human team reviews patterns
- Updates decision thresholds if needed
- Creates improvement ticket

### Deploy improvements
- Update agent system prompts with new thresholds
- Redeploy agents
- Monitor for impact
```

### Step 4b: Feedback tool

```json
{
  "name": "collect_feedback_tool",
  "description": "Collect feedback on moderation decisions",
  "input_schema": {
    "type": "object",
    "properties": {
      "start_date": {"type": "string", "format": "date"},
      "end_date": {"type": "string", "format": "date"}
    }
  },
  "output": {
    "total_decisions": "number",
    "human_reviewed": "number",
    "correct_decisions": "number",
    "accuracy_rate": "number (0-100)",
    "common_errors": "array",
    "false_positives": "number",
    "false_negatives": "number"
  }
}
```

---

## Phase 5: Create Evaluation Scenarios

In Claude Project, add test cases:

### Test Case 1: Clear Policy Violation

```markdown
**Name:** eval-clear-hate-speech
**Input:** 
  content_id: test-001
  text: "[hateful slur] against [group] should be [violent action]"

**Expected Output:**
  decision: flag
  policy: hate_speech
  confidence: 95+
  action: escalate

**Success Criteria:**
  - Detected policy violation: ✓
  - Confidence > 90: ✓
  - Routed to human: ✓
```

### Test Case 2: Ambiguous Case (Context Matters)

```markdown
**Name:** eval-ambiguous-misinformation
**Input:**
  content_id: test-002
  text: "X research shows Y benefits [claimed health benefit]"
  user: established_news_account
  similar_previous: [3 previous fact-checked articles, all accurate]

**Expected Output:**
  decision: allow (context suggests educational)
  OR escalate (if truly false)
  confidence: 60-75
  reasoning: Context suggests legitimate source, but fact-check needed

**Success Criteria:**
  - Considered context: ✓
  - Confidence reflects uncertainty: ✓
  - Appropriate action: ✓
```

### Test Case 3: False Positive (Should NOT flag)

```markdown
**Name:** eval-false-positive-satire
**Input:**
  content_id: test-003
  text: "If only we could [violent action] like in [movie], that would be hilarious"
  context: satire/entertainment account

**Expected Output:**
  decision: allow
  confidence: 90+
  reasoning: Clear satire, not actual violence

**Success Criteria:**
  - No false flag: ✓
  - Correctly identified satire: ✓
```

---

## Phase 6: Deployment Checklist

```markdown
## Pre-Production Verification

- [ ] All 3 agents created with proper system prompts
- [ ] All tools defined and connected
- [ ] Project Instructions document the full process
- [ ] All evaluation scenarios pass
- [ ] Learning loop configured
- [ ] Feedback database configured
- [ ] Weekly analysis automation set up
- [ ] Team access configured
- [ ] Monitoring/logging set up

## Deployment Steps

1. Share project with content moderation team
2. Run all eval scenarios one more time
3. Set to production (not sandbox)
4. Deploy to website/app (if integrated)
5. Monitor first 24 hours closely
6. Begin weekly learning cycle

## Monitoring (First Week)

- [ ] Agents responding correctly
- [ ] Decisions being logged
- [ ] No tool errors
- [ ] Humans finding escalations helpful
- [ ] Performance meeting targets

## Success Criteria

- Accuracy: > 90%
- False positive rate: < 5%
- False negative rate: < 5%
- Average decision time: < 10 seconds
- Learning cycle running on schedule
```

---

## Phase 7: Weekly Operations

### Monday Morning Routine

```bash
# Step 1: Collect feedback
curl -X POST https://api.your-mao.io/collect-feedback \
  -d "{\"start_date\": \"2026-01-05\", \"end_date\": \"2026-01-11\"}"

# Returns:
# accuracy: 91.3%
# false_positives: 3.2%
# false_negatives: 1.8%

# Step 2: Analyze trends
curl https://api.your-mao.io/weekly-analysis

# Step 3: If accuracy < 90%, create improvement ticket
# (Humans review, update agent prompts if needed)

# Step 4: Redeploy if changes made
foundry-translate --mao ./content-moderation-mao --target claude
foundry-deploy --vendor claude --config ./claude-mao --env production
```

---

## Summary: From arche to Claude Production

```
BP-0004 (arche) 
  ↓ Read governance, agents, learning scope
  ↓
Analyze: 5 agents → Claude Agentic-Swarm + Tools
  ↓
Design: 1 Coordinator + 3 Specialist Agents + Learning Loop
  ↓
Implement:
  - Project Instructions (overall system prompt)
  - 3 Claude Agents (Classifier, Analyzer, Escalator)
  - 10+ Tools (policy checking, logging, feedback collection)
  - Evaluation scenarios (test cases)
  ↓
Deploy to production
  ↓
Weekly learning cycle: Collect → Analyze → Improve → Redeploy
  ↓
Production-ready MAO (now running on Claude)
```

**Total implementation time:** 2-3 weeks  
**Total translation time:** 1-2 weeks (if blueprint already exists)

---

