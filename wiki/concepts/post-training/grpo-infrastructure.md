---
title: GRPO Infrastructure
type: concept
created: 2026-06-11
updated: 2026-06-17
tags:
  - reinforcement-learning
  - training
  - infrastructure
  - hardware
  - fine-tuning
  - agentic-rl
  - vllm
sources:
  - transcripts/2025-07-03_willbrown_agents-mcp-rl-lesson5-5-lecture
  - raw/articles/2025-07-03_willbrown_agents-mcp-rl-lesson5-5
  - transcripts/2025-07-02_kylecorbitt_agents-mcp-rl-lesson5-lecture
  - raw/articles/2025-07-02_kylecorbitt_agents-mcp-rl-lesson5
  - raw/articles/2026-06-16_semianalysis_rl-systems-throughput.md
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

## SemiAnalysis Throughput Matching Framework

The SemiAnalysis "RL Systems: Mind the Gap" article (June 2026) provides a practical framework for understanding RL training infrastructure efficiency. The core thesis: **system efficiency comes down to matching generator and trainer throughput.**

### Three-Actor Model

An RL training system involves three actors:

1. **Generator** — The model producing rollouts (completions) for each prompt
2. **RL Environment / Sandbox** — The execution environment where rollouts are evaluated (code execution, math verification, etc.)
3. **Trainer** — The training loop consuming rollouts to compute gradients and update model weights

### The Queue Model

```
Generator → [Queue] → Trainer
```

The generator produces rollouts which are placed into a queue. The trainer consumes rollouts from the queue. The system is balanced when:

- **Generator production rate** = concurrent rollouts / end-to-end latency
- **Trainer consumption rate** = samples per step / training step time
- **Effective generation rate** = acceptance rate × generator production rate

### PipelineRL Asynchrony

**PipelineRL** introduces asynchrony by having the trainer push updated weights to the generator **while rollouts are still in progress**. This contrasts with synchronous execution where the trainer waits for all rollouts to complete before updating weights.

Key properties:
- **Policy staleness** is tolerated to an extent — the generator uses slightly stale weights
- Synchronous execution wastes too much compute at scale due to idle GPU time
- The tradeoff: staleness degrades sample quality vs. throughput gains from continuous pipeline operation

### Group Size Impacts

Group size (N in GRPO) varies by task difficulty:

| Task Difficulty | Recommended N |
|----------------|--------------|
| Easy | 8 |
| Medium | 16 |
| Hard (reasoning) | 64 |

Larger groups provide better advantage estimates but increase sampling cost. The optimal N depends on reward distribution — if rewards are uniform within a group, the training signal vanishes regardless of group size.

### RL Environment / Sandbox Challenges

The sandbox layer (where rollouts execute — e.g., code sandboxes, math verifiers) introduces several bottlenecks:

- **Startup latency**: Cold-starting sandboxes adds significant overhead. [[entities/modal|Modal]] optimizes this through fast container initialization.
- **Concurrency scaling**: Sandboxes must scale to handle many concurrent rollouts without becoming the bottleneck.
- **Robustness**: Models can generate adversarial behavior (writing a million files, OOM abuse). Sandboxes must contain such behavior gracefully.
- **Interaction latency**: The communication overhead between generator and sandbox can dominate at high throughput.

### Throughput Optimizations

- **Early pruning**: Terminate low-quality rollouts early based on partial reward signals, freeing generator capacity for more promising samples.
- **Adaptive sampling**: Dynamically adjust the number of rollouts per prompt based on observed reward variance.
- **Concurrency tuning**: Balance the number of concurrent rollouts against sandbox capacity and trainer consumption rate.
- **Acceptance rate filtering**: Not all generated rollouts are useful — filtering by acceptance rate improves trainer efficiency.

### Policy Staleness Tolerance

A critical insight: the policy can tolerate some staleness. The trainer does not need to block until all in-flight rollouts complete. Instead, the trainer pushes weight updates asynchronously:

1. Trainer completes an optimization step
2. New weights are sent to the generator
3. In-flight rollouts continue with the old weights
4. Next batch of rollouts uses the new weights

This creates a **continuously pipelined system** where the generator never idles waiting for the trainer, and the trainer never idles waiting for rollouts. The staleness window is bounded by the rollout duration.

## Related Concepts

- [[concepts/post-training/grpo-rl-training]] — the GRPO algorithm and training loop
- [[concepts/agents-mcp-rl-course]] — the course these notes derive from
- [[concepts/peft-lora-and-qlora]] — LoRA fundamentals and quantized variants
- [[concepts/evaluation/reward-engineering]] — designing reward signals for RL training
- [[entities/openpipe]] — GRPO infrastructure provider
