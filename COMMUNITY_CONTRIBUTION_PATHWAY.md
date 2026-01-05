# Community Contribution Pathway

**Purpose:** Enable community to propose and contribute new modes, archetypes, blueprints, and patterns to arche.

---

## Overview

arche thrives through community contributions. This guide shows how to:
- **Propose** a new mode, archetype, blueprint, or pattern
- **Refine** your proposal through community feedback
- **Contribute** your work to the arche ecosystem
- **Maintain** your contribution as it evolves

---

## Types of Contributions

### Contribution Type 1: New Mode

**What it is:** A complete architectural approach for building agents (like 3-Layer, RL-Loop, Event-Driven, etc.)

**Complexity:** ⭐⭐⭐⭐⭐ (Highest - requires core arche team involvement)

**Timeline:** 3-6 months from proposal to merge

**Requirements:**
- Solves a distinct architectural problem
- Complements existing modes (not duplicate)
- Has at least 1 working example (real or demonstration)
- Documentation: MODE.md, INSTRUCTIONS.md, pattern examples

**Process:**
1. Open GitHub issue: "RFC: [Mode Name] Mode"
   - Describe the problem it solves
   - Sketch the architecture
   - Show 2-3 example use cases
   
2. Community feedback (2 weeks)
   - Q&A from users
   - Does it fill a gap?
   - Is it distinct from existing modes?

3. Proposal acceptance (core team decides)
   - If accepted: Move to "Mode Development"
   - If rejected: Document reasoning; close issue

4. Mode development (8-12 weeks)
   - Write comprehensive MODE.md
   - Create INSTRUCTIONS.md with agent patterns
   - Build working example in `modes/[mode-name]/examples/`
   - Add test coverage
   - Integrate into MODE_SELECTION.md, MODE_COMPATIBILITY.md

5. Community review (2 weeks)
   - Early adopters try the mode
   - Feedback incorporated
   - Documentation polished

6. Merge to main
   - Released as Emerging mode (MODE_MATURITY.md)
   - Listed in mode registry
   - Added to autonomous mode selection algorithm

---

### Contribution Type 2: New Agent Archetype

**What it is:** Reusable agent pattern with template, use cases, success metrics

**Complexity:** ⭐⭐⭐ (Medium - detailed but focused)

**Timeline:** 2-4 weeks from proposal to merge

**Requirements:**
- Solves common agent design problem
- Template: Agent directive, input/output spec, mode recommendations
- Success metrics: How to evaluate if agent works
- 2+ example use cases
- Fits within existing modes

**Process:**
1. Open GitHub issue: "Propose Archetype: [Archetype Name]"
   - Describe the role: What does this agent do?
   - Problem solved: When/why would someone need this?
   - Use cases: 2-3 concrete examples
   - Mode fit: Which mode(s) work best?

2. Community feedback (1 week)
   - Similar existing archetypes? (Avoid duplication)
   - Is the template clear?
   - Success metrics measurable?

3. Archetype development (1-2 weeks)
   - Write detailed archetype markdown
   - Create template directive
   - Define success metrics
   - Add 2 examples (minimal + complex)

4. Community review (1 week)
   - Others try the archetype in their projects
   - Feedback on template clarity
   - Success metrics validation

5. Merge to main
   - Added to `AGENT_ARCHETYPES.md`
   - Referenced in relevant blueprints
   - Available for new MAO generation

---

### Contribution Type 3: Domain Blueprint

**What it is:** Complete MAO scaffold for a specific domain (incident response, content moderation, etc.)

**Complexity:** ⭐⭐⭐⭐ (High - comprehensive but bounded)

**Timeline:** 4-8 weeks from proposal to merge

**Requirements:**
- Solves known domain problem
- 4-6 agent roles defined with archetype references
- 4+ evaluation scenarios
- Governance & escalation paths
- Learning system architecture
- SLA targets if applicable

**Process:**
1. Open GitHub issue: "Propose Blueprint: [Domain Name]"
   - Describe domain: What problem does it solve?
   - Context: Why is this blueprint needed now?
   - Agent roles: 4-6 key roles in the system
   - Evaluation: 3-4 scenarios to test
   - Timeline: When would you build/ship this?

2. Community feedback (1 week)
   - Is this domain important?
   - Are there better existing blueprints?
   - Mode choices appropriate?

