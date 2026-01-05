# Upgrade Advisories System

**Purpose:** Help MAO teams understand when, how, and why to adopt arche updates.

---

## Overview

arche evolves continuously. Upgrade advisories guide teams through:
- **What changed** in arche modes, archetypes, blueprints
- **Why it matters** for your MAO
- **How to adopt** the change (patch pack or migration)
- **Timeline** for when to upgrade (critical vs. optional)

---

## Advisory Lifecycle

### 1. Advisory Issued
- Published in `ADVISORY_REGISTRY.md` with advisory ID (e.g., ADV-2026-001)
- Describes change, impact, affected MAOs, action required
- Links to patch pack or migration guide

### 2. Advisory Adoption (by MAO teams)
- Teams assess applicability to their MAO
- Teams apply patch pack or follow migration guide
- Teams update `upgrades-log.md` in their MAO

### 3. Advisory Retirement
- After 6 months, advisory moved to archive
- All teams should have adopted by then
- Becomes part of normal documentation

---

## Advisory Categories

### Category 1: Security/Compliance (CRITICAL)
**Adoption required:** Immediately (1-7 days)

Examples:
- Mode vulnerability discovered and patched
- Compliance requirement changes (GDPR, etc.)
- Security best practice added to all blueprints

Template:
```markdown
## ADV-2026-SEC-001: SQL Injection Prevention in Data-Ops Blueprint

**Severity:** CRITICAL
**Affected MAOs:** All BP-0005 (Data Operations) MAOs
**Timeline:** Must adopt within 7 days

### What Changed
Blueprint BP-0005 now includes SQL injection guards for all database queries.

### Why It Matters
Recent audit found potential injection vulnerability in data ingestion agents.

### Action Required
Apply patch FND-PATCH-SEC-001 (see PATCH_REGISTRY.md)

### Rollback Risk
Low. Patch only adds validation, doesn't change logic.

### Questions?
Contact: [team contact]
```

### Category 2: Mode Enhancement (RECOMMENDED)
**Adoption required:** When applicable (2-4 weeks)

Examples:
- New capability added to mode (e.g., RL-Loop batching)
- Performance improvement released
- New archetype added to pattern library

Template:
```markdown
## ADV-2026-ENH-002: RL-Loop Batch Learning Mode

**Severity:** RECOMMENDED
**Affected MAOs:** RL-Loop agents that do real-time learning
**Timeline:** Adopt within 2-4 weeks for performance benefit

### What Changed
RL-Loop mode now supports batch learning (accumulate 1000 decisions, then learn).

### Why It Matters
- 3x faster learning convergence for high-volume decisions
- Reduces computational overhead
- Better for high-frequency trading, content routing, resource allocation

### Action Required
Apply patch FND-PATCH-ENH-002 or follow MODE_MIGRATION_GUIDE (RL-Loop batch learning section)

### Benefit Estimation
- Agents learning from 10K+ decisions/day: ~40% faster convergence
- Agents learning from <1K decisions/day: No significant benefit

### Rollback Risk
Very low. Batch mode is opt-in flag; doesn't affect existing agents.

### Questions?
Contact: [team contact]
```

### Category 3: Archetype Update (OPTIONAL)
**Adoption required:** At next MAO version (monthly)

Examples:
- New agent archetype added to library
- Existing archetype refined with new template
- Success metrics clarified for archetype

Template:
```markdown
## ADV-2026-ARC-003: Debugger Archetype Added

**Severity:** OPTIONAL
**Affected MAOs:** None immediately (new archetype)
**Timeline:** Consider for next MAO iteration

### What Changed
New Debugger archetype added: agents that diagnose agent failures and suggest fixes.

### Why It Matters
- Enables self-healing MAOs
- Useful for incident response, data ops, content moderation
- Reduces manual debugging overhead

### Archetype Details
See AGENT_ARCHETYPES.md (new entry: Debugger)

### Action Required
If you need diagnostic capability: Consider adding Debugger agent to your MAO

### Example Implementation
[Link to example MAO using Debugger]

### Questions?
Contact: [team contact]
```

### Category 4: Blueprint Improvement (OPTIONAL)
**Adoption required:** At domain redesign (annual)

Examples:
- Domain blueprint refined based on learnings
- New eval scenario added
- Governance updated

Template:
```markdown
## ADV-2026-BP-004: BP-0003 Incident Response: Alert Fatigue Mitigation

**Severity:** OPTIONAL
**Affected MAOs:** Incident response MAOs running BP-0003
**Timeline:** Consider for Q2 redesign

### What Changed
BP-0003 now includes Alert Fatigue Mitigation agent (new archetype: Dampener).

### Why It Matters
- Reduces false-positive escalations by ~35% (based on field data)
- Improves on-call reliability
- Prevents alert fatigue burnout

### Action Required
Review eval-scenario-alert-fatigue.md (new scenario in BP-0003)

### Adoption Path
1. Read: BP-0003 updated section "Alert Fatigue Mitigation"
2. Run: eval-scenario-alert-fatigue.md against your MAO
3. Decide: Worth adding Dampener agent? (usually yes if >500 alerts/day)
4. Implement: Add Dampener agent and retest

### Rollback Risk
Very low. Dampener is optional sub-agent; removing it reverts behavior.

### Questions?
Contact: [team contact]
```

