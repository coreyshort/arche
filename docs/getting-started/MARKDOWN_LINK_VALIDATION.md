# Markdown Link Validation Guide

**Ensuring all documentation links remain valid as the project evolves.**

---

## Overview

This guide helps you:
- **Understand** how to check markdown links
- **Prevent** broken links when making changes
- **Fix** broken links quickly
- **Automate** validation in CI/CD

---

## 🔍 Manual Validation

### Quick Check: Find Potential Broken Links

```bash
# Find all markdown links in documentation
cd c:/Users/corey/Projects/arche
grep -r "\]\([^)]*\.md\)" docs/ blueprints/ tools/ --include="*.md" | head -20
```

### Check Relative Paths Work

From any markdown file, you can test if paths work:

```bash
# From docs/getting-started/QUICK_REFERENCE.md
cd docs/getting-started
ls -la ../frameworks/MODE_COMPATIBILITY.md  # Should exist
ls -la ../../blueprints/README.md           # Should exist

# From docs/vendor-translation/README.md
cd docs/vendor-translation
ls -la ../../blueprints/BP-0003-incident-response.md  # Should exist
```

### Manual Validation Checklist

Before committing changes to documentation:

- [ ] All `[text](path.md)` links reference existing files
- [ ] Relative paths use correct depth (`../` vs `../../`)
- [ ] No broken links after moving/renaming files
- [ ] Cross-folder links use proper relative paths

---

## 📋 Path Reference Guide

**From any docs subfolder, to reach:**

| Target | From docs/getting-started/ | From docs/learning/ | From docs/vendor-translation/ |
|--------|---|---|---|
| **docs/frameworks/** | `../frameworks/` | `../frameworks/` | `../frameworks/` |
| **docs/learning/** | `../learning/` | `.` (same folder) | `../learning/` |
| **docs/getting-started/** | `.` (same folder) | `../getting-started/` | `../getting-started/` |
| **blueprints/** | `../../blueprints/` | `../../blueprints/` | `../../blueprints/` |
| **arche-tools/** | `../../arche-tools/` | `../../arche-tools/` | `../../arche-tools/` |
| **tools/** | `../../tools/` | `../../tools/` | `../../tools/` |
| **modes/** | `../../modes/` | `../../modes/` | `../../modes/` |
| **Root file** (e.g., README.md) | `../../README.md` | `../../README.md` | `../../README.md` |

**Rule of thumb:** 
- Docs subfolders are **2 levels deep**: `docs/vendor-translation/`
- To reach root → `../../`
- To reach root-level folders → `../../folder-name/`
- To reach parallel docs folders → `../folder-name/`

---

## 🐛 Common Link Mistakes

### ❌ Mistake 1: Wrong Depth

```markdown
# WRONG - From docs/getting-started/
| Go to | [../../blueprints/](../../blueprints/) |

# CORRECT
| Go to | [../../blueprints/](../../blueprints/) |

# Also CORRECT - same as above
| Go to | [blueprints](../../blueprints/) |
```

### ❌ Mistake 2: Old paths after reorganization

```markdown
# WRONG - Old structure
[See here](VENDOR_TRANSLATION_README.md)

# CORRECT - New structure  
[See here](../vendor-translation/VENDOR_TRANSLATION_README.md)
```

### ❌ Mistake 3: Absolute GitHub URLs when relative would work

```markdown
# LESS IDEAL - Absolute URL
[Read more](https://github.com/coreyshort/arche/blob/main/docs/frameworks/MODE_COMPATIBILITY.md)

# BETTER - Relative path
[Read more](../frameworks/MODE_COMPATIBILITY.md)

# WHY: Relative paths work both on GitHub and locally
```

### ❌ Mistake 4: Forgetting nested depth

```markdown
# WRONG - From docs/vendor-translation/
[Blueprint](../blueprints/README.md)  # ❌ docs/blueprints doesn't exist!

# CORRECT
[Blueprint](../../blueprints/README.md)  # ✅ reaches root-level blueprints/
```

---

## 🛠️ Validation Scripts

### Script 1: Find All Markdown Links

```bash
#!/bin/bash
# Save as: check-links.sh
# Usage: bash check-links.sh

echo "=== All Markdown Links in Project ==="
grep -r "\]\([^)]*\.md\)" docs/ blueprints/ tools/ --include="*.md" | \
  grep -v "Binary" | \
  sort

echo ""
echo "=== Total links found: ==="
grep -r "\]\([^)]*\.md\)" docs/ blueprints/ tools/ --include="*.md" | wc -l
```

### Script 2: Validate Link Paths Exist

```bash
#!/bin/bash
# Save as: validate-links.sh
# Usage: bash validate-links.sh

echo "=== Checking if linked files exist ==="

cd "$(git rev-parse --show-toplevel)" || exit 1

broken_count=0

# Extract all markdown links
grep -r "\]\([^)]*\.md\)" docs/ blueprints/ tools/ --include="*.md" -o -h | \
  sed 's/.*](\([^)]*\)).*/\1/' | \
  sort -u | while read -r link; do
    
    # Skip external links
    if [[ "$link" == http* ]]; then
      continue
    fi
    
    # Skip anchors
    if [[ "$link" == "#"* ]]; then
      continue
    fi
    
    # For each link, find which files reference it
    grep -r "\]\($link\)" docs/ blueprints/ tools/ --include="*.md" -l | while read -r file; do
      # Navigate from the file's directory to check the link
      file_dir=$(dirname "$file")
      check_path="$file_dir/$link"
      
      if [ ! -f "$check_path" ]; then
        echo "❌ BROKEN: $file references $link (doesn't exist at $check_path)"
        ((broken_count++))
      fi
    done
  done

