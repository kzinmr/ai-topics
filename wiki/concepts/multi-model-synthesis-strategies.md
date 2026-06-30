---
title: "Multi-Model Synthesis Strategies"
created: 2026-06-30
updated: 2026-06-30
type: concept
tags:
  - multi-llm
  - orchestration
  - model-routing
  - inference
  - optimization
  - harness-engineering
  - coding-agents
  - cost-optimization
sources:
  - raw/articles/2026-06-29_cognition-devin-fusion-multi-model-harness.md
  - raw/articles/2026-06-12_openrouter-fusion-api-multi-model-synthesis.md
  - raw/articles/2026-06-22_sakana-fugu-multi-agent-system-model.md
---

# Multi-Model Synthesis Strategies

> **"The age of using one model for all of your work is coming to an end."** — In June 2026, Cognition, OpenRouter, and Sakana AI each demonstrated distinct approaches to combining multiple models, achieving performance beyond any single model alone.

## Overview

Multi-model synthesis strategies are architectural patterns that combine multiple LLMs to achieve performance, cost, or capability advantages over any single model alone. Three distinct approaches emerged simultaneously in June 2026:

| Approach | Provider | Pattern | Key Innovation |
|---|---|---|---|
| **Sidekick + Dynamic Routing** | [[entities/cognition]] (Devin Fusion) | Parallel main+sidekick agents | Cache-aware delegation, mid-session model switching |
| **Panel Synthesis** | [[entities/openrouter]] (Fusion API) | Parallel models + judge | Structured consensus/contradiction analysis |
| **Evolved Orchestration** | [[entities/sakana-ai]] ([[concepts/sakana-fugu]]) | RL-trained coordinator | TRINITY role assignment (Thinker/Worker/Verifier) |

## The Three Approaches

### 1. Cognition Devin Fusion: Sidekick Pattern

Cognition's approach runs two parallel agents — a frontier "main" agent and a cost-effective "sidekick" agent, each with persistent cached contexts.

**Core mechanics:**
- Main agent handles planning, ambiguity resolution, and final review
- Sidekick handles routine execution (code writing, file manipulation)
- **Dynamic mid-session routing**: Lightweight classifiers signal when to switch models; switching happens during context compaction (free cache-wise)
- Both agents maintain their own persistent cached contexts, avoiding the expensive cache misses of cross-model tool calls

**Results:** 35% cost reduction at frontier performance; 41% with Fable 5 in the harness. 88% of internal merged PRs driven entirely by automated Fusion router.

**Why it works:** The sidekick pattern retains "real frontier intelligence" rather than "benchmark-score intelligence." It generalizes beyond single-prompt tasks because the main agent can dynamically delegate or reclaim work mid-session.

**Scaling property:** As models get smarter, sidekick works better. Fable 5 delegates more intelligently, requests context more efficiently — yielding a 41% cost improvement vs. 35% with older frontier models.

Source: [[raw/articles/2026-06-29_cognition-devin-fusion-multi-model-harness]]

### 2. OpenRouter Fusion: Panel Synthesis

OpenRouter's approach dispatches the same prompt to a panel of models in parallel, then a judge model synthesizes the results.

**Core mechanics:**
- Panel models each process the prompt independently (with web search, web fetch, bash)
- Judge model reads all responses and produces structured analysis: consensus points, contradictions, partial coverage, unique insights, blind spots
- Judge then writes the final answer grounded in that analysis
- Entire pipeline runs server-side, callable like a single model

**Results (DRACO benchmark):**
- Fable 5 + GPT-5.5 fused: **69.0%** (surpasses every individual model)
- Budget panel (Gemini 3 Flash + Kimi K2.6 + DeepSeek V4 Pro): **64.7%** — beats GPT-5.5 and Opus 4.8, within 1% of Fable 5 at 50% cost
- Self-fusion (Opus 4.8 × 2): **65.5%** — 6.7-point jump over solo, showing that synthesis itself contributes significantly

**Key insight:** Model diversity works like human team diversity — bringing multiple perspectives to complex problems yields superior results. Even self-fusion (same model, different runs) produces meaningful gains because different reasoning paths, tool calls, and source selections emerge.

**API modes:** Model slug (`openrouter/fusion`), server tool, plugin, or chatroom.

Source: [[raw/articles/2026-06-12_openrouter-fusion-api-multi-model-synthesis]]

### 3. Sakana Fugu: Evolved Orchestration

Sakana Fugu takes the most ambitious approach — an RL-trained coordinator that dynamically assigns Thinker, Worker, or Verifier roles to specialized models.

**Core mechanics:**
- TRINITY (ICLR 2026): Evolved coordinator that assigns roles adaptively based on task context
- Conductor (ICLR 2026): RL-trained natural-language coordination strategies
- User sends one request; Fugu distributes work across its model pool and returns a unified response
- Provider flexibility: users can exclude specific providers for compliance/privacy

