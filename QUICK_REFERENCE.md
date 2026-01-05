# arche 2.0: Quick Reference Card

## What's New?

| Component | Purpose | Key Content |
|-----------|---------|-------------|
| **MODE_COMPATIBILITY.md** | Safe mode combinations | 5×5 matrix, 9 patterns, anti-patterns |
| **AGENT_ARCHETYPES.md** | Reusable agent patterns | 8 archetypes with templates & metrics |
| **BP-0003, BP-0004, BP-0005** | Domain blueprints | Production-ready MAO scaffolds |
| **MODE_MIGRATION_GUIDE.md** | Evolve agents safely | 3 migration patterns with phases |
| **UPGRADE_ADVISORIES.md** | Safe ecosystem evolution | Advisory system + registry |
| **COMMUNITY_CONTRIBUTION_PATHWAY.md** | Extend arche | RFC process for modes/archetypes/blueprints |
| **arche_compat_check.py** | Validate combinations | CLI tool to check mode viability |
| **ARCHE_INTEGRATION_GUIDE.md** | Comprehensive overview | How everything connects |

---

## Three Paths to Get Started

### 🎯 Path 1: Use Existing Blueprint (Fastest)
**Timeline:** 2-4 weeks
```
1. Read blueprint-registry.md
2. Pick blueprint (BP-0003, BP-0004, or BP-0005)
3. Use agent templates from blueprint
4. Implement with suggested modes
5. Run eval scenarios
```

### 🔧 Path 2: Custom Mode Combination (Moderate)
**Timeline:** 4-8 weeks
```
1. Identify agents you need
2. Check compatibility: python arche_compat_check.py --modes [list]
3. Select archetypes for each agent
4. Design learning loop
5. Build MAO following mode guides
```

### 🤝 Path 3: Contribute to arche (Community)
**Timeline:** 2-6 months
```
1. Identify gap (new mode/archetype/blueprint)
2. Open GitHub RFC issue
3. Get community feedback
4. Develop contribution
5. Submit for review
6. Merge to arche
```

---

## 8 Agent Archetypes at a Glance

| Archetype | Best Mode | Use Case | Example |
|-----------|-----------|----------|---------|
| **Executor** | 3-Layer | Deterministic tasks | Database query executor |
| **Learner** | RL-Loop | Adaptive strategy | Content preference learner |
| **Orchestrator** | Agentic-Swarm | Coordinating multiple agents | Chief reviewer coordination |
| **Monitor** | Event-Driven | Reactive monitoring | Alert detector |
| **Validator** | 3-Layer | Quality checks | Policy compliance validator |
| **Synthesizer** | 3-Layer/Agentic-Swarm | Combining outputs | Recommendation synthesizer |
| **Router** | 3-Layer/RL-Loop | Smart routing | Content category router |
| **Advisor** | RL-Loop/3-Layer | Recommendations | Health recommendations |

---

## 3 Domain Blueprints Ready to Use

### 📊 BP-0003: Incident Response (ITIL-aligned)
- **Agents:** Alert Monitor, Incident Commander, Triage Analyzer, Knowledge Retriever, Execution Agent
- **Modes:** Event-Driven + Agentic-Swarm + 3-Layer + RL-Loop
- **SLA:** Severity assessment in <5min, escalation in <15min
- **Eval Scenarios:** Infrastructure check, Multi-component failure, Alert fatigue

### 🛡️ BP-0004: Content Moderation
- **Agents:** Content Intake, Policy Classifier, Review Coordinator, Reviewer Interface, Feedback Processor
- **Modes:** Event-Driven + 3-Layer + RL-Loop + Agentic-Swarm
- **Learning:** Classification accuracy, reviewer consistency, appeal minimization
- **Eval Scenarios:** Clear violation, Ambiguous case, Pattern detection

### 📈 BP-0005: Data Operations
- **Agents:** Pipeline Monitor, Issue Triage, Auto-Remediation, Analytics Support, Knowledge Manager
- **Modes:** Event-Driven + 3-Layer + RL-Loop + Agentic-Swarm
- **SLA:** <5min detection, <15min diagnosis, <30min auto-fix
- **Eval Scenarios:** Late arrival, Quality degradation, Performance degradation

---

## Mode Compatibility Quick Check

**Excellent Combinations (✅):**
- 3-Layer + RL-Loop (rules + learning)
- 3-Layer + Agentic-Swarm (specialist teams)
- 3-Layer + Event-Driven (event handlers)
- 3-Layer + Foundry (scaffold generation)
- Event-Driven + Agentic-Swarm (reactive coordination)

**Good Combinations (✓):**
- RL-Loop + Event-Driven (reactive learning)
- RL-Loop + 3-Layer (fallback)
- Agentic-Swarm + 3-Layer (hierarchical)
- Event-Driven + Event-Driven (cascading)

**Caution Combinations (⚠️):**
- RL-Loop + Agentic-Swarm (coordination overhead, test carefully)
- Agentic-Swarm + Agentic-Swarm (meta-coordination, rare)

**Avoid (❌):**
- Foundry + Foundry (use Foundry once at top level only)

**See MODE_COMPATIBILITY.md for full matrix and patterns**

---

## Three Migration Patterns

### 1️⃣ 3-Layer → RL-Loop (Add Learning)
**When:** Rules-based strategy needs to become adaptive
**Duration:** 6-8 weeks (phased)
**Risk:** Low (keep 3-Layer as fallback)
**Example:** Content router (hardcoded rules → learned preferences)

