---
title: "Multi-Objective Policy Distillation (MOPD)"
created: 2026-06-17
updated: 2026-06-17
type: concept
tags:
  - training
  - on-policy-distillation
  - fine-tuning
  - model-training
  - rlvr
  - reinforcement-learning
aliases:
  - MOPD
  - Multi-Teacher On-Policy Distillation
sources:
  - raw/articles/2026-05-04_multi-teacher-on-policy-distillation.md
  - raw/articles/2026-06-08_chinmaykarkar_opd-survey-2026.md
  - raw/articles/2026-06-16_interconnects_post-training-recipe-review.md
  - raw/articles/2026-04-23_xiaomi-mimo-v2.5-pro.md
  - raw/articles/2026-05-31_lukhuang_frontier-asynchronous-rl-solved.md
---

# Multi-Objective Policy Distillation (MOPD)

> **Multi-Objective Policy Distillation (MOPD)** is the dominant post-training recipe that emerged in 2026 for consolidating multiple domain-specialist teacher models into a single generalist student. It is the production-scale evolution of [[concepts/post-training/on-policy-distillation|on-policy distillation]] that solves the "see-saw problem" — where specializing a model in one domain (e.g., math reasoning) degrades performance in others (e.g., creative writing). For the architectural and implementation details of multi-teacher deployments, see [[concepts/multi-teacher-on-policy-distillation|Multi-Teacher On-Policy Distillation]].

MOPD was identified by **Finbarr Timbers** ([[entities/finbarr-timbers]]) and **Nathan Lambert** ([[entities/nathan-lambert]]) in their June 2026 post-training recipe review as the **key pattern** that distinguishes 2026 frontier models from earlier generations. The lineage runs: MiMo Flash V2 introduced the paradigm → DeepSeek V4 and Nemotron 3 Ultra scaled it to 10+ teachers.

---

## Overview

### What MOPD Is

MOPD is a post-training technique that:

1. **Trains N domain-specialist teachers** independently — each undergoes SFT then RL on its specific domain (math, code, agentic tasks, general chat), reaching its own performance ceiling without cross-domain interference.
2. **Samples trajectories from a single student model** — the student generates its own completions (on-policy rollouts), ensuring the distillation targets are drawn from the distribution the student actually encounters at inference time.
3. **Minimizes reverse-KL divergence to each teacher** — on each student rollout, the per-token loss pulls the student's output distribution toward the relevant teacher's distribution, creating dense, token-level supervision.
4. **Produces a unified generalist model** — the consolidated student matches or exceeds the specialist teachers on their respective domains while maintaining balanced performance across all objectives.

### Why It Matters

MOPD addresses the fundamental trade-off in post-training: **specialization vs. generalization**. Earlier post-training recipes (2022-2025) used a single pipeline — SFT → reward model → RL — that could improve a model broadly but struggled to push multiple capabilities simultaneously without them interfering. MOPD decomposes the problem:

- **Pre-2026 (InstructGPT through Llama 3 / Tülu 3):** One unified pipeline. SFT provides broad instruction following, DPO or RL adds preference alignment, and RL with verifiable rewards adds reasoning. Capabilities trade off against each other.
- **2026 (MOPD era):** Fragment into N independent specialist training runs, then consolidate via on-policy distillation. Each specialist reaches its domain ceiling independently; the consolidation step transfers capabilities without the interference that occurs when training jointly.

As [[entities/finbarr-timbers|Finbarr Timbers]] described in his June 2026 interview: "Recipes fragment into many specialist models merged back into one."

---

## Core Mechanism

### Reverse KL Divergence

MOPD uses **reverse KL divergence** (mode-seeking), which is the critical mathematical choice that distinguishes it from traditional distillation (forward KL, mean-seeking):

$$A_{i,t} = \text{sg} \left[ \log \frac{\pi_{\text{train}}(y_{i,t} | x, y_{i,<t}; \theta)}{\pi_{\text{infer}}(y_{i,t} | x, y_{i,<t}; \theta_{\text{teacher}})} \right]$$

Where:
- $\pi_{\text{train}}$ is the student (training) policy
- $\pi_{\text{infer}}$ is the teacher (inference) policy
- $\text{sg}$ denotes the stop-gradient operator
- The advantage $A_{i,t}$ replaces the group-mean advantage used in [[concepts/post-training/grpo|GRPO]]

**Why reverse KL (mode-seeking)?**

