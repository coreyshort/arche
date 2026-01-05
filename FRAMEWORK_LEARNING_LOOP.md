# arche Framework Learning Loop

**Purpose:** Define how arche itself improves based on feedback from MAO teams, contributors, and the community.

**Version:** 1.0 (January 2026)
**Status:** Establishing organizational learning

---

## Overview

arche is more than a static framework. It should improve continuously based on:
- **Field data** from deployed MAOs (what works, what doesn't)
- **Contribution feedback** from community members (what's missing)
- **Usage patterns** (which modes/blueprints/archetypes are most valuable)
- **Evolution opportunities** (how to mature modes, add new capabilities)

This document describes arche's own learning loop.

---

## The Framework Learning Loop

```
┌─────────────────────────────────────────────────────────────┐
│ 1. COLLECT: Teams report learnings & feedback             │
│    • Monthly feedback issues from MAO teams               │
│    • Contribution impact reports                         │
│    • Community discussions & GitHub issues               │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. ANALYZE: Core team reviews patterns quarterly           │
│    • What's working? (adoption, satisfaction)            │
│    • What's broken? (problems, unmet needs)             │
│    • What's missing? (gaps, opportunities)              │
│    • Create quarterly insight report                     │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. PLAN: Core team creates improvement roadmap            │
│    • Prioritize: Which issues are most important?        │
│    • Scope: What work can we do this quarter?           │
│    • Assign: Who owns each improvement?                  │
│    • Release: When will improvements ship?              │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. IMPLEMENT: Core team and community make improvements   │
│    • Update modes, blueprints, archetypes               │
│    • Create new guides, tools, capabilities             │
│    • Document changes clearly                           │
│    • Create upgrade advisories for breaking changes     │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ 5. SHARE: Release improvements to ecosystem              │
│    • Publish upgrade advisories                         │
│    • Update documentation                               │
│    • Announce in community channels                     │
│    • Provide migration guides where needed              │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ 6. VALIDATE: Teams adopt improvements, report results    │
│    • New MAOs use updated frameworks                    │
│    • Existing MAOs migrate to improvements             │
│    • Teams report back on effectiveness               │
│    • Loop closes → back to step 1                      │
└─────────────────────────────────────────────────────────────┘
```

---

## Step 1: COLLECT — Feedback Intake

### What We Collect

**Type 1: Feedback Issues** (from MAO teams)
- Monthly issues with `[FEEDBACK]` tag in GitHub
- Structured report using FEEDBACK_SPECIFICATION.md template
- Content: Metrics, learnings, recommendations, context

**Type 2: Contribution Reports** (from contributors)
- Impact reports after 3 months, 6 months, 1 year
- Adoption data: How many teams using this contribution?
- Satisfaction: Is it working as intended?
- Suggestions: What's missing or broken?

**Type 3: Community Input** (from discussions)
- GitHub discussions on pain points
- Feature requests in issue tracker
- Suggestions in community calls
- Comments on upgrade advisories

**Type 4: Telemetry** (automatic)
- Advisory adoption rates (do teams use updates?)
- Mode selection data (which modes are most popular?)
- Tool usage (which tools are most helpful?)
- Error/warning logs (what's breaking for teams?)

### Collection Process

**Monthly (Manual)**
```
1. Core team monitors GitHub [FEEDBACK] issues
2. Categorize: Blueprint-specific? Mode-level? Archetype? Tool?
3. Extract: Key metrics, patterns, recommendations
4. File: Store in `framework-data/monthly-feedback-[month].md`
```

**Quarterly (Structured Review)**
```
1. Compile all monthly feedback into quarterly summary
2. Identify themes and patterns
3. Assess: Do patterns indicate problems or opportunities?
4. Prioritize: Which issues matter most?
5. Create: Quarterly insight report (step 2)
```

### Feedback Channels

| Channel | Type | Frequency | Response Time |
|---------|------|-----------|---|
| GitHub `[FEEDBACK]` issues | Structured | Monthly expected | Within 1 week |
| GitHub discussions | Unstructured | Ongoing | Within 2 weeks |
| Contribution reports | Structured | Milestone-based | Review quarterly |
| Community calls | Verbal | Monthly (if held) | Notes within 1 week |
| Telemetry/dashboards | Automatic | Continuous | Analyzed quarterly |

---

## Step 2: ANALYZE — Quarterly Review

### Quarterly Review Process

**Timing:** First week of Q+1 (Jan, Apr, Jul, Oct)

**Duration:** 1 full day (core team)

**Agenda:**
1. **Review feedback** (2 hours) — Read all feedback collected this quarter
2. **Identify patterns** (1 hour) — What themes emerge?
3. **Assess impact** (1 hour) — Which problems/opportunities matter most?
4. **Create report** (2 hours) — Document insights and recommendations

### Quarterly Insight Report

**Structure:**

```markdown
# arche Quarterly Insight Report: Q1 2026

## Executive Summary
High-level findings: What's working, what's not, what's needed

## Feedback Summary
- Feedback issues received: N
- Teams reporting: N
- Contributions: N new, N improvements

## Key Findings

### 🟢 What's Working
- BP-0003 (Incident Response): 8 teams, all in production, high satisfaction
- Mode compatibility framework: No incompatibility problems reported
- Learning loops: 95% of MAOs report measurable improvements

### 🟡 What Needs Work
- RL-Loop mode: Convergence issues reported by 3 teams
- BP-0004 evaluation scenarios: Feedback suggests need for domain-specific variants
- Documentation: New users struggling with learning loop setup

### 🔴 What's Missing
- Data quality monitoring (requested by 4 teams)
- Multi-team learning registry (requested by 2 teams)
- Tool for pattern discovery across MAOs (suggested by community)

## Detailed Patterns

### Pattern 1: RL-Loop Convergence Challenges
**Evidence:**
- 3 teams reported slow convergence (>4 weeks)
- Root cause: Reward signal not aligned with team goals
- Teams needed: Better guidance on reward signal design

**Recommendation:**
- Create RL-Loop reward signal design guide
- Add eval scenario specifically for reward signal validation
- Include in next BP-XXXX updates

**Priority:** HIGH
**Owner:** Mode team (RL-Loop)
**Timeline:** Q2 2026

### Pattern 2: Blueprint Customization Needs
**Evidence:**
- Teams using BP-0003, BP-0004, BP-0005 report ~30% modifications
- Common changes: Domain-specific agent specialization, different eval metrics
- Teams would benefit from: Customization guidance, variants for different domains

**Recommendation:**
- Create BP customization guide
- Document common variants (BP-0003-healthcare, BP-0003-finance)
- Establish template for domain variants

**Priority:** MEDIUM
**Owner:** Blueprint team
**Timeline:** Q2 2026

### Pattern 3: Data Quality Monitoring Gap
**Evidence:**
- 4 teams (across data-ops and other domains) need data quality monitoring
- Currently not covered by any blueprint
- Could become BP-0006

**Recommendation:**
- Propose new blueprint: BP-0006 Data Quality Monitoring
- RFC process in Q2
- Aim for release Q3

**Priority:** MEDIUM
**Owner:** Community (with core team support)
**Timeline:** Q2 RFC, Q3 implementation

## Improvement Roadmap: Q2 2026

### High Priority (Start immediately)
1. RL-Loop reward signal design guide (2 weeks)
2. Update MODE_MIGRATION_GUIDE for RL-Loop challenges (1 week)
3. New ADV advisory: "RL-Loop Best Practices" (1 week)

### Medium Priority (Start within 2 weeks)
1. BP customization guide (2 weeks)
2. Design BP domain variants (1 week)
3. Community RFC period for BP-0006 Data Quality (ongoing)

### Lower Priority (Start month 2 of quarter)
1. Tool for pattern discovery (exploratory, 2 weeks)
2. Multi-team learning registry design (exploratory, 1 week)

## Community Contributions to Integrate
1. New archetype: Health Data Validator (from Dr. Smith's team) → Merge Q2
2. BP-0004 variant: Healthcare Content Moderation (from SafeHealth Inc.) → Merge Q2

## Metrics of Framework Health

| Metric | Q4 2025 | Q1 2026 | Target | Status |
|--------|---------|---------|--------|--------|
| Active MAOs | 12 | 18 | 25 | 📈 Growing |
| Team satisfaction | 4.1/5 | 4.3/5 | 4.5+ | 📈 Improving |
| Advisory adoption | 85% | 92% | 95%+ | 📈 Good |
| Issues/problems reported | 8 | 12 | <10 | ⚠️ Growing |
| Contributions received | 2 | 5 | 8+ | 📈 Good |

**Interpretation:** Framework is working well (high satisfaction, adoption). Growing problems indicate growth (more teams = more edge cases). Increasing contributions show community engagement.

## Next Steps
1. Present report to community (monthly call)
2. Create GitHub milestone for Q2 improvements
3. Assign ownership for each improvement
4. Begin work on High Priority items
5. Schedule Q2 RFC for new contributions
```

---

## Step 3: PLAN — Quarterly Roadmap

### Roadmap Creation

**Input:** Quarterly insight report

**Output:** 
- Prioritized improvement list
- Owner assignments
- Timeline estimates
- Dependency mapping

**Process:**

```
1. Core team reviews insight report
2. Score each improvement:
   - Impact: How many teams affected? (1-5 scale)
   - Effort: How much work? (1-5 scale)
   - Dependencies: Blocks on other work? (yes/no)
   - Priority = (Impact × 2 + (6 - Effort)) / Dependency multiplier

3. Rank by priority score
4. Allocate team capacity (realistic hours, not optimistic)
5. Assign owners
6. Create GitHub milestone with issues
7. Communicate timeline to community
```

### Example Roadmap

**Q2 2026 Improvement Plan**

| Improvement | Impact | Effort | Priority | Owner | Timeline | Status |
|-------------|--------|--------|----------|-------|----------|--------|
| RL-Loop reward signal guide | 4 | 2 | 8 | Sarah | Weeks 1-2 | Scheduled |
| Update MODE_MIGRATION_GUIDE | 3 | 1 | 7 | Alex | Week 3 | Scheduled |
| ADV advisory: RL-Loop | 3 | 1 | 7 | Sarah | Week 4 | Scheduled |
| BP customization guide | 3 | 3 | 5 | Jamie | Weeks 2-4 | Scheduled |
| BP domain variants (design) | 2 | 2 | 4 | Jamie | Week 3-4 | Scheduled |
| BP-0006 RFC support | 2 | 2 | 4 | Core team | Weeks 2-4 | Scheduled |
| Pattern discovery tool (explore) | 2 | 3 | 3 | Intern | Weeks 3-4 | Scheduled |

**Capacity:** 100 hours available, 85 hours allocated (85% utilization, leaves buffer)

---

## Step 4: IMPLEMENT — Development

### Development Process

Each improvement follows standard workflow:

```
1. Create GitHub issue (if not existing)
   - Title: Clear and specific
   - Description: What, why, success criteria
   - Labels: Type (guide, tool, advisory), priority
   - Estimate: Time to complete

2. Create draft
   - Write/code in branch
   - Keep changes focused
   - Link to issue for context

3. Review (internal)
   - Core team members review
   - Check: Clarity, completeness, alignment with framework
   - Request changes if needed

4. Gather feedback (external)
   - Share draft with community
   - Issue comments or discussion thread
   - Incorporate feedback

5. Finalize
   - Apply feedback
   - Quality check
   - Ready for merge

6. Document changes
   - Update UPGRADE_ADVISORIES.md if breaking change
   - Mention in release notes
   - Link from related docs
```

### Quality Standards

**For Guides:**
- [ ] Clarity: Can someone new understand?
- [ ] Examples: Concrete examples provided?
- [ ] Links: Cross-references to related docs?
- [ ] Feedback: How to report if guide is unclear?

**For Tools:**
- [ ] Testing: Works as documented?
- [ ] Error handling: Graceful failures?
- [ ] Documentation: README with usage?
- [ ] Feedback: How to report bugs?

**For Updates to Frameworks:**
- [ ] Backward compatibility: Will existing MAOs break?
- [ ] Migration path: How do teams adopt this?
- [ ] Documentation: Updated to reflect changes?
- [ ] Advisory: Created if breaking change?

---

## Step 5: SHARE — Release

### Release Process

**Timing:** Coordinated monthly or quarterly

**Activities:**

1. **Create release notes**
   - Summary of improvements
   - What changed
   - How to adopt
   - Migration guides for breaking changes

2. **Update documentation**
   - Merge changes to main branch
   - Update related docs
   - Update registries

3. **Publish upgrade advisories**
   - Create ADV-XXXX for new advisories
   - Link to guides and migration docs
   - Set timeline for adoption

4. **Announce to community**
   - Email newsletter (if you have one)
   - GitHub release announcement
   - Community call
   - Social media

5. **Provide support**
   - Monitor for questions
   - Provide examples
   - Help teams migrate

### Release Template

```markdown
# arche Release: Q2 2026 Improvements

## Summary
This release includes improvements to RL-Loop mode, blueprint customization 
guidance, and new evaluation scenarios based on Q1 community feedback.

## What's New

### Guides
- **RL-Loop Reward Signal Design Guide** — How to define good reward signals
- **Blueprint Customization Guide** — How to adapt blueprints to your domain
- **Domain Variant Template** — Framework for BP variants (healthcare, finance, etc.)

### Updates
- MODE_MIGRATION_GUIDE improved with RL-Loop convergence best practices
- MODE_COMPATIBILITY.md updated with convergence patterns
- Three new eval scenarios (RL-Loop focused)

### Tools
- [Future] Pattern discovery dashboard (beta)

### Community Contributions
- New archetype: Health Data Validator (contributed by Dr. Smith)
- BP-0004 variant: Healthcare Content Moderation (contributed by SafeHealth Inc.)

## Migration Guide
Most updates are backward compatible. See ADV-2026-Q2-001 for details.

## Adoption Timeline
- RECOMMENDED advisories: Adopt within 2-4 weeks
- OPTIONAL updates: Adopt at next MAO iteration
- New blueprints/archetypes: For new MAOs or redesigns

## Feedback
Have questions? Found issues? We want to hear:
1. Open GitHub issue with `[FEEDBACK]` tag
2. Join discussion thread in GitHub
3. Attend community call

Thank you for using arche and helping us improve!
```

---

## Step 6: VALIDATE — Adoption & Feedback Loop

### Monitoring Adoption

**By metric:**
- What % of teams adopted the improvement?
- How long did adoption take?
- Did improvement solve the reported problem?

**By process:**
- Did migration guides help?
- Were there problems we didn't anticipate?
- Do teams have new feedback on the improvement?

### Closing the Loop

**Quarterly (+ 3 months after release):**

```
1. Check adoption metrics
   - RL-Loop guide adoption: 70% of RL-Loop teams have read it
   - BP customization guide: Used by 40% of new MAO implementations
   - ADV compliance: 88% of teams have reviewed Q2 advisories

2. Gather follow-up feedback
   - Did guide help? (survey)
   - Did problem get solved? (outcome metrics)
   - Are new problems emerging? (support tickets)
   - Improvement ideas? (open issues)

3. Iterate if needed
   - If adoption is low: Was guide unclear? Did it miss key info?
   - If problem not solved: Do we need a different approach?
   - If new problems: Add to next quarterly insight report

4. Document lessons learned
   - What worked in this release cycle?
   - What would we do differently?
   - Updated process for next quarter
```

---

## Governance

### Who Does What

| Role | Responsibility |
|------|-----------------|
| **Core Team** | Collect feedback, analyze patterns, plan improvements, review PRs |
| **Mode Owners** | Maintain assigned modes, respond to issues, propose improvements |
| **Blueprint Authors** | Update blueprints, monitor adoption, support teams using them |
| **Contributors** | Propose improvements, provide feedback, implement contributions |
| **Community** | Use frameworks, report feedback, suggest improvements |

### Decision Making

**Consensus-based:**
- Most decisions by discussion and agreement
- Core team facilitates, doesn't dictate

**Escalation:**
- Disagreements: Discussed in community call
- Unresolved: Core team decides with community input

**Transparency:**
- All decisions documented
- Rationale explained
- Community can appeal/discuss

---

## Metrics for Framework Health

Track these quarterly to assess if learning loop is working:

| Metric | What It Means | Target | Frequency |
|--------|---------------|--------|-----------|
| **Feedback volume** | How engaged is community? | 10-20 issues/month | Monthly |
| **Advisory adoption** | Do teams adopt improvements? | 85%+ | Monthly |
| **Team satisfaction** | Are teams happy? | 4.0+/5.0 | Quarterly |
| **Contribution rate** | Is community extending? | 3-5 new/quarter | Quarterly |
| **Mode maturity progression** | Are modes evolving? | 1-2 mode levels/year | Quarterly |
| **Blueprint variants** | Customization adoption? | 2-4 variants/quarter | Quarterly |
| **Time to improvement** | How fast do we respond? | <6 weeks from feedback to release | Quarterly |
| **Problem resolution** | Do improvements solve issues? | 80%+ of feedback-driven improvements solve their problem | Quarterly |

---

## Example: From Feedback to Improvement

**Real Example Flow:**

```
T=0: Jan 5 — Team reports feedback
  Issue: "[FEEDBACK] RL-Loop convergence too slow"
  Problem: "Took 8 weeks to reach 95% accuracy, expected 4 weeks"
  Context: "Commerce recommendation system"
  Suggestion: "Batch learning mode?"

T=1: Jan 15 — Core team reviews quarterly
  Analysis: "3 teams reported similar RL-Loop slowness"
  Pattern: "Slow convergence when reward signal is sparse"
  Root cause: "Poor reward signal design, not algorithm"

T=2: Jan 20 — Roadmap planning
  Decision: Create "RL-Loop Reward Signal Design Guide"
  Priority: HIGH (3 teams blocked)
  Owner: Sarah
  Timeline: 2 weeks

T=3: Jan 21-Feb 3 — Implementation
  Sarah creates guide with examples
  Covers: What makes good reward signals, common mistakes, testing
  Links to: MODE_MIGRATION_GUIDE, UPGRADE_ADVISORIES

T=4: Feb 5 — Community review
  Post draft for feedback
  Community comments: "Need healthcare example", "More on sparse signals"
  Sarah incorporates feedback

T=5: Feb 10 — Publish
  Guide merged to main
  New ADV advisory: "RL-Loop Reward Signal Design"
  Announced in newsletter and community call

T=6: Feb 11 — Three teams read guide
  Review their reward signals (following guide)
  Find: "We're using binary reward; should be multi-valued"
  Implement recommendations

T=7: Mar 1 — Feedback on guide
  First team reports: "Guide helped us improve convergence by 3 weeks!"
  Second team: "Could use more domain-specific examples"
  Sarah notes for next update

T=8: Apr 1 — Quarterly review
  Success metric: 70% of RL-Loop teams report reading guide
  Outcome metric: Teams using guide report 2-3 week faster convergence
  Feedback: Most useful, a few requests for more examples
  Plan: Update guide in Q3 with domain examples

Loop closes → Back to T=0 (feedback → improvement → validation → feedback)
```

---

## Success Criteria

When is the framework learning loop working well?

✅ **Rapid feedback**: Teams report issues within days/weeks
✅ **Regular analysis**: Quarterly reviews happen on schedule
✅ **Responsive improvements**: High-priority issues addressed within 6 weeks
✅ **Adoption**: 85%+ of teams adopt recommended improvements
✅ **Satisfaction**: Team satisfaction stays 4.0+/5.0
✅ **Community engagement**: 3-5 contributions per quarter
✅ **Framework evolution**: Modes/blueprints improve quarterly
✅ **Impact**: Improvements solve the problems they were meant to solve (80%+)

---

## Next Steps

1. **Establish feedback intake process** — GitHub issue template, review schedule
2. **Schedule first quarterly review** — April 1, 2026
3. **Create first insight report** — Document patterns from early feedback
4. **Begin quarterly roadmap planning** — Prioritize improvements
5. **Share this document** — Make process transparent to community

---

