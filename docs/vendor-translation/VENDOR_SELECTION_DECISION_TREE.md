# Vendor Selection Decision Tree

**Purpose:** Help teams choose the best vendor for their specific arche MAO.

**Version:** 1.0 (January 2026)  
**Status:** Selection framework

---

## Quick Decision Path

Answer these questions in order:

### Question 1: What's Your Primary Constraint?

**A) Enterprise integration requirement** (Must work with existing corporate systems)
→ **Go to: Enterprise Path** (See below)

**B) Speed to production** (Need live as fast as possible)
→ **Go to: Speed Path**

**C) Multimodal capability** (Need image, audio, video processing)
→ **Go to: Multimodal Path**

**D) Full control over infrastructure** (Hosting, security, customization)
→ **Go to: Self-Hosted Path**

**E) Cost optimization** (Minimize ongoing expenses)
→ **Go to: Cost Path**

**F) Advanced multi-agent coordination** (Complex agent-to-agent interaction)
→ **Go to: Coordination Path**

---

## Decision Paths

### Enterprise Path
*For teams in Fortune 500 companies, regulated industries, strict governance*

#### Question: What's your IT landscape?

**Microsoft ecosystem → Copilot Studio**
- Works with Azure services
- AD/SSO integration built-in
- HIPAA/FedRAMP compliance available
- SharePoint/Teams native integration
- **Deployment time:** 2-4 weeks
- **Best for:** Healthcare, Finance, Government

**AWS/GCP dominant → Claude Projects + custom deployment**
- Claude API works with any infrastructure
- Deploy to Lambda, Cloud Run, or VMs
- Full control over data residency
- **Deployment time:** 3-6 weeks
- **Best for:** Tech companies, startups with cloud preference

**Salesforce/Dynamics → Check if vendor has CRM connectors**
- Copilot Studio integrates with Dynamics 365
- Claude via REST API to Salesforce
- **Deployment time:** 2-4 weeks
- **Best for:** CRM-heavy companies

---

### Speed Path
*For teams needing production in days, not weeks*

#### Recommendation: **Claude Projects** (Fastest)

**Why:**
- Create project in claude.ai in 5 minutes
- Add agents in 30 minutes each
- Deploy same day (no infrastructure)
- Learning loops work immediately
- **Total time to production:** 1-3 days

**Process:**
```
Day 1:  Create project + add agents
Day 2:  Add tools + configure logging
Day 3:  Test + deploy to production
```

#### Alternative: **Gemini Agents** (If you prefer Google)

**Why:**
- Similar speed to Claude
- Cloud Run auto-scaling reduces setup
- **Total time to production:** 2-4 days

---

### Multimodal Path
*For MAOs processing images, audio, video, or mixed content*

#### Primary: **Gemini with Agents** (Best multimodal)

**Capabilities:**
- Image understanding (Gemini Vision)
- Audio processing (Gemini 2.0 Audio)
- Video analysis
- Text generation
- All in same agent

**Example use case:** Content moderation MAO that handles images/video/text

#### Secondary: **Claude Projects** (Good multimodal)

**Capabilities:**
- Image analysis and understanding
- File analysis (documents, screenshots)
- Vision-enabled tools
- Text output

**Note:** Claude doesn't process raw audio/video yet, but excellent for image+text

#### Not recommended for multimodal:
- Copilot Studio (limited to text primarily)
- Swarm (local only, same model)
- AutoGen (no built-in multimodal)
- LangGraph (framework, not execution)

---

### Self-Hosted Path
*For teams with data residency requirements, custom infrastructure, air-gapped environments*

#### Tier 1: **Swarm** (Recommended)

**Why:**
- Pure Python, runs anywhere
- No vendor dependency
- Full control over model (use any local model)
- Deterministic (no API variation)
- **Infrastructure:** Single server or laptop

**Trade-offs:**
- You manage model quality/updates
- No cloud scaling
- Limited to open models (or self-hosted API)

**Example:**
```python
# Use with Ollama locally, LM Studio, vLLM, etc.
swarm = Swarm(
    agents=my_agents,
    model="local-llm"  # Your local model
)
```

#### Tier 2: **AutoGen** (Self-hosted option)

**Why:**
- Open source, deploy to your infrastructure
- Supports multiple models (including local)
- Good for team-based swarm
- Learning loops via local logging

**Trade-offs:**
- Requires more setup than Swarm
- Team coordination more complex
- Less mature than Swarm

