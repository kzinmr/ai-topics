---
title: DFlash
created: 2026-04-26
updated: 2026-04-26
type: concept
tags: [inference, optimization, speculative-decoding, diffusion]
sources: [raw/articles/dflash-z-lab-arxiv-2602-06036.md]
---
# DFlash

Lightweight block diffusion model for flash speculative decoding — replaces sequential draft generation with parallel diffusion-based drafting for >6x speedup.

## Definition

DFlash is a **speculative decoding** system that replaces the traditional autoregressive draft model with a **lightweight block diffusion model**. This enables parallel token drafting in a single forward pass, eliminating the sequential bottleneck inherent in conventional speculative decoding.

## The Problem

Autoregressive LLMs decode token-by-token, causing:
- High inference latency
- Poor GPU utilization
- Sequential bottleneck in speculative decoding's draft phase

Traditional speculative decoding uses a smaller "draft model" to predict tokens, which are then verified in parallel by the target model. But the draft model itself is autoregressive — it generates tokens sequentially, capping practical speedups.

## How DFlash Works

### Core Architecture
1. **Block Diffusion Draft Model**: A lightweight diffusion model trained specifically for token block generation
2. **Single Forward Pass Drafting**: Generates multiple draft tokens simultaneously — no sequential drafting
3. **Context-Aware Conditioning**: The draft model is conditioned on features extracted directly from the target LLM, ensuring draft tokens align with the target's distribution
4. **Standard Verification**: Drafted tokens pass through the existing speculative decoding verification pipeline unchanged

### Key Innovation
Instead of asking a small model to sequentially predict the next tokens, DFlash asks a diffusion model to generate a block of tokens in one shot. The target LLM then verifies (accepts or rejects) each drafted token in parallel.

## Performance

| Metric | Result |
|--------|--------|
| Lossless acceleration | >6x across diverse models and tasks |
| vs EAGLE-3 (SOTA) | Up to 2.5x higher speedup |
| Quality | Lossless — no generation quality degradation |
| GPU utilization | Significantly improved |

## Supported Models

DFlash provides draft models for a wide range of LLMs:
- **Qwen3.5-122B-A10B** → [Qwen3.5-122B-A10B-DFlash](https://huggingface.co/z-lab/Qwen3.5-122B-A10B-DFlash)
- **Qwen3.6-35B-A3B** → [Qwen3.6-35B-A3B-DFlash](https://huggingface.co/z-lab/Qwen3.6-35B-A3B-DFlash)
- **Qwen3.6-27B** → [Qwen3.6-27B-DFlash](https://huggingface.co/z-lab/Qwen3.6-27B-DFlash) (Preview)
- **Kimi-K2.5** → [Kimi-K2.5-DFlash](https://huggingface.co/z-lab/Kimi-K2.5-DFlash)
- **gpt-oss-120b** → [gpt-oss-120b-DFlash](https://huggingface.co/z-lab/gpt-oss-120b-DFlash)
- **LLaMA-3.1-8B** → [LLaMA3.1-8B-DFlash](https://huggingface.co/z-lab/LLaMA3.1-8B-Instruct-DFlash-UltraChat)
- Plus Qwen3.5 4B/9B/27B/35B-A3B, Qwen3-Coder models, and more

Training recipes will be open-sourced for custom draft model creation.

## Integration

### vLLM
```bash
vllm serve Qwen/Qwen3.5-27B \
  --speculative-config '{"method": "dflash", "model": "z-lab/Qwen3.5-27B-DFlash"}' \
  --attention-backend flash_attn
```

### SGLang
```bash
python -m sglang.launch_server \
    --model-path Qwen/Qwen3.5-35B-A3B \
    --speculative-algorithm DFLASH \
    --speculative-draft-model-path z-lab/Qwen3.5-35B-A3B-DFlash \
    --speculative-num-draft-tokens 16
```

### Transformers
Only Qwen3 and LLaMA-3.1 models currently supported.

### MLX (Apple Silicon)
Also available for MLX backend.

## GitHub & Ecosystem

- **GitHub**: https://github.com/z-lab/dflash (2.3k stars, 161 forks)
- **HuggingFace Collection**: https://huggingface.co/collections/z-lab/dflash
- **Project Blog**: https://z-lab.ai/projects/dflash/
- **License**: MIT

## Related Concepts

- [[speculative-decoding]] — Framework for accelerating LLM inference via draft-verify
- [[recursive-language-models]] — Alternative paradigm for unbounded context management
- [[turboquant]] — Complementary optimization for KV cache memory reduction
- [[memory-architecture]] — KV cache management and memory optimization

## Open Questions

- How does DFlash compare to autoregressive draft models (EAGLE, Medusa) on different model families?
- What is the training data and recipe for DFlash draft models? (Expected to be open-sourced)
- Does DFlash's diffusion approach scale to very long context lengths (>128K tokens)?
- How does DFlash handle multi-modal models beyond text?
