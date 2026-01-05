# Mode Migration Guide

**Purpose:** Help agents evolve from one mode to another as requirements change.

---

## Overview

Mode migration happens when an agent's role fundamentally changes:
- ✅ **When to migrate:** Requirements shift, learning becomes critical, coordination needed
- ❌ **When NOT to migrate:** Fine-tuning performance within same mode

This guide provides step-by-step migration paths for common transitions.

---

## Migration Patterns

### Pattern 1: 3-Layer → RL-Loop (Add Learning)

**Trigger:** Optimal strategy is no longer fixed; learning from outcomes improves results

**Example:** 
- **Before:** Content router with hardcoded rules (3-Layer)
- **After:** Content router that learns which categories work best (RL-Loop)

**Steps:**

#### Phase 1: Analysis (1 week)
1. **Identify decision point:** Where does the agent make choices?
   - Example: "Which category should this content go to?"

2. **Define action space:** What are the options?
   - Example: [category_1, category_2, category_3, escalate_to_human]

3. **Define reward signal:** How do we know a decision was good?
   - Example: "User didn't appeal the categorization" = +1, "User appealed" = -1

4. **Assess learning data:** Do we have historical outcomes?
   - Example: "Yes, 6 months of decisions with appeal data"

#### Phase 2: Setup (2 weeks)
1. **Keep 3-Layer as fallback:** Existing code runs unchanged

2. **Instrument for learning:** Add outcome logging
   ```
   decision = 3_layer_router(content)
   outcome = get_user_feedback(decision)  # NEW: log this
   ```

3. **Choose algorithm:** Bandit? Q-learning? Policy gradient?
   - For router: Multi-armed bandit (simple, fast)

4. **Initialize policy:** Start with uniform or rule-based
   - Example: Equal probability for each category initially

#### Phase 3: Learning (4 weeks)
1. **Run both in parallel:**
   ```
   3_layer_decision = apply_rules(content)
   rl_decision = apply_policy(content)
   
   # Blend or A/B test
   final_decision = blend(3_layer_decision, rl_decision, trust_ratio=0.8)
   log_both_outcomes(3_layer_decision, rl_decision, actual_outcome)
   ```

2. **Monitor learning curve:**
   - Are we getting more agreements with 3-Layer?
   - Is policy converging?
   - Is performance improving?

3. **Gradually increase trust:**
   - Week 1: Trust 3-Layer 80%, RL 20%
   - Week 2: Trust 3-Layer 70%, RL 30%
   - Week 3: Trust 3-Layer 60%, RL 40%
   - Week 4: Trust 3-Layer 50%, RL 50%

#### Phase 4: Transition (2 weeks)
1. **Monitor metrics closely:**
   - Appeal rate (should stay ~same or improve)
   - Decision quality (rubric score)
   - Learning convergence

2. **Be ready to rollback:**
   - If appeal rate spikes
   - If new decisions are worse
   - If policy oscillates (not converging)

3. **Gradual switchover:**
   - Week 1: Use RL for 50% of traffic, 3-Layer for 50%
   - Week 2: Use RL for 75% of traffic
   - Week 3: Use RL for 95% of traffic
   - Week 4: Use RL for 100% (keep 3-Layer as fallback)

#### Phase 5: Stabilize (ongoing)
1. **Continue monitoring:** Learning should not stop
2. **Update rubrics:** As policy learns, update success metrics
3. **Periodic audits:** Check for policy drift or gaming

**Rollback plan:** If problems arise, revert to 3-Layer immediately (keep it running in parallel)

---

## See Also

- [MODE_COMPATIBILITY.md](MODE_COMPATIBILITY.md) — When/how to combine modes
- [AGENT_ARCHETYPES.md](AGENT_ARCHETYPES.md) — Agent patterns for each mode
- [../../blueprints/](../../blueprints/) — Real-world examples and migrations
- [../README.md](../README.md) — Documentation overview

---

### Pattern 2: 3-Layer → Agentic-Swarm (Add Specialization)

**Trigger:** Single agent becomes too complex; sub-specialization improves quality

**Example:**
- **Before:** Content reviewer with 50-line directive covering all policy areas (3-Layer)
- **After:** Chief Reviewer coordinating 4 specialized reviewers (Agentic-Swarm)

**Steps:**

#### Phase 1: Identify Specializations (1 week)
1. **Analyze current directive:**
   - Which responsibilities take most effort?
   - Which require different expertise?
   - What are natural seams?

2. **Example breakdown:**
   - Original reviewer: 50-line directive with if/else for each policy area
   - Natural split:
     - Hate speech specialist
     - Misinformation specialist
     - Spam specialist
     - Escalation coordinator (for hard cases)

#### Phase 2: Design Swarm (2 weeks)
1. **Define each sub-agent:**
   - Responsibility: What they own
   - Interface: Input/output spec
   - Mode: How they'll be implemented
   - Success criteria: What "good" looks like

2. **Define coordinator:**
   - How to route content to specialists?
   - How to combine their decisions?
   - How to handle disagreement?

3. **Create architecture diagram:**
   ```
   Chief Reviewer (Agentic-Swarm)
   ├─ Hate Speech Specialist (3-Layer)
   ├─ Misinformation Specialist (3-Layer)
   ├─ Spam Specialist (3-Layer)
   └─ Escalation Handler (3-Layer)
   ```

#### Phase 3: Implement Sub-agents (3 weeks)
1. **For each specialist:** Extract relevant rules from original directive

2. **Build interfaces:**
   - Input: [content, metadata]
   - Output: [decision, confidence, reasoning]

3. **Test individually:** Ensure each sub-agent works

#### Phase 4: Build Coordinator (2 weeks)
1. **Routing logic:**
   - Which specialist should review?
   - Send to one specialist or multiple?

