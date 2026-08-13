---
title: Qwen
created: 2026-07-15
updated: 2026-08-13
type: entity
tags:
  - qwen
  - alibaba
  - model
  - company
  - open-source
  - multimodal
  - china
  - local-llm
  - reasoning
  - coding-agents
aliases:
  - Tongyi Qianwen
  - 通义千问
  - Qwen Team
sources:
  - raw/articles/2026-04-15_qwen-3.6-35b-a3b.md
  - raw/articles/2026-07-19_qwen-3-8-launch.md
  - raw/articles/2026-08-03_qwen-qwen3.8-max-release.md
  - raw/articles/2026-07-29_qwen_qwen-mm-plugins.md
  - raw/articles/2026-06-24_arxiv-2606.24597_qwen-agentworld.md
  - https://en.wikipedia.org/wiki/Qwen
  - https://qwen.ai
  - https://huggingface.co/Qwen
---

# Qwen

**Qwen** (Chinese: Tongyi Qianwen, "to comprehend the meaning, and to answer a thousand kinds of questions") is a family of large language models developed by **Alibaba Group's** Cloud Intelligence unit. It is one of the most widely adopted open-weight model families in the world — the backbone of China's open-source AI ecosystem and a frequent base model for fine-tuning, quantization, and derivative projects globally.

## Overview

Qwen began as a proprietary Alibaba Cloud chatbot (beta April 2023, public September 2023) and evolved into a sprawling open-weight family spanning dense and MoE LLMs, vision-language models, audio/omni models, math and coding variants. Its defining traits:

- **Permissive licensing** — most releases are Apache 2.0 (commercial-friendly, no usage restrictions); newer frontier models use a source-available license with revenue thresholds
- **Efficiency focus** — MoE variants (e.g., Qwen3.6-35B-A3B, 3B active) deliver frontier-adjacent performance on consumer hardware
- **Multilingual strength** — strong Chinese + English + 100+ language coverage, making it the default base for regional fine-tunes
- **Agentic direction** — 2026 releases (3.7 Max, 3.8 Max, Qwen-MM-Plugins, Qwen-AgentWorld) pivot toward long-horizon autonomous agents

By 2026 Qwen models had been downloaded **40M+ times** (Wikipedia citation, 2024 figure) with **200,000+ community variants** on Hugging Face; the Qwen app reached **234 million users** by May 2026.

## Model Lineage

| Generation | Date | Key models | Notes |
|---|---|---|---|
| Qwen 1 (Tongyi Qianwen) | Apr 2023–Dec 2023 | 1.8B–72B | Llama-based architecture; weights released Aug–Dec 2023 |
| Qwen2 | Jun 2024 | 0.5B–72B + 57B-A14B MoE | First generation with Apache 2.0 for most sizes |
| Qwen2.5 | Sep 2024 | 0.5B–72B, Qwen2.5-Coder | Coding variants; Qwen2.5-Max (Jan 2025) |
| QwQ / QvQ | Nov 2024–Mar 2025 | QwQ-32B-Preview, QwQ-32B | Reasoning models in the o1 style, Apache 2.0 |
| Qwen2.5-VL / Omni | Jan–Mar 2025 | 3B–72B VL; Omni-7B | Vision-language and real-time omni-modal |
| Qwen3 | Apr 2025 | 0.6B–32B dense; 30B-A3B, 235B-A22B MoE | Thinking/non-thinking mode switching; 36T tokens, 119 languages; Qwen3-Max >1T proprietary |
| Qwen3.5 | Feb 2026 | Open Qwen3.5 + proprietary 3.5-Plus | Desktop/mobile app operation; Coder-Next |
| Qwen3.6 | Apr 2026 | 35B-A3B (open), 3.6-Plus (proprietary), 3.6-27B | Hybrid Gated DeltaNet→MoE architecture; thinking preservation; SWE-bench Verified 73.4% |
| Qwen3.7 Max | May 2026 | 3.7-Max, 3.7-Plus | 1M context; AA Intelligence Index 56.6; long-horizon agent focus |
| Qwen3.8 | Jul–Aug 2026 | **3.8-Max** (~2.4T total / 95B active MoE), 3.8-27B | First open-weight Max-class release; $2/$6 per M pricing; Qwen3.8-2.4T-A95B weights Aug 12 |

### Qwen 3.8 — the frontier push (July–August 2026)

Qwen3.8-Max is the largest model in the family: **~2.4T total / ~95B active** sparse MoE with up to **1M context**. Announced July 19, 2026 (days after [[concepts/kimi-k3|Kimi K3]]), cloud release August 3, open weights August 12 as **Qwen3.8-2.4T-A95B**. Early community analysis places it at the frontier: reportedly ahead of GPT-5.6 Sol, narrowly behind Claude Fable 5. Benchmarks: Arena frontend-code 4th (1,668), TerminalBench 2.1 86.6, PaperBench 93.0 (vs GPT-5.6 Sol 90.5), SWE-bench Pro 67.7.

Key features: `reasoning_effort` control (xhigh/medium/low), "self-evolving" feedback loops during autonomous operation, and the **oh-my-cli** demonstration — a 448+ commit, 125-hour autonomous research loop and an autonomous chip design flow (GCD/RSA accelerator, 8,298→678 gates) run without human-written commits.

**License note**: Qwen3.8-2.4T-A95B requires a commercial license from Alibaba for providers generating >US$50M revenue within 12 months — a shift from the pure Apache 2.0 pattern of earlier generations.

## Architecture & Technical Highlights

