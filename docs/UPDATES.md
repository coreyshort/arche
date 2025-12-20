# Arche Update Management

## Overview

When you create a project with arche, you get a snapshot of the framework at that moment. This document explains how to manage updates as arche evolves.

---

## Update Strategies

### 1. Auto-Update (Default)

**Behavior:** Automatically checks for and applies updates from arche repository.

**When to use:**
- You want the latest patterns and improvements
- Your project is actively developed
- You trust the maturity level of your mode (e.g., 3-layer is mature)

**How it works:**
- Checks GitHub for updates when you interact with agents
- Applies updates to framework files only (agents.md, init_env.md)
- Never touches your custom files (directives/, execution/, your code)
- Shows what changed in console

**Configure:**
```json
// .arche-config
{
  "update_strategy": "auto",
  "mode": "3-layer",
  "form": "automation"
}
```

### 2. Frozen (Snapshot)

**Behavior:** Never updates. Project stays exactly as instantiated.

**When to use:**
- Production systems requiring stability
- You've customized framework files
- You want explicit control over all changes
- Using an emerging mode that's rapidly evolving

**How it works:**
- No automatic checks
- No prompts
- Update script exits immediately with message
- You manually update when ready

**Configure:**
```json
// .arche-config
{
  "update_strategy": "frozen",
  "frozen_version": "v1.0.0",
  "mode": "3-layer",
  "form": "automation"
}
```

### 3. Manual (Explicit Only)

**Behavior:** Only updates when you explicitly run the update command.

**When to use:**
- You want updates but on your schedule
- You review changes before applying
- You're between frozen and auto

**How it works:**
- No automatic checks or prompts
- You run `python update_arche.py` when ready
- Shows diff of changes before applying
- You confirm before proceeding

**Configure:**
```json
// .arche-config
{
  "update_strategy": "manual",
  "mode": "3-layer",
  "form": "automation"
}
```

### 4. Prompt (Periodic)

**Behavior:** Periodically asks if you want to update.

**When to use:**
- You want reminders without forced updates
- Your workflow includes regular check-ins
- You want balance between awareness and control

**How it works:**
- Checks on interval (default: 30 days)
- Shows what's changed since your version
- You choose: update now, skip this time, or change strategy
- Records your choice and next check date

**Configure:**
```json
// .arche-config
{
  "update_strategy": "prompt",
  "update_check_interval_days": 30,
  "last_update_check": "2025-12-20",
  "mode": "3-layer",
  "form": "automation"
}
```

---

## What Gets Updated

