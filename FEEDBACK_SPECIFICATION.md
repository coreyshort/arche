# Feedback Specification for arche MAOs

**Purpose:** Define what data every Multi-Agent Organization (MAO) should collect to enable continuous improvement — both internally and across the arche ecosystem.

**Version:** 1.0 (January 2026)
**Status:** Production Ready

---

## Overview

Every MAO is a learning system. This specification ensures that:
1. **Internal learning** — Each MAO improves its own agents and processes
2. **Ecosystem learning** — arche framework improves based on collective field data
3. **Consistency** — All MAOs speak the same "feedback language"

---

## Core Principle: Minimum Viable Feedback

**Don't collect everything.** Collect:
- **Essential metrics** — Directly indicate whether MAO is working
- **Decision data** — Inputs, outputs, outcomes of key decisions
- **Outcome signals** — External validation of agent performance
- **Anomalies** — Errors, failures, edge cases

Avoid:
- Excessive logging that slows down agents
- Metrics that don't drive decisions
- Proprietary/sensitive data that can't be shared

---

## Feedback Taxonomy

All feedback falls into 4 categories:

### Category 1: Decision Feedback
**What:** Input, decision, outcome for each key agent decision
**Why:** Understand if agents are deciding correctly
**Frequency:** Every decision
**Example:** 
```
Decision: Route content to category X
Outcome: Human reviewer agreed ✓ or disagreed ✗
Learning: Improve category prediction accuracy
```

### Category 2: Outcome Feedback
**What:** Business results of agent actions
**Why:** Measure actual impact
**Frequency:** Daily/weekly aggregate
**Example:**
```
Incident Response Blueprint:
- Incidents responded to: 1,247
- Average response time: 8 min
- Escalations needed: 3%
- Outcome: SLA met ✓
```

### Category 3: System Feedback
**What:** Agent errors, slowdowns, failures
**Why:** Identify bottlenecks and problems
**Frequency:** Real-time logging
**Example:**
```
Error: Policy Classifier timeout after 5s
Frequency: 2 per hour
Impact: 0.5% of content delayed
Action: Investigate classifier performance
```

### Category 4: Learnings Feedback
**What:** Conclusions from outcome analysis
**Why:** Capture insights, document improvements
**Frequency:** Weekly or after significant finding
**Example:**
```
Learning: Classifier accuracy improves 5% when 
we apply additional preprocessing. Implemented 
in change-request CR-2026-012.
```

---

## Feedback Collection Template

Every MAO should maintain a `09_learning/feedback-log.md` file (or equivalent) with these sections:

```markdown
# Feedback Log

## Decision Feedback

| Date | Agent | Decision | Input | Outcome | Confidence | Notes |
|------|-------|----------|-------|---------|------------|-------|
| 2026-01-05 | Content Classifier | Route to category: Misinformation | Text: "COVID-19 vaccine causes autism" | Reviewer: APPROVED ✓ | 95% | Variant of known false claim |
| 2026-01-05 | Content Classifier | Route to category: Spam | Text: "Buy cheap watches here" | Reviewer: APPROVED ✓ | 87% | Obvious commercial spam |
| 2026-01-05 | Alert Severity Assessor | Severity: HIGH | CPU: 98%, Error rate: 25% | Incident Commander: CORRECT ✓ | 92% | Proper escalation |
| 2026-01-05 | Alert Severity Assessor | Severity: LOW | Disk: 85% full | Incident Commander: TOO_LOW ✗ | 45% | Should have been MEDIUM |

## Outcome Feedback

### Daily Summary

**Date:** 2026-01-05

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Decisions processed | 1,247 | 1,000-1,500 | ✓ On-target |
| Accuracy rate | 94.2% | >92% | ✓ Met |
| Processing latency (p95) | 2.3s | <3s | ✓ Met |
| Error rate | 0.8% | <1% | ✓ Met |
| Escalations needed | 3.2% | <5% | ✓ Met |
| User satisfaction | 4.2/5 | >4.0 | ✓ Met |

## System Feedback

| Date | Component | Issue | Frequency | Impact | Status |
|------|-----------|-------|-----------|--------|--------|
| 2026-01-05 | Content Classifier | Timeout after 5s | 2-3/hour | 0.5% of traffic delayed | Investigating performance |
| 2026-01-05 | Alert Router | Queue overflow | 1/day | Alerts delayed 30s | Scaling queue size |
| 2026-01-04 | Knowledge Retriever | API error | 5/hour | Minimal (fallback activated) | Provider issue resolved |

## Learnings

| Date | Finding | Impact | Action | Status |
|------|---------|--------|--------|--------|
| 2026-01-05 | Classifier accuracy +5% with preprocessing | Could improve system by 500 decisions/day correct | Implement in CR-2026-012 | In progress |
| 2026-01-04 | 30% of escalations caused by missing context | Could reduce escalations by 9% | Add context enrichment | Design phase |
| 2026-01-03 | Alert Severity too conservative for application errors | False negatives increasing | Adjust threshold in RL-Loop | Deployed |
```

