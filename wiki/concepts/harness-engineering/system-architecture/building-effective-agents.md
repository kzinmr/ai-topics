---
title: "Building Effective Agents"
type: concept
aliases:
  - building-effective-agents
  - agent-design-patterns
created: 2026-04-12
updated: 2026-05-26
tags:
  - concept
  - architecture
  - harness-engineering
  - anthropic
status: active
related:
  - "[[concepts/building-effective-agents]]"
  - "[[concepts/harness-engineering]]"
  - "[[concepts/context-engineering|Context Engineering]]"
  - "[[concepts/harness-engineering/system-architecture/evals-for-ai-agents]]"
  - "[[concepts/coding-agents/minimal-coding-agent]]"
sources:
  - "https://www.anthropic.com/engineering/building-effective-agents/"
  - "https://simonwillison.net/2024/Dec/20/building-effective-agents/"
  - "[[raw/articles/2024-12-20_simon-willison_building-effective-agents]]"
---

# Building Effective Agents

> **Canonical page promoted.** This subdirectory page was promoted to [[concepts/building-effective-agents]] for broader discoverability. Key content retained below; see the canonical page for the comprehensive reference.

Practical guidelines for building LLM agents, derived from Anthropic collaboration with dozens of teams.

## Core Philosophy

> "Consistently, the most successful implementations use simple, composable patterns rather than complex frameworks."

> "Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs."

**The most successful implementations use simple, composable patterns rather than complex frameworks.**

## Three Core Principles

1. **Maintain simplicity in your agent's design** — Keep agent design simple
2. **Prioritize transparency by explicitly showing the agent's planning steps** — Explicitly display planning steps
3. **Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing** — Thoroughly document and test tools

## Workflows vs Agents

| Dimension | Workflow | Agent |
|------|-------------|-------------|
| Control | LLMs and tools orchestrated via predefined code paths | Model autonomously controls tool use and decision-making |
| Application | Best for well-defined tasks | Best when flexibility and model-driven decisions are needed |
| Characteristics | Predictability, consistency | Open-ended problems, iteration based on environment feedback |

## Building Blocks

### Augmented LLM
An LLM augmented with retrieval, tools, and memory. The fundamental building block of agent systems.

### Prompt Chaining
Decompose a task into sequential steps. Each LLM call processes the output of the previous step.

### Routing
Route tasks to specialized downstream processes based on input classification.

### Parallelization
Execute multiple LLM calls simultaneously and aggregate results.

### Orchestrator-Workers
A central LLM dynamically decomposes tasks and distributes them to worker LLMs for execution.

### Evaluator-Optimizer
An iterative loop between a generating LLM and an evaluating LLM. The evaluator judges quality, the generator improves.

## Agent Implementation Patterns

Agents are inherently simple: **an LLM loop that uses tools based on environment feedback**.

```
command → plan → tool call → environment feedback → iterate → result
```

Key implementation details:
- Getting ground truth from the environment at each step is essential
- Human feedback can be requested at checkpoints or blockers
- Control is maintained through iteration limits

## Framework Pitfalls

> "Frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. But they often create extra layers of abstraction that can obscure the underlying mechanics."

**Advice for developers**: Start by using LLM APIs directly. Many patterns can be implemented in just a few lines of code.

## When to Use Agents

- Open-ended problems where it is difficult or impossible to predict the required steps in advance
- Multiple execution paths where environment feedback determines the next action
- Tasks requiring many steps or branching, which rigid workflows handle poorly

## Simon Willison's Annotations (2024-12-20)

[[entities/simon-willison|Simon Willison]] described this article as "the clearest practical guide to building LLM agents I have seen."
Key insights from his blog post ([[raw/articles/2024-12-20_simon-willison_building-effective-agents]]):

### Praise for Terminology

Willison highly praised Anthropic's terminology definitions:

- The framing of **"agentic systems"** as a parent category
- The clear distinction between **"workflows"** and **"agents"** — workflows orchestrate LLMs with predefined patterns, agents autonomously control processes and tool use
- **"augmented LLM"** — an LLM augmented with tools, etc. Many people call this "agent" alone, which Willison found uncomfortable. Anthropic's terminology clarification resolved this

### Reflections on the Five Workflow Patterns

Willison found all five patterns "meaningful" and appreciated that "having clear names makes reasoning easier." He found the **Evaluator-Optimizer** pattern (code generation → review → improvement loop) "especially fun."

### Resonance with the Complexity Warning

> "When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all."

Willison strongly agrees with this warning. He supports Anthropic's advice to explore possibilities with direct API access and simple code before investing in complex agent frameworks.

### Caution on Agent Autonomy

> "The autonomous nature of agents means higher costs, and the potential for compounding errors."

Willison emphasizes this as a **core practical warning** — autonomy comes with the trade-off of higher costs and compounded errors.

### Cookbook Recipes

Anthropic simultaneously published cookbook recipes explaining all five patterns. In the Evaluator-Optimizer example, a code generation prompt and a code review evaluation prompt are looped, continuing improvements until the evaluator is satisfied.

## Related Concepts

- [[concepts/harness-engineering]] — Parent index
- [[concepts/context-engineering|Context Engineering]] — Context management
- [[concepts/harness-engineering/system-architecture/evals-for-ai-agents]] — Agent evaluation
- [[concepts/coding-agents/minimal-coding-agent]] — Thorsten Ball's 400-line Go implementation. A concrete example of Anthropic's "simple, composable patterns" principle