### Always Updated (if strategy allows):
- `agents.md` or `INSTRUCTIONS.md` (framework instructions)
- `init_env.md` (if exists in mode's _shared/)
- Mode-specific shared files from `modes/{mode}/_shared/`

### Never Updated:
- Your code (directives/, execution/, application logic)
- Custom files you've added
- Project-specific configuration (.env, credentials, etc.)
- `.arche-config` (your preferences)
- `.arche-telemetry` (your project metadata)

### Selectively Updated (with confirmation):
- Form-specific templates (requirements.txt, .gitignore) if they've changed
- README template (only if you haven't modified it)

---

## The Update Tool

### Installation

The update tool is downloaded on first use:

```bash
# Check for updates
python -c "$(curl -fsSL https://raw.githubusercontent.com/coreyshort/arche/main/arche-tools/check_updates.py)"
```

Or download it once:

```bash
curl -O https://raw.githubusercontent.com/coreyshort/arche/main/arche-tools/update_arche.py
python update_arche.py --check
```

### Commands

**Check for updates:**
```bash
python update_arche.py --check
```

**Show what would change:**
```bash
python update_arche.py --diff
```

**Apply updates:**
```bash
python update_arche.py --apply
```

**Change update strategy:**
```bash
python update_arche.py --set-strategy frozen
python update_arche.py --set-strategy auto
python update_arche.py --set-strategy manual
python update_arche.py --set-strategy prompt --interval 60  # days
```

**Pin to specific version:**
```bash
python update_arche.py --pin v1.0.0
```

---

## Configuration File: .arche-config

Located in your project root. Created during bootstrap, modified by update tool.

**Full example:**
```json
{
  "update_strategy": "prompt",
  "update_check_interval_days": 30,
  "last_update_check": "2025-12-20",
  "arche_version": "v1.0.0",
  "mode": "3-layer",
  "form": "automation",
  "telemetry_enabled": true
}
```

**Fields:**
- `update_strategy`: "auto", "frozen", "manual", or "prompt"
- `update_check_interval_days`: Days between prompts (if strategy is "prompt")
- `last_update_check`: ISO date of last check
- `arche_version`: Version you're currently on (commit hash or tag)
- `mode`: Your architectural mode
- `form`: Your project form
- `telemetry_enabled`: Whether to send anonymous usage data

---

## Automatic Update Behavior (Default)

When `update_strategy` is `"auto"` (default):

1. **Trigger:** When you start working (AI agent initializes or you run commands)
2. **Check frequency:** Once per day maximum (cached)
3. **Process:**
   - Fetch latest version for your mode
   - Compare with your current version
   - If changes exist in framework files:
     - Backup current files → `.arche-backups/YYYYMMDD-HHMMSS/`
     - Apply updates
     - Show summary of changes
     - Log to `.arche-update.log`
4. **Rollback:** If issues arise, restore from backup

**Console output:**
```
🔄 Arche Update Available
   Current version: v1.0.0
   Latest version: v1.1.0
   Changes: Updated agents.md with new mode selection guidance
   
   Backing up current files...
   Applying updates...
   ✓ Updated agents.md
   ✓ Updated init_env.md
   
   Backup stored in: .arche-backups/20251220-143022/
   To rollback: python update_arche.py --rollback 20251220-143022
```

---

## Version Pinning

Pin your project to a specific arche version:

```bash
python update_arche.py --pin v1.0.0
```

This sets `update_strategy` to `"frozen"` and records the version. Useful for:
- Production deployments
- Reproducible environments
- Avoiding breaking changes

**Unpinning:**
```bash
python update_arche.py --set-strategy auto
```

---

## Handling Conflicts

If you've modified framework files (agents.md, init_env.md):

1. **Auto strategy:** Skips update, logs warning, suggests manual review
2. **Manual strategy:** Shows 3-way diff (your version, original, new version)
3. **Prompt strategy:** Asks if you want to overwrite your changes

**Best practice:** Don't modify framework files. If you need custom instructions, add them to your directives/ or create a separate `CUSTOM_INSTRUCTIONS.md` that agents can reference.

---

## Update Notifications

### For auto strategy:
- Silent updates (just logs)
- Summary shown in console on significant changes
- Recorded in `.arche-update.log`

### For prompt strategy:
- Notification with change summary
- "Update now", "Remind me in X days", "Switch to manual" options
- Links to changelog/release notes

### For manual strategy:
- No notifications
- Check manually when you want

### For frozen strategy:
- No notifications ever

---

## Migration Between Versions

**Major version changes** (v1.x.x → v2.x.x) may include breaking changes:

1. Update tool warns about breaking changes
2. Shows migration guide URL
3. Requires explicit confirmation
4. Creates backup automatically
5. Suggests testing before committing

**Minor version changes** (v1.0.x → v1.1.x) are safe to apply automatically.

---

## Bootstrap Configuration

During `bootstrap.py --interactive`, you'll be asked:

```
📦 Update Strategy
   How should this project receive arche updates?
   
   1. Auto (recommended) - Automatic updates, latest improvements
   2. Frozen - Never update, stable snapshot
   3. Manual - Update only when you explicitly choose
   4. Prompt - Ask me periodically (every X days)
   
   Choose (1-4): 
```

For direct initialization:
```bash
python bootstrap.py --mode 3-layer --form automation --update-strategy auto
python bootstrap.py --mode 3-layer --form automation --update-strategy frozen
python bootstrap.py --mode 3-layer --form automation --update-strategy prompt --update-interval 60
```

---

## Best Practices

**Use auto strategy when:**
- Mode is mature (3-layer)
- You want the latest patterns
- Your project is in active development

**Use frozen strategy when:**
- Mode is emerging (agentic-swarm, event-driven, rl-loop)
- Project is in production
- You've heavily customized framework files

**Use manual strategy when:**
- You want control but not rigidity
- You review all changes before applying
- You're between dev and production

**Use prompt strategy when:**
- You want reminders without automation
- You're comfortable with periodic reviews
- You want balance

---

## FAQ

**Q: Will updates break my code?**  
A: No. Updates only touch framework files (agents.md, init_env.md). Your code (directives/, execution/, application logic) is never modified.

**Q: What if I've modified agents.md?**  
A: Update tool detects modifications and skips automatic updates. It suggests manual review with diff.

**Q: Can I rollback an update?**  
A: Yes. Backups are stored in `.arche-backups/`. Use `python update_arche.py --rollback TIMESTAMP`.

**Q: How do I know what changed?**  
A: Run `python update_arche.py --diff` or check `.arche-update.log`. Release notes are also linked.

**Q: Do updates work offline?**  
A: No. Updates require internet to fetch from GitHub. If offline, auto/prompt strategies gracefully skip.

**Q: Can I update only specific files?**  
A: Yes. `python update_arche.py --file agents.md --apply`.

**Q: What about modes other than 3-layer?**  
A: Same process. Update tool fetches from `modes/{your-mode}/_shared/`.

**Q: Does telemetry track updates?**  
A: If telemetry is enabled, it records update events (version changes) to help understand adoption patterns. No code or project details are sent.

---

## Implementation Note

This document describes the intended behavior. The `update_arche.py` tool will be implemented to support these strategies. Initial release (v1.0.0) may have manual-only updates with auto/prompt strategies coming in v1.1.0.

Track implementation: https://github.com/coreyshort/arche/issues