---

## Metrics by Agent Type

### For 3-Layer (Deterministic) Agents

**Collect:**
- Decision accuracy (% correct decisions, validated by humans or downstream impact)
- Error rate (% decisions that failed or needed correction)
- Latency (p50, p95, p99 time to decide)
- Compliance (% following all rules)

**Example:** Content reviewer agent
```
Accuracy: 94% (human reviewers agreed with decisions)
Error rate: 2% (decisions that had to be corrected)
Latency: 1.2s p95 (acceptable for review workflow)
Compliance: 100% (all policy checks passed)
```

### For RL-Loop (Learning) Agents

**Collect:**
- Decision outcome (reward signal, quality score, business metric)
- Learning curve (is model improving over time?)
- Convergence (has model stabilized?)
- Exploration vs. exploitation (is agent trying new things or just exploiting known good decisions?)

**Example:** Content preference learner
```
Reward signal: User clicked recommended content (1) or skipped (0)
Learning curve: Model accuracy was 45% (day 1) → 52% (day 7) → 58% (day 14)
Convergence: Accuracy plateau around day 20 at 61%
Exploration: 10% of recommendations are novel (still learning new patterns)
```

### For Event-Driven Agents

**Collect:**
- Event latency (time from event to response)
- Handler success rate (% of events handled correctly)
- Queue depth (how many events waiting?)
- Event loss (% of events dropped/missed?)

**Example:** Alert handler
```
Latency: 1.2s average (time from alert arrival to triage)
Success rate: 98% (handlers succeeded without errors)
Queue depth: 50 events at peak (acceptable)
Event loss: 0% (no alerts dropped)
```

### For Agentic-Swarm Agents

**Collect:**
- Coordination success (% of coordination attempts successful)
- Message latency (time between agent communication)
- Consensus rate (% of decisions with unanimous sub-agents)
- Sub-agent utilization (are all specialists being used?)

**Example:** Review coordinator
```
Coordination success: 99% (rare deadlock)
Message latency: 500ms average (acceptable)
Consensus rate: 87% (all specialists agree on outcome)
Utilization: Hate-speech: 45%, Misinformation: 38%, Spam: 17%
```

### For Foundry (Meta-Agent) Systems

**Collect:**
- MAO generation time (how long to scaffold new MAO?)
- Template quality (do generated templates work without modification?)
- Learning loop functionality (is each MAO learning?)
- Adoption rate (are generated MAOs being used?)

**Example:** Foundry instance
```
Generation time: 3 hours (acceptable, includes review)
Template quality: 95% usable with <10% modifications
Learning loops: 100% of MAOs have feedback collection working
Adoption: 8 of 10 generated MAOs in production after 3 months
```

---

## Feedback Reporting Format

### For Internal Learning (MAO team review)

