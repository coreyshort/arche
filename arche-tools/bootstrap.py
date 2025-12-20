#!/usr/bin/env python3
"""
Bootstrap a new project from the Arche template repository.

This script fetches template files from https://github.com/coreyshort/arche
and initializes a new project with the selected mode and form.

Usage:
    # Interactive mode (recommended)
    python bootstrap.py --interactive
    
    # Direct initialization
    python bootstrap.py --mode 3-layer --form automation --name "My Project"
    
    # Specify target directory
    python bootstrap.py --mode 3-layer --form automation --target /path/to/project
    
    # Use specific version/branch
    python bootstrap.py --mode 3-layer --form automation --branch v1.0.0

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
from datetime import datetime


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


def list_available_modes(branch: str = "main") -> List[str]:
    """List available modes from GitHub."""
    contents = fetch_directory_tree("modes", branch)
    if not contents:
        return []
    
    modes = [
        item["name"] for item in contents
        if item["type"] == "dir" and not item["name"].startswith((".", "_"))
    ]
    return modes


def list_available_forms(mode: str, branch: str = "main") -> List[str]:
    """List available forms for a specific mode."""
    contents = fetch_directory_tree(f"modes/{mode}/forms", branch)
    if not contents:
        return []
    
    forms = [
        item["name"] for item in contents
        if item["type"] == "dir" and not item["name"].startswith((".", "_"))
    ]
    return forms


def fetch_project_json(mode: str, form: str, branch: str = "main") -> Optional[Dict]:
    """Fetch project.json metadata for a form within a mode."""
    url = f"{RAW_URL}/{branch}/modes/{mode}/forms/{form}/project.json"
    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read())
    except urllib.error.URLError:
        return None


def initialize_project(
    mode: str,
    form: str,
    target_dir: Path,
    project_name: Optional[str] = None,
    branch: str = "main",
    enable_telemetry: Optional[bool] = None,
    update_strategy: str = "auto",
    update_interval: Optional[int] = None
) -> bool:
    """
    Initialize a new project from a mode/form.
    
    This function uses selective sync - only files from the selected mode are copied.
    Other modes, forms, and cross-mode documentation remain in the repository.
    This keeps projects lightweight and focused on their specific architectural pattern.
    """
    
    print(f"\n🚀 Initializing project from Arche")
    print(f"   Mode: {mode} (selective sync - only this mode's files)")
    print(f"   Form: {form}")
    print(f"   Source: {REPO_URL}")
    print(f"   Branch: {branch}")
    print(f"   Target: {target_dir}\n")
    
    # Fetch project.json to get metadata
    config = fetch_project_json(mode, form, branch)
    if not config:
        print(f"✗ Form '{form}' in mode '{mode}' not found or invalid")
        return False
    
    print(f"Template: {config.get('name', form)}")
    print(f"Description: {config.get('description', 'No description')}\n")
    
    # Create target directory
    target_dir.mkdir(parents=True, exist_ok=True)
    
    # Fetch shared files for this mode
    print(f"Fetching shared files from modes/{mode}/_shared/...")
    shared_count = fetch_template_recursive(f"modes/{mode}/_shared", target_dir, branch)
    
    # Fetch form-specific files
    print(f"\nFetching {form} form files...")
    form_count = fetch_template_recursive(
        f"modes/{mode}/forms/{form}", 
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
    
    # Create telemetry config if enabled
    if enable_telemetry is None:
        # Check global config
        global_config = Path.home() / ".arche-config"
        if global_config.exists():
            try:
                global_data = json.loads(global_config.read_text())
                enable_telemetry = global_data.get("telemetry_enabled", True)
            except:
                enable_telemetry = True
        else:
            enable_telemetry = True
    
    if enable_telemetry:
        telemetry_data = {
            "telemetry_enabled": True,
            "mode": mode,
            "form": form,
            "project_type": None,
            "team_size": None,
            "created_at": datetime.now().strftime("%Y-%m-%d"),
            "arche_version": branch,
            "notes": "This file is never committed. It helps the arche community understand usage patterns. To disable: set telemetry_enabled to false or delete this file. See TELEMETRY.md"
        }
        telemetry_file = target_dir / ".arche-telemetry"
        telemetry_file.write_text(json.dumps(telemetry_data, indent=2))
        print(f"\n  ✓ Created .arche-telemetry (helps improve arche, see TELEMETRY.md)")
        
        # Ensure it's in .gitignore
        gitignore_file = target_dir / ".gitignore"
        if gitignore_file.exists():
            gitignore_content = gitignore_file.read_text()
            if ".arche-telemetry" not in gitignore_content:
                gitignore_file.write_text(gitignore_content.rstrip() + "\n.arche-telemetry\n")
        else:
            gitignore_file.write_text(".arche-telemetry\n")
    
    # Create update config
    config_data = {
        "update_strategy": update_strategy,
        "mode": mode,
        "form": form,
        "arche_version": branch,
        "branch": branch,
        "created_at": datetime.now().strftime("%Y-%m-%d"),
        "telemetry_enabled": enable_telemetry if enable_telemetry is not None else False
    }
    
    if update_strategy == "prompt" and update_interval:
        config_data["update_check_interval_days"] = update_interval
        config_data["last_update_check"] = datetime.now().strftime("%Y-%m-%d")
    
    config_file = target_dir / ".arche-config"
    config_file.write_text(json.dumps(config_data, indent=2))
    print(f"  ✓ Created .arche-config (update strategy: {update_strategy})")
    
    # Ensure .arche-config is in .gitignore
    gitignore_file = target_dir / ".gitignore"
    if gitignore_file.exists():
        gitignore_content = gitignore_file.read_text()
        if ".arche-config" not in gitignore_content:
            gitignore_file.write_text(gitignore_content.rstrip() + "\n.arche-config\n.arche-backups/\n.arche-update.log\n")
    else:
        gitignore_file.write_text(".arche-config\n.arche-backups/\n.arche-update.log\n")
    
    # Summary
    total_files = shared_count + form_count
    print(f"\n✅ Successfully initialized project!")
    print(f"   Files copied: {total_files}")
    print(f"   Mode: {mode}")
    print(f"   Form: {form}")
    print(f"\n💡 Selective Sync")
    print(f"   Only {mode} mode files were copied to your project.")
    print(f"   Other modes remain in the arche repository.")
    print(f"   Reference documentation at: {REPO_URL}")
    
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
    
    # Feedback reminder
    print(f"\n💡 As you work, contribute improvements back to arche")
    print(f"   Discovered a better pattern? Found an edge case?")
    print(f"   Create an issue: https://github.com/coreyshort/arche/issues")
    print(f"   Your learnings make arche stronger for everyone.")
    print(f"\n   If arche helps you build something valuable, consider helping")
    print(f"   others discover it—clearer docs, better examples, or just")
    print(f"   telling colleagues who might benefit. The virtuous circle grows naturally.")
    
    return True


def interactive_mode(branch: str = "main") -> bool:
    """Interactive mode and form selection and initialization."""
    print("\n🎯 Arche Bootstrap - Interactive Mode")
    print(f"   Repository: {REPO_URL}\n")
    
    # List available modes
    print("Fetching available modes...")
    modes = list_available_modes(branch)
    
    if not modes:
        print("✗ No modes found or unable to connect to GitHub")
        return False
    
    print("\nAvailable modes:")
    for i, mode in enumerate(modes, 1):
        print(f"  {i}. {mode}")
    
    # Get mode selection
    while True:
        try:
            choice = input(f"\nSelect mode (1-{len(modes)}) or 'q' to quit: ").strip()
            if choice.lower() == 'q':
                return False
            
            idx = int(choice) - 1
            if 0 <= idx < len(modes):
                selected_mode = modes[idx]
                break
            else:
                print(f"Please enter a number between 1 and {len(modes)}")
        except (ValueError, KeyboardInterrupt):
            print("\nCancelled.")
            return False
    
    # List available forms for selected mode
    print(f"\nFetching forms for {selected_mode} mode...")
    forms = list_available_forms(selected_mode, branch)
    
    if not forms:
      Telemetry prompt
    print(f"\n📊 Anonymous Telemetry")
    print(f"   Help improve arche by sharing anonymous usage data (mode, form, project type).")
    print(f"   No identifying information is collected. See TELEMETRY.md for details.")
    telemetry_input = input(f"   Enable telemetry? (Y/n): ").strip().lower()
    enable_telemetry = telemetry_input != 'n'
    
    #   print(f"✗ No forms found for {selected_mode} mode")
        return False
    
    print(f"\nAvailable forms in {selected_mode}:")
    for i, form in enumerate(forms, 1):
        config = fetch_project_json(selected_mode, form, branch)
        desc = config.get("description", "No description") if config else "No description"
        print(f"  {i}. {form}"
        selected_mode, 
        selected_form, 
        target_dir, 
        project_name, 
        branch,
        enable_telemetry
    
        print(f"     {desc}")
    
    # Get form selection
    while True:
        try:
            choice = input(f"\nSelect form (1-{len(forms)}) or 'q' to quit: ").strip()
            if choice.lower() == 'q':
                return False
            
            idx = int(choice) - 1
            if 0 <= idx < len(forms):
                selected_form = forms[idx]
                break
            else:
                print(f"Please enter a number between 1 and {len(forms)}")
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
    print(f"   Mode: {selected_mode}")
    print(f"   Form: {selected_form}")
    if project_name:
        print(f"   Name: {project_name}")
    print(f"   Target: {target_dir}")
    
    confirm = input("\nProceed? (y/N): ").strip().lower()
    if confirm != 'y':
        print("Cancelled.")
        return False
    
    # Initialize
    return initialize_project(selected_mode, selected_form, target_dir, project_name, branch)


def main():
    parser = argparse.ArgumentParser(
        description="Bootstrap a new project from Arche modes and forms",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Examples:
  # Interactive mode (recommended for first-time users)
  python bootstrap.py --interactive
  
  # Direct initialization
  python bootstrap.py --mode 3-layer --form automation
  
  # Specify project name and target
  python bootstrap.py --mode 3-layer --form automation --name "My ETL Project" --target ~/projects/my-etl
  
  # Use specific version
  python bootstrap.py --mode 3-layer --form automation --branch v1.0.0
  
  # List available modes
  python bootstrap.py --list-modes
  
  # List forms in a specific mode
  python bootstrap.py --list-forms 3-layer

Repository: {REPO_URL}
        """
    )
    
    parser.add_argument(
        "-i", "--interactive",
        action="store_true",
        help="Interactive mode with guided setup"
    )
    
    parser.add_argument(
        "-m", "--mode",
        type=str,
        help="Mode (3-layer, agentic-swarm, event-driven, rl-loop, etc.)"
    )
    
    parser.add_argument(
        "-f", "--form",
        type=str,
        help="Form within the mode (automation, webapp-fullstack, api-service, etc.)"
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
        "--list-modes",
        action="store_true",
        help="List available modes and exit"
    )
    parser.add_argument(
        "--no-telemetry",
        action="store_true",
        help="Disable anonymous telemetry (default: enabled)"
    )
    
    
    parser.add_argument(
        "--list-forms",
        type=str,
        metavar="MODE",
        help="List available forms for a specific mode and exit"
    )
    
    parser.add_argument(
        "-l", "--list",
        action="store_true",
        help="List available templates and exit"
    )
    
    args = parser.parse_args()
    
    # List modes
    if args.list_modes:
        print(f"Available modes from {REPO_URL}:\n")
        modes = list_available_modes(args.branch)
        if modes:
            for mode in modes:
                print(f"  • {mode}")
        else:
            print("No modes found or unable to connect to GitHub")
        return 0
    
    # List forms for a specific mode
    if args.list_forms:
        print(f"Available forms in '{args.list_forms}' mode from {REPO_URL}:\n")
        forms = list_available_forms(args.list_forms, args.branch)
    enable_telemetry = not args.no_telemetry
    
    success = initialize_project(
        args.mode,
        args.form,
        args.target,
        args.name,
        args.branch,
        enable_telemetrydesc:
                    print(f"    {desc}")
        else:
            print(f"No forms found for mode '{args.list_forms}' or unable to connect to GitHub")
        return 0
    
    # Interactive mode
    if args.interactive:
        success = interactive_mode(args.branch)
        return 0 if success else 1
    
    # Direct mode - require mode and form
    if not args.mode or not args.form:
        parser.error("--mode and --form are required unless using --interactive, --list-modes, or --list-forms")
    
    success = initialize_project(
        args.mode,
        args.form,
        args.target,
        args.name,
        args.branch
    )
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
