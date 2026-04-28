# Understanding and Coding the KV Cache in LLMs from Scratch

Source: Sebastian Raschka, PhD (via Substack/Magazine), June 17, 2025
URL: https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms
Capture date: 2026-04-28

---

KV caches are one of the most critical techniques for efficient inference in LLMs in production.

## Core Concept: Why KV Caching?

LLMs generate text autoregressively (one token at a time). Without a KV cache, the model reprocesses the entire sequence at every step, leading to redundant computations.

- **The Problem:** When generating the third token in "Time flies [fast]", the model recomputes the Key (K) and Value (V) vectors for "Time" and "flies," even though they were already computed in previous steps.
- **The Solution:** Store the K and V vectors for every token as they are generated. In subsequent steps, only compute K and V for the *new* token and retrieve the rest from the cache.

> "The idea of the KV cache is to implement a caching mechanism that stores the previously generated key and value vectors for reuse, which helps us to avoid these unnecessary recomputations."

## Implementation Details (From Scratch)

### Registering Buffers
In the `MultiHeadAttention` constructor, two buffers are added:
```python
self.register_buffer("cache_k", None)
self.register_buffer("cache_v", None)
```

### Modified Forward Pass
If `use_cache` is active, concatenate new vectors with the existing cache:
```python
if use_cache:
    if self.cache_k is None:
        self.cache_k, self.cache_v = keys_new, values_new
    else:
        self.cache_k = torch.cat([self.cache_k, keys_new], dim=1)
        self.cache_v = torch.cat([self.cache_v, values_new], dim=1)
    keys, values = self.cache_k, self.cache_v
else:
    keys, values = keys_new, values_new
```

### Position Tracking
The model must track `current_pos` to ensure new queries align correctly with the cached keys/values.

### Resetting the Cache
```python
def reset_cache(self):
    self.cache_k, self.cache_v = None, None
```

## Performance Comparison
Testing a 124M parameter model generating 200 tokens on Mac Mini (M4 CPU):
- Without KV Cache: ~10.30 seconds
- With KV Cache: ~2.11 seconds
- Result: Approximately **5x speed-up** for a relatively short sequence.

## Pros, Cons, and Optimizations
- **Efficiency:** Reduces per-step complexity from quadratic O(n²) to linear O(n).
- **Memory:** Memory usage grows linearly with sequence length.
- **Complexity:** Adds logic for buffer management and position tracking.

### Advanced Optimization Tips
1. **Pre-allocate Memory:** Instead of `torch.cat`, pre-allocate a large tensor based on `max_seq_len`.
2. **Sliding Window Cache:** Truncate the cache to keep only the last N tokens.
3. **Model Compilation:** `torch.compile` provides a significant boost, especially on CPUs.

## Key Insights for Production
- **Training vs. Inference:** KV caches are only used during inference.
- **Correctness Check:** A correctly implemented KV cache must produce the exact same output as a non-cached model.
- **Scaling:** For models like Llama 3 (131k context), pre-allocating the full cache can consume ~8GB of VRAM.
