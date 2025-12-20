# GitHub Copilot Instructions for Arche Projects

Follow the arche framework for reliable AI-assisted development.

For 3-layer mode projects:
https://raw.githubusercontent.com/coreyshort/arche/main/modes/3-layer/INSTRUCTIONS.md

## Quick Reference

### 3-Layer Architecture
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