if [ "$broken_count" -eq 0 ]; then
  echo "✅ All links valid!"
else
  echo "⚠️ Found $broken_count broken link(s)"
  exit 1
fi
```

### Script 3: Find Files Without READMEs

```bash
#!/bin/bash
# Save as: check-readmes.sh
# Usage: bash check-readmes.sh

echo "=== Checking for missing README.md files ==="
echo ""

for dir in docs docs/getting-started docs/frameworks docs/learning docs/vendor-translation blueprints tools arche-tools modes modes/3-layer modes/event-driven modes/rl-loop modes/agentic-swarm; do
  if [ -d "$dir" ]; then
    if [ ! -f "$dir/README.md" ]; then
      echo "⚠️ Missing: $dir/README.md"
    else
      echo "✅ Found: $dir/README.md"
    fi
  fi
done
```

---

## 🤖 Automated Validation (CI/CD)

### GitHub Actions Workflow

Create `.github/workflows/validate-links.yml`:

```yaml
name: Validate Markdown Links

on:
  pull_request:
    paths:
      - '**/*.md'
  push:
    branches:
      - main
    paths:
      - '**/*.md'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Install markdown-link-check
        run: npm install -g markdown-link-check
      
      - name: Check all markdown links
        run: |
          find docs blueprints tools arche-tools -name "*.md" -type f -print0 | \
          xargs -0 -I {} markdown-link-check \
            --config .markdown-link-check.json \
            --ignore "https://github.com" \
            {}