### 2️⃣ 3-Layer → Agentic-Swarm (Add Specialization)
**When:** Single agent becomes too complex
**Duration:** 6-8 weeks (specialist design + coordination)
**Risk:** Low (coordination can be refined)
**Example:** Single reviewer → Chief Reviewer + 4 specialists

### 3️⃣ Event-Driven → + RL-Loop (Add Learning)
**When:** Event handlers should learn optimal strategy
**Duration:** 4-6 weeks
**Risk:** Very low (opt-in learning)
**Example:** Alert severity assessment (rules → learned)

**See MODE_MIGRATION_GUIDE.md for detailed 5-phase approach**

---

## Upgrade Advisory Timeline

| Severity | Timeline | Action | Example |
|----------|----------|--------|---------|
| 🔴 CRITICAL | 1-7 days | Must adopt | Security vulnerability |
| 🟡 RECOMMENDED | 2-4 weeks | Evaluate & adopt | Mode enhancement, performance |
| 🟢 OPTIONAL | 1-3 months | Consider next cycle | New archetype, blueprint |

**Track in MAO with `upgrades-log.md`**

---

## Compatibility Checker Tool

```bash
# Check if combination is viable
python arche_compat_check.py --modes 3-layer rl-loop agentic-swarm

# List available modes
python arche_compat_check.py --list

# Integration
python arche_compat_check.py --config mao-config.yaml  # Future
```

**Output includes:**
- Pairwise compatibility scores
- Known patterns & anti-patterns
- Warnings & risks
- Actionable recommendations
- Exit codes for CI/CD

---

## Community Contribution Process

### Propose Contribution
1. Open GitHub issue (use RFC template)
2. Title: "RFC: [Mode/Archetype/Blueprint Name]"
3. Include: Problem, Solution, Use Cases, Timeline

### Community Review
- Comment period: 1-2 weeks
- Feedback integrated
- Proposal refined

### Development
- **New Mode:** 8-12 weeks
- **New Archetype:** 1-2 weeks
- **New Blueprint:** 2-4 weeks
- **Pattern/Example:** 1 week

### Review & Merge
- Implementation review (1 week)
- Community sign-off
- Merged to main
- Added to registries

**See COMMUNITY_CONTRIBUTION_PATHWAY.md for templates & details**

---

## Essential Documents Map

```
Start here →  ARCHE_INTEGRATION_GUIDE.md
              ├─ Pick your path (Blueprint/Custom/Contribute)
              │
              ├─ Path 1: Use Blueprint
              │  └─ blueprint-registry.md → BP-XXXX.md
              │
              ├─ Path 2: Custom Combination
              │  ├─ AGENT_ARCHETYPES.md (pick patterns)
              │  ├─ MODE_COMPATIBILITY.md (validate)
              │  ├─ arche_compat_check.py (autocheck)
              │  └─ MODE_INTEGRATION_GUIDE.md (implement)
              │
              ├─ Evolve Agents
              │  └─ MODE_MIGRATION_GUIDE.md
              │
              ├─ Track Updates
              │  └─ UPGRADE_ADVISORIES.md
              │
              └─ Contribute
                 └─ COMMUNITY_CONTRIBUTION_PATHWAY.md
```

---

## Best Practices Checklist

- [ ] Validate with `arche_compat_check.py` before building
- [ ] Create `mode-selection-log.md` explaining mode choices
- [ ] Design learning loop upfront (don't add later)
- [ ] Start with blueprint if one fits your domain
- [ ] Use archetype templates for agent directives
- [ ] Plan migrations gracefully (5-phase approach)
- [ ] Track upgrade adoption in `upgrades-log.md`
- [ ] Share learnings back to community

---

## FAQ One-Liners

**Q: Do I have to use all 5 modes?**
A: No. Use only what you need. Single-mode MAOs are common.

**Q: Can I combine all 5 modes in one MAO?**
A: Possible but rare. Use compatibility checker to assess.

**Q: What if a blueprint doesn't match exactly?**
A: Start with it, modify to fit, run eval scenarios, iterate.

**Q: How often should I check for upgrade advisories?**
A: Weekly is ideal. Critical advisories are announced prominently.

**Q: Where do I ask for help?**
A: GitHub discussions, issues, or contact core team.

**Q: Can I contribute without being on the core team?**
A: Absolutely. Community contributions are encouraged.

---

## Key Metrics

| Metric | Before | After |
|--------|--------|-------|
| **Lines of guidance** | ~2,000 | ~5,000 |
| **Mode combinations documented** | 0 | 15 (5×5 matrix) |
| **Agent patterns available** | ~2 | 8 archetypes |
| **Domain starting points** | 0 | 3 blueprints |
| **Migration paths documented** | 0 | 3 patterns |
| **Tool support** | None | Compatibility checker |
| **Upgrade system** | Ad-hoc | Formal advisory system |
| **Community pathway** | Unclear | Documented RFC process |

---

## Next Steps

1. **Read:** ARCHE_INTEGRATION_GUIDE.md (15 min)
2. **Choose:** Pick your path (Blueprint/Custom/Contribute)
3. **Validate:** Use arche_compat_check.py if custom
4. **Build:** Follow mode guides and archetype templates
5. **Evaluate:** Run eval scenarios
6. **Share:** Contribute learnings back

---

## Resources

- **Main Guide:** ARCHE_INTEGRATION_GUIDE.md
- **Completion Details:** COMPLETION_SUMMARY.md
- **GitHub:** [arche repository]
- **Discussions:** GitHub discussions tab
- **Issues:** GitHub issues (RFC templates available)

---

**Version:** arche 2.0 | **Status:** Production Ready | **Last Updated:** January 2026