| Property | Forward KL (Mean-Seeking) | Reverse KL (Mode-Seeking) |
|----------|--------------------------|---------------------------|
| **Behavior** | Spreads student mass across ALL teacher modes | Concentrates student on teacher's DOMINANT modes |
| **Risk** | Produces unlikely/blended samples from low-probability modes | Safer — stays within high-probability regions |
| **Text Generation** | Can mix incompatible styles/strategies | Produces coherent, teacher-consistent output |
| **Use in MOPD** | Not used | Standard choice across all 2026 frontier models |

In the text generation context, reverse KL is safer because it avoids blending incompatible strategies from different teachers. The student concentrates on what each teacher does best rather than trying to average across all of a teacher's possible behaviors.

### Token-Level Supervision

Unlike standard RL (which provides only a single outcome reward per episode — ~O(1) bits of information), MOPD provides **dense, per-token supervision** via the teacher's log-probability distribution. This means:

- **~O(N) bits per episode** where N = number of tokens, compared to ~O(1) for outcome-based RL
- The model learns *which tokens* contributed to good behavior, not just *that* the outcome was good
- This dense signal is the key to MOPD's sample efficiency advantage

### Group Size = 1

Because the teacher provides the baseline directly (no need to estimate advantage from a group of samples), the **group size can be set to 1**, optimizing throughput. In contrast, [[concepts/post-training/grpo|GRPO]] typically requires sampling multiple completions per prompt (group size N > 1) to estimate reliable advantages.

---

## Student-Teacher Architecture

The MOPD architecture follows a **one-to-many** mapping during distillation:

```
                    ┌──────────────────┐
                    │   Math Teacher   │──┐
                    │  (SFT + Math RL) │  │
                    └──────────────────┘  │
                    ┌──────────────────┐  │    ┌─────────────────────┐
                    │  Code Teacher    │──┼───▶│   General Student   │
                    │ (SFT + Code RL)  │  │    │  (minimize reverse- │
                    └──────────────────┘  │    │   KL to each teacher│
                    ┌──────────────────┐  │    │   on its domain)    │
                    │ Agentic Teacher  │──┤    └─────────────────────┘
                    │ (SFT + Agent RL) │  │
                    └──────────────────┘  │
                    ┌──────────────────┐  │
                    │ General Teacher  │──┘
                    │  (SFT + Chat RL) │
                    └──────────────────┘
```

**The student generates its own trajectories on-policy**, and for each trajectory, the loss pulls the student's distribution toward the teacher that specializes in that domain. This is what makes it "multi-objective" — the student optimizes a set of domain-specific reverse-KL objectives simultaneously.

---

## Key Techniques

### IcePop (Logit Masking)

Training and inference engines (e.g., training with mixed precision vs. inference with quantization) often produce **slightly different logits**, creating numerical mismatch. **IcePop** mitigates this by masking updates where the probability ratio falls outside a tolerance band $[\alpha, \beta]$:

- If the student-teacher probability ratio is within $[\alpha, \beta]$: normal update
- If outside: the update is **masked** (set to zero), forgoing noisy updates where numerical mismatch is large

IcePop is used by GLM-5, Ring 1T, Intellect-3, and Nemotron-3 Super. It is a biased estimator (introduces bias by selectively dropping updates) but dramatically improves training stability at scale.

In the async RL context, IcePop also serves as an importance-sampling ratio control mechanism — see [[concepts/post-training/grpo-rl-training|GRPO infrastructure]].

### Full-Vocabulary Distillation (DeepSeek-V4)

Instead of estimating KL divergence on a single sampled token, DeepSeek-V4 uses the **full logit distribution** across the entire vocabulary for stability. This avoids the variance introduced by sampling a single token. To manage the massive memory load:

- **FP4 Quantization** for inference-only forward passes (teachers and reference model)
- **Metadata Decoupling** — separates lightweight planning data (sample IDs, lengths) from heavy per-token payloads (logits, hidden states), enabling efficient distributed processing

### Write-Ahead Log (WAL) for Fault Tolerance

Standard RL recovery from failures can cause **length bias** — short completions finish before interruption, while long ones get cut off and resampled, skewing the training distribution toward shorter sequences. DeepSeek-V4 uses a **Write-Ahead Log (WAL)**:

> "Whenever a new token is generated, it is immediately appended to the request's WAL… the system continues decoding from the persisted WAL and saved KV cache."

This ensures that even if a rollout is interrupted (node failure, preemption), it can resume from exactly where it left off, eliminating length bias and improving fault tolerance at massive scale.

---

## Model Adoption (2026 Frontier Models)

All major 2026 frontier models converged on MOPD, but each adopted it at a different stage with different teacher configurations:

