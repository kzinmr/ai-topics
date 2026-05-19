---
title: "Linear Agent Code Intelligence"
type: concept
slug: linear-agent-code-intelligence
status: complete
tags: [linear, coding-agents, code-intelligence, developer-tooling, product-management, agent-skills]
created: 2026-05-15
updated: 2026-05-15
aliases: [Linear Code Intelligence, Code Intelligence for Linear Agent]
sources:
  - raw/articles/2026-05-14_linear_code-intelligence-linear-agent.md
  - https://linear.app/changelog/2026-05-14-code-intelligence
  - https://linear.app/docs/code-intelligence
---

# Linear Agent Code Intelligence

> **Definition:** Code Intelligence is a feature of [[entities/linear|Linear]] Agent that gives it controlled, read-only access to your codebase via the GitHub integration, enabling the agent to reason about how your product actually works — not just what's captured in issues, projects, and docs.

Launched May 14, 2026, Code Intelligence turns repositories into **shared product context** that the entire team can query through Linear Agent. It bridges the gap between "what's tracked in Linear" and "what the codebase actually does."

## What It Enables

| User | Use Case |
|------|----------|
| **PMs** | Write sharper specs informed by actual implementation constraints |
| **Support/Sales** | Answer technical questions without interrupting engineering |
| **Engineering** | Investigate bugs, regressions, and unfamiliar parts of the system faster |
| **Anyone** | Ask how a feature is implemented, why something behaves a certain way, what a change might affect |

## Adoption Metrics (Linear Internal)

| Month | Queries | Growth |
|-------|---------|--------|
| February 2026 | 1,055 | — |
| March 2026 | 2,681 | +154% |
| April 2026 | 4,267 | +59% |
| May 2026 (projected) | 5,200+ | +22% |

Each query represents a question someone would otherwise have asked a teammate or spent time investigating on their own — a direct reduction in **coordination tax**.

## Setup

1. Install the [GitHub integration](https://linear.app/docs/github) and enable code access
2. Turn on Code Intelligence in [AI Settings](https://linear.app/settings/ai/code-intelligence)
3. Choose which repositories to include
4. Configure access: limit to members with existing GitHub permissions, or open to the entire workspace

## Architecture

Code Intelligence operates as a **read-only codebase query layer** integrated into Linear Agent:

- **Repository integration**: Connects via GitHub integration; agent reads but does not modify code
- **Permission model**: Two-tier — GitHub-permission-gated or workspace-wide
- **Agent capability**: Linear Agent can explain implementations, trace feature logic, identify constraints
- **Query scope**: Codebase-aware reasoning, not just issue/project/doc context

## Availability

- **Public beta** for Business and Enterprise plans
- **Free** during the beta period
- Requires GitHub integration to be installed

## Strategic Significance

Code Intelligence represents a step toward **agent-native product development** — where the agent has access to the full context (code + issues + docs + plans) needed to reason about the product holistically. It reduces the **coordination tax** that grows with company size: as teams expand, answering "how does this work?" becomes increasingly expensive. Code Intelligence makes the codebase a self-serve resource.

## Related

- [[entities/linear]] — Linear, the project management and issue tracking platform
- [[entities/karri-saarinen]] — Karri Saarinen, Co-Founder & CEO of Linear
- [[concepts/agentic-loop]] — The canonical agent execution pattern
- [[concepts/coding-agents]] — The broader category of AI coding agents
- [[concepts/context-engineering]] — Managing agent context for effective reasoning

## References

- [Linear Changelog — Code Intelligence (May 14, 2026)](https://linear.app/changelog/2026-05-14-code-intelligence)
- [Linear Docs — Code Intelligence](https://linear.app/docs/code-intelligence)
- [[raw/articles/2026-05-14_linear_code-intelligence-linear-agent.md]] — Full changelog extraction
