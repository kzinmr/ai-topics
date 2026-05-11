---
title: Xiaomi MiMo (Model Family)
created: 2026-05-09
updated: 2026-05-09
type: entity
tags:
  - model
  - open-source
  - coding-agents
  - multimodal
  - china
  - xiaomi
sources: [raw/articles/2026-04-23_xiaomi-mimo-v2.5-pro.md]
---

# Xiaomi MiMo Model Family

Open-source large language model family from [[entities/xiaomi|Xiaomi]], released under MIT license. The MiMo family spans multimodal perception models to trillion-parameter agentic coding specialists.

## Model Lineage

| Model | Released | Total Params | Active Params | Context | Focus |
|-------|----------|-------------|---------------|---------|-------|
| MiMo-V2-Flash | Dec 2025 | — | — | — | Initial release |
| MiMo-V2-Omni | Mar 2026 | — | — | 256K | Text, vision, speech |
| MiMo-V2-Pro | Mar 2026 | 1T | 42B | 1M | Agentic coding |
| **MiMo-V2.5-Pro** | Apr 2026 | 1.02T | 42B | 1M | **Flagship agentic** |
| MiMo-V2.5 | Apr 2026 | 310B | 15B | 1M | Native multimodal |
| MiMo-V2.5-TTS | Apr 2026 | — | — | — | Text-to-speech |

## MiMo-V2.5-Pro (Flagship)

The most capable MiMo model, designed for complex software engineering and long-horizon agentic tasks.

### Architecture
- **MoE**: 1.02T total, 42B active parameters
- **Hybrid attention**: Interleaves sliding-window attention (SWA) and global attention (GA) at 6:1 ratio, 128-token window
- **KV-cache efficiency**: ~7x reduction vs standard attention
- **Training**: 27T tokens, FP8 mixed precision, native 32K sequence length, extended to 1M

### Post-Training (3-stage)
1. **Supervised Fine-Tuning** (SFT): Foundation instruction following
2. **Domain-Specialized Training**: Separate teacher models optimized via domain-specific RL (math, safety, agentic tool-use)
3. **Multi-Teacher On-Policy Distillation (MOPD)**: Student model learns from its own rollouts under token-level guidance from all specialist teachers

### Performance
- SWE-bench Pro: Comparable to Claude Opus 4.6
- GDPVal-AA Elo: 1581 (surpasses Kimi K2.6, GLM 5.1)
- Can autonomously complete tasks requiring 1000+ tool calls
- Output speed: 55.6 tokens/sec (median)

### Pricing
- Up to 256K context: $1/M input, $3/M output
- Up to 1M context: $2/M input, $6/M output

## MiMo-V2.5 (Multimodal)

Native full-modal perception model supporting video, audio, image, and text. 310B total, 15B active. Positioned at the Pareto frontier of performance and efficiency.

## Significance

MiMo-V2.5-Pro demonstrates that open-source models can achieve frontier-level agentic coding performance. The MOPD training approach — using multiple specialist teachers to distill into a single student — represents an innovative post-training methodology. Combined with MIT licensing, this makes MiMo one of the most accessible high-performance agentic coding models.

## Related Pages
- [[entities/xiaomi]] — Xiaomi company
- [[concepts/mixture-of-experts]] — MoE architecture
- [[concepts/coding-agents]] — AI coding agents
- [[concepts/glm-5-1]] — GLM-5.1 (competing open-source coding model)
- [[entities/deepseek]] — DeepSeek V4
- [[concepts/qwen]] — Qwen model family
- [[concepts/multimodal]] — Multimodal models
