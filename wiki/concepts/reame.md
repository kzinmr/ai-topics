---
title: "Reame"
created: 2026-07-12
updated: 2026-07-12
type: concept
tags:
  - concept
  - inference
  - cpu-inference
  - infrastructure
  - developer-tooling
  - open-source
  - speculative-decoding
  - model
sources:
  - raw/articles/2026-07-12_reame-cpu-inference-server.md
  - https://github.com/swellweb/reame
---

# Reame

A lean, fully-tested **CPU-first LLM inference server** built on [[concepts/llama-cpp]] (C++, 64 stars). Reame treats cheap CPU hardware — shared vCPUs, free-tier cloud instances, 2-core ARM boxes — as a first-class citizen rather than a fallback from GPU inference. Its central thesis: **"On a CPU, never compute the same thing twice."**

## Problem Statement

Most inference servers ([[concepts/vllm]], [[concepts/ollama]]) were designed for GPU environments and treat CPU as a degraded fallback path. Reame inverts this assumption: it is built from the ground up for CPU workloads where memory bandwidth, not compute throughput, is the bottleneck. The server targets **narrow, repetitive AI workloads over user-owned data** — document extraction, RAG pipelines, batch classification, code autocomplete — where answers live in the provided context rather than the model's general knowledge. In these scenarios, a 7B model can achieve 100% accuracy matching a frontier model, and Reame's caching makes request #100 cost a fraction of request #1.

What Reame is explicitly **not**: a general-purpose ChatGPT replacement, agentic coding assistant, or creative long-form writing engine. If a task requires 100B-class reasoning, use a frontier model; if it requires processing your own documents privately at zero marginal cost, Reame is the tool.

## Architecture

Reame is built on **llama.cpp** as its inference backend, inheriting its broad model support (GGUF format) and CPU-optimized kernels. On top of this, Reame layers several CPU-first innovations:

- **Disk-resident KV cache**: Prompt prefixes are split into fixed token blocks, with a chain hash keying KV snapshots at every block boundary. These snapshots are persisted to disk (zstd-compressed, checksummed, LRU-budgeted) and survive process restarts. A system prompt is paid for once by the first user; subsequent requests restore the longest cached boundary and decode only the tail. On NVMe drives, this yields up to 4.8× end-to-end speedup for warm-cache requests.

- **Self-regulating speculative decoding**: Uses classic Leviathan/Chen acceptance — the rejected token is resampled from the residual distribution, so output is exactly the target model's distribution. Reame adds two CPU-first twists: the draft source can be a zero-cost n-gram lookup mined from the prompt itself (ideal for extraction/rewrite workloads), and a feedback controller continuously measures whether speculation pays on the current hardware, disabling it automatically when it does not (e.g., on heavily oversubscribed vCPUs where the draft model runs as slowly as the target).

- **Interleaved multi-user serving**: N concurrent generations advance together inside single multi-sequence batches, sharing every read of the model weights — the dominant cost in memory-bound CPU decoding.

For more on the underlying techniques, see [[concepts/speculative-decoding]] and [[concepts/kv-cache]].

## Key Features

### Palimpsest (Generation Archive)
Every completed generation is recorded to an on-disk n-gram archive. Future requests draft from this archive at zero computational cost. Domain workloads that repeat themselves — document extraction, batch pipelines — progressively accelerate as the archive grows. Measured: 2.3× speedup on repeated requests (22 → 51 tok/s on Apple M3 Pro with Qwen2.5-1.5B).

### Il Suggeritore (Grammar as Draft Source)
Constrained decoding traditionally uses structure to *forbid* tokens; Reame inverts this by using structure to *propose* them. List numbering, bullet points, and format tokens are speculated for free on content that has never been generated before. Measured: 2.1× speedup on fresh list generation (4.4s → 2.1s).

### The Conclave (Consensus-Based Quality)
`--best-of N` generates N candidate answers to the same prompt in a single interleaved batch — one prefill cloned via KV-copy into N sequences, with every weight read shared across all candidates. The winner is elected by majority voting on the final result; stragglers stop the moment an absolute majority agrees. Honest benchmark: a 1.5B model ×5 candidates lands between the 1.5B and a 3B in accuracy — never above the 3B. Consensus fixes variance, not bias.

### OpenAI-Compatible API
Full support for `/v1/completions`, `/v1/chat/completions`, SSE streaming, sessions, bearer auth, and Prometheus metrics. Any OpenAI client can point at Reame with no changes.

### Zero-Config CLI
`reame run qwen2.5-1.5b` downloads the model once, autoconfigures threads/KV/cache for the host, and drops into a chat (or `--serve`). No configuration file is required until the user wants one.

## Use Cases

