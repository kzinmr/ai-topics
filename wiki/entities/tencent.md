---
title: Tencent
created: 2026-06-14
updated: 2026-08-13
type: entity
tags:
  - tencent
  - company
  - china
  - model
  - open-source
  - ai-agents
  - multimodal
  - infrastructure
aliases:
  - Tencent Holdings
  - 腾讯
  - Tencent Hy Team
sources:
  - raw/articles/2026-06-14_tencent_hunyuan-hy3-moe.md
  - raw/articles/2026-05-20_tencent-hy3-preview.md
  - raw/newsletters/2026-06-29-import-ai-463-self-improving-robots-a-10k-chinese-gpu-cluster-and-an-elegiac-ess.md
  - raw/newsletters/2026-07-06-tencent-s-open-model-crashes-the-frontier.md
  - https://www.tencent.com/en-us/about.html
  - https://github.com/Tencent-Hunyuan
  - https://huggingface.co/tencent
---

# Tencent

**Tencent** (Chinese: Tengxun) is a Chinese multinational technology conglomerate headquartered in Shenzhen, founded 1998. It is one of the world's largest internet companies (WeChat, QQ, Tencent Games, Tencent Cloud) and, through its **Tencent Hy Team** and the Hunyuan model family, one of China's most aggressive AI model developers — culminating in 2026 with the open-source **Hy3**, the first open-weight model to reach near-frontier agentic capability.

## Overview

Tencent's AI strategy is **product-driven**: models are co-designed with inference and business applications (WeChat, Yuanbao chatbot, CodeBuddy/WorkBuddy dev tools, Tencent Docs) for cost efficiency. Starting February 2026, Tencent rebuilt its pre-training and RL infrastructure around three principles:

1. **Well-rounded capabilities** — balancing reasoning, long-context, instruction following, and tool use
2. **Authentic evaluation** — moving beyond standard benchmarks toward real-world performance
3. **Product-driven integration** — model + inference co-design with business applications

The result was the Hy3 line — a generational leap that made Tencent a frontier AI lab rather than a follower.

## Hunyuan Model Lineage

| Generation | Date | Key facts |
|---|---|---|
| Hunyuan (Hy) | 2023–2024 | Tencent's original LLM line; also spawned image/video/3D generative models |
| Hy2 | 2024–2025 | Prior generation; API + product integrations (Tencent Docs AI PPT) |
| **Hy3 Preview** | Apr 2026 | 295B / 21B active MoE, 192 experts top-8, 256K context; rebuilt infra; open-sourced (Tencent Hy Community License) |
| **Hy3** | Jul 2026 | Official release under **Apache 2.0**; MTP layer; day-0 vLLM support; 2.95× mixed-length decode speedup; Nous Portal + OpenRouter availability |
| Hy-MT2 | Jul 2026 | 30B-A3B translation MoE (GGUF available) |

### Hy3 (2026) — the open frontier breakthrough

Hy3 is the flagship: 295B total / 21B active, 192 experts top-8, 256K context, BF16. Despite the fewest active parameters among peers (vs Kimi-K2 32B, DeepSeek-V3 37B), Hy3-Base led math (MATH 76.28, GSM8K 95.37), multilingual (MMMLU 80.15, INCLUDE 78.64) and several coding benchmarks (CRUXEval-I 71.19, LiveCodeBench-v6 34.86).

- **Agentic performance**: powers complex tasks up to 495 steps (document processing, data analysis, knowledge retrieval, MCP toolchain orchestration)
- **Product gains**: CodeBuddy/WorkBuddy TTFT -54%, end-to-end latency -47%, >99.99% success rate; Tencent Docs AI PPT +20% generation success vs Hy2
- **Economics**: $0.18/M input, $0.06/M cached, $0.59/M output; on OpenRouter via SiliconFlow
- **OpenRouter mystery (May 2026)**: surged to #1 by token volume with almost no public discussion — Max Woolf's analysis suggested a single large app using Hy3 as a data-processing backbone (see [[entities/tencent-hy3]])

