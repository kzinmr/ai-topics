---
type: raw_article
date: 2026-07-31
source: https://huggingface.co/unsloth/DeepSeek-V4-Flash-0731-GGUF
source_type: huggingface_model
title: "Unsloth DeepSeek-V4-Flash-0731 GGUF Quantizations"
description: "GGUF quantizations for DeepSeek-V4-Flash (284B params, 13B active, 1M context) by Unsloth AI. 10 quantization variants from UD-Q8_K_XL (lossless) to UD-IQ1_S."
tags: [model, quantization, gguf, deepseek, unsloth, local-inference]
---

# Unsloth DeepSeek-V4-Flash-0731 GGUF

Unsloth AI released GGUF quantizations for **DeepSeek-V4-Flash** on July 31, 2026.

DeepSeek-V4-Flash is the lightweight variant of the DeepSeek-V4 MoE model series:
- **284B total parameters**, 13B active parameters
- **1M token context window**
- MIT License

## Quantization Variants (10 total)

| Quant | Type | Shards |
|-------|------|--------|
| UD-Q8_K_XL | Lossless (Q8) | 5 |
| UD-Q4_K_XL | 4-bit (Q4) | 5 |
| UD-Q3_K_XL | 3-bit (Q3) | 4 |
| UD-Q2_K_XL | 2-bit (Q2) | 3 |
| UD-IQ4_XS | 4-bit IQ | 4 |
| UD-IQ3_XXS | 3-bit IQ | 4 |
| UD-IQ2_XXS | 2-bit IQ | 3 |
| UD-IQ2_M | 2-bit IQ medium | 3 |
| UD-IQ1_M | 1-bit IQ medium | 3 |
| UD-IQ1_S | 1-bit IQ small | 3 |

## Usage

Supports llama.cpp, Ollama, Unsloth Studio, Docker, Pi coding agent, Hermes Agent, and OpenClaw.

```
# llama.cpp
llama serve -hf unsloth/DeepSeek-V4-Flash-0731-GGUF:UD-Q4_K_XL

# Ollama
ollama run hf.co/unsloth/DeepSeek-V4-Flash-0731-GGUF:UD-Q4_K_XL
```

## Source

Announced via Daniel Han (@danielhanchen) on X: "Lossless UD-Q8_K_XL is out! UD-Q4_K_XL also out!"
https://huggingface.co/unsloth/DeepSeek-V4-Flash-0731-GGUF
