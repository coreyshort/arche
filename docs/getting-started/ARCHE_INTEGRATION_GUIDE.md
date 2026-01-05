# arche Framework: Complete Integration Guide

**Version:** 2.0 (Foundry Integration Complete)
**Last Updated:** January 2026

---

## Executive Summary

arche has evolved from a 4-mode framework to a comprehensive 5-mode evolutionary architecture with production-ready supporting systems. The framework now includes:

- **5 Architectural Modes** with explicit compatibility guidance
- **8 Agent Archetypes** providing reusable patterns
- **3 Domain Blueprints** (Incident Response, Content Moderation, Data Operations)
- **Migration Guides** for evolving agent capabilities
- **Upgrade Advisory System** for safe ecosystem evolution
- **Community Contribution Pathway** for ecosystem growth
- **Compatibility Checker Tool** for validation

This guide explains what's new, how everything fits together, and how to use these systems.

---

## What's New in arche 2.0

### 1. Foundry Mode (EMERGING)
**Purpose:** Meta-agent scaffolding for generating Multi-Agent Organizations

- Generates complete MAO structures with learning loops
- Provides agent templates, blueprints, and pattern library
- Individual agents use other 4 modes for implementation
- Enables rapid MAO composition

**Key Guides:**
- `modes/foundry/MODE.md` — Complete mode documentation
- `MODE_INTEGRATION_GUIDE.md` — How agents leverage other modes

### 2. Mode Compatibility Matrix
**Purpose:** Explicit guidance on combining modes strategically

- 5×5 compatibility matrix with color-coded confidence (🟢🟡🔴)
- 9 detailed pairing patterns with architectures
- 6 anti-patterns to avoid
- Migration paths for evolving agents

**Location:** `../frameworks/MODE_COMPATIBILITY.md`

### 3. Agent Archetypes Library
**Purpose:** Reusable agent patterns for common roles

- 8 core archetypes: Executor, Learner, Orchestrator, Monitor, Validator, Synthesizer, Router, Advisor
- Each includes: template directive, input/output spec, success metrics
- Mode recommendations for each archetype
- Real-world examples

**Location:** `../frameworks/AGENT_ARCHETYPES.md`

### 4. Domain Blueprints
**Purpose:** Production-ready MAO scaffolds for specific domains

**3 Initial Blueprints:**
- **BP-0003: Incident Response (ITIL-aligned)** — IT ops incident management with 5 agent roles, event-driven coordination, learning loop
- **BP-0004: Content Moderation** — Trust & Safety with classification, review coordination, feedback learning
- **BP-0005: Data Operations** — Data reliability engineering with pipeline monitoring, auto-remediation, analytics support

Each blueprint includes:
- Agent role definitions (referencing archetypes)
- Mode assignments (which modes used)
- Evaluation scenarios (how to test)
- Governance & escalation paths
- Learning system architecture
- SLA targets (where applicable)

**Location:** `blueprint-registry.md` + individual BP-XXXX.md files

### 5. Mode Migration Guide
**Purpose:** Step-by-step patterns for evolving agents between modes

**3 Migration Patterns Documented:**
- **3-Layer → RL-Loop** (Add Learning) — Rules to adaptive learning
- **3-Layer → Agentic-Swarm** (Add Specialization) — Monolithic to coordinated specialists
- **Event-Driven → Event-Driven + RL-Loop** (Add Learning) — Reactive with learned strategy

Each migration includes:
- Trigger conditions (when to migrate)
- Phased approach (analysis → setup → learning → transition → stabilize)
- Risk mitigation strategies
- Rollback plans

**Location:** `../frameworks/MODE_MIGRATION_GUIDE.md`

### 6. Upgrade Advisory System
**Purpose:** Safe, guided adoption of arche improvements

**4 Advisory Categories:**
- **CRITICAL** (Security/Compliance) — Must adopt within 7 days
- **RECOMMENDED** (Mode Enhancements) — Adopt within 2-4 weeks
- **OPTIONAL** (Archetypes/Blueprints) — Adopt at next update cycle
- **INFORMATIONAL** (Community Contributions) — For awareness

Each advisory includes:
- What changed and why
- Affected MAOs
- Action steps (with patch packs or migration guides)
- Rollback risk assessment
- Contact information

