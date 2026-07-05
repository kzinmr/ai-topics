---
title: Vicki Boykis
type: entity
aliases: [vboykis]
created: 2026-06-18
updated: 2026-06-18
status: L2
sources: [raw/articles/vickiboykis.com--running-local-models-is-good-now--2026-06-15.md, https://vickiboykis.com/about/]
tags: [person, blogger, data-science, local-llm]
---

# Vicki Boykis

Data scientist, ML engineer, and prolific tech blogger at [vickiboykis.com](https://vickiboykis.com). X: [@vboykis](https://x.com/vboykis), GitHub: [veekaybee](https://github.com/veekaybee). Active in the local LLM / open-source AI community.

## Core Interests

- **Local LLM inference**: Running models locally on Apple Silicon hardware since early open-weight model releases. Evaluates models across multiple inference engines (llama.cpp, Ollama, LM Studio).
- **Agentic coding with local models**: Uses Pi (pi.dev) as agent harness with LM Studio as inference server, running in Docker containers for sandboxing.
- **Search & information retrieval**: Working on Rijksearch, a search application. Background in embeddings and data science.
- **ML/data science tooling**: BERTopic-based blog post tagging, recommendation systems (two-tower models).

## Key Contributions

### Local Models Assessment (Jun 2026)
Identified GPT-OSS as the inflection point where local models became "good enough" — the first model where she stopped double-checking against API models. With Gemma 4 family, achieved local agentic coding at ~75% accuracy/speed of frontier models on M2 Mac (64 GB RAM).

Preferred setup: [[entities/lm-studio]] as inference server + [[pi-coding-agent]] as agent harness, all Docker-sandboxed.

### Practical Workflow
- Refactoring Python notebooks into modular repos
- Type hint linting (PEP 585 generics)
- Blog post proofreading
- Unit test generation
- Bootstrapping ML project repos (e.g., two-tower recommendation models)

## Blog

Blog at vickiboykis.com covers: LLMs, ML engineering, data science, search, embeddings, open-source, career advice, computing history. Posts span 2024-2026 with increasing focus on local LLM workflows.

## See Also

- [[entities/lm-studio]] — Her inference server of choice
- [[pi-coding-agent]] — Agent harness she uses for local agentic coding
- [[entities/gemma-4]] — Google's model family she recommends for local use
- [[entities/gpt-oss]] — OpenAI's open-weight model she identified as the local quality inflection point
- [[concepts/ollama]] — Another inference engine she has used
