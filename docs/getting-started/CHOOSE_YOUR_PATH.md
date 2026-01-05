# Choose Your Path: How to Use arche

**Not sure where to start? This guide helps you pick the right approach for your situation.**

---

## 🎯 Quick Decision

**In 60 seconds, answer these questions:**

1. **Do you already have a working MAO?**
   - YES → Go to [Improve Existing MAO](#improve-existing-mao)
   - NO → Continue to question 2

2. **Do you want a blueprint (pre-built starting point)?**
   - YES → Go to [Use Existing Blueprint](#use-existing-blueprint)
   - NO → Go to [Build Custom MAO](#build-custom-mao)

3. **Do you want to contribute back to arche?**
   - YES → Go to [Contribute to arche](#contribute-to-arche)
   - NO → Pick from above

---

## 📘 Three Main Paths

### Path 1: Use Existing Blueprint ⚡

**Timeline:** 2-4 weeks  
**Difficulty:** Beginner  
**Best for:** Teams that want production-ready starting points

#### What You'll Do

1. **Explore blueprints** (1 hour)
   - Read: [../../blueprints/README.md](../../blueprints/README.md)
   - Choose between:
     - BP-0003: Incident Response (security teams)
     - BP-0004: Content Moderation (platform teams)
     - BP-0005: Data Operations (data teams)

2. **Understand the blueprint** (2-4 hours)
   - Read the blueprint document (BP-00XX.md)
   - Review agent definitions
   - Check evaluation scenarios

3. **Translate to your vendor** (3-5 days)
   - Read: [../vendor-translation/VENDOR_SELECTION_DECISION_TREE.md](../vendor-translation/VENDOR_SELECTION_DECISION_TREE.md)
   - Pick your vendor (Claude, Copilot Studio, Gemini, LangGraph, OpenAI Swarm)
   - Follow: [../vendor-translation/VENDOR_INTEGRATION_GUIDE.md](../vendor-translation/VENDOR_INTEGRATION_GUIDE.md)
   - Browse examples: [../vendor-translation/examples/](../vendor-translation/examples/README.md) — 5 complete, 1 planned

4. **Setup learning loops** (2-3 days)
   - Read: [../learning/FEEDBACK_SPECIFICATION.md](../learning/FEEDBACK_SPECIFICATION.md)
   - Implement feedback collection
   - Schedule weekly analysis

5. **Deploy & iterate** (ongoing)
   - Run evaluation scenarios
   - Collect feedback
   - Weekly improvements

#### When to Choose This Path

✅ You need to go live quickly  
✅ Your use case matches one of the 3 blueprints  
✅ You want proven patterns, not custom design  
✅ You prefer learning by example  

#### Related Docs

- [../../blueprints/README.md](../../blueprints/README.md) — Blueprint overview
- [../vendor-translation/README.md](../vendor-translation/README.md) — How to deploy
- [../learning/README.md](../learning/README.md) — Setup feedback loops

---

### Path 2: Build Custom MAO 🔧

**Timeline:** 4-8 weeks  
**Difficulty:** Intermediate  
**Best for:** Teams with specific requirements outside the blueprints

#### What You'll Do

1. **Understand the framework** (4-6 hours)
   - Read: [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
   - Read: [ARCHE_INTEGRATION_GUIDE.md](ARCHE_INTEGRATION_GUIDE.md)

2. **Choose your architecture** (1-2 days)
   - Study: [../frameworks/MODE_COMPATIBILITY.md](../frameworks/MODE_COMPATIBILITY.md)
   - Decide which modes fit your problem
   - Validate with: `python ../../arche-tools/arche_compat_check.py --modes [your-modes]`

3. **Define your agents** (2-4 days)
   - Review: [../frameworks/AGENT_ARCHETYPES.md](../frameworks/AGENT_ARCHETYPES.md)
   - Pick archetypes that match your roles
   - Write agent specifications

4. **Design learning loop** (1-2 days)
   - Read: [../learning/FEEDBACK_SPECIFICATION.md](../learning/FEEDBACK_SPECIFICATION.md)
   - Define metrics for your use case
   - Plan feedback collection

5. **Implement MAO** (2-4 weeks)
   - Build using your chosen vendor
   - Reference mode guides in: [../modes/](../modes/)
   - Follow best practices from: [ARCHE_INTEGRATION_GUIDE.md](ARCHE_INTEGRATION_GUIDE.md)

6. **Test & deploy** (1-2 weeks)
   - Create evaluation scenarios
   - Test against success metrics
   - Deploy to production

#### When to Choose This Path

✅ Your use case is unique  
✅ You want full control over architecture  
✅ You have time for custom design  
✅ Your team is experienced with multi-agent systems  

#### Related Docs

- [../frameworks/MODE_COMPATIBILITY.md](../frameworks/MODE_COMPATIBILITY.md) — Choose your modes
- [../frameworks/AGENT_ARCHETYPES.md](../frameworks/AGENT_ARCHETYPES.md) — Choose agent types
- [../modes/](../modes/) — Detailed mode guides

---

### Path 3: Improve Existing MAO 📈

**Timeline:** 1-4 weeks (ongoing)  
**Difficulty:** Varies  
**Best for:** Teams with working MAOs that need to evolve

#### What You'll Do

1. **Audit current state** (2-3 days)
   - Document current architecture
   - List agents and their roles
   - Identify pain points

2. **Plan improvements** (2-3 days)
   - Check: [../frameworks/MODE_MIGRATION_GUIDE.md](../frameworks/MODE_MIGRATION_GUIDE.md)
   - Should you change modes?
   - Should you add/remove agents?
   - Can you adopt new archetypes?

3. **Setup learning loop** (2-3 days) *if not already done*
   - Implement: [../learning/FEEDBACK_SPECIFICATION.md](../learning/FEEDBACK_SPECIFICATION.md)
   - Start collecting metrics

4. **Execute improvements** (1-2 weeks)
   - Make changes incrementally
   - Test each change
   - Monitor feedback

5. **Iterate quarterly** (ongoing)
   - Weekly: Analyze feedback
   - Monthly: Plan improvements
   - Quarterly: Major changes if needed

#### When to Choose This Path

✅ You already have a working MAO  
✅ You want to evolve it continuously  
✅ You need to adopt new patterns  
✅ You want to improve performance  

#### Related Docs

- [../frameworks/MODE_MIGRATION_GUIDE.md](../frameworks/MODE_MIGRATION_GUIDE.md) — Evolve your architecture
- [../frameworks/UPGRADE_ADVISORIES.md](../frameworks/UPGRADE_ADVISORIES.md) — Safe updates
- [../learning/FRAMEWORK_LEARNING_LOOP.md](../learning/FRAMEWORK_LEARNING_LOOP.md) — Continuous improvement

---

### Path 4: Contribute to arche 🌟

**Timeline:** Varies (3-8 weeks typical)  
**Difficulty:** Intermediate to Advanced  
**Best for:** Teams with novel patterns worth sharing

#### What You'll Do

1. **Understand contribution process** (2-3 hours)
   - Read: [../frameworks/COMMUNITY_CONTRIBUTION_PATHWAY.md](../frameworks/COMMUNITY_CONTRIBUTION_PATHWAY.md)
   - Review existing patterns for reference

2. **Identify contribution** (1-2 weeks)
   - New mode? (architectural paradigm)
   - New archetype? (agent pattern)
   - New blueprint? (domain-specific MAO)
   - Tool or enhancement?

3. **Design & document** (2-4 weeks)
   - Write RFC following template
   - Document patterns
   - Create examples

4. **Get feedback** (1-2 weeks)
   - Post for community review
   - Iterate on feedback
   - Refine based on input

5. **Merge & release** (ongoing)
   - Core team reviews
   - Adds to framework
   - Included in next release

#### When to Choose This Path

✅ You discovered a novel agent pattern  
✅ You built something others might benefit from  
✅ You want to shape arche's evolution  
✅ You have community support  

#### Related Docs

- [../frameworks/COMMUNITY_CONTRIBUTION_PATHWAY.md](../frameworks/COMMUNITY_CONTRIBUTION_PATHWAY.md) — Full contribution guide
- [../../README.md](../../README.md) — Project philosophy

---

## 🗺️ Decision Matrix

| Your Situation | Best Path | Timeline | Effort |
|---|---|---|---|
| Need to launch fast | [Use Blueprint](#path-1-use-existing-blueprint-) | 2-4 weeks | Low |
| Unique use case | [Custom MAO](#path-2-build-custom-mao-) | 4-8 weeks | High |
| Have working MAO, want to improve | [Improve Existing](#path-3-improve-existing-mao-) | 1-4 weeks | Medium |
| Built something worth sharing | [Contribute](#path-4-contribute-to-arche-) | 3-8 weeks | High |
| Combine blueprint + custom | [Hybrid](#hybrid-approach) | 3-6 weeks | Medium |

---

## 🔀 Hybrid Approach

**Many teams use a hybrid:**

1. **Start with blueprint** (gets you running)
2. **Customize over time** (adapt to your needs)
3. **Contribute improvements** (share back to community)

This is actually the recommended approach! You get the benefits of both proven patterns and customization.

**Timeline:** 6-12 weeks total  
**Effort:** Medium

---

## 🎓 Next Steps by Path

**[Path 1: Blueprint](../../blueprints/README.md)**
→ Browse available blueprints

**[Path 2: Custom](../frameworks/MODE_COMPATIBILITY.md)**
→ Study mode combinations

**[Path 3: Improve](../frameworks/MODE_MIGRATION_GUIDE.md)**
→ Plan your evolution

**[Path 4: Contribute](../frameworks/COMMUNITY_CONTRIBUTION_PATHWAY.md)**
→ Read contribution guide

**[Hybrid](ARCHE_INTEGRATION_GUIDE.md)**
→ Start with integration guide

---

## ❓ Still Unsure?

- **Quick answers** → [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
- **Full overview** → [ARCHE_INTEGRATION_GUIDE.md](ARCHE_INTEGRATION_GUIDE.md)
- **By role** → See docs/README.md

**Questions?** Open an issue on GitHub (see [../../README.md](../../README.md) for links).
