---
title: "llm.nvim"
type: concept
created: 2026-04-25
updated: 2026-11-13
tags:
  - concept
  - developer-tooling
  - ide
  - open-source
  - huggingface
sources:
  - https://github.com/huggingface/llm.nvim
  - https://github.com/yacineMTB/dingllm.nvim
aliases:
  - llm.nvim
  - huggingface/llm.nvim
---

# llm.nvim

**llm.nvim** is the flagship Neovim plugin for LLM-assisted development from Hugging Face's `hf` CLI team (created by Yacine Mahdid, then [[entities/hugging-face|Hugging Face]], ~1.2k stars). It embeds LLM chat, inline completions, and prompt templates directly inside the Neovim editor — one of the earliest "editor-native" alternatives to Copilot-style cloud assistants, notable for being **provider-agnostic**: it works equally against local `llama.cpp` servers, Hugging Face Inference Endpoints, or any OpenAI-compatible API.

## Features

- **Chat panel** (`:LLMStartChat`) — streaming chat in a split, with the current buffer/selection as context.
- **Inline completion** — GitHub-Copilot-style ghost-text completion via a completion-capable backend.
- **Prompt templates** — reusable prompts (explain, refactor, test generation) defined in `config.lua`, invoked as keymaps.
- **Multi-provider config** — a single `providers` table maps endpoint names to URLs/models; switch model mid-session with `:LLMChangeModel`.
- **Local-first** — the canonical quickstart targets a local `llama-server` / `text-generation-inference`, making it a common vehicle for offline coding models.

## Configuration sketch

```lua
require("llm").setup{
  global = { request = { timeout = 10000 } },
  providers = {
    ollama = { { name = "llama3", url = "http://localhost:11434/api/generate" } },
    hf     = { { name = "mistral", url = "https://<endpoint>.endpoints.huggingface.co" } },
  },
}
```

## The llm.nvim family

The name is shared by several independent Neovim LLM plugins — a recurring disambiguation trap:

| Plugin | Author | Notes |
|---|---|---|
| **huggingface/llm.nvim** | Yacine Mahdid / HF (~1.2k★) | This page — chat + completions + templates |
| [[concepts/dingllm.nvim]] | Yacine Mahdid (~850★) | Personal predecessor/sister project with extra workflows |
| Kurama622/llm.nvim | Kurama622 (~480★) | Command-based multi-provider chat, supports DeepSeek/GLM etc. |
| melbaldove/llm.nvim | melbaldove (~250★, archived 2024) | "No frills" completion-focused |

## Context

llm.nvim sits in the broader "LLM in the editor" wave alongside Copilot, Cursor, and `aider`, but is distinctive as an **open-source, scriptable, local-model-friendly** option — a natural companion to running open coding models (Qwen-Coder, DeepSeek-Coder) on personal hardware. See [[concepts/how-coding-agents-work]] for the surrounding landscape.

## Related

- [[entities/yacine-mahdid]] — author
- [[concepts/dingllm.nvim]] — sibling plugin by the same author
- [[entities/hugging-face]] — hosting organization
- [[concepts/open-source-llms]] — models commonly run behind it
- [[concepts/how-coding-agents-work]] — editor/agent integration landscape