### Hunyuan generative model family

Beyond LLMs, Tencent-Hunyuan maintains an extensive open-source generative portfolio:

- **HunyuanVideo** (12.4K GitHub stars) — large video generation framework
- **HunyuanImage-3.0** (3.2K) — native multimodal image generation
- **Hunyuan3D-2.1 / 2mini Turbo** (3.8K) — images-to-3D in ~1 second
- **HunyuanOCR** (1.9K) — lightweight OCR VLM
- **HY-Motion-1.0** — text/image-to-3D motion
- **DepthCrafter** — consistent video depth estimation

## AI Infrastructure

- **ARGUS GPU Cluster Telemetry** (June 2026, arXiv:2606.20374) — low-overhead distributed tracing for 10,000+ GPU clusters; diagnoses compute stragglers, communication link degradation, pipeline bubble amplification, JIT compilation blocking
- **AngelSlim** — model compression toolkit (quantization, speculative sampling)
- **CL-bench / CL-bench-Life** — internally-built context learning benchmarks from real business scenarios

## Products & Integration

- **Yuanbao** — Tencent's consumer AI assistant chatbot
- **CodeBuddy / WorkBuddy** — AI development and work tools (major Hy3 beneficiaries)
- **Tencent Docs AI PPT** — presentation generation (Hy3: +20% success vs Hy2)
- **WeChat ecosystem** — AI features integrated into China's dominant super-app
- **Tencent Cloud TokenHub** — model API distribution
- **Hy-Embodied-VLM-1.0 / RxBrain-1.0** — embodied AI / robotics VLMs (July 2026)

## Key People

- **Yao Shunyu** — Chief AI Scientist, Tencent; quoted on the Hy3 rebuild: "At Tencent, we are continuously expanding the scale of our pre-training and reinforcement learning efforts to push the boundaries of model intelligence."

## Competitive Positioning

Tencent's 2026 strategy mirrors the Chinese open-weight surge: release frontier-adjacent models under permissive licenses (Apache 2.0 for Hy3) with day-0 infrastructure support (vLLM), positioning the model as an infrastructure foundation rather than a proprietary product.

| Dimension | Tencent Hy3 | [[entities/deepseek|DeepSeek V4]] | [[entities/qwen|Qwen 3.8]] |
|---|---|---|---|
| Total params | 295B | 1.6T | ~2.4T |
| Active params | 21B | — | 95B |
| License | Apache 2.0 | Open | Source-available (revenue threshold) |
| Context | 256K | — | up to 1M |
| Signature strength | Agentic tasks, efficiency | Cache-pricing economics | Scale, local ecosystem |

## Related

- [[entities/tencent-hy3]] — Hy3 model entity (pricing, OpenRouter analysis, product integration)
- [[concepts/hunyuan-hy3]] — Hunyuan Hy3 concept page (architecture, benchmarks)
- [[entities/qwen|Qwen (Alibaba)]] — Chinese rival model lab
- [[entities/baidu|Baidu (Ernie)]] — Chinese rival model lab
- [[entities/deepseek|DeepSeek]] — competing MoE provider
- [[entities/kimi|Moonshot AI (Kimi)]] — Chinese rival
- [[entities/china-ai-industry]] — China AI industry context
- [[concepts/mixture-of-experts]] — MoE architecture
- [[concepts/open-source-ai]] — Open-source AI strategy
- [[concepts/ai-economics]] — LLM pricing and unit economics

## Sources

- [Tencent official site](https://www.tencent.com/en-us/about.html)
- [GitHub: Tencent-Hunyuan](https://github.com/Tencent-Hunyuan)
- [HuggingFace: tencent](https://huggingface.co/tencent)
- raw/articles/2026-06-14_tencent_hunyuan-hy3-moe.md
- raw/articles/2026-05-20_tencent-hy3-preview.md
- raw/newsletters/2026-07-06-tencent-s-open-model-crashes-the-frontier.md
