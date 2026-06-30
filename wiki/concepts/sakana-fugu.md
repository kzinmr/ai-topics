---
title: "Sakana Fugu"
created: 2026-06-22
updated: 2026-06-24
type: concept
tags:
  - fugu
  - sakana-ai
  - multi-agent
  - orchestration
  - agent-coordination
  - model
  - reinforcement-learning
  - iclr-2026
  - hn-popular
sources:
  - raw/articles/2026-06-22_sakana-fugu-multi-agent-system-model.md
---

# Sakana Fugu

> **Multi-agent system delivered as a single model API.** Available in two variants (Fugu and Fugu Ultra), Fugu dynamically orchestrates a pool of specialized models to tackle complex multi-step tasks — all accessible through one OpenAI-compatible API endpoint. Released June 2026 by [[entities/sakana-ai]].

## Overview

Sakana Fugu is a multi-agent orchestration system that presents itself as a single model behind an OpenAI-compatible API. Rather than requiring users to manually select and switch between models for different subtasks, Fugu handles model selection, role assignment, and coordination internally. The user sends one request; Fugu distributes work across its pool of expert models and returns a unified response.

**Tagline**: "Frontier-level performance without single-vendor dependency."

## Variants

### Fugu (Standard)
- Balanced performance and latency — the default for everyday work
- Drop-in replacement for tools like [[concepts/codex/_index]] for coding and code review
- Responsive chatbot capability from a single endpoint
- Respects data, privacy, and compliance constraints by allowing provider exclusions from the model pool

### Fugu Ultra
- Coordinates a deeper pool of expert agents for maximum answer quality
- Targets hard, high-stakes problems where quality matters more than latency
- Primary use cases: Kaggle competitions, paper reproduction, cybersecurity analysis, literature and patent research

## Research Foundation

Fugu is grounded in two papers accepted at ICLR 2026:

### TRINITY: An Evolved LLM Coordinator
A lightweight evolved coordinator that orchestrates multiple LLMs over several turns. TRINITY assigns **Thinker**, **Worker**, or **Verifier** roles adaptively based on the task context. Demonstrated across coding, math, reasoning, and knowledge tasks. The evolutionary approach discovers coordination strategies that outperform hand-designed multi-agent patterns.

### Conductor: Learning to Orchestrate Agents in Natural Language
Trained with reinforcement learning, Conductor discovers natural-language coordination strategies for directing agent teams. It designs agent communication patterns and focused prompts, demonstrating that diverse LLMs under coordinated orchestration outperform single monolithic models on hard reasoning benchmarks.

Together, these papers establish the theoretical basis for Fugu's architecture: evolved coordination (TRINITY) for role assignment and RL-trained orchestration (Conductor) for natural-language agent direction.

## Architecture

Fugu operates as a **model router and coordinator**, not a single trained model:

1. **Request arrives** at the OpenAI-compatible API endpoint
2. **Coordinator analyzes** the task and determines which specialized models to engage
3. **Role assignment** follows TRINITY patterns: Thinker models reason about the problem, Worker models execute sub-tasks, Verifier models validate outputs
4. **Multi-turn orchestration** allows agents to pass results between each other
5. **Unified response** is returned to the caller

### Provider Flexibility
Users can control which agents participate in Fugu's model pool, opting out of specific providers or models for data privacy, compliance, or organizational requirements. This avoids vendor lock-in and allows deployment in regulated environments.

## Benchmark Performance

Fugu models achieve frontier-level performance:
- Surpass publicly accessible frontier models on standard benchmarks
- Shoulder-to-shoulder with Fable 5 and Mythos Preview in engineering, science, and reasoning evaluations
- Competes without export control risks (no single-vendor dependency)

**Fugu Ultra reported benchmarks (June 2026):** 73.7 on SWE-bench Pro, 82.1 on TerminalBench 2.1 — roughly Fable-class for coding and terminal tasks.

## Experiments

### AutoResearch Integration
Fugu integrates with AutoResearch (Karpathy et al.) for autonomous AI research. In one demonstration, an AI agent used Fugu to iteratively improve a small GPT training recipe — autonomously editing code, running experiments, and keeping changes that reduced validation bits-per-byte.

### Classical Japanese Kana Reading Order Recovery
Tests whether Fugu can recover the reading order of scattered chirashigaki (classical Japanese calligraphy), demonstrating the system's ability to handle culturally specific, unstructured reasoning tasks.

## Use Cases

| Use Case | Recommended Variant | Description |
|---|---|---|
| Everyday coding & code review | Fugu | Integrates with Codex for development workflows |
| Chatbot & general Q&A | Fugu | Single-endpoint responsive chat |
| Kaggle competitions | Fugu Ultra | Deep expert pool for competitive ML |
| Cybersecurity analysis | Fugu Ultra | Multi-perspective threat analysis |
| Academic paper reproduction | Fugu Ultra | Rigorous multi-step research tasks |
| Literature & patent research | Fugu Ultra | Cross-domain synthesis |

## Competitive Positioning

Fugu embodies [[entities/sakana-ai]]'s core thesis: that intelligence can emerge from coordinating simpler components rather than scaling a single monolithic system. By delivering multi-agent orchestration as a single API, Fugu reduces the complexity barrier for teams that want agentic capabilities without building their own orchestration infrastructure.

The "no single-vendor dependency" positioning directly challenges the walled-garden approaches of major frontier labs, aligning with Sakana AI's broader architectural sovereignty mission.

## Related Pages

- [[entities/sakana-ai]] — Sakana AI lab, creators of Fugu
- [[concepts/multi-agents/multi-agent-orchestration]] — Multi-agent orchestration patterns and architectures
- [[concepts/multi-agents/agent-orchestration]] — Agent orchestration concepts and frameworks
- [[concepts/multi-agents/multi-agent-systems]] — Multi-agent systems overview
- [[concepts/codex/_index]] — OpenAI Codex coding agent platform (integrates with Fugu)
- [[concepts/multi-agents/multi-agent-rl]] — Multi-agent reinforcement learning approaches
- [[concepts/multi-model-synthesis-strategies]] — Multi-model synthesis taxonomy (Fugu, Devin Fusion, OpenRouter Fusion)

## External Links

- Sakana Fugu: https://sakana.ai/fugu/
- HN Discussion: https://news.ycombinator.com/item?id=48624782 (130 points, 80 comments)
