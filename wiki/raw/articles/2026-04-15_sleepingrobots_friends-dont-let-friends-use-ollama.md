---
title: "Friends Don't Let Friends Use Ollama"
source_url: "https://sleepingrobots.com/dreams/stop-using-ollama/"
author: Zetaphor
date: 2026-04-15
fetched: 2026-06-16
type: raw-article
tags:
  - ollama
  - local-llm
  - llama-cpp
  - controversy
  - vendor-lock-in
  - open-source
---

# Friends Don't Let Friends Use Ollama

**Source**: [sleepingrobots.com](https://sleepingrobots.com/dreams/stop-using-ollama/)
**Author**: Zetaphor (April 15, 2026, updated April 18, 2026)
**HN Discussion**: [news.ycombinator.com/item?id=47788385](https://news.ycombinator.com/item?id=47788385) (648 points, 208 comments)

## Summary

Ollama gained traction by being the first easy llama.cpp wrapper, then spent years dodging attribution, misleading users, and pivoting to cloud, all while riding VC money earned on someone else's engine.

## Key Arguments

### 1. A llama.cpp Wrapper With Amnesia

- Ollama's entire inference capability comes from **llama.cpp** (created by Georgi Gerganov, March 2023)
- For over a year, Ollama's README contained **no mention of llama.cpp**
- Binary distributions didn't include required MIT license notice
- GitHub issue #3185 went **400+ days without a response** from maintainers
- When acknowledged, Ollama's team wrote: "We spend a large chunk of time fixing and patching it up... Overtime, we will be transitioning to more systematically built engines"

### 2. The Fork That Made Things Worse

- Mid-2025: Ollama moved away from llama.cpp to a custom implementation on top of **ggml** (lower-level tensor library)
- Result: reintroduced bugs that llama.cpp had solved years ago
- Georgi Gerganov himself identified that Ollama had forked and made bad changes to GGML
- **Performance**: llama.cpp runs **1.8x faster** than Ollama (161 vs 89 tokens/sec), CPU gap is 30-50%
- Qwen-3 Coder 32B: ~70% higher throughput with llama.cpp

### 3. Misleading Model Naming

- DeepSeek R1 distilled models listed simply as "DeepSeek-R1" (stripped "R1-Distill" prefix)
- Running `ollama run deepseek-r1` pulls an 8B Qwen-derived distillate, not the real 671B model
- GitHub issues #8557 and #8698 were closed as duplicates with no fix
- "DeepSeek-R1" drives more downloads than "DeepSeek-R1-Distill-Qwen-32B"

### 4. The Closed-Source App

- July 2025: GUI desktop app released in private repository, shipped without a license
- Potential AGPL-3.0 dependencies found in the binary
- Website placed download button next to GitHub link, giving impression of open-source tool
- Code eventually merged into main repo in November 2025

### 5. The Modelfile: Reinventing a Solved Problem

- GGUF spec: "Full information: all information needed to load a model is contained in the model file"
- Ollama's Modelfile duplicates this with a separate Docker-inspired config file
- Ollama only auto-detects chat templates from a hardcoded list; falls back to bare `{{ .Prompt }}` for unknown templates
- Changing parameters copies the entire model (30-60GB)
- Users must translate Jinja templates to Go template syntax

### 6. The Registry Bottleneck

- New models appear on Hugging Face within hours; Ollama registry takes days/weeks
- Only supports Q4_K_S, Q4_K_M, Q8_0, F16, F32 quantizations (no Q5, Q6, IQ quants)
- Models hashed in proprietary blob storage, can't share with other tools
- "Vendor lock-in most users don't notice until they try to leave"

### 7. The Cloud Pivot

- Late 2025: cloud-hosted models alongside local library
- Proprietary models like MiniMax appeared without clear disclosure about data routing
- CVE-2025-51471: token exfiltration vulnerability affecting all versions

### 8. The VC Pattern

- Y Combinator-backed (W21) startup
- Progression: wrap open-source → minimize attribution → create lock-in → launch closed-source → add cloud services

## Recommended Alternatives

| Tool | Description |
|------|-------------|
| **llama.cpp** | The engine itself. OpenAI-compatible API server, web UI, full control, 450+ contributors |
| **llamafile** | Single executable, runs on 6 OSes, no install |
| **llama-swap** | Multi-model orchestration behind single API endpoint |
| **LiteLLM** | Unified OpenAI-compatible proxy across multiple backends |
| **Jan** | AGPLv3 local-first chat app, clean interface |
| **koboldcpp** | AGPL llama.cpp fork with built-in web UI |
| **LM Studio** | Closed-source but good-faith wrapper, proper acknowledgements |
| **ramalama** | Red Hat's container-native model runner |

## Key HN Comments

- "For most users that wanted to run LLM locally, ollama solved the UX problem. If llama provides such UX, they failed terrible at communicating that."
- "Ollama is about 1000x easier to use. Llama.cpp is a great project, but it's also one of the least user friendly pieces of software I've used."
- "The hashed blob storage means if you've been pulling models for months, switching tools requires re-downloading everything."
- "It's as if Ollama is trying to create a walled garden, but the garden is outside of their property."
