---
title: Superpowers
type: entity
aliases: [superpowers-framework]
created: 2026-06-05
updated: 2026-06-05
status: L2
tags:
  - agent-skills
  - ai-agents
  - framework
  - agent-harness
  - agent-skills
  - agent-design-patterns
  - open-source
sources:
  - raw/articles/2026-05-27_hugobowne_the-agentic-software-factory.md
  - raw/articles/2026-05-08_vanishing-gradients_show-us-your-agent-skills-ep1.md
  - https://hugobowne.substack.com/p/the-agentic-software-factory
  - https://github.com/obra/superpowers
---

# Superpowers

**Agent skills framework created by Jesse Vincent ([@obra](https://github.com/obra)).** Superpowers provides a structured approach to defining agent behaviors through progressive disclosure, detailed spec interviews, and sub-agent execution. Used prominently by [[entities/wes-mckinney|Wes McKinney]] as the foundation of his agentic software factory.

## Overview

| | |
|---|---|
| **GitHub** | [obra/superpowers](https://github.com/obra/superpowers) |
| **Creator** | Jesse Vincent ([@obra](https://github.com/obra)) |
| **Type** | Agent skills framework |
| **Users** | Wes McKinney, and growing community |

## Core Design

### Progressive Disclosure

Skills reveal complexity only when needed. A skill has two visible fields (name + description) that are always in the agent's context. The full body is hidden until the agent invokes the skill.

### Thin Drivers

Minimal wrappers that call tools, not fat abstractions. The harness should be minimal; skills encode specific behaviors and judgments.

### Spec Interview

Superpowers runs a **long, detailed spec interview** before any code is written. The agent asks questions about scope, constraints, and architecture. The human answers and shapes the plan, then hands off to a sub-agent execution skill.

> *"One of the pros and cons of Superpowers is it generates amazing software, but it also takes a long time to generate very detailed implementation plans. The idea is that it doesn't really trust leaving that much up to the agent in terms of making decisions."* — Wes McKinney

## McKinney's Usage

McKinney has used Superpowers to run **parallel spec interviews** across multiple git worktrees:

- **Single plan for 14 hours straight** with 45 tasks
- **4-5 projects in flight** simultaneously
- Spec interviews run in parallel while implementation grinds unattended

The structure makes parallel projects possible: a slow plan is something you can step into and out of while it's being formed, and a long implementation runs unattended.

### The Workflow

1. **Spec interview** — Answer agent's questions about scope and constraints
2. **Leave it planning** — Agent continues planning while you work on other things
3. **Implementation** — Sub-agent grinds for hours; you don't watch
4. **Ready to merge** — Check dashboard, fold RoboRev findings, merge what's clean

## Quote

> *"The difference between vibe coding and agentic engineering is planning, architecture, and caring about the output."* — Jesse Vincent, as quoted by Wes McKinney

## Related

- [[entities/wes-mckinney]] — Primary user
- [[entities/roborev]] — Review layer that validates Superpowers output
- [[concepts/agentic-engineering]] — The discipline Superpowers enables

## References

- [GitHub: obra/superpowers](https://github.com/obra/superpowers)
- [The Agentic Software Factory](https://hugobowne.substack.com/p/the-agentic-software-factory) (Vanishing Gradients, May 2026)

## Log

- **2026-06-05**: Initial entity page created.
