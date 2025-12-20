# Arche

**arche** is named after the ancient Greek concept of *archē*—the first principle, origin, or underlying cause from which things come into being.

In philosophy, the archē is not a thing but a generative source: the set of assumptions, structures, and forces that make creation possible. Arche exists in that same spirit. It is not an agent, but the framework from which agents emerge—defining how intent becomes action, how reasoning is shaped, and how systems learn to build themselves. When an agent says "Arche built this," it reflects a lineage: a common origin of patterns, constraints, and principles that guide autonomous work without prescribing its outcomes.

Forms

In Aristotelian philosophy, a form is the organizing principle that makes a thing what it is—distinct from its material, yet inseparable from its realization. A form defines structure, purpose, and potential without prescribing a single instantiation. In Arche, Forms serve the same role. They describe the canonical shapes of projects and agents: enduring patterns of intent, structure, and behavior from which concrete systems can be brought into being. A form is not a template to be copied, but a conceptual lineage to be expressed. When an agent or project is created, it does not merely follow a pattern—it instantiates a form, carrying forward the principles that define how it should reason, act, and evolve.

---

## The 3-Layer Architecture

Arche provides battle-tested project templates implementing a 3-layer architecture that maximizes reliability:

- **Layer 1: Directives** - SOPs in Markdown defining *what* to do
- **Layer 2: Orchestration** - AI agents making intelligent decisions
- **Layer 3: Execution** - Deterministic code that *does* the work

**Why this works:** If AI handles everything, errors compound. 90% accuracy per step = 59% success over 5 steps. The solution is to push complexity into deterministic code. AI focuses on intelligent routing, decision-making, and error handling—while reliable code handles API calls, data processing, and complex business logic.

---

## Available Templates

### 🤖 Automation
**Use for:** Data processing, ETL pipelines, web scraping, report generation, task automation

**Includes:**
- Python virtual environment setup
- Directive and execution script templates  
- Data management structure (`.tmp/`, `local_data/`)
- Common dependencies (pandas, openpyxl, dotenv)

**[View Template →](forms/automation/)**

---

### 🌐 Web App - Full Stack
**Use for:** Complete web applications with frontend and backend

**Includes:**
- Next.js/React frontend structure
- Node.js/Express backend API
- Shared types and utilities
- Docker setup for services

**[View Template →](forms/webapp-fullstack/)**

---

### 🎨 Web App - Frontend Only
**Use for:** Single-page applications, frontend-only projects

**Includes:**
- React + TypeScript with Vite
- Component development directives
- API service integration patterns
- Modern development tooling (ESLint, Prettier)

**[View Template →](forms/webapp-frontend/)**

---

### 🔌 API Service
**Use for:** Backend API services, REST APIs, microservices

**Includes:**
- Express.js/FastAPI templates
- Database migrations and models
- JWT authentication patterns
- Rate limiting and middleware

**[View Template →](forms/api-service/)**

---

### 📊 Data Science
**Use for:** ML/Data Science workflows, model training, data analysis

**Includes:**
- Jupyter notebook structure (exploration, training, evaluation)
- MLflow experiment tracking
- Data validation workflows
- Model training directives

**[View Template →](forms/data-science/)**

---

### 🖥️ CLI Tool
**Use for:** Command-line applications, developer tools, utilities

**Includes:**
- Click framework setup
- Rich terminal output
- Configuration management
- Testing and packaging setup

**[View Template →](forms/cli-tool/)**

---

### 📦 Library
**Use for:** Reusable Python packages, libraries, SDKs

**Includes:**
- Proper package structure
- API design directives
- Testing and type checking
- Documentation and distribution setup

**[View Template →](forms/library/)**

---

## Quick Start

### Option 1: Bootstrap Script (Recommended)

```bash
# Download bootstrap script
curl -O https://raw.githubusercontent.com/coreyshort/arche/main/tools/bootstrap.py

# Interactive mode - guided setup
python bootstrap.py --interactive

# Or directly specify template
python bootstrap.py --type automation

# List all available templates
python bootstrap.py --list
```

### Option 2: Git Sparse Checkout

For advanced users who want fine-grained control:

```bash
# Initialize new project
mkdir my-project && cd my-project
git init

# Add Arche as remote
git remote add template https://github.com/coreyshort/arche.git
git config core.sparseCheckout true

# Specify what to fetch
echo "_shared/*" >> .git/info/sparse-checkout
echo "automation/*" >> .git/info/sparse-checkout

# Pull and flatten
git pull template main
mv _shared/* . && mv automation/* .
rm -rf _shared automation

# Start fresh
git remote remove template
git add .
git commit -m "Initialize from Arche template"
```

---

## After Initialization

