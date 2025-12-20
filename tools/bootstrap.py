#!/usr/bin/env python3
"""
Bootstrap a new project from the Arche template repository.

This script fetches template files from https://github.com/coreyshort/arche
and initializes a new project with the selected template type.

Usage:
    # Interactive mode (recommended)
    python bootstrap.py --interactive
    
    # Direct initialization
    python bootstrap.py --type automation --name "My Project"
    
    # Specify target directory
    python bootstrap.py --type automation --target /path/to/project
    
    # Use specific version/branch
    python bootstrap.py --type automation --branch v1.0.0

Requirements:
    - Python 3.10+
    - Internet connection (to fetch from GitHub)
    - Git (optional, for sparse checkout method)
"""

import argparse
import json
import sys
import urllib.request
import urllib.error
from pathlib import Path
from typing import Dict, List, Optional
import shutil
import tempfile


REPO_URL = "https://github.com/coreyshort/arche"
RAW_URL = "https://raw.githubusercontent.com/coreyshort/arche"
API_URL = "https://api.github.com/repos/coreyshort/arche/contents"


def fetch_file(url: str, target: Path) -> bool:
    """Fetch a single file from GitHub."""
    try:
        with urllib.request.urlopen(url) as response:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(response.read())
        return True
    except urllib.error.URLError as e:
        print(f"✗ Failed to fetch {url}: {e}")
        return False


def fetch_directory_tree(path: str, branch: str = "main") -> Optional[List[Dict]]:
    """Fetch directory contents from GitHub API."""
    url = f"{API_URL}/{path}?ref={branch}"
    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read())
    except urllib.error.URLError as e:
        print(f"✗ Failed to fetch directory listing: {e}")
        return None


def fetch_template_recursive(
    remote_path: str,
    local_path: Path,
    branch: str = "main",
    exclude: Optional[List[str]] = None
) -> int:
    """Recursively fetch template files from GitHub."""
    exclude = exclude or []
    files_copied = 0
    
    contents = fetch_directory_tree(remote_path, branch)
    if not contents:
        return 0
    
    for item in contents:
        name = item["name"]
        if name in exclude:
            continue
            
        if item["type"] == "file":
            # Fetch file
            file_url = f"{RAW_URL}/{branch}/{item['path']}"
            target = local_path / name
            if fetch_file(file_url, target):
                print(f"  ✓ {item['path']}")
                files_copied += 1
                
        elif item["type"] == "dir":
            # Recursively fetch directory
            subdir = local_path / name
            subdir.mkdir(parents=True, exist_ok=True)
            files_copied += fetch_template_recursive(
                item["path"], subdir, branch, exclude
            )
    
    return files_copied


def list_available_templates(branch: str = "main") -> List[str]:
    """List available template types from GitHub."""
    contents = fetch_directory_tree("forms", branch)
    if not contents:
        return []
    
    templates = [
        item["name"] for item in contents
        if item["type"] == "dir" and not item["name"].startswith((".", "_"))
    ]
    return templates


def fetch_project_json(template_type: str, branch: str = "main") -> Optional[Dict]:
    """Fetch project.json metadata for a template."""
    url = f"{RAW_URL}/{branch}/forms/{template_type}/project.json"
    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read())
    except urllib.error.URLError:
        return None


def initialize_project(
    template_type: str,
    target_dir: Path,
    project_name: Optional[str] = None,
    branch: str = "main"
) -> bool:
    """Initialize a new project from a template."""
    
    print(f"\n🚀 Initializing project from Arche template: {template_type}")
    print(f"   Source: {REPO_URL}")
    print(f"   Branch: {branch}")
    print(f"   Target: {target_dir}\n")
    
    # Fetch project.json to get template metadata
    config = fetch_project_json(template_type, branch)
    if not config:
        print(f"✗ Template '{template_type}' not found or invalid")
        return False
    
    print(f"Template: {config.get('name', template_type)}")
    print(f"Description: {config.get('description', 'No description')}\n")
    
    # Create target directory
    target_dir.mkdir(parents=True, exist_ok=True)
    
    # Fetch shared files
    print("Fetching shared files from _shared/...")
    shared_count = fetch_template_recursive("_shared", target_dir, branch)
    
    # Fetch template-specific files
    print(f"\nFetching {template_type} template files...")
    template_count = fetch_template_recursive(
        f"forms/{template_type}", 
        target_dir, 
        branch,
        exclude=["project.json"]  # Don't copy project.json to target
    )
    
    # Create directories specified in config
    print("\nCreating project directories...")
    for dir_name in config.get("directories", []):
        dir_path = target_dir / dir_name
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"  ✓ {dir_name}/")
    
    # Summary
    total_files = shared_count + template_count
    print(f"\n✅ Successfully initialized project!")
    print(f"   Files copied: {total_files}")
    print(f"   Template type: {template_type}")
    
    # Next steps
    print(f"\n📋 Next steps:")
    if "python" in config.get("languages", []):
        print(f"   cd {target_dir}")
        print(f"   python3 -m venv venv")
        print(f"   source venv/bin/activate")
        print(f"   pip install -r requirements.txt")
    else:
        print(f"   cd {target_dir}")
        print(f"   # Follow setup instructions in README.md")
    
    return True


