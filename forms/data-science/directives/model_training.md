# Model Training Directive

## Goal
Train machine learning models with proper experiment tracking and reproducibility.

## Inputs
- Prepared training and validation datasets
- Model architecture/algorithm choice
- Hyperparameters to tune
- Evaluation metrics

## Process

### 1. Setup Experiment Tracking
```python
import mlflow
import mlflow.sklearn
from datetime import datetime

# Set experiment
mlflow.set_experiment("model-training")

# Start run
with mlflow.start_run(run_name=f"experiment-{datetime.now().strftime('%Y%m%d-%H%M')}"):
    # Log parameters, metrics, and model
    mlflow.log_params(params)
    mlflow.log_metrics(metrics)
    mlflow.sklearn.log_model(model, "model")
```

### 2. Training Script Template
Create in `execution/train_model.py`:

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report
import mlflow
import mlflow.sklearn
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def load_and_prepare_data(data_path: str):
    """Load and split data into train/val sets."""
    df = pd.read_csv(data_path)
    
    # Separate features and target
    X = df.drop('target', axis=1)
    y = df['target']
    
    # Split data
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    return X_train, X_val, y_train, y_val

def train_model(X_train, y_train, params):
    """Train model with given parameters."""
    model = RandomForestClassifier(**params, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_val, y_val):
    """Evaluate model and return metrics."""
    y_pred = model.predict(X_val)
    
    metrics = {
        'accuracy': accuracy_score(y_val, y_pred),
        'f1_score': f1_score(y_val, y_pred, average='weighted')
    }
    
    report = classification_report(y_val, y_pred)
    
    return metrics, report

def main():
    # Configuration
    data_path = 'data/processed_data.csv'
    model_dir = Path(os.getenv('MODEL_DIR', './models'))
    model_dir.mkdir(exist_ok=True)
    
    # Hyperparameters
    params = {
        'n_estimators': 100,
        'max_depth': 10,
        'min_samples_split': 5,
        'min_samples_leaf': 2
    }
    
    # Set experiment
    mlflow.set_experiment("model-training")
    
    with mlflow.start_run():
        # Log parameters
        mlflow.log_params(params)
        
        # Load data
        print("Loading data...")
        X_train, X_val, y_train, y_val = load_and_prepare_data(data_path)
        
        # Train model
        print("Training model...")
        model = train_model(X_train, y_train, params)
        
        # Evaluate
        print("Evaluating model...")
        metrics, report = evaluate_model(model, X_val, y_val)
        
        # Log metrics
        mlflow.log_metrics(metrics)
        
        # Log model
        mlflow.sklearn.log_model(model, "model")
        
        # Save locally
        import joblib
        model_path = model_dir / f"model_{mlflow.active_run().info.run_id}.pkl"
        joblib.dump(model, model_path)
        mlflow.log_artifact(model_path)
        
        print(f"\nResults:")
        print(f"Accuracy: {metrics['accuracy']:.4f}")
        print(f"F1 Score: {metrics['f1_score']:.4f}")
        print(f"\nClassification Report:\n{report}")
        print(f"\nModel saved to: {model_path}")

if __name__ == "__main__":
    main()
```

### 3. Hyperparameter Tuning
For systematic tuning, use GridSearchCV or Optuna:

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='f1_weighted',
    n_jobs=-1
)

grid_search.fit(X_train, y_train)
best_model = grid_search.best_estimator_
```

### 4. Model Versioning
- Save models with timestamps: `model_20241219_143052.pkl`
- Track model versions in MLflow
- Document model lineage (data version + code version + hyperparameters)

## Outputs
- Trained model artifact saved to `models/`
- Experiment logged in MLflow with metrics
- Training logs and evaluation reports
- Model card documenting performance

## Edge Cases
- **Imbalanced classes** → Use SMOTE, class weights, or stratified sampling
- **Overfitting** → Add regularization, reduce complexity, use cross-validation
- **Long training times** → Use early stopping, reduce data size for prototyping
- **NaN predictions** → Check for missing values in features
- **Model degradation** → Monitor performance on new data

## Tools/Scripts
- `execution/train_model.py` - Main training script
- MLflow for experiment tracking
- Scikit-learn, TensorFlow, or PyTorch for models
- Joblib or pickle for model serialization

## Success Criteria
- Model trains without errors
- Validation metrics meet minimum thresholds
- All experiments are tracked in MLflow
- Model is saved and reproducible
- Performance is documented
