---
title: Agent Harness Primitives
created: 2026-04-25
updated: 2026-04-25
type: concept
tags: [training, framework, pattern]
sources: [raw/articles/2026-04-25-langchain-anatomy-agent-harness.md, raw/articles/2026-04-25-harness-engineering-era-3.md]
---

# Agent Harness Primitives

A harness is every piece of code, configuration, and execution logic that wraps a raw model to turn it into a work engine. Agent = Model + Harness. The bottleneck has shifted from **model capability** to **execution infrastructure**.

## Core Thesis

> "If you're not the model, you're the harness." — Vivek Trivedy (LangChain Blog, Mar 2026)

A raw model takes in data (text, images, audio) and outputs text. It cannot out-of-the-box maintain durable state, execute code, access realtime knowledge, or set up environments. Harnesses supply these missing capabilities.

## The Three Eras of AI Engineering

| Era | Paradigm | Mental Model | Scope | Limitations |
|-----|----------|-------------|-------|-------------|
| 2024 | Prompt Engineering | "Talking to the AI" | Crafting instructions (CoT, few-shot) | No memory/state, brittle to wording |
| 2025 | Context Engineering | "Feeding the AI" | RAG, context optimization, memory | No constraint enforcement, no feedback loops |
| 2026 | Harness Engineering | "Housing the AI" | Environments, feedback loops, control systems | — |

Shift: from `what to show` → `where to work`; from `enabling capability` → `ensuring reliability`.

## 6 Core Harness Primitives

### 1. Filesystem Abstraction
The most foundational primitive. Ships with fs-ops tools and enables:
- Agents get a workspace to read data, code, documentation
- Work can be incrementally added and offloaded
- **Natural collaboration surface** for multi-agent and human coordination
- Git adds versioning, rollback, and branching

### 2. Code/Bash Execution
General-purpose tool enabling autonomous problem-solving via ReAct loops: reason → act → observe → repeat.

### 3. Tool & Skill System
MCPs, custom tools, skills — bundled infrastructure that extends model capabilities. Skills encode engineering taste into context.

### 4. Orchestration Logic
Subagent spawning, handoffs, model routing, checkpoint management. Graph-based frameworks (LangGraph) provide stateful, multi-actor workflows with cyclical architectures.

### 5. Feedback Loops
Agent self-review before PRs → agent-to-agent review → human checkpoint at key milestones. Automated feedback incorporation and iteration cycles.

### 6. Recovery Mechanisms
Garbage collection, quality grading, automated refactoring PRs. Treat tech debt as high-interest.

## 4 Foundational Principles

1. **Progressive Disclosure** — Give agents a map (~100-line AGENTS.md), not a 1,000-page manual
2. **Repository as System of Record** — If agents can't access it in-context, it doesn't exist
3. **Enforce Invariants, Not Implementations** — Define what must be true, not how to make it true
4. **Agent Legibility** — Optimize for the agent's reasoning, not human preferences

## Practical Implementation Roadmap

1. Start with `AGENTS.md` + docs structure + one linter + basic sandbox
2. Organize `docs/` into design-docs, exec-plans, product-specs, references
3. Encode constraints as tooling (custom linters with remediation instructions)
4. Create sandbox environments with observability stacks & auto-teardown
5. Build feedback loops (agent self-review → agent-to-agent review → human checkpoint)
6. Establish garbage collection (doc freshness, quality grading, refactoring PRs)

## Real-World Proof Points

- **OpenAI internal experiment** (Aug 2025): 3–7 engineers produced ~1 million lines of code with zero manually written code. The breakthrough was the surrounding harness.
- **LangChain's Vivek Trivedy**: "Agent = Model + Harness" — the harness makes model intelligence useful.
- **Steven Cen** (Medium, Mar 2026): "AI writes code, humans design harnesses" — the paradigm shift is complete.

## Related Concepts

- [[concepts/harness-engineering]] — Ryan Lopopolo's broader harness engineering thesis
- [[concepts/context-engineering]] — Context Engineering: feeding the AI information
- [[concepts/openai-symphony]] — OpenAI Symphony: orchestrating large numbers of coding agents
- [[concepts/multi-agent-autonomy-scale]] — Multi-Agent Autonomy Scale
- [[concepts/cognitive-cost-of-agents]] — Cognitive Cost of Agents (Simon Willison)
