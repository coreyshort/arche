#!/usr/bin/env python3
"""
Ultra-simple issue creator for arche improvements.
AI agents can run this with minimal setup.

Usage:
    # Interactive mode (recommended)
    python submit_improvement.py
    
    # Quick mode
    python submit_improvement.py --title "Add validation" --problem "Missing checks" --solution "Add validation step"
    
Environment Variables (optional):
    GITHUB_TOKEN: If set, creates issue via API. If not set, generates copy-paste template.
"""

import os
import sys
import json
import argparse
from typing import Optional


def generate_template(title: str, mode: str, category: str, priority: str, 
                     problem: str, solution: str, implementation: str = "", 
                     testing: str = "") -> str:
    """Generate markdown template for manual submission."""
    return f"""## Copy this to: https://github.com/coreyshort/arche/issues/new

---
**Title:** [Improvement]: {title}

**Mode:** {mode}

**Category:** {category}

**Priority:** {priority}

## Problem / Motivation

{problem}

## Proposed Solution

{solution}

{f'''## Implementation Details

```diff
{implementation}
```
''' if implementation else ''}

{f'''## Testing Steps

{testing}
''' if testing else ''}

---

**Labels:** improvement, status:proposed
"""


def create_via_api(title: str, body: str, token: str) -> Optional[str]:
    """Create issue via GitHub API."""
    try:
        import urllib.request
        
        url = "https://api.github.com/repos/coreyshort/arche/issues"
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json"
        }
        
        data = json.dumps({
            "title": f"[Improvement]: {title}",
            "body": body,
            "labels": ["improvement", "status:proposed"]
        }).encode()
        
        req = urllib.request.Request(url, data=data, headers=headers, method='POST')
        
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read())
            return result.get('html_url')
            
    except Exception as e:
        print(f"⚠️  API submission failed: {e}", file=sys.stderr)
        return None


def interactive_mode() -> dict:
    """Interactive prompts to collect issue details."""
    print("🤖 Arche Improvement Submission\n")
    
    title = input("Issue title (short description): ").strip()
    
    print("\nMode:")
    print("1. ✅ 3-layer (Mature)")
    print("2. 🚀 agentic-swarm (Emerging)")
    print("3. 🚀 event-driven (Emerging)")
    print("4. 🚀 rl-loop (Emerging)")
    print("5. 🔧 Cross-mode / Framework-wide")
    mode_choice = input("Select mode (1-5): ").strip()
    mode_map = {
        "1": "✅ 3-layer (Mature)",
        "2": "🚀 agentic-swarm (Emerging)",
        "3": "🚀 event-driven (Emerging)",
        "4": "🚀 rl-loop (Emerging)",
        "5": "🔧 Cross-mode / Framework-wide"
    }
    mode = mode_map.get(mode_choice, "🔧 Cross-mode / Framework-wide")
    
    print("\nCategory:")
    print("1. Mode Architecture")
    print("2. Form/Template")
    print("3. Bootstrap Script")
    print("4. Documentation")
    print("5. Other")
    category_choice = input("Select category (1-5): ").strip()
    category_map = {
        "1": "Mode Architecture",
        "2": "Form/Template",
        "3": "Bootstrap Script",
        "4": "Documentation",
        "5": "Other"
    }
    category = category_map.get(category_choice, "Other")
    
    print("\nPriority:")
    print("1. Low")
    print("2. Medium")
    print("3. High")
    priority_choice = input("Select priority (1-3): ").strip()
    priority_map = {"1": "Low", "2": "Medium", "3": "High"}
    priority = priority_map.get(priority_choice, "Medium")
    
    print("\nProblem / Motivation:")
    print("(Describe what issue you encountered or pattern you observed)")
    problem = input("> ").strip()
    
    print("\nProposed Solution:")
    print("(What should change?)")
    solution = input("> ").strip()
    
    print("\nImplementation Details (optional, press Enter to skip):")
    print("(Code diffs or specific changes)")
    implementation = input("> ").strip()
    
    print("\nTesting Steps (optional, press Enter to skip):")
    print("(How to validate this works)")
    testing = input("> ").strip()
    
    return {
        "title": title,
        "mode": mode,
        "category": category,
        "priority": priority,
        "problem": problem,
        "solution": solution,
        "implementation": implementation,
        "testing": testing
    }


def main():
    parser = argparse.ArgumentParser(
        description="Submit arche improvement - creates issue or generates template"
    )
    parser.add_argument("--title", help="Issue title")
    parser.add_argument("--mode", default="🔧 Cross-mode / Framework-wide", help="Which mode")
    parser.add_argument("--category", default="Other", help="Category")
    parser.add_argument("--priority", default="Medium", help="Priority level")
    parser.add_argument("--problem", help="Problem description")
    parser.add_argument("--solution", help="Proposed solution")
    parser.add_argument("--implementation", default="", help="Implementation details")
    parser.add_argument("--testing", default="", help="Testing steps")
    
    args = parser.parse_args()
    
    # Interactive mode if no arguments provided
    if not args.title:
        data = interactive_mode()
    else:
        if not args.problem or not args.solution:
            print("❌ Error: --problem and --solution are required in non-interactive mode")
            sys.exit(1)
        data = {
            "title": args.title,
            "mode": args.mode,
            "category": args.category,
            "priority": args.priority,
            "problem": args.problem,
            "solution": args.solution,
            "implementation": args.implementation,
            "testing": args.testing
        }
    
    # Build issue body
    body = f"""## Mode
{data['mode']}

## Category
{data['category']}

## Priority
{data['priority']}

## Problem / Motivation

{data['problem']}

## Proposed Solution

{data['solution']}
"""
    
    if data['implementation']:
        body += f"\n## Implementation Details\n\n```diff\n{data['implementation']}\n```\n"
    
    if data['testing']:
        body += f"\n## Testing Steps\n\n{data['testing']}\n"
    
    # Try API submission if token available
    token = os.getenv("GITHUB_TOKEN")
    
    if token:
        print("\n🔄 Creating issue via GitHub API...")
        url = create_via_api(data['title'], body, token)
        
        if url:
            print(f"\n✅ Success! Issue created: {url}")
            return
    
    # Fallback: generate template
    print("\n" + "="*60)
    print("📋 GITHUB_TOKEN not found or API failed.")
    print("Copy the text below and paste at:")
    print("https://github.com/coreyshort/arche/issues/new")
    print("="*60 + "\n")
    
    template = generate_template(
        data['title'], data['mode'], data['category'], data['priority'],
        data['problem'], data['solution'], data['implementation'], data['testing']
    )
    print(template)
    
    print("\n" + "="*60)
    print("💡 Tip: Set GITHUB_TOKEN environment variable for automatic submission")
    print("   Get token: https://github.com/settings/tokens")
    print("="*60)


if __name__ == "__main__":
    main()
