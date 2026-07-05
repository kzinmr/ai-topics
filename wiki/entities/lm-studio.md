---
title: LM Studio
type: entity
created: 2026-06-18
updated: 2026-06-18
status: L2
sources: [raw/articles/vickiboykis.com--running-local-models-is-good-now--2026-06-15.md, https://lmstudio.ai/]
tags: [product, tool, local-llm, inference]
---

# LM Studio

Desktop application for running local LLMs with an OpenAI-compatible API server. Provides a GUI for downloading, configuring, and running GGUF models, plus a local inference endpoint compatible with OpenAI's completions API.

## Overview

LM Studio simplifies local model inference by bundling model management, quantization selection, and API serving into a single desktop app. Used as the inference backend by local agentic coding practitioners like [[entities/vicki-boykis]].

## Key Features

- **Model discovery**: Browse and download GGUF models from Hugging Face directly within the app
- **OpenAI-compatible API**: Serves models at `http://localhost:1234/v1`, compatible with any OpenAI SDK/client
- **Model configuration**: Adjust context window, quantization, system prompts, and GPU allocation
- **Session introspection**: View live token inference, token in/out counts, KV cache usage
- **Multiple model support**: Load and switch between models

## Usage in Agentic Coding

LM Studio is commonly paired with agent harnesses like [[pi-coding-agent]] or [[entities/claude-code]] (via local provider) to run agentic coding workflows entirely locally. Configuration typically involves:

1. Download a model (e.g., `gemma-4-26b-a4b`, `gemma-4-12b-qat`)
2. Start the local server on port 1234
3. Point the agent harness at `http://localhost:1234/v1` (or `host.docker.internal:1234/v1` for Docker setups)

## Trade-offs

- Convenient GUI but adds overhead vs raw [[concepts/llama-cpp]]
- Context window limited by hardware (typically 32K-128K on consumer hardware)
- KV cache can consume significant RAM (up to 64 GB for large models on Apple Silicon)

## Alternatives

- [[concepts/ollama]] — CLI-first local inference, lighter weight
- [[concepts/llama-cpp]] — Raw C++ inference, minimal overhead
- llamafiles — Single-file portable model executables
- vLLM — High-throughput server-side inference

## See Also

- [[entities/vicki-boykis]] — Blog post documenting LM Studio in local agentic workflow
- [[local-llm-inference]] — Concept page on local model inference approaches
- [[entities/gemma-4]] — Google model family frequently used with LM Studio
