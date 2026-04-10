---
title: "Georgi Gerganov"
created: 2026-04-10
updated: 2026-04-10
tags: [person, local-llm, inference, open-source]
aliases: ["ggerganov", "georgi"]
---

# Georgi Gerganov (@ggerganov)

Creator of llama.cpp, whisper.cpp, and the GGML/GGUF ecosystem that enabled local LLM inference on consumer hardware.

## Summary

Georgi Gerganov is a Bulgarian software engineer who created the foundational open-source tools that made local LLM inference practical on consumer hardware. His work on **llama.cpp** and the **GGML** library enabled running large language models on CPUs and Apple Silicon without requiring expensive GPUs.

## Key Projects

### llama.cpp (2023-present)
- Pure C/C++ implementation of LLaMA inference
- Supports GGUF quantization format (4-bit, 5-bit, 8-bit)
- Runs on CPU, Apple Silicon, and consumer GPUs
- Over 60K+ GitHub stars
- **2025:** Joined Hugging Face to integrate llama.cpp into the broader open-source AI stack
- Website: github.com/ggerganov/llama.cpp

### GGML / GGUF
- Tensor library optimized for consumer hardware
- GGUF format: quantized model serialization enabling CPU inference
- Replaced older GGJT format with unified, extensible structure

### whisper.cpp
- C/C++ port of OpenAI's Whisper speech recognition
- Enables local speech-to-text without cloud APIs
- Part of the same local-first AI philosophy

### Other Projects
- **llama-bench** — Benchmarking tool for comparing model/hardware performance
- **stable-diffusion.cpp** — Local image generation
- **rwkv.cpp** — RWKV model inference

## Impact on Local LLM Ecosystem

Gerganov's work is the **foundation** of the local LLM movement:
1. **Democratized Inference** — Made it possible to run 7B-70B models on laptops
2. **Ollama Built on llama.cpp** — The popular local LLM runner uses llama.cpp as its inference backend
3. **LM Studio Integration** — Desktop GUI for local models relies on GGUF format
4. **Quantization Standard** — GGUF became the de facto format for community model sharing

## Community Presence

- **GitHub:** github.com/ggerganov (highly active, regular commits)
- **X/Twitter:** @ggerganov (occasional updates on projects)
- **r/LocalLLaMA:** Frequently discussed, benchmark results shared
- **Hugging Face:** Models and datasets under ggml-org

## Related wikilinks

- [[concepts/local-llm]] — Local LLM inference ecosystem
- [[entities/llama-cpp]] — His flagship project
- [[entities/gguf]] — Quantization format he created
- [[concepts/harness-engineering]] — Local LLMs used in agent workflows
- [[entities/nous-research]] — Hermes models quantized to GGUF
- [[entities/qwen3-6-plus]] — Qwen models heavily used with llama.cpp
- [[entities/mistral-voxtral-tts]] — Mistral models popular in local inference
- [[entities/openai-spud]] — OpenAI's hardware strategy

## Sources

- llama.cpp GitHub repository: github.com/ggml-org/llama.cpp
- Hugging Face announcement (2025)
- r/LocalLLaMA community discussions
- Various benchmark threads and model comparisons
