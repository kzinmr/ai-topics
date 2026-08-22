---
title: "Together AI"
type: entity
created: 2026-05-08
updated: 2026-08-22
tags:
  - company
  - infrastructure
  - open-source
  - inference
  - hardware
  - evaluation
aliases: ["Together Compute", "Together Computer Inc."]
sources:
  - https://www.together.ai/
  - https://www.together.ai/blog
  - raw/articles/together.ai--blog-announcing-our-series-c--4c861109.md
  - raw/articles/2026-07-31_together-ai_autoscaling-endpoints-llm-inference.md
  - raw/articles/together.ai--blog-a-b-test-models-in-production--0e300cb3.md
  - raw/articles/together.ai--blog-deepseek-v4-pro-0813-vs-claude-fable-5-on-deepswe-cost---246b2add.md
---

# Together AI

Together AI is a research-driven AI cloud platform offering a full stack for inference, fine-tuning, and GPU clusters — all powered by cutting-edge open-source research. It provides the AI Native Cloud: an integrated platform for serving, training, and shaping generative AI models with no vendor lock-in.

| | |
|---|---|
| **Type** | AI Infrastructure / Cloud Platform |
| **Founded** | 2022 (San Francisco, CA) |
| **Leadership** | Vipul Ved Prakash (Co-founder & CEO), Ce Zhang (Co-founder & CTO), Chris Re (Co-founder), Percy Liang (Co-founder) |
| **Key Products** | Serverless Inference, GPU Clusters, Fine-Tuning Platform, Batch Inference, AI Factory, Together Chat, FlashAttention kernel series |
| **Website** | [together.ai](https://www.together.ai) |
| **Tech Blog** | [together.ai/blog](https://www.together.ai/blog) |

## Key Facts

- Founded by Vipul Ved Prakash (serial entrepreneur), Chris Re and Percy Liang (leading Stanford AI researchers), and Ce Zhang (distributed systems expert)
- Raised **$800M** Series C (July 2026) from Aramco Ventures, NVIDIA, Vista Equity, General Catalyst, and others — on top of $150M+ Series B
- Platform usage grew 200% year-over-year; serves AI-native companies including Cognition, Decagon, Eleven Labs, Cursor, and Suno
- Secured commitments for over **500 MW of compute capacity**
- Creators of FlashAttention, ThunderKittens, ATLAS, and other GPU kernel innovations for transformer efficiency

## Products & Technology

Together AI offers serverless and dedicated model inference APIs, self-service GPU clusters (H100, B200, GB200), a fine-tuning platform for open-source models, and batch inference at 50% cost reduction. Its research arm produces breakthroughs like FlashAttention-4 (1.3x faster than cuDNN on Blackwell) and ATLAS (4x faster LLM inference). Supports all major open-source models.


### Deploy and Inference Any Model (DCI) — May 2026

Together AI launched **DCI**, a feature that lets developers deploy and inference **any model from HuggingFace** with one command. Key innovations:

- **No pre-integration needed** — Unlike traditional cloud providers, DCI doesn't require models to be pre-approved or pre-integrated
- **Automatic containerization** — Handles Docker image building, dependency resolution, and GPU provisioning automatically
- **HuggingFace-native workflow** — Developers specify a HuggingFace model repo (e.g., `meta-llama/Llama-4-Maverick`) and DCI handles the rest
- **Cost-effective** — Eliminates the need for dedicated infrastructure teams or complex deployment pipelines
- **Fast deployment** — Models are typically available within minutes, not days

This represents a significant **democratization of model deployment** — lowering the barrier from specialized MLOps teams to individual developers. It positions Together AI as the most accessible platform for custom model serving.

**Competitive context**: This is similar to what providers like [Replicate](https://replicate.com/) and [Baseten](https://baseten.co/) offer, but Together AI's integration with their existing GPU cluster infrastructure gives it a performance edge.


### Inference-Native Autoscaling (July 2026)

Together AI introduced **autoscaling endpoints for Dedicated Model Inference** that use metrics the inference engine natively understands, rather than traditional CPU/memory utilization which maps poorly to LLM workloads.

**Inference-native metrics**:
| Metric | What it measures | Why it matters |
|--------|-----------------|----------------|
| In-flight requests | Active requests being processed | Direct measure of inference queue pressure |
| Time-to-first-token (TTFT) | Latency from request to first output token | User-facing latency signal |
| GPU utilization | Compute resource consumption | Hardware efficiency indicator |
| Token throughput | Tokens generated per second | Raw inference capacity |

**Configuration**: Replica bounds (min/max), metric selection with target values, and separate scale-up/scale-down windows that control scaling eagerness vs. patience. This enables more responsive and cost-effective autoscaling for LLM deployments compared to generic Kubernetes HPA on CPU metrics.

Source: [[raw/articles/2026-07-31_together-ai_autoscaling-endpoints-llm-inference.md]]


### Endpoint-Level A/B Testing for Models (Aug 2026)

Together AI detailed how to run **A/B experiments at the endpoint level** for LLMs — the question "is the new model actually better for *our* users" (on retention, thumbs-up rate, task completion), which **shadow traffic cannot answer** (shadowing proves operational soundness — latency/errors/throughput — but discards responses so no user ever acts on them; quality questions need real end-user exposure where a slice of users gets model B and you compare outcomes).

**Why not build it in the app layer:** the common DIY approach (a feature flag or hash-mod-100 on user ID, two hardcoded model strings, a spreadsheet defining the arms) entangles the experiment with application infrastructure — routing logic ships with the app, cohort splits drift as clients cache decisions, and the branching code lingers long after the experiment "ends" because nobody's sure it's safe to delete. Together instead attaches the experiment to the **endpoint**:

- **Experiment shape**: exactly one **control** + one or more **variants**, each pointing at a deployment, each with a `percent` that must sum to 100 and controls traffic routing.
- **Routing mechanics**: the experiment **subdivides the control's share** of the base traffic split — when a request resolves to the control, it is re-sampled among the experiment arms by their percents (e.g. 95% stays control, 5% goes to the variant). Because the control is the sole entrypoint, the arm percents are **absolute traffic shares**. A control whose split weight is 0 gives the experiment nothing to subdivide, so it receives no traffic at all.

**Significance:** Pushing experimentation into the serving endpoint (rather than the app) isolates model-selection logic from application code and gives model teams production A/B harnessing comparable to what they'd otherwise wire up per-service. This is complementary to Together's endpoint autoscaling work and relevant to any team serving multiple model generations in production (cf. [[concepts/evaluation/ai-evaluation|LLM evaluation]] and online-vs-offline testing).

Source: [A/B Test Models in Production — Together AI Blog](https://www.together.ai/blog/a-b-test-models-in-production) (Aug 2026)

### DeepSWE Model Comparisons: V4 Pro 0813 vs Fable 5, Kimi K3 vs GPT-5.6 Sol (Jul–Aug 2026)

Together AI has published a series of head-to-head cost/coding/routing comparisons on the [[concepts/ai-benchmarks/deepswe-benchmark|DeepSWE]] benchmark. The Aug 2026 installment pairs **DeepSeek V4 Pro 0813** (max, $0.24/rollout) against **Claude Fable 5** (max, $21.63/rollout) — a 90x cost gap:

- Fable leads first-shot quality (69.7% vs 62.8% pass@1) but Pro erases the lead under retries (pass@4: 88.5% vs 84.1%)
- 260 solves per $100 for Pro vs 3 for Fable; no speed penalty (Fable is simply far more verbose: 115k output tokens)
- Fable's price-justifying cells: Rust (85% vs 65%) and serialization-heavy work; Pro wins concurrency and durability (58 vs 45)
- Lowest per-task correlation of any measured pairing (0.39) → union covers 94.7% of tasks; Pro-first cascade reaches **82.7% at $8.28/task** (vs Fable alone 69.7% at $21.63, and above a one-shot oracle router at 78.8%)
- Follow-up to the July 2026 Kimi K3 vs GPT-5.6 Sol comparison (85.6% cascade accuracy at 95.6% coverage)

Full results and routing analysis: [[concepts/ai-benchmarks/deepswe-benchmark|DeepSWE Benchmark page]].

Source: [DeepSeek V4 Pro 0813 vs Claude Fable 5 on DeepSWE — Together AI Blog](https://www.together.ai/blog/deepseek-v4-pro-0813-vs-claude-fable-5-on-deepswe-cost-coding-and-routing) (Aug 2026)


## World's Fastest Speech-to-Text Stack (May 2026)

Together AI achieved the **two lowest-latency speech-to-text models** ranked by Artificial Analysis: NVIDIA's Parakeet-TDT 0.6B v3 and OpenAI's Whisper Large v3. Parakeet-TDT v3 can transcribe ~20 hours of audio (the Harry Potter film franchise) in under 10 seconds.

Key optimizations that made this possible:

### 1. TensorRT Multi-Profile Engine (Encoder)
- Audio inputs range from 200ms streaming packets to 30-second continuous speech
- Single engine tuned for largest shape wastes compute on short utterances (padding overhead)
- **Multi-profile TensorRT engine**: one copy of weights in memory, right optimization profile per request
- Memory savings: modest (6GB → 5GB), but **several times faster** on small-input regime vs padded profile

### 2. Conditional CUDA Graphs (Decoder)
- Parakeet decoder loop: `predict(frame) → if token != BLANK → emit(token) → update(state)`
- The `if` branch forces **CPU-GPU round-trip** per iteration, preventing CUDA graph capture
- **Solution**: conditional CUDA graph nodes — device-side kernel evaluates condition, tells CUDA runtime which subgraph to execute
- **2–3x faster decoder**, entire loop captured as single CUDA graph launch

### 3. Zero-Copy CPU Path
- Collapsed 3–4 microservice processes into fewer processes to eliminate kernel copies and serialization/deserialization
- **Persistent Unix domain sockets** with custom minimal framing protocol instead of ZeroMQ
- **Shared memory** for large files: zero-copy data path, both processes map same physical region

### 4. epoll-Based Evented I/O (Streaming)
- One-thread-per-connection caused GIL contention explosion under hundreds of concurrent streams
- **Migrated to epoll**: single thread monitors thousands of connections, kernel returns full ready set
- **Far less scheduler pressure**, critical for streaming ASR where tail latency (p95) makes voice systems "feel slow"

### 5. gc.freeze() — The P95 Killer
- Preallocated buffer pools at startup landed in Python's oldest GC generation
- Full GC passes walked **hundreds of thousands of references**, causing ~200ms p95 spikes
- **One-line fix**: `gc.freeze()` excludes preallocated state from future GC scans
- P95 spikes eliminated, P50 improved from smoother traffic patterns

> **Key insight**: Voice latency is an **end-to-end systems problem**. GPU time, queue depth, and model execution all looked normal — the latency spike lived in the Python runtime itself.

## Related

- [[entities/modal-labs]] — competitor in GPU cloud and serverless inference
- [[entities/deepseek]] — open-source model; available for inference on Together AI
- [[entities/openai]] — Together AI offers open-source alternatives to proprietary GPT APIs
- [[entities/anthropic]] — Together AI provides infrastructure for open-source models used in similar enterprise contexts
