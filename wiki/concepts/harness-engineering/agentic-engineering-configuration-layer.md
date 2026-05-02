---
title: "Agentic Engineering — Configuration Layer"
type: concept
slug: agentic-engineering-configuration-layer
created: 2026-05-02
updated: 2026-05-02
status: complete
tags:
  - concept
  - harness-engineering
  - agentic-engineering
  - claude-code
  - coding-agents
aliases:
  - configuration-layer
  - CLAUDE.md-patterns
sources:
  - https://paulhoekstra.substack.com/p/agentic-engineering-the-configuration
  - raw/articles/2026-05-02_paul-hoekstra-agentic-engineering-part1-configuration-layer.md
---

# Agentic Engineering: The Configuration Layer

> The foundational layer of agentic engineering — structured project-level instructions that bridge the gap between mediocre and elite results from coding agents.

Part of [[concepts/harness-engineering/agentic-engineering]] (4-layer framework by [[entities/paul-hoekstra|Paul Hoekstra]]). Defined in contrast to "vibe coding" where agents default to sycophantic, low-quality code without proper configuration.

## Core Principles

### CLAUDE.md as Behavioral Baseline
- Acts as `.editorconfig` for agent behavior — a Markdown file at project root
- Read automatically at session start; sent with every tool call/retry
- Prompt caching reduces cost of stable prefix to ~10% of normal prices
- **Keep it short** — every token competes for attention (context rot)

### <HARD-GATE> Enforcement
XML-like tags that Claude gives disproportionate weight to:
```markdown
<HARD-GATE>
Do NOT write any code until you have presented a design and the user has approved it.
</HARD-GATE>
```

### Skills System
- Task-specific Markdown files in `.claude/skills/`
- Loaded on demand to prevent context rot
- **SkillsBench finding:** Claude Haiku + human-curated skills (27.7%) > Opus without skills (22.0%)
- Human-curated > AI-generated instructions (AI-generated often degrades performance)

### Division of Labor Strategy
| File | Scope | Purpose |
|------|-------|---------|
| CLAUDE.md | Always-relevant | Project rules (linting, file limits) |
| Skills | Task-specific | Procedures (TDD, debugging) |
| Live Prompt | Current task | Unique details for this interaction |

### Anti-Rationalization Tables
List excuses the model might use to skip steps, with corrections — pre-emptive countermeasures against agent "rationalization."

## Recommended Snippets

```markdown
## Hard Limits
- Functions: <= 100 lines
- Cyclomatic complexity: <= 8
- Positional parameters: <= 5

## Python Tooling
- Package manager: uv
- Linting + formatting: ruff
- Run commands: Always uv run <tool>

## Behavioral Rules
- NEVER create files unless absolutely necessary
- ALWAYS read a file before editing it
- NEVER commit secrets, credentials, or .env files
```

## Related Workflow Frameworks

- [superpowers](https://github.com/obra/superpowers) — TDD/debugging/verification plugin
- [Get Shit Done](https://github.com/gsd-build/get-shit-done) — slash commands + meta-prompting
- [Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin) — Plan → Work → Review → Compound

## Graph Structure

```
[agentic-engineering-configuration-layer]
  ──part-of──→ [concept: agentic-engineering]
  ──author──→ [entity: paul-hoekstra]
  ──relates-to──→ [concept: harness-engineering]
  ──contrasts──→ [vibe-coding]
```

## Related Concepts
- [[concepts/harness-engineering/agentic-engineering]] — Parent framework
- [[entities/paul-hoekstra]] — Author
- [[concepts/harness-engineering]] — Umbrella philosophy

## Sources
- [Agentic Engineering, Part 1: The Configuration Layer](https://paulhoekstra.substack.com/p/agentic-engineering-the-configuration)
