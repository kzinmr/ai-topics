---
title: 'MoE Train-Inference Mismatch'
type: concept
created: 2026-06-12
updated: 2026-06-12
tags: [mixture-of-experts, training, inference, optimization, deepseek]
sources:
  - url: https://x.com/sheriyuo/status/2063295181131247674
    title: 'RL Interview Questions 2026 — Q11'
    date: 2026-06-06
---

# MoE Train-Inference Mismatch

In [[mixture-of-experts]] (MoE) models, the routing mechanism behaves differently during training versus inference, leading to degraded deployment quality if not addressed.

## What Is the Mismatch?

During **training**, MoE uses token-level routing where each token independently selects its top-k experts over large batches. During **inference**, several factors shift this behavior:

- **Batch size**: Training processes thousands of tokens per step; autoregressive generation processes one token at a time. This changes the statistical distribution of expert selection.
- **Precision**: Training typically uses BF16/FP16; inference may use INT8/FP8 quantization. Small differences in the gating network's floating-point output can flip top-k expert assignments.
- **Expert capacity**: Training uses capacity factors to limit tokens per expert and drops overflow tokens. Inference must serve every token — no dropping allowed.

## Specific Problems

- **Routing inconsistency**: FP precision differences between training and inference cause the router to select different experts for the same input, degrading output quality.
- **Token dropping vs. no dropping**: Training drops tokens when an expert is full; inference cannot, so experts must handle load spikes they never saw during training.
- **KV cache interactions**: In autoregressive generation, the KV cache grows per-token but expert routing decisions change per position, causing cache fragmentation across experts.

## Solutions

### Training-Time Mitigations

- **Auxiliary load-balancing loss**: Regularizes the router to distribute tokens evenly across experts, reducing imbalance at inference.
- **Shared experts**: [[deepseek-v3-2]] introduced shared experts that process *all* tokens regardless of routing. This provides a stable base computation, reducing sensitivity to routing errors.
- **FP8 training**: DeepSeek V3 pioneered FP8 training so that training and inference precision match, eliminating gating-network drift.

### Inference-Time Mitigations

- **Expert Parallelism (EP)**: Distributes experts across GPUs so that each GPU handles a manageable subset. [[elastic-ep]] in [[inference/sglang]] adds fault-tolerant EP for production deployments.
- **Fine-grained expert parallelism**: [[deepseek-v4]]'s MegaMoE uses many small experts with fine-grained EP, improving load distribution and reducing per-expert capacity pressure.

### Combined Approach (DeepSeek)

DeepSeek's strategy addresses mismatch at both ends:

1. Shared experts reduce routing dependency (training + inference)
2. FP8 training matches inference precision (training)
3. Fine-grained routing with many small experts smooths load (training)
4. MegaMoE + Elastic EP handles deployment scale (inference)

## Key Insight

The mismatch is fundamentally a **distribution shift** problem: routing decisions made under training conditions (large batch, high precision, capacity limits) don't transfer perfectly to inference conditions (small batch, lower precision, no capacity limits). The best solutions attack from both sides — make training more inference-aware and make inference more robust to routing variation.

## See Also

- [[rl-interview-questions-2026]]
- [[model-quantization]]
- [[inference/vllm]]