| Feature | MiMo-V2-Flash | GLM-5 | Nemotron-Cascade 2 | DeepSeek-V4 |
|---------|---------------|-------|--------------------|-------------|
| **Stage** | Final (Consolidation) | Final (Recovery) | Intermediate (Stabilization) | Final (Scaling) |
| **Student Init** | General SFT | Post-RL checkpoint | Post-Multi-domain RL | Likely SFT |
| **Teacher Pool** | SFT, RL, & "Self" | Prior RL stage terminals | Math SFT, RLHF, Multi-domain | 10+ RL Specialists |
| **Advantage Type** | OPD + Outcome Reward | Pure OPD | Pure OPD | Pure OPD |
| **Domains** | General + Agentic | Reasoning → Agentic → General | Math + Instruction | 4 domains, 3 reasoning-effort modes |

### MiMo-V2-Flash: Capability Merging with Self-Distillation

[[entities/xiaomi|Xiaomi]]'s MiMo-V2-Flash (and the larger **MiMo-V2.5-Pro**, a 1.02T-parameter MoE model with 42B active parameters) uses MOPD as the final stage in a 3-stage post-training paradigm: SFT → Domain-Specialized Training → MOPD.

Key innovation: **Self-distillation** — using a frozen snapshot of the student itself as one of the teachers to prevent catastrophic drift. The advantage function interpolates OPD with an Outcome Reward Model (ORM):

$$A_{i,t} = A_{i,t}^{\text{OPD}} + \alpha \cdot A_{i,t}^{\text{ORM}}$$

This allows the student to **exceed teacher performance** on certain metrics by incorporating outcome-based reward signals alongside the distillation signal.

MiMo-V2.5-Pro achieves SWE-bench Pro scores comparable to Claude Opus 4.6 and a GDPVal-AA Elo of 1581, surpassing Kimi K2.6 and GLM 5.1.

### GLM-5: Capability Recovery

Zhipu AI's GLM-5 uses MOPD to **recover performance lost during sequential RL stages**. The pipeline trains Reasoning → Agentic → General RL sequentially, and each stage can degrade capabilities from prior stages. MOPD at the final stage re-anchors the model to prior RL stage terminals, recovering lost capabilities.

### Nemotron-Cascade 2: Mid-Pipeline Stabilization

Nvidia's Nemotron-Cascade 2 uses MOPD as an intermediate **"re-anchor"** step — periodically running MOPD during instruction-following RL to prevent math reasoning decay. They found MOPD was **significantly more sample-efficient than GRPO** for this stabilization purpose.

### DeepSeek-V4: Massive-Scale Consolidation

DeepSeek-V4 represents the most ambitious MOPD deployment, distilling from **10+ RL specialist teachers** across 4 domains and 3 reasoning-effort modes:
- **Non-think**: Fast, straightforward responses
- **Think High**: Moderate reasoning depth
- **Think Max**: Maximum reasoning effort for hard problems

This produces a single model that can modulate its reasoning effort based on the prompt, covering a wide Pareto frontier of speed vs. accuracy trade-offs.

---

## Variants

MOPD sits within a broader family of on-policy distillation techniques. Chinmay Karkar's June 2026 survey (~40 papers) established a taxonomy of OPD variants:

### On-Policy Self-Distillation (OPSD)

**OPSD** removes the external teacher entirely — the student supervises itself using privileged context (e.g., ground-truth answers, retrieved skills, or environment feedback). Key variants:

- **SDFT** (Shenfeld et al., 2026): Student + expert demonstration as privileged context
- **SDPO** (Zhao et al., 2026): Student + ground-truth answer for math reasoning
- **SDAR** (Lu et al., 2026): Student + retrieved skills for multi-turn agent tasks, with a sigmoid gate for asymmetric trust
- **RMSD** (Applied Compute): Filtered loss mask for out-of-distribution tasks in production

See [[concepts/post-training/on-policy-self-distillation|On-Policy Self-Distillation]] for the foundational OPSD technique.

### Cross-Tokenizer OPD

Standard OPD/MOPD requires the teacher and student to share the same tokenizer (for per-token log-probability comparison). This limits distillation to same-family model pairs. Cross-tokenizer OPD techniques attempt to bridge this gap:

- **ULD** (Universal Logit Distillation)
- **DSKD** (Dual-Space Knowledge Distillation)
- **GOLD** (Generalized On-policy Logit Distillation)
- **CTPD** (Cross-Tokenizer Policy Distillation)

These remain active research areas as of mid-2026.