def interactive_mode(branch: str = "main") -> bool:
    """Interactive template selection and initialization."""
    print("\n🎯 Arche Template Bootstrap - Interactive Mode")
    print(f"   Repository: {REPO_URL}\n")
    
    # List available templates
    print("Fetching available templates...")
    templates = list_available_templates(branch)
    
    if not templates:
        print("✗ No templates found or unable to connect to GitHub")
        return False
    
    print("\nAvailable templates:")
    for i, template in enumerate(templates, 1):
        config = fetch_project_json(template, branch)
        desc = config.get("description", "No description") if config else "No description"
        print(f"  {i}. {template}")
        print(f"     {desc}")
    
    # Get user selection
    while True:
        try:
            choice = input(f"\nSelect template (1-{len(templates)}) or 'q' to quit: ").strip()
            if choice.lower() == 'q':
                return False
            
            idx = int(choice) - 1
            if 0 <= idx < len(templates):
                template_type = templates[idx]
                break
            else:
                print(f"Please enter a number between 1 and {len(templates)}")
        except (ValueError, KeyboardInterrupt):
            print("\nCancelled.")
            return False
    
    # Get project name
    project_name = input("\nProject name (optional, press Enter to skip): ").strip()
    if not project_name:
        project_name = None
    
    # Get target directory
    default_target = Path.cwd()
    target_input = input(f"\nTarget directory (default: {default_target}): ").strip()
    target_dir = Path(target_input) if target_input else default_target
    
    # Confirm
    print(f"\n📝 Summary:")
    print(f"   Template: {template_type}")
    if project_name:
        print(f"   Name: {project_name}")
    print(f"   Target: {target_dir}")
    
    confirm = input("\nProceed? (y/N): ").strip().lower()
    if confirm != 'y':
        print("Cancelled.")
        return False
    
    # Initialize
    return initialize_project(template_type, target_dir, project_name, branch)


def main():
    parser = argparse.ArgumentParser(
        description="Bootstrap a new project from Arche templates",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Examples:
  # Interactive mode (recommended for first-time users)
  python bootstrap.py --interactive
  
  # Direct initialization
  python bootstrap.py --type automation
  
  # Specify project name and target
  python bootstrap.py --type automation --name "My ETL Project" --target ~/projects/my-etl
  
  # Use specific version
  python bootstrap.py --type automation --branch v1.0.0

Template Repository: {REPO_URL}
        """
    )
    
    parser.add_argument(
        "-i", "--interactive",
        action="store_true",
        help="Interactive mode with guided setup"
    )
    
    parser.add_argument(
        "-t", "--type",
        type=str,
        help="Template type (automation, webapp-fullstack, api-service, etc.)"
    )
    
    parser.add_argument(
        "-n", "--name",
        type=str,
        help="Project name (used for customization)"
    )
    
    parser.add_argument(
        "--target",
        type=Path,
        default=Path.cwd(),
        help="Target directory for project (default: current directory)"
    )
    
    parser.add_argument(
        "-b", "--branch",
        type=str,
        default="main",
        help="Git branch or tag to use (default: main)"
    )
    
    parser.add_argument(
        "-l", "--list",
        action="store_true",
        help="List available templates and exit"
    )
    
    args = parser.parse_args()
    
    # List templates mode
    if args.list:
        print(f"Available templates from {REPO_URL}:\n")
        templates = list_available_templates(args.branch)
        if templates:
            for template in templates:
                config = fetch_project_json(template, args.branch)
                desc = config.get("description", "") if config else ""
                print(f"  • {template}")
                if desc:
                    print(f"    {desc}")
        else:
            print("No templates found or unable to connect to GitHub")
        return 0
    
    # Interactive mode
    if args.interactive:
        success = interactive_mode(args.branch)
        return 0 if success else 1
    
    # Direct mode - require template type
    if not args.type:
        parser.error("--type is required unless using --interactive or --list")
    
    success = initialize_project(
        args.type,
        args.target,
        args.name,
        args.branch
    )
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
