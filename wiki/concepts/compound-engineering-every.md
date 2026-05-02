---
title: "Compound Engineering (Every Inc.)"
created: 2026-05-02
updated: 2026-05-02
type: concept
tags:
  - concept
  - agentic-engineering
  - harness-engineering
  - product-management
  - every-inc
aliases:
  - compound-engineering-every
  - every-compound-engineering
sources:
  - raw/articles/2026-05-02_guide-to-agent-native-product-management.md
---

# Compound Engineering (Every Inc.)

Compound Engineering is an AI-native software development philosophy created by [[entities/every-inc|Every Inc.]], primarily authored by [[entities/kieran-klaassen|Kieran Klaassen]]. The core insight: **each unit of engineering work should make subsequent units easier—not harder.**

This is distinct from [[concepts/compound-engineering-loop|Simon Willison's Compound Engineering Loop]], which focuses on the human-agent feedback cycle. Every's version is a complete engineering + product management philosophy with an installable plugin.

## Core Philosophy

> "Instead of features adding complexity and fragility, they teach the system new capabilities. Over time, the codebase becomes easier to understand, easier to modify, and easier to trust."

### Traditional vs. Compound Engineering

| Aspect | Traditional | Compound Engineering |
|--------|-------------|---------------------|
| Codebase trajectory | Accumulates technical debt | Accumulates AI knowledge |
| New features | Require negotiation with old code | Teach the system new capabilities |
| Bug fixes | One-time fix | Eliminate entire categories of future errors |
| Patterns | Remain ad-hoc | Become reusable tools |
| Team structure | Armies of engineers | Highly leveraged individuals |

## Implementation

Compound Engineering is operationalized through the **compound-engineering-plugin** (GitHub: `EveryInc/compound-engineering-plugin`, 7,000+ stars), an agent-agnostic plugin for Claude Code, Codex, and other coding agents.

### Available Skills

| Command | Purpose | Category |
|---------|---------|----------|
| `/ce-strategy` | Product strategy interviews (Rumelt framework) | Planning |
| `/ce-product-pulse` | Automated product health reports | Monitoring |
| `/ce-ideate` | Feature ideation | Planning |
| `/ce-plan` | Feature planning and ticket generation | Planning |
| `/ce-brainstorm` | Structured brainstorming | Planning |

### Adoption Scale (4 Stages)

1. **Stage 1:** Agents have file access + can run tests and git commits
2. **Stage 2:** Agents have browser + local logs + PR creation
3. **Stage 3:** Agents have production logs (read-only), error tracking, monitoring
4. **Stage 4:** Full agent-native workflow with all MCP-connected tools

## Evidence of Effectiveness

- Every runs 5 software products (Spiral, Cora, Sparkle, Monologue, Lex) with single-person engineering teams
- 7-figure revenue with ~15 total headcount
- Referenced by Will Larson (lethain.com) as a notable engineering innovation

## Relationship to [[concepts/compound-engineering-loop|Simon Willison's Loop]]

These are complementary concepts at different scales:

| Dimension | Every's Compound Engineering | Simon's Compound Engineering Loop |
|-----------|----------------------------|-----------------------------------|
| Scope | Entire engineering + PM philosophy | Code-level feedback cycle |
| Artifacts | Plugin, skills, strategy docs | Hoarded knowledge |
| Focus | Business outcomes, product strategy | Code quality, iterative improvement |
| Automation | Agent-managed planning + monitoring | Human-in-the-loop code review |

## Related Pages

- [[entities/every-inc]] — Company
- [[entities/kieran-klaassen]] — Creator
- [[entities/marcus-moretti]] — PM guide author
- [[concepts/agent-native-product-management]] — PM application
- [[concepts/compound-engineering-loop]] — Simon Willison's related concept
- [[concepts/harness-engineering]] — Related discipline
