---
title: "MoE Training Methodology (Noumena)"
created: 2026-05-08
updated: 2026-05-08
type: concept
tags: [moe, training, methodology, speedrun, evaluation, infrastructure, fp8]
sources: [raw/articles/2026-03-14_noumena-research-12-posts.md]
---

# MoE Training Methodology (Noumena Research Program)

Synthesis of Noumena Network's 12 research posts on Mixture-of-Experts training methodology, published March 14, 2026. These posts document a coherent research program built around the **speedrun loop** as the core instrument for architecture research.

## Core Philosophy

Noumena's approach is built on three principles:
1. **Small-model speedruns** are the fastest honest instrument for architecture research
2. **Downstream evaluation** (not just training loss) must gate all decisions
3. **Reproducibility is the experiment** — a production-grade system validates findings

## The Speedrun Loop

The central methodology: train small MoE models rapidly as probes, validate hypotheses, then scale what works.

- **Eval-gated**: Configuration search is guided by downstream task evaluation, not just loss curves
- **Canonical lane**: Standardized fp8 training path on B200 hardware for reproducible comparisons
- **Autoresearch**: "Let the Speedrun Search Itself" — automated hyperparameter exploration gated by eval scores

### Why Speedruns Work

- Fast iteration: hours instead of weeks
- Honest signal: small models reveal architecture effects without confounding scale factors
- Reproducible: standardized configs in `configs/speedrun/` produce comparable leaderboard entries

## Key Findings

### 1. MoE Training Has Unique Failure Modes

"Why Training MoEs is So Hard" identifies three failure modes qualitatively different from dense training:
- **Load imbalance**: Uneven token distribution across experts
- **Routing collapse**: Experts becoming under-specialized or unused
- **Optimization instability**: Expert parameters diverging or collapsing

### 2. Routing Collapse ≠ Quality Collapse

**Super-4096** finding: Loss keeps improving while routing collapses under extreme sparsity. This counter-intuitive result suggests that routing degradation and model quality can decouple — a model can get better even as expert utilization patterns degrade.

### 3. Per-Expert Learning Rates Matter

"Do MoE Experts Need Different Learning Rates?" revisits Moonlet's old 15x expert-LR rule, finding it overshoots in bf16 AdamW. This implies:
- Expert learning rate tuning is precision-dependent
- Rules of thumb from fp8 don't transfer to bf16
- Automated per-expert LR search may be necessary

### 4. FP8/FP4 Precision Dynamics

**NVFP4 Dynamics** documents the gap between NVFP4 and BF16 training recipes, and what closed it. Key insight: lower-precision formats require different optimization recipes — you can't just swap the dtype.

### 5. Measurement Beyond Loss

"Make It Measurable" and "The Atlas Hypothesis" argue that training loss alone is insufficient for MoE evaluation:
- Output-only dashboards can't name what pretraining built
- Need metrics for expert utilization, routing entropy, load balance
- Downstream eval is the ultimate truth signal

### 6. Dense-vs-MoE Comparisons Need a Fairness Contract

"What Are We Holding Fixed?" demonstrates that dense vs. MoE comparisons are meaningless without explicit agreement on what's held constant (compute, parameters, FLOPs, training tokens). A failed transfer experiment exposed the hidden assumptions in standard comparison frameworks.

### 7. Polysemy in MoE Experts

"Reproducing Canon, mHC, and Engram" documents failed reproduction attempts and one real polysemy failure — where an expert encodes multiple unrelated concepts. This challenges the assumption that MoE experts naturally specialize into clean, interpretable sub-functions.

## RDEP: Systems Innovation

**RDEP** (Research Dispatch/Expert Parallelism) replaces NCCL all-to-all with direct CUDA IPC dispatch/return for single-node MoE training. See [[concepts/rdep]] for full details.

## Related Pages

- [[entities/noumena-network]] — Noumena entity
- [[concepts/rdep]] — RDEP expert parallelism
- [[concepts/mixture-of-experts]] — General MoE concept
- [[concepts/speedrun]] — Speedrun methodology (if exists)
