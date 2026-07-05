---
title: "Speculative Decoding"
created: 2026-04-18
updated: 2026-06-20
type: concept
tags:
  - inference
  - optimization
  - methodology
  - architecture
aliases: [speculative-sampling, assisted-generation, drafter-verifier, mtp-drafters]
sources:
  - raw/articles/2025-10-09_vllm-speculative-decoding-blog.md
  - raw/articles/2023-02-08_jaymody-speculative-sampling.md
  - raw/articles/crawl-2026-04-18-speculative-decoding.md
  - raw/articles/2026-04-28_fireworks-ai-open-weight-models-sed.md
  - raw/articles/2026-05-05_google-gemma-4-multi-token-prediction-drafters.md
  - raw/articles/2026-05-05_gemma-4-drafter-explained.md
  - raw/articles/modal.com--blog-spec-is-all-u-need--42b624c7.md
  - https://vllm.ai/blog/spec-decode
  - https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/
---

# Speculative Decoding

A technique to accelerate LLM inference by using a smaller "draft" model to generate candidate tokens, which are then verified in parallel by a larger "target" model. Reduces per-token latency by 2-4x for output-heavy workloads.

## How It Works

1. **Draft phase:** Small draft model generates multiple tokens sequentially (fast, low cost)
2. **Verification phase:** Target model evaluates all draft tokens in parallel using forward passes
3. **Accept/reject:** Target model accepts matching tokens, rewrites rejected ones
4. **Repeat:** Continue until end of sequence

### Key Insight

The target model can verify multiple draft tokens in a single forward pass (same computation cost as verifying one token). This creates a throughput multiplier: if the average acceptance rate is α, the speedup ≈ 1 / (1 - α).

## Two Main Approaches

### Draft-and-Verify (Traditional)
- Requires a separate smaller model (e.g., 7B draft + 70B target)
- Draft model must be trained/finetuned for the same domain
- Best acceptance rates when draft model is well-aligned with target

### Self-Speculative Decoding
- Uses early layers of the *same* model as the draft
- No additional model training needed
- Example: Llama-3 8B's first 4 layers can draft for the full 8B model
- More practical for most deployments

### Multi-Token Prediction (MTP) Drafters — Google Gemma 4 (May 2026)

Google introduced **MTP drafters** for the Gemma 4 model family, a specialized speculative decoding architecture achieving up to **3× faster inference** with zero quality degradation:

- **Shared KV Cache**: Drafters reuse the target model's activations and KV cache, eliminating redundant computation.
- **Clustering for edge models**: E2B/E4B edge models use a clustering technique in the embedder to bypass logit calculation bottlenecks.
- **Batch optimization on Apple Silicon**: Batch sizes of 4–8 unlock ~2.2× additional speedup for the 26B MoE model.
- **Supported frameworks**: LiteRT-LM, MLX, Ollama, vLLM, SGLang, Hugging Face Transformers.
- **License**: Apache 2.0.

MTP represents a production-hardened implementation of speculative decoding, deployed across Google's entire Gemma 4 family from edge (E2B) to workstation (31B). It can be seen as the "Google-flavored" answer to the draft-and-verify paradigm: a purpose-built lightweight drafter sharing compute with the target model.

See also: [[gemma-4|Google Gemma 4]], [Google Blog: Accelerating Gemma 4 with MTP](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/)

## Performance Characteristics

| Scenario | Speedup | Acceptance Rate | Best For |
|----------|---------|-----------------|----------|
| Well-matched draft | 2-4x | 70-90% | Code generation, creative writing |
| Self-speculative | 1.5-2.5x | 50-70% | General purpose, no extra model needed |
| Poor draft match | 1.1-1.3x | 20-40% | Specialized domains, domain mismatch |

## Token Economics Connection

Speculative decoding directly impacts [[concepts/token-economics]]:
- **Cost reduction:** 2-4x throughput = 50-75% fewer GPU hours per output
- **Latency improvement:** Critical for interactive applications (chat, coding assistants)
- **Memory efficiency:** No additional GPU memory needed beyond draft model

