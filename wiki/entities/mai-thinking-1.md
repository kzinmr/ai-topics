---
title: "MAI-Thinking-1"
type: entity
created: 2026-06-21
updated: 2026-07-10
tags:
  - microsoft
  - model
  - reasoning-model
  - training
  - optimization
  - mixture-of-experts
  - grpo
related:
  - [[entities/microsoft]]
  - [[concepts/mai-thinking-1-tech-report]]
  - [[concepts/mixture-of-experts]]
  - [[concepts/post-training/grpo]]
sources:
  - [MAI-Thinking-1: Building a Hill-Climbing Machine](https://microsoft.ai/wp-content/uploads/2026/06/main_20260602_2.pdf)
  - raw/articles/2026-06-03_microsoft-mai-thinking-1-tech-report.md
---

# MAI-Thinking-1

**MAI-Thinking-1** is a powerful reasoning model developed from scratch by Microsoft AI (MAI). It is a 35B active / 1T total parameter Mixture of Experts (MoE) model, trained on 30T tokens of clean enterprise-grade data without distillation from third-party models.

## Key Innovations
- **Hill-Climbing Machine**: The development treats model creation as a system-level optimization problem, using iterative improvements for rapid scaling.
- **From-scratch Training**: Trained on 30T tokens of clean, enterprise-grade data without synthetic distillation.
- **Reinforcement Learning (RL) Climb**: A robust RL recipe for sustained log-linear performance improvement, leveraging chains of thought (CoT) and tool use.
- **Specialist Models**: The process produced three models for STEM reasoning, agentic coding/tool use, and helpfulness/safety.

## Architecture

### Attention
- **Periodic local/global**: 5 local attention layers + 1 global (Gemma 3 pattern)
- **Local**: Sliding window attention, window=512, RoPE base=10,000
- **Global**: No positional encoding (NoPE) — comparable to RoPE, more efficient
- **GQA**: 8 KV heads, 128-dim per head
- **QK Norm**: RMSNorm on queries and keys
- **FlashAttention-4** + Ulysses-style context parallelism

### MoE Feed-Forward
- **Interleaved dense/MoE**: Alternating layers (first FFN is dense), not every-layer-MoE
- **SwiGLU** activation for both dense and MoE FFN
- **LatentMoE** (NVIDIA): Shared down-projection before all-to-all dispatch, routing on original representation
- **8 of 512 experts** routed per token with softmax gating
- **No shared expert**: Adding shared experts to interleaved layout has "little or no benefit"
- **Dropless MoE**: Variable message size for all-to-all, bounded memory under high imbalance
- **Global-batch load balancing**: Empirical frequencies aggregated across data-parallel workers AND microbatches

### Model Specifications

| Spec | Value |
|------|-------|
| Total parameters | 962B (MoE, ~1T family) |
| Active parameters | 34.7B |
| Layers | 78 |
| Hidden dim | 6,656 |
| FFN dim | 13,312 (dense), 10,240 (expert) |
| Experts | 512 total, top-8 routed |
| KV/Q heads | 8/80 |
| Training tokens | 33.5T total (30T pre-training + 3.55T mid-training) |
| Max context | 256K |
| Tokenizer | o200k_base (OpenAI, 200K vocab) |

### Scaling Ladder

Architecture family varies only model depth; all other dimensions derived via heuristic `hidden_size = L * 256/3`:

| Model | Active | Total | Layers |
|-------|--------|-------|--------|
| L12 | 365M | 3.9B | 12 |
| L18 | 760M | 13B | 18 |
| L30 | 2.6B | 58B | 30 |
| L42 | 6.1B | 159B | 42 |
| L66 | 21.7B | 615B | 66 |
| L78 (MAI-Base-1) | 34.7B | 962B | 78 |

## Performance

### STEM & Agentic Coding

| Benchmark | MAI-Thinking-1 | Sonnet 4.6 | Opus 4.6 |
|-----------|---------------|------------|----------|
| SWE-Bench Pro | **52.8%** | -- | competitive |
| AIME 2025 | **97.0%** | beaten | -- |
| AIME 2026 | **94.5%** | -- | -- |
| LiveCodeBench v6 | **87.7%** | -- | -- |
| SWE-Bench Verified | competitive | -- | -- |

### General Capabilities

| Benchmark | MAI-Thinking-1 | Sonnet 4.6 |
|-----------|---------------|------------|
| MMLU Pro | 85 | 87 |
| SimpleQA Verified | 31 | 29 |
| IF Bench | 69 | 50 |
| Advanced IF | 85 | 86 |
| Multi-Challenge | 53 | 57 |
| BFCL v3 | 72 | 76 |
| HealthBench | 35 | 38 |

### Human Side-by-Side (1,276 tasks)

| Comparison | Win | Tie | Loss |
|-----------|-----|-----|------|
| vs Sonnet 4.6 | 49% | 6% | 45% |
| vs Opus 4.6 | 43% | 5% | 52% |

## Key Ideas
- **Hill-Climbing Machine**: Treating model development as an iterative, system-level optimization problem.
- **Reinforcement Learning (RL)**: Using a robust RL recipe to achieve sustained log-linear performance improvements.
- **From-Scratch Training**: Utilizing clean, enterprise-grade data without distillation from third-party models.
- **STEM Reasoning**: High performance on benchmarks like AIME 2025 and SWE-Bench Pro.

## Reinforcement Learning: Modified GRPO

The most distinctive design choice: **zero synthetic data means no cold start phase**. Capabilities emerge purely from RL on the base model.

Based on GRPO (Shao et al., 2024) with token-level policy gradient, with two key modifications:

- **Adaptive entropy control**: Dynamically adjusts upper clip bound to maintain target entropy H*=0.3 using an integral controller; initializes k=0 (symmetric clipping)
- **Outer ratio clip**: Hard outer clip on ALL branches to prevent catastrophic gradient-norm spikes (r_out = clip(r_i,t, r_min, r_max))

**Reward decomposition**: R(q, y_i) = R_task(q, y_i) + w_lang * R_lang(y_i) - w_len * R_len(y_i), with task reward domain-dependent (code execution, AI judge, or trained RM), language consistency penalty, and length penalty weighted by problem difficulty.

**Sampling strategy**: Two-stage pass-rate filtering; top-p sampling for rollouts; self-distillation cycles (RL -> self-distillation SFT -> RL).

## Training Infrastructure
- **YOLO Framework**: MAI's in-house "You Only Launch Once" distributed training framework built on PyTorch, supporting pre-training, mid-training, and RL phases with custom kernels, parallelism, and fault-tolerance.
- **Cluster**: 8K GB200 GPUs, single logical cluster, one site (Phoenix, AZ)
- **Goodput**: 90.0% at 8K GPUs — primary production KPI
- **Total overhead**: 51 hours (recomputation: 6.5h, non-stepping: 14h, MFU drop: 18h)
- **Determinism**: First-class infrastructure property; eliminates silent data corruption
- **Serving**: SGLang
- **Inference hardware**: MAIA-200 (Microsoft custom silicon) — 40% higher token generation throughput per Watt vs GB200

## Safety & Red Teaming

### Internal Safety Evaluation
The report describes a comprehensive internal safety evaluation framework:

**Over-refusal measurement**: An internal benchmark measures over-refusal on low-risk requests, flagging refusals, hedging, or unwarranted partial refusals. Paired with safety pass rates on high-sensitivity items, this surfaces safer behavior on high-risk requests and more helpful behavior on benign ones. Across five of eight evaluated categories, MAI-Thinking-1 outperformed Sonnet 4.6 on this safety-helpfulness balance, with the largest gains in Chemical/Biological/Radiological/Nuclear (CBRN), Self Harm, and Elections & Politics.

**Jailbreak evaluation**: ~9.5K jailbreak prompts built from 2.5K unique seed scenarios (vendors, internal red-teaming, HarmBench, StrongREJECT). Categorized into three buckets:
- **Foundational Techniques**: single-step transformations (jailbreak wrappers, prompt templates)
- **Compositional Techniques**: multiple transformations or structured rewrites (PyRIT, PAP-style, multilingual)
- **Adaptive Techniques**: interaction, search, or multi-turn structure (TAP, multi-turn attacks)

MAI-Thinking-1 achieved attack success rates (ASR) comparable with Sonnet 4.6 and Opus 4.6 across all three buckets.

### Internal Red Teaming
Conducted by MAI red teamers (safety researchers + recruited external annotators) throughout model development. Across top-priority remediation categories identified during red teaming, aggregate attack success fell ~22% from pre-mitigation to final candidate, with ~44% reduction in jailbreak success, ~43% in hate/fairness issues, ~30% in child safety, and ~20% in mental health attacks.

### Independent Red Teaming
Additional red-teaming by Microsoft's AI Red Team (AIRT) and third-party vendors, focused on areas where static evaluations are weakest: automated adversarial attack methods, code/cyber-misuse safety, psychosocial harms, and multilingual coverage.

- **TAP (Tree of Attacks with Pruning)** was surfaced as a robustness gap. Microsoft built a closed-loop adversarial data pipeline (broad scenario generation → attack-transformation templates → TAP-style adaptive refinement → model-specific failures) that produced a large reduction in TAP jailbreak susceptibility, bringing the model to parity with state-of-the-art models.
- **Low-resource language framing**: Content reliably refused in English was elicited in Yoruba, Telugu, Amharic, Burmese, Khmer, and Malay. Microsoft responded by expanding safety training data with multilingual adversarial seeds, translating high-yield English attack patterns into affected languages. Multilingual robustness in lower-resource languages remains an area of continued investment.

## Sources
- [MAI-Thinking-1: Building a Hill-Climbing Machine — Microsoft AI Technical Report](https://microsoft.ai/wp-content/uploads/2026/06/main_20260602_2.pdf)
- raw/articles/2026-06-03_microsoft-mai-thinking-1-tech-report.md
