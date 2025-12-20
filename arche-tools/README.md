# Arche Management Tools

Utilities for managing arche projects and framework updates.

## Available Tools

### bootstrap.py

Initialize new projects from arche modes and forms.

**Usage:**
```bash
# Download from GitHub
curl -O https://raw.githubusercontent.com/coreyshort/arche/main/tools/bootstrap.py

# Interactive mode (recommended)
python bootstrap.py --interactive

# Direct initialization
python bootstrap.py --type automation --name "My Project"

# List available templates
python bootstrap.py --list

# Pin to specific version
python bootstrap.py --type automation --branch v1.0.0
```

**Features:**
- ✅ No dependencies (pure Python stdlib)
- ✅ No authentication required (uses public GitHub API)
- ✅ Smart fetching (only downloads needed files)
- ✅ Interactive guided setup
- ✅ Version pinning support
- ✅ Template validation

**Note:** Uses GitHub's public API which has rate limits for unauthenticated requests (60/hour per IP). For heavy usage, you can set a `GITHUB_TOKEN` environment variable to increase limits.

---

## Planned Tools

### create_issue.py *(Coming Soon)*

CLI for creating structured improvement issues with implementation details.

**Will support:**
- Interactive issue creation
- Automatic labeling by category/priority
- Template validation
- Direct GitHub API integration

---

### validate.py *(Coming Soon)*

Validate template structure and metadata.

**Will check:**
- `project.json` schema compliance
- Required files presence
- Directory structure consistency
- Cross-template compatibility

---

### test_init.py *(Coming Soon)*

Test suite for template initialization.

**Will verify:**
- All templates initialize successfully
- No missing files or broken references
- Bootstrap script works for each template
- Generated projects are valid

---

## Development

These tools are designed to be:
- **Self-contained** - No external dependencies when possible
- **Idempotent** - Safe to run multiple times
- **Well-documented** - Clear usage and error messages
- **Testable** - Can be validated automatically

## Contributing

When adding new tools:
1. Follow pure stdlib approach when feasible
2. Add comprehensive docstrings
3. Include usage examples in this README
4. Test with all template types
5. Update main arche README with new tool docs
