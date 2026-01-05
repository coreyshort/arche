# Vendor Translation Quick Reference

**Use this card to quickly navigate vendor translation resources and make decisions.**

---

## 📋 At a Glance

```
Want to...                          Go to...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Choose a vendor?                    VENDOR_SELECTION_DECISION_TREE.md
Translate your MAO?                 VENDOR_INTEGRATION_GUIDE.md
Understand the system?              VENDOR_TRANSLATION_SPECIFICATION.md
See a working example?              EXAMPLE_BP0004_TO_CLAUDE.md
Understand the plan?                VENDOR_TRANSLATION_IMPLEMENTATION_SUMMARY.md
```

---

## 🎯 Quick Decision (1 min)

### My primary need is:

| Need | Recommended Vendor | Why | Setup Time |
|------|---|---|---|
| **Fastest to production** | Claude Projects | Simplest UI, live in hours | 1-3 days |
| **Enterprise compliance** | Copilot Studio | AD/SSO, governance, compliance | 2-4 weeks |
| **Multimodal (images/audio)** | Gemini with Agents | Vision + audio native | 2-4 days |
| **Full control/self-hosted** | Swarm (Python) | Pure code, no vendor | 2-3 days |
| **Team multi-agent work** | AutoGen | Distributed coordination | 3-5 days |
| **Complex custom workflows** | LangGraph | Maximum flexibility | 2-4 weeks |

---

## 🚀 Translate Your MAO (5 steps)

### Step 1: Get your arche MAO
```
my-mao/
├── 00_governance/FOUNDRY_CONTRACT.md
├── 01_agents/[agent definitions]
├── 02_blueprints/[optional architecture]
└── 09_learning/[feedback & eval scenarios]
```

### Step 2: Choose vendor
```bash
# Run decision tree or refer to quick decision table above
```

### Step 3: Translate
```bash
# Manual translation (until foundry-translate available)
# Follow: VENDOR_INTEGRATION_GUIDE.md
# Example: EXAMPLE_BP0004_TO_CLAUDE.md
```

### Step 4: Test
```bash
# Run all evaluation scenarios
# Should pass: 95%+ success rate
```

### Step 5: Deploy
```bash
# Deploy to vendor (process varies by vendor)
# Setup learning loops immediately
# Begin weekly improvement cycle
```

**Total time:** 1-3 weeks (varies by MAO size and vendor)

---

## 📊 Vendor Comparison

### Tier 1: Cloud (Ready Now)

```
CLAUDE PROJECTS
├─ Best for: Fastest MVP
├─ Multimodal: ✓ Images
├─ Self-hosted: ✗
├─ Cost: LOW
├─ Setup: 1-3 days
└─ Agents: Up to ~10

COPILOT STUDIO
├─ Best for: Enterprise
├─ Multimodal: ⚠️ Limited
├─ Self-hosted: ✗
├─ Cost: MEDIUM
├─ Setup: 2-4 weeks
└─ Agents: Unlimited

GEMINI WITH AGENTS
├─ Best for: Multimodal
├─ Multimodal: ✓ Vision + Audio
├─ Self-hosted: ✗
├─ Cost: LOW
├─ Setup: 2-4 days
└─ Agents: Unlimited
```

### Tier 2: Flexible (Phase 2)

```
SWARM
├─ Best for: Self-hosted
├─ Multimodal: Framework-agnostic
├─ Self-hosted: ✓ Full control
├─ Cost: FREE (+ hosting)
├─ Setup: 2-3 days
└─ Agents: Unlimited

AUTOGEN
├─ Best for: Distributed teams
├─ Multimodal: ✓ Via tools
├─ Self-hosted: ✓
├─ Cost: FREE (+ hosting)
├─ Setup: 3-5 days
└─ Agents: Unlimited
```

### Tier 3: Custom (Phase 3)

```
LANGGRAPH
├─ Best for: Custom workflows
├─ Multimodal: Via tools
├─ Self-hosted: ✓
├─ Cost: Framework free
├─ Setup: 2-4 weeks
└─ Agents: Unlimited complexity
```

---

## 🔄 Learning Loop Cycle (Weekly)

