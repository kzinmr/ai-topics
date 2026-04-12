---
title: "Walden Yan"
status: draft
type: entity
tags: [cognition, devin, engineer, multi-agents]
related: [cognition-devin-philosophy, dont-build-multi-agents]
sources:
  - https://cognition.ai/blog/dont-build-multi-agents
  - https://x.com/walden_yan/status/2025936695661826481
---

# Walden Yan — Cognition Engineer

Engineer at Cognition Labs, author of "Don't Build Multi-Agents" — a foundational critique of traditional multi-agent architectures.

## Core Philosophy

> "I think the most important insight from Cognition is that **context continuity beats parallelism**." — Walden Yan

### Don't Build Multi-Agents

Walden's position on agent architecture:

- **Single-threaded agents with context continuity outperform parallel multi-agent systems**
- Handoffs between agents lose critical context — "the devil is in the details"
- A single agent with a long context window that can maintain its own thread of thought is more reliable than multiple specialized agents
- **Context continuity** > **parallelism** for most coding tasks

### The Context Continuity Argument

Walden argues that:

1. Multi-agent systems suffer from context loss during handoffs
2. Each agent has to rebuild understanding from scratch
3. A single agent maintains implicit knowledge across the session
4. The cost of coordination often exceeds the benefit of parallelism

> "When you hand off work between agents, you're not just passing context — you're passing responsibility. And responsibility doesn't serialize well."

## See Also

- [[concepts/cognition-devin-philosophy]] — Cognition's core philosophy
- [[entities/scott-wu]] — Cognition CEO
- [[entities/nader-dabit]] — Cognition Growth Engineer
