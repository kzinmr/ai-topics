---
title: DeepSeek-V3
created: 2026-05-08
updated: 2026-05-26
type: concept
tags:
  - model
  - inference
  - infrastructure
  - training
  - benchmark
  - open-source
  - deepseek
sources:
  - raw/papers/2024-12-27_2412.19437_deepseek-v3-technical-report.md
  - https://arxiv.org/abs/2412.19437
---

# DeepSeek-V3

DeepSeek-V3 is a **671B total parameter** ( **37B activated** per token) Mixture-of-Experts (MoE) language model. Announced by DeepSeek-AI (China) in December 2024. A milestone paper that fundamentally shifted the cost paradigm for open-source LLMs, achieving performance comparable to GPT-4o and Claude-3.5-Sonnet at a training cost of just **$5.576M (2.788M H800 GPU hours)** .

## Architecture

DeepSeek-V3 inherits and extends the architecture of [[deepseek-v2|DeepSeek-V2]].

### Multi-head Latent Attention (MLA)

An attention mechanism that reduces KV cache through low-rank joint compression.

```
c_KV_t = W_DKV · h_t          ← Compressed latent vector (dimension d_c ≪ d_h · n_h · l_k)
k_C_t = W_UK · c_KV_t          ← Up-projection (for content)
k_R_t = RoPE(W_KR · h_t)       ← Separated RoPE key (for positional encoding)
```

- **At inference time**: Only the compressed latent vector `c_KV_t` and separated key `k_R_t` are cached → significant KV cache reduction
- **Effect**: V3 dramatically improves inference memory efficiency through MLA. Inherited from V2, but validated at V3's scale

### DeepSeekMoE

Highly efficient MoE architecture with two key features:

1. **Fine-Grained Expert Segmentation**: Splitting into many small experts rather than a few large ones → more flexible knowledge combinations
2. **Shared Expert Isolation**: Designating a "shared expert" that all tokens always pass through → preventing redundant duplication of common knowledge

V3 configuration: **1 shared expert + 256 routed experts** (top 8 experts activated per token)

### Auxiliary-Loss-Free Load Balancing

Traditional MoE models impose an **auxiliary loss** to ensure balanced expert utilization, but this degrades model performance.

DeepSeek-V3's innovative approach:
- Adding a **dynamic bias term** `b_i` to each expert
- **During routing**: Top-k selection using affinity score `s_i + b_i` (bias-corrected)
- **During gating**: Multiplication by original affinity score `s_i` (no bias correction = zero performance degradation)
- **Bias update**: Increase `b_i` for underloaded experts, decrease `b_i` for overloaded experts

> The first large-scale MoE model to achieve load balancing without relying on auxiliary loss. Successfully equalized expert utilization with zero performance degradation.

### Multi-Token Prediction (MTP)

A training objective that **simultaneously predicts multiple future tokens** at each token position.

- **Structure**: MTP modules added from the main Transformer's hidden state `h_t` to predict D consecutive additional tokens `t+1, t+2, ..., t+D` (implemented with D=1)
- **Effect**: Increased training signal density, improving data efficiency (one factor in achieving strong performance on 14.8T tokens of pretraining)
- **Inference-time use**: MTP modules repurposed for **speculative decoding** → **1.8x generation speed improvement** (TPS: tokens per second)

## Training

### FP8 Mixed Precision Training

A milestone achievement that **first validated the effectiveness of FP8 training** at 671B scale.

| Quantization Target | Method | Granularity |
|--------------------|--------|-------------|
| Activations | Tile-wise scaling | 1×128 |
| Weights | Block-wise scaling | 128×128 |

- **Promotion to high-precision accumulation**: Within Tensor Core FP8 GEMM, promoted to FP32 accumulation at 128-element intervals, preventing precision loss
- **Memory efficiency**: ~50% memory reduction vs FP16/BF16, communication volume halved

### DualPipe Algorithm

A novel pipeline parallelism strategy that completely overlaps computation and communication.

- **Forward/backward passes** overlapped with **cross-node all-to-all communication** → near-zero communication overhead
- **Memory savings**: Recomputing RMSNorm and MLA up-projections (no activation storage), placing EMA parameters on CPU memory
- **15 days of meticulous planning**: Fine-grained scheduling of forward/backward CUDA kernel placement to avoid SM resource contention

### Training Cost Breakdown

| Stage | H800 GPU Hours | Estimated Cost ($2/hr) |
|-------|----------------|------------------------|
| Pretraining | 2,664K | $5.328M |
| Context extension (→128K) | 119K | $0.238M |
| Post-training | 5K | $0.01M |
| **Total** | **2,788K** | **$5.576M** |

### Training Stability

**Zero unrecoverable loss spikes** throughout the entire training process, no rollbacks required. Extremely unusual stability for a model of this scale, demonstrating the robustness of the architecture and system design.

### Dataset

- 14.8 trillion tokens of high-quality diverse data (web, code, math, multilingual)
- Document packing and Fill-in-Middle (FIM) strategy employed
- Tokenizer: Byte-level BPE, vocabulary size 128K

## Post-Training

### Distillation from DeepSeek-R1