**Results:** Fugu Ultra achieves 73.7 on SWE-bench Pro, 82.1 on TerminalBench 2.1 — roughly Fable-class.

**Key difference from Fusion:** Fugu is an opaque orchestration layer delivered as a single API. The user doesn't choose which models participate (beyond exclusions). OpenRouter Fusion lets the user explicitly configure the panel.

Source: [[raw/articles/2026-06-22_sakana-fugu-multi-agent-system-model]]

## Comparative Analysis

| Dimension | Devin Fusion (Sidekick) | OpenRouter Fusion (Panel) | Sakana Fugu (Orchestration) |
|---|---|---|---|
| **Architecture** | 2 parallel agents (main + sidekick) | N parallel models + judge | RL-trained coordinator pool |
| **User control** | Low (harness decides) | High (choose panel + judge) | Low (opaque pool) |
| **Cost strategy** | Delegate cheap work to sidekick | Use cheap models in panel | Coordinator selects cost-efficient models |
| **Cache efficiency** | High (persistent contexts per agent) | Low (each panel call is fresh) | Unknown (API-level abstraction) |
| **Transparency** | Medium (see which model does what) | High (see all panel outputs) | Low (single unified response) |
| **Best for** | Long coding sessions | Research/synthesis tasks | General-purpose multi-step tasks |
| **Benchmark** | FrontierCode (coding) | DRACO (deep research) | SWE-bench Pro, TerminalBench |
| **Latency** | ~same as single model (sidekick runs in parallel) | 2-3x slower | Unknown |

## Relationship to Model Routing

These synthesis strategies are distinct from but related to [[concepts/coding-agents/model-routing|model routing]] (per-turn model selection):

- **Model routing** (Augment Prism, Solo Agency): Selects ONE model per turn based on task complexity. Sequential.
- **Sidekick pattern** (Devin Fusion): Runs TWO models in parallel, delegates dynamically. Concurrent.
- **Panel synthesis** (OpenRouter Fusion): Runs N models in parallel, fuses results. Concurrent + synthesis.
- **Evolved orchestration** (Sakana Fugu): RL-learned role assignment across a pool. Adaptive.

Model routing optimizes cost by choosing the cheapest capable model per turn. Synthesis strategies optimize quality by combining multiple models' outputs. Devin Fusion bridges both: the sidekick is a routing decision (cheap model for cheap work), while the main-sidekick interaction is a synthesis pattern.

## The Economics Argument

All three approaches address the same economic reality:

> "You wouldn't drive a Lamborghini to the grocery store, so why should you take a model that can discover zero-day vulnerabilities in software and use it to round the corner of a button?" — Cognition

- **Devin Fusion**: Frontier model costs are "reaching prohibitive levels" — 35-41% savings by offloading routine work
- **OpenRouter Fusion**: Budget panels achieve frontier-class results at 50% cost
- **Sakana Fugu**: "Frontier-level performance without single-vendor dependency" — avoids premium single-model pricing

The convergence of these three approaches in the same month (June 2026) signals a structural shift: the industry is moving from "pick the best model" to "orchestrate multiple models."

## Implications for Harness Engineering

Multi-model synthesis is a [[concepts/harness-engineering|harness engineering]] problem, not a model problem:

- The routing/delegation logic is harness code
- Cache management across models is harness infrastructure
- The judge/synthesis prompt is a harness component
- Model switching during compaction is a harness optimization

This aligns with the "Harness > Model" consensus: the orchestration layer captures more value than any individual model.

## Open Questions

1. **When does synthesis beat routing?** Panel synthesis adds latency (2-3x). For time-sensitive tasks, routing may be superior.
2. **Synthesis overfitting?** OpenRouter found that judge model choice shifts scores 10-25 points. Are we optimizing for the judge, not the task?
3. **Composition of panels?** OpenRouter showed budget panels work well for research. Do they work for coding? Math? Creative writing?
4. **Fugu's opacity trade-off:** Sakana's approach maximizes convenience but minimizes user control. When is this the right trade-off?
5. **Sidekick scaling:** Cognition found sidekick works better as models improve. Does this continue indefinitely, or does the sidekick eventually become unnecessary?

## Related Pages

- [[concepts/coding-agents/model-routing]] — Per-turn model selection (precursor to synthesis strategies)
- [[concepts/sakana-fugu]] — Sakana Fugu architecture and research foundation
- [[entities/openrouter]] — OpenRouter platform and Fusion API
- [[entities/cognition]] — Cognition / Devin architecture
- [[entities/devin]] — Devin agent details
- [[concepts/harness-engineering]] — Harness engineering discipline (synthesis is a harness problem)
- [[concepts/multi-agents/multi-agent-orchestration]] — Multi-agent orchestration patterns
- [[concepts/inference-optimization]] — Inference cost optimization
- [[concepts/harness-commoditization]] — The harness layer as competitive moat
