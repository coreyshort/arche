# API Design Directive

## Goal
Design clean, intuitive, and maintainable public APIs for the library.

## Inputs
- Functionality requirements
- User personas and use cases
- Similar libraries for inspiration

## Process

### 1. API Design Principles

**Simplicity**: Most common use cases should be simple
```python
# Good: Simple common case
result = process(data)

# Avoid: Requiring too many arguments for common cases
result = process(data, format='json', validate=True, strict=False, encoding='utf-8')
```

**Consistency**: Similar operations should work similarly
```python
# Good: Consistent patterns
client.get_user(id)
client.get_post(id)
client.get_comment(id)

# Avoid: Inconsistent naming
client.fetch_user(id)
client.retrieve_post(id)
client.load_comment(id)
```

**Explicitness**: Better explicit than implicit
```python
# Good: Clear about what's happening
save_to_file(data, path="output.json", overwrite=True)

# Avoid: Implicit behavior
save(data, "output.json")  # Does it overwrite? Who knows?
```

### 2. Module Organization

```
src/package_name/
├── __init__.py          # Public API exports
├── core.py              # Core functionality
├── exceptions.py        # Custom exceptions
├── utils.py             # Utility functions
├── _internal.py         # Private/internal code (prefix with _)
└── submodule/           # Feature-specific submodules
    ├── __init__.py
    └── feature.py
```

### 3. Public API in `__init__.py`

```python
# src/package_name/__init__.py
"""Package description and usage example."""

__version__ = "0.1.0"

# Export public API
from .core import MainClass, main_function
from .exceptions import PackageError, ValidationError

# Define what's exported with import *
__all__ = [
    "MainClass",
    "main_function",
    "PackageError",
    "ValidationError",
]
```

### 4. Class Design

```python
# src/package_name/core.py
from typing import Optional, List, Dict, Any

class DataProcessor:
    """Process data with various transformations.
    
    Args:
        config: Configuration dictionary
        validate: Whether to validate inputs (default: True)
        
    Example:
        >>> processor = DataProcessor({"format": "json"})
        >>> result = processor.process(data)
    """
    
    def __init__(
        self,
        config: Optional[Dict[str, Any]] = None,
        validate: bool = True
    ):
        self.config = config or {}
        self.validate = validate
        
    def process(self, data: List[Dict]) -> List[Dict]:
        """Process a list of data items.
        
        Args:
            data: List of dictionaries to process
            
        Returns:
            Processed data
            
        Raises:
            ValidationError: If validation fails
            ProcessingError: If processing fails
        """
        if self.validate:
            self._validate(data)
        
        return self._transform(data)
    
    def _validate(self, data: List[Dict]) -> None:
        """Internal validation method."""
        # Private methods start with _
        pass
    
    def _transform(self, data: List[Dict]) -> List[Dict]:
        """Internal transformation method."""
        pass
```

### 5. Function Design

```python
def process_data(
    data: List[Dict],
    *,  # Force keyword arguments after this
    format: str = "json",
    validate: bool = True,
    **kwargs  # Accept additional options
) -> Dict[str, Any]:
    """Process data and return results.
    
    Args:
        data: Input data to process
        format: Output format (json, csv, xml)
        validate: Whether to validate inputs
        **kwargs: Additional processing options
        
    Returns:
        Dictionary with processing results
        
    Raises:
        ValueError: If format is invalid
        ValidationError: If validation fails
        
    Example:
        >>> result = process_data(data, format="json")
        >>> print(result['status'])
        'success'
    """
    pass
```

### 6. Custom Exceptions

```python
# src/package_name/exceptions.py
class PackageError(Exception):
    """Base exception for package_name."""
    pass

class ValidationError(PackageError):
    """Raised when validation fails."""
    pass

class ProcessingError(PackageError):
    """Raised when processing fails."""
    pass
```

### 7. Type Hints

Always use type hints for public API:

```python
from typing import List, Dict, Optional, Union, Callable

def transform(
    data: List[Dict[str, Any]],
    transformer: Callable[[Dict], Dict],
    filter_fn: Optional[Callable[[Dict], bool]] = None
) -> List[Dict[str, Any]]:
    """Transform data using provided function."""
    pass
```

### 8. Documentation Standards

Every public function/class needs:
- One-line summary
- Args section
- Returns section
- Raises section (if applicable)
- Example usage

```python
def example(arg1: str, arg2: int = 10) -> bool:
    """One-line summary of what this does.
    
    More detailed explanation if needed. Can span multiple
    lines and include context, algorithms, etc.
    
    Args:
        arg1: Description of arg1
        arg2: Description of arg2 (default: 10)
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When arg2 is negative
        
    Example:
        >>> result = example("test", 5)
        >>> print(result)
        True
    """
    pass
```

## Outputs
- Well-documented public API
- Type-hinted functions and classes
- Custom exceptions for error cases
- Clear examples in docstrings

## Edge Cases
- Backward compatibility → Use deprecation warnings
- Breaking changes → Major version bump
- Optional dependencies → Graceful fallbacks
- Configuration → Sane defaults

## Tools/Scripts
- mypy for type checking
- pydocstyle for docstring validation
- sphinx for documentation generation

## Success Criteria
- All public APIs have type hints
- All public APIs have complete docstrings
- No mypy errors
- Examples in docstrings work
- API is intuitive for target users