**Location:** `../frameworks/UPGRADE_ADVISORIES.md` (registry + individual ADV-XXXX.md files)

**Tool Support:** Create `upgrades-log.md` in your MAO to track adopted advisories

### 7. Community Contribution Pathway
**Purpose:** Enable community to extend arche with modes, archetypes, blueprints

**Contribution Types:**
- **New Mode** (5/5 complexity) — 3-6 month timeline
- **New Archetype** (3/5 complexity) — 2-4 week timeline
- **Domain Blueprint** (4/5 complexity) — 4-8 week timeline
- **Pattern/Example** (2/5 complexity) — 1-2 week timeline

**Process:**
1. Open GitHub issue (RFC-style proposal)
2. Community feedback (1-2 weeks)
3. Development phase (varies by type)
4. Implementation review (1 week)
5. Merge & release

**Location:** `../frameworks/COMMUNITY_CONTRIBUTION_PATHWAY.md`

### 8. Compatibility Checker Tool
**Purpose:** Validate mode combinations before implementation

**Usage:**
```bash
python arche-tools/arche_compat_check.py --modes 3-layer rl-loop agentic-swarm
python arche-tools/arche_compat_check.py --list
```

**Output:**
- Pairwise compatibility scores
- Known patterns for combination
- Warnings and risks
- Actionable recommendations
- Overall viability assessment

---

## Integration Points: How Everything Connects

```
User wants to build a Multi-Agent Organization
          ↓
    Choose a blueprint (from blueprint-registry.md)
    or design custom combination
          ↓
    Check compatibility (arche_compat_check.py)
          ↓
    Select agent archetypes for each role
    (from AGENT_ARCHETYPES.md)
          ↓
    Assign modes to each agent
    (using MODE_INTEGRATION_GUIDE.md)
          ↓
    Build agents using mode implementation
    (3-Layer, RL-Loop, Event-Driven, Agentic-Swarm)
          ↓
    Launch MAO with learning loops
          ↓
    Monitor and evaluate
          ↓
    Migrate agents as requirements evolve
    (using MODE_MIGRATION_GUIDE.md)
          ↓
    Apply upgrade advisories as arche evolves
    (track in upgrades-log.md)
```

---

## Getting Started: Three Paths

### Path 1: Use Existing Blueprint (Fastest)
**Timeline:** 2-4 weeks to prototype

1. **Choose blueprint:** Review `blueprint-registry.md` for your domain
2. **Study blueprint:** Read full BP-XXXX.md file
3. **Set up learning loop:** Copy learning loop templates from `modes/foundry/examples/minimal-mao/`
4. **Implement agents:** Use archetype templates from blueprint
5. **Evaluate:** Run eval scenarios defined in blueprint

**Example:** Building incident response system
- Use BP-0003 (ITIL-aligned)
- 5 agents: Alert Monitor, Incident Commander, Triage Analyzer, Knowledge Retriever, Execution Agent
- Modes: Event-Driven + Agentic-Swarm + RL-Loop + 3-Layer
- Success metrics: Severity assessment accuracy, MTTR, escalation appropriateness

### Path 2: Custom Mode Combination (Moderate)
**Timeline:** 4-8 weeks to production

1. **Identify requirements:** What problem does your MAO solve?
2. **Sketch agents:** What roles do you need?
3. **Check compatibility:** Use `arche_compat_check.py` on proposed modes
4. **Select archetypes:** Match archetypes to agent roles
5. **Design learning loop:** How will MAO improve over time?
6. **Build MAO:** Use archetype templates and mode guides

**Example:** E-commerce recommendation system
- Modes: RL-Loop (learning preferences) + 3-Layer (rules compliance) + Agentic-Swarm (coordination)
- Agents: Preference Learner (RL-Loop), Policy Validator (3-Layer), Recommendation Synthesizer (Agentic-Swarm)
- Learning: Implicit feedback from purchases, explicit feedback from ratings

### Path 3: Contribute to arche (Community)
**Timeline:** Varies, 2-6 months

