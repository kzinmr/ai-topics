---
title: "OpenAI Codex Superapp"
type: concept
created: 2026-04-24
updated: 2026-04-24
tags: [product, openai, coding-agents, devtools, chatgpt]
aliases: ["Codex Superapp"]
sources: []
---

# OpenAI Codex Superapp

The OpenAI Codex interface becoming the primary ChatGPT experience — a "superapp" positioning for the AI coding agent.

## Overview

As of April 24, 2026, the OpenAI Codex interface has become the **main interface** for ChatGPT, superseding the traditional conversational interface. This marks a strategic shift from ChatGPT as a general-purpose chat interface to a superapp for AI-powered coding and agent work.

## Key Developments

### Codex as Primary Interface

- Codex is now the default/main experience in ChatGPT
- Traditional ChatGPT chat is now a secondary option
- This represents a pivot toward developer-first positioning

### GPT-5.5 Availability

GPT-5.5 is available in OpenAI Codex and rolling out to paid ChatGPT subscribers (April 2026). Key details:

| Model | Input ($/1M) | Output ($/1M) | Notes |
|-------|-------------|---------------|-------|
| GPT-5.5 | $5 | $30 | Main model |
| GPT-5.5 Pro | $30 | $180 | Higher tier |
| GPT-5.4 | $2.5 | $15 | Remains at half price |

### Codex Backdoor API

OpenAI officially supports third-party integration with ChatGPT subscriptions via the open-source Codex CLI mechanism:

> "We want people to be able to use Codex, and their ChatGPT subscription, wherever they like! That means in the app, in the terminal, but also in JetBrains, Xcode, OpenCode, Pi, and now Claude Code." — Romain Huet, OpenAI (March 2026)

This has enabled tools like:
- **OpenClaw** — Third-party agent harness (OpenAI welcomed it after Anthropic blocked similar integration)
- **llm-openai-via-codex** — Simon Willison's plugin for CLI access to Codex subscriptions
- **Claude Code** — Now listed as a supported integration

### The "Codex Backdoor" Implications

The Codex CLI's open-source nature allows:
1. Any developer to reverse-engineer subscription authentication
2. Third-party tools to route prompts through existing ChatGPT subscriptions
3. Bypass of the delayed public API for GPT-5.5
4. Creates a "backdoor" to access frontier models at subscription prices

See [[gpt-models]] for GPT model details, [[openai]] for company context, [[openai-agents-sdk]] for the official SDK approach.

## Related Concepts

- [[gpt-models]] — GPT-5.5 and the GPT model series
- [[openai]] — OpenAI company and products
- [[openai-agents-sdk]] — Official Agents SDK (alternative to subscription hooking)
- [[harness-engineering]] — Harness engineering philosophy
- [[anthropic]] — Anthropic (competitor who blocked OpenClaw)

## Sources

-  (AINews, 2026-04-24)
-  (Simon Willison Newsletter, 2026-04-24)
- [Simon Willison: GPT-5.5 via Codex backdoor API](https://simonwillison.net/2026/Apr/23/gpt-5-5/)
- [OpenAI Index: Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)
