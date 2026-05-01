---
title: GPT-OSS (OpenAI Open Models)
created: 2026-05-01
updated: 2026-05-01
type: entity
tags: [model, open-source, openai, text-generation, moe, local-llm]
sources: [raw/articles/2025-08-05_openai-gpt-oss-open-weight-models.md]
---

# GPT-OSS

OpenAI's first open-weight model release since GPT-2. Released August 5, 2025 under **Apache 2.0 license**. Two Mixture-of-Experts (MoE) variants: `gpt-oss-120b` (117B total, 5.1B active) and `gpt-oss-20b` (21B total, 3.6B active). Trained using reinforcement learning techniques informed by OpenAI's frontier models including o3 and o4-mini.

This release marks a significant strategic shift — OpenAI, historically the most closed of the major AI labs, joining the open-weight movement alongside [[entities/meta]] (LLaMA), [[entities/deepseek]], and [[entities/mistral-ai]].

## Architecture

| Feature | gpt-oss-120b | gpt-oss-20b |
|---|---|---|
| Total Params | 117B | 21B |
| Active/Token | 5.1B | 3.6B |
| Layers | 36 | 24 |
| Experts (Total/Active) | 128/4 | 32/4 |
| Context Window | 128K | 128K |
| Minimum Memory | ~80GB (MXFP4) | ~16GB (MXFP4) |

- **Attention:** Alternating dense and locally banded sparse patterns; Grouped Multi-Query Attention (GQA), group size 8
- **Positional Encoding:** Rotary Positional Embedding (RoPE)
- **Tokenizer:** `o200k_harmony` (open-sourced alongside models)
- **Quantization:** Native MXFP4 support for consumer hardware deployment

## Performance

- **gpt-oss-120b:** Near-parity with o4-mini on core reasoning; outperforms o1 and GPT-4o on HealthBench
- **gpt-oss-20b:** Matches or exceeds o3-mini; optimized for edge/local deployment
- **Adjustable reasoning effort:** low/medium/high — one sentence in system message toggles chain-of-thought depth
- Full chain-of-thought visible to developers (not intended for end-users; may contain hallucinations)

## Safety Framework

- Evaluated under OpenAI's Preparedness Framework
- Internal adversarial fine-tuning on biology and cybersecurity data — models could not reach high-risk capability levels
- $500,000 Kaggle red teaming prize for community-driven safety testing
- CoT monitoring recommended for deployment

## Ecosystem & Deployment
- **Platforms:** Hugging Face, Azure, AWS, vLLM, Ollama, llama.cpp, Databricks
- **Hardware:** NVIDIA, AMD, Cerebras, Groq, Apple Metal
- **Windows:** GPU-optimized ONNX Runtime versions
- **Developer tools:** Harmony Renderer (Python/Rust), Open Model Playground
- **Prompt format:** Harmony prompt format, open-sourced renderer

## Strategic Significance

OpenAI's embrace of open-weight models under Apache 2.0 represents a pragmatic acknowledgment that the open model ecosystem — led by [[entities/meta]]'s LLaMA family, [[entities/deepseek]], and [[entities/qwen3-6-plus]] — has become an unstoppable force. The permissive license enables fine-tuning, commercial use, and on-premises deployment without API dependency.

OpenAI itself recommends hosted API for multimodal support or managed tools, but gpt-oss provides a sovereign alternative.

## Related
- [[entities/openai]] — parent company and broader model family
- [[entities/hugging-face]] — primary distribution platform
- [[concepts/mixture-of-experts]] — MoE architecture principles
- [[concepts/local-llm]] — local deployment landscape
- [[entities/gemma-4]] — Google's competing open model family
- [[entities/gpt-5.5]] — OpenAI's latest proprietary model
