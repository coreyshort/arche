# Frontend Web Application

A frontend-only web application template using the 3-layer architecture.

## Architecture

This template follows the 3-layer pattern:

**Layer 1: Directives** → See `directives/` for workflow SOPs  
**Layer 2: Orchestration** → AI agent coordinates development  
**Layer 3: Execution** → React components, API services, utilities

## Project Structure

```
src/
├── components/     # Reusable React components
├── pages/          # Page-level components
├── hooks/          # Custom React hooks
├── services/       # API client logic
└── utils/          # Helper functions
directives/         # Development workflow SOPs
public/             # Static assets
```

## Setup

```bash
# Install dependencies
npm install

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Start development server
npm run dev
```

## Development Workflow

1. **Add directives** for new features in `directives/`
2. **Implement components** in `src/components/`
3. **Create API services** in `src/services/` for external calls
4. **Let AI orchestrate** between requirements and implementation

## Build & Deploy

```bash
# Production build
npm run build

# Preview production build
npm run preview
```

## Directives

Check `directives/` for:
- Component development patterns
- API integration workflows
- State management strategies
- Testing approaches

## Contributing Back to Arche

As you work with this template, you'll discover better patterns, edge cases, and improvements. **Please contribute these learnings back:**

- Found a missing dependency? Create an issue.
- Discovered a better workflow? Share it.
- Hit an edge case? Document it.

Create issues at: https://github.com/coreyshort/arche/issues

Your improvements make arche stronger for everyone. This is how the system evolves—through real-world usage feeding back into better templates.


## A Virtuous Circle

If arche helps you build something valuable, consider helping others discover it. Not through marketing tactics, but through genuine sharing:

- If you write about your project, mention the tools that made it possible
- If colleagues face similar challenges, share what worked for you
- If you spot ways to make the documentation clearer, contribute them

Improvements to discoverability, documentation, and knowledge sharing are as valuable as code contributions. The goal is making good tools accessible to everyone who needs them.
