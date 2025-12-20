# CLI Tool

Command-line application template using the 3-layer architecture.

## Architecture

This template follows the 3-layer pattern:

**Layer 1: Directives** → See `directives/` for CLI workflow SOPs  
**Layer 2: Orchestration** → AI agent coordinates development  
**Layer 3: Execution** → CLI commands and core business logic

## Project Structure

```
src/
├── cli/            # CLI command definitions
├── core/           # Business logic
└── utils/          # Helper functions
directives/         # Workflow SOPs
execution/          # Utility scripts
tests/              # Test suite
```

## Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .

# Configure
cp .env.example .env
```

## Usage

After installation, run:

```bash
# Get help
mytool --help

# Example commands (customize for your tool)
mytool process --input data.csv --output results.json
mytool config --set key=value
mytool status
```

## Development

### Adding Commands

Edit `src/cli/__init__.py`:

```python
import click

@click.group()
def main():
    """My CLI tool description."""
    pass

@main.command()
@click.option('--input', '-i', required=True, help='Input file')
def process(input):
    """Process the input file."""
    click.echo(f"Processing {input}...")
```

### Testing

```bash
# Run tests
pytest

# With coverage
pytest --cov=src --cov-report=html
```

## Directives

Check `directives/` for:
- Command design patterns
- Configuration management
- Error handling strategies
- Testing approaches

## Distribution

```bash
# Build package
python setup.py sdist bdist_wheel

# Install from wheel
pip install dist/cli-tool-0.1.0-py3-none-any.whl
```

## Contributing Back to Arche

As you work with this template, you'll discover better patterns, edge cases, and improvements. **Please contribute these learnings back:**

- Found a missing dependency? Create an issue.
- Discovered a better workflow? Share it.
- Hit an edge case? Document it.

Create issues at: https://github.com/coreyshort/arche/issues

Your improvements make arche stronger for everyone. This is how the system evolves—through real-world usage feeding back into better templates.
