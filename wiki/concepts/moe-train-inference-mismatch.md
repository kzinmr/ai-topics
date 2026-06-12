---
title: 'MoE Train-Inference Mismatch'
type: concept
created: 2026-06-12
updated: 2026-06-12
tags: [mixture-of-experts, training, inference, optimization, deepseek, distributed-training]
sources:
  - url: https://x.com/sheriyuo/status/2063295181131247674
    title: 'RL Interview Questions 2026 — Q11'
    date: 2026-06-06
  - url: https://arxiv.org/abs/2006.16668
    title: 'GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding (Lepikhin et al., Google, 2020)'
    date: 2020-06-30
  - url: https://arxiv.org/abs/2101.03961
    title: 'Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity (Fedus et al., Google, 2021)'
    date: 2021-01-11
  - url: https://arxiv.org/abs/2412.19437
    title: 'DeepSeek-V3 Technical Report (DeepSeek-AI, 2024)'
    date: 2024-12-27
---

# MoE Train-Inference Mismatch

In [[mixture-of-experts]] (MoE) models, the routing mechanism behaves differently during training versus inference, leading to degraded deployment quality if not addressed.

## What Is the Mismatch?

During **training**, MoE uses token-level routing where each token independently selects its top-k experts over large batches. During **inference**, several factors shift this behavior:

- **Batch size**: Training processes thousands of tokens per step; autoregressive generation processes one token at a time. This changes the statistical distribution of expert selection.
- **Precision**: Training typically uses BF16/FP16; inference may use INT8/FP8 quantization. Small differences in the gating network's floating-point output can flip top-k expert assignments.
- **Expert capacity**: Training uses capacity factors to limit tokens per expert and drops overflow tokens. Inference must serve every token — no dropping allowed. This concept originates from **GShard** (Lepikhin et al., 2020), which introduced the capacity factor $c$ to bound the number of tokens each expert processes: $c = (\text{tokens} / \text{experts}) \times \text{capacity\_factor}$. When $c$ is exceeded, overflow tokens are dropped. **Switch Transformer** (Fedus et al., 2021) showed that even with a modest capacity factor (1.0–1.25), a significant fraction of tokens can be dropped during training, creating a distribution mismatch at inference time where all tokens must be served.

## Specific Problems

- **Routing inconsistency**: FP precision differences between training and inference cause the router to select different experts for the same input, degrading output quality.
- **Token dropping vs. no dropping**: Training drops tokens when an expert is full; inference cannot, so experts must handle load spikes they never saw during training.
- **KV cache interactions**: In autoregressive generation, the KV cache grows per-token but expert routing decisions change per position, causing cache fragmentation across experts.

## Solutions

### Training-Time Mitigations

- **Auxiliary load-balancing loss**: Regularizes the router to distribute tokens evenly across experts, reducing imbalance at inference. Introduced by **Switch Transformer** (Fedus et al., 2021) as $L_{\text{aux}} = \alpha \cdot N \sum_{i=1}^{N} f_i \cdot P_i$ where $f_i$ is the fraction of tokens routed to expert $i$ and $P_i$ is the average routing probability. However, this auxiliary loss can **degrade model quality** when set too high — it forces uniform routing at the expense of task performance.
- **Auxiliary-loss-free load balancing**: **DeepSeek-V3** (DeepSeek-AI, 2024) introduced a dynamic bias mechanism that adjusts expert selection without an auxiliary loss term. A learnable bias $b_i$ is added to the gating scores for load balancing, but crucially, the bias is **excluded from the gradient computation** — it only affects routing decisions, not training gradients. This eliminates the quality degradation that auxiliary losses cause while still achieving balanced expert utilization.
- **Shared experts**: DeepSeek-V3 introduced shared experts that process *all* tokens regardless of routing. This provides a stable base computation, reducing sensitivity to routing errors. The shared experts handle common patterns while routed experts handle specialization.
- **FP8 training**: DeepSeek V3 pioneered FP8 training so that training and inference precision match, eliminating gating-network drift.

### Inference-Time Mitigations

- **Expert Parallelism (EP)**: Distributes experts across GPUs so that each GPU handles a manageable subset. [[elastic-ep]] in [[inference/sglang]] adds fault-tolerant EP for production deployments.
- **Fine-grained expert parallelism**: [[deepseek-v4]]'s MegaMoE uses many small experts with fine-grained EP, improving load distribution and reducing per-expert capacity pressure.

### Combined Approach (DeepSeek)

DeepSeek's strategy addresses mismatch at both ends:

1. **Auxiliary-loss-free load balancing** eliminates quality-vs-balance tradeoff (training)
2. **Shared experts** provide stable base computation independent of routing (training + inference)
3. **FP8 training** with tile-wise (1×128) activation and block-wise (128×128) weight quantization matches inference precision (training)
4. **Fine-grained routing** with many small experts smooths load distribution (training)
5. **MegaMoE + Elastic EP** handles deployment scale with fault tolerance (inference)

> **Paper reference**: DeepSeek-V3 achieved 671B total parameters / 37B activated with zero irrecoverable loss spikes during training. The auxiliary-loss-free mechanism was critical — previous models (DeepSeek-V2) used traditional auxiliary loss which degraded downstream task performance by ~1-2% compared to balanced routing without auxiliary loss.

## Key Insight

The mismatch is fundamentally a **distribution shift** problem: routing decisions made under training conditions (large batch, high precision, capacity limits) don't transfer perfectly to inference conditions (small batch, lower precision, no capacity limits). The best solutions attack from both sides — make training more inference-aware and make inference more robust to routing variation.

## See Also

- [[rl-interview-questions-2026]]
- [[mixture-of-experts]]
- [[deepseek-v3-2]]
- [[deepseek-v4]]
- [[elastic-ep]]
- [[model-quantization]]
- [[inference/vllm]]
- [[inference/sglang]]
- [[raw/papers/2024-12-27_2412.19437_deepseek-v3-technical-report]]
