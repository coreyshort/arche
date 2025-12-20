#!/usr/bin/env python3
"""
Arche Update Tool - Manage framework updates for your arche project

This script checks for updates to arche framework files and applies them
according to your configured update strategy.

Usage:
    python update_arche.py --check              # Check for updates
    python update_arche.py --diff               # Show what would change
    python update_arche.py --apply              # Apply updates
    python update_arche.py --set-strategy auto  # Change update strategy
    python update_arche.py --rollback TIMESTAMP # Rollback to backup

Update Strategies:
    auto   - Automatically apply updates (default)
    frozen - Never update (stable snapshot)
    manual - Only update when explicitly requested
    prompt - Ask periodically whether to update
"""

import argparse
import json
import sys
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime, timedelta
import shutil
import hashlib
from typing import Dict, List, Optional, Tuple


REPO_URL = "https://github.com/coreyshort/arche"
RAW_URL = "https://raw.githubusercontent.com/coreyshort/arche"
API_URL = "https://api.github.com/repos/coreyshort/arche"


def load_config() -> Dict:
    """Load .arche-config from current directory."""
    config_file = Path(".arche-config")
    if not config_file.exists():
        print("✗ .arche-config not found. Are you in an arche project directory?")
        print(f"  Expected: {config_file.absolute()}")
        sys.exit(1)
    
    try:
        return json.loads(config_file.read_text())
    except json.JSONDecodeError as e:
        print(f"✗ Invalid .arche-config: {e}")
        sys.exit(1)


def save_config(config: Dict):
    """Save config to .arche-config."""
    config_file = Path(".arche-config")
    config_file.write_text(json.dumps(config, indent=2))


def get_file_hash(file_path: Path) -> str:
    """Get SHA256 hash of file contents."""
    if not file_path.exists():
        return ""
    return hashlib.sha256(file_path.read_bytes()).hexdigest()


def fetch_latest_version(branch: str = "main") -> Optional[str]:
    """Fetch latest commit SHA or tag from GitHub."""
    try:
        url = f"{API_URL}/commits/{branch}"
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            return data["sha"][:7]  # Short SHA
    except urllib.error.URLError:
        print("⚠ Unable to check for updates (no internet connection)")
        return None


def fetch_framework_files(mode: str, branch: str = "main") -> Dict[str, str]:
    """Fetch framework files from GitHub for the specified mode."""
    files = {}
    base_path = f"modes/{mode}/_shared"
    
    # Common framework files
    framework_files = ["agents.md", "INSTRUCTIONS.md", "init_env.md"]
    
    for filename in framework_files:
        url = f"{RAW_URL}/{branch}/{base_path}/{filename}"
        try:
            with urllib.request.urlopen(url) as response:
                files[filename] = response.read().decode('utf-8')
        except urllib.error.URLError:
            # File might not exist in this mode
            continue
    
    return files


def check_for_updates(config: Dict, verbose: bool = True) -> Tuple[bool, Dict[str, str]]:
    """
    Check if updates are available.
    Returns: (updates_available, files_dict)
    """
    mode = config.get("mode")
    current_version = config.get("arche_version", "unknown")
    branch = config.get("branch", "main")
    
    if verbose:
        print(f"🔍 Checking for updates...")
        print(f"   Mode: {mode}")
        print(f"   Current version: {current_version}")
    
    latest_version = fetch_latest_version(branch)
    if not latest_version:
        return False, {}
    
    if verbose:
        print(f"   Latest version: {latest_version}")
    
    if latest_version == current_version:
        if verbose:
            print("✓ You're up to date!")
        return False, {}
    
    # Fetch latest files
    latest_files = fetch_framework_files(mode, branch)
    
    if not latest_files:
        if verbose:
            print("✗ Unable to fetch framework files")
        return False, {}
    
    # Check which files have changed
    changed_files = {}
    for filename, content in latest_files.items():
        local_file = Path(filename)
        if not local_file.exists():
            # New file
            changed_files[filename] = content
            continue
        
        local_hash = get_file_hash(local_file)
        remote_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()
        
        if local_hash != remote_hash:
            changed_files[filename] = content
    
    if changed_files and verbose:
        print(f"\n📦 Updates available:")
        for filename in changed_files.keys():
            print(f"   • {filename}")
    
    return bool(changed_files), changed_files


