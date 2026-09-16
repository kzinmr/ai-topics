---
title: "GGUF"
type: concept
created: 2026-04-25
updated: 2026-09-16
tags:
  - local-llm
  - quantization
redirect: concepts/local-llm/gguf
---

# GGUF

> **This page redirects to [[concepts/local-llm/gguf]]** — the canonical page on the GGUF file format.

**GGUF** (GPT-Generated Unified Format) is llama.cpp's model file format — successor to GGML — storing weights (with built-in quantization types like Q4_K_M, Q8_0), tokenizer metadata, and architecture info in a single file. It is the distribution format for Ollama, LM Studio, and most local-LLM tooling.

## Where the Substance Lives

- [[concepts/local-llm/gguf]] — Canonical GGUF page: format layout, quantization type table
- [[concepts/llama-cpp]] → [[concepts/local-llm/llama-cpp]] — The engine that reads GGUF
- [[concepts/local-llm/ollama]] — Runner that distributes GGUF models
