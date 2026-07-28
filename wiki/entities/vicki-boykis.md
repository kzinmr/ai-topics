---
title: Vicki Boykis
type: entity
aliases: [vboykis, veekaybee]
created: 2026-06-18
updated: 2026-07-28
status: L3
sources:
  - raw/articles/vickiboykis.com--running-local-models-is-good-now--2026-06-15.md
  - https://vickiboykis.com/about/
  - https://vickiboykis.com/
tags:
  - person
  - blogger
  - data-science
  - local-llm
  - ml-engineer
  - recsys
  - search
  - embeddings
  - community-builder
---

# Vicki Boykis

**Vicki Boykis** is a founding ML engineer, prolific tech blogger at [vickiboykis.com](https://vickiboykis.com), and active community builder in the local LLM / open-source AI space. X: [@vboykis](https://x.com/vboykis), GitHub: [veekaybee](https://github.com/veekaybee).

## Professional Background

### Current Role
Founding ML engineer at a startup focused on recommendation systems, personalization, and information retrieval.

### Previous Experience
- **Mozilla.ai** — Worked on LLMs and LLM infrastructure
- **Duo** — ML and recommendation systems
- **Tumblr / Automattic** — ML engineering
- **Comcast** — ML engineering

### Education & Credentials
- Author of peer-reviewed paper on embeddings (DOI: [10.5281/zenodo.8015029](https://zenodo.org/record/8015029))
- Technical editor for *Building Recommendation Systems* and *SQL for Data Scientists*
- Contributor to Increment Magazine ("The Best-Laid Plans", "Architecture for Generations")

## Core Interests

- **Local LLM inference**: Running models locally on Apple Silicon hardware since early open-weight model releases. Evaluates models across multiple inference engines (llama.cpp, Ollama, LM Studio).
- **Agentic coding with local models**: Uses Pi (pi.dev) as agent harness with LM Studio as inference server, running in Docker containers for sandboxing.
- **Search & information retrieval**: Background in embeddings, information retrieval, and distributed systems. Built Viberary (book recommendations by vibe). Working on Rijksearch.
- **ML/data science tooling**: BERTopic-based blog post tagging, recommendation systems (two-tower models), MLOps and production ML, distributed systems.

## Key Contributions

### Local Models Assessment (Jun 2026)
Identified GPT-OSS as the inflection point where local models became "good enough" — the first model where she stopped double-checking against API models. With Gemma 4 family, achieved local agentic coding at ~75% accuracy/speed of frontier models on M2 Mac (64 GB RAM).

Preferred setup: [[entities/lm-studio]] as inference server + [[pi-coding-agent]] as agent harness, all Docker-sandboxed.

### Viberary (Book Recommendation by Vibe)
Built Viberary, a recommendation system that recommends books based on "vibe" — a notable example of applied embeddings and information retrieval in the cultural domain.

### Embeddings Paper
Authored "Embeddings Approaches" (DOI: 10.5281/zenodo.8015029), a paper explaining what embeddings are and how they work — widely referenced in ML education.

### Normconf (Conference Organizer)
Founded and ran **Normconf**, an ML/data conference that brought together practitioners for talks on applied ML engineering.

### Community & Keynotes
- **AMLC Charlottesville** Keynote (2026)
- **Pycon Italia** Keynote (2024)
- **PyData Amsterdam** Keynote (2023)
- **Normconf** Keynote (2022)

### Practical Workflow
- Refactoring Python notebooks into modular repos
- Type hint linting (PEP 585 generics)
- Blog post proofreading
- Unit test generation
- Bootstrapping ML project repos (e.g., two-tower recommendation models)

## Blog

Blog at vickiboykis.com covers: LLMs, ML engineering, data science, search, embeddings, open-source, career advice, computing history. Posts span 2022-2026 with increasing focus on local LLM workflows.

### Notable Posts (2025-2026)
- **Running local models is good now** (Jun 2026) — Assessment of GPT-OSS as local model inflection point
- **We should be more tired than the model** (May 2026) — Agentic coding reflections
- **Tagging my blog posts with BERTopic and LLMs** (May 2026) — Applied ML tooling
- **Mechanical sympathy** (Apr 2026) — Understanding hardware for ML work
- **Querying 3 billion vectors** (Feb 2026) — Large-scale vector search
- **How big are our embeddings now and why?** (Sep 2025) — Embedding size analysis
- **GGUF, the long way around** (Feb 2024) — Deep dive into GGUF format for local models
- **Don't worry about LLMs** (May 2024) — Practical perspective on LLM adoption
- **Why are we using LLMs as calculators?** (Nov 2024) — Critical take on LLM misuse

### Writing Style & Philosophy
Boykis writes in a direct, practitioner-focused voice that blends technical depth with clear explanations. Her posts frequently connect low-level implementation details (GGUF internals, vector search architecture) to high-level engineering philosophy (mechanical sympathy, owning software problems). She is notably transparent about failures and uncertainties, and consistently advocates for understanding fundamentals over chasing trends.

## Cross-References

- [[entities/lm-studio]] — Her inference server of choice
- [[pi-coding-agent]] — Agent harness she uses for local agentic coding
- [[entities/gemma-4]] — Google's model family she recommends for local use
- [[entities/gpt-oss]] — OpenAI's open-weight model she identified as the local quality inflection point
- [[concepts/ollama]] — Another inference engine she has used
- [[concepts/local-llm-inference]] — The broader practice of running models locally
- [[concepts/embeddings]] — Her paper and ongoing interest in embeddings

## References

- [vickiboykis.com](https://vickiboykis.com)
- [About page](https://vickiboykis.com/about/)
- [GitHub: veekaybee](https://github.com/veekaybee)
- [Embeddings Paper (Zenodo)](https://zenodo.org/record/8015029)