## Implementation Requirements

- **vLLM support:** Built-in speculative decoding since v0.4
- **TGI support:** Text Generation Inference supports it natively
- **Custom implementations:** Require careful tuning of draft token count and acceptance thresholds
- **Hardware considerations:** Works best on GPUs with high memory bandwidth (H100, A100)

## Limitations

- **Overhead:** If acceptance rate is too low, the draft generation overhead outweighs benefits
- **Non-determinism:** Results vary based on draft model quality and token count
- **Domain sensitivity:** Works best when draft and target models share training data distribution
- **Streaming incompatibility:** Harder to implement with streaming outputs (must wait for full draft sequence)

## Gentle Introduction

For a hands-on, code-driven introduction, [[entities/jay-mody|Jay Mody]]'s tutorial on speculative sampling ([speculative-sampling](https://jaykmody.com/blog/speculative-sampling/)) implements the full algorithm in NumPy with GPT-2 models:

- **GPT-2 1.5B** (target) / **GPT-2 124M** (draft), K=4 → **2.23x speedup** at temperature=0 (identical output)
- Algorithm is mathematically equivalent to sampling from target model alone
- Common phrases are easier for small models → big efficiency gains

## Related

- [[concepts/token-economics]] — Throughput optimization and cost reduction
- [[concepts/attention-mechanism-variants]] — Different attention mechanisms affect speculative decoding performance
- [[concepts/local-llm/model-quantization]] — Quantization can be combined with speculative decoding

## Custom Speculator Training (Fireworks AI Approach)

Fireworks AI has pioneered an approach where customers train **custom draft models (speculators)** specifically for their fine-tuned models. Unlike generic speculative decoding where a pre-existing smaller model serves as the draft, custom speculators are trained on the fine-tuned model's output distribution, achieving significantly higher token acceptance rates.

### Key Insight
A speculator trained on the same distribution as the target model achieves acceptance rates closer to 90%+ (vs. 70-90% for generic well-matched drafts). This directly translates to near-optimal speedup — approaching the theoretical maximum of 1/(1-α) where α approaches 1.

### Workflow
1. Fine-tune target model using RFT or SFT on domain-specific data
2. Train a small draft model (typically 1-5% of target params) on the same output distribution via distillation
3. Deploy speculator + target model pair on Fireworks infrastructure
4. Achieve 2-5x inference speedup over standalone target model

### Relevance for Fine-Tuned Models
For production deployments where models are fine-tuned on proprietary data, generic speculative decoding often underperforms because the draft model was trained on a different distribution. Custom speculators solve this mismatch. See [[entities/fireworks-ai]] and [[concepts/post-training/reinforcement-fine-tuning]].

## vLLM Implementation

vLLM is the most widely-deployed production serving framework for speculative decoding, supporting three methods:

