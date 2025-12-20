# Quick Reference: Creating Issues as an AI Agent

## One-Time Setup (2 minutes)

1. **Get GitHub Token:**
   - Visit: https://github.com/settings/tokens
   - Click "Generate new token (classic)"
   - Name: `arche-improvements`
   - Scope: ✅ `public_repo` only
   - Copy token

2. **Save Token:**
   ```bash
   echo "export GITHUB_TOKEN=ghp_yourTokenHere" >> ~/.bashrc
   source ~/.bashrc
   ```

## Creating an Issue (30 seconds)

```bash
python .github/create_issue.py \
  --title "Your improvement title" \
  --mode "3-layer" \
  --category "documentation" \
  --priority "medium" \
  --problem "What's wrong or missing?" \
  --solution "How to fix it"
```

## Available Options

**Modes:** `3-layer`, `agentic-swarm`, `event-driven`, `rl-loop`, `cross-mode`, `new-mode`

**Categories:** `mode-architecture`, `form-template`, `bootstrap`, `documentation`, `seo-discoverability`, `marketing-outreach`, `social-media`, `community-growth`, `other`

**Priority:** `critical`, `high`, `medium`, `low`

## Optional Fields

Add implementation details:
```bash
--implementation "```diff
- old code
+ new code
```"
```

Add commit message:
```bash
--commit-message "feat: add better validation"
```

Add testing steps:
```bash
--testing "1. Run script 2. Verify output 3. Check edge cases"
```

## Testing First (Dry Run)

```bash
python .github/create_issue.py \
  --title "Test" \
  --mode "3-layer" \
  --category "documentation" \
  --priority "low" \
  --problem "Test" \
  --solution "Test" \
  --dry-run  # ← Shows what would be created without creating it
```

## Troubleshooting

**Error: "GITHUB_TOKEN not set"**
```bash
export GITHUB_TOKEN=ghp_yourToken
```

**Error: "Bad credentials"**
- Token is wrong or expired
- Get new token: https://github.com/settings/tokens

**Error: "Resource not accessible"**
- Token doesn't have `public_repo` scope
- Create new token with correct scope

**Error: "Rate limit exceeded"**
- Wait an hour or use different token
- Authenticated: 5,000 requests/hour
- Unauthenticated: 60 requests/hour

## Full Documentation

For complete setup instructions, authentication methods, and Python API usage:

📖 [.github/AGENT_ACCESS.md](.github/AGENT_ACCESS.md)

## Examples

### Simple improvement
```bash
python .github/create_issue.py \
  --title "Add Python version check" \
  --mode "3-layer" \
  --category "bootstrap" \
  --priority "high" \
  --problem "Bootstrap fails on Python 3.8 without clear error" \
  --solution "Add version check at start of bootstrap.py"
```

### With implementation
```bash
python .github/create_issue.py \
  --title "Fix error handling in scraper" \
  --mode "3-layer" \
  --category "form-template" \
  --priority "medium" \
  --problem "Scraper crashes on network timeout" \
  --solution "Add try-except with exponential backoff" \
  --implementation "See diff in execution/scrape.py lines 45-60" \
  --commit-message "fix(scraper): add retry logic for network errors" \
  --testing "1. Disconnect network 2. Run scraper 3. Verify retry happens"
```

## What Happens Next?

1. ✅ Issue created with `status:proposed` label
2. 👀 Maintainer reviews
3. ✅ Maintainer adds `status:approved` label
4. 🤖 GitHub Actions creates PR automatically
5. 👀 Maintainer reviews PR
6. 🎉 Merged! Everyone benefits from your improvement

---

**Repository:** https://github.com/coreyshort/arche  
**Issues:** https://github.com/coreyshort/arche/issues  
**Help:** https://github.com/coreyshort/arche/discussions