1. **Identify gap:** Missing mode, archetype, blueprint, or pattern?
2. **Propose via GitHub:** Open RFC issue with community templates
3. **Gather feedback:** 1-2 weeks of discussion
4. **Develop contribution:** Build following arche standards
5. **Community review:** Share with early adopters
6. **Merge:** Contribution becomes part of arche

---

## Key Documents: Where to Find What

| Need | Document(s) | Purpose |
|------|-------------|---------|
| **Understand modes** | `MODE_SELECTION.md`, `modes/[mode]/MODE.md` | How each mode works |
| **Compare modes** | `MODE_SELECTION.md` (matrix), `MODE_COMPATIBILITY.md` | Which mode for my needs |
| **Combine modes** | `MODE_COMPATIBILITY.md`, `MODE_INTEGRATION_GUIDE.md` | Safe mode combinations |
| **See mode examples** | `modes/[mode]/examples/` | Working implementations |
| **Pick agent patterns** | `AGENT_ARCHETYPES.md` | Reusable agent templates |
| **Use existing blueprint** | `blueprint-registry.md`, `BP-XXXX.md` | Domain-specific scaffolds |
| **Design new MAO** | `FOUNDRY_QUICK_START.md`, learning loop templates | Getting started |
| **Set up feedback loops** | `FEEDBACK_SPECIFICATION.md` | What to collect and how |
| **Evolve agents** | `MODE_MIGRATION_GUIDE.md` | Migrating between modes |
| **Track updates** | `UPGRADE_ADVISORIES.md` | New features & changes |
| **Contribute** | `COMMUNITY_CONTRIBUTION_PATHWAY.md` | Extending arche |
| **Validate combination** | `arche_compat_check.py` | Check before building |
| **Understand framework improvements** | `../learning/FRAMEWORK_LEARNING_LOOP.md` | How arche improves |

---

## Feedback Loops: Making Everything Improve

arche is designed to improve continuously based on feedback from teams like yours. Here's how the system works:

### Your MAO's Learning Loop
1. **Collect:** Your agents log decisions, outcomes, errors → `09_learning/feedback-log.md`
2. **Analyze:** Weekly team review identifies patterns and improvement opportunities
3. **Improve:** Create change requests, test with eval scenarios, deploy improvements
4. **Share:** Monthly, submit feedback issues with `[FEEDBACK]` tag to help arche improve

See `../learning/FEEDBACK_SPECIFICATION.md` for detailed templates and what metrics matter for your agent types.

