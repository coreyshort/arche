# Quick Agent Issue Submission

**For AI agents having trouble submitting issues** - Use this simplified guide.

## 🚀 Fastest Method: Copy-Paste Template

If you can't access the GitHub API, just copy this markdown template and tell the user to paste it at https://github.com/coreyshort/arche/issues/new

```markdown
---
title: "[Improvement]: YOUR_TITLE_HERE"
labels: improvement, status:proposed
---

## Mode
- [ ] ✅ 3-layer (Mature)
- [ ] 🚀 agentic-swarm (Emerging)
- [ ] 🚀 event-driven (Emerging)
- [ ] 🚀 rl-loop (Emerging)
- [ ] 🌱 New mode proposal
- [ ] 🔧 Cross-mode / Framework-wide

## Category
- [ ] Mode Architecture
- [ ] Form/Template
- [ ] Bootstrap Script
- [ ] Documentation
- [ ] SEO & Discoverability
- [ ] Community

## Priority
- [ ] Low
- [ ] Medium
- [ ] High
- [ ] Critical

## Problem / Motivation
<!-- What pattern or pain point triggered this? -->


## Proposed Solution
<!-- What should change? -->


## Implementation Details
<!-- Code diffs or specific changes -->

```diff
# Show exact changes here
```


## Testing Steps
<!-- How to validate this works -->

```

---

## 💻 If You Have GitHub Token: Simple cURL

**One command** to create an issue:

```bash
curl -X POST \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -H "Content-Type: application/json" \
  https://api.github.com/repos/coreyshort/arche/issues \
  -d '{
    "title": "[Improvement]: YOUR_TITLE",
    "body": "## Problem\nYour problem description\n\n## Solution\nYour solution",
    "labels": ["improvement", "status:proposed"]
  }'
```

**Get a token:** https://github.com/settings/tokens (needs `public_repo` scope)

---

## 🐍 Python One-Liner

```python
import os, requests
token = os.getenv("GITHUB_TOKEN")
response = requests.post(
    "https://api.github.com/repos/coreyshort/arche/issues",
    headers={"Authorization": f"token {token}"},
    json={
        "title": "[Improvement]: YOUR_TITLE",
        "body": "## Problem\nDescription\n\n## Solution\nProposal",
        "labels": ["improvement", "status:proposed"]
    }
)
print(f"Created: {response.json()['html_url']}")
```

---

## 🤖 No GitHub Access? Use This Workaround

**Tell the user:**

> I've drafted an improvement for the arche project. Can you submit it here: https://github.com/coreyshort/arche/issues/new
>
> Here's the content to paste:
>
> [paste the markdown template above with filled-in details]

---

## 📝 Minimal Issue Format

If even the template is too much, here's the absolute minimum:

```
Title: [Improvement]: SHORT_DESCRIPTION

Body:
Problem: WHAT_ISSUE_YOU_FOUND
Solution: WHAT_SHOULD_CHANGE
```

That's enough to get started. Maintainer will ask for more details if needed.

---

## Common Issues

**"No GITHUB_TOKEN"**
- Get token: https://github.com/settings/tokens
- Set it: `export GITHUB_TOKEN=ghp_yourToken`

**"403 Forbidden"**
- Token needs `public_repo` scope
- Regenerate token with correct permissions

**"Can't install requests library"**
- Use cURL instead (no dependencies)
- Or ask user to submit manually

**"Not sure what to put"**
- Just describe the problem you encountered
- Maintainer will help refine it

---

## Full Documentation

For comprehensive guide: [AGENT_ACCESS.md](AGENT_ACCESS.md) (371 lines)

For most agents: **Use the copy-paste template above** ↑
