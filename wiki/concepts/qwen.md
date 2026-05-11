---
title: Qwen Model Family
created: 2026-04-25
updated: 2026-05-09
type: concept
tags:
  - model
  - open-source
  - alibaba
  - coding-agents
  - multimodal
  - local-llm
sources: [raw/articles/2026-04-15_qwen-3.6-35b-a3b.md]
---

# Qwen Model Family

Open-source large language model family from [[entities/alibaba|Alibaba]]'s Qwen Team. Known for efficient architectures, strong multilingual performance, and permissive licensing (Apache 2.0 for most releases).

## Model Generations

### Qwen 3.6 (April 2026)

| Model | Total Params | Active Params | Type | License |
|-------|-------------|---------------|------|---------|
| Qwen3.6-Plus | — | — | Dense, API-only | Proprietary |
| **[[concepts/qwen-3-6-35b|Qwen3.6-35B-A3B]]** | 35B | 3B | Sparse MoE | Apache 2.0 |

Qwen3.6-35B-A3B is the first open-weight Qwen3.6 model, achieving 73.4% on SWE-bench Verified with only 3B active parameters. Introduces **thinking preservation** — retaining reasoning context across conversation turns for stable iterative development workflows.

### Qwen 3.5 (2025)

- Qwen3.5-35B-A3B: Predecessor to 3.6-35B-A3B
- Qwen3.5-27B: 27B dense model
- Strong performance on coding and reasoning benchmarks

## Key Characteristics

- **Efficiency focus**: MoE variants achieve frontier-adjacent performance with dramatically fewer active parameters
- **Single-GPU deployability**: Models like Qwen3.6-35B-A3B run on consumer hardware (RTX 4090 with quantization)
- **Apache 2.0 licensing**: Commercial-friendly, no usage restrictions
- **Multimodal support**: Vision encoder in recent releases
- **Long context**: Up to 1M tokens (extended) in recent variants

## Ecosystem

- **Hugging Face**: Primary distribution channel, 3.3M+ downloads for Qwen3.6-35B-A3B
- **Inference engines**: vLLM, SGLang, KTransformers, Transformers
- **API**: Qwen Studio, Alibaba Cloud Model Studio

## Related Pages
- [[concepts/qwen-3-6-35b]] — Qwen 3.6-35B-A3B deep dive
- [[entities/alibaba]] — Alibaba (parent company)
- [[concepts/mixture-of-experts]] — MoE architecture
- [[concepts/local-ai]] — Local model inference
- [[concepts/coding-agents]] — AI coding agents
- [[entities/xiaomi-mimo]] — MiMo-V2.5-Pro
- [[concepts/glm-5-1]] — GLM-5.1
