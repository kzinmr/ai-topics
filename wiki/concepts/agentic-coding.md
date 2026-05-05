---
title: "Agentic Coding"
type: concept
aliases:
  - agentic-coding
  - spec-driven-development
created: 2026-04-25
updated: 2026-05-05
tags:
  - concept
  - coding-agents
  - software-development
  - workflow
  - testing
sources:
  - raw/articles/2026-05-04_drew-breunig-10-lessons-agentic-coding.md
  - https://www.dbreunig.com/2026/05/04/10-lessons-for-agentic-coding.html
related:
  - speculative-decoding
  - harness-engineering
  - ai-agent-engineering
---

# Agentic Coding

**Agentic Coding** is the practice of developing software with AI coding agents, where code generation is cheap and the human role shifts from writing syntax to defining intent, designing architecture, writing tests, and exercising taste.

> "Agentic code is 'free as in puppies.' Support isn't cheap and neither is security." — Drew Breunig

## Core Principles (Drew Breunig's 10 Lessons)

### The Spec-Driven Development Triangle
Agentic coding is organized around three living documents:

1. **The Spec** — The evolving plan and intent. Constantly updated as implementation reveals new insights.
2. **The Code** — The cheap, replaceable implementation. Forked, rebuilt, and discarded freely.
3. **The Tests** — The durable behavioral contract. End-to-end tests validate product functions (the *what*), not implementation details (the *how*).

### Key Workflow Patterns

| # | Lesson | Core Insight |
|---|--------|-------------|
| 1 | **Implement to Learn** | Use low-cost agentic coding to surface hidden design decisions and refine specs. |
| 2 | **Rebuild Often** | Fork and recode experiments frequently — reconnaissance was previously too expensive. |
| 3 | **Invest in E2E Tests** | Behavioral contracts provide the safety net for frequent rebuilding from scratch. |
| 4 | **Document Intent** | Code shows *method*, tests show *goal*, but neither captures the **why**. |
| 5 | **Keep Specs in Sync** | Living specs enable accurate agent context and easier rebuilds. |
| 6 | **Find the Hard Stuff** | Value is in intuitive design, performance, security, resilience, and architecture — not boilerplate. |
| 7 | **Automate the Easy Stuff** | Build loops, distill skills, automate code review. But avoid the "Mystery House" trap. |
| 8 | **Develop Your Taste** | Internal taste is the only feedback loop fast enough to keep up with agent output. |
| 9 | **Agents Amplify Experience** | Technical expertise is a force multiplier — terminology and framing save countless cycles. |
| 10 | **Mind the Hidden Costs** | Maintenance, support, and security costs persist even when code creation is nearly free. |

## The Value Shift

With frontier models making code generation cheap, value migrates from *syntax labor* to:

- **Strategic intent** — what should be built and why
- **Architectural taste** — how systems should be structured
- **Testing rigor** — behavioral contracts that survive rebuilds
- **Domain expertise** — the intuition that separates effective prompts from vague ones

> "Talented developers underestimate how much intuition they bring to their prompts... Pair technical expertise coupled with great taste for an unbeatable advantage."

## Relationship to Other Concepts

```
[agentic-coding] ──author──→ [[drew-breunig|Drew Breunig]]
[agentic-coding] ──extends──→ [[harness-engineering]]
[agentic-coding] ──contrasts──→ traditional-software-development
[agentic-coding] ──teaches──→ spec-driven-development
```

Agentic coding can be seen as the human-side practice layer of [[harness-engineering]] — where "Agent = Model + Harness" meets the developer's workflow, taste, and testing discipline.

## Graph Structure Query

This section informs graph queries: authored by [[drew-breunig|Drew Breunig]], extends [[harness-engineering]], teaches spec-driven development methodology.

## Related Concepts

- [[harness-engineering]] — The umbrella philosophy: Agent = Model + Harness
- [[ai-agent-engineering]] — System-side build patterns for agent construction
- [[speculative-decoding]] — Inference optimization that makes coding agents faster
- [[drew-breunig]] — Author of the 10 Lessons framework

## Sources

- [10 Lessons for Agentic Coding](https://www.dbreunig.com/2026/05/04/10-lessons-for-agentic-coding.html) — Drew Breunig, May 4, 2026
- [Raw article](raw/articles/2026-05-04_drew-breunig-10-lessons-agentic-coding.md)
