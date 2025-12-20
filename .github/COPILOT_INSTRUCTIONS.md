# GitHub Copilot Instructions for Arche Projects

Follow the arche framework for reliable AI-assisted development.

## Choose Your Mode

Arche supports multiple architectural modes. Choose based on your project:

**For most projects (mature, proven):**
https://raw.githubusercontent.com/coreyshort/arche/main/modes/3-layer/INSTRUCTIONS.md

**For multi-agent systems (emerging):**
https://raw.githubusercontent.com/coreyshort/arche/main/modes/agentic-swarm/MODE.md

**For event-driven systems (emerging):**
https://raw.githubusercontent.com/coreyshort/arche/main/modes/event-driven/MODE.md

**For learning agents (emerging):**
https://raw.githubusercontent.com/coreyshort/arche/main/modes/rl-loop/MODE.md

**Not sure? Let AI decide:**
https://raw.githubusercontent.com/coreyshort/arche/main/AUTONOMOUS_MODE_SELECTION.md

---

## Quick Reference (3-Layer Mode)

### Architecture
- **Layer 1 (Directives):** Read `directives/*.md` files to understand what to do
- **Layer 2 (Orchestration):** You make intelligent decisions and route between tools  
- **Layer 3 (Execution):** Call scripts in `execution/` to do the actual work

### Your Role
- Check `execution/` for existing tools before writing new code
- Read relevant directives to understand goals, inputs, outputs, and edge cases
- Update directives as you learn from errors and edge cases
- Self-anneal: Fix → Test → Update directive → System stronger

### File Organization
- `directives/` - Natural language SOPs (what to do)
- `execution/` - Deterministic scripts (how to do it)
- `.tmp/` - Temporary files, never commit
- `.env` - Environment variables

Be pragmatic. Be reliable. Self-anneal.
