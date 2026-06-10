---
title: Xiaomi MiMo (Model Family)
created: 2026-05-09
updated: 2026-06-10
type: entity
tags:
  - model
  - open-source
  - coding-agents
  - multimodal
  - china
  - xiaomi
sources:
  - raw/articles/2026-04-23_xiaomi-mimo-v2.5-pro.md
  - raw/articles/2026-06-08_xiaomi-mimo-tilert-1000tps.md
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
| **MiMo-V2.5-Pro-UltraSpeed** | Jun 2026 | 1.02T | 42B | 1M | **1000 tok/s inference** |

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

## MiMo-V2.5-Pro-UltraSpeed (June 2026)

Ultra-high-speed inference variant developed in collaboration with [[entities/tilert|TileRT]]. First 1T-parameter model to break **1000 tokens/s** on commodity GPUs.

### Key Technologies
- **FP4 (MXFP4) quantization**: MoE Experts only, other modules retain original precision. FP4 QAT keeps capability on par with FP8.
- **DFlash speculative decoding**: Block-level masked parallel prediction ([arXiv:2602.06036](https://arxiv.org/abs/2602.06036)). Draft model fills entire block of masked positions in single forward pass. Acceptance lengths: Coding 6.30, Math 5.56, Agent 4.29.
- **TileRT persistent kernel**: Entire compute pipeline resident on GPU, launched once. Warp specialization for heterogeneous pipeline collaboration.

### Access
- API: https://platform.xiaomimimo.com/ultraspeed (3× standard price, ~10× speed)
- Chat: https://ultraspeed.xiaomimimo.com
- Trial: June 9-23, 2026 (application-based)
- Open-source checkpoint: https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash

## Significance

MiMo-V2.5-Pro demonstrates that open-source models can achieve frontier-level agentic coding performance. The MOPD training approach — using multiple specialist teachers to distill into a single student — represents an innovative post-training methodology. Combined with MIT licensing, this makes MiMo one of the most accessible high-performance agentic coding models.

## Pricing

- **May 26, 2026**: MiMo-V2.5 Series API pricing permanently reduced — up to **99%** compared to previous pricing. Unified pricing across all context lengths. MiMo Token Plans also upgraded to 5–8× more usable tokens. [Source: @XiaomiMiMo](https://x.com/XiaomiMiMo/status/2059314052892099070)

## Related Pages
- [[entities/xiaomi]] — Xiaomi company
- [[concepts/mixture-of-experts]] — MoE architecture
- [[concepts/coding-agents]] — AI coding agents
- [[concepts/glm-5-1]] — GLM-5.1 (competing open-source coding model)
- [[entities/deepseek]] — DeepSeek V4
- [[concepts/qwen]] — Qwen model family
- [[concepts/multimodal]] — Multimodal models
- [[entities/tilert]] — TileRT inference engine (UltraSpeed backend)
- [[concepts/speed-as-scaling-law]] — Speed as the next scaling law
