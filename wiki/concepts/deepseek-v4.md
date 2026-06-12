---
title: DeepSeek-V4
created: 2026-05-08
updated: 2026-06-10
type: concept
tags:
  - model
  - context-management
  - quantization
  - inference
  - ai-agents
  - training
  - benchmark
  - deepseek
sources:
  - raw/papers/2026-04-xx_deepseek-v4-technical-report.md
  - raw/articles/2026-05-08_hn-deepseek-v4-discussion.md
  - https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf
  - raw/newsletters/2026-05-22-tpweek162-deepseek-v4.md
  - raw/newsletters/2026-05-23-ainews-all-model-labs-are-now-agent-labs.md
  - raw/articles/2026-06-07_deepseek-v4-pro-vs-gpt-5-5-pro.md
  - https://runtimewire.com/article/deepseek-v4-pro-beats-gpt-5-5-pro-on-precision
  - raw/newsletters/2026-06-09-deepseekv4-1-6t-day-0-to-day-43-performance-over-time-huawei-gb300-nvl72-mi355x-.md
---

# DeepSeek-V4

DeepSeek-V4 is a Mixture-of-Experts (MoE) model series achieving ultra-efficient processing with a **1 million token (1M) context**. Announced by DeepSeek-AI in April 2026. Built on the [[concepts/deepseek-v3|V3]] architecture, it introduces multiple revolutionary technologies including **Hybrid Attention, Manifold-Constrained Hyper-Connections (mHC), and Muon Optimizer**, reducing inference costs at 1M context by **3.7–10×** compared to V3.2.

## Model Lineup

| Model | Total Parameters | Active Parameters | Context | License |
|--------|-------------|-----------------|-------------|-----------|
| **V4-Pro** | 1.6T | 49B | 1M tokens | MIT |
| **V4-Flash** | 284B | 13B | 1M tokens | MIT |
| **V4-Pro-Max** | 1.6T+ | 49B+ (reasoning) | 1M tokens | MIT |

## Architectural Innovations

### Hybrid Attention: 3-Layer Hybrid Attention

Conventional self-attention has $O(n^2)$ quadratic complexity relative to sequence length. At 1M context, this becomes a fatal bottleneck. V4 solves this by interleaving three complementary attention mechanisms:

| Layer | Method | Compression Ratio | Attention | Role |
|---------|------|--------|-------------|------|
| **CSA** (Compressed Sparse Attention) | KV cache compression + Top-k sparse attention | m=4 | DeepSeek Sparse Attention (DSA) | Efficient capture of long-range dependencies |
| **HCA** (Heavily Compressed Attention) | Ultra-compressed (up to 128x) + dense attention | m'=up to 128 | Dense | Coarse-grained global context awareness |
| **SWA** (Sliding Window Attention) | Local window | window size=128 | Dense | Preservation of local fine-grained dependencies |

**Architectural characteristics**:
- CSA has queries attending only to top-k entries of compressed KV → dramatically reduces computation
- HCA maintains global context at low cost through extreme compression
- SWA ensures local patterns (grammar/syntax between adjacent tokens, etc.) are not missed
- Outputs of the 3 layers are integrated via a gating mechanism (details undisclosed)

### Manifold-Constrained Hyper-Connections (mHC)

Extends conventional residual connections by constraining the residual mapping onto the manifold of **doubly stochastic matrices**.

$$x_{l+1} = x_l + f_\theta(x_l) \quad \rightarrow \quad x_{l+1} = M(x_l) \cdot f_\theta(x_l)$$

Where $M(x_l)$ is a doubly stochastic matrix (each row and column sums to 1, all elements $\geq$ 0).

- **Spectral norm $\leq$ 1**: Dramatically improves numerical stability in forward and backward propagation
- **Effect**: Suppresses vanishing/exploding gradients in ultra-deep, long-sequence scenarios like 1M context
- Like V3's auxiliary-loss-free load balancing, enables extending model depth without compromising training stability

### Muon Optimizer

Replaces AdamW with **Muon** in most modules.

- **Hybrid Newton-Schulz Iterations**: Numerical method for orthogonalization. Iteratively improves matrix orthogonality
- **Effect**: Faster convergence and improved training stability compared to AdamW
- **Scope**: Major modules such as attention projection matrices, MLP weights. Some areas like MoE routing continue using AdamW