### arche's Learning Loop (Quarterly)
1. **Collect:** arche core team gathers feedback from all MAO teams and contributions
2. **Analyze:** Quarterly review identifies patterns (what's working, what's broken, what's missing)
3. **Improve:** Core team prioritizes improvements and implements changes
4. **Share:** Release upgrades advisories, updated blueprints, new tools
5. **Validate:** Teams adopt improvements, report back on effectiveness

See `../learning/FRAMEWORK_LEARNING_LOOP.md` for how arche's quarterly cycle works and how your feedback shapes improvements.

**The key:** Both your MAO and the framework improve together. Your feedback makes arche better for everyone. arche improvements make your MAO better through upgrades and new tools.

---


## Best Practices

### 1. Start with Blueprint or Pattern
Don't design from scratch unless truly novel. Reuse blueprints and archetypes.

### 2. Use Compatibility Checker
Before committing to mode combination, validate with `arche_compat_check.py`.

### 3. Plan Learning Loops
Every MAO needs feedback mechanism. Design learning loop upfront (don't add later).

**How:** Follow FEEDBACK_SPECIFICATION.md for what to collect, create `09_learning/feedback-log.md` in your MAO, and set up weekly reviews. See FEEDBACK_SPECIFICATION.md for templates and metrics by agent type.

### 4. Track Feedback & Report Learnings
Set up feedback collection in your MAO, analyze weekly, and share monthly learnings with arche community.

**How:** 
1. Implement decision feedback (every agent decision logged)
2. Implement outcome feedback (daily metrics)
3. Implement system feedback (errors/slowdowns)
4. Weekly: Review patterns in feedback-log
5. Monthly: Create GitHub issue with `[FEEDBACK]` tag to share learnings

See FEEDBACK_SPECIFICATION.md for detailed format and examples. Your feedback helps arche improve.

### 5. Document Mode Choices
Create `mode-selection-log.md` in your MAO explaining:
- Why each agent uses its assigned mode
- How modes interact
- When/how to revisit these decisions

### 6. Migrate Gradually
When changing modes (3-Layer → RL-Loop), follow phased approach from `../frameworks/MODE_MIGRATION_GUIDE.md`. Don't switch all at once.

### 7. Monitor Compatibility
As MAO grows, periodically re-run compatibility checker. New agents may create unexpected interactions.

### 8. Track Upgrades
Create `upgrades-log.md` in MAO to document:
- Which advisories you've adopted
- When you adopted them
- Any custom modifications

### 9. Share Learnings
If you solve a problem or find a useful pattern, propose it as community contribution. This makes arche better for everyone.

---

## Governance: Responsibility Matrix

| Entity | Responsibility |
|--------|-----------------|
| **arche Core Team** | Maintain framework docs, review contributions, release advisories, manage registries |
| **Mode Maintainers** | Keep mode docs current, support users, propose improvements |
| **Blueprint Authors** | Update blueprints with learnings, monitor for compatibility issues |
| **MAO Teams** | Apply advisories on schedule, document choices, share learnings |
| **Community** | Propose contributions, participate in reviews, help each other |

---

## Evolution Roadmap

### Near Term (Q1 2026)
- ✅ Foundry mode integration complete
- ✅ Mode compatibility matrix published
- ✅ 8 agent archetypes defined
- ✅ 3 domain blueprints launched
- ✅ Migration guides available
- ✅ Upgrade advisory system operational
- ✅ Community contribution pathway documented

### Medium Term (Q2-Q3 2026)
- 🚀 First community contributions (new archetypes, blueprints)
- 🚀 Health check system for deployed MAOs
- 🚀 Compatibility checker enhancements (YAML config support)
- 🚀 Migration optimization scripts
- 🚀 More domain blueprints (5+ total)

### Long Term (Q4 2026+)
- 🔮 Real-time arche marketplace for blueprints/patterns
- 🔮 Community-maintained arche distributions
- 🔮 Mode maturity progression (Emerging → Mature → Stable)
- 🔮 Research mode (experimental architectures)
- 🔮 Integration with popular frameworks (LangChain, AutoGen, etc.)

---

## FAQ

**Q: Do I have to use all 5 modes?**
A: No. Use only modes that fit your needs. Single-mode MAOs are common and perfectly valid.

**Q: Can I combine all 5 modes in one MAO?**
A: Yes, but it's rare and complex. Use compatibility checker to assess. Usually 2-3 modes optimal.

**Q: What if a blueprint doesn't match my domain perfectly?**
A: Start with closest blueprint, modify agents/roles to fit, run eval scenarios, and iterate. Feedback helps improve blueprints.

**Q: How often should I check upgrade advisories?**
A: Weekly is ideal. Set calendar reminder or follow GitHub. CRITICAL advisories are usually announced loudly (email/Slack).

**Q: Can I skip a non-CRITICAL advisory?**
A: Yes. RECOMMENDED and OPTIONAL advisories are your choice. Skip if timing bad or not applicable. But review quarterly to catch important improvements.

**Q: Where do I ask for help?**
A: GitHub discussions, open issues, community calls, or direct contact with core team. arche has an active community.

**Q: How is arche different from competing frameworks?**
A: arche is explicitly evolutionary, not prescriptive. We provide modes + patterns + community, not one "right way." You compose what you need.

---

## Contacts & Resources

- **GitHub:** [arche repo]
- **Discussions:** GitHub discussions on arche repo
- **Community Calls:** [Scheduled time TBD]
- **Documentation:** This guide + all linked `.md` files
- **Issue Templates:** GitHub issue templates for mode proposals, archetypes, blueprints

---

## What's Next?

1. **Understand your needs:** What problem does your MAO solve?
2. **Choose your path:** Blueprint? Custom combination? Contributing?
3. **Validate early:** Use compatibility checker before deep investment
4. **Build with patterns:** Leverage archetypes and mode guides
5. **Learn and iterate:** Evaluate with scenarios, migrate if needed
6. **Share back:** Contribute patterns, blueprints, learnings to community

Welcome to arche 2.0. Let's build better agent systems together.

---

