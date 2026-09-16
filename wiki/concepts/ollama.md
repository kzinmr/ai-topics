---
title: "Ollama"
type: concept
created: 2026-04-25
updated: 2026-09-16
tags:
  - local-llm
  - developer-tooling
  - open-source
redirect: concepts/local-llm/ollama
---

# Ollama

> **This page redirects to [[concepts/local-llm/ollama]]** — the canonical, comprehensive page on Ollama as a local LLM runner.

**Ollama** is an open-source tool that packages local LLM inference into a Docker-like experience: `ollama pull llama3` / `ollama run llama3`. Built on top of llama.cpp (and later its own engine), it manages GGUF model files, provides a local REST API, and powers many downstream tools (Open WebUI, coding-agent local backends, LM Studio competitors).

## Where the Substance Lives

- [[concepts/local-llm/ollama]] — Canonical page: architecture, Modelfile system, ecosystem, GPU support
- [[concepts/llama-cpp]] — The inference engine underneath Ollama (redirects to [[concepts/local-llm/llama-cpp]])
- [[concepts/gguf]] — The model file format Ollama distributes
- [[entities/lm-studio]] — The main GUI-based alternative for local models

## Related Pages

- [[concepts/local-llm/_index|Local LLM hub]]
- [[concepts/model-quantization]]
