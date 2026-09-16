---
title: "llama.cpp"
type: concept
created: 2026-04-25
updated: 2026-09-16
tags:
  - local-llm
  - open-source
redirect: concepts/local-llm/llama-cpp
---

# llama.cpp

> **This page redirects to [[concepts/local-llm/_index|Local LLM hub]]** (subdirectory hub member). The top-level stub and the subdirectory stub both point here; the substantive llama.cpp coverage is in the [[concepts/local-llm/_index|Local LLM hub]].

**llama.cpp** is Georgi Gerganov's open-source C/C++ inference engine for running LLaMA-family (and now nearly all open-weight) models on CPUs, Apple Silicon, and consumer GPUs. It originated the GGML/GGUF formats and the k-quants quantization scheme, and underpins Ollama, LM Studio, and most local-LLM tooling.

## Where the Substance Lives

- [[concepts/local-llm/gguf]] — GGUF format and quantization types (llama.cpp's file format)
- [[concepts/local-llm/model-quantization]] — Quantization methods used by llama.cpp
- [[concepts/local-llm/ollama]] — The runner built atop llama.cpp
- [[concepts/cpu-inference-llm]] — CPU inference techniques popularized by llama.cpp

## Related Pages

- [[concepts/local-llm/_index|Local LLM hub]]
- [[concepts/inference]]
