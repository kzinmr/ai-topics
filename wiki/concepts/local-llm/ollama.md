---
title: "Ollama — Local LLM Runner"
type: concept
created: 2026-04-15
updated: 2026-04-29
status: complete
tags:
  - local-llm
  - developer-tooling
  - open-source
aliases: [ollama-runner, ollama-cli]
sources:
  - url: "https://ollama.com/"
    title: "Ollama — Official Site"
  - url: "https://github.com/ollama/ollama"
    title: "Ollama — GitHub Repository"
  - url: "https://myaiguide.co/repos/ollama-ollama"
    title: "Ollama: Run AI Models Locally (2026 Guide)"
---
# Ollama — Local LLM Runner

**Ollama** is an open-source tool for running large language models (LLMs) locally. Implemented in Go and released under the MIT license. As of April 2026, it has achieved **168,000 GitHub Stars** and **52 million monthly downloads**, making it the most widely used local LLM runner.

## Architecture

Ollama uses **llama.cpp** as its internal engine, providing model management, a REST API, and a CLI interface on top.

```
User (CLI / API)
    ↓
Ollama (Go implementation)
    ├─ Model Registry (1000+ models)
    ├─ Modelfile System
    └─ llama.cpp (C++ inference engine)
         ├─ GGUF Quantization
         ├─ GPU Acceleration (CUDA/Metal/ROCm)
         └─ CPU + GPU Hybrid Inference
```

## Key Features

| Feature | Description |
|---------|------------|
| **One-line install** | `curl -fsSL https://ollama.com/install.sh | sh` |
| **Model management** | `ollama pull <model>` / `ollama rm <model>` |
| **Interactive mode** | `ollama run <model>` for instant chat |
| **REST API** | OpenAI-compatible endpoints (`/api/chat`, `/api/generate`) |
| **Auto GPU detection** | CUDA (NVIDIA), Metal (Apple), ROCm (AMD) |
| **Modelfile** | Custom system prompts, parameters, templates |
| **Cross-platform** | Linux, macOS, Windows |
| **Multi-model switching** | Host multiple models on a single server |

## Modelfile Format

```dockerfile
FROM llama3.2

# System prompt configuration
SYSTEM "You are a helpful AI assistant. Please answer in English."

# Parameter settings
PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER num_ctx 4096

# Template settings
TEMPLATE """{{ .System }}
User: {{ .Prompt }}
Assistant: """
```

## Supported Models (as of April 2026)

Supports 50+ major models:
- **Meta**: Llama 3/3.1/3.2/4, Llama 3.3 Nemotron
- **Google**: Gemma 2/3
- **DeepSeek**: DeepSeek V3, DeepSeek-R1
- **Alibaba**: Qwen 2.5/3
- **Microsoft**: Phi-3/4
- **Mistral**: Mistral, Mixtral
- **NousResearch**: Hermes series
- **Others**: Kimi-K2.5, GLM-5, MiniMax, gpt-oss

## Performance Benchmarks

| Hardware | 7B Q4_K_M | 13B Q4_K_M | 70B Q4_K_M |
|----------|-----------|-----------|-----------|
| RTX 4060 (8GB) | 40+ tok/s | — | — |
| RTX 4090 (24GB) | 100+ tok/s | 50+ tok/s | 10+ tok/s |
| Mac M3 Max (96GB) | 60+ tok/s | 35+ tok/s | 8+ tok/s |
| CPU only (32GB RAM) | 5-10 tok/s | 2-5 tok/s | — |

## Use Cases

1. **Development & prototyping**: Quickly try models locally
2. **Private chat**: No data sent externally
3. **Agent backend**: Use Ollama as the LLM backend for local agents
4. **Education & learning**: Understand and experiment with model behavior
5. **Offline environments**: Provide AI functionality without internet connection

## Cloud Plans (2026)

Ollama launched cloud services in 2026:
- **Free**: Basic cloud access
- **Pro** ($20/mo): 3 parallel models, 50x cloud usage
- **Max** ($100/mo): 10 parallel models, 5x usage

## Ollama vs Other Tools

| Tool | Strengths | Weaknesses |
|------|-----------|------------|
| **Ollama** | Ease of use, model registry, cross-platform | Limited customization |
| **LM Studio** | GUI, model discovery via GUI | Weak server mode |
| **llama.cpp** | Best performance, full customization | Complex setup |
| **LocalAI** | Full OpenAI API compatibility | Smaller community |
| **vLLM** | Production inference optimization | Heavy setup |

## Related wikilinks

- [[concepts/inference/llama-cpp]] — llama.cpp inference engine
- [[concepts/local-llm/_index]] — Local LLM ecosystem overview
- [[concepts/local-llm/inference-hardware]] — Inference hardware requirements
- [[concepts/inference/sglang]] — SGLang fast inference

## Sources

- [Ollama Official Site](https://ollama.com/)
- [Ollama GitHub](https://github.com/ollama/ollama)
- [Ollama: Run AI Models Locally (2026 Guide)](https://myaiguide.co/repos/ollama-ollama)
