---
title: "OpenAI"
type: entity
created: 2026-04-16
updated: 2026-04-27
tags: [company, llm, ai-agents, product, openai, gpt, agents-sdk]
aliases: ["OpenAI Inc."]
sources:
  - raw/newsletters/2026-04-24-chatgpt-images-2-0-is-genuinely-fantastic.md
  - raw/articles/openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md
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
- **GPT-5.5** (Apr 2026) — First fully retrained base model since GPT-4.5. Designed for multi-step work (planning, tool use, self-checking). Scored 82.7% on Terminal-Bench 2.0. Key unlock for production agent deployment.
  - **Codex unification**: Since GPT-5.4, OpenAI unified Codex and the main model into a single system — no separate coding model line. GPT-5.5 takes this further with strong gains in agentic coding, computer use, and any task on a computer. OpenAI confirmed it will not release a GPT-5.5-Codex model ([Romain Huet, Apr 2026](https://simonwillison.net/2026/Apr/25/romain-huet/)).
- **o-series** — Reasoning-focused models with extended thinking
- **GPT-4o / GPT-4o-mini** — Multimodal models with vision and audio capabilities

### Developer Tools
- **Workspace Agents** (Apr 2026) — Codex-powered shared agents for Business/Enterprise plans. Integrates Slack, Salesforce, Notion, Google Drive with persistent memory and role-based governance. Designed for organizational workflows, not individual use.
- **Agents SDK** (v0.14.0, April 2026) — Python SDK for building agents with:
  - Native sandbox execution (isolated workspaces)
  - Harness/Compute architectural separation
  - Manifest-based workspace portability
  - Standardized integrations: MCP, Skills, AGENTS.md, Shell, Apply Patch
  - Provider ecosystem: Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, Vercel
  - Security: Default-deny, relative paths only, `..` traversal blocked
  - Durability: Snapshotting & rehydration for long-horizon tasks
- **Symphony** — Agent orchestration framework (see [[concepts/harness-engineering]])
- **Codex** — AI coding agent. Since GPT-5.4, Codex has been unified into the main model — there is no separate coding model line. No GPT-5.5-Codex will be released ([Romain Huet, Apr 2026](https://simonwillison.net/2026/Apr/25/romain-huet/)).

### Other Products
- **ChatGPT** — Conversational AI interface
- **GPT Image 2 (ChatGPT Images 2.0)** — Second-generation image generation integrated into ChatGPT. Includes **Thinking mode** with web search mid-generation. 2K resolution with legible non-Latin scripts. Hit #1 on all Image Arena leaderboards; beat Google's Nano Banana models by +242 points (largest gap ever) in Text-to-Image. See [[concepts/chatgpt-images-2.0]] for full details.
- **ChatGPT for Clinicians** (Apr 2026) — Free tool for verified US physicians, NPs, PAs, pharmacists. Includes cited medical sources and HIPAA-compliant options.
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
- [[concepts/openai-agents-sdk]] — OpenAI's agent development framework
- [[concepts/openai-workspace-agents]] — Codex-powered enterprise shared agents
- [[concepts/gpt-5.5]] — First fully retrained base model since GPT-4.5
- [[concepts/harness-engineering]] — Ryan Lopopolo / Symphony orchestration philosophy
- [[concepts/sandbox]] — AI agent sandbox isolation technologies
- [[concepts/chatgpt-images-2.0]] — GPT Image 2 image generation
- [[concepts/nano-banana-2]] — Google's NB2 image generation competitor

## Sources
- [Simon Willison: A quote from Romain Huet (2026-04-25)](https://simonwillison.net/2026/Apr/25/romain-huet/) — Codex unified into main model since GPT-5.4, no GPT-5.5-Codex
- [OpenAI Agents SDK Blog (2026-04-15)](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)
- [OpenAI API Sandbox Docs](https://developers.openai.com/api/docs/guides/agents/sandboxes)