#### Not self-hosted:
- Claude Projects (cloud-only)
- Copilot Studio (cloud-only)
- Gemini with Agents (cloud-only)

---

### Cost Path
*For teams optimizing for lowest total cost of ownership*

#### Lowest cost options (in order):

**1. Swarm (Open source) - FREE**
- No per-call costs
- Host on $5/month VPS
- **Cost:** ~$100/year + labor

**2. Claude Projects - LOW**
- Pay-per-API-call (Claude model)
- Run in free tier: ~$20-100/month
- Scale to production: ~$500-2000/month
- **Cost:** Variable based on usage

**3. Gemini with Agents - LOW**
- Pay-per-1M tokens
- Competitive with Claude
- Often cheaper at scale: ~$200-1000/month
- **Cost:** $300-1500/month

**4. Copilot Studio - MEDIUM**
- Per-user licensing ($15-30/month per user)
- Plus infrastructure (Azure)
- **Cost:** $500-3000/month (depends on users)

**5. AutoGen (self-hosted) - LOW**
- No API costs
- Infrastructure costs
- **Cost:** $100-500/month + labor

**6. LangGraph (self-hosted) - LOW**
- Framework only (no model)
- Use Claude API + self-hosted: ~$300+/month
- Or local model: ~$100-300/month

#### Cost optimization tips:

✅ Use Claude for high-volume, simple tasks
✅ Use Swarm locally if latency not critical
✅ Cache frequently used data in vector DBs
✅ Batch similar requests together
✅ Monitor token usage weekly
✅ Use smaller models for deterministic tasks
✅ Implement rate limiting to control costs

---

### Coordination Path
*For complex multi-agent orchestration scenarios*

#### Best for multi-agent:

**1. Agentic-Swarm (Claude Projects)**
- Ask-and-combine pattern
- Coordinator + specialists
- Works well up to ~10 agents
- **Good for:** Decision-making swarms (voting, consensus)

**2. Agentic-Swarm (Copilot Studio)**
- Skill routing and delegation
- Conversation-based coordination
- Works well for up to ~8 agents
- **Good for:** Team-based coordination, handoffs

**3. Swarm (Python library)**
- Function-based routing
- Can coordinate unlimited agents
- Deterministic hand-offs
- **Good for:** Complex flows, local coordination

**4. AutoGen (Multi-agent conversational)**
- Agents debate and discuss
- Self-organizing
- Works well for 3-7 agents
- **Good for:** Brainstorming, consensus decisions

**5. LangGraph (Custom orchestration)**
- Define state graphs
- Full control over routing
- Unlimited complexity
- **Complexity:** Requires developer expertise
- **Good for:** Custom workflows not fitting standard patterns

#### Not recommended for complex coordination:
- Gemini (good for single agents)
- Standalone Claude (better with Projects)

---

## Full Comparison Matrix

| Factor | Claude Projects | Copilot Studio | Gemini | Swarm | AutoGen | LangGraph |
|--------|---|---|---|---|---|---|
| **Speed to production** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐ |
| **Multimodal** | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | N/A | ⭐⭐⭐ | N/A |
| **Cost (small scale)** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Enterprise integrations** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐ | ⭐⭐ | ⭐ |
| **Self-hosted option** | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| **Multi-agent coordination** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Learning loop native** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Vendor lock-in risk** | 🔴 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |
| **Model selection** | Claude only | GPT/Claude/Local | Gemini only | Any model | Any model | Any model |
| **Setup complexity** | 🟢 Easy | 🟡 Medium | 🟡 Medium | 🟡 Medium | 🔴 Hard | 🔴 Hard |

---

## Decision Tree Summary (All Paths)

```
START: What's your constraint?
│
├─ Enterprise integrations?
│  ├─ Yes, Microsoft ecosystem → COPILOT STUDIO
│  ├─ Yes, AWS/GCP → CLAUDE + Custom deployment
│  └─ Yes, Salesforce → Check vendor CRM connectors
│
├─ Speed critical (days, not weeks)?
│  └─ Yes → CLAUDE PROJECTS (fastest)
│
├─ Multimodal (images, audio, video)?
│  ├─ Yes → GEMINI WITH AGENTS (best)
│  └─ Maybe → CLAUDE PROJECTS (good)
│
├─ Self-hosted required (data residency)?
│  ├─ Yes, Python project → SWARM
│  ├─ Yes, distributed team → AUTOGEN
│  └─ Yes, complex flows → LANGGRAPH
│
├─ Cost optimization?
│  ├─ Lowest cost → SWARM (open source)
│  ├─ Low cost, cloud → CLAUDE or GEMINI
│  └─ Self-hosted low cost → SWARM or AUTOGEN
│
└─ Complex multi-agent coordination?
   ├─ Yes, many agents → SWARM, AUTOGEN, or LANGGRAPH
   ├─ Yes, enterprise → COPILOT STUDIO or AUTOGEN
   └─ Yes, custom workflows → LANGGRAPH
```

