---
title: "Sero (0xSero)"
handle: "@0xsero"
url: "https://www.sybilsolutions.ai/"
twitter: "https://x.com/0xsero"
status: active
tags:
  - ai-infrastructure
  - open-source
  - local-ai
  - multi-agent
  - developer-tools
  - elizaOS
  - blockchain
---

# Sero (@0xsero)

## Overview

Sero (known online as **0xSero**) is an open-source developer, AI infrastructure builder, and founder of **Sybil Solutions**. He operates at the intersection of AI agents, blockchain infrastructure, and developer tooling. He is a major contributor to **ElizaOS** (17k+ GitHub stars) and has built numerous open-source tools focused on local AI, privacy-first data extraction, and multi-agent orchestration.

He runs an **8x RTX 3090 homelab** for local model inference and is a vocal advocate for "Freedom Tech" — systems that give individuals control over their data and AI workflows rather than creating corporate dependency.

## Background

- **Founder**, Sybil Solutions — AI infrastructure and developer tools
- **Current**: Building **Thrive Protocol** — AI systems that automate treasury allocations from crypto ecosystems to builders ($150M+ committed capital, 1,800+ funded builders)
- **Previous**: Ethereum Foundation, ZKSync governance infrastructure, MakerDAO, Gnosis, Superfluid, Lens Protocol
- **Contributor**, ElizaOS — agentic framework (17k+ stars)
- **Podcast Host**, Ethers Club — 57 episodes with builders on technology, business, and spirituality
- **Location**: United States

His trajectory: Content protection (DMCA takedowns, creator rights) → Web3/DAOs (governance infra) → AI Infrastructure (agents, local models, developer tools). He describes becoming a father as a turning point that shifted his focus toward building systems that give individuals more control.

## Key Open-Source Projects

### AI Data Extraction Toolkit (578+ stars)
- Python toolkit to extract complete conversation history, code context, and metadata from AI coding assistants (Claude Code, Cursor, Codex, Windsurf, Trae)
- Outputs structured JSONL files ready for ML training
- Built to solve the problem of developers not having access to their own AI interaction data

### Parchi (461+ stars)
- AI-powered browser copilot as a Chrome extension
- Chat-driven browser automation: navigate, read, click, extract — all through natural language
- Supports any OpenAI-compatible endpoint, with hosted proxy option
- Includes a Relay daemon/CLI for exposing Parchi as a local automation endpoint

### vLLM Studio (374+ stars)
- Unified local AI workstation for model lifecycle management
- Supports vLLM, SGLang, llama.cpp, ExLlamaV3
- Features: orchestration, observability, remote access, OpenAI-compatible proxy
- Built because existing tools (LM Studio for vLLM/SGLang) didn't exist

### Azul (165+ stars)
- Terminal web browser written in Rust
- Features AI chat integration, tool-calling, multi-engine search
- Part of his broader "Freedom Tech" philosophy

### Open Orchestra
- Hub-and-spoke multi-agent orchestration system with Neo4j-backed memory
- 22+ tool APIs integration
- Designed for complex agentic workflows requiring persistent memory

### Mem-Layer (78+ stars)
- Graph-based memory management system for AI models
- Scoped persistence, temporal awareness, cross-model sharing
- Built as an MCP-compatible memory layer

## Homelab & Local AI Philosophy

Sero runs an **8x RTX 3090** homelab and has documented his journey from spending $2,000+/month on AI subscriptions to achieving self-sufficiency with local models:

| Factor | Corporate AI | Homelab |
|--------|-------------|---------|
| Cost/month | $2,000+ | ~$50 (electricity) |
| Rate limits | Constant concern | None |
| Data privacy | Sent to servers | Never leaves home |
| Customization | Restricted | Full control |

His preferred models: **MiniMax-M2** and **GLM** (Chinese open models). He serves MiniMax-M2 at 100+ tokens/second via vLLM and has built a **MiniMax-M2 Proxy** to make it compatible with standard OpenAI APIs.

### Private Home RAG
His most valuable use case: a fully private RAG system indexing financial records, legal documents, scanned contracts, photos, and messages. Stack: PostgreSQL + pgvector, BGE-M3 embeddings (dense + sparse + multi-vector).

## Core Ideas

### Freedom Tech
> "The best tools give you control, not dependency."

Sero advocates for technology that empowers individuals rather than creating corporate lock-in. This spans from local AI inference to blockchain governance systems.

### Build in Public
175+ public repositories, most open source. He believes in transparent development and community-driven improvement. His projects consistently attract contributors and forking activity.

### Boring Reliability
> "The best infrastructure is invisible."

He focuses on the "boring plumbing" that makes AI agents work in production — orchestration layers, memory systems, data pipelines — rather than flashy frontends.

### AI Data Ownership
His AI Data Extraction toolkit was born from realizing that developers don't own their conversation data with AI coding assistants. He advocates for local-first data storage and the right to use your own interaction history for training personalized models.

### Local AI Is Now Viable
> "We are at a point where intelligence can fit on 36GB of RAM."

His homelab experiments demonstrate that competitive AI inference is achievable on consumer hardware, making centralized AI subscriptions increasingly unnecessary for individual developers.

## Blockchain & Governance Work

Before AI, Sero built significant infrastructure in the Web3 space:
- **ZKSync governance event monitor**: Processing 80k–160k daily RPC calls into structured RSS feeds
- **Ethereum Foundation IVCNotes**: Zero-knowledge proofs + IVC for private digital notes
- **GitCoin Grants**: Cross-chain donation bridge evaluation
- **MakerDAO, Gnosis, Superfluid, Lens Protocol**: Various governance and DeFi contributions

## Related

- [[elizaOS]] — Major contributor to the agentic framework
- [[local-ai]] — Advocate for running models on consumer hardware
- [[multi-agent]] — Open Orchestra, agent coordination
- [[developer-tools]] — Azul, Parchi, vLLM Studio
- [[blockchain]] — ZKSync, Ethereum governance infrastructure
- [[vllm]] — Local inference infrastructure
- [[mcp]] — Mem-Layer and tool integration
- [[freedom-tech]] — Core philosophy
- [[teknium]] — Fellow ElizaOS contributor and AI agent builder

## Key Links

- **Website**: [sybilsolutions.ai](https://www.sybilsolutions.ai/)
- **GitHub**: [github.com/0xSero](https://github.com/0xSero)
- **X/Twitter**: [@0xsero](https://x.com/0xsero)
- **Farcaster**: [@0xsero](https://warpcast.com/0xsero)
- **Blog**: [sybilsolutions.ai/blog](https://www.sybilsolutions.ai/blog/)
