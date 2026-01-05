# 3-Layer Mode

**Maturity:** ✅ Mature  
**Paradigm:** Deterministic execution with AI orchestration  
**Production Projects:** 50+ known deployments  
**Last Status Update:** December 2025

## Overview

The 3-layer mode maximizes reliability by separating concerns into three distinct layers:

- **Layer 1: Directives** - Natural language SOPs defining *what* to do
- **Layer 2: Orchestration** - AI making intelligent decisions and routing
- **Layer 3: Execution** - Deterministic code *doing* the work

## When to Use This Mode

**Best for:**
- Data processing and ETL pipelines
- Web scraping and automation
- API integrations with complex business logic
- Report generation and scheduled tasks
- Projects where reliability > adaptability
- Teams wanting predictable, testable outcomes

**Consider alternatives when:**
- You need real-time agent coordination (→ agentic-swarm mode)
- Your system is primarily event-driven (→ event-driven mode)
- Agents need to learn from outcomes over time (→ rl-loop mode)

**Detailed comparison:** See [../MODE_SELECTION.md](../MODE_SELECTION.md) for comprehensive mode selection guidance.

## The Problem It Solves

**Pure AI coding compounds errors:**  
90% accuracy per step × 5 steps = 59% success rate

**Solution:**  
Push complexity into deterministic code. AI orchestrates, code executes reliably.

## Architecture Pattern

```
User Intent
    ↓
AI reads directives/*.md (what to do)
    ↓
AI calls execution/* scripts (how to do it)
    ↓
Deterministic results + learning feedback
    ↓
AI updates directives (system improves)
```

## Forms Available

This mode includes project forms for different use cases:

- **automation** - Data processing, ETL, scraping
- **webapp-fullstack** - Full-stack web applications  
- **webapp-frontend** - Frontend-only SPAs
- **api-service** - Backend APIs and microservices
- **data-science** - ML workflows and analysis
- **cli-tool** - Command-line applications
- **library** - Reusable packages

## Self-Annealing Loop

**Within your project:**
1. Encounter issue → Fix script → Test → Update directive → Stronger

**Across ecosystem:**
1. Discover pattern → GitHub Issue → Approved → Merged → Everyone benefits

## Evolution Path

This mode emerged from production experience with AI-assisted development. As agent paradigms evolve, new modes will emerge alongside it. The 3-layer pattern remains valuable for projects requiring deterministic reliability.

## Getting Started

See [INSTRUCTIONS.md](INSTRUCTIONS.md) for AI assistant configuration.

---

**Repository:** https://github.com/coreyshort/arche  
**Discuss this mode:** https://github.com/coreyshort/arche/discussions
