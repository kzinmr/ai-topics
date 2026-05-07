---

## Related Entities

- [[entities/samuel-colvin]]
title: "Harrison Chase"
type: entity
tags:
  - person
  - langchain
  - open-source
  - harness-engineering
status: complete
description: "Co-founder and CEO of LangChain. Pioneer of the Open Models / Open Runtime / Open Harness agent architecture framework."
updated: 2026-05-06
sources:
  - "https://x.com/hwchase17/status/2034297125417460044"
  - "https://www.langchain.com/blog/nvidia-enterprise"
  - "https://www.langchain.com/blog/your-harness-your-memory"
  - "https://www.langchain.com/blog/agent-observability-needs-feedback-to-power-learning"
  - "https://github.com/langchain-ai/langchain"
  - "https://www.linkedin.com/in/harrison-chase-961287118"
related:
  - "[[entities/langchain]]"
  - "[[entities/deep-agents]]"
  - "[[concepts/harness-engineering]]"
  - "[[entities/nvidia]]"
  - "[[entities/nvidia-nemoclaw]]"
---

# Harrison Chase

**Harrison Chase** (@hwchase17) is Co-founder and CEO of **LangChain**, the open-source agent engineering platform with over 1 billion downloads and 100+ million monthly downloads.

## LangChain Architecture Vision (March 2026)

Chase articulated the **"Open Models, Open Runtime, Open Harness"** framework, arguing that all production AI agents (Claude Code, OpenClaw, Manus, etc.) share the same underlying architecture decomposed into three layers:

```
┌─────────────────────────────────┐
│       Open Harness              │  ← Orchestration, memory, tool routing
│     (LangChain DeepAgents)      │
├─────────────────────────────────┤
│       Open Runtime              │  ← Sandbox, execution environment
│    (NVIDIA OpenShell / bash)    │
├─────────────────────────────────┤
│       Open Models               │  ← LLM intelligence layer
│  (Nemotron, Claude, GPT, etc.)  │
└─────────────────────────────────┘
```

### Open Models
The intelligence layer. Chase advocates for **model-agnostic** architectures that can swap in the best model for each task. Key example: **NVIDIA Nemotron 3 Super** (120B hybrid Mamba-Transformer, 12B active parameters, 1M context).

### Open Runtime
The environment where agents operate. This is where Chase's framework connects to the user's insight: **agent on bash** naturally selects CLI tools for function calling, while **agent on Python REPL** naturally selects Python functions. The runtime determines the "native" tool-use interface. NVIDIA's answer: **OpenShell** — a secure, sandboxed runtime with kernel-level isolation, policy enforcement, and credential protection.

### Open Harness
The orchestration layer connecting model to runtime. Chase's **Deep Agents** (LangChain's open-source harness) provides built-in task planning, sub-agent spawning, long-term memory, and context management. The harness determines the agent's behavioral patterns.

## NVIDIA Partnership (March 2026)

LangChain announced an enterprise agentic AI platform built with NVIDIA:
- Joined the **Nemotron Coalition** for frontier open model development
- LangSmith observability + Deep Agents harness + NVIDIA infrastructure
- NVIDIA NIM microservices for deployment (up to 2.6x throughput)
- LangGraph parallel execution + speculative execution optimizations
- NeMo Agent Toolkit for profiling, evaluation, and MCP/A2A protocol support

## "Your Harness, Your Memory" Thesis (April 2026)

Chase published a key thesis: **agent memory is inextricably linked to the harness**. Using a closed/proprietary harness means yielding control of agent memory to a third party. This creates vendor lock-in at the memory layer. His position:
- Memory should be open, owned by the agent builder
- Harnesses should be model-agnostic to preserve optionality
- Deep Agents uses open standards (AGENTS.md, Agent Skills) and supports pluggable memory backends (Mongo, Postgres, Redis)

## Agent Observability & Feedback Loop Thesis (May 2026)

Chase published "Agent Observability Needs Feedback to Power Learning" arguing that **observability alone is insufficient** — the critical value comes from closing the feedback loop between observing agent behavior and systematically improving performance.

**Key arguments:**
1. **Traces as the Foundation** — "In software, the code documents the app; in AI, the traces do."
2. **Feedback-Powered Learning Loop** — Collect traces → enrich with evaluations → identify failures → make changes → validate → repeat
3. **Offline + Online Evaluations** — Golden-set evals (unit tests for LLMs) + real-time production drift detection
4. **Human-in-the-Loop Calibration** — LLM-as-judge isn't always right; LangSmith routes to human reviewers
5. **Framework-Agnostic Observability** — LangSmith supports AutoGen, Claude Agent SDK, CrewAI, Mastra, OpenAI Agents, PydanticAI, Vercel AI SDK — not just LangChain/LangGraph

Source: [langchain.com/blog/agent-observability-needs-feedback-to-power-learning](https://www.langchain.com/blog/agent-observability-needs-feedback-to-power-learning)

## LangChain Platform

- **LangChain** (open-source framework) — composable LLM application builder
- **LangGraph** — stateful multi-agent orchestration with complex control flows
- **Deep Agents** — agent harness with planning, sub-agents, memory
- **LangSmith** — observability (15B+ traces, 100T+ tokens processed)
- **LangSmith Deployment** — production deployment platform

## Related People

- **Ryan Lopopolo** (@_lopopolo) — Symphony, Harness Engineering co-thought-leader
- **Sydney Runkle** — Deep Agents runtime author
- **Vivek Trivedy** — Deep Agents runtime author, context fragments theorist
- **Ali Golshan** (NVIDIA) — OpenShell co-author

## Key Quotes

> "Claude Code, OpenClaw, Manus and other agents all use the same architecture under the hood. They consist of a model, a runtime (environment), and a harness." — X post, March 2026

> "In order to own your memory, you need to be using an Open Harness." — "Your Harness, Your Memory" blog, April 2026
