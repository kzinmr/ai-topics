---
title: "LLM Parameter Counts"
type: concept
created: 2026-07-11
updated: 2026-07-11
tags:
  - llm
  - transformer-architecture
  - education
  - model
  - scaling
sources:
  - raw/articles/gilesthomas.com--2026-07-llm-parameter-counts--674e98c7.md
---

# LLM Parameter Counts

Understanding how parameters are distributed across components of a Large Language Model is essential for building intuition about model size, memory requirements, and architectural tradeoffs. A common surprise is how **unevenly** parameters are distributed.

## Parameter Breakdown in GPT-2 Architecture

A standard GPT-2 model has four main parameter groups:

| Component | Description | Typical Share |
|-----------|-------------|---------------|
| **Input embeddings** | Maps tokens to vectors (vocab_size × d_model) | Large for small models |
| **Attention layers** (Q, K, V, O projections) | The mechanism everyone focuses on | ~1/3 of transformer block params |
| **Feed-forward networks** (FFN) | Two linear layers with activation | ~2/3 of transformer block params |
| **Output head** | Maps hidden states back to vocab | Large for small models |

### Key Surprises

1. **Embeddings dominate small models**: With a vocab size of 50,257 and embedding dimension of 768, each embedding matrix is ~38M parameters. For GPT-2 small (124M total), input + output embeddings are **~60% of all parameters** without weight tying.

2. **FFN has ~2x the parameters of attention**: Despite attention getting most of the conceptual focus, the feed-forward network in each transformer block has roughly twice as many parameters as the attention layers. For a standard FFN with 4× expansion: `2 × (d_model × 4 × d_model)` vs attention's `4 × (d_model × d_model)`.

3. **Weight tying** (sharing input/output embedding matrices) significantly reduces total parameter count, especially for smaller models.

4. **Modern models have much larger vocabularies** (hundreds of thousands of tokens), making embeddings an even larger fraction of total parameters.

## Scaling Intuition

- **Small models** (124M params): Embeddings can be >50% of total parameters
- **Medium models** (1.5B params): Transformer layers dominate, embeddings are a smaller fraction
- **Large models** (70B+ params): Transformer layers are overwhelmingly dominant; embeddings are a rounding error

## Why This Matters

- **Memory estimation**: When planning GPU memory for inference, knowing the parameter distribution helps estimate KV cache vs model weight memory
- **Pruning and compression**: Embedding-heavy models may benefit more from vocabulary reduction than attention pruning
- **Training efficiency**: The "uninteresting" FFN layers contain most of the model's capacity — understanding them is key to understanding scaling
- **Architecture decisions**: Weight tying, vocabulary size, and FFN expansion ratio are high-leverage design choices

## Visualization Tool
Giles Thomas built an interactive [GPT-2 parameter visualizer](https://www.gilesthomas.com/2026/07/llm-parameter-counts) (using GPT-5.6 Sol via Codex) that shows parameter breakdowns for different model sizes and configurations, including custom settings with weight tying and QKV bias toggles.

## Related
- [[concepts/transformer-architecture]]
- [[concepts/scaling-laws]]
- [[concepts/llm]]
- [[concepts/tokenization]]
- [[concepts/kv-cache]]
- [[entities/gpt-2]]
