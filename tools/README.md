# Tools: Implementation Utilities

**CLIs and scripts for working with arche MAOs.**

---

## 🛠️ Available Tools

### arche_compat_check.py
**Validate mode combinations and MAO architecture**

**Purpose:** Ensure your MAO uses compatible modes

**Usage:**
```bash
python arche_compat_check.py --modes 3-layer rl-loop
# ✅ VALID: 3-Layer + RL-Loop compatible

python arche_compat_check.py --modes event-driven agentic-swarm 3-layer
# ✅ VALID: Event-Driven + Agentic-Swarm + 3-Layer compatible

python arche_compat_check.py --modes 3-layer event-driven
# ⚠️ WARNING: Mode combination unusual (but valid)
```

**Features:**
- ✅ Validates mode pairs
- ✅ Checks anti-patterns
- ✅ Suggests alternatives
- ✅ Explains recommendations

**Reference:** See ../frameworks/MODE_COMPATIBILITY.md for pairing patterns

---

## 🚀 Coming Soon: Phase 1

### foundry-translate
**Translate arche MAOs to vendor formats**

**Purpose:** Auto-generate vendor-specific MAO from arche blueprint

**Usage:**
```bash
foundry-translate --mao ./my-mao.md --target claude --output ./claude-mao/
# Generates Claude Projects structure

foundry-translate --mao ./my-mao.md --target copilot --output ./copilot-mao/
# Generates Copilot Studio configuration

foundry-translate --mao ./my-mao.md --all-vendors --output ./deployments/
# Generates for all 6 vendors
```

**Supported Vendors:**
- Claude Projects
- Copilot Studio
- Gemini with Agents
- OpenAI Swarm
- AutoGen
- LangGraph

**Status:** Specification complete (../vendor-translation/VENDOR_TRANSLATION_SPECIFICATION.md)  
**Implementation:** Phase 1 (4-6 weeks)

---

## 🚀 Coming Soon: Phase 2

### foundry-deploy
**Deploy translated MAOs to vendors**

**Purpose:** One-command deployment to any vendor

**Usage:**
```bash
foundry-deploy --vendor claude --config ./claude-mao --env production
# Deploys to Claude Projects

foundry-deploy --vendor copilot --config ./copilot-mao --env staging
# Deploys to Copilot Studio (staging)

foundry-deploy --all-vendors --config ./deployments --sync
# Deploys to all vendors and keeps in sync
```

**Features:**
- ✅ Deploy to any vendor
- ✅ Environment management (dev/staging/prod)
- ✅ Sync across multiple vendors
- ✅ Rollback support

**Status:** Specification stage  
**Implementation:** Phase 2 (6-8 weeks)

---

## 🚀 Future: Phase 3

### foundry-analyze
**Analyze feedback and recommend improvements**

**Purpose:** Mine learning loop data for insights

**Usage:**
```bash
foundry-analyze --mao my-mao --period weekly
# Shows weekly accuracy trends

foundry-analyze --mao my-mao --find-patterns
# Identifies common error patterns

foundry-analyze --mao my-mao --recommend-improvements
# Suggests prompt/threshold changes
```

### foundry-migrate
**Migrate MAOs between vendors**

**Purpose:** Move your MAO from one vendor to another

**Usage:**
```bash
foundry-migrate --from claude --to copilot --mao-id my-content-moderation
# Migrates Claude MAO to Copilot Studio (keeping history)
```

---

## 🛠️ Development Setup

### For Users
All tools available via:
```bash
pip install arche-tools
foundry-translate --help
```

### For Contributors
```bash
git clone <arche repo>
cd tools/
pip install -e .
python arche_compat_check.py --test
```

---

## 📊 Tool Roadmap

| Tool | Status | Phase | When |
|------|--------|-------|------|
| arche_compat_check.py | ✅ Available | Now | Use today |
| foundry-translate | 🚀 Planned | Phase 1 | 4-6 weeks |
| foundry-deploy | 🚀 Planned | Phase 2 | 6-8 weeks |
| foundry-analyze | 🚀 Planned | Phase 3 | 8-12 weeks |
| foundry-migrate | 🚀 Planned | Phase 3 | 8-12 weeks |

---

## 🎓 Usage Examples

### Example 1: Validate Your MAO
```bash
# Check modes are compatible
python arche_compat_check.py --modes agentic-swarm rl-loop
# ✅ VALID

# Check against anti-patterns
python arche_compat_check.py --modes event-driven event-driven
# ⚠️ WARNING: Duplicate mode
```

### Example 2: Translate and Deploy (Once Phase 1 Ready)
```bash
# Generate vendor formats
foundry-translate --mao BP-0004-content-moderation.md --all-vendors

# Deploy to Claude
foundry-deploy --vendor claude --config ./claude-mao --env production

# Deploy to Copilot
foundry-deploy --vendor copilot --config ./copilot-mao --env production
```

---

## 📝 Documentation

- **Mode Compatibility:** ../frameworks/MODE_COMPATIBILITY.md
- **Translation Guide:** ../vendor-translation/VENDOR_INTEGRATION_GUIDE.md
- **Specification:** ../vendor-translation/VENDOR_TRANSLATION_SPECIFICATION.md

---

## 🤝 Contributing

To contribute new tools:
1. See ../frameworks/COMMUNITY_CONTRIBUTION_PATHWAY.md
2. Design matches arche principles
3. Submit RFC (Request for Comments)
4. 2-week community review
5. Implementation and testing

---

## Next Steps

### Now
- Use `arche_compat_check.py` to validate your mode combinations

### Phase 1 (4-6 weeks)
- Use `foundry-translate` to auto-generate vendor formats

### Phase 2+
- Use full tool suite for deployment and management

---

