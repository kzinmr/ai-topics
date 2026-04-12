---
title: "Hamel Husain"
created: 2026-04-12
tags: [person, ai-engineering, evaluation, open-source, mcp]
sources:
  - "https://hamel.dev"
  - "https://open.substack.com/pub/lenny/p/why-ai-evals-are-the-hottest-new-skill"
  - "https://github.com/hamelsmu/evals-skills"
---

# Hamel Husain

AI engineer, educator, and consultant focused on practical AI evaluation and development methodologies. Known for his extensive writing on AI evals, LLM-as-Judge, and Harness Engineering.

## Background

- AI engineering consultant who has worked with **50+ companies** and taught **4,000+ students**
- Author of one of the most comprehensive practical guides to AI evaluation
- Creates open-source tools for the AI engineering community
- Regular speaker and newsletter author on AI engineering best practices

## Core Ideas

### AI Evaluation Philosophy
- **"Process first, tools second"** — evaluation is about methodology, not platforms
- **Binary over Likert** — pass/fail judgments are more actionable than 1-5 scales
- **Error analysis > metrics** — bottom-up examination of failures beats top-down metric tracking
- **60-80% of dev time** should be spent on error analysis and evaluation
- **"When everything is important, nothing is"** — generic metrics create false confidence

### Critique Shadowing Methodology
A 7-step iterative process for building aligned LLM-as-Judge evaluators:
1. Find the Principal Domain Expert
2. Create a Dataset (features × scenarios × personas)
3. Domain Expert Reviews Data (pass/fail + detailed critiques)
4. Fix Errors
5. Build LLM Judge Iteratively (using expert examples as few-shot)
6. Perform Error Analysis (classify by root cause)
7. Create Specialized Judges (if needed)

Key insight: "The real value is looking at your data. Creating an LLM judge is a nice 'hack' to trick people into carefully examining their data."

### Evals Skills for Coding Agents
Published [evals-skills](https://github.com/hamelsmu/evals-skills) — a plugin set for AI coding agents to perform evaluations:
- eval-audit, error-analysis, generate-synthetic-data, write-judge-prompt, validate-evaluator, evaluate-rag, build-review-interface
- Connects to Harness Engineering philosophy: "Documentation tells the agent what to do. Telemetry tells it whether it worked. Evals tell it whether the output is good."

### Synthetic Data Strategy
- Generate inputs, not outputs — prevents inheriting model biases
- Define dimensions (Features, Scenarios, Personas), create 20 tuples manually, then scale with LLM
- Two-step generation: (a) LLM generates structured tuples, (b) separate prompt converts to natural language

### Tool Selection Framework
Evaluated LangSmith, Braintrust, Arize Phoenix, and Inspect AI in a panel discussion:
- No single "best" tool exists
- Prioritize human review capabilities over automated scoring
- Demand clean data export — avoid proprietary lock-in
- Test the "trace → experiment → annotate" loop for friction before committing

## Key Works

| Title | Type | Date | URL |
|-------|------|------|-----|
| Your AI Product Needs Evals | Blog Post | 2024 | https://hamel.dev/blog/posts/evals/ |
| Using LLM-as-a-Judge For Evaluation: A Complete Guide | Blog Post | Oct 2024 | https://hamel.dev/blog/posts/llm-judge/ |
| LLM Evals: Everything You Need to Know | Blog Post | 2025 | https://hamel.dev/blog/posts/evals-faq/ |
| Selecting The Right AI Evals Tool | Blog Post | 2025 | https://hamel.dev/blog/posts/eval-tools/ |
| Evals Skills for Coding Agents | Blog Post + OSS | 2025 | https://hamel.dev/blog/posts/evals-skills/ |
| A Field Guide to Rapidly Improving AI Products | Blog Post | 2025 | https://hamel.dev/blog/posts/field-guide/ |
| Inspect AI (OSS Library) | Open Source | 2025 | https://hamel.dev/notes/llm/evals/inspect.html |
| evals-skills (GitHub) | Open Source | 2025 | https://github.com/hamelsmu/evals-skills |
| Why AI Evals Are the Hottest New Skill | Lenny's Podcast | 2025 | https://open.substack.com/pub/lenny/p/why-ai-evals-are-the-hottest-new-skill |

## Related Entities

- [[ai-evals]] — Main evaluation framework
- [[critique-shadowing]] — His signature methodology
- [[harness-engineering]] — Connected philosophy
- [[llm-as-judge]] — Core evaluation technique
- [[error-analysis]] — Foundational practice
- [[eval-tools-comparison]] — Tool comparison framework
- [[evals-skills]] — Coding agent skills