- **Hybrid attention (3.6 generation)**: Gated DeltaNet + Gated Attention alternating with MoE layers — a departure from pure attention that improves efficiency
- **Thinking preservation**: retains reasoning context across conversation turns for stable iterative development workflows
- **MoE efficiency**: 35B-A3B runs on a single RTX 4090 (quantized); RTX PRO 6000 (96GB) runs BF16 without tensor parallelism
- **Speculative decoding**: DFlash up to 6× lossless acceleration
- **Multimodal**: vision encoders in recent releases; Qwen2.5-Omni accepts text/images/video/audio, outputs text+audio

## Agent Ecosystem (2026)

- **[[entities/qwen-mm-plugins|Qwen-MM-Plugins]]** (Jul 2026) — open-source skill+MCP plugin system making any agent harness multimodal-native: vision, video-memory, video-edit, Blender 3D, FreeCAD, edu-agent. Supports Claude Code, Codex, Qoder, OpenClaw, Qwen Code, Gemini CLI
- **[[concepts/qwen-agentworld|Qwen-AgentWorld]]** (Jun 2026) — 397B MoE language world model trained via CPT→SFT→RL on 7 domain environments; enables agent policy training without real environment access
- **oh-my-cli** — autonomous coding agent built on Qwen3.8-Max (see above)
- **Accio** — Alibaba's B2B AI-native shopping/sourcing app built on Qwen

## Organization & People

Qwen is developed by the **Tongyi Large Model Business Unit** (formerly Tongyi Laboratory) inside Alibaba Cloud, under the **Alibaba Token Hub** AI business unit (formed March 2026, led by CEO Eddie Wu; Zhou Jingren as chief AI architect, Wu Zeming as CTO).

- **[[entities/jianlin-su|Jianlin Su]]** — Alibaba-affiliated researcher; inventor of RoPE, adopted by Qwen and virtually all major open LLMs
- **Lin Junyang** — former Qwen model division head, resigned March 2026 after Qwen3.5 release
- **Qwen Exodus** — key Qwen team members departed in 2026 to found [modelfit.io](https://modelfit.io); Qwen3.8-Max is widely framed as the team's final major release under Alibaba

## Ecosystem & Derivatives

- **Base for fine-tunes**: 200K+ Hugging Face variants; e.g., [[concepts/bonsai-27b|Bonsai 27B]] by [[entities/prism-ml|Prism ML]], Xiaomi MiMo, DeepReinforce Ornith
- **Sea-Lion** (AI Singapore, Nov 2025): replaced LLaMA with Qwen as the regional LLM base
- **Inference engines**: vLLM, SGLang, KTransformers, Transformers
- **Distribution**: Hugging Face, ModelScope (Alibaba's China-accessible hub), Qwen Studio / Alibaba Cloud Model Studio
- **US-China policy note**: the US-China Economic and Security Review Commission credits China's open-source approach (exemplified by Qwen) with helping overcome compute constraints

## Competitive Positioning

Qwen competes at every tier of the Chinese and global model landscape:

| Tier | Qwen offering | Rivals |
|---|---|---|
| Frontier (closed API) | Qwen3.7/3.8 Max, ~$1.30–$2.00 in / $6–7.80 out per M | [[entities/deepseek|DeepSeek]], [[entities/tencent-hy3|Tencent Hy3]], GPT-5.x, Claude |
| Open frontier | Qwen3.8-2.4T-A95B (open weights) | [[concepts/kimi-k3|Kimi K3]], DeepSeek V4 |
| Efficient MoE / local | Qwen3.6-35B-A3B | GLM, MiniMax, [[entities/xiaomi-mimo|MiMo]] |
| Local dense | Qwen3.6/3.8-27B | Llama, Gemma |

Qwen's strategy mirrors [[concepts/open-source-ai|open-source AI]] advocacy: use Apache 2.0 releases to seed ecosystem lock-in, then monetize via Alibaba Cloud API. The 2026 shift toward revenue-threshold licensing for frontier models marks a partial retreat from that pattern.

## Related

- [[concepts/qwen]] — Qwen Model Family concept page (pricing, generations)
- [[concepts/qwen-3-8]] — Qwen 3.8 deep dive
- [[concepts/qwen-3-6-35b]] — Qwen3.6-35B-A3B deep dive
- [[concepts/qwen3-6-27b]] — Qwen3.6-27B
- [[entities/qwen-3-7-max]] — Qwen 3.7 Max entity
- [[entities/qwen-mm-plugins]] — Multimodal plugin system
- [[entities/tencent|Tencent (Hunyuan)]] — Chinese rival model lab
- [[entities/baidu|Baidu (Ernie)]] — Chinese rival model lab
- [[entities/china-ai-industry]] — China AI industry context
- [[concepts/mixture-of-experts]] — MoE architecture
- [[concepts/model-quantization]] — Quantization ecosystem that Qwen anchors
- [[concepts/local-llm/local-ai]] — Local LLM deployment

## Sources

- [Wikipedia: Qwen](https://en.wikipedia.org/wiki/Qwen)
- [Qwen official blog](https://qwen.ai)
- [HuggingFace: Qwen](https://huggingface.co/Qwen)
- [GitHub: QwenLM](https://github.com/QwenLM)
- raw/articles/2026-04-15_qwen-3.6-35b-a3b.md
- raw/articles/2026-07-19_qwen-3-8-launch.md
- raw/articles/2026-08-03_qwen-qwen3.8-max-release.md
- raw/articles/2026-07-29_qwen_qwen-mm-plugins.md
- raw/articles/2026-06-24_arxiv-2606.24597_qwen-agentworld.md
