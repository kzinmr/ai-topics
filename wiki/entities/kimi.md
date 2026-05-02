---
title: "Moonshot AI / Kimi"
aliases:
  - moonshot-ai
  - moonshotai
  - kimi-k2
tags:
  - company
  - model
  - china
  - open-source
created: 2026-04-30
updated: 2026-04-30
type: entity
---

# Moonshot AI / Kimi

> **Moonshot AI** (月之暗面, *Yuè Zhī Ànmiàn* — "Dark Side of the Moon") is a Beijing-based Chinese AI company and one of China's "AI Tigers." Founded in March 2023 by Tsinghua University alumni, the company is best known for its **Kimi** series of large language models and the eponymous chatbot, which pioneered ultra-long context windows. Moonshot has established a reputation for open-weight releases and competitive performance against frontier Western models.

---

## Company Background

### Founding & Name

Moonshot AI was founded in March 2023 by **Yang Zhilin** (CEO), **Zhou Xinyu**, and **Wu Yuxin** — all alumni of Tsinghua University. The company launched on the 50th anniversary of Pink Floyd's *The Dark Side of the Moon*, Yang's favorite album, which inspired the Chinese name. The English name "Moonshot" reflects the ambitious nature of the mission — described by Yang as "like landing on the moon."

### Mission & Vision

Yang Zhilin has stated three milestones toward the company's goal of achieving AGI:

1. **Long context length** — processing large volumes of information in a single pass
2. **Multimodal world model** — understanding text, images, and video natively
3. **Scalable general architecture** — capable of continuous self-improvement without human input

### Funding & Valuation

Moonshot has raised aggressively from Chinese tech giants, reaching an **~$18 billion valuation** by early 2026:

| Date | Amount | Valuation | Lead Investors |
|------|--------|-----------|----------------|
| 2023 | $60M | $300M | — |
| Feb 2024 | $1B | $2.5B | Alibaba (36% stake) |
| Aug 2024 | $300M | $3.3B | Tencent, Gaorong Capital |
| Dec 2025 | $500M | $4.3B | IDG, Alibaba, Tencent |
| Jan 2026 | $700M+ | $10B | Alibaba, Tencent, 5Y Capital |
| Mar 2026 | ~$1B | ~$18B | Existing backers (expanded round) |

The company is reportedly considering an IPO on the Hong Kong Stock Exchange.

### Products & Platforms

- **Kimi Chatbot** — consumer-facing AI assistant (web, iOS, Android)
- **Kimi App** — desktop/mobile application
- **Kimi API** — platform.moonshot.ai (OpenAI-compatible)
- **Kimi Code** — terminal & IDE agent for developers
- **Kimi Researcher** — autonomous research agent
- **Kimi Audio & Kimina Prover** — specialized capabilities
- **OK Computer** — agentic feature for multi-page website/slide creation
- **Mooncake** — serving platform processing 100B tokens daily (awarded Erik Riedel Best Paper at USENIX FAST)

### Controversies

In February 2026, **Anthropic** accused Moonshot of using thousands of fraudulent accounts to harvest data from Claude for training.

---

## Kimi Model Family Overview

Moonshot has maintained a rapid **2–3 month major-update cadence** since mid-2025. The model family evolution:

| Model | Release | Key Features |
|-------|---------|-------------|
| **Kimi v1** | Oct 2023 | First public chatbot; 128K token context |
| **Kimi (2M chars)** | Mar 2024 | Expanded to 2M Chinese character context |
| **Kimi K1.5** | Jan 2025 | Reasoning model matching OpenAI o1 in math/coding |
| **Kimi-VL** | Apr 2025 | Open-source 16B MoE (3B active) vision-language model |
| **Kimi-Dev** | Jun 2025 | 72B coding model; SOTA on SWE-bench Verified |
| **Kimi K2** | Jul 2025 | **1T parameter MoE** (32B active); open-weight under Modified MIT License |
| **K2-Thinking** | Nov 2025 | Chain-of-thought reasoning variant; outperformed GPT-5 and Claude 4.5 on key benchmarks |
| **Kimi K2.5** | Jan 2026 | Multimodal MoE + **MoonViT** vision encoder (400M params); native video/image + Agent Swarm v1 |
| **Kimi K2.6** | Apr 2026 | **Current flagship** — 12-hour execution, 300-agent swarms, long-horizon coding |

### Open-Weight Licensing

K2, K2.5, and K2.6 are released under a **Modified MIT License** requiring attribution for products exceeding 100M monthly users or $20M monthly revenue.

---

## Kimi K2.6 — Flagship Model

### Architecture

