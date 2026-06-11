---
title: Simon Last
type: entity
created: 2026-05-20
updated: 2026-05-20
tags:
  - person
  - product-management
  - ai-agents
  - developer-tooling
aliases:
  - Simon Last
  - @simonlast
sources:
  - raw/articles/substack.com--redirect-2-eyjlijoiahr0chm6ly9vcgvulnn1ynn0ywnrlmnvbs9wdwivc--c27d9b81.md
  - https://www.linkedin.com/in/simon-last-41404140
  - https://x.com/simonlast
related:
  - entities/notion
  - concepts/agent-harness
  - concepts/dark-factory-software-factory
  - concepts/notion-cli
---

# Simon Last

**Simon Last** (LinkedIn: [simon-last](https://www.linkedin.com/in/simon-last-41404140), X: [@simonlast](https://x.com/simonlast)) is a product and engineering leader at **[[entities/notion|Notion]]**, where he has been instrumental in building Notion's Custom Agents and agent harness architecture. He is known for the "Simon Vortex" — a rapid prototyping mode that drives high-velocity AI engineering at Notion.

## Overview

Last has been building agent capabilities at Notion since early 2022, starting with experiments using GPT-4 and early tool-calling frameworks. He has overseen **four to five complete rebuilds** of Notion's agent harness, evolving from custom XML to tool definitions with progressive disclosure. His philosophy emphasizes building for where models are going, not just where they are today.

## Core Topics

### Agent Harness Architecture

Led the evolution of Notion's agent harness through five iterations:
1. **Early JavaScript coding agents** (2022) — initial experiments with GPT-4, too fragile
2. **Custom XML** — structured but overly complex
3. **Markdown and SQL-like abstractions** — simpler, more maintainable
4. **Tool definitions with progressive disclosure** — current approach
5. **Shortened system prompt** — reduced complexity exposed to the model

> "We designed our own tool calling framework and tried to fine-tune models to use it over multiple turns. The models were just too dumb and the context window was way too short."

### Software Factory Vision

Last is a strong advocate for the **software factory** concept — automated workflows where agents spec, code, test, debug, review, and maintain codebases together. He sees coding agents as "the kernel of AGI" and believes the future involves agents composing with other agents in shared workspaces.

### "Simon Vortex" Prototyping

At Notion, the "Simon Vortex" refers to a rapid prototyping culture where:
- Velocity is super high
- Direction changes daily
- Senior engineers swarm on problems
- Management boundaries are loose
- It's the equivalent of an SK Works lab for AI features

### Product Philosophy

- **"Demos over memos"** — prototypes must be working feature flags, not mockups
- **Build for agents first** — "the majority of our traffic will be coming from agents using our interface, not humans"
- **Focus on user journeys, not cool tools** — the failure mode is building "cool tools" without clear user value
- **Balance GI-pilled thinking with shipping** — work on future capabilities while maintaining useful current products

## Notion CLI Advocacy

Last is bullish on **CLI over MCP** for agent interfaces:
- CLI is self-debugging and more transparent
- MCP makes sense for standardized tool access, but CLI offers better developer experience
- The `ntn` CLI was designed with both human and agent users in mind

## Career at Notion

| Period | Role | Key Achievement |
|--------|------|----------------|
| 2022 | Early AI experiments | First tool-calling experiments with GPT-4 |
| 2023 | Agent harness v1-v3 | Multiple rebuilds as model capabilities evolved |
| 2024 | Custom Agents development | Shipped Notion's AI features (Q&A, unified AI) |
| 2025 | Meeting Notes | Launched high-signal data capture feature |
| 2026 | Custom Agents launch | Final production release after 4-5 rebuilds |

## Cross-References

- **[[entities/notion]]** — Current employer, leads AI product/engineering
- **[[entities/sarah-sachs]]** — Close collaborator, manages AI engineering team
- **[[concepts/dark-factory-software-factory]]** — Advocates for automated software factories
- **[[concepts/harness-engineering/agent-harness]]** — Built Notion's agent harness through multiple iterations
- **[[concepts/notion-cli]]** — Championed CLI-first agent interfaces

## Sources

- [Latent Space Podcast: Notion's Token Town — Simon Last & Sarah Sachs](raw/articles/substack.com--redirect-2-eyjlijoiahr0chm6ly9vcgvulnn1ynn0ywnrlmnvbs9wdwivc--c27d9b81.md) — April 2026 podcast transcript
- [LinkedIn](https://www.linkedin.com/in/simon-last-41404140)
- [X/Twitter](https://x.com/simonlast)
