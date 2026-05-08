---
title: "Noumena Network Research — 12 Posts on MoE Training Methodology"
url: https://noumena.com/research/
date: 2026-03-14
source: noumena
type: research-collection
tags: [moe, training, infrastructure, methodology, speedrun, rdep, fp8, nvfp4]
---

# Noumena Network Research Collection

> AI Engineered for mastery. Research lab and product company building systems that improve with expert judgment in real work.

## 12 Research Posts (March 14, 2026)

### Framing Posts

#### 1. Why Training MoEs is So Hard
*Type: research framing*
Three failure modes that make frontier MoE training qualitatively different from dense training.

#### 2. What We Built
*Type: systems framing*
A production-grade MoE training system, because reproducibility is the experiment.

### Methodology Posts

#### 3. The Speedrun Loop
*Type: methodology result*
A small-model speedrun is our fastest honest instrument for architecture research. Using small models as rapid-turnaround probes to validate hypotheses before scaling.

#### 4. Make It Measurable
*Type: methodology result*
What to track when loss isn't enough. Complementary metrics beyond training loss for evaluating MoE training quality.

#### 5. What Are We Holding Fixed?
*Type: methodology result*
Dense-vs-MoE comparison depends on the fairness contract; a failed transfer exposed the real problem of comparing architectures under different constraints.

#### 6. The Atlas Hypothesis
*Type: research hypothesis*
Why output-only dashboards cannot name what pretraining built, and what a real receipt would have to measure. Argues for richer instrumentation of the training process.

### Research Results

#### 7. Let the Speedrun Search Itself
*Type: research result*
Eval-gated config-only autoresearch on the canonical super fp8 lane. Automated hyperparameter search guided by downstream evaluation, not just training loss.

#### 8. Reproducing Canon, mHC, and Engram
*Type: research result*
A research narrative: wrong starts, PhysicsLM4 alignment, and one real polysemy failure. Documents the process of reproducing three known MoE techniques and discovering failure modes.

#### 9. Super-4096
*Type: research result*
Loss keeps improving while routing collapses under extreme sparsity. Counter-intuitive finding that model quality can continue improving even as expert routing degenerates.

#### 10. Do MoE Experts Need Different Learning Rates?
*Type: research result*
Why Moonlet's old 15x expert-LR rule overshoots in bf16 AdamW. Empirical investigation of per-expert learning rate tuning.

#### 11. NVFP4 Dynamics
*Type: research result*
Why our NVFP4 recipe lagged BF16, and what actually closed almost all of the gap. Investigation of NVIDIA's FP4 format for MoE training.

### Systems

#### 12. RDEP
*Type: systems result*
Keeping sparse expert compute hot across a whole NVLink fabric. Direct dispatch/return using CUDA IPC instead of NCCL all-to-all collectives.
