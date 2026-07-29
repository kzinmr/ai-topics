---
title: Burke Holland
type: entity
created: 2026-07-29
updated: 2026-07-29
tags:
  - person
  - developer-tooling
  - github-copilot
  - microsoft
  - agentic-engineering
  - harness-engineering
  - educator
  - blogger
aliases:
  - "@burkeholland"
  - burkeholland
sources:
  - raw/articles/2026-07-28_burkeholland_the-harness-is-all-you-need-mostly.md
  - https://x.com/burkeholland
  - https://burkeholland.github.io/
---

# Burke Holland

**Burke Holland** (`@burkeholland`) is a developer advocate and engineer at GitHub (Microsoft), focused on practical AI-assisted software development with GitHub Copilot. He is a leading voice in agent harness literacy — the philosophy that understanding your agent harness deeply matters more than chasing every new AI tool, MCP, or skill.

## Overview

Burke Holland works at the intersection of developer tooling and AI agents, with a focus on making GitHub Copilot accessible and productive for everyday developers. His writing and talks emphasize practical, repeatable workflows over complex agent configurations. He is the creator of **Postrboard**, a CSS framework designed to give AI agents design guidance.

His core thesis — "the harness is all you need (mostly)" — argues that deep harness literacy (understanding `[[entities/copilot-cli|GitHub Copilot CLI]]`, plan mode, Autopilot, Rubber Duck review) yields more consistent productivity gains than constantly adopting new MCP servers, skills, or custom agent configurations.

## Core Ideas

### Harness-First Philosophy

Holland advocates for mastering the agent harness before adding complexity:

- **Learn the harness once, use it everywhere** — GitHub Copilot's harness is consistent across CLI, app, VS Code, Visual Studio, and JetBrains. Surface details differ but the core workflow is portable.
- **Less is way more** — The most impactful productivity gains come from how you use the harness, not from what you install or configure.
- **Start simple** — The CLI (terminal interface) is the recommended starting point for learning because it's stripped down to text interaction with no UI overhead.
- **Slop awareness** — Skills and MCP registries are filled with non-functional generated content. Verify before adopting.

### The 8-Step Copilot Workflow

Holland's signature contribution is an 8-step practical workflow for GitHub Copilot:

1. **Pick a tool** — Any Copilot surface (CLI, app, VS Code). The harness is consistent across them.
2. **Turn on YOLO mode** (`/allow-all`) — Agents need autonomy for productivity. Run in sandboxes (Codespaces, dev containers) for safety.
3. **Start with a prototype** — "Give me 20 mocks" before implementation. Visual prototyping surfaces requirements you wouldn't think of. Works for non-visual tasks too (Mermaid diagrams for API designs).
4. **Plan methodically** — Use `/plan` mode. The model asks edge-case questions you can't anticipate. Install the `grill-me` skill from Matt Pocock for aggressive questioning.
5. **Implement with Autopilot** — Built-in loop that ensures the agent completes every plan item. Automatic subagent orchestration (Explore for reading, General Purpose for complex work).
6. **Human review and iteration** — Be conversational, don't overthink prompts. Be ruthless about quality. "Knowing what a quality result is from something that isn't is the value that you bring."
7. **Rubber duck the result** — Cross-model review (different AI family). Can be combined with Autopilot for iterative improvement loops.
8. **Profit** — Stage, commit, move on. Start a new chat session for unrelated topics.

### Model & Cost Advice
- Use **medium-sized models** (GPT 5.6 Terra, Claude Sonnet) on medium reasoning for most work
- **Stick with one model** per feature/bug — prompt caching saves tokens across sessions
- Rubber Duck + Autopilot loops cost more tokens but are "an investment in your future self"

## Projects

- **Postrboard** — A CSS framework designed for AI agent use, providing design guidance as a skill ([burkeholland.github.io/postrboard-design](https://burkeholland.github.io/postrboard-design))

## Writing & Speaking

### Notable Articles
- **"The harness is all you need (mostly)"** (July 2026) — X Article presenting the 8-step Copilot workflow. Emphasizes harness literacy over tool chasing. [[raw/articles/2026-07-28_burkeholland_the-harness-is-all-you-need-mostly.md|Raw article]]

## Cross-References

- [[entities/copilot-cli]] — GitHub Copilot CLI, the harness Holland recommends as a starting point
- [[concepts/github-copilot-agent-platform]] — The broader platform Holland's workflow operates within
- [[concepts/agentic-engineering]] — Holland's workflow embodies agentic engineering principles (verification, iteration, human taste)
- [[concepts/harness-engineering]] — The umbrella philosophy; Holland is a practitioner advocate
- [[entities/simon-willison]] — Fellow advocate for practical, harness-focused agentic engineering
- [[entities/ryan-lopopolo]] — Harness engineering theorist; Holland provides the practitioner complement

## References

- `raw/articles/2026-07-28_burkeholland_the-harness-is-all-you-need-mostly.md` — X Article: "The harness is all you need (mostly)"
