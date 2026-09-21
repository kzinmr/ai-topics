---
title: "GitHub — ekzhang/openjev-sglang: Jev-compatible API endpoint based on open models (prefill-only)"
created: 2026-09-21 22:45:00
updated: 2026-09-21 22:45:00
type: raw-article
source_url: https://github.com/ekzhang/openjev-sglang
fetched: 2026-09-21
tags: [raw, x-accounts-scan]
---

# GitHub - ekzhang/openjev-sglang

A server implementing the [TypeSafe/Jev HTTP API](https://docs.typesafe.ai/api) with **Qwen3.6-35B-A3B on SGLang**.

Each container one B200 with SGLang **0.5.19's Rust frontend**, radix caching, and **breakable prefill CUDA graphs**. A separate Python API process uses FastAPI, uvloop, the Rust-backed HF tokenizer, and pooled asynchronous HTTP connections to SGLang on localhost. CUDA dependencies stay in SGLang's container; `uv sync` on your laptop installs only the API, deployment tools, and tests.

## Run on Modal

Deploy via Modal Server (`unauthenticated=True`, `routing_region="us-west"`). Autoscaling has no explicit container cap and scales to zero after five idle minutes. If SGLang exits unexpectedly, the API exits too — the Modal launcher watches the API and exits the container so Modal can replace it, rather than leaving a live HTTP process with a dead inference backend.

Cache warmups also request one unused token probability to avoid SGLang's [mixed-logprob batch crash](https://github.com/sgl-project/sglang/issues/34719). This keeps warmups and scoring requests batch-compatible without patching SGLang.

Model weights persist in the `openjev-huggingface` Modal Volume, alongside SGLang's tuning cache and Triton compilation cache. A scaled-to-zero Server returns **503** while it starts; the included smoke command retries startup responses.

Smoke test covers all three answer types, a 64-answer question, basic semantic sanity checks, and rejection of 65 answers.

## Request

`POST /v1/systemone` with `state` (chat messages or structured objects) and `questions` map. Question types:

- `noul`: binary yes/no → returns `P(yes)`
- `choice`: multiple choice with criteria → argmax + full distribution
- `score`: ordinal scale → `sum(level_index * probability)` with legend

Example request routes a support ticket through refund detection (noul), department routing (choice), and urgency scoring.

## How inference works

1. Validate schema, answer count, body size, context length, total token budget.
2. Render the native chat template **once**, with thinking disabled. Split out a common prefix and independently tokenize each question suffix.
3. Send the common prefix to `/generate` with `max_new_tokens=1`, await completion, and discard the sampled token. This warms SGLang's radix cache.
4. Concurrently send `prefix + question suffix + assistant header + "Answer:\n"` for each question. Every call again has **`max_new_tokens=1`**. Request `token_ids_logprob` for every answer label and `logprob_start_len=-1`, so there is no need to recompute prompt logprobs.
5. Renormalize the requested label logprobs with stable softmax.

This is a prefill plus first-token-readout workload: there is no generated chain of thought and no autoregressive continuation after the first token. There are **N+1 one-token calls for N questions**, including the cache-warming call. Speculative decoding is not enabled.

Qwen tokenizes `10` and `64` as multiple tokens. Answer labels are therefore `A`–`Z`, followed by verified single-token letter combinations (`AA`, `AB`, ...). All 64 labels are checked against the actual tokenizer at startup. This keeps 64-way classification an exact one-token readout instead of comparing only the first digit of a multi-token number.

Radix reuse is opportunistic, not a pinned per-request KV session. Hybrid Qwen's recurrent state, cache page boundaries, cache pressure, and concurrent requests can reduce hits. The backend uses `--mamba-radix-cache-strategy extra_buffer`. `x-openjev-prefix-tokens` exposes the requested common prefix size; `x-openjev-cached-tokens` sums the branch cache hits.

## Limits and configuration

Defaults: **64 questions**, **2–64 answers per Choice/Score**, **2 MiB JSON**, **32,768 tokens per branch**, **262,144 total submitted input tokens**, **16 simultaneous evaluations**, **64 simultaneous backend calls**. Invalid requests return 422 before inference; oversized bodies return 413; overload returns 529 with `Retry-After`.

| Variable | Default |
| --- | --- |
| `OPENJEV_MODEL` | `nvidia/Qwen3.6-35B-A3B-NVFP4` |
| `OPENJEV_SERVED_MODEL_NAME` | `Qwen/Qwen3.6-35B-A3B` |
| `OPENJEV_FRONTEND` | `rust` (`python` is an explicit fallback) |
| `OPENJEV_MAX_INPUT_TOKENS` | 32768 |
| `OPENJEV_MAX_CONCURRENT_REQUESTS` | 16 |
| `OPENJEV_TEMPERATURE` | 1.0 (applied during label normalization) |

## Author's accompanying X posts (2026-09-20/21)

- Eric Zhang (@ekzhang1, Thinking Machines Lab, ex-Modal): "Did some SFT on Qwen3.6-35B-A3B this evening, just to get it to respond better to Jev-y prompts. Cost: $5, easy 10 min training run on Tinker. +8% on GPQA diamond and +12% on MMLU-Pro. Also evaled @jaredpalmer's Kev here for comparison."
- Follow-up reply: "SGLang radix cache reuse seems to do fine in openjev-sglang. I haven't verified that SGLang is actually batching up the requests with their RadixAttention though."
