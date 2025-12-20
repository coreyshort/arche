# Arche Telemetry & Usage Insights

## Philosophy

Arche evolves through understanding real-world usage. To guide mode maturity decisions and discover emerging patterns, we collect **optional, privacy-conscious metadata** about how arche is used.

**Core Principles:**
1. **Transparency:** You know exactly what's collected
2. **Minimal:** Only aggregated, non-identifying metadata
3. **Opt-out:** Easy to disable completely
4. **No tracking:** No analytics scripts, no user tracking, no PII
5. **Community benefit:** Data helps prioritize improvements and mature modes

---

## What's Collected

### Via GitHub Issues (Optional)

When you create an improvement issue, you can optionally provide:
- **Mode:** Which architectural mode (3-layer, agentic-swarm, etc.)
- **Form:** Which project template (automation, webapp, etc.)
- **Project Type:** High-level category (internal tool, SaaS, research, etc.)
- **Team Size:** Small (1-3), Medium (4-10), Large (10+)

**Not collected:** Project names, company names, code, data, or any identifying information.

### Via Git Commits (Optional)

Projects can include metadata in commit messages using conventional commit format:

```
feat(mode:3-layer,form:automation): add new scraping directive

The parentheses contain optional metadata that helps track mode/form usage.
```

**Not collected:** Code content, repository names, user identities, or any project-specific information.

### Via Bootstrap Telemetry (Optional)

When using `bootstrap.py`, it can create a `.arche-telemetry` config file:

```json
{
  "telemetry_enabled": true,
  "mode": "3-layer",
  "form": "automation",
  "created_at": "2025-12-20",
  "arche_version": "1.0.0"
}
```

This file is **gitignored by default** and never leaves your machine unless you explicitly choose to share it in an issue.

---

## How It's Used

### Mode Maturity Decisions

Understanding adoption helps evolve mode maturity:
- **🌱 Proposed → 🔨 Experimental:** First real-world usage
- **🔨 Experimental → 🚀 Emerging:** 5+ production projects, patterns stabilizing
- **🚀 Emerging → ✅ Mature:** 50+ production projects, battle-tested patterns

### Improvement Prioritization

Knowing which modes and forms are popular helps prioritize:
- Documentation improvements
- Bug fixes
- New features
- New forms for heavily-used modes

### Pattern Discovery

Aggregated metadata can reveal:
- Common form combinations (e.g., webapp + automation)
- Team size trends per mode
- Emerging use cases not covered by existing forms

---

## Opting Out

### Method 1: Don't Provide Metadata

Simply skip optional fields in GitHub Issues or omit metadata from commit messages. This is always your choice.

### Method 2: Disable Bootstrap Telemetry

When running `bootstrap.py`, answer "no" to telemetry:

```bash
python bootstrap.py --interactive
# When prompted: "Enable anonymous telemetry? [Y/n]" → n
```

Or use the flag directly:
```bash
python bootstrap.py --mode 3-layer --form automation --no-telemetry
```

### Method 3: Remove Existing Config

Delete `.arche-telemetry` from your project:

```bash
rm .arche-telemetry
```

### Method 4: Global Opt-Out

Create a global config to never enable telemetry:

```bash
echo '{"telemetry_enabled": false}' > ~/.arche-config
```

Bootstrap will respect this global setting.

---

## Privacy Guarantees

**We will NEVER collect:**
- Personal identifiable information (names, emails, IPs)
- Code or file contents
- Project names or repository URLs
- Company or organization names
- API keys or credentials
- Execution logs or error details
- Usage timestamps beyond creation date

**We will ONLY collect:**
- Mode selection (e.g., "3-layer")
- Form selection (e.g., "automation")
- Aggregated counts for maturity decisions
- Optional, self-reported project type categories

**How data is stored:**
- GitHub Issues are public by design—you control what you share
- `.arche-telemetry` files never leave your machine unless you share them
- No external analytics services, no tracking scripts, no databases

---

## Reviewing Telemetry Data

All telemetry is transparent and community-accessible:

**View aggregated stats:**
```bash
# Query GitHub Issues for mode/form distribution
https://github.com/coreyshort/arche/issues?q=label%3Amode%3A3-layer
```

**View your own telemetry config:**
```bash
cat .arche-telemetry
```

**Understand maturity status:**
See [MODE_MATURITY.md](MODE_MATURITY.md) for how telemetry informs maturity evolution.

---

## FAQs

**Q: Is telemetry required?**  
No. It's completely optional and easy to disable.

**Q: Can I use arche without telemetry?**  
Absolutely. All features work identically with or without telemetry.

**Q: Who sees telemetry data?**  
GitHub Issues are public. Your local `.arche-telemetry` file is private unless you share it.

**Q: Can I see what's being collected?**  
Yes. Check `.arche-telemetry` in your project or review issue templates at `.github/ISSUE_TEMPLATE/`.

**Q: What if I change my mind?**  
Delete `.arche-telemetry` anytime or create `~/.arche-config` with `{"telemetry_enabled": false}`.

**Q: Does this slow down my project?**  
No. Telemetry is a local config file. No network calls, no performance impact.

**Q: How does this help me?**  
Better understanding of usage means better prioritization of improvements, clearer documentation, and faster mode maturation—benefiting everyone in the arche ecosystem.

---

## Contributing to Telemetry

If you're building with arche and want to help the ecosystem evolve:

1. **Include mode/form in GitHub Issues** when reporting improvements
2. **Use metadata in commit messages** if comfortable: `feat(mode:3-layer,form:automation): ...`
3. **Enable bootstrap telemetry** to help track mode adoption
4. **Share your experience** in GitHub Discussions

Every data point helps prioritize what matters most to the community.

---

**Telemetry is about building better tools together, not surveillance.**

If you have concerns or suggestions about telemetry, open a GitHub Discussion: https://github.com/coreyshort/arche/discussions