3. Blueprint development (2-4 weeks)
   - Write blueprint markdown (governance, learning loop, etc.)
   - Define 4+ eval scenarios with success criteria
   - Create agent templates for each role
   - Add learning system architecture
   - Document SLA/non-negotiables

4. Community review (1-2 weeks)
   - Beta testers build prototype using blueprint
   - Feedback on agent role clarity
   - Eval scenarios realistic?
   - Learning system sensible?

5. Merge to main
   - Added to `blueprint-registry.md`
   - Gets blueprint ID (BP-XXXX)
   - Becomes available for Foundry MAO generation

---

### Contribution Type 4: Pattern or Example

**What it is:** Reusable pattern, integration example, or teaching material

**Complexity:** ⭐⭐ (Low - focused, specific)

**Timeline:** 1-2 weeks from proposal to merge

**Requirements:**
- Solves specific integration/usage problem
- Code/markdown + documentation
- 1-2 example use cases
- Clear, copy-pasteable (if code)

**Process:**
1. Open GitHub discussion: "[Pattern Name] - [Use Case]"
   - What problem does this solve?
   - Why is it useful?
   - Who would benefit?

2. Community feedback (1 week)
   - Is this pattern useful?
   - Is it well-documented?
   - Any edge cases to consider?

3. Implementation (1 week)
   - Polish code/documentation
   - Add comments
   - Create example

4. Merge to main
   - Added to `pattern-library.md` (or equivalent)
   - Referenced from relevant guides
   - Available for community to use

---

## How to Propose: GitHub Templates

### Template 1: New Mode RFC

```markdown
## RFC: [Mode Name] Mode

### Problem Statement
What architectural problem does this mode solve?

### Proposed Solution
High-level sketch of how the mode works

### Example Use Cases
- Use case 1: [Domain], [specific scenario]
- Use case 2: [Domain], [specific scenario]
- Use case 3: [Domain], [specific scenario]

### Comparison to Existing Modes
How is this different from:
- 3-Layer: [comparison]
- RL-Loop: [comparison]
- Event-Driven: [comparison]
- Agentic-Swarm: [comparison]

### Initial Implementation Sketch
```
[ASCII diagram or pseudocode showing mode structure]
```

### Timeline
How long would mode development take?

### Next Steps
What feedback would be most helpful?
```

### Template 2: Propose Archetype

```markdown
## Propose Archetype: [Name]

### Role Definition
What does this agent do? (1-2 sentences)

### Problem Solved
When/why would a team need this archetype?

### Use Cases
- Case 1: [Context], [what it does]
- Case 2: [Context], [what it does]

### Suggested Mode
Which mode(s) work best for this archetype?

### Success Metrics
How would we know if this agent is working well?

### Next Steps
What would help refine this proposal?
```

### Template 3: Propose Blueprint

```markdown
## Propose Blueprint: [Domain]

### Domain Description
What problem does this domain solve?

### Agent Roles (sketch)
- Role 1: [Name and responsibility]
- Role 2: [Name and responsibility]
- [etc., 4-6 roles]

### Key Challenges
What's hard about this domain?

### Evaluation Scenarios
How would we test if the blueprint works?
- Scenario 1: [Description]
- Scenario 2: [Description]
- Scenario 3: [Description]

### Governance
Are there non-negotiables or SLAs?

### Timeline
When would you build this blueprint?

### Next Steps
What feedback would help?
```

### Template 4: Share Pattern/Example

```markdown
## [Pattern Name]

### Problem
What problem does this solve?

### Solution
[Code, architecture, or process]

### Use Cases
When would someone use this?

### Trade-offs
What are the pros/cons?

### Next Steps
How should this be refined?
```

---

## Contribution Checklist

Before proposing, ask yourself:

**New Mode:**
- [ ] Solves a distinct architectural problem?
- [ ] Complements (not duplicates) existing modes?
- [ ] Have I sketched the architecture?
- [ ] Do I have 2-3 example use cases?
- [ ] Am I prepared for 3-6 month development?

**New Archetype:**
- [ ] Solves a common agent design problem?
- [ ] Different from existing archetypes? (Check AGENT_ARCHETYPES.md)
- [ ] Have I drafted a template?
- [ ] Have I defined success metrics?
- [ ] Have I sketched 2 examples?

