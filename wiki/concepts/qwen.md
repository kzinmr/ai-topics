---
title: Qwen Model Family
created: 2026-04-25
updated: 2026-05-23
type: concept
tags:
  - model
  - open-source
  - alibaba
  - coding-agents
  - multimodal
  - local-llm
sources:
  - raw/articles/2026-04-15_qwen-3.6-35b-a3b.md
  - raw/newsletters/2026-05-22-nvidia-s-ai-factory-boom-hits-81-6b.md
  - raw/newsletters/2026-05-23-ainews-all-model-labs-are-now-agent-labs.md
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


### Qwen 3.7 Max (May 2026)

| Attribute | Value |
|-----------|-------|
| AA Intelligence Index | **56.6** (+4.8pt over preview) |
| Key Gains | Scientific reasoning, coding, agentic capability, reduced hallucination |
| Caveat | Improvement partly from abstention (not answering uncertain questions) and higher token usage — not pure intelligence gain |

Qwen3.7 Max represents Alibaba's frontier push. The 56.6 AA Intelligence Index score places it competitively against GPT-5.5 and Claude Opus 4.5 on scientific reasoning and coding benchmarks.

**Caveat**: The 4.8-point jump is partially attributable to increased abstention rates (the model declines to answer when uncertain rather than guessing) and higher token usage per prompt. This means the apparent gain may not translate linearly to real-world agentic performance where answering is required.

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
