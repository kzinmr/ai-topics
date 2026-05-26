---
title: KV Cache — Key-Value Caching in Transformer Inference
created: 2026-04-28
updated: 2026-05-11
type: concept
tags:
  - architecture
  - inference
  - optimization
  - methodology
sources:
  - raw/articles/crawl-2026-04-28-kv-cache.md
  - raw/articles/2025-02-14_dailydoseofds_kv-caching-explained.md
---

# KV Cache: Key-Value Caching in Transformer Inference

KV (Key-Value) Cache is an optimization technique that dramatically improves LLM inference efficiency in the Transformer architecture. By eliminating redundant recomputation during autoregressive generation, it improves inference speed by 5x or more.

## Problem: Computational Cost of Autoregressive Generation

LLMs generate tokens sequentially (autoregressively). At each step, the model re-computes attention over the entire input sequence, resulting in `O(n²)` complexity (n = sequence length).

Without KV Cache, when generating the 3rd token, the model recomputes the Key (K) and Value (V) vectors for the 1st and 2nd tokens.

## Solution: Eliminating Recomputation with KV Cache

Store each token's K and V vectors in a cache; when generating a new token, only compute the new token's K and V and append to the cache.

- Reduces complexity from `O(n²)` to `O(n)`
- But memory usage increases linearly (tradeoff)

## Implementation Essentials

### 1. Buffer Registration
```python
self.register_buffer("cache_k", None)
self.register_buffer("cache_v", None)
```

### 2. Forward Pass Modification
```python
if use_cache:
    if self.cache_k is None:
        self.cache_k, self.cache_v = keys_new, values_new
    else:
        self.cache_k = torch.cat([self.cache_k, keys_new], dim=1)
        self.cache_v = torch.cat([self.cache_v, values_new], dim=1)
    keys, values = self.cache_k, self.cache_v
```

### 3. Position Tracking
When using cache, track `current_pos` so the new query position correctly corresponds to the existing K/V in the cache.

### 4. Cache Reset
```python
def reset_cache(self):
    self.cache_k, self.cache_v = None, None
```

## Performance

124M parameter model, 200 token generation (Mac Mini M4 CPU):
- **Without:** ~10.30 sec
- **With:** ~2.11 sec
- **Result:** Approximately **5x speedup**

## Advanced Optimizations

| Technique | Effect |
|------|------|
| **Pre-allocation** | Pre-allocated tensors instead of `torch.cat` prevent memory fragmentation |
| **Sliding Window Cache** | Keep only the latest N tokens, prevent GPU memory exhaustion |
| **PagedAttention (vLLM)** | Manage cache with non-contiguous memory blocks, maximize memory efficiency |
| **KV Cache Quantization** | Store KV cache in lower precision, reduce memory usage |

## Important Notes

- **Why the first token is slow**: The delay in generating the first token (in ChatGPT, etc.) is due to computing the KV cache for the entire prompt. Subsequent tokens are generated almost instantly.
- **Training vs Inference:** KV Cache is only used during inference. Training processes all tokens in parallel so it is not needed.
- **Correctness:** A correct KV Cache implementation produces **exactly the same output** as a non-cached model. Any difference indicates a position encoding mismatch.
- **Memory consumption:** For Llama 3 (131k context), a full cache consumes approximately 8GB of VRAM.

### Memory Consumption Examples

| Model | KV cache per 1K tokens | 4K tokens |
|--------|------------------------------|-----------|
| Qwen 2.5 R1 1.5B | 28 MiB | 112 MiB |
| Qwen 2.5 R1 7B | 56 MiB | 224 MiB |
| Llama 3.1 8B | 128 MiB | 512 MiB |
| Mistral NeMo 12B | 160 MiB | 640 MiB |
| Llama 3.3 70B Instruct | 320 MiB | 1.25 GiB |

Reference: Avi Chawla, "KV Caching in LLMs, Explained Visually" (Feb 2025)

## Related Concepts

- [[concepts/context-engineering]] — KV Cache as foundational technology for context window optimization
- [[concepts/attention-mechanism-variants]] — Relationship between KV Cache and variants like GQA, MLA, SWA
- [[concepts/token-economics]] — Impact of KV Cache on inference costs
- [[concepts/harness-engineering/system-architecture/context-compaction]] — KV Cache memory savings via context compaction
