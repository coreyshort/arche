# Modes: Architectural Paradigms for Agentic Systems

**Foundation documents and specifications for the 4 core modes and how to choose between them.**

---

## 📚 Quick Navigation

| Your Goal | Read | Time |
|-----------|------|------|
| **Choose a mode for my MAO** | [MODE_SELECTION.md](MODE_SELECTION.md) | 15 min |
| **AI: Autonomous mode selection** | [AUTONOMOUS_MODE_SELECTION.md](AUTONOMOUS_MODE_SELECTION.md) | 5 min |
| **Understand mode maturity** | [MODE_MATURITY.md](MODE_MATURITY.md) | 10 min |
| **Deep dive into a specific mode** | [3-layer/](3-layer/), [rl-loop/](rl-loop/), [event-driven/](event-driven/), [agentic-swarm/](agentic-swarm/) | Varies |

---

## 🎯 The 4 Modes

### ✅ 3-Layer Mode (Mature)

**Paradigm:** Deterministic execution with AI orchestration

- Best for: Reliability-critical, data processing, automation
- Maturity: Mature - battle-tested in 50+ production projects
- Documentation: [3-layer/MODE.md](3-layer/MODE.md)
- Forms: CLI tools, APIs, libraries, data science, web apps

**When to use:** You need predictable, testable workflows

---

### 🚀 Agentic Swarm Mode (Emerging)

**Paradigm:** Multi-agent coordination and collaboration

- Best for: Complex systems, specialized agents working together
- Maturity: Emerging - patterns being discovered in production
- Documentation: [agentic-swarm/MODE.md](agentic-swarm/MODE.md)

**When to use:** Multiple agents need to coordinate and debate

---

### 🚀 Event-Driven Mode (Emerging)

**Paradigm:** Reactive agents responding to event streams

- Best for: Real-time systems, webhooks, message queues, IoT
- Maturity: Emerging - patterns being discovered in production
- Documentation: [event-driven/MODE.md](event-driven/MODE.md)

**When to use:** Your system reacts to continuous event streams

---

### 🚀 Reinforcement Learning Loop Mode (Emerging)

**Paradigm:** Agents learning from outcomes over time

- Best for: Optimization, personalization, adaptive systems
- Maturity: Emerging - patterns being discovered in production
- Documentation: [rl-loop/MODE.md](rl-loop/MODE.md)

**When to use:** Your system should improve from outcomes

---

## 📖 Core Documents

### [MODE_SELECTION.md](MODE_SELECTION.md)
**Choose the right mode for your needs**

- 30-second decision tree
- Comprehensive mode comparison matrix
- Real-world use cases
- Decision framework (requirements vs mode fit)
- Common mistakes to avoid
- Timeline and effort estimates

**Read this if:** You're deciding which mode to use

---

### [AUTONOMOUS_MODE_SELECTION.md](AUTONOMOUS_MODE_SELECTION.md)
**Algorithm for AI agents to select modes programmatically**

- Mode scoring algorithm
- Requirements analysis framework
- Tie-breaking rules (favor maturity)
- Example decisions
- Integration points

**Read this if:** You're building an AI system to choose modes

---

### [MODE_MATURITY.md](MODE_MATURITY.md)
**Understand how modes evolve through maturity stages**

- Maturity levels: 🌱 Proposed → ✅ Mature
- Stability and production readiness criteria
- How adoption affects maturity
- Release schedule for mode improvements
- Breaking changes policy

**Read this if:** You want to understand mode stability and roadmap

---

## 🏗️ Mode Specifications

Each mode has its own directory with complete documentation:

```
modes/
├── 3-layer/
│   ├── MODE.md (overview & architecture)
│   ├── INSTRUCTIONS.md (how to build)
│   ├── forms/ (5 ready-made structures)
│   │   ├── api-service/
│   │   ├── cli-tool/
│   │   ├── library/
│   │   ├── data-science/
│   │   └── webapp-fullstack/
│   └── _shared/ (utilities & reference)
│
├── rl-loop/
│   ├── MODE.md (overview & architecture)
│   └── ...
│
├── event-driven/
│   ├── MODE.md (overview & architecture)
│   └── ...
│
└── agentic-swarm/
    ├── MODE.md (overview & architecture)
    └── ...
```

**To use a mode:**
1. Read [MODE_SELECTION.md](MODE_SELECTION.md) to understand the paradigm
2. Read the mode's MODE.md for detailed architecture
3. Follow INSTRUCTIONS.md for implementation
4. Choose a form or create a custom structure

---

## 🔗 Related Documentation

- **[../../docs/frameworks/MODE_COMPATIBILITY.md](../../docs/frameworks/MODE_COMPATIBILITY.md)** — Can I combine modes? When should I?
- **[../../blueprints/](../../blueprints/)** — Production-ready MAOs using these modes
- **[../../docs/getting-started/CHOOSE_YOUR_PATH.md](../../docs/getting-started/CHOOSE_YOUR_PATH.md)** — Learning paths for different users
- **[../../README.md](../../README.md)** — Project philosophy and overview

