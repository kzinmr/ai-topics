---
title: "GGUF Quantization"
type: concept
created: 2026-04-25
updated: 2026-09-16
tags:
  - local-llm
  - quantization
redirect: concepts/local-llm/gguf
---

# GGUF Quantization

> **This page redirects to [[concepts/local-llm/gguf]]** — the canonical page on the GGUF format and its quantization types — and [[concepts/local-llm/model-quantization]] for quantization theory and method comparison.

**GGUF quantization** refers to the k-quants / i-quants schemes (Q4_K_M, Q5_K_M, Q8_0, IQ2_XXS, ...) used by the llama.cpp ecosystem to shrink LLM weights to 2–8 bits per parameter, enabling large-model inference on consumer CPUs and Apple Silicon.

## Where the Substance Lives

- [[concepts/local-llm/gguf]] — Canonical GGUF page: format, quantization type table, metadata
- [[concepts/local-llm/model-quantization]] — Quantization methods in depth (GPTQ, AWQ, GGUF k-quants)
- [[concepts/model-quantization]] — Umbrella quantization concept page (HQQ, bitsandbytes, serving-side)
- [[concepts/local-llm/llama-cpp]] — The engine that implements GGUF quantization

## Related Pages

- [[concepts/local-llm/_index|Local LLM hub]]
- [[concepts/ollama]] → [[concepts/local-llm/ollama]]