## Training Infrastructure

### Dataset

Pretrained on **32T+ tokens** of diverse, high-quality data. More than double V3's data scale (14.8T).

### Training Stabilization Techniques

**Anticipatory Routing**:
- Decouples MoE routing updates from backbone updates
- Computes routing indices using historical parameters $\theta_{t-\Delta t}$
- **Purpose**: Prevent loss spikes from abrupt routing changes
- Further strengthens V3's "zero rollback" stability

**SwiGLU Clamping**:
- Clamps the linear component of the SwiGLU activation function to $[-10, 10]$
- Suppresses extreme activation outliers, ensuring stability for FP8/FP4 low-precision training

### MegaMoE: Fine-Grained Expert Parallelism

One of V4's biggest system innovations.

- **Fusion of communication and computation**: Unifies all-to-all communication into a single pipelined kernel
- **Bandwidth efficiency**: "1 GBps of interconnect bandwidth is sufficient to hide 6.1 TFLOP/s of computation"
- Maximally leverages H800 GPU interconnect constraints (~400 GBps NVLink)

### TileLang DSL

A domain-specific language for custom kernel development.

| Feature | Effect |
|------|------|
| **Host Codegen** | Reduces CPU-side orchestration overhead from hundreds of μs → <1μs |
| **Deterministic Kernels** | Avoids non-deterministic atomic operations, guaranteeing bit-level reproducibility between training and inference |
| **Fused Kernels** | Fuses multiple operations into a single kernel, minimizing HBM reads/writes |

## Efficiency: Comparison with V3.2 (at 1M Context)

| Metric | V4-Pro vs V3.2 | V4-Flash vs V3.2 |
|------|---------------|-----------------|
| **FLOPs per token** | 27% (**3.7× reduction**) | 10% (**10× reduction**) |
| **KV cache size** | 10% (**10× reduction**) | 7% (**14× reduction**) |

### KV-Cache Reduction: 2% of Baseline

DeepSeek V4 compressed attention achieves **KV-cache at just 2%** of naive attention at 1M context:

| Technique | Effective KV-cache |
|-----------|-------------------|
| CSA (stride 4) | 25% of naive |
| HCA (stride 128) | 0.8% for global context |
| Combined (CSA+HCA+SWA) | ~2% of naive |

A model needing 1TB KV-cache with standard attention needs only ~20GB — enabling single-node inference.

> At 1M context, V4-Pro's FLOPs are approximately 1/4 of V3.2's, and KV cache is 1/10. This is due to the synergistic effect of Hybrid Attention and mHC.

## Post-Training

### 2-Stage Pipeline

```
Specialist Training → On-Policy Distillation (OPD)
```

**Stage 1: Specialist Training**
- Trains individual specialist models in each domain: math, code, agents
- Method: SFT + [[concepts/post-training/grpo|GRPO]]
- Each specialist is optimized to the limit in a specific domain

**Stage 2: On-Policy Distillation (OPD)**
- A single student model learns from the **full vocabulary logit distributions** of multiple teacher specialists
- Less information loss than conventional distillation (discrete outputs only)
- Integrates multi-domain capabilities into a single model

### Agent Features

**Interleaved Thinking**:
- V3.2 and earlier: reasoning trace reset at tool call boundaries
- V4: Maintains and continues reasoning trace across user message boundaries
- Improves performance on complex agent tasks involving multiple tool calls

**Quick Instruction**:
- Processes auxiliary tasks (e.g., web search intent detection) via special tokens like `<|action|>` or `<|query|>`
- No separate small model needed → latency reduction

### FP4 QAT (Quantization-Aware Training)

| Application Area | Purpose |
|---------|------|
| MoE expert weights | Memory traffic reduction (75% reduction vs FP16) |
| CSA indexer path | Accelerate index computation |

FP4 has half the bit width of FP8. However, activations remain FP8/BF16, with only weights quantized to FP4 — a hybrid strategy.

## Benchmarks

### Reasoning & Coding

