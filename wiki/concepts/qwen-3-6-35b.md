---
title: Qwen 3.6-35B-A3B
created: 2026-05-09
updated: 2026-05-09
type: concept
tags:
  - model
  - open-source
  - coding-agents
  - local-llm
  - multimodal
  - qwen
  - alibaba
sources: [raw/articles/2026-04-15_qwen-3.6-35b-a3b.md]
---

# Qwen 3.6-35B-A3B

The first open-weight model in the Qwen 3.6 family from [[entities/alibaba|Alibaba]], released April 15, 2026 under Apache 2.0 license. A sparse Mixture-of-Experts (MoE) model that delivers agentic coding performance rivaling much larger dense models while running on a single consumer GPU.

## Specifications

| Property | Value |
|----------|-------|
| Total parameters | 35B |
| Active parameters | 3B per token |
| Layers | 40 |
| Architecture | Hybrid: (Gated DeltaNet → MoE) + (Gated Attention → MoE) |
| Experts | 256 total, 8 routed + 1 shared |
| Context (native) | 262,144 tokens |
| Context (extended) | 1,010,000 tokens |
| License | Apache 2.0 |
| Weights format | BF16 |

## Architecture Innovation

The model uses a novel **Gated DeltaNet** attention mechanism — a linear attention variant — combined with standard Gated Attention, both followed by MoE layers. The hidden layout repeats this pattern 10 times: `10 × (3 × (Gated DeltaNet → MoE) → 1 × (Gated Attention → MoE))`.

**DeltaNet specifics**:
- 32 linear attention heads for V, 16 for QK
- Head dimension: 128
- More efficient than standard attention for long sequences

**MoE specifics**:
- 256 total experts, 8 routed + 1 shared active per token
- Expert intermediate dimension: 512
- Trained with multi-step prediction (MTP)

## Performance

| Benchmark | Score |
|-----------|-------|
| SWE-bench Verified | 73.4% |
| GPQA Diamond | 86.0% |
| Overall (BenchLM) | 67/100 |

Competitive with Qwen3.5-27B (dense) and Gemma4-31B (dense), despite having only 3B active parameters.

## Key Features

### Thinking Preservation
A novel capability that retains reasoning context from historical messages across conversation turns. This makes iterative development workflows (code review → fix → re-review) more stable and efficient, reducing redundant reasoning.

### Hardware Requirements
- **Single RTX 4090 (24GB)**: Runs with quantization
- **RTX PRO 6000 (96GB)**: Runs in BF16 without tensor parallelism
- **DFlash speculative decoding**: Up to 6× lossless acceleration

### Multimodal Support
Includes a vision encoder for image understanding alongside text, enabling multimodal thinking and non-thinking modes.

## Adoption

- 3.3M+ Hugging Face downloads in first month
- Supported by Transformers, vLLM, SGLang, KTransformers
- Available via Qwen Studio and Alibaba Cloud Model Studio API

## Significance

Qwen 3.6-35B-A3B demonstrates that sparse MoE models can achieve remarkable agentic coding capability at a fraction of the active parameter count of dense alternatives. Combined with Apache 2.0 licensing, thinking preservation, and single-GPU deployability, it sets a new standard for accessible, production-grade open-source coding models.

## Related Pages
- [[concepts/qwen]] — Qwen model family overview
- [[concepts/mixture-of-experts]] — MoE architecture
- [[concepts/coding-agents]] — AI coding agents
- [[concepts/local-ai]] — Local model inference
- [[entities/alibaba]] — Alibaba (Qwen parent)
- [[concepts/glm-5-1]] — GLM-5.1 (competing open-source coding model)
- [[entities/xiaomi-mimo]] — MiMo-V2.5-Pro
