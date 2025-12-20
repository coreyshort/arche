# Data Validation Directive

## Goal
Ensure data quality and consistency before analysis or model training.

## Inputs
- Raw data files (CSV, Excel, database exports, API responses)
- Data schema/specifications
- Expected data ranges and constraints

## Process

### 1. Initial Inspection
```python
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data/raw_data.csv')

# Basic info
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(df.info())
print(df.describe())
```

### 2. Check for Issues
- **Missing values**: `df.isnull().sum()`
- **Duplicates**: `df.duplicated().sum()`
- **Data types**: Verify expected types
- **Value ranges**: Check min/max make sense
- **Unique values**: For categorical columns

### 3. Validation Script Template
Create in `execution/validate_data.py`:

```python
import pandas as pd
from pathlib import Path

def validate_dataframe(df: pd.DataFrame, schema: dict) -> dict:
    """Validate dataframe against expected schema.
    
    Args:
        df: DataFrame to validate
        schema: Dict with expected columns, types, constraints
        
    Returns:
        Dict with validation results and issues found
    """
    issues = []
    
    # Check required columns
    missing_cols = set(schema['required_columns']) - set(df.columns)
    if missing_cols:
        issues.append(f"Missing columns: {missing_cols}")
    
    # Check data types
    for col, expected_type in schema.get('types', {}).items():
        if col in df.columns and df[col].dtype != expected_type:
            issues.append(f"Column {col} has type {df[col].dtype}, expected {expected_type}")
    
    # Check value ranges
    for col, (min_val, max_val) in schema.get('ranges', {}).items():
        if col in df.columns:
            if df[col].min() < min_val or df[col].max() > max_val:
                issues.append(f"Column {col} values outside range [{min_val}, {max_val}]")
    
    # Check for nulls in required columns
    for col in schema.get('not_null', []):
        if col in df.columns and df[col].isnull().any():
            issues.append(f"Column {col} has null values")
    
    return {
        'valid': len(issues) == 0,
        'issues': issues,
        'row_count': len(df),
        'null_counts': df.isnull().sum().to_dict()
    }

if __name__ == "__main__":
    # Example usage
    df = pd.read_csv('data/input.csv')
    
    schema = {
        'required_columns': ['id', 'value', 'category'],
        'types': {'id': 'int64', 'value': 'float64'},
        'ranges': {'value': (0, 100)},
        'not_null': ['id', 'category']
    }
    
    results = validate_dataframe(df, schema)
    print(f"Validation: {'✓ PASSED' if results['valid'] else '✗ FAILED'}")
    if not results['valid']:
        print("Issues found:")
        for issue in results['issues']:
            print(f"  - {issue}")
```

### 4. Handle Common Issues
- **Missing values**: Impute, drop, or flag
- **Duplicates**: Remove or aggregate
- **Outliers**: Investigate, cap, or remove
- **Inconsistent formats**: Standardize dates, strings
- **Data drift**: Compare distributions over time

## Outputs
- Validation report (pass/fail with issues)
- Cleaned dataset (if issues were fixable)
- Documentation of data quality issues

## Edge Cases
- Empty datasets → Fail validation
- Unexpected columns → Log warning, proceed if required columns present
- Encoding issues → Try different encodings (utf-8, latin-1)
- Large files → Use chunking: `pd.read_csv(chunksize=10000)`

## Tools/Scripts
- `execution/validate_data.py` - Data validation script
- Pandas for data manipulation
- Great Expectations (optional) for advanced validation

## Success Criteria
- All required columns present
- No critical data quality issues
- Data types match expectations
- Value ranges are reasonable
- Validation results documented