### Black-Box Distillation

An emerging frontier: distilling from **API-only teachers** where logits are not accessible. Instead of matching token-level distributions, the student learns from the teacher's generated text (sequence-level). This is relevant for cases where the best teacher models are only available behind APIs and output only generated text, not log-probabilities.

### MOPD vs. MIMO

The **MIMO** (Multi-Input Multi-Output) framework proposed multi-expert pipelines with independent domain specialists consolidated via OPD — this was the conceptual precursor to MOPD. MOPD generalizes this by allowing any number of teachers across any number of objectives, with the student optimizing a weighted combination of reverse-KL objectives.

---

## Related Concepts

### Relationship to GRPO

MOPD can be understood as a modification of [[concepts/post-training/grpo|GRPO]] where the group-mean advantage is replaced by a teacher-derived, token-level advantage. The training loop structure (sample → compute advantage → update policy) is identical; only the advantage computation differs. See [[concepts/post-training/grpo-rl-training|GRPO training]] for the underlying RL framework.

### Relationship to RLHF and DPO

MOPD is complementary to, not a replacement for, [[concepts/post-training/rlhf|RLHF]] and [[concepts/post-training/rlhf-dpo-preference|DPO]]:

| Method | Supervision | When Used |
|--------|-------------|-----------|
| **RLHF / DPO** | Human preferences (pairwise) | Early alignment stage — teaches values, style, harmlessness |
| **RLVR** | Verifiable rewards (math, code) | Specialist training — pushes domain-specific capability ceilings |
| **MOPD** | Teacher distributions (multi-domain) | Consolidation — merges specialists without cross-domain interference |

The 2026 post-training stack is: SFT → DPO/RLHF → Specialist RL (with RLVR) → MOPD → Unified Model.

### Relationship to Model Distillation

MOPD is a specific form of [[concepts/model-distillation|model distillation]] distinguished by:
- **On-policy**: Student generates its own trajectories (not teacher-generated data)
- **Multi-teacher**: N specialists → 1 generalist (not 1:1)
- **Reverse KL**: Mode-seeking divergence (not forward KL or cross-entropy)
- **Token-level**: Dense per-token supervision (not sequence-level)

### Async RL Context

MOPD training benefits from **asynchronous RL** infrastructure, which decouples rollout generation from policy updates for 2-3x throughput gains. However, async RL introduces policy lag (stale trajectories) that must be managed with importance-sampling ratio controls like IcePop. See Luke Huang's May 2026 survey on [[concepts/post-training/grpo-rl-training|async RL]] for the algorithmic and systems fixes used by frontier labs.

---

## References

1. "Multi-Teacher On-Policy Distillation (MOPD): A New Post-Training Primitive" — Yumoxu Notion, May 2026. Source: `raw/articles/2026-05-04_multi-teacher-on-policy-distillation.md`
2. "The Imitation Game: State of Policy Distillation in Language Model Training" — Chinmay Karkar, June 2026. Source: `raw/articles/2026-06-08_chinmaykarkar_opd-survey-2026.md`
3. "Frontier Post-Training Recipe Review with Finbarr Timbers" — Nathan Lambert, Interconnects #18, June 2026. Source: `raw/articles/2026-06-16_interconnects_post-training-recipe-review.md`
4. "MiMo-V2.5-Pro — Xiaomi's Trillion-Parameter Open-Source Agent Model" — Xiaomi, April 2026. Source: `raw/articles/2026-04-23_xiaomi-mimo-v2.5-pro.md`
5. "Is Frontier Asynchronous RL Solved?" — Luke J. Huang, May 2026. Source: `raw/articles/2026-05-31_lukhuang_frontier-asynchronous-rl-solved.md`

## See Also

- [[concepts/multi-teacher-on-policy-distillation]] — Detailed architecture and implementation of multi-teacher OPD
- [[concepts/post-training/on-policy-distillation]] — Foundational single-teacher OPD technique (Thinking Machines Lab, Oct 2025)
- [[concepts/post-training/on-policy-self-distillation]] — OPSD: self-distillation without external teachers
- [[concepts/model-distillation]] — Broader category of distillation techniques
- [[concepts/post-training/grpo]] — GRPO, the RL framework underlying MOPD's training loop
- [[concepts/post-training/rlhf]] — RLHF, the earlier preference-based alignment paradigm
- [[entities/nathan-lambert]] — Host of Interconnects podcast, post-training recipe analysis
- [[entities/finbarr-timbers]] — Identified MOPD as the key 2026 post-training pattern
