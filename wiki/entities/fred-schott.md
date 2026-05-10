---
title: "Fred K. Schott (@FredKSchott)"
type: entity
handle: "@FredKSchott"
created: 2026-05-10
updated: 2026-05-10
tags:
  - person
  - agent-harness
  - coding-agents
  - open-source
aliases:
  - "fred-schott"
  - "Fred Schott"
  - "FredKSchott"
sources:
  - "https://x.com/FredKSchott"
  - "https://github.com/fredkschott"
  - "https://x.com/FredKSchott/status/2050274923852210397"
  - "raw/articles/2026-05-09_addyosmani-agent-harness-engineering.md"
related:
  - "[[concepts/agent-harness]]"
  - "[[entities/addy-osmani]]"
  - "[[entities/vtrivedy10]]"
---

# Fred K. Schott (@FredKSchott)

| | |
|---|---|
| **X** | [@FredKSchott](https://x.com/FredKSchott) |
| **GitHub** | [fredkschott](https://github.com/fredkschott) |
| **Role** | Creator of **Astro** (web framework) and **Flue** (agent harness framework) |
| **Known for** | Building foundational developer infrastructure — from static site generators to agent harnesses |

## Bio

Fred K. Schott is a developer tools creator best known as the co-creator of **Astro**, the modern web framework (islands architecture, zero-JS by default). In May 2026, he launched **Flue** — the first dedicated **agent harness framework** for TypeScript.

Schott identifies as "CEO of HTML" — a playful nod to his focus on building practical, developer-first infrastructure that abstracts away complexity.

## Flue: The Agent Harness Framework

Flue is a TypeScript-native agent harness framework released in May 2026. Its key design principles:

| Principle | Implementation |
|-----------|---------------|
| **100% headless, programmable** | No TUI/GUI assumptions — deploy anywhere |
| **Markdown-driven logic** | Skills, roles, and AGENTS.md define agent behavior |
| **Built-in harness** | Sessions, sub-agents, sandboxing, loop orchestration shipped OOTB |
| **Zero-config sandboxing** | Isolated execution without manual setup |
| **Node.js, Cloudflare, GitHub Actions** | Deploy on multiple runtimes |

Flue was the first framework to frame itself explicitly as an **agent harness framework** rather than an AI SDK or chat wrapper. As Addy Osmani noted, "Flue... was apparently inspired by an earlier version of [the Agent Harness Engineering] post."

**Python port**: PyFlue, created by Shashikant Jagtap, brings the same Markdown-skills, persistent sessions, sandboxed FS/shell, and pluggable backends (DeepAgents, OpenAI Agents SDK, Google ADK, PydanticAI) to Python.

Flue was featured by Render for one-click deployment.

## Core Ideas

### Harness-as-a-Service (HaaS)

Flue embodies the HaaS paradigm: instead of wiring agent loops, context management, and sandboxes from scratch, developers select Flue, configure skills/prompts/hooks, and focus purely on domain logic.

### Agent = Model + Harness

Schott's framing aligns perfectly with Vivek Trivedy's definition. Flue explicitly separates the model (interchangeable, via any provider) from the harness (Flue's runtime).

## Related

- [[entities/addy-osmani]] — Cited Flue as a HaaS exemplar in "Agent Harness Engineering"
- [[entities/vtrivedy10]] — Coined "Agent = Model + Harness"
- [[concepts/agent-harness]] — Comprehensive harness architecture reference
- [[concepts/why-harness-development-boom]] — Structural forces driving harness development