| Benchmark | V4-Pro-Max | Comparison |
|-----------|-----------|---------|
| **Codeforces** | **3206 rating** (equivalent to human rank ~23) | — |
| Code Agents (internal R&D) | 67% pass rate | Claude Opus 4.5: 70% |
| Math/Reasoning | Comparable or superior to GPT-5.2, Gemini-3.0-Pro | — |

### Knowledge & Language

| Benchmark | V4-Pro-Max | Comparison |
|-----------|-----------|------|
| SimpleQA | 57.9% | Best open model |
| Chinese-SimpleQA | 84.4% | — |
| Chinese Functional Writing | 62.7% win rate | vs Gemini-3.1-Pro |

### Real Tasks

| Task | V4-Pro-Max | Comparison |
|--------|-----------|------|
| 30 Advanced Professional Tasks | **63% non-loss rate** | vs Claude Opus 4.6 |
| Long-Context | Surpasses Gemini-3.1-Pro | Academic benchmarks |

## Evolution Summary from V3

| Dimension | DeepSeek-V3 (Dec 2024) | DeepSeek-V4 (Apr 2026) |
|------|----------------------|----------------------|
| **Max Parameters** | 671B / 37B active | 1.6T / 49B active |
| **Context** | 128K | **1M** |
| **Attention** | MLA | **Hybrid Attention (CSA+HCA+SWA)** |
| **Residual Connections** | Standard Residual | **mHC (manifold-constrained)** |
| **Optimizer** | AdamW | **Muon (+ AdamW partially)** |
| **Data Scale** | 14.8T tokens | **32T+ tokens** |
| **Training Stabilization** | Aux-Loss-Free | Anticipatory Routing + SwiGLU Clamping |
| **Expert Parallelism** | Standard | **MegaMoE** |
| **Kernel Development** | CUDA hand-written | **TileLang DSL** |
| **Post-Training** | SFT + GRPO + R1 distillation | **Specialist Training + OPD** |
| **Quantization** | FP8 | **FP4 QAT (weights only)** |
| **Agents** | — | Interleaved Thinking, Quick Instruction |
| **Code** | Codeforces 1134 | **Codeforces 3206** |

## Serving DeepSeek-V4 (Together AI, May 2026)

Together AI published early bring-up experience serving V4 on NVIDIA HGX B200 GPUs. Key findings:

### KV Cache Policy Determines Real-World Capacity