**Domain Blueprint:**
- [ ] Solves an important domain problem?
- [ ] Can I define 4-6 distinct agent roles?
- [ ] Have I sketched 3-4 eval scenarios?
- [ ] Do I understand governance requirements?
- [ ] Can I explain the learning system?

**Pattern/Example:**
- [ ] Solves a real problem someone faced?
- [ ] Is it generalizable (not one-off)?
- [ ] Is it well-documented?
- [ ] Are there example use cases?

---

## Review Process

### Phase 1: Initial Review (Core Team, 1 week)
- ✅ Is proposal within scope?
- ✅ Does it complement existing work?
- ✅ Is proposal clear and complete?
- ✅ Redirect to other resources if needed

### Phase 2: Community Feedback (Everyone, 1-2 weeks)
- ✅ Is this useful?
- ✅ Are there edge cases?
- ✅ Better alternative approaches?
- ✅ Support, ideas, offers to help?

### Phase 3: Development (Proposer, varies by type)
- ✅ Follow guidance from Phase 1 & 2
- ✅ Build/document the contribution
- ✅ Create examples
- ✅ Test with community members (optional)

### Phase 4: Implementation Review (Core Team + Community, 1 week)
- ✅ Quality check
- ✅ Documentation complete?
- ✅ Integrated with existing frameworks?
- ✅ Ready for production use?

### Phase 5: Merge & Release
- ✅ Added to main branch
- ✅ Listed in registries
- ✅ Announced to community
- ✅ Maintained going forward

---

## Best Practices for Contributions

### 1. Start with GitHub Issues (not Pull Requests)
- Don't code in isolation
- Get feedback early
- Avoid wasted effort on wrong approach

### 2. Write Clear Documentation
- Other people need to understand your contribution
- Assume readers have arche context but not deep domain knowledge
- Include examples and diagrams

### 3. Integrate with Existing Frameworks
- Your contribution should fit into arche ecosystem
- Reference relevant modes, archetypes, patterns
- Update registries and cross-references

### 4. Test and Validate
- Show working examples
- Have community members try it
- Gather evidence that it works

### 5. Be Open to Feedback
- Criticism of your contribution is not personal
- Be willing to refine/revise
- Community makes contributions stronger

### 6. Maintain Your Contribution
- After merge, monitor for issues
- Update when related work evolves
- Help others use your contribution

---

## Frequently Asked Questions

**Q: Can I propose a mode without a working implementation?**

A: For modes, a sketch or prototype is good; full implementation happens during development phase. For archetypes and blueprints, you should have a fairly complete draft before proposing.

**Q: How long does review take?**

A: 1-2 weeks for initial feedback, then development phase varies (1 week to 6 months depending on scope), then 1 week for implementation review. Plan accordingly.

**Q: What if my proposal gets rejected?**

A: We'll explain why. Usually it's one of:
- Overlaps with existing work
- Timing not right
- Doesn't fit arche philosophy
- Needs more development before proposing

If rejected, you can still use it for your own projects; it just won't be part of official arche.

**Q: Can I contribute as a community member (not core team)?**

A: Absolutely. arche is designed for community contributions. You don't need to be on the core team; just start with an issue and let's discuss.

**Q: How do I stay connected after contributing?**

A: Several ways:
- Join GitHub discussions
- Subscribe to issues related to your contribution
- Help review others' proposals
- Attend community calls (if we have them)

**Q: Can I contribute proprietary patterns?**

A: Yes, but they need to fit arche's open philosophy. Trade secrets should stay proprietary; patterns and learnings should be shareable. If unsure, ask.

---

## Community Guidelines

When contributing or reviewing others' contributions:

✅ **Do:**
- Be respectful and constructive
- Ask clarifying questions
- Share domain expertise
- Help reviewers understand your contribution
- Celebrate others' work

❌ **Don't:**
- Dismiss ideas without explanation
- Push your idea as "the only right way"
- Ignore feedback
- Contribute code without documentation
- Assume others understand your domain

---

## Next: Start Contributing!

1. **Browse existing issues** in GitHub
2. **Identify a gap** you can help with
3. **Read this guide** (you're doing it!)
4. **Open an issue** using template above
5. **Engage with community** feedback
6. **Build something great**
7. **Submit to arche**
8. **Celebrate!** 🎉

Questions? Ask in GitHub discussions or contact core team.

---

