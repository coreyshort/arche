\# Agent Instructions

\> This file is mirrored across CLAUDE.md, AGENTS.md, and GEMINI.md so the same instructions load in any AI environment.

You operate within a 3-layer architecture that separates concerns to maximize reliability. LLMs are probabilistic, whereas most business logic is deterministic and requires consistency. This system fixes that mismatch.

\#\# The 3-Layer Architecture

\*\*Layer 1: Directive (What to do)\*\*  
\- Basically just SOPs written in Markdown, live in \`directives/\`  
\- Define the goals, inputs, tools/scripts to use, outputs, and edge cases  
\- Natural language instructions, like you'd give a mid-level employee

\*\*Layer 2: Orchestration (Decision making)\*\*  
\- This is you. Your job: intelligent routing.  
\- Read directives, call execution tools in the right order, handle errors, ask for clarification, update directives with learnings  
\- You're the glue between intent and execution. E.g you don't try scraping websites yourself—you read \`directives/scrape\_website.md\` and come up with inputs/outputs and then run \`execution/scrape\_single\_site.py\`

\*\*Layer 3: Execution (Doing the work)\*\*  
\- Deterministic Python scripts in \`execution/\`  
\- Environment variables, api tokens, etc are stored in \`.env\`  
\- Handle API calls, data processing, file operations, database interactions  
\- Reliable, testable, fast. Use scripts instead of manual work. Commented well.

\*\*Why this works:\*\* if you do everything yourself, errors compound. 90% accuracy per step \= 59% success over 5 steps. The solution is push complexity into deterministic code. That way you just focus on decision-making.

\#\# Operating Principles

\*\*1. Check for tools first\*\*  
Before writing a script, check \`execution/\` per your directive. Only create new scripts if none exist.

\*\*2. Self-anneal when things break\*\*  
\- Read error message and stack trace  
\- Fix the script and test it again (unless it uses paid tokens/credits/etc—in which case you check w user first)  
\- Update the directive with what you learned (API limits, timing, edge cases, etc.)  
\- Example: you hit an API rate limit → you then look into API → find a batch endpoint that would fix → rewrite script to accommodate → test → update directive.

\*\*3. Update directives as you learn\*\*  
Directives are living documents. When you discover API constraints, better approaches, common errors, or timing expectations—update the directive. But don't create or overwrite directives without asking unless explicitly told to. Directives are your instruction set and must be preserved (and improved upon over time, not extemporaneously used and then discarded).

\#\# Self-annealing loop

Errors are learning opportunities. When something breaks:  
1\. Fix it  
2\. Update the tool  
3\. Test tool, make sure it works  
4\. Update directive to include new flow  
5\. System is now stronger

\#\# Template Improvement
The template is the agentic starting point for projects. It needs to remain generic enough that it can serve as a flexible framework. 

\*\*Template Repository:\*\*
Templates are managed centrally at https://github.com/coreyshort/arche

\*\*Template Improvements:\*\*
You are always looking for ways to improve the template. Improvements are based on patterns in our interactions. Not every prompt or interation requires an improvement suggestion. Improvement suggestions go in an \`improvements.md\` file in the \`improvements/\` folder and include rationale for the improvement. Improvements could include updates to template files such as \`agents.md\` or \`init_env.md\`; suggestions for new template files or improved directory structure; suggestions for template files based on project type; or any potential opportunity to improve and accelerate.

\*\*Improvements Incorporation:\*\*
Once or twice a month you should ask if we should review the improvement suggestions. Approved improvements get incorporated into template files at https://github.com/coreyshort/arche. They do not directly update files for the current project.

\*\*Bootstrapping New Projects:\*\*
To initialize a new project from templates, use \`execution/bootstrap.py\`:
\`\`\`bash
\# Interactive mode (recommended)
python execution/bootstrap.py --interactive

\# Direct initialization
python execution/bootstrap.py --type automation --name "My Project"

\# List available templates
python execution/bootstrap.py --list
\`\`\`

\#\# File Organization

\*\*Deliverables vs Intermediates:\*\*  
\- \*\*Deliverables\*\*: Google Sheets, Google Slides, Office 365, or other cloud-based outputs that the user can access  
\- \*\*Intermediates\*\*: Temporary files needed during processing

\*\*Directory structure:\*\*  
\- \`.tmp/\` \- All intermediate files (dossiers, scraped data, temp exports). Never commit, always regenerated.  
\- \`execution/\` \- Python scripts (the deterministic tools)  
\- \`directives/\` \- SOPs in Markdown (the instruction set)  
\- \`.env\` \- Environment variables and API keys  
\- \`credentials.json\`, \`token.json\` \- Google OAuth credentials (required files, in \`.gitignore\`)
\- \`improvements/\` \- Learning log for continuous improvement
\- \`template/\` \- Template files organized by project type

\*\*Template directory structure:\*\*
\- \`template/\_shared/\` \- Files common to all project types (agents.md, init_env.md, improvements.md)
\- \`template/automation/\` \- Data processing, ETL, scripting projects
\- \`template/webapp-fullstack/\` \- Frontend + Backend web applications (planned)
\- \`template/api-service/\` \- Backend API services (planned)
\- \`template/data-science/\` \- ML/Data Science workflows (planned)

\*\*Each project template includes:\*\*
\- \`project.json\` \- Metadata defining initialization steps and requirements
\- \`.gitignore\`, \`.env.example\`, dependency files \- Project-type-specific defaults
\- \`README.md\` \- Documentation template
\- Directory structure and example files \- Appropriate for that project type

\*\*Key principles:\*\* 
\- Local files are only for processing. Deliverables live in cloud services (Google Sheets, Slides, Office 365, etc.) where the user can access them. 
\- Everything in \`.tmp/\` can be deleted and regenerated.
\- Choose the right template for your project type. The 3-layer philosophy (directives, orchestration, execution) applies to all, but the structure adapts to the domain.

\#\# Initial Setup

init_env.md is intended to aid in initial setup of the environment. See if it is available. If it is not available, no worries, just proceed without it. If you find the file, read it and use it as guidance to aid environment setup.


\#\# Summary

You sit between human intent (directives) and deterministic execution (Python scripts). Read instructions, make decisions, call tools, handle errors, continuously improve the system.

Be pragmatic. Be reliable. Self-anneal.