---

## Advisory Registry

| Advisory ID | Category | Title | Status | Impact |
|-------------|----------|-------|--------|--------|
| ADV-2026-001 | Security | Foundry Mode Security Review | **ACTIVE** | 🔴 CRITICAL |
| FND-0004 | Enhancement | Mode Integration in MAOs | **ACTIVE** | 🟡 RECOMMENDED |
| ADV-2026-ENH-002 | Enhancement | RL-Loop Batch Learning | **ACTIVE** | 🟡 RECOMMENDED |
| ADV-2026-BP-001 | Blueprint | BP-0003: Alert Fatigue | **PENDING** | 🟢 OPTIONAL |

---

## Using Advisories in Your MAO

### 1. Track Adoption

Create `upgrades-log.md` in your MAO:

```markdown
# Upgrade and Advisory Log

## Adopted Advisories

| Advisory | Version | Date | Status | Notes |
|----------|---------|------|--------|-------|
| ADV-2026-001 | 1.0 | 2026-01-15 | ✅ Applied | Security review passed |
| FND-0004 | 1.1 | 2026-01-10 | ✅ Applied | Mode integration working well |
| ADV-2026-ENH-002 | 1.0 | 2026-01-20 | 🔄 In Progress | Batch learning in test |

## Pending Advisories

| Advisory | Status | Timeline |
|----------|--------|----------|
| ADV-2026-BP-001 | Evaluating | Q2 redesign |
```

### 2. Subscribe to Notifications

Check `ADVISORY_REGISTRY.md` weekly (or use RSS if available):
- Critical advisories: Act immediately
- Recommended: Evaluate impact within 2 weeks
- Optional: Consider at next update cycle

### 3. Ask Questions

If an advisory doesn't apply to you, ask why:
- Does your MAO use that mode/blueprint/archetype?
- Is timeline realistic for your team?
- Do you need help applying the patch?

---

## Creating a New Advisory

When arche core team has an update to share:

### 1. Draft Advisory

Use template matching your category:
- CRITICAL: Security template
- RECOMMENDED: Enhancement template
- OPTIONAL: Archetype/Blueprint template

### 2. Review Checklist

- [ ] Clear title (what changed)
- [ ] Severity level assigned
- [ ] Affected MAOs listed
- [ ] Action steps explicit
- [ ] Rollback plan documented
- [ ] Contact info provided
- [ ] Patch or guide linked

### 3. Publish

1. Add to `ADVISORY_REGISTRY.md` (marked PENDING)
2. Create advisory markdown file (e.g., `ADV-2026-001.md`)
3. Link from `ADVISORY_REGISTRY.md`
4. Notify known MAO teams (email/Slack/GitHub)
5. Update status to ACTIVE

### 4. Archive

After 6 months:
1. Move advisory to `archived-advisories/`
2. Update registry (mark as ARCHIVED)
3. Assume all teams have adopted

---

## FAQ: Advisories

**Q: Do I have to adopt every advisory?**

A: No. CRITICAL advisories are mandatory. RECOMMENDED and OPTIONAL advisories are your choice based on:
- Does it apply to my MAO?
- Does the benefit justify the work?
- When do I have time to implement?

**Q: What if I disagree with an advisory?**

A: Great question. Open an issue in GitHub or discuss with team. Advisories are guidance, not laws. If there's a better approach for your situation, let's talk.

**Q: Can I ask for a custom advisory for my domain?**

A: Yes. If you need domain-specific guidance (e.g., "Healthcare incident response"), we can create a domain-specific advisory or blueprint extension. Reach out to core team.

**Q: How often are advisories released?**

A: ~1-2 per month (mix of security, enhancements, optional updates). Critical advisories are rare (hopefully).

**Q: What if I miss an advisory?**

A: No problem. Advisories remain available indefinitely. You can apply them anytime. CRITICAL advisories are high-visibility; you won't miss those.

---

## Advisory Archive

Advisories older than 6 months are moved to `archived-advisories/` directory.

These document historical context:
- How arche has evolved
- What teams have dealt with
- Patterns and lessons learned

Example: "How we addressed RL-Loop convergence issues" (helpful for new teams implementing learning)

---

## See Also

- [MODE_COMPATIBILITY.md](MODE_COMPATIBILITY.md) — Mode compatibility and integration patterns
- [AGENT_ARCHETYPES.md](AGENT_ARCHETYPES.md) — Agent patterns affected by upgrades
- [MODE_MIGRATION_GUIDE.md](MODE_MIGRATION_GUIDE.md) — Guidance for migrating between versions
- [COMMUNITY_CONTRIBUTION_PATHWAY.md](COMMUNITY_CONTRIBUTION_PATHWAY.md) — How to propose improvements
- [../README.md](../README.md) — Documentation overview

---