### 1. Draft Model-Based
Uses a separate smaller model (e.g., Llama 68M) to propose tokens for a large model (e.g., Llama 70B).
- **Requirement:** Both models must share the same vocabulary (problematic for Llama 3's unique tokenizer)
- **Memory:** Draft model can run on fewer GPUs via `speculative_draft_tensor_parallel_size`
- **Configuration:**
  ```python
  llm = LLM(
      model="facebook/opt-6.7b",
      speculative_model="facebook/opt-125m",
      num_speculative_tokens=5,
  )
  ```

### 2. Prompt Lookup Decoding (N-gram Matching)
Matches repeating n-gram patterns between the prompt and generation — zero model overhead.
- **Best for:** Summarization, document-based Q&A (high input-output overlap)
- **Configuration:**
  ```python
  llm = LLM(
      model="facebook/opt-6.7b",
      speculative_model="[ngram]",
      num_speculative_tokens=5,
      ngram_prompt_lookup_max=4,
      ngram_prompt_lookup_min=1,
  )
  ```

### 3. Medusa / Eagle / MLPSpeculator (Multi-Head)
Adds specialized prediction heads to the target model's hidden states, predicting multiple future tokens in parallel.
- **Benefit:** No separate draft model or vocabulary compatibility needed
- **Trade-off:** Requires training additional heads per target model

### Critical Performance Insight: QPS Sensitivity

vLLM's benchmarks reveal that **speculative decoding is net-positive only at low QPS** (latency-bound workloads):

| Scenario | Dataset | Speedup |
|:---|---:|:---:|
| **Low QPS (QPS=1)** | ShareGPT (Draft Model) | **1.5x** |
| **Low QPS (QPS=1)** | CNN/DailyMail (N-gram) | **2.8x** |
| **High QPS** | Various | **1.4x – 1.8x Slowdown** |

In compute-bound (high-QPS) environments, the extra compute for drafting and verification becomes a bottleneck — making speculative decoding **slower** than not using it. This is a critical deployment consideration.

### Future: Dynamic Speculative Decoding

vLLM's upcoming **Dynamic Speculative Decoding** addresses the high-QPS regression by:
- Automatically adjusting the number of speculative tokens based on real-time system load
- Shortening proposals when the system is busy or draft accuracy is low
- Ensuring speculative decoding is always a net benefit regardless of traffic patterns
- [[concepts/local-llm/_index]] — Inference optimization techniques

## Modal's Speculative Decoding Thesis (June 2026)

In June 2026, Modal published a strong thesis on speculative decoding titled *"Speculation Is All You Need,"* arguing that speculative decoding is **the only engine optimization that matters** for high-interactivity inference. The post frames speculative decoding as uniquely "Bitter Lesson-pilled" — its speedup increases with more data and compute, unlike kernel optimizations which deliver diminishing returns.

### DFlash Architecture

Modal introduced **DFlash** (Decoding with Flash), a custom domain-specific speculator architecture. Alongside MTP (Multi-Token Prediction) and EAGLE-3, DFlash represents a modern class of speculators that **piggyback on the target model's past computations** — reusing hidden states and KV cache rather than running a fully independent draft model. This design minimizes overhead while maintaining high acceptance rates.

### Qwen 3.5 Performance Results

Modal released the SOTA DFlash speculator for **Qwen 3.5 397B-A17B** and announced new speculators for **Qwen 3.5 122B-A10B** that achieve:

- **1000+ tokens/second** at **concurrency 1** on **NVIDIA B200** GPUs
- **2-3× speedup** from custom domain-specific speculators (vs. 2-3% from kernel optimization alone)

These results were achieved at single-request latency — the regime most critical for interactive applications like chat and coding assistants.

### Bitter Lesson Framing

Modal argues speculative decoding is structurally aligned with the [Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html): as models get larger and are trained on more data, the draft model's predictions improve, acceptance rates rise, and speedups compound. Kernel-level optimizations, by contrast, deliver fixed, non-compounding gains. This makes speculative decoding the highest-leverage long-term investment in inference optimization.

### Open-Source Engine Parity

A key claim in the post is that **open-source engines (SGLang, vLLM) have closed the gap with proprietary inference engines**, largely because speculative decoding — now well-supported in both frameworks — eliminates the latency advantage that proprietary engines once held. The remaining frontier is custom speculator quality, not engine internals.

### Custom Speculator Training as "ML on Easy Mode"

Modal describes training custom speculators as **"ML on easy mode"**: the data-generating process is itself an ML model (the target LLM), so training data is effectively infinite and free. This eliminates the primary bottleneck of most ML projects (data collection/curation) and makes speculator training highly parallelizable and automatable. Combined with the 2-3× speedups from domain-specific speculators vs. negligible gains from kernel tuning, Modal argues the field is under-investing in speculative decoding.

See also: [[entities/modal-labs]], [[entities/sglang]], [[concepts/vllm]]

## Sources

-  — vLLM and speculative decoding analysis- Sebastian Raschka, "A Visual Guide to Attention Mechanisms" (Ahead of AI, 2026)
