---
title: "Building Effective Agents"
type: concept
created: 2026-04-12
updated: 2026-06-02
tags:
  - concept
  - architecture
  - harness-engineering
  - anthropic
  - ai-agents
  - workflow
  - tool
aliases:
  - building-effective-agents
  - agent-design-patterns
  - anthropic-agent-guide
related:
  - "[[concepts/context-engineering]]"
  - "[[concepts/writing-tools-for-agents]]"
  - "[[concepts/harness-engineering]]"
  - "[[concepts/managed-agents]]"
  - "[[concepts/multi-agent-research-system]]"
  - "[[concepts/minimal-coding-agent]]"
sources:
  - "https://www.anthropic.com/engineering/building-effective-agents"
  - "raw/articles/2026-05-08_anthropic-engineering_building-effective-agents.md"
  - "raw/articles/2024-12-20_simon-willison_building-effective-agents.md"
---

# Building Effective Agents

**Building Effective Agents** is Anthropic's practical guide to constructing LLM-based agentic systems, published December 2024. Derived from collaboration with dozens of production teams, it codifies the patterns that consistently work: simple, composable building blocks over complex frameworks. The article became a canonical reference in the agent engineering field, praised by [[entities/simon-willison|Simon Willison]] as "the clearest practical guide to building LLM agents I have seen."

## Core Philosophy

> "Consistently, the most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns."

> "Success in the LLM space isn't about building the most sophisticated system. It's about building the *right* system for your needs."

Three core principles:
1. **Simplicity** — Maintain simplicity in agent design
2. **Transparency** — Explicitly show the agent's planning steps
3. **ACI Design** — Carefully craft the agent-computer interface through thorough tool documentation and testing

## Workflows vs. Agents

The article draws a key architectural distinction within "agentic systems":

| Dimension | Workflow | Agent |
|-----------|----------|-------|
| **Control** | LLMs orchestrated via predefined code paths | Model autonomously controls tool use and decisions |
| **Predictability** | High — consistent execution paths | Lower — adapts based on environment feedback |
| **Best for** | Well-defined, decomposable tasks | Open-ended problems requiring flexibility |

**The critical advice**: find the simplest solution first. Only add complexity when it demonstrably improves outcomes. Many applications need nothing more than optimized single LLM calls with retrieval and in-context examples.

## Building Blocks (Compositional Patterns)

The article defines a hierarchy of patterns, from simple building blocks to autonomous agents:

### Augmented LLM
The fundamental unit — an LLM enhanced with **retrieval**, **tools**, and **memory**. Modern models can actively use these capabilities: generating search queries, selecting tools, determining what to retain.

### Workflow Patterns

| Pattern | Description | When to Use |
|---------|-------------|-------------|
| **Prompt Chaining** | Sequential steps with programmatic gates between them | Tasks cleanly decomposable into fixed subtasks |
| **Routing** | Classify input → specialized handler | Distinct categories better handled separately |
| **Parallelization** | Sectioning (independent subtasks) or Voting (multiple attempts) | Speed or confidence through multiple perspectives |
| **Orchestrator-Workers** | Central LLM dynamically delegates to workers | Unpredictable subtasks (e.g., multi-file code changes) |
| **Evaluator-Optimizer** | Generate + evaluate loop until quality threshold | Clear evaluation criteria, iterative refinement adds value |

### Autonomous Agent

An LLM using tools in a loop based on environmental feedback:

```
command → plan → tool call → environment feedback → iterate → result
```

Key implementation details:
- **Ground truth** from the environment at each step is essential
- **Human feedback** at checkpoints or blockers
- **Iteration limits** for control
- Agents are "typically just LLMs using tools based on environmental feedback in a loop"

## When to Use Agents

Agents suit **open-ended problems** where:
- Required steps can't be predicted in advance
- Multiple execution paths exist, determined by environment feedback
- Many steps or branching that rigid workflows handle poorly

**Trade-off**: autonomy means higher costs and potential for compounding errors. Test extensively in sandboxed environments with guardrails.

## Framework Guidance

> "Frameworks make it easy to get started... But they often create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug."

