---
title: "How Speculative Decoding Boosts vLLM Performance by up to 2.8x"
source: "vLLM Blog"
url: "https://vllm.ai/blog/spec-decode"
author: "vLLM Team"
date: 2025-10-09
tags:
  - inference
  - vllm
  - speculative-decoding
  - performance
  - optimization
---

# How Speculative Decoding Boosts vLLM Performance by up to 2.8x

Speculative decoding is a lossless acceleration technique in vLLM that reduces latency by using a smaller "draft" model to propose tokens, which are then verified in parallel by a larger "target" model.

## Core Mechanism
Traditionally, LLMs generate tokens autoregressively (one-by-one). Speculative decoding changes this into a two-step parallel process:
1. **Drafting:** A small, efficient model proposes a sequence of candidate tokens.
2. **Verification:** The target model performs a **single forward pass** to verify the entire sequence. It accepts correct tokens and corrects the first incorrect one.

> **Key Insight:** This method reduces the number of expensive forward passes required from the large model, significantly cutting down latency without losing accuracy.

## Supported Methods in vLLM

vLLM supports three distinct types of speculative decoding:

### 1. Draft Model-Based
Uses a separate, smaller model (e.g., Llama 68M) to predict tokens for a large model (e.g., Llama 70B).
- **Requirement:** Both models must share the same vocabulary.
- **Challenge:** Finding a compatible small model with the same vocabulary (e.g., Llama 3's unique vocabulary makes this difficult).

### 2. Prompt Lookup Decoding (N-gram Matching)
Instead of a second model, the system looks for repeating patterns within the prompt itself.
- **Best for:** Tasks with high input-output overlap like **summarization** or **document-based Q&A**.
- **Benefit:** Zero additional model overhead.

### 3. Medusa / Eagle / MLPSpeculator
Adds specialized "heads" or layers to the large model to predict multiple future tokens simultaneously.
- **Benefit:** Eliminates the need for a separate draft model by leveraging the target model's internal hidden states.

## Performance Benchmarks

Performance varies significantly based on the Query Per Second (QPS) load:

| Scenario | Dataset | Speedup |
| :--- | :--- | :--- |
| **Low QPS (QPS=1)** | ShareGPT (Draft Model) | **1.5x** |
| **Low QPS (QPS=1)** | CNN/DailyMail (N-gram) | **2.8x** |
| **High QPS** | Various | **1.4x - 1.8x Slowdown** |

**The Trade-off:** In high-QPS (compute-bound) environments, the extra compute required for drafting and verification can create a bottleneck, leading to performance degradation.

## Implementation & Code Examples

### Basic Draft Model Configuration
```python
from vllm import LLM
llm = LLM(
    model="facebook/opt-6.7b",
    speculative_model="facebook/opt-125m",
    num_speculative_tokens=5,
)
```

### N-gram Prompt Lookup
```python
llm = LLM(
    model="facebook/opt-6.7b",
    speculative_model="[ngram]",
    num_speculative_tokens=5,
    ngram_prompt_lookup_max=4,
    ngram_prompt_lookup_min=1,
)
```

### Optimized Tensor Parallelism
To save resources, you can run the draft model on a single GPU while the target model is distributed.
```python
llm = LLM(
    model="meta-llama/Meta-Llama-3.1-70B-Instruct",
    tensor_parallel_size=4,
    speculative_model="ibm-fms/llama3-70b-accelerator",
    speculative_draft_tensor_parallel_size=1, # Draft model uses only 1 GPU
)
```

## Future Roadmap: Dynamic Speculative Decoding
To solve the "High QPS slowdown" issue, vLLM is developing **Dynamic Speculative Decoding**.
- **Function:** Automatically adjusts the number of speculative tokens based on real-time system load and draft model accuracy.
- **Goal:** Shorten proposal lengths when the system is busy or accuracy is low, ensuring speculative decoding is always a net benefit.