2. **Synthesis logic:**
   - If all agree: Use their decision
   - If disagreement: Route to escalation
   - If no specialist matches: Escalate

3. **Test coordination:**
   - Sample content through new swarm
   - Compare to original 3-Layer decisions
   - Ensure coverage (no content unreviewed)

#### Phase 5: Parallel Testing (4 weeks)
1. **Run both systems:**
   ```
   3_layer_decision = original_reviewer(content)
   swarm_decision = chief_reviewer(content)
   
   log_both(3_layer_decision, swarm_decision)
   use_3_layer_decision  # Keep original in production
   ```

2. **Measure agreement:**
   - % decisions that agree
   - Appeal rates (should be similar)
   - Quality scores (should be similar or better)

3. **Monitor swarm health:**
   - Sub-agent utilization balanced?
   - Escalation rates reasonable?
   - Performance acceptable?

#### Phase 6: Transition (2 weeks)
1. **Gradual switchover (like RL-Loop):**
   - Week 1: 25% swarm, 75% 3-Layer
   - Week 2: 50% swarm, 50% 3-Layer
   - Week 3: 75% swarm, 25% 3-Layer
   - Week 4: 100% swarm (keep 3-Layer fallback)

2. **Watch key metrics:**
   - Appeal rate
   - Decision latency
   - Sub-agent errors

#### Phase 7: Stabilize (ongoing)
1. **Monitor sub-agent performance:** Are any underutilized?
2. **Optimize routing:** Routing accuracy matters
3. **Add/remove specialists:** As patterns emerge

**Rollback plan:** Revert to 3-Layer if swarm produces worse results

---

### Pattern 3: Event-Driven → Event-Driven + RL-Loop (Add Learning)

**Trigger:** Handling strategy should improve from outcomes

**Example:**
- **Before:** Alert handler with static severity rules (Event-Driven)
- **After:** Alert handler that learns optimal severity assessment (RL-Loop)

**Steps:**

#### Phase 1: Analysis (1 week)
1. **Identify learnable aspect:** Where could learning help?
   - Example: "Which severity level to assign to incoming alert"

2. **Define reward signal:** What outcome matters?
   - Example: "Was the alert escalated appropriately?" (not too high/low)

3. **Assess historical data:** Do past alerts have quality scores?
   - Example: "Yes, escalations reviewed by humans"

#### Phase 2: Wrap Handler in RL-Loop (2 weeks)
1. **Keep Event-Driven as-is:** Original event ingestion/routing unchanged

2. **Wrap handler:**
   ```
   on_alert_received(alert):
       # Event-Driven: Ingest and route
       alert_enriched = enrich_alert(alert)
       
       # RL-Loop: Assess severity
       severity = rl_agent.predict_severity(alert_enriched)
       
       # Execute handler
       handle_alert(alert_enriched, severity)
       
       # Log for learning (add outcome later)
       log_decision(alert_enriched, severity)
   ```

3. **Test that handlers still work correctly**

#### Phase 3: Learning Loop (4 weeks)
1. **Collect outcomes:**
   ```
   # Humans review escalations
   review_outcome = get_human_review(alert_id)  # "appropriate" / "too-high" / "too-low"
   ```

2. **Train RL agent:**
   ```
   for alert_id, human_assessment in historical_alerts:
       alert_data = get_alert_data(alert_id)
       predicted_severity = rl_agent.predict(alert_data)
       
       # Reward: How close was prediction to human assessment?
       reward = similarity(predicted_severity, human_assessment)
       
       rl_agent.learn(alert_data, predicted_severity, reward)
   ```

3. **Monitor learning curve:**
   - Is agent improving?
   - Are escalations more appropriate?
   - Is accuracy converging?

#### Phase 4: Transition (2 weeks)
1. **Gradual blend (like before):**
   - Week 1: 20% RL-learned severity, 80% rule-based
   - Week 2: 40% RL, 60% rule-based
   - Week 3: 60% RL, 40% rule-based
   - Week 4: 100% RL

2. **Monitor escalation appropriateness:**
   - Are false escalations decreasing?
   - Are missed escalations decreasing?

#### Phase 5: Stabilize (ongoing)
1. **Continue learning:** New alerts improve the model
2. **Watch for drift:** Does model performance degrade over time?
3. **Periodic retraining:** Retrain on recent data monthly

**Rollback plan:** Revert to rule-based severity if escalations become inappropriate

---

## Post-Migration: Learning from Migration

After any migration, document:
- **What changed:** Mode transition (X → Y)
- **Why:** Trigger and benefit expected
- **How long:** Each phase duration
- **Key decisions:** Important choices made
- **Lessons learned:** What worked, what was hard
- **Metrics before/after:** Quantified impact

This becomes valuable data for pattern library and future migrations.

---

## Checklist: Before Starting Migration

- [ ] Clear trigger: Why are we migrating now?
- [ ] Defined success metrics: How will we know it worked?
- [ ] Rollback plan: How quickly can we revert?
- [ ] Stakeholder alignment: Team agrees this change is needed?
- [ ] Learning data available: Do we have data to learn from?
- [ ] Parallel testing possible: Can we run both modes during transition?
- [ ] Timeline realistic: Phased approach over weeks, not days?
- [ ] Monitoring in place: Can we observe both systems?

---

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| **Worse performance during migration** | Keep original mode running in parallel; use gentle blending (80/20 → 60/40 → etc.) |
| **Policy doesn't converge** | Set learning timeout; revert if no improvement after 2 weeks |
| **Cascading failures** | Canary deployment; start with low-traffic portion of user base |
| **Unexpected edge cases** | Sample post-migration decisions manually before full cutover |
| **Stakeholder concerns** | Transparent metrics; regular updates on progress |

---