```
MONDAY 9 AM:
Collect feedback on last week's decisions
├─ Query: All agent decisions + human outcomes
└─ Output: accuracy_rate, error_patterns

MONDAY 10 AM:
Analyze patterns
├─ Identify: False positives/negatives
└─ Output: recommendations for improvement

TUESDAY:
Review findings
├─ Team discusses: Should we change anything?
└─ Decision: Implement change or monitor more

WEDNESDAY (if change approved):
Deploy improvement
├─ Update: arche MAO documentation
├─ Re-translate: to vendor format
└─ Deploy: Updated version to production

THURSDAY-FRIDAY:
Monitor
├─ Watch: Is improvement helping?
└─ Track: New metrics validate improvement

REPEAT NEXT WEEK
└─ Continuous improvement cycle
```

---

## 🛠️ Translation Process (High Level)

```
INPUT: arche MAO (vendor-agnostic)
  ├─ governance (what's the MAO?)
  ├─ agents (which agents needed?)
  ├─ mode (3-Layer, RL-Loop, etc?)
  └─ learning (feedback setup?)
           ↓
PARSE & ANALYZE
  ├─ Extract agent roles
  ├─ Identify decision points
  ├─ Map to vendor capabilities
  └─ Check compatibility
           ↓
TRANSLATE
  ├─ Agent 1 → Vendor format
  ├─ Agent 2 → Vendor format
  ├─ Tools → Vendor format
  └─ Learning → Vendor format
           ↓
GENERATE
  ├─ Project config
  ├─ Agent definitions
  ├─ Tool definitions
  └─ Test cases
           ↓
VALIDATE
  ├─ Run eval scenarios
  ├─ Check all scenarios pass
  └─ Verify learning setup
           ↓
OUTPUT: Production-ready vendor deployment
```

---

## 📁 Key Files

### For Decision-Making
- `VENDOR_SELECTION_DECISION_TREE.md` - Help choose vendor
- `VENDOR_TRANSLATION_SPECIFICATION.md` - Why & how translation works

### For Implementation
- `VENDOR_INTEGRATION_GUIDE.md` - How to translate (modes, vendors, learning loops)
- `EXAMPLE_BP0004_TO_CLAUDE.md` - Concrete worked example

### For Planning
- `VENDOR_TRANSLATION_IMPLEMENTATION_SUMMARY.md` - Full roadmap & timeline
- This file - Quick reference

---

## 🎓 Mode-Specific Translation

### 3-Layer Mode (Deterministic)
```
arche: Follow steps exactly
claude: System prompt with step-by-step instructions
copilot: Sequential skill calling
swarm: Function-based routing (sequential)
```

### RL-Loop Mode (Learning from Outcomes)
```
arche: Log decisions, learn from outcomes, improve
claude: Tool for storing learned patterns + system prompt to use them
gemini: Use learned thresholds in agent logic
swarm: Store successful patterns in agent state
```

### Event-Driven Mode (Reactive)
```
arche: Respond to events immediately
claude: Process event, take action, return (all within tool call)
gemini: Cloud Functions/Run handle event trigger
swarm: Listen for events, route to handler
```

### Agentic-Swarm Mode (Multi-Agent)
```
arche: Coordinator asks specialists for input, synthesizes
claude: Coordinator agent calls specialist agents via tools
copilot: Conversation routing to skills
autogen: Agents discuss and debate
langgraph: State machine controls transitions
```

---

## ❌ Common Mistakes to Avoid

```
❌ Edit vendor output directly
   → Regenerate from source (arche MAO)

❌ Skip evaluation scenarios
   → Always test before production

❌ Forget learning loop setup
   → Learning is mandatory, not optional

❌ Use different versions for different vendors
   → One arche MAO, multiple vendor outputs

❌ Hardcode vendor-specific logic in arche MAO
   → Keep arche vendor-agnostic

❌ Ignore feedback for weeks
   → Weekly learning cycle is key

✅ Keep arche MAO as source of truth
✅ Regenerate vendor format when MAO changes
✅ Test all evaluation scenarios
✅ Setup learning loops immediately
✅ Review feedback weekly
✅ Keep vendor formats isolated
```

---

## 📞 Quick Troubleshooting

