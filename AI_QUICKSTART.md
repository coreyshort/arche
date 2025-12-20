# AI Agent Quick Start

> **For AI agents:** Read this first. Everything you need in under 2 minutes.

## What is arche?

Evolutionary framework for building AI agent systems. Multiple architectural modes, not prescriptive.

## Getting Started (Choose One)

**Autonomous:** `python -c "$(curl -fsSL https://raw.githubusercontent.com/coreyshort/arche/main/arche-tools/bootstrap.py)" --interactive`

**Existing project:** Read the appropriate INSTRUCTIONS.md for your mode

**Just exploring:** Continue below

## Core Concept

**Modes** = architectural paradigms (3-layer, event-driven, etc.)  
**Forms** = project templates within a mode (automation, webapp, api-service, etc.)  

You only get files for **your selected mode** - not everything.

## Navigation Map

| If you need... | Read this... |
|---|---|
| Start new project | Run bootstrap.py (see above) |
| Choose a mode | [AUTONOMOUS_MODE_SELECTION.md](AUTONOMOUS_MODE_SELECTION.md) (8 questions, score-based) |
| Understand a mode | `modes/{mode}/MODE.md` |
| Configure AI assistant | `modes/{mode}/INSTRUCTIONS.md` |
| Compare modes | [MODE_SELECTION.md](MODE_SELECTION.md#comparison-matrix) |
| Understand mode maturity | [MODE_MATURITY.md](MODE_MATURITY.md) (6 levels: 🌱→✅) |
| Improve arche | Create [GitHub Issue](https://github.com/coreyshort/arche/issues) (pattern-based, not task-by-task) |
| Understand telemetry | [TELEMETRY.md](TELEMETRY.md) (optional, anonymous, 4 opt-outs) |
| Manage updates | [docs/UPDATES.md](docs/UPDATES.md) (4 strategies) |

## Most Common: 3-Layer Mode

**When:** Reliability-critical, predictable workflows, data processing, automation

**Architecture:**
- **Directives** (what to do) - Markdown SOPs in `directives/`
- **Orchestration** (decision making) - You, the AI agent
- **Execution** (doing the work) - Deterministic Python scripts in `execution/`

**Quick setup:**
```bash
curl -O https://raw.githubusercontent.com/coreyshort/arche/main/arche-tools/bootstrap.py
python bootstrap.py --mode 3-layer --form automation
```

**Full instructions:** [modes/3-layer/INSTRUCTIONS.md](modes/3-layer/INSTRUCTIONS.md)

## Decision Tree (30 seconds)

```
Need predictable, reliable workflows? → 3-layer (mature ✅)
Multiple agents coordinating? → agentic-swarm (emerging 🚀)
Event-driven architecture? → event-driven (emerging 🚀)
Agent learns from feedback? → rl-loop (emerging 🚀)
Unclear? → Default to 3-layer (lowest risk)
```

## Key Files (Selective Sync)

When you bootstrap, you get ~15-30 files:
- `modes/{mode}/_shared/` - Core files (agents.md, init_env.md)
- `modes/{mode}/forms/{form}/` - Template files for your project type
- `.arche-config` - Update preferences
- **Not copied:** Other modes, docs, tools (reference via URL if needed)

## Pattern-Based Improvements

**Do:** Observe patterns over multiple interactions → Reflect → Create GitHub Issue when you've identified recurring problems

**Don't:** Create issues task-by-task or for single observations

**Scope:** Full ecosystem (technical, docs, discoverability, community, mode evolution, telemetry)

## Self-Annealing

When things break:
1. Fix it
2. Update the tool/script
3. Test
4. Update directive
5. System is stronger

Two levels: **Within project** (fix immediately) + **Across arche** (reflect, then create issue)

## That's It

You now know enough to start. Read detailed docs only when you need them.

**Repository:** https://github.com/coreyshort/arche  
**Default mode:** 3-layer (if unclear)  
**Philosophy:** Evolutionary, not prescriptive
