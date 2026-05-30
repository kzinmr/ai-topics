---
title: "Together AI"
type: entity
created: 2026-05-08
updated: 2026-05-30
tags:
  - company
  - infrastructure
  - open-source
  - inference
  - hardware
aliases: ["Together Compute", "Together Computer Inc."]
sources:
  - https://www.together.ai/
  - https://www.together.ai/blog
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
- Raised $150M+ Series B; backed by Salesforce Ventures, Nvidia, and others
- Creators of FlashAttention, ThunderKittens, ATLAS, and other GPU kernel innovations for transformer efficiency
- Platform usage grew 200% year-over-year; serves AI-native companies and enterprises

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
