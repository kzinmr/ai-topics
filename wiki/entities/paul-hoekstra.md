---
title: Paul Hoekstra
type: entity
created: 2026-05-02
updated: 2026-05-02
status: L2
tags:
  - person
  - data-engineer
  - agentic-engineering
  - claude-code
aliases:
  - paulhoekstra
sources:
  - https://paulhoekstra.substack.com/
  - raw/articles/2026-05-02_paul-hoekstra-agentic-engineering-part1-configuration-layer.md
  - raw/articles/2026-05-02_paul-hoekstra-agentic-engineering-part2-capability-layer.md
  - raw/articles/2026-05-02_paul-hoekstra-agentic-engineering-part3-orchestration-layer.md
  - raw/articles/2026-05-02_paul-hoekstra-agentic-engineering-part4-guardrails-layer.md
  - raw/articles/2026-05-02_paul-hoekstra-claude-code-statusline-aquarium.md
  - raw/articles/2026-05-02_paul-hoekstra-visual-output-claude-code.md
---

# Paul Hoekstra

**Paul Hoekstra** is a data engineer and author of the Substack publication **Paul's Pipeline** (launched April 2026). He writes about AI, data engineering, and side projects, with a focus on practical agentic engineering workflows using coding agents like Claude Code and Codex.

## Agentic Engineering Series (March–April 2026)

Hoekstra's signature contribution is a 4-part series defining the **Agentic Engineering Framework** — a systematic approach to configuring, equipping, orchestrating, and safeguarding AI coding agents.

### The Four Layers

1. **[[concepts/harness-engineering/agentic-engineering-configuration-layer|The Configuration Layer]]** — CLAUDE.md, Skills, pre-commit hooks. The foundational layer that prevents agents from defaulting to "defensive sludge."
2. **[[concepts/harness-engineering/agentic-engineering-capability-layer|The Capability Layer]]** — MCP tools, live documentation, visual output, persistent memory strategies.
3. **[[concepts/harness-engineering/agentic-engineering-orchestration-layer|The Orchestration Layer]]** — Subagents, Git worktrees, agent teams, context quality management.
4. **[[concepts/harness-engineering/agentic-engineering-guardrails-layer|The Guardrails Layer]]** — Permission systems, sandboxing, AST-grep, homoglyph attack prevention.

### Core Philosophy

> "Engineers who were already writing good code can now ship much more, much faster. Engineers who were writing dogwater before... well, they're mostly just writing lots more of that."

The difference between elite and mediocre agent results is the **Configuration Layer** — structured project-level instructions that override the model's default "sycophantic" behavior.

## Other Notable Articles

### Visual Output with Claude Code (April 2026)
Argues that Claude Design is a wrapper around capabilities Claude Code already has. Covers frontend-slides, Remotion, Figma MCP, and draw.io MCP for generating slides, video, UI designs, and architecture diagrams.

### Claude Code Statusline Customization (April 2026)
Shows how to transform the empty Claude Code statusline into a real-time dashboard for development metrics, ops monitoring, and personal productivity — including creative visualizations like a Doom HUD and aquarium.

## Key Contributions

- **Named the Configuration Layer problem** — identified that agents without structured project instructions default to low-quality "defensive sludge"
- **<HARD-GATE> enforcement pattern** — XML-like tags that Claude gives disproportionate weight to
- **Three-layer memory strategy** — MEMORY.md (project), episodic-memory (session), QMD (knowledge)
- **Context over Roles design principle** — read-heavy delegation as sweet spot for subagent orchestration

## Related Entities

- [[entities/simon-willison]] — Agentic Engineering patterns (precursor framework)
- [[concepts/harness-engineering/agentic-engineering]] — Main concept page

## Sources

- [Paul's Pipeline (Substack)](https://paulhoekstra.substack.com/)
- Various raw articles in `wiki/raw/articles/`