**Frequency:** Weekly

**Format:** Markdown in `09_learning/feedback-log.md`

**Audience:** MAO development team

**Purpose:** Identify improvements, update agents, test changes

---

### For Ecosystem Learning (share with arche)

**Frequency:** Monthly (optional but encouraged)

**Format:** JSON export (for aggregation)

**How:** Create issue in arche GitHub with `[FEEDBACK]` tag

**Example issue:**
```markdown
Title: [FEEDBACK] BP-0004 Content Moderation - Monthly Report (Jan 2026)

## Summary
BP-0004 instance running for 1 month, moderate success with lessons.

## Key Metrics
- Decisions: 50,000
- Accuracy: 91% (target: >92%)
- Escalations: 5.2% (target: <5%)
- Learning improvements: Classifier +3% accuracy after feedback loop

## Lessons Learned
1. Feedback Processor needs human feedback on appeals (not just binary correct/wrong)
2. Alert fatigue from false positives in misinformation detection
3. Reviewer consistency improves with weekly calibration meetings

## Recommendations
- Update BP-0004 eval scenario to include reviewer calibration metric
- Consider reducing false positive rate in misinformation classifier
- Document best practice: weekly reviewer calibration

## JSON Data
[Full metrics in JSON format for analysis]
```

---

### For Contribution Impact (if you contributed a pattern/blueprint/archetype)

**Frequency:** After each major milestone (3 months, 6 months, 1 year)

**Format:** GitHub discussion or issue

**Example:**
```markdown
Title: Impact Report - BP-0005 Data Operations Blueprint

## Adoption
- 5 teams using blueprint
- 3 teams in production
- 2 teams in pilot

## Feedback
- Generally positive; learning loops work well
- Suggestion: Add "data quality" agent (currently missing)
- Question: How to handle ML pipeline failures (not covered)

## Metrics
- Avg incident response time: 8 minutes (SLA 15 min)
- False positive rate: 3.2% (expected ~5%)
- Team satisfaction: 4.1/5

## Next version
Suggest BP-0005-v2 to include:
- Data quality monitoring agent
- ML pipeline failure handling
- Cross-team learning registry
```

---

## Integration with Learning Loop

### Phase 1: Collect (Continuous)
Agents log decisions, outcomes, errors → `09_learning/feedback-log.md`

### Phase 2: Analyze (Weekly)
Team reviews feedback-log, identifies patterns → `09_learning/issue-backlog.md`

### Phase 3: Improve (Weekly-Monthly)
Create change requests for improvements → `09_learning/change-requests.md`

### Phase 4: Test (Before Deploy)
Run eval scenarios to validate changes → `09_learning/eval/scorecard.md`

### Phase 5: Share (Monthly-Quarterly)
Report learnings back to arche ecosystem → GitHub issue with `[FEEDBACK]`

### Phase 6: Close Loop (Quarterly)
arche reviews feedback, updates blueprints/modes/advisories → affects next MAO generation

---

## Privacy & Sensitivity

### What NOT to Log

❌ Personally identifiable information (PII)
❌ Sensitive business metrics (unless anonymized)
❌ Proprietary algorithms
❌ Customer secrets
❌ Financial details (unless aggregated)

### What's Safe to Log

✅ Aggregate metrics (accuracy %, latency ms, SLA met/missed)
✅ Pattern information ("50% of escalations are due to X")
✅ Generic learnings ("preprocessing improved accuracy")
✅ Framework improvements needed ("blueprint needs Y capability")

### Anonymization

