---
title: "Hermes 4"
created: 2026-05-28
updated: 2026-05-28
type: entity
tags:
  - model
  - reasoning
  - llm
  - text-generation
  - open-source
  - nous-research
  - synthetic-data
  - post-training
  - hybrid-reasoning
  - rlvr
sources:
  - raw/papers/2025-08-25_2508.18255_hermes-4-technical-report.md
  - https://huggingface.co/collections/NousResearch/hermes-4-collection-68a731bfd452e20816725728
  - https://github.com/NousResearch/atropos
---

# Hermes 4

**Hermes 4** is a family of open-weight **hybrid reasoning models** developed by [[nous-research|Nous Research]], released in August 2025. The models combine structured, multi-turn reasoning (via `<think>` / `</think>` delimiters) with broad instruction-following ability. Three sizes were trained: **14B** (from Qwen3-14B base), **70B**, and **405B** (from Llama 3.1 bases).

| Fact | Detail |
|------|--------|
| **Developer** | [[nous-research|Nous Research]] |
| **Base Models** | Llama 3.1 (70B, 405B), Qwen3 (14B) |
| **Training Data** | ~5M samples, ~19B tokens |
| **Data Composition** | 3.5M reasoning + 1.6M non-reasoning samples |
| **Training Infrastructure** | 192 × NVIDIA B200 GPUs |
| **Training Framework** | Modified TorchTitan + Axolotl (Stage 2) |
| **Context Length** | 16,384 tokens (training), 40,960 (inference) |
| **License** | Open weights (public on HuggingFace) |
| **arXiv** | [2508.18255](https://arxiv.org/abs/2508.18255) |
| **HuggingFace** | [NousResearch/hermes-4-collection](https://huggingface.co/collections/NousResearch/hermes-4-collection-68a731bfd452e20816725728) |
| **Release** | August 25, 2025 (v1), September 2, 2025 (v2) |

## Overview

Hermes 4 is a **hybrid reasoning model family** — meaning it can operate in both **reasoning mode** (generating chain-of-thought traces inside `<think>` tags) and **non-reasoning mode** (direct answer generation). This dual-mode design allows the model to allocate more computation to difficult problems while remaining efficient for simpler tasks.

The model adopts a **"neutrally-aligned"** philosophy — designed to have the **lowest refusal rate** among frontier models (RefusalBench: 57.1 in reasoning mode vs. 11.34 for GPT-5 and 5.60 for gpt-oss-120b), while still refusing prompts related to exploitation, human trafficking, and suicide/self-harm.

**Key innovations** in Hermes 4 include:
- **DataForge**: A graph-based synthetic data generator using DAGs with PDDL action interfaces
- **Atropos**: An open-source RL environment manager for rejection sampling against ~1,000 task-specific verifiers
- **Reasoning length control**: A novel second-stage SFT that teaches the model to close `</think>` at 30K tokens with minimal performance cost
- **Composability**: Graphs implement a node interface, enabling arbitrary nesting of higher-order graphs

## Model Sizes & Training

| Model | Base | Params | Parallelism | LR | B200 Hours |
|-------|------|--------|-------------|-----|-----------|
| Hermes 4 14B | Qwen3-14B | 14B | FSDP | 5×10⁻⁵ | 4,454 |
| Hermes 4 70B | Llama 3.1-70B | 70B | FSDP+TP | 1×10⁻⁵ | 12,864 |
| Hermes 4 405B | Llama 3.1-405B | 405B | FSDP+TP | 5×10⁻⁶ | 71,616 |

All models trained for 9,000 steps with 300 warmup steps, global batch size 384, 16,384 token context. Uses **First-Fit Decreasing packing** (>99.9% batch efficiency) with **Flex Attention** for intra-sample attention masking. Only tokens from the "assistant" role contribute to the loss (loss-masking).

## DataForge: Graph-Based Synthetic Data

DataForge is a **graph-based synthetic data generator** inspired by AgentInstruct, where data flows through a **directed acyclic graph (DAG)** of processing nodes. Each node implements the **PDDL action interface** — defining preconditions and postconditions that determine data flow eligibility. Edges are implicit: a directed edge from node A to node B exists iff A's postconditions satisfy B's preconditions.

**Key properties:**
- **Declarative graph construction**: Researchers specify node behaviors and graph structure emerges from precondition/postcondition matching
- **Graph composability**: Because every graph has a single source and target, graphs can be nested as nodes in higher-order graphs to arbitrary depth
- **Multi-stage refinement**: Typical pipeline is passage transformation → instruction generation → answer generation → LLM judge review (with retries)
- **Training on intermediates**: The model is trained on all intermediate LLM calls, not just final QA pairs — giving Hermes 4 specialized instruction generation and judging capabilities

Seed data is drawn from a biased sample of DCLM and FineWeb, semantically deduplicated via ModernBert embeddings (cosine similarity threshold 0.7), then filtered through an LLM judge.

## Atropos: RL Environment Manager

Atropos serves dual roles as both an RL training environment manager and an evaluation framework. For the Hermes 4 dataset, it performed rejection sampling against ~1,000 task-specific verifiers.

**Key environments used:**
- **Answer Format Training**: Rewards correct output formatting (>150 formats) decoupled from semantic correctness
- **Instruction Following (RLVR-IFEval)**: Constraint-based instruction following with adaptive online curriculum
- **Internbootcamp**: 70K rejection-sampled trajectories from ~1,000 reasoning tasks, using DeepHermes for multi-trajectory generation
- **Schema Adherence**: Dynamic JSON schema generation/editing with programmatic Pydantic validation
- **Tool Use**: Agentic behavior training with `<tool_call>` tokens and programmatic validation

## Reasoning Length Control

A key challenge: the 14B model exceeded the 40,960-token context limit on 60% of LiveCodeBench evaluations. The solution: a **second SFT stage** that teaches the model to emit `</think>` at exactly 30,000 tokens.

**Approach:**
1. Generate reasoning traces from the current policy
2. Force-insert `</think>` at 30K tokens
3. Mask all tokens except `</think>` and `<eos>` — the model sees its own reasoning but only receives gradient on the termination decision
4. This avoids distribution collapse risks from training on full self-generated outputs

**Results (Hermes 4 14B):**

| Benchmark | Stage 1 | 30K-tuned | Overlong@40960 ↓ |
|-----------|---------|-----------|-------------------|
| AIME'24 | 55.0 | 55.4 (+0.7%) | 28.2% → 0.1% |
| LCBv6 | 28.6 | 42.5 (+48.6%) | 60.0% → 0.1% |
| GPQA Diamond | 57.4 | 60.2 (+4.7%) | 18.2% → 0.2% |

At most 3.9% relative performance reduction on reasoning for ≥98.9% reduction in overlong rates.

## Evaluation Results

### Hermes 4 405B vs. Comparable Models

| Benchmark | Hermes 4 405B R (N) | Cogito 405B R (N) | DeepSeek R1 671B | DeepSeek V3 671B | Qwen3 235B R (N) |
|-----------|---------------------|-------------------|-------------------|-------------------|-------------------|
| **AIME'24** | **81.9** (11.4) | 40.8 (17.7) | 86.5 | 50.6 | 78.2 (34.1) |
| **AIME'25** | **78.1** (10.6) | 32.7 (9.8) | 83.1 | 42.2 | 71.8 (25.1) |
| **GPQA Diamond** | 70.6 (39.4) | 68.2 (56.2) | 78.1 | 68.0 | 69.7 (57.7) |
| **LCBv6** | 61.4 (28.1) | 40.9 (32.2) | 71.8 | 49.2 | 65.1 (34.6) |
| **Arena-Hard v1** | **93.7** (53.5) | 91.0 (82.8) | 95.0 | 92.6 | 93.9 (91.7) |
| **EQBench3** | 85.5 (74.6) | 67.2 (69.5) | 86.5 | 83.1 | 80.0 (81.1) |
| **CreativeWriting3** | 79.3 (50.6) | 67.4 (67.9) | 80.3 | 76.7 | 77.5 (74.1) |
| **RefusalBench** | **57.1** (43.2) | 15.4 (12.1) | 16.7 | 28.1 | 34.3 (15.3) |

R = reasoning mode, N = non-reasoning mode. Hermes 4 leads open-weight models on AIME'24/25 (reasoning), Arena-Hard, and RefusalBench. Falls behind DeepSeek R1 on GPQA, LCBv6, and MMLU-Pro.

### Hermes 4 70B & 14B

Both smaller models show strong reasoning capabilities. Hermes 4 70B reaches AIME'24 73.5 (reasoning), GPQA Diamond 66.1, EQBench3 84.7 — competitive with much larger models. The 14B reaches AIME'24 55.4, significantly ahead of Qwen3-14B in non-reasoning mode (55.4 vs 28.5).

## Behavioral Characteristics

Hermes 4 exhibits **high behavioral plasticity** that distinguishes it from other large models:

- **Lower policy rigidity**: Unlike GPT-5 and Claude Opus 4.1 (which foreground safety disclaimers even in fictional prompts), Hermes 4 interprets fictional prompts as role-play and generates in-character responses
- **Template sensitivity**: Changing the chat template from `<assistant>` to `<me>` causes Hermes 4 to adopt a first-person, peer-like persona — a deeper shift than baseline models
- **Anti-sycophancy**: With explicit system-prompt instructions, Hermes 4's chain-of-thought traces show active steering away from deference
- **Stylistic transfer**: Strong capability in creative writing style emulation, avoiding both surface-level mimicry and near-verbatim pastiche

## Evaluation Infrastructure

Hermes 4's evaluation pipeline is notable for its engineering rigor:

- **OpenAI-compatible endpoint**: All benchmarks target the same inference instance, avoiding engine/version fragmentation
- **Atropos as eval framework**: Self-contained single-file evaluations, detailed sample-level logging, overlapped inference+scoring
- **Elastic inference cluster**: sglang-router with preemptible workers that auto-scale using available compute
- **Transparency**: All evaluation samples released on HuggingFace for reproducibility

## Related Pages

- [[nous-research]] — Developer organization
- [[hermes-agent]] — Nous Research's agent framework
- [[gepa]] — Genetic-Pareto Prompt Evolution (also by Nous Research)
- [[concepts/dataforge]] — Graph-based synthetic data generation
- [[concepts/atropos]] — RL environment manager
- [[concepts/hybrid-reasoning]] — Models combining reasoning + instruction-following