---

## Recommended Combinations (Common Scenarios)

### Scenario 1: "Startup MVP, fastest to market"
**Choice:** Claude Projects
- Deploy today
- Add learning loops immediately
- Scale as you grow
- Migrate later if needed

### Scenario 2: "Enterprise financial services"
**Choice:** Copilot Studio + Swarm backup
- Compliance and governance
- Microsoft ecosystem
- Self-hosted fallback if needed
- Learning loops in Azure

### Scenario 3: "Content moderation at scale"
**Choice:** Gemini with Agents
- Handle images/video/text
- Auto-scaling on Cloud Run
- Logs to Cloud Logging for feedback
- Cost efficient at volume

### Scenario 4: "Distributed AI team, high customization"
**Choice:** Swarm (locally) + Claude API (for quality)
- Full control
- Team coordination via local codebase
- No vendor lock-in
- Can test models locally first

### Scenario 5: "Healthcare, strict data residency"
**Choice:** Swarm with local Ollama
- All data stays on-premises
- Deterministic execution
- Audit trail under your control
- Learning logs in your database

### Scenario 6: "Complex workflow orchestration"
**Choice:** LangGraph
- Define exact state flow
- Multiple decision points
- Integration with existing systems
- Requires developer expertise

---

## Migration Path (If You Choose Wrong)

Good news: arche design makes it easy to change vendors!

```
Scenario: Deployed to Claude Projects, now want Swarm

Step 1: Export your arche MAO from Claude
Step 2: Run foundry-translate --target swarm
Step 3: Deploy to Swarm
Step 4: Learning loops migrate (same format)

Time: 1-2 weeks
```

**That's why keeping arche MAO as source of truth matters.**

---

## Final Recommendation Algorithm

```python
def recommend_vendor(constraints):
    """Recommend vendor based on constraints"""
    
    score = {}  # vendor -> score
    
    # Enterprise requirement
    if constraints.get("enterprise_required"):
        if "microsoft_ecosystem" in constraints:
            score["copilot"] = 100
        else:
            score["claude"] += 50
            score["gemini"] += 50
    
    # Speed critical
    if constraints.get("speed_critical"):
        score["claude"] += 80  # Projects is fastest
        score["gemini"] += 60
    
    # Multimodal
    if constraints.get("multimodal"):
        score["gemini"] = 100
        score["claude"] += 70
    
    # Self-hosted
    if constraints.get("self_hosted"):
        score["swarm"] = 100
        score["autogen"] += 50
        score["langgraph"] += 50
    
    # Cost optimization
    if constraints.get("cost_critical"):
        score["swarm"] += 80  # Free
        score["claude"] += 50
        score["gemini"] += 50
    
    # Complex coordination
    if constraints.get("complex_multi_agent"):
        score["swarm"] += 80
        score["autogen"] += 90
        score["langgraph"] += 100
    
    return sorted(score.items(), key=lambda x: x[1], reverse=True)
```

---

## Next Steps

1. **Answer the questions** above for your MAO
2. **Check the recommended path** for your constraints
3. **Review the implementation guide** (VENDOR_INTEGRATION_GUIDE.md)
4. **Deploy to chosen vendor** with confidence
5. **Set up learning loops** immediately
6. **Track improvements** weekly

---

## See Also

- [VENDOR_TRANSLATION_SPECIFICATION.md](VENDOR_TRANSLATION_SPECIFICATION.md) — Complete architecture and vendor specs
- [VENDOR_INTEGRATION_GUIDE.md](VENDOR_INTEGRATION_GUIDE.md) — Step-by-step translation guide
- [../frameworks/MODE_COMPATIBILITY.md](../frameworks/MODE_COMPATIBILITY.md) — Mode compatibility considerations
- [../learning/](../learning/) — Setup feedback loops for vendor deployments
- [../../blueprints/](../../blueprints/) — Real-world MAO examples to translate
- [../README.md](../README.md) — Vendor translation documentation overview

---

