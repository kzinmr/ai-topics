---
title: "llama.cpp"
type: concept
created: 2026-04-25
updated: 2026-11-27
tags:
  - local-llm
  - open-source
sources: []
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

## 2026-11-27: hardware-specific vibe-coded forks (AMD RDNA)

devnull.land (26 Nov, HN 379 pts) recommends **llama-cpp-rdna-boosts** for AMD GPUs: leaner than upstream llama.cpp, taking the author's token generation from 35 to 55 tok/s and prefill from 700 to 1300 tok/s (YMMV).

The general pattern he describes - "an explosion in the number of bespoke inference engines" (Strata, Basalt, RustingStrata, etc.) - is not about llama.cpp/SGLang/vLLM being bad, but about them being **generalist** engines optimized for no particular hardware. The new forks share four traits: they target a specific model/hardware subset, they are **vibe-coded end-to-end with a frontier model**, they chase raw token-generation speed, and LLM-assisted development lets small authors move faster than the generalist engines' release cadence. Same economic logic as the AI-assisted personal-infrastructure wave (`concepts/ai-assisted-self-hosting-renaissance`) and as `concepts/cli-over-mcp-pattern`-style "small focused tool beats general platform" arguments - with the usual caveat that a single-user benchmark on one card is not evidence of general superiority. Raw: `raw/articles/2026-11-26_devnull-land_amd-specific-llama-cpp-fork.md`.

## Related Pages

- [[concepts/local-llm/_index|Local LLM hub]]
- [[concepts/inference]]
