---
title: "OpenAI"
type: entity
created: 2026-04-16
updated: 2026-04-29
tags:
  - company
  - model
  - ai-agents
  - product
  - openai
  - agents-sdk
aliases: ["OpenAI Inc."]
sources:
  - raw/newsletters/2026-04-24-chatgpt-images-2-0-is-genuinely-fantastic.md
  - raw/articles/openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md
  - raw/newsletters/2026-04-28-openai-breaks-free-from-microsoft.md
  - raw/articles/simonwillison.net--2026-apr-25-romain-huet--fea00393.md
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

### Key Products & Technologies

#### Language Models
- **GPT-4/5 series** — Frontier LLMs powering ChatGPT and API integrations
- **GPT-5.5** (Apr 2026) — First fully retrained base model since GPT-4.5. Designed for multi-step work (planning, tool use, self-checking). Scored 82.7% on Terminal-Bench 2.0. Key unlock for production agent deployment.
  - **Key change:** Since GPT-5.4, OpenAI unified Codex and the main model into a single system. There is no separate coding line anymore. GPT-5.5 extends this further with strong gains in agentic coding, computer use, and any task on a computer (per Romain Huet).
  - **Prompting guidance:** OpenAI recommends treating GPT-5.5 as a **new model family to tune for**, not a drop-in replacement for GPT-5.2 or GPT-5.4. Start with the smallest prompt that preserves the product contract, then tune reasoning effort, verbosity, tool descriptions, and output format ([Simon Willison, Apr 2026](https://simonwillison.net/2026/Apr/25/gpt-5-5-prompting-guide/)).
  - **Codex migration:** OpenAI recommends running `$openai-docs migrate this project to gpt-5.5` to follow the embedded upgrade guide in their openai-docs skill.
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

### Strategic Initiatives (OpenAI Ecosystem)
- **World ID 4.0 / AgentKit** — Sam Altman's Worldcoin project reached 18M verified users across 160 countries. AgentKit enables AI agents to carry cryptographic proof they act for verified humans. Vercel has "human in the loop" authentication live; Okta planning "Human Principal" for API policies. New integrations include Tinder (verified-human badges), Zoom ("Deep Face" iris+live selfie cross-checks), and DocuSign (proof-of-human signatures).
- **SpaceX-Cursor Deal** — SpaceX has right to acquire Cursor for $60B or pay $10B for collaborative compute credits (likely Colossus H100 equivalents). Signals industry trend: top coding labs need to own both model and product.
- **Microsoft Partnership Renegotiation (Apr 2026)** — OpenAI ended exclusive distribution agreement with Microsoft, allowing multi-cloud deployment on AWS, Google Cloud, and Oracle. Microsoft retains nonexclusive IP license through 2032 with capped 20% revenue share through 2030. AGI escape clause replaced with fixed timelines. See [[entities/microsoft]] for Microsoft perspective.

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

### OpenAI-related articles
- [2026-04-06-openai-anthropic-google-distillation-alliance](2026-04-06-openai-anthropic-google-distillation-alliance.md)
- [2026-04-11-geohot-openai-nothing-without-people](2026-04-11-geohot-openai-nothing-without-people.md)
- [feed.tedium.co--link-15204-17327554-openai-anthropic-ai-tools-expensive-alte--a5938895](feed.tedium.co--link-15204-17327554-openai-anthropic-ai-tools-expensive-alte--a5938895.md)
- [garymarcus.substack.com--p-three-thoughts-on-the-musk-openai--867f8dfb](garymarcus.substack.com--p-three-thoughts-on-the-musk-openai--867f8dfb.md)
- [martinalderson.com--posts-are-openai-and-anthropic-really-losing-money-on-infere--beeb95b5](martinalderson.com--posts-are-openai-and-anthropic-really-losing-money-on-infere--beeb95b5.md)
- [open.substack.com--pub-swyx-p-ainews-openai-launches-gpt-image--6e7fb087](open.substack.com--pub-swyx-p-ainews-openai-launches-gpt-image--6e7fb087.md)
- [openai-agents-sdk-next-evolution-2026-04](openai-agents-sdk-next-evolution-2026-04.md)
- [openai-codex-orchestration-symphony](openai-codex-orchestration-symphony.md)
- [openai-equip-responses-api-computer-environment-2026-03-11](openai-equip-responses-api-computer-environment-2026-03-11.md)
- [openai-harness-engineering-lopopolo](openai-harness-engineering-lopopolo.md)
- [openai-sandbox-agents-api-guide-2026-04](openai-sandbox-agents-api-guide-2026-04.md)
- [openai-unlocking-codex-harness](openai-unlocking-codex-harness.md)
- [openai-unrolling-codex-agent-loop](openai-unrolling-codex-agent-loop.md)
- [simonwillison.net--2026-apr-28-openai-codex--558b4b74](simonwillison.net--2026-apr-28-openai-codex--558b4b74.md)
- [theatlantic.com--technology-2026-04-openai-trial-elon-musk-sam-altman-686984--5e03c7a7](theatlantic.com--technology-2026-04-openai-trial-elon-musk-sam-altman-686984--5e03c7a7.md)
- [thesignal.substack.com--openai-is-cooking-anthropic-sweep-2026-04-26](thesignal.substack.com--openai-is-cooking-anthropic-sweep-2026-04-26.md)
- [trendingtopics.eu--is-this-gpt-6-openai-bets-everything-on-new-model-spud--f17ba49f](trendingtopics.eu--is-this-gpt-6-openai-bets-everything-on-new-model-spud--f17ba49f.md)
- [wheresyoured.at--hatersguide-openai--1e5ccc17](wheresyoured.at--hatersguide-openai--1e5ccc17.md)
- [wheresyoured.at--how-openai-kills-oracle--55ef849c](wheresyoured.at--how-openai-kills-oracle--55ef849c.md)
- [wheresyoured.at--openai-cfo-news--6d149a3a](wheresyoured.at--openai-cfo-news--6d149a3a.md)
- [wheresyoured.at--openai-projects-chatgpt-plus-subscriptions-to-drop-by-80-fro--4a94de93](wheresyoured.at--openai-projects-chatgpt-plus-subscriptions-to-drop-by-80-fro--4a94de93.md)

## Sources
- **OpenAI Agents SDK Blog (2026-04-15)** — [openai.com](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)
- **OpenAI API Sandbox Docs** — [developers.openai.com](https://developers.openai.com/api/docs/guides/agents/sandboxes)
- **Simon Willison: GPT-5.5 prompting guide (2026-04-25)** — [simonwillison.net](https://simonwillison.net/2026/Apr/25/gpt-5-5-prompting-guide/)
- **Alex Banks, The Signal: "OpenAI Is Cooking, The Anthropic Sweep, and SpaceX Courts Cursor" (2026-04-26)** — [substack.com](https://open.substack.com/pub/thesignal/p/openai-is-cooking-the-anthropic-sweep)

## References

- openai-symphony-codex-orchestration
- sign-of-the-future-gpt-55
