---
title: "OpenAI"
type: entity
created: 2026-04-16
updated: 2026-04-25
tags: [company, llm, ai-agents, product, openai, gpt, agents-sdk]
aliases: ["OpenAI Inc."]
sources: [raw/newsletters/2026-04-24-chatgpt-images-2-0-is-genuinely-fantastic.md]
---

# OpenAI

| | |
|---|---|
| **Type** | AI Research & Product Company |
| **Founded** | 2015 |
| **Leadership** | Sam Altman (CEO), Greg Brockman (President/CTO), Ilya Sutskever (Chief Scientist, former) |
| **Key Products** | GPT-4/5 series, ChatGPT, Codex, DALL-E, Whisper, o-series, Agents SDK, Symphony |
| **Website** | [openai.com](https://openai.com) |
| **API** | [platform.openai.com](https://platform.openai.com) |

## Overview

OpenAI is a leading AI research and product company known for developing the GPT series of large language models, ChatGPT, and a growing ecosystem of AI developer tools. The company has been at the forefront of the AI agent revolution, releasing the **Agents SDK** (v0.14.0, April 2026) which provides standardized infrastructure for building production-ready agents with sandbox execution capabilities.

## Key Products & Technologies

### Language Models
- **GPT-4/5 series** — Frontier LLMs powering ChatGPT and API integrations
- **o-series** — Reasoning-focused models with extended thinking
- **GPT-4o / GPT-4o-mini** — Multimodal models with vision and audio capabilities

### Developer Tools
- **Agents SDK** (v0.14.0, April 2026) — Python SDK for building agents with:
  - Native sandbox execution (isolated workspaces)
  - Harness/Compute architectural separation
  - Manifest-based workspace portability
  - Standardized integrations: MCP, Skills, AGENTS.md, Shell, Apply Patch
  - Provider ecosystem: Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, Vercel
  - Security: Default-deny, relative paths only, `..` traversal blocked
  - Durability: Snapshotting & rehydration for long-horizon tasks
- **Symphony** — Agent orchestration framework (see [[harness-engineering]])
- **Codex** — AI coding agent

### Other Products
- **ChatGPT** — Conversational AI interface
- **GPT Image 2 (ChatGPT Images 2.0)** — Second-generation image generation integrated into ChatGPT. Superior prompt adherence, professional output quality, significantly lower hallucinations vs. competitors. Features Select lasso tool and aspect ratio control for post-generation iteration. 40–60s generation time (~2x slower than Google's NB2 but widely preferred for quality).
- **DALL-E** — Text-to-image generation
- **Whisper** — Speech recognition
- **Sora** — Video generation

## Security Architecture

OpenAI's Agents SDK introduces a clear **Harness/Compute separation**:
- **Harness (Control Plane):** Agent loop, model calls, tool routing, handoffs, approvals, tracing, recovery, auth, billing
- **Compute (Execution Plane):** File I/O, commands, dependency installs, port exposure, provider-specific state

This separation mitigates prompt-injection/exfiltration risks and isolates credentials from model-generated code.

## Customer Validation

> *"The updated Agents SDK made it production-viable for us to automate a critical clinical records workflow that previous approaches couldn't handle reliably enough. For us, the difference was not just extracting the right metadata, but correctly understanding the boundaries of each encounter in long, complex records."*
> — **Rachael Burns**, Staff Engineer & AI Tech Lead, Oscar Health

## Related Concepts
- [[openai-agents-sdk]] — OpenAI's agent development framework
- [[harness-engineering]] — Ryan Lopopolo / Symphony orchestration philosophy
- [[sandbox]] — AI agent sandbox isolation technologies
- [[chatgpt-images-2.0]] — GPT Image 2 image generation
- [[nano-banana-2]] — Google's NB2 image generation competitor

## Sources
- 
- 
- [OpenAI Agents SDK Blog (2026-04-15)](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)
- [OpenAI API Sandbox Docs](https://developers.openai.com/api/docs/guides/agents/sandboxes)
