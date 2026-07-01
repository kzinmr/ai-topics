---
title: "Together AI at ICML 2026"
created: 2026-07-01
updated: 2026-07-01
type: concept
tags:
  - research
  - inference
  - agents
  - event
  - announcement
  - optimization
  - hardware
sources:
  - raw/articles/2026-06-30_together-ai-icml-2026.md
---

# Together AI at ICML 2026

Together AI presented nine accepted papers at ICML 2026 (Seoul, June 2026), spanning the full AI stack — from agents at the top to GPU kernels at the bottom. The portfolio reflects the company's vertically integrated approach: research that improves every layer of the inference platform [[entities/together-ai|Together AI]] operates in production.

## Overview

The nine papers are organized by where they sit in the compute stack, reflecting Together AI's thesis that frontier AI performance requires co-optimization across all layers — not isolated improvements at any single layer.

## Papers by Stack Layer

### Layer 1: Agents (Top of Stack)

**DSGym: A Holistic Framework for Evaluating and Training Data Science Agents**
- 1,000+ data-science tasks spanning 10+ domains
- Unified evaluation and training API with self-contained execution environments
- Enables reproducible benchmarking and RL-based training of data science agents
- Joint work with Stanford, Duke, and Harvard
- Addresses the growing need for rigorous [[concepts/evaluation/agent-evaluation-methodology|agent evaluation]] frameworks as data science agents move toward production

**ThunderAgent: A Simple, Fast and Program-Aware Agentic Inference System**
- 1.5–3.6× higher serving throughput for agent workloads
- Adoptable in three lines of code — makes the inference engine "agent-aware" by recognizing multi-turn agent workflow patterns
- Fixes up to 7.14× latency inflation under load (a critical issue for production agent deployments)
- Joint work with Georgia Tech, CMU, and UIUC

### Layer 2: Reasoning & Training

**TTT-Discover: Learning to Discover at Test Time**
- Achieves state-of-the-art discoveries across math, GPU kernels, algorithms, and biology using an open 120B model
- Applies RL at test time on individual problems rather than searching over frozen model outputs
- Represents a fundamental advance in [[concepts/inference-time-compute|inference-time compute]] — shifting discovery from training-time optimization to test-time adaptation
- Joint work with Stanford, NVIDIA, and UCSD

**RARO: Escaping the Verifier — Learning to Reason via Demonstrations**
- Achieves 25% win rate vs 5.9% for supervised fine-tuning (SFT), with no verifier required
- Enables RL-grade reasoning on tasks that lack formal checkers — poetry, financial analysis, and other open-ended domains
- Breaks the dependency on verifiable reward signals that has constrained RL for reasoning to math and code

### Layer 3: Inference Optimization

Three papers advancing production inference efficiency:

- **Opportunistic Expert Activation** — Optimizes Mixture-of-Experts (MoE) decode by selectively activating experts based on runtime conditions rather than static routing
- **Speculative Decoding** — Adaptive to live traffic patterns, cutting per-token costs by dynamically adjusting draft model behavior based on real-time acceptance rates. Builds on the broader [[concepts/speculative-decoding|speculative decoding]] paradigm
- **KV Cache & Context** — Enables longer context windows, larger batch sizes, and faster MoE decoding through cache compression and memory management techniques

### Layer 4: Kernels & Hardware (Bottom of Stack)

Two papers on kernel-level optimizations that translate raw GPU hardware capability into usable inference throughput. These continue Together AI's lineage of kernel innovations (FlashAttention, ThunderKittens, ATLAS) that underpin efficient LLM serving.

## Key Research Highlights

### DSGym
The first holistic framework that combines evaluation and training for data science agents. Unlike prior benchmarks that only measure final accuracy, DSGym provides sandboxed execution environments with a unified API — enabling both assessment and reinforcement learning-based improvement of agent behavior across diverse data science tasks.

### ThunderAgent
Addresses a critical production gap: standard inference engines treat every request as independent, but agent workloads are inherently multi-turn with shared context. By making the engine "agent-aware," ThunderAgent eliminates redundant computation across turns and prevents the latency cascades that cripple agent serving under load.

### TTT-Discover
Demonstrates that test-time RL can achieve discovery-level performance without the enormous computational cost of training-time search. By learning to discover at inference time on a single problem rather than searching over a frozen model's output distribution, TTT-Discover makes open-ended scientific discovery more computationally tractable.

### RARO
Solves the "verifier bottleneck" in RL-based reasoning. Most RL-for-reasoning approaches (like GRPO) require a verifiable reward signal — limiting them to math, code, and other domains with ground-truth checkers. RARO achieves comparable reasoning gains purely from demonstration data, opening RL-grade reasoning to creative and analytical domains.

## Production Impact

Together AI translates its ICML 2026 research directly into platform improvements:

| Metric | Value |
|--------|-------|
| **Coding agent throughput** | 31% more TPS than next-fastest OSS engine for production coding agent workloads |
| **Platform adoption** | 40+ models chosen for production deployment on the Together platform |
| **Hardware availability** | B200 GPUs now available on-demand via Together GPU Clusters |
| **Agent workload efficiency** | 1.5–3.6× throughput improvement via ThunderAgent for multi-turn agent serving |

The research-to-production pipeline is central to Together AI's strategy: ICML papers on speculative decoding and KV cache optimization directly reduce per-token costs for platform customers, while ThunderAgent's agent-aware serving improves the economics of hosting agent workloads at scale.

## See Also

- [[entities/together-ai|Together AI]] — Company profile, products, and technology stack
- [[concepts/evaluation/agent-evaluation-methodology|Agent Evaluation]] — Frameworks and methodology for evaluating AI agents
- [[concepts/inference-time-compute|Inference-Time Compute]] — Test-time computation strategies including TTT-Discover's approach
- [[concepts/speculative-decoding|Speculative Decoding]] — The speculative decoding paradigm for inference acceleration
- [[concepts/token-economics|Token Economics]] — How inference optimization research translates to cost reduction at scale
