---
title: "AI Agents"
type: concept
created: 2026-04-25
updated: 2026-11-13
tags:
  - concept
  - ai-agents
  - taxonomy
sources: []
aliases:
  - ai-agents
  - AI agent
  - autonomous agents
---

# AI Agents

> **Hub page.** "AI Agents" is the most-linked umbrella term in this wiki (70+ inbound references) but was kept a stub since the 2026-04-25 bulk import. This page now serves as the **taxonomy/triage map**: read this first to find the right specialized page, since virtually every sub-topic has its own canonical page.

## Definition

An **AI agent** is an LLM-driven system that, in a loop, (1) perceives task state from its environment, (2) plans and selects actions, (3) executes them via **tools** (code execution, browsers, APIs, file systems), and (4) observes results — iterating until a goal condition or budget is met. This contrasts with a single-shot "prompt → response" interaction and with fixed pipelines ("build agents, not pipelines"). Anthropic's operational definition: *a system where the model dynamically directs its own process and tool use* ([[concepts/building-effective-agents]]).

## The anatomy (Agent = Model + Harness)

```
        ┌──────────────────────────────────────────┐
        │                HARNESS                   │
        │  system prompt · tools · sandbox ·       │
        │  context mgmt · memory · permissions     │
        │  ┌────────────────────────────────────┐  │
        │  │            MODEL (LLM)             │  │
        │  │   plan → act (tool call) → observe │  │
        │  └────────────────────────────────────┘  │
        └──────────────────────────────────────────┘
                 ▲                    │
                 └──── environment ────┘
```

- **Model** — reasoning/tool-calling capability; see [[concepts/agent-model-drift]].
- **Harness** — everything around the model: [[concepts/harness-engineering]] (umbrella philosophy), [[concepts/agent-harnesses]], [[concepts/agent-harness-primitives]], [[concepts/outer-harness]].
- **Loop & orchestration** — [[concepts/agent-loop-orchestration]], [[concepts/subagents]], [[concepts/multi-agents/agent-orchestration]].
- **Context & memory** — [[concepts/context-engineering/_index]] (directory), [[concepts/ai-agent-memory]], [[concepts/ai-agent-memory-middleware]].
- **Tools** — [[concepts/writing-tools-for-agents]], [[concepts/programmatic-tool-calling]], [[concepts/agent-native-tool-fallacy]].

## Where the deep coverage lives

| Sub-topic | Canonical page(s) |
|---|---|
| Foundational patterns | [[concepts/building-effective-agents]], [[concepts/ai-agent-architecture]], [[concepts/agents-planning-orchestration]] |
| Harness/scaffolding | [[concepts/harness-engineering]], [[concepts/agent-scaffolding]], [[concepts/bitter-lesson-agent-harnesses]] |
| Human-side practice | [[concepts/agentic-engineering]], [[concepts/vibe-coding-vs-agentic-engineering]] |
| Long-horizon behavior | [[concepts/long-horizon-agents]], [[concepts/agents-scaffolding-composition-inference-scaling-hypothesis]] |
| Coding agents | [[concepts/how-coding-agents-work]], [[concepts/coding-agents/_index]] |
| Computer/browser use | [[concepts/computer-using-agent]], [[concepts/agentic-browsing]] |
| Agent–agent protocols | [[concepts/agent-communication-standards]], [[concepts/a2a-agent-protocol]], [[concepts/agent-client-protocol]] |
| Safety & security | [[concepts/ai-agent-safety]], [[concepts/ai-agent-security]], [[concepts/agentic-misalignment]] |
| Economics | [[concepts/agent-economics]], [[concepts/agent-execution-tax]] |
| Evaluation | [[concepts/evaluation/evals-for-ai-agents]], [[concepts/ai-benchmarks/gaia-benchmark]] |
| Production | [[concepts/production-ai-agents]], [[concepts/reliable-agent-patterns]] |
| Failure modes | [[concepts/ai-agent-traps]], [[concepts/agent-slop]], [[concepts/single-agent-ceiling]] |

## Terminology disputes

- **Agent vs. workflow** — Anthropic's "workflows" (predefined code paths) vs. "agents" (model-directed); contested boundary, see [[concepts/agent-vs-pipeline-architecture]].
- **"Agent" as marketing term** — many "agent" products are deterministic pipelines; see [[concepts/unharnessed-agents]] and [[concepts/agent-native-tool-fallacy]].
- **Agentic engineering ≠ AI agent engineering** — human-side usage patterns vs. system-side build patterns (see [[concepts/harness-engineering]] hierarchy).

## Related

- [[concepts/harness-engineering]] — the umbrella philosophy
- [[concepts/building-effective-agents]] — Anthropic's pattern catalog
- [[concepts/agentic-engineering]] — the practitioner discipline
- [[concepts/production-ai-agents]] — deployment concerns
