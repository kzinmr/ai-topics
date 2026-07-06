---
title: "Post-Training — Overview"
tags:
sources: []
  - training
  - reinforcement-learning
  - fine-tuning
created: 2026-04-19
updated: 2026-06-12
---

# Post-Training — Overview

Post-training encompasses all techniques applied after pre-training to adapt a language model for deployment: supervised fine-tuning (SFT), preference optimization (RLHF, DPO, GRPO), reinforcement learning (RLVR, async RL), and the supporting infrastructure. This page is the index for the post-training concept cluster.

## Core Techniques

| Technique | Description | Use Case |
|-----------|-------------|----------|
| **SFT** (Supervised Fine-Tuning) | Train on input-output pairs | Instruction following, domain adaptation |
| **PEFT** (Parameter-Efficient Fine-Tuning) | Train only a subset of parameters (LoRA, QLoRA, adapters) | Limited GPU memory, multi-adapter serving |
| **RLHF** (Reinforcement Learning from Human Feedback) | Train with human preference data | Alignment, safety, helpfulness |
| **DPO** (Direct Preference Optimization) | Preference optimization without reward model | Simpler alternative to RLHF |
| **GRPO** (Group Relative Policy Optimization) | Compare completions within groups | Reasoning, format enforcement, verifiable tasks |
| **RLVR** (RL with Verifiable Rewards) | RL with automatically verifiable rewards | Math, code, structured output |
| **Async RL** | Decoupled rollout and training | 2-3x throughput for large-scale RL |

## Sub-pages

### SFT & Parameter-Efficient Methods
- [[concepts/post-training/peft-lora-qlora]] — Parameter-efficient fine-tuning (LoRA, QLoRA, adapters)
- [[concepts/post-training/instruction-fine-tuning]] — Instruction tuning methodology
- [[concepts/post-training/axolotl]] — YAML-config fine-tuning framework
- [[concepts/post-training/unsloth]] — 2-5x faster fine-tuning with 50-80% less memory

### GRPO & PPO
- [[concepts/post-training/grpo]] — GRPO fundamentals
- [[concepts/post-training/grpo-rl-training]] — GRPO training details
- [[concepts/post-training/grpo-infrastructure]] — GRPO VRAM math and infrastructure
- [[concepts/post-training/grpo-memory-modeling]] — GRPO memory modeling
- [[concepts/post-training/rl-algorithms-for-llm-training]] — Comprehensive RL algorithm Q&A

### Preference Optimization (RLHF, DPO, ORPO, KTO)
- [[concepts/post-training/rlhf]] — RLHF overview
- [[concepts/post-training/rlhf-dpo-preference]] — RLHF, DPO, ORPO, KTO methods
- [[concepts/post-training/rlhf-dpo-orpo-kto-preference-optimization]] — Preference optimization techniques
- [[concepts/post-training/rlhf-reinforcement-learning-from-human-feedback]] — RLHF deep dive

### RLVR & Verifiable Rewards
- [[concepts/post-training/rlvr]] — RL with Verifiable Rewards
- [[concepts/post-training/rlvr-science-limitations]] — RLVR limitations in science
- [[concepts/post-training/verifiers-rl]] — Verifier-based RL

### RL Frameworks & Infrastructure
- [[concepts/post-training/areal]] — AReaL (Ant Group)
- [[concepts/post-training/slime-rl]] — slime (Tsinghua/THUDM)
- [[concepts/post-training/openrlhf]] — OpenRLHF
- [[concepts/post-training/nemo-rl]] — NeMo RL (NVIDIA)
- [[concepts/post-training/trl]] — TRL (HuggingFace)
- [[concepts/post-training/skyrl]] — SkyRL
- [[concepts/post-training/roll-rl]] — ROLL (Alibaba)
- [[comparisons/open-source-rl-libraries-comparison]] — 10 RL library comparison

### Async RL & Scaling
- [[concepts/post-training/asynchronous-rl]] — Asynchronous RL for LLM post-training
- [[concepts/post-training/rl-scaling-boundaries]] — RL scaling boundaries
- [[concepts/post-training/rl-harness-lifecycle]] — RL harness lifecycle

### Agentic RL & Distillation
- [[concepts/post-training/sdar-self-distilled-agentic-rl]] — SDAR
- [[concepts/post-training/on-policy-distillation]] — On-policy distillation
- [[concepts/post-training/on-policy-self-distillation]] — On-policy self-distillation
- [[concepts/post-training/on-policy-vs-off-policy-rl]] — On-policy vs off-policy
- [[concepts/post-training/ragen]] — RAGEN
- [[concepts/post-training/multi-turn-tool-use-rl]] — Multi-turn tool-use RL

### RL Fundamentals
- [[concepts/post-training/reinforcement-learning]] — RL basics
- [[concepts/post-training/reinforcement-fine-tuning]] — Reinforcement Fine-Tuning (RFT)
- [[concepts/post-training/training-free-rl]] — Training-Free RL
- [[concepts/post-training/rl-exploration-test-time-vs-training]] — RL exploration: training vs test-time
- [[concepts/post-training/rpg-regularized-policy-gradient]] — RPG

### Other
- [[concepts/post-training/prime-rl-post-training]] — Prime RL post-training
- [[concepts/post-training/echo-rl]] — Echo RL
- [[concepts/post-training/miles-rl]] — Miles RL
- [[concepts/post-training/hands-on-modern-rl]] — Hands-on Modern RL curriculum
- [[concepts/post-training/rl-interview-questions-2026]] — RL Interview Questions 2026

### Training Frameworks & Infrastructure
- [[concepts/post-training/pytorch-fsdp]] — FSDP for distributed training
- [[concepts/post-training/quantization-overview]] — Model quantization

## The Post-Training Pipeline

```
Pre-trained Model → SFT → Preference Optimization (DPO/GRPO/RLHF) → RLVR → Quantization → Deployment
     ↓                  ↓                    ↓                        ↓         ↓
  Base weights    Instruction format    Reward alignment        Verifiable   GGUF/GPTQ/FP8
                                                             rewards (math/code)
```

## When to Fine-Tune vs Prompt

> **Moved to [[concepts/post-training/fine-tuning]]** — includes the decision framework table, Ameisen's hierarchy of needs, the 2026 analysis (Context Rot, GRPO evolution, Knowledge Storage Spectrum), and concrete "when to use what" guidance.

## Related Concepts

- [[concepts/harness-engineering]] — Fine-tuning as part of the model + harness paradigm
- [[concepts/local-llm/_index]] — Running fine-tuned models locally
- [[concepts/inference]] — Inference optimization post-training