def show_diff(config: Dict):
    """Show diff of what would change."""
    mode = config.get("mode")
    branch = config.get("branch", "main")
    
    print(f"📋 Checking differences for {mode} mode...\n")
    
    latest_files = fetch_framework_files(mode, branch)
    
    for filename, new_content in latest_files.items():
        local_file = Path(filename)
        
        if not local_file.exists():
            print(f"➕ {filename} (new file)")
            print(f"   {len(new_content.splitlines())} lines")
            continue
        
        old_content = local_file.read_text()
        old_hash = get_file_hash(local_file)
        new_hash = hashlib.sha256(new_content.encode('utf-8')).hexdigest()
        
        if old_hash != new_hash:
            print(f"📝 {filename} (modified)")
            old_lines = old_content.splitlines()
            new_lines = new_content.splitlines()
            print(f"   {len(old_lines)} lines → {len(new_lines)} lines")
            # Could add actual diff here using difflib
        else:
            print(f"✓ {filename} (unchanged)")
    
    print()


def create_backup() -> str:
    """Create backup of current framework files."""
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_dir = Path(".arche-backups") / timestamp
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    framework_files = ["agents.md", "INSTRUCTIONS.md", "init_env.md"]
    
    for filename in framework_files:
        source = Path(filename)
        if source.exists():
            dest = backup_dir / filename
            shutil.copy2(source, dest)
    
    # Also backup config
    config_source = Path(".arche-config")
    if config_source.exists():
        shutil.copy2(config_source, backup_dir / ".arche-config")
    
    return timestamp


def apply_updates(config: Dict, files: Dict[str, str], auto: bool = False) -> bool:
    """Apply updates to local files."""
    if not files:
        print("✓ No updates to apply")
        return True
    
    print(f"\n📦 Applying updates...")
    
    # Create backup
    print("   Creating backup...")
    timestamp = create_backup()
    print(f"   ✓ Backup created: .arche-backups/{timestamp}/")
    
    # Apply changes
    for filename, content in files.items():
        local_file = Path(filename)
        
        # Check if file was modified by user
        if local_file.exists():
            # Simple check: compare with last known version
            # (In full implementation, would track original hashes)
            pass
        
        print(f"   Updating {filename}...")
        local_file.write_text(content)
        print(f"   ✓ {filename} updated")
    
    # Update config
    latest_version = fetch_latest_version(config.get("branch", "main"))
    if latest_version:
        config["arche_version"] = latest_version
        config["last_update_check"] = datetime.now().strftime("%Y-%m-%d")
        save_config(config)
    
    print(f"\n✅ Updates applied successfully!")
    print(f"   New version: {latest_version}")
    print(f"   Backup: .arche-backups/{timestamp}/")
    print(f"   To rollback: python update_arche.py --rollback {timestamp}")
    
    # Log update
    log_file = Path(".arche-update.log")
    log_entry = f"[{datetime.now().isoformat()}] Updated to {latest_version} - {len(files)} files\n"
    with open(log_file, "a") as f:
        f.write(log_entry)
    
    return True


def rollback(timestamp: str) -> bool:
    """Rollback to a specific backup."""
    backup_dir = Path(".arche-backups") / timestamp
    
    if not backup_dir.exists():
        print(f"✗ Backup not found: {backup_dir}")
        return False
    
    print(f"🔄 Rolling back to backup: {timestamp}")
    
    for backup_file in backup_dir.iterdir():
        if backup_file.name.startswith("."):
            continue
        
        dest = Path(backup_file.name)
        print(f"   Restoring {backup_file.name}...")
        shutil.copy2(backup_file, dest)
        print(f"   ✓ {backup_file.name} restored")
    
    # Restore config
    backup_config = backup_dir / ".arche-config"
    if backup_config.exists():
        shutil.copy2(backup_config, ".arche-config")
    
    print("\n✅ Rollback complete!")
    return True