| Problem | Check | Solution |
|---------|-------|----------|
| Agent not responding | Tool definitions | Verify tool JSON matches schema |
| Evaluation fails | Test case assumptions | Review if scenario is realistic |
| Learning not happening | Logging enabled? | Verify log tool is being called |
| Accuracy low | Agent prompt clarity | Review system prompt instructions |
| Performance slow | Vendor limits | Check rate limits, model size |
| Can't migrate vendor | Source still MAO? | Verify you have original arche MAO |

---

## 🎯 Success Criteria

### For Your Translation

- [ ] All agents translated to vendor format
- [ ] All tools defined with correct JSON schemas
- [ ] All evaluation scenarios pass (95%+ success)
- [ ] Learning loop configured and logging
- [ ] Feedback collection working
- [ ] Weekly analysis automation scheduled
- [ ] Improvement deployment process defined

### For Your MAO

- [ ] Accuracy target met (90%+)
- [ ] False positive rate acceptable (< 5%)
- [ ] False negative rate acceptable (< 5%)
- [ ] Response time meets requirements
- [ ] Weekly improvements being made
- [ ] Team satisfied with performance

---

## 🚀 Phase Rollout

```
PHASE 1 (4-6 weeks): Tier 1 Vendors
├─ Claude Projects      ✓ Easy
├─ Copilot Studio       ✓ Complex
└─ Gemini with Agents   ✓ Multimodal

PHASE 2 (6-8 weeks): Tier 2 Vendors
├─ OpenAI Swarm         Add
└─ AutoGen              Add

PHASE 3 (8-12 weeks): Tier 3 + Ecosystem
├─ LangGraph            Add
└─ Community distros    Add

TODAY: Ready to start Phase 1!
```

---

## 📈 Metrics to Track

**Weekly:**
- Accuracy rate
- False positive count
- False negative count
- Response time (p50, p95, p99)

**Monthly:**
- Cumulative learning improvements
- Vendor comparison (is one better?)
- User satisfaction
- Cost per decision

**Quarterly:**
- Migration readiness (could we switch vendors?)
- Feedback quality improvement
- New capabilities added
- Blueprint community contributions

---

## 💡 Pro Tips

- Start with Claude Projects (fastest learning)
- Keep evaluation scenarios comprehensive
- Review feedback even if on track
- Document why vendor was chosen
- Plan migration path from day 1
- Test vendor switching early (while low volume)
- Share learnings with other teams using same vendor

---

## 🔗 Related arche Documents

- `VENDOR_TRANSLATION_SPECIFICATION.md` - Architecture & design
- `MODE_COMPATIBILITY.md` - Understanding mode combinations
- `AGENT_ARCHETYPES.md` - Agent pattern library
- `BP-0003-incident-response.md` - Example MAO (can translate)
- `BP-0004-content-moderation.md` - Example MAO (see EXAMPLE_BP0004_TO_CLAUDE.md)
- `BP-0005-data-operations.md` - Example MAO (can translate)
- `FEEDBACK_SPECIFICATION.md` - Feedback loop details

---

## ⏱️ Time Estimates

| Task | Time | Notes |
|------|------|-------|
| Choose vendor | 30 min | Use decision tree |
| Read guides | 2-3 hours | Understand process |
| Design translation | 1-2 days | Plan how agents map |
| Implement | 5-10 days | Build agent definitions, tools |
| Test | 2-5 days | Run eval scenarios |
| Deploy | 1-2 days | Setup in vendor |
| Monitor (week 1) | 2-3 hours/day | Watch closely |
| Weekly operation | 2-3 hours/week | Feedback + learning |
| **Total to production** | **1-3 weeks** | Depends on MAO size |

---

## 🎯 Next Action

1. **Read the section that matches your need** (from "At a Glance" above)
2. **Use the referenced document** for detailed guidance
3. **Follow the step-by-step process** in VENDOR_INTEGRATION_GUIDE.md
4. **Test with evaluation scenarios**
5. **Deploy and start weekly learning cycle**

**Questions?** Refer to full documentation files listed above.

---

**Version:** 1.0  
**Last Updated:** January 5, 2026  
**Status:** ✅ Ready for Phase 1 implementation

