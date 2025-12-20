# Python Library Template

A reusable Python package/library template using the 3-layer architecture.

## Architecture

This template follows the 3-layer pattern for library development:

**Layer 1: Directives** → See `directives/` for development SOPs  
**Layer 2: Orchestration** → AI agent coordinates development  
**Layer 3: Execution** → Library code with deterministic behavior

## Project Structure

```
src/package_name/     # Your library code
tests/                # Test suite
docs/                 # Documentation
examples/             # Usage examples
directives/           # Development SOPs
```

## Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e ".[dev]"

# Or install all extras
pip install -e ".[dev,docs]"
```

## Development Workflow

### 1. Rename Package
Replace `package_name` throughout the project:
- `src/package_name/` directory
- Import statements
- `setup.py` package references

### 2. Add Functionality
Implement your library in `src/package_name/`:
```python
# src/package_name/core.py
def your_function(arg):
    """Your function documentation."""
    return result
```

### 3. Write Tests
Add tests in `tests/`:
```python
# tests/test_core.py
from package_name.core import your_function

def test_your_function():
    assert your_function("input") == "expected"
```

### 4. Run Tests
```bash
# Run all tests
pytest

# With coverage
pytest --cov=package_name --cov-report=html

# Test across Python versions
tox
```

### 5. Format Code
```bash
# Format with Black
black src/ tests/

# Sort imports
isort src/ tests/

# Lint
flake8 src/ tests/

# Type check
mypy src/
```

## Documentation

```bash
# Build docs
cd docs
make html

# View docs
open _build/html/index.html
```

## Distribution

### Build Package
```bash
# Install build tools
pip install build twine

# Build distribution
python -m build

# Check the build
twine check dist/*
```

### Publish to PyPI
```bash
# Test PyPI first
twine upload --repository testpypi dist/*

# Production PyPI
twine upload dist/*
```

## Usage Examples

See `examples/` for usage examples:
```python
from package_name import your_function

result = your_function("input")
print(result)
```

## Directives

Check `directives/` for:
- API design guidelines
- Testing strategies
- Documentation standards
- Release procedures

## Version Management

This project uses [Semantic Versioning](https://semver.org/):
- MAJOR.MINOR.PATCH
- Update version in `setup.py`
- Tag releases: `git tag v0.1.0`
