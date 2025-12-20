#!/usr/bin/env python3
"""
Helper script for AI agents to create GitHub Issues in the arche repository.

Usage:
    python create_issue.py --title "Your title" --mode "3-layer" --category "Bootstrap" --priority "medium"

Environment Variables:
    GITHUB_TOKEN: Personal access token with 'public_repo' scope
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.error
from typing import Optional, Dict, List


REPO_OWNER = "coreyshort"
REPO_NAME = "arche"
API_BASE = "https://api.github.com"


def get_github_token() -> Optional[str]:
    """Get GitHub token from environment."""
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("❌ Error: GITHUB_TOKEN environment variable not set", file=sys.stderr)
        print("\nTo create a token:", file=sys.stderr)
        print("1. Go to: https://github.com/settings/tokens", file=sys.stderr)
        print("2. Generate new token (classic) with 'public_repo' scope", file=sys.stderr)
        print("3. Set: export GITHUB_TOKEN=ghp_yourTokenHere", file=sys.stderr)
        print("\nSee .github/AGENT_ACCESS.md for detailed instructions", file=sys.stderr)
    return token


def create_issue(
    title: str,
    body: str,
    labels: Optional[List[str]] = None,
    token: Optional[str] = None
) -> Dict:
    """
    Create an issue in the arche repository.
    
    Args:
        title: Issue title
        body: Issue body (markdown)
        labels: List of label names
        token: GitHub token (uses GITHUB_TOKEN env var if not provided)
    
    Returns:
        dict: Issue data from GitHub API
    
    Raises:
        ValueError: If token is missing
        urllib.error.HTTPError: If API request fails
    """
    if not token:
        token = get_github_token()
        if not token:
            raise ValueError("No GitHub token available")
    
    url = f"{API_BASE}/repos/{REPO_OWNER}/{REPO_NAME}/issues"
    
    data = {
        "title": title,
        "body": body,
        "labels": labels or ["improvement", "status:proposed"]
    }
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }
    
    request = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(request) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"❌ GitHub API Error ({e.code}):", file=sys.stderr)
        print(error_body, file=sys.stderr)
        raise


def format_improvement_issue(
    title: str,
    mode: str,
    category: str,
    priority: str,
    problem: str,
    solution: str,
    implementation: Optional[str] = None,
    commit_message: Optional[str] = None,
    testing: Optional[str] = None
) -> str:
    """
    Format an improvement issue body according to the template.
    
    Args:
        title: Short title of improvement
        mode: Which mode (3-layer, agentic-swarm, event-driven, rl-loop, cross-mode)
        category: Category (mode architecture, form/template, bootstrap, documentation, etc.)
        priority: Priority level (critical, high, medium, low)
        problem: Problem description
        solution: Proposed solution
        implementation: Implementation details with code diffs
        commit_message: Suggested commit message
        testing: Testing steps
    
    Returns:
        str: Formatted markdown issue body
    """
    body = f"""## Improvement Details

**Mode:** {mode}  
**Category:** {category}  
**Priority:** {priority}

## Problem / Motivation

{problem}

## Proposed Solution

{solution}
"""
    
    if implementation:
        body += f"""
## Implementation Details

{implementation}
"""
    
    if commit_message:
        body += f"""
## Suggested Commit Message

```
{commit_message}
```
"""
    
    if testing:
        body += f"""
## Testing Steps

{testing}
"""
    
    body += """
---

*This issue was created programmatically by an AI agent.*
"""
    
    return body


def main():
    parser = argparse.ArgumentParser(
        description="Create a GitHub Issue for arche improvements",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Simple issue
    python create_issue.py \\
        --title "[Improvement]: Better validation" \\
        --mode "3-layer" \\
        --category "Bootstrap" \\
        --priority "medium" \\
        --problem "Bootstrap doesn't validate Python version" \\
        --solution "Add version check before proceeding"
    
    # Issue with implementation
    python create_issue.py \\
        --title "[Improvement]: Add error handling" \\
        --mode "3-layer" \\
        --category "Form/Template" \\
        --priority "high" \\
        --problem "Script crashes on network errors" \\
        --solution "Add try-except and retry logic" \\
        --implementation "See diff below..." \\
        --testing "1. Disconnect network 2. Run script 3. Verify graceful error"
    
Environment:
    Set GITHUB_TOKEN environment variable with a token that has 'public_repo' scope.
    See .github/AGENT_ACCESS.md for setup instructions.
        """
    )
    
    parser.add_argument(
        "--title",
        required=True,
        help="Issue title (should start with '[Improvement]: ')"
    )
    
    parser.add_argument(
        "--mode",
        required=True,
        choices=["3-layer", "agentic-swarm", "event-driven", "rl-loop", "cross-mode", "new-mode"],
        help="Which mode this improvement targets"
    )
    
    parser.add_argument(
        "--category",
        required=True,
        choices=[
            "mode-architecture",
            "form-template",
            "bootstrap",
            "documentation",
            "seo-discoverability",
            "marketing-outreach",
            "social-media",
            "community-growth",
            "other"
        ],
        help="Category of improvement"
    )
    
    parser.add_argument(
        "--priority",
        required=True,
        choices=["critical", "high", "medium", "low"],
        help="Priority level"
    )
    
    parser.add_argument(
        "--problem",
        required=True,
        help="Problem description / motivation"
    )
    
    parser.add_argument(
        "--solution",
        required=True,
        help="Proposed solution"
    )
    
    parser.add_argument(
        "--implementation",
        help="Implementation details with code diffs"
    )
    
    parser.add_argument(
        "--commit-message",
        help="Suggested commit message in conventional commit format"
    )
    
    parser.add_argument(
        "--testing",
        help="Testing steps to validate the improvement"
    )
    
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print issue body without creating (for testing)"
    )
    
    args = parser.parse_args()
    
    # Ensure title starts with [Improvement]:
    if not args.title.startswith("[Improvement]:"):
        args.title = f"[Improvement]: {args.title}"
    
    # Format issue body
    body = format_improvement_issue(
        title=args.title,
        mode=args.mode,
        category=args.category,
        priority=args.priority,
        problem=args.problem,
        solution=args.solution,
        implementation=args.implementation,
        commit_message=args.commit_message,
        testing=args.testing
    )
    
    # Determine labels
    labels = [
        "improvement",
        "status:proposed",
        f"mode:{args.mode}",
        f"category:{args.category}",
        f"priority:{args.priority}"
    ]
    
    if args.dry_run:
        print("=" * 80)
        print("DRY RUN - Would create issue with:")
        print("=" * 80)
        print(f"Title: {args.title}")
        print(f"Labels: {', '.join(labels)}")
        print()
        print(body)
        print("=" * 80)
        return 0
    
    # Create issue
    try:
        print(f"Creating issue: {args.title}")
        issue = create_issue(args.title, body, labels)
        
        print("✅ Issue created successfully!")
        print(f"   URL: {issue['html_url']}")
        print(f"   Number: #{issue['number']}")
        return 0
        
    except ValueError as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        return 1
    except urllib.error.HTTPError as e:
        print(f"❌ Failed to create issue", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"❌ Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