def set_strategy(strategy: str, interval: Optional[int] = None):
    """Change update strategy."""
    valid_strategies = ["auto", "frozen", "manual", "prompt"]
    
    if strategy not in valid_strategies:
        print(f"✗ Invalid strategy: {strategy}")
        print(f"   Valid options: {', '.join(valid_strategies)}")
        sys.exit(1)
    
    config = load_config()
    config["update_strategy"] = strategy
    
    if strategy == "prompt" and interval:
        config["update_check_interval_days"] = interval
    
    if strategy == "frozen":
        current_version = config.get("arche_version", "unknown")
        config["frozen_version"] = current_version
    
    save_config(config)
    
    print(f"✓ Update strategy set to: {strategy}")
    if strategy == "prompt" and interval:
        print(f"  Check interval: {interval} days")


def check_should_prompt(config: Dict) -> bool:
    """Check if it's time to prompt for updates."""
    strategy = config.get("update_strategy", "auto")
    
    if strategy != "prompt":
        return False
    
    last_check = config.get("last_update_check")
    if not last_check:
        return True
    
    interval_days = config.get("update_check_interval_days", 30)
    last_check_date = datetime.fromisoformat(last_check)
    next_check_date = last_check_date + timedelta(days=interval_days)
    
    return datetime.now() >= next_check_date


def main():
    parser = argparse.ArgumentParser(
        description="Arche Update Tool - Manage framework updates",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("--check", action="store_true", help="Check for updates")
    parser.add_argument("--diff", action="store_true", help="Show what would change")
    parser.add_argument("--apply", action="store_true", help="Apply updates")
    parser.add_argument("--set-strategy", type=str, help="Change update strategy (auto/frozen/manual/prompt)")
    parser.add_argument("--interval", type=int, help="Set check interval in days (for prompt strategy)")
    parser.add_argument("--rollback", type=str, metavar="TIMESTAMP", help="Rollback to specific backup")
    parser.add_argument("--pin", type=str, metavar="VERSION", help="Pin to specific version")
    
    args = parser.parse_args()
    
    config = load_config()
    strategy = config.get("update_strategy", "auto")
    
    # Handle strategy change
    if args.set_strategy:
        set_strategy(args.set_strategy, args.interval)
        return 0
    
    # Handle rollback
    if args.rollback:
        success = rollback(args.rollback)
        return 0 if success else 1
    
    # Handle pin
    if args.pin:
        config["update_strategy"] = "frozen"
        config["frozen_version"] = args.pin
        config["arche_version"] = args.pin
        save_config(config)
        print(f"✓ Pinned to version: {args.pin}")
        return 0
    
    # Check if frozen
    if strategy == "frozen":
        print("🔒 Update strategy: frozen")
        print("   This project will not receive updates.")
        print("   To enable updates: python update_arche.py --set-strategy auto")
        return 0
    
    # Handle check
    if args.check:
        has_updates, files = check_for_updates(config, verbose=True)
        return 0 if not has_updates else 1
    
    # Handle diff
    if args.diff:
        show_diff(config)
        return 0
    
    # Handle apply
    if args.apply or strategy == "auto":
        has_updates, files = check_for_updates(config, verbose=True)
        
        if not has_updates:
            return 0
        
        if strategy == "manual" and not args.apply:
            print("\n💡 Updates available. Run with --apply to install.")
            return 0
        
        success = apply_updates(config, files, auto=(strategy == "auto"))
        return 0 if success else 1
    
    # Default: show status
    print(f"📊 Arche Update Status")
    print(f"   Strategy: {strategy}")
    print(f"   Mode: {config.get('mode')}")
    print(f"   Version: {config.get('arche_version', 'unknown')}")
    
    has_updates, _ = check_for_updates(config, verbose=False)
    if has_updates:
        print("\n   ⬆️  Updates available!")
        print("   Run 'python update_arche.py --check' for details")
    else:
        print("\n   ✓ Up to date")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
