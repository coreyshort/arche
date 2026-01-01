# Submit Improvement

Report an improvement to enhance arche for all users.

## Goal

Capture learnings from your project and feed them back to improve arche's templates, documentation, and patterns.

## When to Use This Directive

Use this when you:
- Discover a better pattern or approach
- Encounter edge cases not documented
- Find missing validations or error handling
- Identify documentation gaps
- Observe patterns across multiple interactions (not single tasks)

## Inputs

**Pattern Observation:**
- What issue/pattern did you observe?
- Did it recur across multiple interactions?
- What context makes this significant?

**Proposed Improvement:**
- What should change?
- How does this make arche better?
- Who benefits from this change?

## Tools/Scripts to Use

### Option 1: Interactive Script (Recommended)
```bash
# Run from your arche project
curl -O https://raw.githubusercontent.com/coreyshort/arche/main/.github/submit_improvement.py
python submit_improvement.py
```

This script:
- Prompts for all required information
- Validates inputs
- Creates issue via API (if GITHUB_TOKEN set) OR generates copy-paste template
- No external dependencies needed

### Option 2: Quick Template
If script fails, copy this template and fill it in:

```markdown
**Title:** [Improvement]: SHORT_DESCRIPTION

**Problem:** Describe the pattern you observed

**Solution:** What should change

**Mode:** Which mode (3-layer, agentic-swarm, etc.)

**Priority:** Low/Medium/High
```

Paste at: https://github.com/coreyshort/arche/issues/new

### Option 3: One-Line cURL (if you have GITHUB_TOKEN)
```bash
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Content-Type: application/json" \
  https://api.github.com/repos/coreyshort/arche/issues \
  -d '{
    "title": "[Improvement]: YOUR_TITLE",
    "body": "## Problem\n\nYOUR_PROBLEM\n\n## Solution\n\nYOUR_SOLUTION",
    "labels": ["improvement", "status:proposed"]
  }'
```

## Process

1. **Observe pattern:** Notice recurring issues or opportunities
2. **Reflect:** Is this significant? Does it affect multiple users?
3. **Draft improvement:** Use script or template above
4. **Submit:** Create GitHub Issue
5. **Maintainer reviews:** Adds `status:approved` if valid
6. **Automated PR:** GitHub Actions creates PR from approved issue
7. **Merge & benefit everyone:** Your learning strengthens arche

## Outputs

- GitHub Issue created at https://github.com/coreyshort/arche/issues
- Improvement tracked and reviewed
- If approved: Automated PR created and merged
- Future arche projects benefit from your learning

## Edge Cases

**"Script fails / no Python"**
- Use Option 2 (copy-paste template)
- Or tell user to submit manually

**"Not sure if improvement is significant"**
- Ask yourself: Would this help multiple users?
- If unsure, submit anyway. Maintainer will evaluate.

**"Already found similar issue"**
- Comment on existing issue with additional context
- Or reference it in new issue

**"No GitHub account"**
- AI agent should ask user to create GitHub account
- Or request user submit on agent's behalf

## Self-Annealing

This directive itself can be improved:
- Too complex? Simplify steps
- Missing common case? Add to edge cases
- Better tool/script? Update tools section

Report improvements to this directive using... this directive. 🔄

## Notes

- **Pattern-based, not task-by-task:** Only submit after observing recurring patterns
- **Be specific:** Include concrete examples and implementation details
- **Think ecosystem:** How does this help all arche users?
- **Respect maintainer time:** Well-formed issues get faster review