- **Naive SWA storage**: 3.8KB per token (higher than V3's 3.4KB)
- **Optimized cache policy**: Single HGX B200 node capacity increased from ~1.2M to ~3.7M tokens
- **Lesson**: V4's architecture creates the *opportunity* for long-context efficiency, but realized capacity depends on how the engine manages different cache types

### Three Cache Layouts Must Be Managed Simultaneously

| Cache Type | Size per Token | Storage Strategy |
|-----------|---------------|-----------------|
| CSA (stride 4) | Compressed | Store compressed state, efficient prefix caching |
| HCA (stride 128) | ~8K entries total | Dense attention over compressed global context |
| SWA (window ~128) | Exact local state | Full store, periodic checkpoints, or recompute-on-hit |

### Regime-Dependent Performance

- **Long-context decode-heavy workloads**: Benefit immediately from KV cache compression
- **Short-context prefill-heavy workloads**: Sensitive to kernel maturity, MXFP4 vs NVFP4 performance differences
- **Coding agents**: Benefit from both long-context and prefix-heavy workloads (shared repo state)

### Endpoint Profiles Matter

The same V4 weights need different serving configurations for different workloads. Long-context agents, short chat, and RL rollouts each have distinct optimization targets (cost per trajectory vs latency vs throughput).

> Full analysis: [[concepts/deepseek-v4-serving]]

## Deployment Performance: Day 0 to Day 43

SemiAnalysis published a comprehensive 106-paragraph analysis tracking DeepSeek V4 Pro 1.6T inference performance across multiple hardware SKUs from Day 0 (April 25, 2026) through Day 43 (June 7, 2026), as part of their InferenceX initiative. All performance data is documented in their [open-source GitHub repo](https://github.com/SemiAnalysisAI/InferenceX).

### Day 0 Performance

- **CUDA vLLM/SGLang**: Worked great out of the box — both supported native DeepSeek V4 Pro on Day 0. Most advertised recipes for newer SKUs (B200, B300) functioned without major issues. NVIDIA delivered a GB200 distributed inference Dynamo vLLM recipe in srt-slurm using disaggregated inference and wide expert parallelism (WideEP).
- **NVIDIA B200/B300**: SGLang supported MTP (Multi-Token Prediction) from Day 3, substantially improving throughput at higher interactivity.
- **Huawei Ascend 950DT**: Demonstrated Day 0 inference performance support per official documentation.
- **AMD MI355X (ROCm)**: Did NOT work well initially. Could only run FP8 on Day 0; native FP4+FP8 checkpointing was broken. AITER's fused_moe was broken on GFX950, and the mHC pre-projection crashed in eager execution.
- **TensorRT-LLM**: Did not support DeepSeek V4 out of the box because `mhcFusedHcKernel.cu` had a hardcoded `FHC_HIDDEN = 4096` constant matching Opus 4.8's hidden size (4096), not V4 Pro's 7168 hidden size. NVIDIA engineers removed the guard entirely rather than adding V4 support, causing a week-long period where the kernel compiled silently for the wrong hidden size.

### ROCm Recovery: 100x Improvement in 26 Days

The AMD SGLang engineering team, led by HaiShaw, massively improved ROCm performance over the first month:

- **Day 0**: Technically working but not deployable in production (FP8 only, AITER issues, ATOM limited to single-sequence KV cache)
- **Day 0→1**: First commit after baseline submission mopped up significant low-hanging fruit
- **By Day 26 (May 21)**: Over **100× performance improvement** achieved, with MI355X exceeding H200 performance at lower interactivity levels after AITER mHC kernels were introduced
- **By Day 33 (May 27)**: FP4 support added, with improvement coming from AMD replacing AITER linear with Marlin24 and adding the AITER mHC kernel at every layer

### NVIDIA GB300 NVL72

The GB300 cluster was down when DeepSeek V4 launched. CoreWeave contributed spare dev GB300 NVL72 racks for InferenceX benchmarking. Results were published later in the tracking period.

### InferenceX Initiative

The SemiAnalysis InferenceX initiative benchmarks each SKU's performance using open-source images and recipes across multiple frameworks. Supported by OpenAI, Oracle, Microsoft, Weka, PyTorch Foundation, vLLM, SGLang, and CoreWeave. A key goal is to record Day 0 performance as a baseline against which engineering improvements are measured over time.

## Community Reception & Independent Benchmarks (HN)

Key findings extracted from the V4 launch discussion on Hacker News ([thread](https://news.ycombinator.com/item?id=47884971)):

### Community Benchmarks

| Benchmark | V4-Pro-Max | Context |
|-----------|-----------|------|
| **SWE-bench Verified** | **80.6%** | First open-weight model to exceed 80% |
| PhD-level math | Highly rated | More rigorous proofs than Gemini in probability theory, statistics, random matrix theory |
| System design/refactoring | Comparable to Claude 3.5 Opus | — |
| Customer support (Flash) | Equivalent or better than Gemini-3-Flash | Surpasses Qwen 3.5, and cheaper |
| White-collar tasks | V4-Pro ≥ Claude 3.5 Sonnet | But falls short of Opus 4.6 (Thinking enabled) |

### Local Inference

- **V4-Flash**: Native weights ~154GB → runnable on **Mac Studio M3 Ultra (512GB RAM)**
- **V4-Pro**: Full precision ~800GB, heavily quantized ~400GB+ → requires data-center-grade VRAM
- MIT license, open weights → unrestricted free deployment possible

### Developer Experience

| Item | Evaluation |
|------|------|
| Documentation | Praised as "no-BS" |
| Agent Integration | Works with Aider, Claude Code, Zed |
| API Limitations | No JSON Schema or Batch API support |
| Stability | Frequent "429 Overload" at launch |

### Geopolitical Aspects

- **Censorship**: China-hosted API censors political topics (Tiananmen Square, Taiwan, etc.). However, reports indicate that **local/quantized versions can bypass restrictions**
- **Preference for "hard refusal"**: Some users prefer Chinese models' "explicit refusal" over Western models' "moralizing/white-washing"
- **Dumping strategy**: Analyzed by some as an ultra-low-price strategy to capture market share
- **Questions about sanctions effectiveness**: Demonstrates that frontier-grade AI can be built even under US semiconductor export controls
- **"European option"**: Mistral/Kyutai caught between low-cost Chinese models and high-performance US models

## Pricing: Permanent 75% Cut (May 2026)

On May 22-23 2026, DeepSeek announced a **permanent 75% price reduction** for V4-Pro, not a promotional offer:

| Pricing | Input (per M tokens) | Output (per M tokens) |
|---------|---------------------|----------------------|
| V4-Pro (new) | **$0.435** | **$0.87** |
| Competitive comparison | 3-19× cheaper | 3-19× cheaper |

**Significance**: This pricing — $0.435/M input, $0.87/M output — makes V4-Pro 3-19× cheaper than competing frontier models (GPT-5.5, Claude Opus 4.5, Gemini 3.5 Flash). The "Intelligence too cheap to meter" meme captures the strategic implication: model economics are deflating so rapidly that **model quality becomes a threshold commodity**, and the real competitive advantage shifts to agent infrastructure and execution platforms.

This pricing move is directly connected to [[concepts/model-labs-to-agent-labs]] thesis — when model inference costs collapse, model providers must differentiate on [[entities/greg-brockman|agent platforms]] rather than benchmark scores.

**See also**: [[concepts/model-labs-to-agent-labs]] for the industry context of model economics deflation.

## V4 Pro vs GPT-5.5 Pro: Precision Benchmarks (June 2026)

In June 2026, RuntimeWire reported that **DeepSeek V4 Pro beat GPT-5.5 Pro on precision benchmarks**, a significant milestone for open-weight models competing with proprietary frontier models.

| Benchmark | DeepSeek V4 Pro | GPT-5.5 Pro | Notes |
|-----------|----------------|-------------|-------|
| Precision tasks | **Higher** | Lower | V4 Pro demonstrated superior accuracy on precision-oriented evaluations |
| General reasoning | Competitive | Competitive | Both models perform at frontier level |

This result reinforces the [[concepts/model-labs-to-agent-labs|model-labs-to-agent-labs]] thesis: open-weight models are closing the capability gap with proprietary alternatives, accelerating the commoditization of model quality.

**Source**: [RuntimeWire](https://runtimewire.com/article/deepseek-v4-pro-beats-gpt-5-5-pro-on-precision) (June 7, 2026), HN discussion (284 points, 135 comments)

## Historical Significance

DeepSeek-V4 is a milestone achievement in the following respects:

1. **Practical 1M context**: Hybrid Attention enables processing million-token-length sequences at practical cost
2. **Efficiency revolution**: 3.7-10× FLOPs reduction, 10-14× KV cache reduction vs V3.2 → fundamentally transforms the economics of long-context inference
3. **mHC**: A new regularization paradigm introducing manifold constraints to residual connections
4. **MegaMoE + TileLang**: System software innovations overcoming hardware limitations
5. **On-Policy Distillation**: A new distillation paradigm learning from full logit distributions of multiple specialists
6. **Agent-Native Design**: Interleaved Thinking, Quick Instruction — the first DeepSeek model designed from the start for agent use cases
7. **SWE-bench 80.6%**: First open-weight model to break the 80% barrier. A landmark achievement in democratizing coding agent performance

## Related Pages

- [[entities/deepseek]] — DeepSeek company overview
- [[concepts/deepseek-v3]] — Previous generation architecture
- [[concepts/deepseek-v3-2]] — Immediate predecessor (DSA, scalable RL, agent synthesis)
- [[concepts/deepseek-r1]] — Reasoning-specialized model (origin of GRPO)
- [[concepts/post-training/grpo]] — RL algorithm used in post-training
- [[concepts/mixture-of-experts]] — MoE architecture in general
- [[long-context]] — Long-context processing techniques
- [[concepts/speculative-decoding]] — Speculative decoding
- [[fp4]] — 4-bit quantization
- [[tilelang]] — Kernel development DSL
- [[concepts/inference]] — Inference optimization techniques
