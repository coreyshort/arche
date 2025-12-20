# Arche: Evolutionary Framework for Agentic Systems

**arche** is named after the ancient Greek concept of *archē*—the first principle, origin, or underlying cause from which things come into being.

In philosophy, the archē is not a thing but a generative source: the set of assumptions, structures, and forces that make creation possible. Arche exists in that same spirit. It is not an agent or a single architecture, but the **evolutionary framework** from which agentic systems emerge—defining how intent becomes action, how reasoning is shaped, and how systems learn to build themselves.

**Arche doesn't prescribe one approach.** It provides a foundation for multiple modes of agentic development, each suited to different paradigms. As the world of agents evolves, new modes emerge independently based on market and industry evolution.

**Modes have maturity levels** that evolve as they gain adoption and stability. See [MODE_MATURITY.md](MODE_MATURITY.md) for the maturity model.

**Choosing a mode?** See [MODE_SELECTION.md](MODE_SELECTION.md) for detailed guidance on which mode fits your project.

---

## Modes: Multiple Paradigms, One Foundation

Arche supports different **modes**—fundamental architectural approaches for building agentic systems. Each mode addresses different problems and fits different use cases.

### ✅ 3-Layer Mode (Mature)

**Paradigm:** Deterministic execution with AI orchestration  
**Best for:** Reliability-critical projects, data processing, automation  
**Maturity:** Mature - 50+ production projects, battle-tested patterns, stable ecosystem

[Learn about 3-layer mode →](modes/3-layer/MODE.md)

---

### � Agentic Swarm Mode (Emerging)

**Paradigm:** Multi-agent coordination and collaboration  
**Best for:** Complex systems requiring specialized agents working together  
**Maturity:** Emerging - Patterns being discovered in production, structure being shaped

[Learn about agentic-swarm mode →](modes/agentic-swarm/MODE.md)

---

### 🚀 Event-Driven Mode (Emerging)

**Paradigm:** Reactive agents responding to event streams  
**Best for:** Real-time systems, webhooks, message queues, IoT  
**Maturity:** Emerging - Patterns being discovered in production, structure being shaped

[Learn about event-driven mode →](modes/event-driven/MODE.md)

---

### 🚀 Reinforcement Learning Loop Mode (Emerging)

**Paradigm:** Agents learning from outcomes over time  
**Best for:** Optimization, personalization, adaptive systems  
**Maturity:** Emerging - Patterns being discovered in production, structure being shaped

[Learn about rl-loop mode →](modes/rl-loop/MODE.md)

---

## The Philosophy

**Arche improves through use.** Every project built with arche discovers new patterns, edge cases, and better approaches. These learnings flow back through GitHub Issues, making the framework stronger for everyone.

**Modes evolve independently.** As agent paradigms mature in production, new modes emerge. The framework doesn't dictate architecture—it captures what works in practice.

**A virtuous circle.** When arche helps you build something valuable, others could benefit too. If you discover ways to help more people find it—clearer documentation, better examples, thoughtful writing about your experience—those contributions strengthen the whole ecosystem.

---

## Quick Start

### For 3-Layer Mode Projects

**Simplest start (1 minute):**

Tell your AI assistant to follow the 3-layer mode:
```
Follow the 3-layer mode: https://raw.githubusercontent.com/coreyshort/arche/main/modes/3-layer/INSTRUCTIONS.md
```

**Model-agnostic:** Works with Claude, ChatGPT, Copilot, Gemini, and any future AI.

**Let AI select mode autonomously:**

AI agents can analyze your project and select the appropriate mode without human intervention:
```
Initialize an arche project for: [describe your project]
Use the autonomous mode selection algorithm to choose the best mode.
```

The AI will analyze requirements, score modes, and bootstrap with the optimal choice. See [AUTONOMOUS_MODE_SELECTION.md](AUTONOMOUS_MODE_SELECTION.md).

**Full project setup (5 minutes):**

```bash
# Download bootstrap script
curl -O https://raw.githubusercontent.com/coreyshort/arche/main/tools/bootstrap.py

# Interactive setup
python bootstrap.py --interactive

# Or direct initialization
python bootstrap.py --mode 3-layer --form automation --target my-project
```

See [3-layer mode documentation](modes/3-layer/MODE.md) for details.

---

### For Other Modes

**Emerging modes** (agentic-swarm, event-driven, rl-loop) are in active development. If you're working with these paradigms:

1. Read the mode documentation to understand the approach
2. Build using those patterns
3. **Contribute your learnings** through GitHub Issues
4. Help shape these modes as they mature

The framework evolves through real-world usage.

---

## Forms Within Modes

Each mode can contain multiple **forms**—specific project templates for different use cases.

**3-layer mode forms:**
- `automation` - Data processing, ETL, scraping
- `webapp-fullstack` - Full-stack web applications
- `webapp-frontend` - Frontend-only SPAs
- `api-service` - Backend APIs and microservices
- `data-science` - ML workflows and analysis
- `cli-tool` - Command-line applications
- `library` - Reusable packages

**Other modes** will develop forms as patterns emerge from production use.

---

## Contributing

### Improving Existing Modes

Discovered a better pattern? Found an edge case? Create a GitHub Issue:

https://github.com/coreyshort/arche/issues

Include:
- Which mode and form (if applicable)
- The pattern or problem
- Proposed solution with implementation details
- Testing approach

### Proposing New Modes

See an emerging paradigm not captured by existing modes? Propose it:

1. Create a GitHub Issue describing the paradigm
2. Explain what problems it solves
3. Share production examples demonstrating the pattern
4. Propose initial structure and principles

**New modes must emerge from real-world production use**, not theoretical possibilities. They require demonstrated patterns that work reliably.

---

## The Self-Annealing System

**Within your project:**
Fix → Test → Document → System stronger

**Across the ecosystem:**
Discover → Share → Merge → Everyone benefits

This feedback loop is mandatory, not optional. It's the engine that makes arche evolve.

---

## Why Multiple Modes?

The world of agentic systems is evolving rapidly. Different problems require different architectures:

- **Reliability-critical work** needs deterministic execution (3-layer)
- **Complex coordination** needs multi-agent collaboration (agentic-swarm)
- **Reactive systems** need event-driven patterns (event-driven)
- **Adaptive systems** need learning loops (rl-loop)

**Arche doesn't force one approach.** It provides a foundation where multiple modes can coexist, evolve independently, and be selected based on the problem at hand.

As new paradigms emerge—agent mesh networks, quantum-enhanced reasoning, biological computing patterns—they can become modes within arche.

---

## Links

- **Repository:** https://github.com/coreyshort/arche
- **Issues & Contributions:** https://github.com/coreyshort/arche/issues
- **Discussions:** https://github.com/coreyshort/arche/discussions

---

## Forms

In Aristotelian philosophy, a form is the organizing principle that makes a thing what it is—distinct from its material, yet inseparable from its realization. A form defines structure, purpose, and potential without prescribing a single instantiation.

In Arche, both **Modes** and **Forms** serve this role at different levels:

- **Modes** are architectural forms—fundamental paradigms for how agents reason and act
- **Forms within modes** are project forms—specific templates for common use cases

When you instantiate from arche, you're not copying a template. You're expressing a form—carrying forward principles that define how your system should reason, act, and evolve.

---

*An evolutionary framework for agentic systems*
