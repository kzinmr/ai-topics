---
title: GRPO Infrastructure
type: concept
created: 2026-06-11
updated: 2026-06-11
tags: [reinforcement-learning, grpo, infrastructure, gpu, vram, lora, training, agentic-rl, vllm]
sources:
  - transcripts/2025-07-03_willbrown_agents-mcp-rl-lesson5-5-lecture
  - raw/articles/2025-07-03_willbrown_agents-mcp-rl-lesson5-5
  - transcripts/2025-07-02_kylecorbitt_agents-mcp-rl-lesson5-lecture
  - raw/articles/2025-07-02_kylecorbitt_agents-mcp-rl-lesson5
---

# GRPO Infrastructure

## VRAM Napkin Math

The **10× rule** provides a quick estimate: a 7B-parameter model requires ~70GB total VRAM for full-parameter training. This breaks down as follows:

- **Model weights**: bfloat16 → 2 bytes/param → 14GB for 7B
- **Gradients**: fp32 → 4 bytes/param → 28GB for 7B
- **AdamW optimizer**: 2 momentum vectors (first moment + second moment) at fp32 = 8 bytes/param → 56GB for 7B

The convention is **bfloat16 for model weights** and **fp32 for gradients and optimizer states**. fp8 tooling is still immature and not yet reliable for production GRPO training.

[LoRA](concepts/peft-lora-and-qlora) reduces this dramatically. With the default r=16, alpha=32 configuration, you get a **100× parameter reduction**, making GRPO feasible on much smaller GPU setups.

## PPO vs GRPO Tradeoffs

| Aspect | PPO | GRPO |
|--------|-----|------|
| Critic model | Full copy for per-token advantage estimation | None — no critic needed |
| Memory cost | Huge (doubled model footprint) | Significantly lower |
| Advantage estimation | Per-token via learned value function | Group sampling — reward normalized within group |
| Accessibility | Requires large GPU clusters | Democratized RL at smaller scales |

GRPO is **not the endgame**. The core goal is advantage estimation, and a large design space remains open. GRPO's group-based normalization is one clever solution, but alternatives like VinePPO and REINFORCE batch methods explore different tradeoffs.

## GPU Architecture Patterns

### Pattern A — ART-style Swapping

Inference and training share the same GPUs, swapping between phases. Simpler hardware requirements but introduces idle time during phase transitions.

### Pattern B — Verifiers-style Overlapping

Designated inference and training GPUs with cascade scheduling. Inference runs continuously on dedicated GPUs while training proceeds in parallel. More complex orchestration but higher GPU utilization.

### vLLM LoRA Hot-Swap API

vLLM provides **first-class support for switching [LoRA](concepts/peft-lora-and-qlora) adapters** without reloading the base model. This is critical for GRPO workflows where you need to frequently swap between the training adapter and inference adapter during rollout generation.

## LoRA for GRPO

Default configuration: **r=16, alpha=32**.

The 100× parameter reduction from LoRA has a powerful side effect: it enables **beta=0** (no reference model needed). Because LoRA constrains updates to a low-rank subspace, it acts as an **implicit regularizer**, making the KL-divergence penalty against a reference model unnecessary.

This is safe and recommended — removing the reference model saves significant VRAM and simplifies the training loop.

vLLM's first-class LoRA hot-swap API makes this practical: you can load the base model once and hot-swap LoRA adapters for different training iterations or reward models.

## Async RL (Two Meanings)

The term "async RL" refers to two distinct concepts:

### Off-Policy Async

Stale rollouts generated from an older copy of the model. Simpler to implement but less stable — the policy being optimized drifts from the policy that generated the data.

### Async Inference

Isolated multi-turn rollouts via **vLLM micro-batching** (token-level dynamic batching). Each rollout progresses independently, with vLLM dynamically batching tokens across in-flight requests. Treat vLLM as an **OpenAI-compatible endpoint** — the training loop makes API calls and vLLM handles batching internally.

## Key GRPO Gotchas

- **Beta=0 is safe with LoRA**: No reference model needed. The low-rank constraint provides implicit regularization.
- **Temperature MUST be 1**: Lower temperatures cause mathematical issues with the GRPO advantage estimation. The reward normalization within groups assumes a proper probability distribution.
- **Caching must be disabled for training**: Multiple rollouts within a group must be independent. KV-cache reuse would create correlated rollouts, breaking the group normalization assumption.
- **Reward std dev collapse = stop learning**: If reward standard deviation within groups approaches zero, the model is output-saturated and stops learning. Monitor this metric closely.

## Frontier Research Directions

- **VinePPO**: Tree search for better credit assignment — traces value estimates along branching rollout trajectories.
- **REINFORCE batch approach**: Variance reduction through batch-level baselines rather than learned value functions.
- **Think-token removal during training**: Stripping chain-of-thought tokens from the loss to avoid penalizing reasoning structure.
- **Test-time training**: Generate synthetic Q&A pairs from a problem, train a [LoRA](concepts/peft-lora-and-qlora) adapter in minutes at inference time, apply it for the current query.
- **LM-as-judge tournaments**: For non-verifiable domains, use tournament-style pairwise comparisons with language model judges as the [reward signal](concepts/reward-engineering).

## RL-as-a-Service Skepticism

Many RL-as-a-Service offerings are **thin wrappers around TRL** (Transformer Reinforcement Learning). Before paying a premium, know the GPU market rates:

| GPU | Approximate Rate |
|-----|-----------------|
| H100 | $1–2/hr |
| H200 | ~$3/hr |

**Trusted providers** with genuine infrastructure and expertise:
- [OpenPipe](entities/openpipe) — purpose-built GRPO training infrastructure
- Bespoke Labs — custom RL training pipelines
- OpenAI RFT — reinforcement fine-tuning API
- Databricks — integrated ML platform with RL support

If a service charges significantly above market GPU rates without clear added value, you're likely paying for a TRL wrapper.

## Related Concepts

- [[concepts/grpo-rl-training]] — the GRPO algorithm and training loop
- [[concepts/agents-mcp-rl-course]] — the course these notes derive from
- [[concepts/peft-lora-and-qlora]] — LoRA fundamentals and quantized variants
- [[concepts/reward-engineering]] — designing reward signals for RL training
- [[entities/openpipe]] — GRPO infrastructure provider
