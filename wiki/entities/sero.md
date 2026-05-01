---
title: "Sero (0xSero)"
tags: [person]
created: 2026-04-24
updated: 2026-04-24
type: entity
---


# Sero (@0xsero)

## Overview

Sero (known online as **0xSero**) is an open-source developer, AI infrastructure builder, and founder of **Sybil Solutions**. He operates at the intersection of AI agents, blockchain infrastructure, and developer tooling. He is a major contributor to **ElizaOS** (17k+ GitHub stars) and has built numerous open-source tools focused on local AI, privacy-first data extraction, and multi-agent orchestration.

He runs an **8x RTX 3090 homelab** (192GB VRAM, 512GB RAM) for local model inference and is a vocal advocate for **"Freedom Tech"** — systems that give individuals control over their data and AI workflows rather than creating corporate dependency. His philosophy centers on "boring reliability," data ownership, and the conviction that competitive AI inference is now achievable on consumer hardware.

## Background

- **Founder**, Sybil Solutions — AI infrastructure and developer tools
- **Current**: Building **Thrive Protocol** — AI systems that automate treasury allocations from crypto ecosystems to builders ($150M+ committed capital, 1,800+ funded builders)
- **Previous**: Ethereum Foundation, ZKSync governance infrastructure, MakerDAO, Gnosis, Superfluid, Lens Protocol
- **Contributor**, ElizaOS — agentic framework (17k+ stars)
- **Co-author**, "Single-agent AI coding is a nightmare for engineers" (with @MilksandMatcha, April 2026) — Back of House multi-agent patterns, kitchen metaphor (Head Chef/Line Cook), 5 workflow patterns
- **Podcast Host**, Ethers Club — 57 episodes with builders on technology, business, and spirituality
- **Location**: United States

His trajectory: Content protection (DMCA takedowns, creator rights) → Web3/DAOs (governance infra) → AI Infrastructure (agents, local models, developer tools). He describes becoming a father as a turning point that shifted his focus toward building systems that give individuals more control.

> "This age is coming to a close, models are using 6x the tokens, we have hit the token price floor... What this means for us is 30-100$ a day in usage if you use this." — @seroxdesigns

## Weekly Hardware-Tier Model Recommendations

Starting April 2026, Sero publishes a weekly curated list of the best local models organized by available VRAM/RAM. The series covers 8 tiers: **8 GB → 512 GB**, with specific model recommendations for autocomplete, tool calling, multimodal, coding, agentic, and general use cases.

**Methodology:** Each tier features the best available model for that memory budget, with direct HuggingFace links to GGUF/requantized variants. The series reflects his hands-on experience running an 8x RTX 3090 homelab and testing dozens of open-weight models in real workflows.

