---
title: "DS4 (DwarfStar 4) — antirez Local AI Inference Project"
created: 2026-05-15
updated: 2026-05-15
type: concept
tags:
  - local-llm
  - inference
  - quantization
  - deepseek
  - open-source
  - tool
  - coding-agent
  - hardware
  - model
aliases: [ds4, dwarfstar-4, antirez-ds4]
sources:
  - raw/articles/antirez.com--news-165--a8668e18.md
  - https://github.com/antirez/ds4
---

# DS4 (DwarfStar 4)

## Overview

**DS4 (DwarfStar 4)** is Salvatore Sanfilippo's ([[entities/antirez-com|antirez]]) local AI inference project that loads **DeepSeek V4 Flash** using extreme **asymmetric quantization (2/8-bit)** to run frontier-quality models on consumer hardware (96-128GB RAM Macs). Built in approximately one week using GPT-5.5 as a coding partner, DS4 became one of the fastest-growing local AI projects of early 2026.

The project represents a significant milestone: antirez describes it as the **first time a local model has been usable for "serious stuff"** that he would normally delegate to cloud frontier models (Claude, GPT). The asymmetric quantization recipe — 2-bit for most layers, 8-bit for critical ones — is the key enabler, allowing the 685B-parameter DeepSeek V4 Flash to fit in consumer RAM while maintaining near-frontier quality.

## Architecture

- **Single-model focus**: Unlike general-purpose runners (llama.cpp, Ollama), DS4 is optimized for one specific model: DeepSeek V4 Flash. This specialization enables deep optimizations.
- **2/8-bit asymmetric quantization**: Most layers at 2-bit precision with critical layers at 8-bit — a recipe that preserves reasoning quality while dramatically reducing memory footprint
- **Vector steering**: Built-in support for steering model behavior, giving users more control over output than cloud APIs allow
- **GitHub**: https://github.com/antirez/ds4

## Relationship to Other Projects

- **vs. [[concepts/ds4-deepseek-flash-metal|ds4.c (Armin Ronacher)]]**: Ronacher's fork focuses on Apple Silicon Metal GPU acceleration and Pi extension integration. Antirez's original DS4 is the upstream project that spawned this fork.
- **vs. [[concepts/llama-cpp]]**: llama.cpp is a general-purpose GGUF runner; DS4 is model-specific with hand-tuned quantization for one architecture.
- **vs. Ollama / LM Studio**: These are user-friendly wrappers; DS4 is a developer-focused tool designed for power users comfortable with terminal-based workflows.

## Future Plans (from antirez's May 14, 2026 update)

1. **Quality benchmarks** — systematic evaluation to track model quality across updates
2. **Coding agent integration** — built-in coding agent as part of the DS4 project (not an external harness)
3. **Dedicated CI hardware** — a home server to run continuous integration for long-term quality
4. **More ports and platform support**
5. **Distributed inference** — both serial and parallel modes, enabling larger-than-RAM models across multiple machines (antirez describes this as "a very important point")
6. **Model-specific variants** — plans for ds4-coding, ds4-legal, ds4-medical expert variants. Philosophy: "you just load what you need depending on the question." Not tied to MoE architecture — these are separate fine-tuned checkpoints, not a single model with expert routing.

### Model-Agnostic Philosophy

Antirez explicitly states DS4 is not tied to DeepSeek V4 Flash forever. The project will track "the best current open weights model that is *practically fast* on a high-end Mac or 'GPU in a box' gear (like the DGX Spark)." The next expected contender is V4 Flash's upcoming checkpoint, potentially a coding-tuned version.

## Key Insight

> "It is the first time since I play with local inference that I find myself using a local model for serious stuff that I would normally ask to Claude / GPT. This, I think, is really a big thing."

> "AI is too critical to be just a provided service."

Antirez frames the local vs. cloud experience as a spectrum: **A** = the traditional small local model experience, **B** = the frontier model you use online. DS4 is "a lot more B than A" — a qualitative shift, not just incremental improvement. The combination of (a) a quasi-frontier open-weights model, (b) asymmetric quantization that works, and (c) sufficient consumer hardware (96-128GB Macs) has created a tipping point for local AI.

## Related Pages

- [[entities/antirez-com]] — Project creator
- [[concepts/ds4-deepseek-flash-metal]] — Armin Ronacher's Metal-optimized fork
- [[concepts/deepseek-v4]] — The underlying model
- [[entities/deepseek]] — Model provider
- [[concepts/llama-cpp]] — General-purpose local inference
- [[concepts/local-llm]] — Broader local AI movement