### 1. Setup Environment

```bash
cd your-project

# Python projects
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Node.js projects
npm install  # or yarn install
```

### 2. Configure

```bash
# Copy environment template
cp .env.example .env

# Edit with your API keys and settings
nano .env  # or your preferred editor
```

### 3. Start Building

- **Add directives** in `directives/` for your workflows
- **Create execution scripts** in `execution/` for deterministic operations
- **Let AI orchestrate** between directives and execution

---

## Project Structure

Each template follows this organization:

```
template-name/
├── project.json           # Template metadata and initialization config
├── .gitignore            # Project-type-specific exclusions
├── .env.example          # Environment variable templates
├── README.md             # Project documentation template
├── requirements.txt      # Dependencies (Python projects)
│   or package.json       # Dependencies (Node projects)
├── directives/           # SOPs and workflow definitions
│   └── _template_directive.md
└── execution/            # Deterministic scripts/code
    └── _template_script.py
```

All templates share these files from `_shared/`:
- `agents.md` - Core 3-layer architecture instructions
- `init_env.md` - Environment setup guide

---

## The Self-Annealing Loop

The architecture improves over time through continuous learning:

1. **Encounter an issue** during development
2. **Fix the execution script** (deterministic code)
3. **Test it** to ensure it works
4. **Update the directive** with new learnings
5. **System is now stronger** for next time

---

## Bootstrap Script Features

The `bootstrap.py` script provides:

- ✅ **Interactive mode** - Guided template selection
- ✅ **Direct initialization** - Specify template with `--type` flag
- ✅ **Template listing** - Browse available templates with `--list`
- ✅ **Version pinning** - Use specific releases with `--branch v1.0.0`
- ✅ **No dependencies** - Pure Python stdlib, no pip install needed
- ✅ **Smart fetching** - Only downloads needed files from GitHub

### Usage Examples

```bash
# Interactive wizard
python bootstrap.py --interactive

# Direct initialization in current directory
python bootstrap.py --type automation

# Initialize in specific directory
python bootstrap.py --type automation --target ~/projects/my-etl

# Use specific version
python bootstrap.py --type automation --branch v1.0.0

# List available templates
python bootstrap.py --list
```

---

## Philosophy in Practice

### The Problem with Pure AI Coding

When AI writes all code directly, small errors compound:
- 90% accuracy per step
- 5 steps = 0.9^5 = 59% success rate
- Complex workflows become unreliable

### The Solution: Separation of Concerns

**AI excels at:**
- Understanding natural language requirements
- Making decisions based on context
- Routing between different tools
- Handling edge cases and errors
- Updating documentation with learnings

**Deterministic code excels at:**
- Consistent, repeatable operations
- Complex data transformations
- API integrations
- File system operations
- Database transactions

**The 3-layer architecture combines both strengths.**

---

## Contributing Templates

Have a project type that would benefit from this architecture?

**Propose a new template:**
1. Create a GitHub Issue at https://github.com/coreyshort/arche/issues
2. Use the "Template Improvement" template
3. Include:
   - Category: Select "template-new" or relevant category
   - Use case description and target users
   - Proposed directory structure
   - Required dependencies and configuration
   - Example directive and execution patterns
4. Maintainer will review and create implementation PR

**You do NOT need fork/write access**—the improvement workflow handles everything through GitHub Issues.

### Template Design Guidelines

When proposing templates:
- [ ] Clear use case and description
- [ ] `project.json` with all metadata
- [ ] Example directive showing SOP structure
- [ ] Example execution script demonstrating patterns
- [ ] Sensible defaults for common tools
- [ ] Documentation explaining the workflow
- [ ] Compatible with bootstrap script

---

## Examples & Use Cases

### Automation Template

Perfect for:
- ETL pipelines pulling data from APIs
- Web scraping with error handling
- Report generation from databases
- Batch file processing
- Data warehouse updates
- Scheduled task automation

### Web App Template *(Coming Soon)*

Perfect for:
- SaaS applications
- Internal tools
- Customer portals
- Content management systems
- Real-time dashboards

### API Service Template *(Coming Soon)*

Perfect for:
- Microservices
- REST/GraphQL APIs
- Webhook handlers
- Integration middleware
- Backend services

---

## Version History

- **v1.0.0** - Initial release with automation template
- More templates coming soon!

---

## Links

- **Repository:** https://github.com/coreyshort/arche
- **Issues:** https://github.com/coreyshort/arche/issues
- **Discussions:** https://github.com/coreyshort/arche/discussions

---

## Attribution

If you use this project, attribution or a link back to this repository is appreciated.

**License:** [View LICENSE](LICENSE)

---

*Built for reliable AI-assisted development*