| Specification | Value |
|--------------|-------|
| Organization | Moonshot AI |
| Model Type | Mixture of Experts (MoE) |
| Total Parameters | ~1 Trillion |
| Active Parameters | 32B |
| Number of Experts | 384 (8 routed + 1 shared per token) |
| Attention | MLA (Multi-head Latent Attention) — same variant as DeepSeek V3 |
| Context Window | 256K tokens |
| Quantization | Native INT4 |
| Multimodality | Native (text, images, video without separate vision modules) |
| Optimizer | MuonClip (Moonshot's custom optimizer for trillion-param MoE stability) |
| Activation | SwiGLU |

### Four Variants

| Variant | Purpose |
|---------|---------|
| **Instant** | Low-latency chat for speed-critical use |
| **Thinking** | Deep chain-of-thought reasoning |
| **Agent** | Autonomous research and document tasks |
| **Agent Swarm** | Large-scale parallel work (up to 300 concurrent sub-agents) |

### Key Features

#### 1. Long-Horizon Coding

K2.6 demonstrated exceptional autonomous execution capability:

- **Qwen3.5-0.8B Local Deployment:** Deployed a model on Mac via Zig implementation — 4,000+ tool calls, 12+ hours continuous execution, 14 iterations, throughput from ~15 to ~193 tokens/sec (~20% faster than LM Studio)
- **Exchange-Core Financial Engine Overhaul:** Autonomously overhauled an 8-year-old open-source matching engine — 13-hour execution, 12 optimization strategies, 1,000+ tool calls, 4,000+ lines modified, **185% medium throughput leap** (0.43→1.24 MT/s), **133% peak throughput gain** (1.23→2.86 MT/s)
- Supports **4,000+ sequential tool calls** per run
- Multi-language capability: Rust, Go, Python, Zig

#### 2. Agent Swarm Architecture

K2.6 is the first LLM to integrate agent swarm capabilities natively into the training objective (rather than bolted on at the API layer):

- **Up to 300 concurrent sub-agents** in parallel
- **4,000 steps per run**
- Deployed in production autonomous scenarios including OpenClaw and Hermes Agent
- Swarm behavior is a **first-class capability**, not an orchestration layer

#### 3. Long Context & Attention Optimization

- **256K token context window** with MLA (Multi-head Latent Attention)
- **FlashKDA** — high-performance Kimi Delta Attention kernels with ~1.7–2.2× speedup over chunked KDA
- Context caching for repeated long-document queries
- Designed for document-level reasoning and multi-file codebase understanding

### Benchmarks

| Benchmark | K2.6 Score | Notes |
|-----------|-----------|-------|
| **BrowseComp** | 83.2 | Strong web-browsing comprehension |
| **SWE-Bench Verified** | 80.2 | Software engineering benchmark |
| **SWE-Bench Pro** | SOTA-class | Professional-grade engineering tasks |
| **SWE-Multilingual** | SOTA-class | Multi-language code repair |
| **Terminal-Bench 2.0 (Terminus-2)** | 66.7 | Terminal-based coding agent benchmark |
| **Humanity's Last Exam (Full) w/ tools** | SOTA-class | Hardest general knowledge + tool use |
| **DeepSearchQA (f1-score)** | SOTA-class | Deep search and retrieval |
| **Toolathlon** | SOTA-class | Multi-tool orchestration |
| **OSWorld-Verified** | SOTA-class | OS-level agent tasks |
| **MathVision w/ python** | SOTA-class | Visual math reasoning |
| **V\* w/ python** | SOTA-class | Visual question answering |

### Deployment Options

- **Kimi.com** — web interface (chat + agent modes)
- **Kimi App** — desktop & mobile
- **API** — platform.moonshot.ai
- **Kimi Code** — terminal & IDE agent
- **Cloudflare Workers AI** — Day-0 support via `@cf/moonshotai/kimi-k2.6`
- **Hugging Face** — open weights: `moonshotai/Kimi-K2.6`
- **Local GGUF** — community quantizations (Q4_X variants, ~8GB VRAM)

---

## Technical Innovations

### Muon / MuonClip Optimizer

Moonshot developed the **Muon optimizer** (later MuonClip) to stabilize training at trillion-parameter scale. MoE models are prone to attention explosions and loss spikes at that size; MuonClip achieves ~**2× computational efficiency** compared to AdamW for large models.

### Mooncake Serving Platform

The Mooncake inference serving platform processes **100 billion tokens daily** and was awarded the **Erik Riedel Best Paper Award** at USENIX FAST, a top-tier systems conference.

### Kimi Delta Attention (KDA)

A proprietary attention method — implemented as **FlashKDA** — that improves generation speed and reduces memory overhead during long-context processing with ~1.7–2.2× speedup over prior chunked approaches.

### MoonViT Vision Encoder

A 400M-parameter vision encoder introduced with K2.5, enabling native video and image understanding without cascaded vision modules.

---

## Competitive Position

Moonshot has maintained the leading position among **Chinese open-source model labs** since DeepSeek v3.2 in late 2025. K2.6 competes directly with:

| Competitor | Comparison |
|-----------|-----------|
| **Claude Opus 4.6/4.7** | Comparable on agentic and coding benchmarks |
| **GPT-5.4** | Competes on agentic benchmarks like BrowseComp |
| **DeepSeek V4** | Rival Chinese open-source model |
| **Qwen3.6 35B MoE** | Competing open-source MoE (different scale class) |

---

## Related Pages

- [[concepts/kimi-k2-5]] — Previous generation (January 2026)
- [[concepts/kimi-k2-6]] — Technical deep dive on K2.6 architecture
- [[concepts/kimi-k2-thinking]] — November 2025 reasoning variant
- [[concepts/deepseek-v3]] — Competitor from DeepSeek
- [[qwen3-6-plus|Qwen3.6 35B MoE]] — Competing open MoE model
- [[concepts/open-model-consortium]]

---

## References

- [Moonshot AI Official Site](https://www.moonshot.ai)
- [Kimi Chatbot](https://www.kimi.com)
- [API Platform](https://platform.moonshot.ai)
- [Kimi K2.6 on Hugging Face](https://huggingface.co/moonshotai/Kimi-K2.6)
- [Kimi K2.6 Blog Post](https://www.kimi.com/blog/kimi-k2-6)
- [Kimi K2.6 on Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/models/kimi-k2.6/)
- [Wikipedia: Moonshot AI](https://en.wikipedia.org/wiki/Moonshot_AI)
- [Wikipedia: Kimi (chatbot)](https://en.wikipedia.org/wiki/Kimi_(chatbot))