**Notable picks from April 2026:**
- **8 GB**: Zeta-2 (autocomplete), NVIDIA Nemotron-3 Nano 4B (tool calling)
- **24 GB**: Qwen3.5-27B ("the best model you can get"), Nemotron-Cascade-2-30B-A3B (agentic)
- **96 GB**: Hermes-70B jailbroken, Nemotron-120B-Super (OpenClaw deployment)
- **256 GB**: MiniMax-M2.5 6-bit MLX (#1), Qwen3.5-262B-REAP (#2)
- **512 GB**: MiniMax-M2.* FP16 (#1), Qwen3.5-397B 8-bit (#2)

Source: [X thread](https://x.com/0xsero/status/2037837722094641610)

## Key Open-Source Projects

### AI Data Extraction Toolkit (594+ stars)
- Python toolkit to extract complete conversation history, code context, and metadata from AI coding assistants (Claude Code, Cursor, Codex, Windsurf, Trae)
- Outputs structured JSONL files ready for ML training
- Built to solve the problem of developers not having access to their own AI interaction data
- **Evolution**: Spawned **pi-brain** (151 stars, Mar 2026) — privacy-first dataset extraction with local-only static privacy engine, structured review, and Hugging Face export

### TurboQuant (976 stars)
- Near-optimal KV cache quantization for LLM inference (3-bit keys, 2-bit values) with Triton kernels + vLLM integration
- Implements ICLR 2026 paper (arXiv:2504.19874) methodology
- **Key finding**: 30.9% KV cache reduction on Qwen3.5-27B-AWQ (dense, 4-bit weights) on single RTX 5090; ~2x context window on dense models with 4x RTX 3090
- Honest about limitations: "5.1x compression" claim is misleading — doesn't count Pi/S matrices or ring buffer overhead; honest figure ~4.6x at 4k tokens

### Parchi (461+ stars)
- AI-powered browser copilot as a Chrome extension
- Chat-driven browser automation: navigate, read, click, extract — all through natural language
- Supports any OpenAI-compatible endpoint, with hosted proxy option
- Includes a Relay daemon/CLI for exposing Parchi as a local automation endpoint

### vLLM Studio (366+ stars)
- Unified local AI workstation for model lifecycle management
- Supports vLLM, SGLang, llama.cpp, ExLlamaV3
- Features: orchestration, observability, remote access, OpenAI-compatible proxy
- Built because "LM Studio for vLLM/SGLang" didn't exist

### Open Orchestra (269 stars)
- Hub-and-spoke multi-agent orchestration plugin for OpenCode
- 6 built-in worker profiles: Vision, Docs, Coder, Architect, Explorer, Memory
- Neo4j-backed persistent memory system
- 5-tool async task API: start/await/peek/list/cancel tasks
- Inspired by AutoGen and LangGraph patterns

### Azul (165+ stars)
- Terminal web browser written in Rust
- Features AI chat integration, tool-calling, multi-engine search
- Part of his broader "Freedom Tech" philosophy

### factory-cursor-bridge (62 stars)
- Unified BYOK proxy that wires ~/.factory/config.json models into Cursor IDE
- Supports multiple providers, protocol translation (OpenAI ↔ Anthropic), automatic model prefixing
- Uses cloudflared tunnel to bypass Cursor's localhost SSRF protection

### Mem-Layer (78+ stars)
- Graph-based memory management system for AI models
- Scoped persistence, temporal awareness, cross-model sharing
- Built as an MCP-compatible memory layer

## Homelab & Local AI Philosophy

Sero documented his journey from spending **~$10,000/mo in value** (across Cursor Pro, Claude API, and other tools) for **~$2,012 actual cost** to achieving self-sufficiency with local models:

### Hardware Build (Total: ~$12,360)
| Component | Specification | Cost |
|-----------|---------------|------|
| **GPUs** | 8x RTX 3090 (24GB each = **192GB VRAM**) | $7,118.64 |
| **Memory** | 512GB DDR4 ECC | $2,224.61 |
| **Motherboard** | ASRock Romed8-2T | $902.63 |
| **CPU** | EPYC 7443P | $739.01 |
| **Storage** | 2TB + 4TB Samsung NVMe | $552.54 |
| **Power** | 2x 1,600W Corsair + 1x 1,000W Corsair | $723.00 |
| **Case** | Custom zip-tied rack | ~$100 |

### Performance Benchmarks
| Metric | Value | Configuration |
|--------|-------|---------------|
| **Prefill Throughput** | 3,000–9,000 TPS | 4–8x 3090 + vLLM |
| **Generation Throughput** | 30–50 TPS | 4x 3090 + vLLM optimized |
| **Context Window** | 180k–500k+ tokens | 6–8x 3090 |
| **Peak VRAM Usage** | 192GB | 8x 3090 full load |

**Cerebras REAP Benchmark (GLM-4.5-Air-Reap-82b, 8-bit)**: Prompt processing peak `1,012 T/s`, avg `920–980 T/s`; Generation `43–44 T/s` consistent across full context.

### Model Preferences & Rankings
| Tier | Model | Primary Use Case | Quantization |
|------|-------|------------------|--------------|
| **S-Tier** | GLM-4.5-Air | Daily driver, vision tasks | AWQ-4bit |
| | GLM-4.5V | Screenshot analysis, UI understanding | AWQ-4bit |
| | MiniMax-M2.1 | Agentic workflows, complex reasoning | AWQ-4bit |
| **A-Tier** | Hermes-70B | Unrestricted queries | Q5_K_M |
| | Qwen-72B | General purpose | Q5_K_M |
| | GPT-OSS-120B | STEM work | Q4_K_M |

> "MiniMax is way better at doing things until they're done, it's smarter, doesn't get stuck in loops, and tool calls almost never fail." — @seroxdesigns

### Private Home RAG
His most valuable use case: a fully private RAG system indexing financial records, legal documents, scanned contracts, photos, and messages. Stack: PostgreSQL + pgvector, BGE-M3 embeddings (dense + sparse + multi-vector). Index: HNSW for fast retrieval. Storage: 1.2TB indexed documents.

> "1 week of my local llms working 24/7 nearly fully autonomously (Needs help every 8 hours or so.) 10% of this is output. 9.6M output tokens with claude sonnet = ~$150. 85M input tokens with sonnet = ~$240." — @seroxdesigns

## Core Ideas

### Freedom Tech
> "The best tools give you control, not dependency."

Sero advocates for technology that empowers individuals rather than creating corporate lock-in. This spans from local AI inference to blockchain governance systems.

### Build in Public
200+ public repositories, most open source. He believes in transparent development and community-driven improvement. His projects consistently attract contributors and forking activity.

### Boring Reliability
> "The best infrastructure is invisible."

He focuses on the "boring plumbing" that makes AI agents work in production — orchestration layers, memory systems, data pipelines — rather than flashy frontends.

### AI Data Ownership
His AI Data Extraction toolkit was born from realizing that developers don't own their conversation data with AI coding assistants. He advocates for local-first data storage and the right to use your own interaction history for training personalized models.

### Anti-Inference Resale
> "I really think selling inference is not the right choice for any wrapper, ADE, etc.. You won't be able to keep up with the model provider's subsidies. I would pay $1,000/month for good apps to plug my models into."

He argues that wrapper/ADE businesses should focus on building polished applications rather than competing on inference pricing against subsidized model providers.

### Digital Wellness
> "YouTube shorts and short in general are a cancer... @YouTube add a feature to disable this, it's genuine garbage that destroys the mind and soul."

**Rules for Sanity:**
1. Do not use AI to write blogs, posts, or emails
2. Do not form relationships with LLMs
3. Avoid short-form content entirely
4. Touch grass & read physical books
5. Never insult or humiliate people online
6. Respect yourself

> "if there is one thing that you must not do is surrender don't surrender your dreams, your passion, your curiosity or your freedom never"

### Local AI Is Now Viable
> "We are at a point where intelligence can fit on 36GB of RAM."

His homelab experiments demonstrate that competitive AI inference is achievable on consumer hardware, making centralized AI subscriptions increasingly unnecessary for individual developers.

## AI/LLM Stance & Model Comparisons

- **Anthropic & AI Anthropomorphism**: Strongly opposes attributing emotions to AI. Views LLMs strictly as mathematical functions, though acknowledges their capability.
  > "My goat says it how it is. Anthropic is misleading you. Clankers do not have emotions, Clankers feel nothing. They are a math function, doesn't mean they're not absolutely awesome."
- **OpenAI Codex vs. GPT-5.4**: 
  > "GPT-5.3-Codex is still the best coding agent, no doubt about it. GPT-5.4 is better at computer use, but doesn't match the sheer autistic power Codex holds."
- **Pi & Caching**: Praises Pi's token caching implementation as a benchmark for all AI harnesses to reduce costs. Calls Pi the *"neovim of coding agents."*
- **Anthropic Subscription Rules**: Criticizes Anthropic for unclear, inconsistent terms regarding agent usage, CI pipelines, and distributed sandboxes.

## Blockchain & Governance Work

Before AI, Sero built significant infrastructure in the Web3 space:
- **Thrive Protocol**: AI systems that automate treasury allocations from crypto ecosystems to builders. **Proof of Value** consensus mechanism ensures capital moves only when real, measurable outcomes are proven. $150M+ committed capital, 1,800+ builders funded.
- **ZKSync event monitor**: Processing 80k–160k daily RPC calls into structured RSS feeds
- **Ethereum Foundation IVCNotes**: Zero-knowledge proofs + IVC for private digital notes
- **GitCoin Grants**: Cross-chain donation bridge evaluation
- **MakerDAO, Gnosis, Superfluid, Lens Protocol**: Various governance and DeFi contributions

## Related

- [[concepts/elizaos]] — Major contributor to the agentic framework
- [[concepts/local-ai]] — Advocate for running models on consumer hardware
- [[concepts/multi-agent]] — Open Orchestra, agent coordination
- [[concepts/developer-tools]] — Azul, Parchi, vLLM Studio, pi-brain
-  — ZKSync, Ethereum governance infrastructure, Thrive Protocol
- [[concepts/vllm]] — Local inference infrastructure
- [[concepts/model-context-protocol-mcp]] — Mem-Layer and tool integration
-  — Core philosophy- [[teknium]] — Fellow ElizaOS contributor and AI agent builder
-  — KV cache quantization research
## Key Links

- **Website**: [sybilsolutions.ai](https://www.sybilsolutions.ai/)
- **GitHub**: [github.com/0xSero](https://github.com/0xSero)
- **X/Twitter**: [@0xsero](https://x.com/0xsero)
- **Farcaster**: [@0xsero](https://warpcast.com/0xsero)
- **Blog**: [sybilsolutions.ai/blog](https://www.sybilsolutions.ai/blog/)
- **Thrive Protocol**: [thriveprotocol.com](https://blog.thriveprotocol.com/about)
