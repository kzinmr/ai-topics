---
title: LM Studio
type: entity
created: 2026-06-18
updated: 2026-08-01
status: L3
sources:
  - raw/articles/vickiboykis.com--running-local-models-is-good-now--2026-06-15.md
  - https://lmstudio.ai/
  - https://lmstudio.ai/changelog
  - https://lmstudio.ai/docs/bionic
  - https://lmstudio.ai/blog
tags: [product, tool, local-llm, inference, macos, apple-silicon, ai-agents, cli]
aliases: [Element Labs, lmstudio.ai, lms]
---

# LM Studio

Desktop application for running local LLMs with an OpenAI-compatible API server, made by **Element Labs, Inc.** Provides a GUI for downloading, configuring, and running GGUF models, plus local inference endpoints compatible with OpenAI's completions, Responses, and Anthropic Messages APIs. Since July 2026 it also ships **Bionic**, a separate agent app for open models.

## Overview

LM Studio simplifies local model inference by bundling model management, quantization selection, and API serving into a single desktop app. It is the most widely used local-first inference tool in the agentic coding community, serving as the inference backend for practitioners like [[entities/vicki-boykis]]. The company behind it is **Element Labs, Inc.** (San Francisco), which also publishes the `lms` CLI, `lmstudio-js`, and `lmstudio-python` SDKs.

As of mid-2026 the product line has split into two apps:

- **LM Studio (classic)** — the desktop model runner and local server (0.4.x series)
- **LM Studio Bionic** — a separate agent application for open models (Work Projects + Code Projects), launched July 16, 2026

## Key Features

- **Model discovery**: Browse and download GGUF models from Hugging Face directly within the app
- **OpenAI-compatible API**: Serves models at `http://localhost:1234/v1`, compatible with any OpenAI SDK/client
- **Anthropic-compatible API**: `/v1/messages` support enables running Claude Code against local models (announced Jan 30, 2026)
- **OpenAI Responses API**: `/v1/responses` endpoint with stateful chats, remote MCP, and custom tools (Oct 2025)
- **Model configuration**: Adjust context window, quantization, system prompts, chat templates, and GPU allocation
- **Session introspection**: View live token inference, token in/out counts, KV cache usage
- **Multiple model support**: Load and switch between models; tensor parallelism for multi-GPU (CUDA, 0.4.15)
- **MTP Speculative Decoding**: Stable in 0.4.14+ for models with built-in multi-token prediction heads
- **Chat to PDF export** with styled markdown and Mermaid diagram rendering (0.4.17)
- **LM Studio Engine Protocol**: New engine architecture (beta 0.4.15, default-on 0.4.19) enabling more frequent llama.cpp engine updates and load-time speculative decoding

## LM Studio Bionic (July 2026)

**Bionic** is LM Studio's AI agent for open models — "an Agent made for Open Models. Natively local." Launched July 16, 2026 in initial preview for macOS and Windows.

- **Two project types**: Work Projects (research, writing, analysis, document work) and Code Projects (local codebase with file, search, Git, and shell tools)
- **Sessions**: Create separate sessions per task; run multiple sessions across projects in parallel
- **Model sources**: Frontier open models in LM Studio Secure Cloud (Zero Data Retention), local models on-device, or remote models via LM Link
- **Voice input**: Real-time on-device voice transcription in multiple languages, processed locally
- **Agentic capabilities**: document creation/editing with auto-save, coding, automations, and computer control
- **Supported frontier models**: GLM 5.2, Kimi K3 (added Jul 27, 2026), DeepSeek V4 Pro, Kimi Code K2.7
- **Pricing**: Free tier (local LLMs + voice transcription, web search with ZDR, LM Link for up to 5 devices); pay-as-you-go cloud credits for hosted inference

### Bionic Cloud Pricing (per 1M tokens, ZDR)

| Model | Input | Cached | Output |
|-------|-------|--------|--------|
| Kimi K3 | $3.00 | $0.30 | $15.00 |
| GLM 5.2 | $1.50 | $0.30 | $4.50 |
| Kimi Code K2.7 | $0.95 | $0.16 | $4.00 |
| DeepSeek V4 Pro | $1.74 | $0.15 | $3.48 |
| Kimi K2.6 | $0.95 | $0.16 | $4.00 |