Reasoning capabilities (verification, introspection patterns) distilled from the [[concepts/deepseek-r1|DeepSeek-R1]] series into V3. This enables strong reasoning ability in the base model.

### GRPO (Group Relative Policy Optimization)

Reinforcement learning algorithm used as an alternative to RLHF:
- **No critic model** of the same size as the policy model → significant memory and compute savings
- Policy optimization through relative reward comparison within groups
- Reward models: Rule-based (math/coding) + Model-based (general tasks)

### Long Context

Context extended from 4K → 32K → 128K tokens using YaRN. Two-stage gradual extension minimized performance degradation on long-context tasks.

## Benchmarks

### Comparison with Open-Source Models

| Benchmark | DeepSeek-V3 | Qwen2.5-72B | Llama-3.1-405B | DeepSeek-V2.5 |
|-----------|-------------|-------------|----------------|---------------|
| MMLU | 88.5 | 85.3 | 84.4 | 80.6 |
| MMLU-Pro | 75.9 | 59.1 | 57.3 | 57.4 |
| MATH-500 | 90.2 | 80.0 | 73.8 | 74.7 |
| HumanEval-Mul | 82.6 | 77.3 | 77.2 | 77.4 |
| LiveCodeBench | 40.5 | 24.4 | 22.3 | 21.0 |

### Comparison with Closed-Source Models

| Benchmark | DeepSeek-V3 | GPT-4o-0513 | Claude-3.5-Sonnet-1022 |
|-----------|-------------|-------------|------------------------|
| MMLU | 88.5 | 87.2 | 88.3 |
| MATH-500 | 90.2 | 74.6 | 78.3 |
| GPQA Diamond | 59.1 | 49.9 | 65.0 |
| Chinese SimpleQA | 64.8 | 38.2 | 39.4 |

Notably, it **surpassed GPT-4o in math (MATH-500: 90.2) and programming (LiveCodeBench: 40.5)** . Scored over 1.7× GPT-4o on Chinese factual accuracy (Chinese SimpleQA).

## Historical Significance

DeepSeek-V3 is a milestone paper in LLM history for multiple reasons:

1. **Cost disruption**: Achieved GPT-4-class performance for $5.576M (Western frontier model training costs estimated at $100M+) → overturned the premise that "LLM training requires massive capital"
2. **Large-scale FP8 training validation**: First to demonstrate practical FP8 training at 671B parameters → became standard practice for subsequent model development
3. **Auxiliary-Loss-Free Load Balancing**: Solved the long-standing MoE problem (performance degradation from auxiliary loss) → widely adopted in subsequent MoE models
4. **Multi-Token Prediction (MTP)**: Training density improvement + 1.8x inference speedup via speculative decoding → efficiency revolution on both training and inference fronts
5. **DualPipe**: New standard for distributed training through complete computation-communication overlap
6. **Open-weight strategy**: Full release under MIT license → accelerated global research community

This paper demonstrated that **"frontier performance can be reached with constrained compute resources through algorithmic and system innovation."** It was also a landmark achievement for Chinese AI research, becoming the foundation for the subsequent DeepSeek V3.2 and V4 series.

## Successor Models

- **[[concepts/deepseek-v3-2|DeepSeek V3.2 / V3.2 Speciale]]** (December 2025) — 685B params. Three innovations: DeepSeek Sparse Attention (DSA: $O(L^2)→O(Lk)$), scalable RL (enhanced GRPO, post-training budget >10% of pretraining), large-scale agent task synthesis (1,827 environments, 85K prompts). V3.2-Speciale won gold medals at IMO 2025, IOI 2025, and placed 2nd worldwide at ICPC World Finals. Performance approaching GPT-5/Gemini-3.0-Pro. Technical report (arXiv:2512.02556).
- **[[concepts/deepseek-v4|DeepSeek V4]] series** (April 2026) — 1.6T Pro / 284B Flash, 1M context, MIT license

## Hardware Design Recommendations

The paper makes four specific recommendations for future AI hardware design:

1. **Communication offload co-processor**: Separate all-to-all communication from SM to dedicated processor
2. **High-precision FP8 accumulation**: Improve FP8 GEMM accumulation precision within Tensor Cores (eliminating need for CUDA Core promotion)
3. **Native support for fine-grained quantization**: Tensor Cores directly handle scaling factors
4. **Online quantization**: Fuse FP8 casting with memory access (TMA) to reduce HBM read/write

## Related Pages

- [[entities/deepseek]] — DeepSeek company overview
- [[deepseek-v2]] — Previous generation architecture (origin of MLA/DeepSeekMoE)
- [[concepts/deepseek-v3-2]] — Successor model (DSA + enhanced GRPO + agent synthesis)
- [[concepts/mixture-of-experts]] — MoE architecture in general
- [[concepts/speculative-decoding]] — Speculative decoding technology
- [[fp8-training]] — FP8 mixed precision training
- [[concepts/post-training/grpo]] — Group Relative Policy Optimization
- [[yaRN]] — Context extension method
- [[concepts/inference]] — General inference efficiency techniques
- [[training]] — Large-scale training techniques
