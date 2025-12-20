# Mode Maturity Model

Arche modes progress through maturity stages based on real-world adoption, stability, and completeness.

## Maturity Levels

### 🌱 Proposed
**Definition:** Conceptual mode with compelling real-world evidence but not yet structured.

**Criteria:**
- Multiple production examples demonstrating the pattern
- Clear problem that existing modes don't solve
- Community/industry validation of the approach
- Not yet implemented in arche structure

**Status:** Awaiting maintainer approval to create mode structure

**Example:** A new paradigm identified through GitHub Issue with NEW_MODE_PROPOSAL

---

### 🔨 Experimental
**Definition:** Mode structure created, actively being shaped by early adopters.

**Criteria:**
- MODE.md and INSTRUCTIONS.md exist
- At least 1-2 initial forms created
- Limited production usage (< 10 known projects)
- Patterns still stabilizing, breaking changes likely
- Community actively discovering best practices

**Guidance:** Use if pioneering this paradigm. Expect iteration and refinement.

---

### 🚀 Emerging
**Definition:** Mode proven in production, patterns stabilizing, growing adoption.

**Criteria:**
- 10-50 known production projects using this mode
- Patterns documented and reliable
- Multiple forms available for different use cases
- Active community contributing improvements
- Minor iterations expected, major architecture stable

**Guidance:** Safe for production use. Patterns are proven but ecosystem still growing.

**Current modes:** agentic-swarm, event-driven, rl-loop

---

### ✅ Mature
**Definition:** Battle-tested mode with extensive adoption and stable patterns.

**Criteria:**
- 50+ production projects (or industry-wide adoption)
- Patterns fully documented with extensive examples
- Rich form ecosystem covering major use cases
- Minimal breaking changes, improvements are refinements
- Strong community, established best practices
- Proven reliability over extended time (6+ months)

**Guidance:** Recommended for most projects in this paradigm. Fully production-ready.

**Current modes:** 3-layer

---

### 🏛️ Legacy
**Definition:** Superseded by newer modes but maintained for existing projects.

**Criteria:**
- Functionality preserved but not actively developed
- Better alternatives now exist in other modes
- Security/compatibility updates only
- No new forms or features planned

**Guidance:** Existing projects can continue safely. New projects should consider alternative modes.

**Current modes:** None

---

### 🔒 Deprecated
**Definition:** No longer maintained. Migration path provided.

**Criteria:**
- Known issues or fundamental limitations
- Better alternatives available
- Migration guide to replacement mode/form
- No further updates or support

**Guidance:** Do not use. Migrate to recommended alternative.

**Current modes:** None

---

## Status Evolution

Mode status evolves based on:
- **Production adoption** (tracked through GitHub Discussions, Issues, user reports)
- **Pattern stability** (breaking changes decrease over time)
- **Community feedback** (improvement issues, discussions, contributions)
- **Form ecosystem** (number and diversity of available forms)
- **Time in production** (proven reliability over months/years)

### Requesting Status Changes

If a mode's status should be updated (e.g., Emerging → Mature):

1. Create GitHub Issue with:
   - Current status and proposed status
   - Evidence supporting the change (adoption metrics, stability indicators, community growth)
   - Links to production examples, discussions, improvement issues
   
2. Maintainer reviews evidence and community feedback

3. If approved:
   - MODE.md status updated
   - README.md mode listing updated
   - Announcement in GitHub Discussions

### Transparency

Mode maturity is tracked openly:
- Each MODE.md shows current status
- Status rationale documented in mode's README section
- Evolution history visible in git commits
- Community can challenge/advocate for status changes through Issues

---

**Philosophy:** Status reflects reality, not aspiration. Modes advance through demonstrated production use, not timelines. A mode can remain Experimental indefinitely if adoption doesn't materialize—and that's valuable information for the ecosystem.