## LM Link & Locally (Mobile)

- **LM Link** — share models between devices; no longer waitlisted (0.4.16, June 2026)
- **Locally** — LM Studio's mobile app for iPhone/iPad (launched June 8, 2026, 0.4.16); run your largest local models on the go via LM Link
- **Locally AI acquisition**: In April 2026, the Locally AI apps (by Adrien) joined the LM Studio family to double down on Apple platforms

## Usage in Agentic Coding

LM Studio is commonly paired with agent harnesses like [[entities/pi]] (pi-coding-agent), [[entities/claude-code]] (via its Anthropic-compatible API), or Codex (`codex --oss`) to run agentic coding workflows entirely locally. Configuration typically involves:

1. Download a model (e.g., `gemma-4-26b-a4b`, `gemma-4-12b-qat`, `kimi-k3`)
2. Start the local server on port 1234
3. Point the agent harness at `http://localhost:1234/v1` (or `host.docker.internal:1234/v1` for Docker setups)

The 0.4.15 release specifically fixed prompt-cache drops when using Claude Code and fixed tool errors while using `codex --oss` — a signal of how central agent-harness integration has become to the product.

## Supported Hardware

- **Apple Silicon**: MLX engine (mlx-engine v1.8.1+ significantly improved performance; v1.8.5 adds KV-cache checkpointing for repeated long-context agentic workflows); M5 support via MLX fixes (0.3.38)
- **NVIDIA**: CUDA with Flash Attention default, tensor parallelism; supports DGX Spark (Linux ARM, Oct 2025) and DGX Station GB300 Blackwell (Mar 2026)
- **AMD**: ROCm and Vulkan backends; Strix Halo and Radeon AI PRO R9600D/R9700 support via llama.cpp 2.22.1 (0.4.17)
- **Linux**: ARM builds for DGX Spark

## Version History Highlights (0.4.x era)

| Version | Date | Key Changes |
|---------|------|-------------|
| 0.4.20 | Jul 22, 2026 | Enterprise internal network model endpoints; Bionic over LM Link |
| 0.4.19 | Jul 7, 2026 | Engine Protocol default ON; `/reasoning` in `lms chat` |
| 0.4.17 | Jun 26, 2026 | AMD Strix Halo; Mermaid rendering; speculative decoding defaults |
| 0.4.16 | Jun 8, 2026 | **Locally mobile app**; LM Link no longer waitlisted; 8k default context |
| 0.4.15 | May 29, 2026 | Engine Protocol beta 2; Claude Code + Codex fixes; tensor parallelism |
| 0.4.14 | May 22, 2026 | **MTP Speculative Decoding stable** |
| 0.4.12 | May 13, 2026 | Qwen 3.6 support; MCP OAuth fix |
| 0.4.0 | Jan 28, 2026 | Server deployment, continuous batching, new REST API, refreshed UI |

## Trade-offs

- Convenient GUI but adds overhead vs raw [[concepts/llama-cpp]]
- Context window limited by hardware (typically 32K-128K on consumer hardware)
- KV cache can consume significant RAM (up to 64 GB for large models on Apple Silicon)

## Alternatives

- [[concepts/ollama]] — CLI-first local inference, lighter weight
- [[concepts/llama-cpp]] — Raw C++ inference, minimal overhead
- llamafiles — Single-file portable model executables
- vLLM — High-throughput server-side inference

## See Also

- [[entities/vicki-boykis]] — Blog post documenting LM Studio in local agentic workflow
- [[concepts/local-llm]] — Concept hub on local model inference approaches
- [[entities/gemma-4]] — Google model family frequently used with LM Studio
- [[entities/claude-code]] — Agent harness with official LM Studio integration
- [[entities/nvidia-dgx-spark]] — Linux ARM hardware supported by LM Studio

## Log

- **2026-08-01**: Enriched L2→L3 with Bionic agent, cloud pricing, LM Link/Locally, Engine Protocol, MTP speculative decoding, hardware support, version history (from lmstudio.ai homepage, changelog, docs, blog).
- **2026-06-18**: Initial entity page creation (L2 depth).
