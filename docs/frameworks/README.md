# Frameworks: Core arche Architecture

**Understanding modes, agents, and how to compose them.**

---

## 📚 Quick Navigation

| Document | Purpose |
|----------|---------|
| **MODE_COMPATIBILITY.md** | 5×5 matrix of mode combinations |
| **AGENT_ARCHETYPES.md** | 8 reusable agent patterns |
| **MODE_MIGRATION_GUIDE.md** | Evolve MAOs between modes |
| **UPGRADE_ADVISORIES.md** | Manage framework evolution |
| **COMMUNITY_CONTRIBUTION_PATHWAY.md** | Add to arche frameworks |

---

## 🎯 Core Concepts

### 4 Architectural Modes

1. **3-Layer** - Deterministic, rule-based execution
2. **RL-Loop** - Learning from outcomes, improving decisions
3. **Event-Driven** - Reactive, asynchronous processing
4. **Agentic-Swarm** - Multi-agent coordination and debate

### 8 Agent Archetypes

Reusable patterns for specific roles:
1. **Executor** - Carries out decisions
2. **Learner** - Captures and applies learnings
3. **Orchestrator** - Coordinates multiple agents
4. **Monitor** - Watches for issues
5. **Validator** - Checks decisions against rules
6. **Synthesizer** - Combines multiple inputs
7. **Router** - Directs work to appropriate handler
8. **Advisor** - Provides guidance/recommendations

---

## 📋 Documents

### MODE_COMPATIBILITY.md
**Can I combine modes? When?**
- 5×5 compatibility matrix
- 9 pairing patterns (which work well together)
- 6 anti-patterns (avoid these)
- Migration paths between modes
- Real-world examples

### AGENT_ARCHETYPES.md
**8 reusable agent patterns**
- Template for each archetype
- Metrics and success criteria
- Mode recommendations
- Real-world applications
- Anti-patterns (what to avoid)

### MODE_MIGRATION_GUIDE.md
**Evolve your MAO over time**
- 3 detailed migration patterns
- Phased 5-7 step approaches
- Risk mitigation strategies
- Testing and validation
- Rollback procedures

### UPGRADE_ADVISORIES.md
**Managing framework evolution**
- 4 advisory categories (CRITICAL, RECOMMENDED, OPTIONAL, INFORMATIONAL)
- Lifecycle guidance
- Deprecation process
- Migration timelines
- Advisory registry

### COMMUNITY_CONTRIBUTION_PATHWAY.md
**Add to arche frameworks**
- RFC process for proposals
- 4 contribution types (blueprints, archetypes, patterns, modes)
- Review and acceptance criteria
- Timelines (1 week to 6 months)
- Maintenance expectations

---

## 🔄 Mode Selection

**Choose based on your problem:**

| Problem | Recommended Mode |
|---------|------------------|
| Clear rules, deterministic flow | 3-Layer |
| Need to improve from outcomes | RL-Loop |
| Respond to events in real-time | Event-Driven |
| Complex coordination, debates | Agentic-Swarm |
| Multiple concurrent processes | Event-Driven + Agentic-Swarm |
| Learning + deterministic | 3-Layer + RL-Loop |

---

## 🎓 Usage Path

1. **Understanding modes** → Read MODE_COMPATIBILITY.md
2. **Building MAO** → Reference AGENT_ARCHETYPES.md
3. **Growing MAO** → Use MODE_MIGRATION_GUIDE.md
4. **Contributing** → Follow COMMUNITY_CONTRIBUTION_PATHWAY.md

---

## 📊 Status

✅ MODE_COMPATIBILITY.md - Complete with 9 pairing patterns  
✅ AGENT_ARCHETYPES.md - Complete with 8 archetypes + templates  
✅ MODE_MIGRATION_GUIDE.md - Complete with 3 migration patterns  
✅ UPGRADE_ADVISORIES.md - Complete with lifecycle governance  
✅ COMMUNITY_CONTRIBUTION_PATHWAY.md - Complete with RFC process

---

## Examples

See also: **blueprints/** for concrete implementations
- BP-0003: Incident Response (Event-Driven + Agentic-Swarm + 3-Layer + RL-Loop)
- BP-0004: Content Moderation (Agentic-Swarm + RL-Loop)
- BP-0005: Data Operations (3-Layer + RL-Loop)

---

## Next Steps

1. **Understand your mode choice** → MODE_COMPATIBILITY.md
2. **Pick agent patterns** → AGENT_ARCHETYPES.md
3. **Build your MAO** → See blueprints/ for examples
4. **Plan evolution** → MODE_MIGRATION_GUIDE.md if you'll grow

---

