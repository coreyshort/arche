# Data Science Project

ML/Data Science workflow template using the 3-layer architecture.

## Architecture

This template follows the 3-layer pattern:

**Layer 1: Directives** → See `directives/` for data workflow SOPs  
**Layer 2: Orchestration** → AI agent coordinates analysis pipeline  
**Layer 3: Execution** → Production scripts in `execution/`

## Project Structure

```
notebooks/
├── exploration/    # EDA and data analysis
├── training/       # Model training experiments
└── evaluation/     # Model evaluation and comparison
execution/          # Production pipeline scripts
directives/         # Workflow SOPs
models/             # Trained model artifacts
data/               # Local data (gitignored)
.tmp/               # Temporary files
```

## Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Start Jupyter
jupyter lab
```

## Workflow

### 1. Exploration Phase
- Create notebooks in `notebooks/exploration/`
- Perform EDA, visualizations, hypothesis testing
- Document findings and insights

### 2. Experimentation Phase
- Create training notebooks in `notebooks/training/`
- Try different models and hyperparameters
- Use MLflow/Wandb to track experiments

### 3. Production Phase
- Convert best approaches to scripts in `execution/`
- Implement data pipelines
- Save trained models to `models/`

## Directives

Check `directives/` for:
- Data validation workflows
- Feature engineering patterns
- Model training procedures
- Evaluation strategies

## Best Practices

- **Never commit data files** - Use `.gitignore`
- **Track experiments** - Use MLflow or Wandb
- **Version models** - Save with timestamps/versions
- **Document assumptions** - In notebooks and directives
- **Validate data** - Always check data quality

## Contributing Back to Arche

As you work with this template, you'll discover better patterns, edge cases, and improvements. **Please contribute these learnings back:**

- Found a missing dependency? Create an issue.
- Discovered a better workflow? Share it.
- Hit an edge case? Document it.

Create issues at: https://github.com/coreyshort/arche/issues

Your improvements make arche stronger for everyone. This is how the system evolves—through real-world usage feeding back into better templates.

## Growing Arche's Reach

Arche improves with wider adoption. More users means more feedback, better templates, and a stronger ecosystem. Consider:

- Share your project on social media (Twitter, LinkedIn, dev.to)
- Write a blog post about your experience with arche
- Suggest README improvements or SEO optimizations
- Recommend arche to colleagues working on similar projects

Marketing and outreach suggestions are valuable improvements—create issues for them too!