```

Create `.markdown-link-check.json`:

```json
{
  "ignorePatterns": [
    {
      "pattern": "^https://github.com"
    },
    {
      "pattern": "^http"
    }
  ],
  "replacementPatterns": [
    {
      "pattern": "^\\.\\.?/",
      "replacement": "file://"
    }
  ]
}
```

---

## ✅ Pre-Commit Checklist

Before pushing changes with markdown updates:

1. **Run the validation script**
   ```bash
   bash validate-links.sh
   ```

2. **Test relative paths manually**
   ```bash
   cd docs/getting-started
   # Try navigating the paths in your changes
   ls -la ../../blueprints/
   ```

3. **Check for common mistakes**
   - [ ] No `/docs/` in paths (should be `../` not `/docs/`)
   - [ ] Correct depth (`../../` for root, `../` for parallel folders)
   - [ ] All referenced files exist
   - [ ] No hardcoded usernames or local paths

4. **Verify in GitHub**
   - [ ] Links work in GitHub's web view
   - [ ] Links work locally with `python -m http.server`

---

## 📊 Link Inventory

### Documentation Links by Folder

**docs/getting-started/:**
- QUICK_REFERENCE.md (8 links)
- README.md (6 links)
- ARCHE_INTEGRATION_GUIDE.md (5 links)
- COMPLETION_SUMMARY.md (2 links)
- CHOOSE_YOUR_PATH.md (12 links)

**docs/frameworks/:**
- README.md (4 links)
- MODE_COMPATIBILITY.md (3 links)
- AGENT_ARCHETYPES.md (2 links)

**docs/learning/:**
- README.md (3 links)

**docs/vendor-translation/:**
- README.md (7 links)

**Total documented links: ~50+**

---

## 🔄 When Moving/Renaming Files

If you move or rename a markdown file:

1. **Find all references** to the old path
   ```bash
   grep -r "old-file-name.md" docs/ --include="*.md"
   ```

2. **Update all references** to the new path
   ```bash
   # Use multi_replace_string_in_file tool to update in bulk
   ```

3. **Test the new paths**
   ```bash
   bash validate-links.sh
   ```

4. **Check Git for broken symlinks**
   ```bash
   git status | grep "deleted"
   ```

---

## 🎯 Best Practices

✅ **DO:**
- Use relative paths for internal docs
- Keep paths 2-3 levels deep maximum
- Use descriptive link text
- Validate links before committing
- Document path conventions (like this guide!)

❌ **DON'T:**
- Use absolute file paths (`C:\Users\...`)
- Use hardcoded GitHub URLs for local docs
- Create links without testing
- Move files without updating references
- Use different path styles in same file

---

## 📚 Examples

### Example 1: Link from docs/getting-started/

```markdown
# Correct links from docs/getting-started/README.md

| Goal | Link |
|---|---|
| Same folder | [QUICK_REFERENCE.md](QUICK_REFERENCE.md) |
| Parallel folder | [../frameworks/MODE_COMPATIBILITY.md](../frameworks/MODE_COMPATIBILITY.md) |
| Root folder | [../../README.md](../../README.md) |
| Root subfolder | [../../blueprints/README.md](../../blueprints/README.md) |
| Choose path | [CHOOSE_YOUR_PATH.md](CHOOSE_YOUR_PATH.md) |
```

### Example 2: Link from docs/vendor-translation/

```markdown
# Correct links from docs/vendor-translation/README.md

| Goal | Link |
|---|---|
| Parallel folder | [../getting-started/QUICK_REFERENCE.md](../getting-started/QUICK_REFERENCE.md) |
| Other parallel | [../frameworks/MODE_COMPATIBILITY.md](../frameworks/MODE_COMPATIBILITY.md) |
| Root folder | [../../README.md](../../README.md) |
| Root subfolder | [../../blueprints/README.md](../../blueprints/README.md) |
```

---

## 🆘 Troubleshooting

**Q: Link works in VS Code but not on GitHub**  
A: Check for typos in the filename (case-sensitive on Linux/GitHub)

**Q: Can't find file from relative path**  
A: Use `pwd` to verify current directory, then trace the path with `cd ../`

**Q: Too many levels of `../`**  
A: You're probably targeting a root-level folder; use `../../folder/`

**Q: Absolute path keeps breaking**  
A: Replace with relative path: `../../../` instead of `/Users/corey/`

---

## 📞 Need Help?

- Check [Path Reference Guide](#-path-reference-guide) above
- Review [Common Mistakes](#-common-link-mistakes)
- Run validation script: `bash validate-links.sh`
- Test manually with: `cd <folder> && ls -la <path>`
