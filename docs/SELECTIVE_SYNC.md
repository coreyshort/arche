# Selective Sync Architecture

## Problem

As arche grows with more modes, forms, and documentation, projects shouldn't need to download everything. A 3-layer automation project doesn't need agentic-swarm files, and vice versa.

## Solution: Selective Sync

**Principle:** Projects only receive files for their selected mode and form. Everything else stays in the repository.

---

## What Gets Synced

### Into Your Project

When you bootstrap with `--mode 3-layer --form automation`:

**Copied:**
- `modes/3-layer/_shared/` → Project root
  - `agents.md` (or INSTRUCTIONS.md depending on mode)
  - `init_env.md`
  - Any other mode-specific shared files

- `modes/3-layer/forms/automation/` → Project root
  - `.gitignore`
  - `requirements.txt`
  - `README.md` (template)
  - Form-specific structure and files

**Generated:**
- `.arche-telemetry` (if enabled)
- Project directories specified in `project.json`

### NOT Copied (Referenced via URLs)

- Other modes: `agentic-swarm/`, `event-driven/`, `rl-loop/`
- Other forms within the same mode
- Cross-mode documentation:
  - `MODE_SELECTION.md`
  - `MODE_MATURITY.md`
  - `AUTONOMOUS_MODE_SELECTION.md`
  - `TELEMETRY.md`
  - Root `README.md`
- Bootstrap tools
- Examples directory

**Why not copy these?**
- They're not needed for day-to-day work
- They change as arche evolves (URL references stay current)
- They add bloat
- They create confusion (mixing multiple modes)

---

## Implementation: bootstrap.py

The bootstrap script implements selective sync:

```python
# Only fetches selected mode's shared files
shared_count = fetch_template_recursive(f"modes/{mode}/_shared", target_dir, branch)

# Only fetches selected form's files
form_count = fetch_template_recursive(
    f"modes/{mode}/forms/{form}", 
    target_dir, 
    branch,
    exclude=["project.json"]
)
```

**No recursion beyond the selected mode and form.**

---

## How AI Agents Work With This

### Within Your Project

AI agents operate using the files in your project:
- Read `agents.md` or `INSTRUCTIONS.md` for mode-specific guidance
- Follow the architectural pattern of your selected mode
- Contribute improvements back via GitHub Issues

### Referencing Other Modes

If context requires understanding other modes (e.g., for comparison or migration):
- Reference via GitHub URLs: `https://github.com/coreyshort/arche/blob/main/modes/agentic-swarm/MODE.md`
- AI reads the URL content without copying files
- Keeps project focused while accessing full ecosystem knowledge

### Mode Selection

When starting a new project:
- AI reads `AUTONOMOUS_MODE_SELECTION.md` from URL
- Analyzes requirements, scores modes
- Selects best mode
- Bootstraps with only that mode's files

---

## Benefits

**For Projects:**
- Lightweight (only 10-50 files vs hundreds)
- Fast bootstrap (seconds, not minutes)
- No confusion from unrelated modes
- Clear architectural focus
- Updates via URL references stay current

**For Arche:**
- Can grow unbounded (10 modes, 50 forms, extensive docs)
- No concern about project bloat
- Easy to add new modes
- Clean separation between modes
- Centralized documentation always current

**For AI Agents:**
- Clear context (one mode's instructions)
- Faster file reads (fewer files)
- No mixing of architectural paradigms
- URL references provide access to full knowledge when needed

---

## Migration Between Modes

If your project needs to change modes:

1. **Analyze why:** Is it a fundamental architecture mismatch or a temporary need?
2. **Reference new mode:** Read its documentation via URL
3. **Bootstrap new project:** `python bootstrap.py --mode [new-mode] --form [form]`
4. **Migrate code:** Copy your business logic into new structure
5. **Test thoroughly:** Architectures differ significantly

**Modes are not interchangeable.** Selective sync enforces this by keeping them separate.

---

## Examples

### Example 1: 3-layer automation project

**Gets:**
- `agents.md` (3-layer instructions)
- `init_env.md`
- `requirements.txt` (automation-specific)
- `.gitignore` (automation-specific)
- `README.md` (automation template)

**Doesn't get:**
- agentic-swarm files
- event-driven files
- rl-loop files
- webapp forms
- Cross-mode docs

**Total files:** ~15-20

### Example 2: Agentic-swarm project (future)

**Gets:**
- `modes/agentic-swarm/_shared/` files
- `modes/agentic-swarm/forms/[selected-form]/` files

**Doesn't get:**
- 3-layer files
- Other modes
- Other forms

**Total files:** ~20-30 (mode-specific)

---

## FAQ

**Q: How do I reference MODE_SELECTION.md if it's not in my project?**  
A: Via URL: `https://github.com/coreyshort/arche/blob/main/MODE_SELECTION.md`

**Q: What if I need to understand another mode?**  
A: Reference its MODE.md via URL. AI agents can read URLs without copying files.

**Q: Can I manually copy other modes into my project?**  
A: Not recommended. It creates confusion and mixing paradigms. Bootstrap a separate project instead.

**Q: What if a mode needs cross-mode utilities?**  
A: Put them in that mode's `_shared/` directory or create a `tools/` subdirectory within the mode.

**Q: How do updates to arche affect my project?**  
A: Your project files are static. Reference documentation via URLs to see latest. Manually update if needed.

**Q: Can I have multiple modes in one project?**  
A: Not directly. Some complex systems use multiple modes across services (e.g., 3-layer backend + event-driven notifications). These are separate codebases that integrate.

---

## Conclusion

Selective sync keeps arche **generative, not prescriptive**. Each project embodies one mode precisely, while the full ecosystem remains accessible via references. As arche grows to 10, 20, or 50 modes, individual projects stay focused and lightweight.

**Arche scales. Your project doesn't need to.**
