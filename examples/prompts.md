# Simple Prompts to Start with Arche

Copy-paste any of these to get started immediately.

## 1. Simplest Start (Use Existing Project)

```
Follow arche 3-layer mode: https://raw.githubusercontent.com/coreyshort/arche/main/modes/3-layer/INSTRUCTIONS.md
```

**Use when:** You have an existing project and want to add arche's 3-layer architecture.

---

## 2. Generate New Project (Specific Type)

```
Generate a new project using arche.
Reference: https://raw.githubusercontent.com/coreyshort/arche/main/modes/3-layer/INSTRUCTIONS.md
Project type: automation
Description: ETL pipeline that scrapes real estate listings and loads to Google Sheets
```

**Use when:** You know what type of project you want (automation, webapp, API, etc.).

**Replace** `Project type` with: automation, webapp-fullstack, webapp-frontend, api-service, data-science, cli-tool, or library.

---

## 3. Auto-Select Mode (AI Chooses)

```
Initialize an arche project for: Real-time stock trading alert system that monitors price movements and sends notifications

Use autonomous mode selection: https://raw.githubusercontent.com/coreyshort/arche/main/AUTONOMOUS_MODE_SELECTION.md
```

**Use when:** You're unsure which mode fits best. AI will analyze requirements and choose.

---

## 4. Specify Mode + Form

```
Generate a new project using arche.
Mode: 3-layer
Form: automation
Reference: https://raw.githubusercontent.com/coreyshort/arche/main/modes/3-layer/INSTRUCTIONS.md

Description: Daily email digest summarizing Hacker News top stories
```

**Use when:** You know exactly what architectural pattern and project type you need.

---

## 5. Explore and Learn

```
Explain the arche framework to me.
Reference: https://raw.githubusercontent.com/coreyshort/arche/main/README.md

Show me the available modes and when to use each.
```

**Use when:** You want to understand arche before starting.

---

## 6. Add to Existing Complex Project

```
I have an existing project at [path/to/project].
Add arche 3-layer architecture to organize the codebase.
Reference: https://raw.githubusercontent.com/coreyshort/arche/main/modes/3-layer/INSTRUCTIONS.md

Analyze the current structure and propose how to refactor it into:
- directives/ (what to do)
- execution/ (deterministic scripts)
- orchestration (AI decision-making)
```

**Use when:** Refactoring an existing project to use arche patterns.

---

## Tips

**Model-Agnostic:** All these prompts work with Claude, ChatGPT, GitHub Copilot, Gemini, or any AI assistant.

**URLs are Key:** The AI reads the URL content and follows those instructions. No local files needed to start.

**Customize:** Add your specific requirements after the prompt. The AI will adapt.

**Iteration:** If the first result isn't perfect, refine your description and try again. The AI learns from your feedback.
