# Arche: Evolutionary Framework for Agentic Systems

![License](https://img.shields.io/github/license/coreyshort/arche)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-active-success)

**🤖 For AI Agents:** Start with [AI_QUICKSTART.md](AI_QUICKSTART.md) (2 min read, navigation map included)

**📋 Not sure where to start?** See [docs/getting-started/CHOOSE_YOUR_PATH.md](docs/getting-started/CHOOSE_YOUR_PATH.md) for a guided path selection

**⬆️ Upgrading from v1.x?** See [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) — v2.0.0 is backwards compatible, no code changes needed

---

**arche** is named after the ancient Greek concept of *archē*—the first principle, origin, or underlying cause from which things come into being.

In philosophy, the archē is not a thing but a generative source: the set of assumptions, structures, and forces that make creation possible. Arche exists in that same spirit. It is not an agent or a single architecture, but the **evolutionary framework** from which agentic systems emerge—defining how intent becomes action, how reasoning is shaped, and how systems learn to build themselves.

**Arche doesn't prescribe one approach.** It provides a foundation for multiple modes of agentic development, each suited to different paradigms. As the world of agents evolves, new modes emerge independently based on market and industry evolution.

**Modes have maturity levels** that evolve as they gain adoption and stability. See [modes/MODE_MATURITY.md](modes/MODE_MATURITY.md) for the maturity model.

**Choosing a mode?** See [modes/MODE_SELECTION.md](modes/MODE_SELECTION.md) for detailed guidance on which mode fits your project.

---

## Modes: Multiple Paradigms, One Foundation

In the beginning, there was arche — the first principle from which agency arises.

From this foundation emerge modes: the fundamental ways agency comes into being. A mode names how intent is formed, how reasoning unfolds, and how action becomes possible. It is not a framework imposed from above, but a manner of being — a way in which agency expresses itself when it acts.

Within each mode, forms take shape as concrete realizations in code and behavior. Forms adapt a mode to particular problems, environments, or constraints, while remaining faithful to the underlying expression of agency.
arche endures beneath all expression. Modes reveal how agency may be. Forms give that possibility shape.

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

## 📚 Documentation Structure

All arche documentation is organized by role and use case:

```
docs/
├── getting-started/          ← Start here (all roles)
│   ├── QUICK_REFERENCE.md
│   ├── ARCHE_INTEGRATION_GUIDE.md
│   └── COMPLETION_SUMMARY.md
│
├── frameworks/               ← Core architecture
│   ├── MODE_COMPATIBILITY.md
│   ├── AGENT_ARCHETYPES.md
│   ├── MODE_MIGRATION_GUIDE.md
│   └── COMMUNITY_CONTRIBUTION_PATHWAY.md
│
├── learning/                 ← Feedback & improvement
│   ├── FEEDBACK_SPECIFICATION.md
│   └── FRAMEWORK_LEARNING_LOOP.md
│
└── vendor-translation/       ← Deploy to any platform
    ├── VENDOR_TRANSLATION_SPECIFICATION.md
    ├── VENDOR_INTEGRATION_GUIDE.md
    ├── VENDOR_SELECTION_DECISION_TREE.md
    └── examples/
        └── EXAMPLE_BP0004_TO_CLAUDE.md

blueprints/                   ← Production-ready MAOs
├── BP-0003-incident-response.md
├── BP-0004-content-moderation.md
└── BP-0005-data-operations.md

tools/                        ← Implementation utilities
├── arche_compat_check.py
└── (foundry-translate coming Phase 1)
```

### 🎯 Where to Start

| You are... | Go to... | Time |
|-----------|----------|------|
| **Brand new to arche** | [docs/getting-started/QUICK_REFERENCE.md](docs/getting-started/QUICK_REFERENCE.md) | 5 min |
| **Need to choose a mode** | [docs/frameworks/MODE_COMPATIBILITY.md](docs/frameworks/MODE_COMPATIBILITY.md) | 15 min |
| **Want to build a MAO** | [blueprints/](blueprints/) | 30 min |
| **Need to deploy to vendor** | [docs/vendor-translation/README.md](docs/vendor-translation/README.md) | 20 min |
| **Want full architecture** | [docs/getting-started/ARCHE_INTEGRATION_GUIDE.md](docs/getting-started/ARCHE_INTEGRATION_GUIDE.md) | 1 hour |

---

## Architecture & Selective Sync

**Arche grows, your project doesn't.**

As arche evolves with more modes, forms, and patterns, individual projects stay lightweight through **selective sync**:

- **What's copied:** Only the mode and form you select
- **What's referenced:** Cross-mode documentation (modes/MODE_SELECTION.md, TELEMETRY.md) via URLs
- **What's excluded:** All other modes, forms, and templates

**Example:** A 3-layer/automation project gets:
- `modes/3-layer/_shared/` (agents.md, init_env.md)
- `modes/3-layer/forms/automation/` (project structure, requirements.txt, README template)
- **Not:** agentic-swarm, event-driven, rl-loop, or any other modes

**Benefits:**
- Lightweight projects focused on one architectural pattern
- Faster bootstrap and setup
- No confusion from unrelated modes
- Clear separation of concerns
- Repository can grow without bloating projects

**Accessing other modes:**
If your project evolves and needs a different mode:
1. Reference mode documentation at GitHub URLs
2. Bootstrap a new project with the new mode
3. Migrate your code to the new structure

**AI agents automatically understand this:** When working in a project, they only see the selected mode's files and reference other modes via URLs when needed.

---

## The Philosophy

**Arche improves through use.** Every project built with arche discovers new patterns, edge cases, and better approaches. These learnings flow back through GitHub Issues, making the framework stronger for everyone.

**Modes evolve independently.** As agent paradigms mature in production, new modes emerge. The framework doesn't dictate architecture—it captures what works in practice.

**A virtuous circle.** When arche helps you build something valuable, others could benefit too. If you discover ways to help more people find it—clearer documentation, better examples, thoughtful writing about your experience—those contributions strengthen the whole ecosystem.

---

## Quick Start

Multiple ways to get started with arche—choose what works for your workflow:

### Option 1: Single Prompt (10 seconds)

Just tell your AI:
```
Follow arche 3-layer mode: https://raw.githubusercontent.com/coreyshort/arche/main/modes/3-layer/INSTRUCTIONS.md
```

**That's it.** Your AI now operates using the 3-layer architecture.

### Option 2: Single-Line Config File (30 seconds)

Add one line to your project:

**For Cursor:**
```bash
echo "Follow: https://raw.githubusercontent.com/coreyshort/arche/main/modes/3-layer/INSTRUCTIONS.md" > .cursorrules
```

**For GitHub Copilot:**
```bash
echo "Follow: https://raw.githubusercontent.com/coreyshort/arche/main/modes/3-layer/INSTRUCTIONS.md" > .github/copilot-instructions.md
```

**For Claude Projects:**
Add this to your project instructions:
```
Follow: https://raw.githubusercontent.com/coreyshort/arche/main/modes/3-layer/INSTRUCTIONS.md
```

### Option 3: AI Generates Entire Project (1 minute)

Tell your AI:
```
Generate a new project using arche.
Reference: https://raw.githubusercontent.com/coreyshort/arche/main/modes/3-layer/INSTRUCTIONS.md
Project type: [automation/webapp/api/etc.]
Description: [what you want to build]
```

Your AI will read the instructions, select the appropriate form, and bootstrap the full project structure.

### Option 4: Let AI Select Mode Autonomously (1 minute)

For more complex projects, let AI analyze and choose:
```
Initialize an arche project for: [describe your project]
Use autonomous mode selection: https://raw.githubusercontent.com/coreyshort/arche/main/modes/AUTONOMOUS_MODE_SELECTION.md
```

The AI will:
1. Analyze your requirements
2. Score all modes (3-layer, agentic-swarm, event-driven, rl-loop)
3. Select the best fit
4. Bootstrap with optimal structure

### Option 5: Full Manual Setup (5 minutes)

**For new projects using the bootstrap script:**

```bash
# Download bootstrap script
curl -O https://raw.githubusercontent.com/coreyshort/arche/main/arche-tools/bootstrap.py

# Interactive setup
python bootstrap.py --interactive

# Or direct initialization
python bootstrap.py --mode 3-layer --form automation --target my-project
```

**Selective Sync:** Bootstrap only copies files from your selected mode. Other modes stay in the repository, keeping your project lightweight and focused.

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

**For AI Agents:** 
- **Having trouble?** [.github/AGENT_QUICK_SUBMIT.md](.github/AGENT_QUICK_SUBMIT.md) - Simplified submission (copy-paste template, no token needed)
- **Full setup:** [.github/AGENT_ACCESS.md](.github/AGENT_ACCESS.md) - Complete guide with GitHub API access

**Optional:** Include anonymous telemetry (project type, team size) to help prioritize improvements. See [TELEMETRY.md](TELEMETRY.md).

### Proposing New Modes

See an emerging paradigm not captured by existing modes? Propose it:

1. Create a GitHub Issue describing the paradigm
2. Explain what problems it solves
3. Share production examples demonstrating the pattern
4. Propose initial structure and principles

**New modes must emerge from real-world production use**, not theoretical possibilities. They require demonstrated patterns that work reliably.

---

## Telemetry & Privacy

Arche collects **optional, anonymous usage data** to guide mode maturity and prioritize improvements:
- Mode and form selection (e.g., "3-layer/automation")
- Optional project type (internal tool, SaaS, research, etc.)
- Optional team size category

**What's NOT collected:** Project names, code, company names, or any identifying information.

**Opt-out:** Use `--no-telemetry` flag, delete `.arche-telemetry`, or set `~/.arche-config` with `{"telemetry_enabled": false}`.

**Full details:** [TELEMETRY.md](TELEMETRY.md)

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

## Examples

The `examples/` directory contains:

**Single-line config files:**
- `.cursorrules` - Cursor editor (single line)
- `.github-copilot-instructions.md` - GitHub Copilot (single line)
- `claude-project-instructions.md` - Claude Projects (single line)

**Prompt templates:**
- `prompts.md` - Copy-paste prompts for different scenarios
  - Use existing project
  - Generate new project
  - Auto-select mode
  - Explore and learn
  - Add to complex project

**Model-specific examples:**
- `github-copilot-instructions.md` - Full GitHub Copilot setup
- `claude-project-custom-instructions.md` - Full Claude Projects setup
- `chatgpt-custom-instructions.md` - Full ChatGPT setup
- `gemini-instructions.md` - Full Google Gemini setup

Each file demonstrates how to reference mode-specific instructions for that AI tool.

---

## Forms

In Aristotelian philosophy, a form is the organizing principle that makes a thing what it is—distinct from its material, yet inseparable from its realization. A form defines structure, purpose, and potential without prescribing a single instantiation.

In Arche, both **Modes** and **Forms** serve this role at different levels:

- **Modes** are architectural forms—fundamental paradigms for how agents reason and act
- **Forms within modes** are project forms—specific templates for common use cases

When you instantiate from arche, you're not copying a template. You're expressing a form—carrying forward principles that define how your system should reason, act, and evolve.

---

*An evolutionary framework for agentic systems*
