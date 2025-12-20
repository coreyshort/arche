# Agent Access to GitHub Repository

This document explains how AI agents can submit issues to the arche repository at https://github.com/coreyshort/arche/issues

## Problem

AI agents need to create GitHub Issues to submit improvements, but GitHub's API requires authentication. There are several approaches to enable this.

---

## Solution 1: GitHub Personal Access Token (Recommended)

**Best for:** Most AI agents and automation systems

### Setup Steps

1. **Create a GitHub Personal Access Token (Classic):**
   - Go to: https://github.com/settings/tokens
   - Click "Generate new token" → "Generate new token (classic)"
   - Token name: `arche-agent-improvements`
   - Select scopes:
     - ✅ `public_repo` (for creating issues in public repos)
   - Click "Generate token"
   - **Copy the token immediately** (you won't see it again)

2. **Store token securely:**
   ```bash
   # In your project's .env file
   echo "GITHUB_TOKEN=ghp_yourTokenHere" >> .env
   
   # OR set as environment variable
   export GITHUB_TOKEN=ghp_yourTokenHere
   ```

3. **Use in API calls:**
   ```bash
   curl -X POST \
     -H "Authorization: token $GITHUB_TOKEN" \
     -H "Accept: application/vnd.github.v3+json" \
     https://api.github.com/repos/coreyshort/arche/issues \
     -d '{
       "title": "[Improvement]: Better error handling",
       "body": "## Problem\n\nEncountered edge case...",
       "labels": ["improvement", "status:proposed"]
     }'
   ```

4. **Python example:**
   ```python
   import os
   import requests
   
   GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
   REPO_OWNER = "coreyshort"
   REPO_NAME = "arche"
   
   def create_improvement_issue(title: str, body: str, labels: list = None):
       """Create an improvement issue in the arche repository."""
       if not GITHUB_TOKEN:
           raise ValueError("GITHUB_TOKEN environment variable not set")
       
       url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"
       headers = {
           "Authorization": f"token {GITHUB_TOKEN}",
           "Accept": "application/vnd.github.v3+json"
       }
       
       data = {
           "title": title,
           "body": body,
           "labels": labels or ["improvement", "status:proposed"]
       }
       
       response = requests.post(url, headers=headers, json=data)
       response.raise_for_status()
       
       return response.json()
   
   # Usage
   issue = create_improvement_issue(
       title="[Improvement]: Add validation step",
       body="## Problem\n\nDetails...\n\n## Proposed Solution\n\nImplementation..."
   )
   print(f"Created issue: {issue['html_url']}")
   ```

### Security Notes

- **Never commit tokens to git** (add to `.gitignore`)
- Use minimal scopes (only `public_repo` for public repos)
- Rotate tokens regularly
- Consider using separate tokens for different projects
- Tokens expire based on your settings

---

## Solution 2: GitHub CLI (gh)

**Best for:** Local development and interactive agents

### Setup Steps

1. **Install GitHub CLI:**
   ```bash
   # macOS
   brew install gh
   
   # Linux (Debian/Ubuntu)
   sudo apt install gh
   
   # Windows
   winget install GitHub.cli
   ```

2. **Authenticate:**
   ```bash
   gh auth login
   # Follow prompts to authenticate via browser
   ```

3. **Create issues:**
   ```bash
   gh issue create \
     --repo coreyshort/arche \
     --title "[Improvement]: Better validation" \
     --body "## Problem\n\nDetails...\n\n## Solution\n\nImplementation..." \
     --label "improvement,status:proposed"
   ```

4. **From Python:**
   ```python
   import subprocess
   import json
   
   def create_issue_via_cli(title: str, body: str):
       """Create issue using gh CLI."""
       cmd = [
           "gh", "issue", "create",
           "--repo", "coreyshort/arche",
           "--title", title,
           "--body", body,
           "--label", "improvement,status:proposed",
           "--json", "url"
       ]
       
       result = subprocess.run(cmd, capture_output=True, text=True)
       
       if result.returncode != 0:
           raise Exception(f"Failed to create issue: {result.stderr}")
       
       data = json.loads(result.stdout)
       return data["url"]
   ```

### Benefits

- No need to manage tokens manually
- Handles authentication securely
- Works across all GitHub operations
- Better error messages

---

## Solution 3: GitHub App (For Organizations)

**Best for:** Enterprise deployments with multiple agents

### Overview

GitHub Apps provide fine-grained permissions and are ideal for organizational use. This is more complex to set up but provides better security and auditing.

### Setup Steps

1. **Create GitHub App:**
   - Go to: https://github.com/settings/apps/new
   - Set permissions:
     - Issues: Read & Write
   - Generate private key
   - Install app on repository

2. **Authenticate with JWT:**
   ```python
   import jwt
   import time
   import requests
   
   def get_installation_token(app_id: str, private_key: str, installation_id: str):
       """Get installation access token for GitHub App."""
       # Generate JWT
       payload = {
           "iat": int(time.time()),
           "exp": int(time.time()) + 600,
           "iss": app_id
       }
       
       token = jwt.encode(payload, private_key, algorithm="RS256")
       
       # Exchange for installation token
       headers = {
           "Authorization": f"Bearer {token}",
           "Accept": "application/vnd.github.v3+json"
       }
       
       url = f"https://api.github.com/app/installations/{installation_id}/access_tokens"
       response = requests.post(url, headers=headers)
       response.raise_for_status()
       
       return response.json()["token"]
   ```

**Note:** This approach requires more setup but is recommended for production systems processing high volumes of issues.

---

## Solution 4: OAuth App (For User-Facing Tools)

**Best for:** Web applications where users authorize the agent

If you're building a tool that helps users create issues, use OAuth:

1. Register OAuth App at: https://github.com/settings/developers
2. Implement OAuth flow to get user tokens
3. Use user tokens to create issues on their behalf

---

## Recommended Approach by Use Case

| Use Case | Recommended Solution | Why |
|----------|---------------------|-----|
| Individual agent/developer | GitHub CLI | Easiest setup, secure |
| Automated CI/CD | Personal Access Token | Simple integration |
| Multiple agents | Personal Access Token | Centralized management |
| Enterprise/Organization | GitHub App | Fine-grained permissions |
| User-facing tool | OAuth App | Users authorize agent |

---

## Integration with Arche Instructions

Update your agent's configuration to include the GitHub token:

### For Claude Projects:
```
GITHUB_TOKEN=ghp_yourTokenHere

Follow: https://raw.githubusercontent.com/coreyshort/arche/main/modes/3-layer/INSTRUCTIONS.md
```

### For Cursor (.cursorrules):
```
export GITHUB_TOKEN=ghp_yourTokenHere
Follow: https://raw.githubusercontent.com/coreyshort/arche/main/modes/3-layer/INSTRUCTIONS.md
```

### In .env file:
```bash
# GitHub API access for creating improvement issues
GITHUB_TOKEN=ghp_yourTokenHere
```

---

## Testing Your Setup

Test that your agent can create issues:

```bash
# Using curl
curl -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/coreyshort/arche/issues \
  -d '{"title":"Test Issue","body":"Testing agent access","labels":["test"]}'

# Using gh CLI
gh issue create --repo coreyshort/arche --title "Test Issue" --body "Testing access"
```

**Remember to close test issues after verifying access works!**

---

## Rate Limits

GitHub API has rate limits:

**Authenticated requests:**
- 5,000 requests per hour per token
- Sufficient for most agent workloads

**Unauthenticated requests:**
- 60 requests per hour per IP
- Not suitable for agents (too low)

---

## Troubleshooting

### "Bad credentials" error
- Token is incorrect or expired
- Token doesn't have required scopes
- Solution: Regenerate token with `public_repo` scope

### "Resource not accessible" error
- Repository is private (it's not - arche is public)
- Token doesn't have correct permissions
- Solution: Check token scopes

### "Validation failed" error
- Issue body is malformed
- Required fields missing
- Solution: Check JSON structure matches GitHub API requirements

### Rate limit exceeded
- Too many requests in short time
- Solution: Implement exponential backoff, reduce request frequency

---

## Security Best Practices

1. **Never expose tokens in:**
   - Git commits
   - Public documentation
   - Error messages
   - Logs

2. **Use environment variables:**
   ```bash
   # .env (in .gitignore)
   GITHUB_TOKEN=ghp_actualToken
   ```

3. **Rotate tokens regularly:**
   - Set expiration when creating
   - Create new token before old expires
   - Update all systems using token

4. **Use minimal permissions:**
   - Only `public_repo` for public repositories
   - Don't grant admin or delete permissions

5. **Monitor usage:**
   - Check GitHub settings → Personal access tokens
   - Review which applications/systems are using tokens
   - Revoke unused tokens

---

## Additional Resources

- **GitHub REST API Documentation:** https://docs.github.com/en/rest/issues/issues
- **GitHub CLI Documentation:** https://cli.github.com/manual/
- **GitHub Apps Documentation:** https://docs.github.com/en/apps
- **Rate Limiting:** https://docs.github.com/en/rest/overview/rate-limits-for-the-rest-api

---

## Support

If you encounter issues setting up agent access:

1. Check this document first
2. Search existing issues: https://github.com/coreyshort/arche/issues
3. Ask in Discussions: https://github.com/coreyshort/arche/discussions
4. Create an issue (manually): https://github.com/coreyshort/arche/issues/new

---

**Last Updated:** December 20, 2024  
**Maintainer:** Corey Short ([@coreyshort](https://github.com/coreyshort))