---

## 🚀 Quick Start by Mode

**Want to start immediately?**

### Using 3-Layer Mode
1. Pick a form: [3-layer/forms/](3-layer/forms/)
2. Read: [3-layer/INSTRUCTIONS.md](3-layer/INSTRUCTIONS.md)
3. Start building!

### Using RL-Loop Mode
1. Understand feedback loops: [../../docs/learning/FEEDBACK_SPECIFICATION.md](../../docs/learning/FEEDBACK_SPECIFICATION.md)
2. Read: [rl-loop/MODE.md](rl-loop/MODE.md)
3. Design your learning pipeline

### Using Event-Driven Mode
1. Design your event schema
2. Read: [event-driven/MODE.md](event-driven/MODE.md)
3. Setup event sources and handlers

### Using Agentic Swarm Mode
1. Define your agents
2. Read: [agentic-swarm/MODE.md](agentic-swarm/MODE.md)
3. Design coordination patterns

---

## 📊 Mode Comparison at a Glance

| Aspect | 3-Layer | RL-Loop | Event-Driven | Agentic Swarm |
|--------|---------|---------|--------------|---------------|
| **Maturity** | ✅ Mature | 🚀 Emerging | 🚀 Emerging | 🚀 Emerging |
| **Determinism** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Scalability** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Complexity** | Low | Medium | Medium | High |
| **Team Size** | 1-3 | 2-4 | 2-5 | 3-6 |
| **Typical Duration** | Weeks | Weeks-Months | Weeks | Months |

---

## ❓ Common Questions

**Q: Can I combine modes?**  
A: Yes! See [../../docs/frameworks/MODE_COMPATIBILITY.md](../../docs/frameworks/MODE_COMPATIBILITY.md) for pairing patterns.

**Q: Can I switch modes later?**  
A: Yes, with planning. See [../../docs/frameworks/MODE_MIGRATION_GUIDE.md](../../docs/frameworks/MODE_MIGRATION_GUIDE.md).

**Q: Which mode is "best"?**  
A: There is no best mode—only the right mode for your problem. Use [MODE_SELECTION.md](MODE_SELECTION.md) to decide.

**Q: What if my use case doesn't fit?**  
A: Propose a new mode! See [../../docs/frameworks/COMMUNITY_CONTRIBUTION_PATHWAY.md](../../docs/frameworks/COMMUNITY_CONTRIBUTION_PATHWAY.md).

**Q: How do modes evolve?**  
A: See [MODE_MATURITY.md](MODE_MATURITY.md) for the evolutionary path.

---

## 🎓 Learning Path by Role

**Product Manager** → Start with [MODE_SELECTION.md](MODE_SELECTION.md)  
**Engineer** → Start with [3-layer/INSTRUCTIONS.md](3-layer/INSTRUCTIONS.md) or [MODE_SELECTION.md](MODE_SELECTION.md)  
**Data Scientist** → Look at [3-layer/forms/data-science/](3-layer/forms/data-science/)  
**AI Researcher** → Deep dive: [RL-Loop Mode](rl-loop/MODE.md), [Event-Driven Mode](event-driven/MODE.md), [Agentic Swarm](agentic-swarm/MODE.md)  
**DevOps/Platform** → [Event-Driven](event-driven/MODE.md), [Agentic Swarm](agentic-swarm/MODE.md)  
**AI Agent** → Use [AUTONOMOUS_MODE_SELECTION.md](AUTONOMOUS_MODE_SELECTION.md)

---

## 🔄 Mode Evolution

Modes follow a maturity progression:

```
🌱 Proposed     → Conceptual, not yet in arche
📋 Planned      → Scheduled for development
🚀 Emerging     → In production, patterns being discovered
✅ Mature       → Battle-tested, stable ecosystem
📦 Stable       → Frozen (no breaking changes)
🏚️ Legacy       → Deprecated but supported
```

Current status:
- **Mature:** 3-Layer
- **Emerging:** RL-Loop, Event-Driven, Agentic-Swarm
- **Planned:** Streaming, Hierarchical, Reflective

See [MODE_MATURITY.md](MODE_MATURITY.md) for details.

---

## 📞 Need Help?

- **Choosing a mode?** → [MODE_SELECTION.md](MODE_SELECTION.md)
- **Understanding maturity?** → [MODE_MATURITY.md](MODE_MATURITY.md)
- **Building your MAO?** → Mode-specific INSTRUCTIONS.md files
- **Combining modes?** → [../../docs/frameworks/MODE_COMPATIBILITY.md](../../docs/frameworks/MODE_COMPATIBILITY.md)
- **Contributing?** → [../../docs/frameworks/COMMUNITY_CONTRIBUTION_PATHWAY.md](../../docs/frameworks/COMMUNITY_CONTRIBUTION_PATHWAY.md)

---

**Last updated:** January 2026  
**Status:** Stable
