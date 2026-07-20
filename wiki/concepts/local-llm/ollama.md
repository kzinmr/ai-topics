---
title: "Ollama — Local LLM Runner"
type: concept
created: 2026-04-15
updated: 2026-07-20
status: complete
tags:
  - local-llm
  - developer-tooling
  - open-source
  - controversy
  - vendor-lock-in
aliases: [ollama-runner, ollama-cli]
sources:
  - url: "https://ollama.com/"
    title: "Ollama — Official Site"
  - url: "https://github.com/ollama/ollama"
    title: "Ollama — GitHub Repository"
  - url: "https://myaiguide.co/repos/ollama-ollama"
    title: "Ollama: Run AI Models Locally (2026 Guide)"
  - url: "https://sleepingrobots.com/dreams/stop-using-ollama/"
    title: "Friends Don't Let Friends Use Ollama (Zetaphor, 2026-04-15)"
  - url: "https://news.ycombinator.com/item?id=47788385"
    title: "HN Discussion (648 points, 208 comments)"
---
# Ollama — Local LLM Runner

**Ollama** is an open-source tool for running large language models (LLMs) locally. Implemented in Go and released under the MIT license. As of April 2026, it has achieved **168,000 GitHub Stars** and **52 million monthly downloads**, making it the most widely used local LLM runner.

## Architecture

Ollama uses **llama.cpp** as its internal engine (since mid-2025 transitioning to a custom ggml-based backend), providing model management, a REST API, and a CLI interface on top.

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

## Controversy & Criticism (2024–2026)

Ollama has faced significant criticism from the local LLM community, most comprehensively documented in [Friends Don't Let Friends Use Ollama](https://sleepingrobots.com/dreams/stop-using-ollama/) (Zetaphor, April 2026, [HN discussion](https://news.ycombinator.com/item?id=47788385) — 648 points, 208 comments).

### Attribution & License Issues
- For over a year, Ollama's README contained **no mention of llama.cpp** despite it being the entire inference backend
- Binary distributions didn't include required MIT license notice for llama.cpp code
- GitHub issue #3185 requesting license compliance went **400+ days without a response**
- Ollama's team stated they planned to "transition to more systematically built engines," distancing from llama.cpp

### The ggml Fork (Mid-2025)
- Ollama moved from llama.cpp to a custom implementation on top of **ggml** (lower-level tensor library)
- Result: reintroduced bugs that llama.cpp had solved years ago (broken structured output, vision model failures, GGML assertion crashes)
- Georgi Gerganov identified that Ollama had forked and made bad changes to GGML
- **Performance gap**: llama.cpp runs **1.8x faster** than Ollama (161 vs 89 tokens/sec on same hardware); CPU gap is 30-50%; Qwen-3 Coder 32B shows ~70% higher throughput with llama.cpp

### Misleading Model Naming
- DeepSeek R1 distilled models listed as "DeepSeek-R1" (stripped "R1-Distill" prefix)
- `ollama run deepseek-r1` pulls an 8B Qwen-derived distillate, not the real 671B model
- GitHub issues #8557 and #8698 closed as duplicates with no fix

### Closed-Source Desktop App (July 2025)
- GUI app released in private repository without a license
- Potential AGPL-3.0 dependencies found in the binary
- Code eventually merged into main repo in November 2025

### Modelfile & Registry Lock-in
- Modelfile duplicates information already embedded in GGUF metadata
- Ollama only auto-detects chat templates from a hardcoded list; falls back to bare `{{ .Prompt }}` for unknown templates
- Changing a parameter (e.g., temperature) copies the entire model (30-60GB)
- Models stored in proprietary hashed blob storage — can't share with other tools without re-downloading
- Registry only supports Q4_K_S, Q4_K_M, Q8_0, F16, F32 quantizations (no Q5, Q6, IQ quants)

### Cloud Pivot & Privacy Concerns
- Late 2025: cloud-hosted models added alongside local library
- Proprietary models (e.g., MiniMax) appeared without clear disclosure about data routing off-machine
- CVE-2025-51471: token exfiltration vulnerability affecting all versions

### VC Pattern
- Y Combinator-backed (W21) startup following familiar playbook: wrap open-source → minimize attribution → create lock-in → launch closed-source → add cloud services

## Recommended Alternatives

| Tool | Type | Description |
|------|------|-------------|
| **llama.cpp** | Open-source (MIT) | The engine itself. llama-server with OpenAI-compatible API, web UI, full control, 450+ contributors |
| **llamafile** | Open-source | Single executable, runs on 6 OSes, no install required |
| **Jan** | Open-source (AGPLv3) | Local-first chat app with clean interface |
| **koboldcpp** | Open-source (AGPL) | llama.cpp fork with built-in web UI and extensive configuration |
| **LM Studio** | Closed-source (good-faith) | One-click GUI, proper llama.cpp acknowledgements, accepts any GGUF |
| **ramalama** | Open-source | Red Hat's container-native model runner with explicit upstream attribution |

## Ollama vs Other Tools

| Tool | Strengths | Weaknesses |
|------|-----------|------------|
| **Ollama** | Ease of use, model registry, cross-platform | Limited customization |
| **LM Studio** | GUI, model discovery via GUI | Weak server mode |
| **llama.cpp** | Best performance, full customization | Complex setup |
| **LocalAI** | Full OpenAI API compatibility | Smaller community |
| **vLLM** | Production inference optimization | Heavy setup |

## Funding History

| Round | Date | Amount | Lead | Details |
|-------|------|--------|------|---------|
| Seed | Unknown | Unknown | Y Combinator (W21) | Initial development |
| Series A | 2026-07-09 | $65M | Undisclosed | Accelerate open model infrastructure, grow team, expand cloud services |

### Series A (2026-07-09) — "All Aboard Open Models"

Ollama raised **$65M in Series A funding** to accelerate development of open model infrastructure, grow the engineering team, and expand cloud services. The funding was announced in a blog post titled "All Aboard Open Models" on July 9, 2026, and gained significant attention on HN (133 points, 54 comments) when it resurfaced on July 19.

**Key context:**
- Ollama had reached **168K GitHub Stars** and **52 million monthly downloads** by April 2026
- Founders: Michael (Kitematic → Docker Desktop, acquired 2015) and the Ollama team
- The raise signals growing investor confidence in open-source AI inference tools
- Positions Ollama to compete with cloud inference providers (Groq, Fireworks, Together AI)
- Follows the YC startup playbook: open-source core → add services → monetize cloud

**HN Discussion Themes:**
- Concerns about the \"open core, closed cloud\" business model
- Comparisons to Docker's trajectory (acquisition → enterprise monetization)
- Debate on whether open-source inference tools can sustain as VC-backed companies
- Excitement about the democratization of local AI

## Related wikilinks

- [[concepts/inference/llama-cpp]] — llama.cpp inference engine
- [[concepts/local-llm/_index]] — Local LLM ecosystem overview
- [[concepts/local-llm/inference-hardware]] — Inference hardware requirements
- [[concepts/inference/sglang]] — SGLang fast inference

## Sources

- [Ollama Official Site](https://ollama.com/)
- [Ollama GitHub](https://github.com/ollama/ollama)
- [Ollama: Run AI Models Locally (2026 Guide)](https://myaiguide.co/repos/ollama-ollama)