Before sharing with arche ecosystem:
1. Remove/anonymize domain-specific context
2. Report patterns, not individual decisions
3. Aggregate across time periods (don't report individual user impact)
4. Share learnings, not raw data

**Example:**
```
Good: "Classifier accuracy increased 5% after adding preprocessing step"
Bad: "Our healthcare billing system accuracy is now 97.3%"

Good: "30% of escalations need additional context" 
Bad: "Patient #12345 escalated because of visit date conflict"
```

---

## Feedback Template for MAO README

Include this in every MAO's README.md:

```markdown
## Learning & Feedback

This MAO maintains a learning loop to improve continuously.

### Feedback Collection
- Frequency: Real-time (decisions), daily aggregates (metrics), weekly analysis (patterns)
- Location: `09_learning/feedback-log.md`
- Feedback categories: Decision accuracy, outcomes, system health, learnings

### Improvement Process
1. **Collect:** Agents log decisions and outcomes
2. **Analyze:** Weekly review identifies patterns and issues
3. **Improve:** Create change requests for improvements
4. **Test:** Run eval scenarios before deploying changes
5. **Share:** Report learnings to arche ecosystem (optional but encouraged)

### How to Share Feedback
Found improvements that should go back to arche? Create a GitHub issue:
- Title: `[FEEDBACK] [Blueprint/Mode/Archetype] - [Learning]`
- Include: Metrics, context, recommendations
- Link: Reference this MAO

See FEEDBACK_SPECIFICATION.md in arche repo for detailed guidance.
```

---

## Success Criteria

After implementing this specification, you'll know it's working if:

✅ Every MAO has `09_learning/feedback-log.md` with structured data
✅ Teams can answer: "Is our MAO improving?" (weekly)
✅ Teams can answer: "What helped us improve?" (monthly)
✅ arche team can answer: "Which blueprints are working?" (quarterly)
✅ arche can identify: "Which archetypes need refinement?" (quarterly)
✅ arche discovers: "Common problems across teams" (quarterly)
✅ arche updates: Modes/blueprints/archetypes based on field data (quarterly)
✅ Community learns: Best practices shared between teams (monthly)

---

## Rollout Timeline

### Phase 1: Documentation (Week 1)
- Publish FEEDBACK_SPECIFICATION.md (this file)
- Create feedback-log template in Foundry examples
- Update ARCHE_INTEGRATION_GUIDE.md with this spec

### Phase 2: Pilot (Weeks 2-4)
- Invite 3 teams to pilot feedback collection
- Gather feedback on specification clarity
- Refine based on pilot experience

### Phase 3: Ecosystem Rollout (Week 5+)
- All new MAOs generated by Foundry include feedback logging
- Encourage existing MAOs to adopt (retroactively)
- Monthly community reporting becomes standard

### Phase 4: Analysis (Month 2+)
- arche team reviews feedback quarterly
- Create improvement plan based on patterns
- Update blueprints/archetypes/modes with learnings

---

## FAQ

**Q: Isn't this just logging?**

A: No. Logging is collection. This spec adds:
- Structure (what to collect)
- Analysis (weekly review for patterns)
- Action (improvements based on patterns)
- Loop closure (feedback flows back to framework)

**Q: How much overhead?**

A: Minimal. Structured logging adds ~5-10% CPU. Analysis is manual but quick (30 min/week).

**Q: What if I'm too small to do all this?**

A: Start with Category 1 (Decision Feedback). Add others as you grow.

**Q: Do I have to share feedback with arche?**

A: No, it's optional. But it's how arche improves, and you benefit from others' learnings.

**Q: How do I know if I'm doing it right?**

A: Run the checklist:
- [ ] Decision feedback logged for each agent decision
- [ ] Weekly outcome summary compiled
- [ ] System errors tracked and analyzed
- [ ] Learnings documented when improvements made
- [ ] Check: "Can I see evidence my MAO is improving?"

If yes to all, you're doing it right.

---

## Next Steps

1. **Implement in Foundry:** Add feedback-log template to all new MAOs
2. **Update existing MAOs:** Encourage adoption retroactively
3. **Create feedback intake process:** arche team reviews submissions monthly
4. **Build feedback dashboard:** Visualize ecosystem learning (future)
5. **Run quarterly analysis:** Update frameworks based on field data

---

