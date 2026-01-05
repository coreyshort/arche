# Changelog

All notable changes to arche will be documented in this file.

## [2.0.0] - January 5, 2026

### 📌 IMPORTANT: Backwards Compatible Release

**This is a documentation-only upgrade.** No breaking changes. All v1.x projects continue working without any modifications.

→ **For v1.x users:** See [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) for upgrade information (spoiler: no action needed to keep working, but you'll want the docs improvements)

### 🎉 Major Improvements

- **Cross-Folder Navigation:** All documentation sections now interconnected with "See Also" sections for seamless navigation between frameworks, vendor-translation, and learning docs
- **Discoverability:** CHOOSE_YOUR_PATH guide now linked from root README and AI_QUICKSTART for better user onboarding
- **Resource Hub:** docs/README.md now showcases all resource folders (blueprints, modes, arche-tools, examples, tools) with clear purpose statements
- **Framework Integration:** Vendor-translation and framework docs now cross-reference each other through "See Also" sections

### 📚 What's New

- "See Also" sections added to 5 framework documentation files (MODE_COMPATIBILITY, AGENT_ARCHETYPES, MODE_MIGRATION_GUIDE, UPGRADE_ADVISORIES, COMMUNITY_CONTRIBUTION_PATHWAY)
- "See Also" sections added to 3 vendor-translation files (VENDOR_SELECTION_DECISION_TREE, VENDOR_TRANSLATION_SPECIFICATION, VENDOR_INTEGRATION_GUIDE)
- Related Resources section added to docs/README.md
- Blueprint placeholders created (BP-0003, BP-0004, BP-0005) with "Coming Soon" status
- Enhanced AI agent navigation guidance in AI_QUICKSTART.md
- New MIGRATION_GUIDE.md for upgrading from v1.x

### 🔧 Improvements

- Fixed blueprint file references in ARCHE_INTEGRATION_GUIDE.md
- Better visibility for learning loop documentation
- Clearer path selection workflow for new users
- Improved cross-documentation visibility and discoverability

### ⚠️ Known Status

- **Blueprint Examples:** BP-0003 (Incident Response), BP-0004 (Content Moderation), and BP-0005 (Data Operations) are in development with "Coming Soon" status. Structure and rationale documented, full implementation arriving Q1 2026.
- **Vendor Examples:** Worked example available for Claude (see EXAMPLE_BP0004_TO_CLAUDE.md). Additional vendor translation examples in development.

### 📖 Documentation Statistics

- 50+ documentation files with coherent structure
- 8 new "See Also" cross-reference sections
- 1 new Related Resources hub
- 3 new blueprint placeholder files
- 400+ cross-folder links (all tested and working)

### Next Steps

- Complete full blueprint documentation (Q1 2026)
- Expand vendor translation examples to all supported platforms
- Add more domain-specific blueprint templates based on community feedback

---

## [0.2.0] - January 4, 2026

### Added
- Blueprint registry with BP-0003 (industrial PM / Pragmatic)
- Pattern library (dimensions, archetypes, anti-patterns)
- Patch pack system with starter patches
- Foundry rubric and evaluation scenarios
- Minimal example generated MAO
