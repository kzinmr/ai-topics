---
title: LLaMA 4
created: 2026-06-09
updated: 2026-06-09
type: concept
tags: [model, open-source, multimodal, meta, moe, foundation-models, llama]
sources:
  - raw/articles/2026-06-09_meta-llama-4.md
---

# LLaMA 4

**LLaMA 4** is Meta's fourth-generation open-weight large language model family, released in April 2026. It succeeds [[concepts/llama-3]] and introduces multimodal capabilities, new architecture variants, and significant performance improvements over its predecessor.

## Overview

LLaMA 4 represents Meta's continued commitment to open-weight AI research, offering models that compete with proprietary frontier systems while being freely available for research and commercial use (under custom licensing terms).

## Model Variants

### LLaMA 4 Scout
The compact variant optimized for edge deployment and resource-constrained environments. Designed for on-device inference with competitive performance at smaller parameter counts.

### LLaMA 4 Maverick
The full-scale flagship model delivering state-of-the-art performance across benchmarks. Targets the frontier model tier alongside [[concepts/deepseek-v4|DeepSeek-V4]], [[concepts/gpt/gpt-5-5|GPT-5.5]], and [[concepts/claude-opus|Claude Opus 4.8]].

## Architecture

- **Multimodal**: Native vision-language capabilities (text + image understanding)
- **Mixture of Experts (MoE)**: Community analysis suggests MoE architecture for efficient scaling
- **Open-Weight**: Available for download and fine-tuning under Meta's custom license

## Competitive Positioning

| Model | Release | Open-Weight | Multimodal | Key Advantage |
|-------|---------|-------------|------------|---------------|
| LLaMA 4 | Apr 2026 | Yes | Yes | Open research ecosystem |
| DeepSeek V4 | Apr 2026 | Yes | Limited | 1M context window |
| Qwen 3.7 | 2026 | Yes | Yes | Multilingual strength |
| GPT-5.5 | 2026 | No | Yes | Frontier reasoning |

## Ecosystem

LLaMA 4 models are available through:
- **[[entities/meta|Meta AI]]** — Official distribution
- **[[entities/huggingface|Hugging Face]]** — Community hosting and fine-tuning
- **[[concepts/ollama|Ollama]]** — Local deployment
- **[[concepts/llama-cpp|llama.cpp]]** — CPU/GPU inference

## Community Discussion

The open-weight vs open-source debate continues with LLaMA 4's custom license terms, which include usage restrictions not present in truly open-source licenses. The models' competitive positioning against DeepSeek V4 (which achieved a 75% price reduction) and Qwen 3.7 (strong multilingual capabilities) is an active topic in the AI community.

## See Also

- [[concepts/llama-3|LLaMA 3]] — Previous generation
- [[concepts/deepseek-v4|DeepSeek V4]] — Key competitor
- [[concepts/open-weight-ai|Open-Weight AI]] — Licensing philosophy
- [[entities/meta|Meta AI]] — Developer organization
- [[concepts/foundation-models|Foundation Models]]
