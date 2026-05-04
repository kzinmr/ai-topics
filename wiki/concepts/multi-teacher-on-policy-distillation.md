---
title: "Multi-Teacher On-Policy Distillation (MOPD)"
type: concept
created: 2026-05-04
updated: 2026-05-04
tags:
  - concept
  - distillation
  - post-training
  - reinforcement-learning
  - grpo
  - on-policy
aliases:
  - MOPD
  - On-Policy Distillation
  - OPD
  - Multi-Teacher Distillation
related: [[grpo-rl-training]], [[model-distillation]], [[reinforcement-fine-tuning]], [[rlhf]]
sources:
  - raw/articles/2026-05-04_multi-teacher-on-policy-distillation.md
  - https://yumoxu.notion.site/multi-teacher-on-policy-distillation
---

# Multi-Teacher On-Policy Distillation (MOPD)

**Multi-Teacher On-Policy Distillation (MOPD)** is a post-training primitive that emerged in 2026 as the standard solution to the *"see-saw problem"* in LLM post-training — where specializing in one area (e.g., Math RL) degrades performance in others (e.g., open-ended writing). It samples trajectories from the student model and matches one or more teacher distributions via **reverse KL divergence**, providing dense, token-level supervision within a GRPO-like training loop.

## Core Concept: From GRPO to OPD

### The Mathematical Shift
In standard [[grpo-rl-training|GRPO]], the advantage $A_{i,t}$ is calculated relative to a group mean. In **On-Policy Distillation (OPD)**, the advantage is replaced by the log-ratio between student and teacher:

$$A_{i,t} = \text{sg} \left[ \log \frac{\pi_{\text{train}}(y_{i,t} | x, y_{i,<t}; \theta)}{\pi_{\text{infer}}(y_{i,t} | x, y_{i,<t}; \theta_{\text{teacher}})} \right]$$

- **Reverse KL** is **mode-seeking**: while forward KL (mean-seeking) spreads student mass across all teacher modes, reverse KL concentrates the student on the teacher's dominant modes, making it safer for complex text generation.
- **Efficiency**: Because the teacher provides the baseline, group size can be set to 1, optimizing throughput.

### IcePop
Training and inference engines often produce slightly different logits. **IcePop** mitigates this by masking updates where the probability ratio falls outside a tolerance band $[\alpha, \beta]$ — forgoing noisy updates where mismatch is large.

## Comparison with Related Techniques

| Aspect | GRPO | OPD | RFT |
|--------|------|-----|-----|
| **Advantage Source** | Group mean baseline | Teacher-student log-ratio | LLM-as-Judge score |
| **Supervision** | Reward model | Teacher distribution | Production traces |
| **Group Size** | N (multiple samples) | 1 (single sample) | N/A |
| **KL Direction** | N/A | Reverse KL (mode-seeking) | N/A |
| **Primary Use** | Reasoning improvement | Capability consolidation / recovery | Behavioral tuning from traces |

## 2026 Frontier Model Implementations

All four major 2026 frontier models converged on MOPD using different strategies:

| Feature | MiMo-V2-Flash | GLM-5 | Nemotron-Cascade 2 | DeepSeek-V4 |
|---------|---------------|-------|--------------------|-------------|
| **Stage** | Final (Consolidation) | Final (Recovery) | Intermediate (Stabilization) | Final (Scaling) |
| **Student Init** | General SFT | Post-RL checkpoint | Post-Multi-domain RL | Likely SFT |
| **Teacher Pool** | SFT, RL, & "Self" | Prior RL stage terminals | Math SFT, RLHF, Multi-domain | 10+ RL Specialists |
| **Advantage** | OPD + Outcome Reward | Pure OPD | Pure OPD | Pure OPD |

### Key Model Insights

- **MiMo-V2-Flash (Capability Merging):** Uses "Self-distillation" (a snapshot of the student) to prevent catastrophic drift. Interpolates OPD with an **Outcome Reward Model (ORM)** to exceed teacher performance: $A_{i,t} = A_{i,t}^{\text{OPD}} + \alpha A_{i,t}^{\text{ORM}}$
- **GLM-5 (Capability Recovery):** Focuses on recovering performance lost during sequential RL stages (Reasoning → Agentic → General)
- **Nemotron-Cascade 2 (Mid-pipeline Reset):** Uses MOPD as a periodic "re-anchor" to prevent math reasoning decay during instruction-following RL. Found MOPD significantly more sample-efficient than GRPO
- **DeepSeek-V4 (Massive Scale):** Distills from 10+ teachers across 4 domains and 3 "reasoning-effort" modes (Non-think, Think High, Think Max)

## Engineering & Infrastructure (DeepSeek-V4)

### Full-Vocabulary Distillation
Instead of estimating KL on a single sampled token, DeepSeek uses the full logit distribution for stability. To manage the massive memory load:
- **FP4 Quantization** for inference-only forward passes (teachers/reference)
- **Metadata Decoupling** — separates lightweight planning data from heavy per-token payloads

### Fault-Tolerant Rollouts with WAL
Standard RL recovery causes **length bias** (short completions finish, long ones get interrupted and resampled). DeepSeek uses a **Write-Ahead Log (WAL)**:
> "Whenever a new token is generated, it is immediately appended to the request's WAL… the system continues decoding from the persisted WAL and saved KV cache."

## Trends & Future Directions

- **Convergence:** All frontier models use reverse KL on student rollouts + multi-teacher frameworks + IcePop for stability
- **Divergence:** *When* to apply MOPD (end vs. middle) and *what* teachers (SFT vs. RL specialists)
- **Future:** **Black-box distillation** (API-only teachers) and **Teacher-student co-evolution** (iterative loops where student becomes next generation's teacher)

## Related Concepts
- [[grpo-rl-training]] — the RL framework OPD evolved from
- [[model-distillation]] — broader category of distillation techniques
- [[reinforcement-fine-tuning]] — alternative post-training approach using production traces
- [[rlhf]] — earlier preference-based alignment paradigm
