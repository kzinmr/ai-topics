---
title: "Running local models is good now"
author: Vicki Boykis
date: 2026-06-15
url: https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/
tags: [agentic, llms, ml, local-llms, open-source]
---

# Running local models is good now

Local agentic coding has gotten great over the past few months.

Vicki Boykis describes her journey with local models on a 2022 M2 Mac with 64 GB RAM and 1TB storage.

## Models Used
- Mistral 7B
- Gemma 3
- OpenAI OSS-20B
- Qwen 3 MOE (Qwen 2.5 Coder variants)

## Inference Engines
- raw llama.cpp with Open WebUI
- llama-cpp-python
- Ollama
- llamafiles
- LM Studio

## Key Points
- GPT-OSS was the inflection point where local models became "good enough" — first model where she stopped double-checking against API models
- Gemma 4 family (especially `gemma-4-26b-a4b`) enables local agentic coding at ~75% accuracy/speed of frontier models
- `Gemma-4-12b-qat` is smaller/faster alternative with good performance relative to size
- Used for: Python refactoring, type hint linting, blog proofreading, unit tests, bootstrapping repos
- All agentic workflows run in Docker containers with limited permissions

## Setup
- Agent harness: Pi (pi.dev)
- Inference server: LM Studio
- Docker container setup with host.docker.internal networking
- Pi's models.json configured to point at LM Studio endpoint

## Trade-offs
- Inference can be slow
- Context windows are small and hardware-limited
- Early model releases suffer from prompt template mismatches (patched quickly)
- KV cache grows to 64 GB RAM on M2 Mac
- Not yet ready for production software development

## Benefits
- Introspect everything: live token inference, GPU token processing
- Change context window, system prompt, quantizations
- Pit models against each other
- Full control over harness configuration
