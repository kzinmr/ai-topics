---
title: "Hidden Technical Debt of AI Systems: Agent Harness"
source: "https://leehanchung.github.io/blogs/2026/05/08/hidden-technical-debt-agent-harness/"
author: "Hanchung Lee (Han Lee)"
date: 2026-05-08
type: article
tags: [agent-harness, technical-debt, agent-infrastructure, system-prompt, tool-surface, rollout-protocol, context-management]
---

# Hidden Technical Debt of AI Systems: Agent Harness

Third in the "Hidden Technical Debt of AI Systems" series. Focuses on the **agent harness** — the orchestration layer between the model and its environment. Core argument: most of today's harness code (system prompts, tool wrappers, planners, memory stacks, multi-agent graphs) will be made redundant by the next generation of models, and teams treating their harness as a permanent product surface are accumulating severe technical debt.

## What Is an Agent Harness?

An **agent** = **harness** + **foundation model**. Analogy: model = CPU, harness = operating system (provides interrupts, interfaces, memory management, illusion of infinite resources).

### Components of a Harness

- **System prompt and persona** – standing instructions
- **Tool surface** – functions exposed to the model, with schemas/descriptions
- **Rollout protocol** – single-turn, multi-turn, ReAct, plan-and-execute, deep-research, multi-agent
- **Context manager** – what gets carried, compacted, summarized, dropped across turns
- **Memory** – short-term scratchpads, mid-term progress files, long-term stores
- **Sub-agent topology** – orchestrator, workers, judges, hand-off protocols
- **Guardrails and gates** – input/output filters, action gates, allowlists, approval tiers
- **Verifiers and judges** – decide success, continuation, stopping
- **Observability** – traces, replay, eval hooks

### Inner vs Outer Harness (Birgitta Böckeler)

- **Inner harness** – shipped by the model builder (e.g., Claude Agent SDK, Codex app server)
- **Outer harness** – assembled by the user (e.g., AGENTS.md, MCP servers, custom skills)

## Research vs Production Harness — The Critical Asymmetry

The most under-discussed property: the training harness and the production harness are **different artifacts** and should be engineered separately.

| Dimension | Training / Research Harness | Production Harness |
|-----------|---------------------------|---------------------|
| Action space | Maximal – let model try anything | Minimal – explicit allowlist, deny by default |
| Tools | Raw, low-level, easy to extend | Wrapped, scoped, versioned |
| Failures | Welcome – failure is signal | Suppressed – fail closed, retry, page |
| Network | Often offline or recorded | Live, strict egress policies |
| Guardrails | KL caps, reward shaping, curriculum gates | RBAC, JWT, action gates, output filters |
| Verifier | Programmatic, scaled, noisy on purpose | Deterministic where possible, human-in-loop |
| State | Forkable, snapshottable, replayable | Durable, per-user, auditable |
| Cost model | Many cheap rollouts; tail behavior matters | Few expensive sessions; latency & reliability |
| "Good" means | Policy improves on held-out distribution | User's task succeeds without incident |

### Three Consequences

1. **Training harness should NOT be a stripped-down production harness** — copying production's allowlists starves the model of learning opportunities.
2. **Production harness should NOT be a deployed training harness** — shipping an open-ended research environment leads to prompt injection and data exfiltration.
3. **The bridge is an evaluation harness** that mirrors production tightly, run by the same team owning prompts and tools.

## First-Party vs Third-Party Harness

- **First-party harness advantage:** The model was post-trained inside that specific harness. Drop the same model into a third-party harness → run it **out-of-distribution**.
- **Third-party can win on a neglected axis:** Example — Letta Code on Opus 4.5 scored 59.1% vs Claude Code's 41.6% by investing in durable memory. On stronger first-party harnesses (GPT 5.1, Gemini 3), Letta lands within a few points but does not lead.

> "The harness is load-bearing, and a third-party harness with a deliberate axis of investment can outperform a first-party harness that neglects that axis."

## Alignment: Inside Out vs Outside In

- **Production harness**: fences around behavior — necessary but limited.
- **Training harness**: shapes behavior from the inside — the model learns what "good" means within its training environment.
- **Bridge**: evaluation harness catches regressions.

## Five Harness Design Principles

1. **Treat the harness as temporary scaffolding** — the model will absorb more harness responsibility each generation.
2. **Separate training, evaluation, and production harnesses** — different artifacts, different owners.
3. **The evaluation harness is your moat** — invest here more than in production.
4. **Prefer outer-harness simplicity** — fewer custom pieces = less drift from the training distribution.
5. **Assume the model improves weekly** — what's "impossible" today may be trivial next month.

> "The agent is the foundation model plus the harness, and the harness is temporary."
