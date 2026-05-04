---
title: "Multi-Teacher On-Policy Distillation (MOPD): A New Post-Training Primitive"
source: Notion (yumoxu)
author: Unknown
date: 2026-05-04
url: https://yumoxu.notion.site/multi-teacher-on-policy-distillation
tags: [distillation, post-training, llm-training, grpo, reverse-kl]
---

# Multi-Teacher On-Policy Distillation (MOPD): A New Post-Training Primitive

## Core Concept: From GRPO to OPD

On-policy distillation (OPD) samples trajectories from the student model and matches a teacher's distribution via **reverse KL divergence**. This provides dense, token-level supervision within a training loop similar to Group Relative Policy Optimization (GRPO).

### The Mathematical Shift
In standard GRPO, the advantage $A_{i,t}$ is calculated relative to a group mean. In OPD, the advantage is replaced by the log-ratio between student and teacher:

$$A_{i,t} = \text{sg} \left[ \log \frac{\pi_{\text{train}}(y_{i,t} | x, y_{i,<t}; \theta)}{\pi_{\text{infer}}(y_{i,t} | x, y_{i,<t}; \theta_{\text{teacher}})} \right]$$

- **Why Reverse KL?** It is **mode-seeking**. While forward KL (mean-seeking) spreads student mass across all teacher modes (often leading to unlikely samples), reverse KL concentrates the student on the teacher's dominant modes, making it safer for complex text generation.
- **Efficiency:** Because the teacher provides the baseline, group size can be set to 1, optimizing throughput.

### IcePop
Training and inference engines often produce slightly different logits. **IcePop** mitigates this by masking updates where the probability ratio falls outside a tolerance band $[\alpha, \beta]$:
> "This forgoes all noisy updates in cases where the mismatch is large."

## Comparison of 2026 Frontier Models

| Feature | MiMo-V2-Flash | GLM-5 | Nemotron-Cascade 2 | DeepSeek-V4 |
|---------|---------------|-------|--------------------|-------------|
| **Stage** | Final (Consolidation) | Final (Recovery) | Intermediate (Stabilization) | Final (Scaling) |
| **Student Init** | General SFT | Post-RL checkpoint | Post-Multi-domain RL | Likely SFT |
| **Teacher Pool** | SFT, RL, & "Self" | Prior RL stage terminals | Math SFT, RLHF, Multi-domain | 10+ RL Specialists |
| **Advantage** | OPD + Outcome Reward | Pure OPD | Pure OPD | Pure OPD |

### Key Model Insights
- **MiMo-V2-Flash (Capability Merging):** Uses "Self-distillation" (a snapshot of the student) to prevent catastrophic drift. Interpolates OPD with an **Outcome Reward Model (ORM)** to exceed teacher performance.
- **GLM-5 (Capability Recovery):** Focuses on recovering performance lost during sequential RL stages (Reasoning → Agentic → General).
- **Nemotron-Cascade 2 (Mid-pipeline Reset):** Uses MOPD as a periodic "re-anchor" to prevent math reasoning decay during instruction-following RL. MOPD was significantly more sample-efficient than GRPO.
- **DeepSeek-V4 (Massive Scale):** Distills from 10+ teachers across 4 domains and 3 "reasoning-effort" modes (Non-think, Think High, Think Max).

## Engineering & Infrastructure (DeepSeek-V4)

### Full-Vocabulary Distillation
Instead of estimating KL on a single sampled token, DeepSeek uses the full logit distribution for stability. To manage the massive memory load:
- **FP4 Quantization:** Used for inference-only forward passes (teachers/reference).
- **Metadata Decoupling:** Separates lightweight planning data (sample IDs, lengths) from heavy per-token payloads (logits, hidden states).

### Fault-Tolerant Rollouts (WAL)
Standard RL recovery can cause **length bias** (short completions finish; long ones get interrupted and resampled). DeepSeek uses a **Write-Ahead Log (WAL)**:
> "Whenever a new token is generated, it is immediately appended to the request's WAL… the system continues decoding from the persisted WAL and saved KV cache."

## Summary of Trends
- **Convergence:** All models use reverse KL on student rollouts and multi-teacher frameworks. Most use IcePop for stability.
- **Divergence:** Models differ on *when* to apply MOPD (end vs. middle of pipeline) and *what* teachers to use (SFT vs. RL specialists).
- **Future Directions:** Research moving toward **Black-box distillation** (API-only teachers) and **Teacher-student co-evolution** (iterative loops).
