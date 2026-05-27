---
title: "Compound Engineering Loop"
type: concept
aliases:
  - compound-loop
  - iterative-improvement-loop
created: 2026-04-13
updated: 2026-05-27
tags:
  - concept
  - agentic-engineering
  - person
status: complete
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/ai-should-help-us-produce-better-code/"
---

# Compound Engineering Loop

An iterative improvement cycle proposed by Simon Willison, involving collaboration between AI coding agents and human developers.

## Definition

> "I write some code, I review it, I improve it, I save what I've learned, and I repeat. Each cycle makes me more effective, and each cycle makes my agent more effective too."

## The Five Stages of the Loop

1. **Write**: Have the agent write code
2. **Review**: Human scrutinizes code, identifies issues
3. **Improve**: Request fixes from the agent, or modify it yourself
4. **Save**: Add what was learned to the "hoard" (accumulated knowledge)
5. **Repeat**: Start the next cycle with better context for the agent

## Why "Compound"

Each cycle acts as "interest" for the next. Accumulated knowledge (the hoard) improves the quality of context passed to the agent, resulting in exponential improvement in agent performance.

```
Cycle 1: Basic prompt → AI generates code → Human reviews → Learn X
Cycle 2: (Prompt + X) → AI generates better code → Human reviews → Learn Y
Cycle 3: (Prompt + X + Y) → AI generates even better code → ...
```

## Differences from Vibe Coding

| Feature | Vibe Coding | Compound Engineering |
|------|-------------|---------------------|
| Iteration | Considered complete in one pass | Continuous improvement cycle |
| Learning | Not accumulated | Added to hoard each cycle |
| Quality | OK if it superficially works | Human reviews and improves |
| Long-term | Cognitive debt accumulates | Knowledge grows compoundingly |

## Related Concepts
- [[concepts/harness-engineering/agentic-workflows/code-hoarding]] — Knowledge accumulation pattern
- [[concepts/agentic-engineering]] — Agentic Engineering overview
- [[concepts/harness-engineering/agentic-workflows/cognitive-debt]] — Cognitive debt (repaid via Compound Loop)
- [[concepts/compound-engineering-every]] — Every's Compound Engineering (business/PM perspective expansion)