| Use Case | Why It Fits | Suggested Model |
|---|---|---|
| Document extraction & classification (RAG, invoices, tickets) | Answers live in context; prompts share prefixes → disk cache pays | Qwen2.5 1.5B–7B |
| Batch pipelines (product tagging, meta descriptions, email triage) | Repetitive by nature → Palimpsest accelerates; zero per-token cost | Qwen2.5 1.5B–3B |
| AI features in thin-margin SaaS | A €5 VPS instead of metered API keeps unit economics viable | Qwen2.5 1.5B–7B |
| Privacy-bound work (legal, medical, public sector) | Data never leaves the server — full sovereignty | Qwen2.5 7B |
| Private code autocomplete (Continue.dev) | Line-level completion is a narrow task; code stays on-device | Qwen2.5-Coder 1.5B |

## Performance

All numbers below were produced by the shipped binary on the named hardware, including the negative results that shaped the design.

| Hardware | Model | Configuration | Result |
|---|---|---|---|
| Oracle Cloud free tier (2× ARM, 12 GB) | Qwen2.5-7B Q4_K_M | Plain, KV q8_0 | **3.3 tok/s** |
| Oracle Cloud free tier | TriLM 3.9B ternary TQ2_0 | 1.1 GB total RAM | **~10 tok/s** |
| Apple M3 Pro (6 threads) | Qwen2.5-1.5B Q4_K_M | Plain | **52 tok/s** |
| Shared Contabo VPS (18 oversubscribed vCPUs) | 1.5B + 0.5B draft | Speculative, 87% acceptance | **3.2× speedup** |
| Shared Contabo VPS | TinyLlama 1.1B | Warm disk cache vs cold | **4.8× end-to-end** |
| Apple M3 Pro | Qwen2.5-1.5B | Repeated request (Palimpsest) | **2.3×** (22→51 tok/s) |
| Apple M3 Pro | Qwen2.5-1.5B | Fresh list generation (Suggeritore) | **2.1×** (4.4s→2.1s) |
| Oracle Cloud free tier | OLMoE 7B-A1B (MoE) | 8-needle long-context test | **100% accuracy, 17.8 tok/s** |
| Oracle Cloud free tier (max resize: 4 OCPU, 24 GB) | OLMoE 7B-A1B | 3 threads | **26.7 tok/s** |

**Key negative results**: A 30B-class MoE on the maxed free tier answered extraction questions perfectly but was 10× slower than a 7B-A1B that also scored 100% — when answers live in context, extra parameters buy nothing. On heavily oversubscribed shared vCPUs, speculation is counter-productive; Reame detects this and disables it at runtime. The Conclave never closes the gap to a model twice the size on hard reasoning.

## Comparison to Other Inference Servers

| Feature | Reame | [[concepts/vllm]] | llama.cpp server | [[concepts/ollama]] |
|---|---|---|---|---|
| **Primary target** | CPU (first-class) | GPU (CUDA) | CPU/GPU (general) | CPU/GPU (consumer) |
| **Disk KV cache** | Yes (survives restarts) | No (GPU-resident only) | Experimental | No |
| **Generation archive** | Yes (Palimpsest) | No | No | No |
| **Self-regulating speculation** | Yes (auto-disables) | No | Manual draft model | No |
| **Consensus decoding** | Yes (Conclave) | No | No | No |
| **Interleaved multi-user** | Yes | Yes (continuous batching) | Limited | No |
| **Zero-config** | Yes (`reame run`) | No | No | Yes (`ollama run`) |
| **OpenAI API** | Yes | Yes | Yes | Yes |
| **Test suite** | 210 isolated test cases | Extensive | Limited | Limited |

For background on CPU-first inference, see [[concepts/cpu-inference-llm]].

## Limitations

- **Not for frontier reasoning**: Small models (1.5B–7B) cannot match 100B+ models on complex reasoning, broad knowledge, or creative generation.
- **MoE prefill bottleneck**: Mixture-of-Experts models touch nearly every expert during prefill, negating the active-parameter efficiency advantage on document reading workloads.
- **Speculation fails on oversubscribed CPUs**: When the draft model runs at the same speed as the target, speculation adds overhead. Reame detects this but cannot fix it.
- **Conclave caps at variance reduction**: Majority voting corrects random slips, not systematic misunderstanding. A 1.5B ×5 never exceeds a single 3B.
- **Narrow workload bias**: The caching architecture rewards repetitive, prefix-sharing workloads. One-shot, highly diverse prompts see little benefit.
- **Early-stage project**: 64 stars, created July 2026. Production deployment should be evaluated carefully against established alternatives.

## Related Pages

- [[concepts/inference]] — General overview of LLM inference approaches
- [[concepts/llama-cpp]] — The C++ inference engine Reame is built on
- [[concepts/cpu-inference-llm]] — Broader landscape of CPU-first LLM inference
- [[concepts/speculative-decoding]] — The technique behind Reame's self-regulating speculation
- [[concepts/kv-cache]] — Key-Value cache mechanisms in transformer inference
- [[concepts/vllm]] — GPU-first inference server for comparison
- [[concepts/ollama]] — Consumer-focused local inference tool
