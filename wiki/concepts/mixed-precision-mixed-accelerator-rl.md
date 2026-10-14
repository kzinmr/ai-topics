---
title: Mixed-precision, mixed-accelerator RL
created: 2026-10-14
updated: 2026-10-14
type: concept
confidence: medium
tags: [inference, training, open-weight, agent-infrastructure]
sources:
  - raw/articles/2026-10-14_modal-mixed-precision-mixed-accelerator-rl.md
related:
  - on-policy-vs-off-policy-rl
  - grpo-rl-training
  - sglang
  - nvfp4-4bit-floating-point
  - fp8-training
  - serverless-gpu-inference
  - mimo-v2-6-scaling-rl-self-improvement
aliases:
  - Mixed samplers
  - Mixed-precision RL
  - Mixed-accelerator RL
  - Mixed sampler RL
---

# Mixed-precision, mixed-accelerator RL

**Mixed-precision, mixed-accelerator RL** (Modal's term: "mixed samplers") is the idea of
running RL **rollout/sampling** on *different* precisions (FP8, NVFP4, BF16) and *different*
accelerators than the trainer — instead of matching the trainer exactly — and absorbing the
resulting training–inference mismatch with off-policy correction. The goal is to bring the same
speed/cost optimizations used in ordinary model serving (cheap quantization, co-designed
kernels, accelerators specialized for long-context prefill) into the RL loop, where **sampling
already consumes 80–85% of the GPUs** in large runs.

Introduced by Modal (2026-10-13) in *"Toward RL on mixed-precision, mixed-accelerator
samplers."*

## The two problems

1. **Learning.** Each serving optimization adds train–inference mismatch, making samples more
   **off-policy** and destabilizing training. The fix is **off-policy correction**, which makes
   no assumption about *why* the policies differ, so it applies equally to different precisions
   or accelerators (as in stale-sample async training). See
   [on-policy-vs-off-policy-rl](on-policy-vs-off-policy-rl.md).
2. **System.** RL infra is usually built around **homogeneous accelerator clusters**; mixed
   samplers need autoscaling accelerators that burst and run their own kernels. Modal solves
   this with **serverless GPUs** (see [serverless-gpu-inference](serverless-gpu-inference.md)).

## How they made it stable (Modal's demo)

Setup: train **Qwen3.6-35B-A3B** (open-weight MoE) on agentic coding up to **256K tokens** of
context over Xiaomi's **2.7K repository tasks** (MiMo-V2.6 release, traces removed); reward = 1
if the patch passes tests in a fresh sandbox. **Miles** RL framework, **SGLang** samplers,
**Megatron-LM** trainer updating in BF16 on B200s; **fully async, no staleness limit**; eval on
**SWE-bench Pro V2** (BF16 checkpoints).

Samplers span **six accelerator kinds** — B200/B300 serve **NVFP4**; H100/H200 serve **FP8 and
BF16**; A100/RTX PRO 6000 serve **BF16**; each runs its own kernels and keeps **KV cache in
FP8**. The trainer (BF16) does not replay the samplers' MoE routing decisions.

Starting from **GRPO** with no correction, three pieces make it stable:

1. **Masked importance sampling (MIS)** — multiply each token term by its importance ratio and
   **mask** tokens whose ratio leaves a fixed range, keeping every ratio bounded so a few rare,
   huge-ratio tokens can't dominate the update.
2. **Score centering (SC)** — subtract, per position, the expected log-prob gradient under the
   sampling policy, so in expectation only advantage differences move the policy (removes drift).
3. **Top-p sampling + mask replay** — samplers draw each token only from the top-p candidate set
   (rare extreme-ratio tokens never enter the data); the trainer renormalizes over the same set,
   so both policies share the same support.

## Why it matters / open questions

If RL can run its dominant cost (sampling) on cheap quantized, heterogeneous, bursty GPUs while
staying stable, the **unit cost of agentic-RL training drops substantially** — a lever distinct
from the algorithmic scaling story (see
[mimo-v2-6-scaling-rl-self-improvement](mimo-v2-6-scaling-rl-self-improvement.md)). Open
questions: how well MIS/SC/top-p replay generalize beyond one model family and one benchmark;
whether NVFP4 sampler drift grows on harder/longer tasks; and how much of the win is
Modal-specific serverless elasticity vs. the correction math. Single-source, one model, one
eval suite → `confidence: medium`.

## Sources

- [Toward RL on mixed-precision, mixed-accelerator samplers — Modal](https://modal.com/blog/toward-rl-on-mixed-precision-mixed-accelerator-samplers)
- Raw: `raw/articles/2026-10-14_modal-mixed-precision-mixed-accelerator-rl.md`
