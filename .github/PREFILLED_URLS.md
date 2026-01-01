# Pre-Filled Issue URLs

**For AI agents:** Use these URLs to pre-populate GitHub issue forms. Just fill in the details and submit.

## Quick Links

### Report a Bug
```
https://github.com/coreyshort/arche/issues/new?labels=bug&template=bug_report.yml
```

### Suggest Improvement (3-Layer Mode)
```
https://github.com/coreyshort/arche/issues/new?title=%5BImprovement%5D%3A+&labels=improvement,status:proposed&body=%23%23+Mode%0A%E2%9C%85+3-layer+(Mature)%0A%0A%23%23+Problem+%2F+Motivation%0A%0A%0A%23%23+Proposed+Solution%0A
```

### Suggest Improvement (General)
```
https://github.com/coreyshort/arche/issues/new?title=%5BImprovement%5D%3A+&labels=improvement,status:proposed&body=%23%23+Problem+%2F+Motivation%0A%0A%0A%23%23+Proposed+Solution%0A
```

### New Mode Proposal
```
https://github.com/coreyshort/arche/issues/new?labels=improvement,status:proposed&title=%5BNew+Mode%5D%3A+&body=%23%23+Mode+Name%0A%0A%23%23+Paradigm%0A%0A%23%23+Real-World+Evidence%0A%0A%23%23+Problem+This+Solves%0A
```

### Documentation Improvement
```
https://github.com/coreyshort/arche/issues/new?labels=documentation&title=%5BDocs%5D%3A+&body=%23%23+Which+Document%0A%0A%23%23+Issue%0A%0A%23%23+Suggested+Fix%0A
```

## How AI Agents Can Use These

### Method 1: Direct Link (Simplest)
Tell the user:
```
I've drafted an improvement. Please open this link and submit:
https://github.com/coreyshort/arche/issues/new?title=[YOUR_ENCODED_TITLE]&body=[YOUR_ENCODED_BODY]
```

### Method 2: Generate Dynamic URL
```python
import urllib.parse

def create_issue_url(title: str, body: str) -> str:
    """Generate pre-filled GitHub issue URL."""
    base = "https://github.com/coreyshort/arche/issues/new"
    params = {
        "title": f"[Improvement]: {title}",
        "body": body,
        "labels": "improvement,status:proposed"
    }
    query = urllib.parse.urlencode(params)
    return f"{base}?{query}"

# Usage
url = create_issue_url(
    title="Add validation to bootstrap.py",
    body="## Problem\n\nMissing Python version check\n\n## Solution\n\nAdd validation step"
)
print(f"Submit here: {url}")
```

### Method 3: QR Code (For Mobile)
```python
import qrcode

url = create_issue_url("Your improvement", "Problem\n\nSolution")
qr = qrcode.make(url)
qr.save("submit_improvement.png")
print("Scan QR code to submit issue")
```

## URL Length Limits

GitHub URLs are limited to ~8,000 characters. For long issue bodies:

1. **Use shortened body** with link to full details:
   ```
   body = "See full details at: [paste.your-service.com/abc123]"
   ```

2. **Use the Python script instead**:
   ```bash
   python .github/submit_improvement.py
   ```

3. **Generate copy-paste template**:
   ```python
   template = f"""
   Title: [Improvement]: {title}
   
   {body}
   
   Paste at: https://github.com/coreyshort/arche/issues/new
   """
   ```

## Examples

### Example 1: Simple Improvement
```python
import urllib.parse

title = "Add Python version check"
body = """## Problem
Bootstrap script doesn't validate Python version.

## Solution
Add version check at script start:
```python
import sys
if sys.version_info < (3, 10):
    print("Python 3.10+ required")
    sys.exit(1)
```

## Testing
Run with Python 3.9 and verify error message."""

url = f"https://github.com/coreyshort/arche/issues/new?{urllib.parse.urlencode({
    'title': f'[Improvement]: {title}',
    'body': body,
    'labels': 'improvement,status:proposed'
})}"

print(f"Submit: {url}")
```

### Example 2: Documentation Fix
```python
url = f"https://github.com/coreyshort/arche/issues/new?{urllib.parse.urlencode({
    'title': '[Docs]: Clarify mode selection criteria',
    'body': '## Document\nMODE_SELECTION.md\n\n## Issue\nUnclear when to use event-driven vs rl-loop\n\n## Fix\nAdd decision tree flowchart',
    'labels': 'documentation'
})}"
```

### Example 3: Bug Report
```python
url = f"https://github.com/coreyshort/arche/issues/new?{urllib.parse.urlencode({
    'title': '[Bug]: Bootstrap fails on Windows',
    'body': '## Environment\nWindows 11, Python 3.11\n\n## Error\nFileNotFoundError: .arche-config\n\n## Expected\nShould create file with forward slashes',
    'labels': 'bug'
})}"
```

## Best Practices

1. **Keep URLs under 2,000 chars** for reliability
2. **URL-encode all parameters** (use `urllib.parse.urlencode`)
3. **Test the URL** before sharing with user
4. **Provide fallback** (copy-paste template if URL too long)
5. **Use descriptive titles** (helps maintainer triage)

## Integration with AI Assistants

### Claude Projects
Add to custom instructions:
```
When I observe a pattern that could improve arche, generate a pre-filled issue URL using:
https://github.com/coreyshort/arche/issues/new?title=[encoded]&body=[encoded]
```

### GitHub Copilot
Add to .github/copilot-instructions.md:
```
When suggesting arche improvements, use pre-filled URLs from:
https://github.com/coreyshort/arche/blob/main/.github/PREFILLED_URLS.md
```

### ChatGPT Custom Instructions
```
For arche improvements, generate issue URLs like:
https://github.com/coreyshort/arche/issues/new?title=%5BImprovement%5D%3A+[TITLE]&body=[BODY]
```

## Testing Your URL

```bash
# URL decode to verify contents
python3 << 'EOF'
import urllib.parse
import sys

url = sys.argv[1] if len(sys.argv) > 1 else input("Paste URL: ")
params = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)

print("\nDecoded Parameters:")
for key, values in params.items():
    print(f"\n{key}:")
    for value in values:
        print(f"  {value}")
EOF
```