**Advice**: Start by using LLM APIs directly. Many patterns can be implemented in a few lines of code. If using a framework, understand the underlying code.

Referenced frameworks: Claude Agent SDK, Strands Agents SDK (AWS), Rivet, Vellum.

## Appendix: Agents in Practice

Two particularly promising production domains:

### Customer Support
Natural conversation flow + tool integration (customer data, order history, knowledge base). Actions like refunds handled programmatically. Success measured through resolution rates. Usage-based pricing models (charge per successful resolution) demonstrate confidence.

### Coding Agents
Code solutions are verifiable through automated tests. Agents iterate using test results as feedback. Problem space is well-defined and structured. Output quality measurable objectively. Human review remains crucial for broader system alignment.

## Appendix: Prompt Engineering Your Tools (ACI)

The article introduces the **agent-computer interface (ACI)** concept — invest as much effort in tool design as in human-computer interfaces (HCI):

- **Format matters**: Writing diffs requires knowing line counts upfront; JSON requires escaping. Keep formats close to what models see naturally in training data.
- **Put yourself in the model's shoes**: Is tool usage obvious from the description and parameters?
- **Parameter naming**: Think of writing great docstrings for a junior developer.
- **Poka-yoke**: Change arguments so mistakes are harder (e.g., require absolute file paths instead of relative ones).
- **Test empirically**: Run many example inputs to see what mistakes the model makes.

> "We actually spent more time optimizing our tools than the overall prompt." — on building the SWE-bench agent

## Relationship to the Agent Engineering Ecosystem

This article sits at the foundation of [[concepts/harness-engineering]] — it defines the core building blocks that more advanced patterns compose from:

```
Building Effective Agents (foundational patterns)
├──→ Context Engineering (how to fill the context window)
├──→ Writing Tools for Agents (ACI design methodology)
├──→ Managed Agents (meta-harness for agent deployment)
├──→ Multi-Agent Research System (orchestrator-workers in production)
└──→ Harness Engineering (environment design philosophy)
```

## Graph Structure Query

```
[building-effective-agents] ──author──→ [anthropic]
[building-effective-agents] ──contrasts──→ [complex-agent-frameworks]
[building-effective-agents] ──extends──→ [harness-engineering]
[building-effective-agents] ──relates-to──→ [context-engineering]
[building-effective-agents] ──teaches──→ [agent-workflow-patterns]
[building-effective-agents] ──precedes──→ [writing-tools-for-agents]
```

Authored by Anthropic (Erik S. and Barry Zhang). Extends [[concepts/harness-engineering]] as foundational building blocks. The ACI appendix directly precedes the full methodology in [[concepts/writing-tools-for-agents]].

## Simon Willison's Annotations (2024-12-20)

[[entities/simon-willison|Simon Willison]] praised the article's terminology framework:
- **"Agentic systems"** as parent category
- Clear distinction between **"workflows"** and **"agents"**
- **"Augmented LLM"** — resolving the discomfort of calling a single LLM with tools an "agent"

He found the **Evaluator-Optimizer** pattern "especially fun" and strongly agreed with the complexity warning: explore with direct API access before investing in frameworks.

## Related Concepts

- [[concepts/context-engineering]] — Context window optimization techniques
- [[concepts/writing-tools-for-agents]] — ACI design methodology (the tool design deep-dive)
- [[concepts/harness-engineering]] — Parent framework (environment design philosophy)
- [[concepts/managed-agents]] — Meta-harness architecture
- [[concepts/multi-agent-research-system]] — Orchestrator-workers in production
- [[concepts/minimal-coding-agent]] — Thorsten Ball's 400-line Go implementation of these principles
- [[concepts/swe-bench-agent-scaffolding]] — SWE-bench agent implementation details
- [[concepts/agentic-loop]] — The core agent execution loop

## Sources

- [Building Effective Agents — Anthropic Engineering](https://www.anthropic.com/engineering/building-effective-agents)
- [Simon Willison's annotations (2024-12-20)](https://simonwillison.net/2024/Dec/20/building-effective-agents/)
- [[raw/articles/2026-05-08_anthropic-engineering_building-effective-agents.md]]
- [[raw/articles/2024-12-20_simon-willison_building-effective-agents.md]]
