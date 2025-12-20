# CLI Command Design Directive

## Goal
Design and implement command-line commands with consistent UX and error handling.

## Inputs
- Command requirements and functionality
- Expected arguments and options
- Output format specifications

## Process

### 1. Command Structure
Use Click for command definition:

```python
# src/cli/__init__.py
import click
from rich.console import Console
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
console = Console()

@click.group()
@click.version_option(version='0.1.0')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose output')
@click.pass_context
def main(ctx, verbose):
    """My CLI Tool - Description of what it does."""
    ctx.ensure_object(dict)
    ctx.obj['VERBOSE'] = verbose
    
    if verbose:
        console.print("[blue]Verbose mode enabled[/blue]")

@main.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--output', '-o', type=click.Path(), help='Output file path')
@click.option('--format', type=click.Choice(['json', 'csv', 'yaml']), default='json')
@click.pass_context
def process(ctx, input_file, output, format):
    """Process an input file and generate output.
    
    Example:
        mytool process data.csv -o results.json --format json
    """
    try:
        console.print(f"[green]Processing {input_file}...[/green]")
        
        # Import business logic from src/core/
        from src.core.processor import process_file
        
        result = process_file(input_file, format)
        
        if output:
            Path(output).write_text(result)
            console.print(f"[green]✓[/green] Output saved to {output}")
        else:
            console.print(result)
            
    except Exception as e:
        console.print(f"[red]✗ Error:[/red] {str(e)}")
        if ctx.obj['VERBOSE']:
            console.print_exception()
        raise click.Abort()

if __name__ == '__main__':
    main()
```

### 2. Command Design Principles
- **Single responsibility**: Each command does one thing well
- **Composable**: Commands can be chained or scripted
- **Idempotent**: Running twice produces same result
- **Fail gracefully**: Clear error messages, non-zero exit codes

### 3. Argument vs Option Guidelines
**Arguments** (positional, required):
- Input files
- Primary resource identifiers
- Core required values

**Options** (named, often optional):
- Flags and switches
- Configuration overrides
- Output formatting
- Behavioral modifiers

### 4. User Feedback
Use Rich for enhanced output:

```python
from rich.console import Console
from rich.progress import track
from rich.table import Table

console = Console()

# Progress bars
for item in track(items, description="Processing..."):
    process(item)

# Tables
table = Table(title="Results")
table.add_column("Name", style="cyan")
table.add_column("Status", style="green")
for row in results:
    table.add_row(row['name'], row['status'])
console.print(table)

# Styled messages
console.print("[green]✓[/green] Success!")
console.print("[red]✗[/red] Error occurred")
console.print("[yellow]⚠[/yellow] Warning")
```

### 5. Configuration Management
Support multiple config sources (priority order):
1. Command-line options (highest)
2. Environment variables
3. Config file (YAML/JSON)
4. Defaults (lowest)

```python
import yaml
from pathlib import Path

def load_config():
    config_file = os.getenv('CONFIG_FILE', 'config.yaml')
    if Path(config_file).exists():
        with open(config_file) as f:
            return yaml.safe_load(f)
    return {}
```

## Outputs
- Functional CLI command with help text
- Clear success/error messages
- Appropriate exit codes (0 = success, non-zero = error)

## Edge Cases
- **Missing required files** → Show clear error, suggest solutions
- **Invalid input format** → Validate early, fail fast
- **Permission errors** → Check file access before processing
- **Large inputs** → Show progress, allow interruption (Ctrl+C)
- **Piped input** → Support stdin: `cat data | mytool process -`

## Tools/Scripts
- Click for argument parsing
- Rich for enhanced terminal output
- PyYAML for config files
- Python-dotenv for environment variables

## Success Criteria
- Command runs with `--help` showing clear documentation
- Required arguments validated before processing
- Error messages are actionable
- Exit codes are correct (0 for success)
- Works in both interactive and scripted contexts
