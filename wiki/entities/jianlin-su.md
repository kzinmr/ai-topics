---
title: Jianlin Su
created: 2026-08-07
updated: 2026-08-07
type: entity
tags: [deepseek, researcher, china, rope, position-encoding, ai-researcher]
sources:
  - raw/articles/2021-04-20_2104.09864_roformer-rotary-position-embedding.md
  - https://x.com/Xianbao_QIAN/status/2085316531894853967
related:
  - concepts/transformer-architecture.md
  - entities/deepseek.md
  - concepts/llm-architecture.md
aliases:
  - Su Jianlin
---

# Jianlin Su

Jianlin Su is a Chinese AI researcher best known as the inventor of **Rotary Position Embedding (RoPE)**, one of the most impactful innovations in modern LLM architecture. RoPE has been adopted by virtually all major open-source language models since 2023, including Llama, DeepSeek, Qwen, Mistral, and Kimi.

## RoPE (Rotary Position Embedding)

Su introduced RoPE in the 2021 paper **"RoFormer: Enhanced Transformer with Rotary Position Embedding"** (arXiv:2104.09864), co-authored with Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, and Yunfeng Liu.

RoPE encodes positional information by applying rotation matrices to query and key vectors in the self-attention mechanism. Unlike absolute position embeddings (which learn a fixed vector per position) or relative position biases (which add offsets to attention scores), RoPE:

- Encodes **relative position** naturally through the rotation angle difference between positions
- Can be **seamlessly integrated** into existing attention mechanisms without architectural changes
- Maintains **theoretical elegance** grounded in complex number rotation in high-dimensional spaces
- Supports **arbitrary sequence lengths** and long-context extension through position interpolation

The core insight is remarkably simple: rotate the query and key vectors by an angle proportional to their position index. The dot product between two rotated vectors depends only on their relative position difference, giving the model relative position awareness for free.

## Impact on the LLM Ecosystem

RoPE's adoption trajectory is extraordinary:

| Model Family | First RoPE Adoption | Notes |
|---|---|---|
| **Llama** (Meta) | Llama 1 (Feb 2023) | All Llama variants use RoPE |
| **DeepSeek** | DeepSeek-V2 (2024) | Su is a key researcher at DeepSeek |
| **Qwen** (Alibaba) | Qwen-1 (2023) | All Qwen generations use RoPE |
| **Mistral** | Mistral 7B (Sep 2023) | All Mistral models use RoPE |
| **Kimi / Moonshot** | Kimi (2023) | Long-context pioneer |
| **Gemma** (Google) | Gemma 2 (2024) | Google's open models |
| **Mixtral** | Mixtral 8x7B (Dec 2023) | MoE with RoPE |

By 2026, RoPE is so dominant that positional encoding choices have largely converged. Alternatives like ALiBi and NoPE exist but are niche. RoPE's success is a rare case where a single elegant mathematical idea wins on both theoretical and empirical grounds.

## Career and Affiliation

Jianlin Su is affiliated with **DeepSeek**, where he continues to work on model architecture and training methodology. He was born in 1993, making him one of the most influential young researchers in the Chinese AI ecosystem.

Su is known within the Chinese ML community for his technical blog and willingness to share detailed mathematical derivations. His work exemplifies the "research as craft" ethos — taking a simple mathematical idea (rotation in high-dimensional space) and demonstrating its practical superiority through rigorous experimentation.

## Research Contributions Beyond RoPE

Su has contributed to several other areas of ML research:
- **Transformer architecture optimization** — improving efficiency and expressiveness of attention mechanisms
- **Pre-training methodology** — contributions to the training recipes used at DeepSeek
- **Mathematical ML** — blog posts and technical notes explaining complex ML concepts with clear derivations (in Chinese)

## See Also

- RoPE is used in [[concepts/transformer-architecture]] as the standard position encoding
- Su's current employer: [[entities/deepseek]]
- Related position encoding techniques: position interpolation, context extension, YaRN
- The broader trend of Chinese AI research talent: [[entities/china-ai-industry]]
