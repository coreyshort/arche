# .github Directory

This directory contains GitHub-specific configuration and tools for the arche repository.

## Files

### For Contributors

- **[AGENT_ACCESS.md](AGENT_ACCESS.md)** - Complete guide for AI agents to programmatically create GitHub Issues
  - GitHub Personal Access Token setup
  - GitHub CLI usage
  - GitHub App configuration
  - Code examples in Python and bash
  
- **[create_issue.py](create_issue.py)** - Python script for creating improvement issues
  ```bash
  # Usage example
  export GITHUB_TOKEN=ghp_yourToken
  python .github/create_issue.py \
    --title "Better validation" \
    --mode "3-layer" \
    --category "bootstrap" \
    --priority "medium" \
    --problem "Script doesn't validate Python version" \
    --solution "Add version check before proceeding"
  ```

### Issue Templates

- **[ISSUE_TEMPLATE/improvement.yml](ISSUE_TEMPLATE/improvement.yml)** - Structured template for improvement submissions
- **[ISSUE_TEMPLATE/config.yml](ISSUE_TEMPLATE/config.yml)** - Issue template configuration
- **[NEW_MODE_PROPOSAL.md](NEW_MODE_PROPOSAL.md)** - Template for proposing new architectural modes

### GitHub Actions Workflows

- **[workflows/auto-pr.yml](workflows/auto-pr.yml)** - Automatically creates PRs from approved issues
- **[workflows/label-management.yml](workflows/label-management.yml)** - Manages issue labels

### Copilot Configuration

- **[COPILOT_INSTRUCTIONS.md](COPILOT_INSTRUCTIONS.md)** - Instructions for GitHub Copilot to understand arche patterns

## Quick Start for AI Agents

1. **Get GitHub Token:**
   ```bash
   # Visit: https://github.com/settings/tokens
   # Create token with 'public_repo' scope
   export GITHUB_TOKEN=ghp_yourToken
   ```

2. **Create an improvement issue:**
   ```bash
   python .github/create_issue.py \
     --title "[Improvement]: Your title" \
     --mode "3-layer" \
     --category "documentation" \
     --priority "medium" \
     --problem "Description of issue" \
     --solution "Proposed fix"
   ```

3. **Issue workflow:**
   - Issue created with `status:proposed` label
   - Maintainer reviews and adds `status:approved`
   - GitHub Actions automatically creates PR
   - Maintainer reviews and merges

See [AGENT_ACCESS.md](AGENT_ACCESS.md) for complete documentation.

## Permissions

- **Anyone can create issues** (with or without GitHub account via manual form)
- **AI agents need GitHub token** for programmatic issue creation
- **Only maintainers** can approve issues and merge PRs

## Support

- Issues: https://github.com/coreyshort/arche/issues
- Discussions: https://github.com/coreyshort/arche/discussions
