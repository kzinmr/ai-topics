---
title: "Reame: CPU Inference Server That Gets Faster as It Runs"
url: https://github.com/swellweb/reame
source: github
date_fetched: 2026-07-12
topics: [inference, cpu-inference, model-serving, reame, infrastructure]
type: raw_article
---

# Reame: A CPU Inference Server That Gets Faster as It Runs

## GitHub Repo Info
- Stars: 64
- Description: Reame — CPU-first LLM inference server on llama.cpp: disk KV cache, self-regulating speculation, generation archive, interleaved multi-user, the Conclave. Your hardware, your realm.
- Language: C++
- Topics: ['cpu', 'gguf', 'inference', 'kv-cache', 'llama-cpp', 'llm', 'openai-api', 'speculative-decoding']
- Created: 2026-07-06T19:28:10Z
- Updated: 2026-07-12T10:13:44Z

## README (abridged)
<p align="center">
  <img src="docs/figures/logo.svg" alt="Reame" width="300">
</p>

**A lean, fully-tested LLM inference server built on [llama.cpp](https://github.com/ggml-org/llama.cpp) — designed for the hardware you already have: shared vCPUs, free tiers, 2-core ARM boxes.**

Reame is not the first inference server. It's the first one that treats cheap CPU
hardware as a first-class citizen instead of a fallback. Its thesis is simple:

> **On a CPU, never compute the same thing twice.**

## What Reame is for

Reame is built for **narrow, repetitive AI workloads over your own data, on
hardware you already pay for** — the case where the answer lives in the
context you provide, not in the model's general knowledge. That is exactly
where a small model matches a frontier one (we measured 100% accuracy on
long-context extraction with a 7B on a free 2-core ARM box) and where
Reame's memory makes request #100 cost a fraction of request #1.

| Use case | Why it fits | Suggested model |
|---|---|---|
| Document extraction & classification (RAG, invoices, tickets, scraping) | answers live in the context; prompts share prefixes → the disk cache pays | Qwen2.5 1.5B–7B |
| Batch pipelines (tag 10k products overnight, meta descriptions, email triage) | repetitive by nature → Palimpsest drafts them; €0 per token, no rate limits | Qwen2.5 1.5B–3B |
| AI features inside a thin-margin SaaS | a €5 VPS instead of a metered API keeps unit economics alive | Qwen2.5 1.5B–7B |
| Privacy-bound work (legal, medical, public sector) | data never leaves your server — full sovereignty | Qwen2.5 7B |
| Private code autocomplete (Continue.dev + OpenAI-compatible API) | line-level completion is a narrow task; code never leaves the laptop | Qwen2.5-Coder 1.5B |

**What Reame is NOT for**: a
general-purpose ChatGPT replacement (frontier reasoning and broad knowledge
need frontier parameter counts), agentic coding assistants, or creative
long-form writing at scale. If your task needs a 100B-class brain, buy one;
if it needs *your documents processed privately, forever, at zero marginal
cost* — that's a realm you can own.

- 🗂️ **Persistent shared-prefix KV cache** — prompt prefixes are snapshotted to disk
  (zstd, checksummed, LRU-budgeted) and reused **across different prompts, restarts
  and processes**. A system prompt is paid for once, by the first user.
- 📜 **Palimpsest: the server remembers what it generated** — every completed
  generation feeds an on-disk n-gram archive; future requests draft from it
  at zero cost. Domain workloads repeat themselves — let them pay off.
- 🎭 **Il Suggeritore: grammar as a draft source** — constrained decoding uses
  structure to *forbid* tokens; Reame inverts it and uses structure to
  *propose* them. List numbering, bullets and format tokens are speculated
  for free on content nobody has ever generated before.
- 🔮 **Self-regulating speculative decoding** — a small draft model *or* zero-cost
  n-gram lookup proposes tokens; the target verifies them in one batched pass.
  Reame *measures* whether speculation pays on your hardware and switches it
  off by itself when it doesn't.
- 🏛️ **The Conclave: consensus as a quality knob** — `--best-of N` generates N
  candidate answers to the same prompt in one interleaved batch (one prefill,
  cloned into the others via KV copy; every weight read shared) and elects the
  winner by majority on the final result. The moment an absolute majority
  agrees, the stragglers are stopped. Honestly measured: it squeezes roughly
  one extra correct answer per quiz out of *the model you already run* — it
  does not make a 1.5B out-reason a 3B (consensus fixes variance, not bias).
- 👥 **Interleaved multi-user serving** — N concurrent generations advance together
  inside single multi-sequence batches, sharing every read of the model weights
  (the cost that dominates memory-bound CPU decoding).
- 🌐 **OpenAI-compatible REST API** — `/v1/completions`, `/v1/chat/completions`,
  SSE streaming, sessions, bearer auth, metrics. Point any OpenAI client at it.
- ⚡ **Zero-config CLI** — `reame run qwen2.5-1.5b` downloads the model once,
  autoconfigures threads/KV/cache for the host and drops into a chat (or
  `--serve`). No config file until you want one.
- 🧪 **210 isolated test cases** — every layer is mockable and tested without a
  model; correctness of the multi-sequence, speculative and KV-clone paths is
  pinned against real models in integration tests.

![Architecture](docs/figures/architecture.svg)

## Measured, not promised

Every number below was produced by the shipped binary on the hardware named —
including the negative results that shaped the design.

| Hardware | Model | Configuration | Result |
|---|---|---|---|
| Oracle Cloud **free tier** (2× ARM, 12 GB, €0/mo) | Qwen2.5-7B Q4_K_M | plain, KV q8_0 | **3.3 tok/s** |
| Oracle Cloud free tier | TriLM 3.9B ternary TQ2_0 | 1.1 GB total RAM | **~10 tok/s** |
| Apple M3 Pro (6 threads) | Qwen2.5-1.5B Q4_K_M | plain | **52 tok/s** |
| Shared Contabo VPS (18 oversubscribed vCPUs) | 1.5B + 0.5B draft | speculative, 87% acceptance | **3.2× speedup** |
| Shared Contabo VPS | TinyLlama 1.1B | warm disk cache vs cold | **4.8× end-to-end** |
| Apple M3 Pro | Qwen2.5-1.5B | prompt-lookup on a rewrite task | **1.44×** |
| Apple M3 Pro | TinyLlama, 3 concurrent users | interleaved vs serialized | **1.6×** |
| Apple M3 Pro | Qwen2.5-1.5B, repeated request | archive speculation (palimpsest) | **2.3×** (22→51 tok/s) |
| Apple M3 Pro | Qwen2.5-1.5B, fresh list generation | form drafting (suggeritore) | **2.1×** (4.4s→2.1s) |
| Apple M3 Pro | Qwen2.5-1.5B ×5 candidates | Conclave: shared prefill + early consensus + fast nucleus | 8-question quiz wall **97s → ~50s** |
| Apple M3 Pro | Qwen2.5-1.5B `--best-of 5` vs single | 3 arithmetic quizzes, strict grading | **+0.5 to +2 correct**, ~2.5× wall (not 5×) |
| Oracle Cloud free tier | **OLMoE 7B-A1B (MoE)** vs dense 7B | same 8-needle long-context test | **100% accuracy both · 17.8 vs 3.3 tok/s (5.4×)** |
| Oracle Cloud free tier (resized: 4 OCPU, 24 GB) | OLMoE 7B-A1B | 3 threads after the free-tier max resize | **26.7 tok/s** |
| Oracle Cloud free tier (4 OCPU, 24 GB) | Qwen3-30B-A3B Q4_K_M | same 8-needle test | 8/8 — but **~335s/question vs ~35s** for OLMoE |

Three negative results that matter. A 30B-class MoE on the maxed free tier answered the same extraction questions perfectly — and ten times slower than a 7B-A1B that also scored 100%: when the answer lives in the context, extra parameters buy nothing (MoE prefill touches nearly every expert, so the 3B-active discount vanishes on document reading). Use 30B-class models for hard reasoning in background batches, not for serving. On heavily oversubscribed shared vCPUs a draft
model runs as slowly as its target, so speculation is counter-productive there —
Reame detects this and disables it at runtime. And the Conclave does **not**
close the gap to a model twice the size on hard reasoning: majority voting
corrects random slips, not systematic misunderstanding — we measured a 1.5B ×5
land between the 1.5B and a 3B, never above the 3B. Benchmarks that only show
wins are advertising; these are engineering.

## How it works

**Shared-prefix disk cache.** Prompts are split into fixed token blocks; a chain
hash keys a KV snapshot at every block boundary. A *different* prompt that shares
a prefix restores the longest cached boundary and decodes only its own tail.
Unlike GPU-resident prefix caches, snapshots live on NVMe: they survive restarts.

![Shared-prefix cache](docs/figures/prefix-cache.svg)

**Self-regulating speculation.** Classic Leviathan/Chen acceptance (the rejected
token is resampled from the residual distribution, so the output distribution is
exactly the target's), with two CPU-first twists: the draft source can be free
n-gram lookup mined from the prompt itself — ideal for extraction and rewrite
workloads — and a feedback controller adapts the draft length and turns


## HN Discussion (51 points)
[]
