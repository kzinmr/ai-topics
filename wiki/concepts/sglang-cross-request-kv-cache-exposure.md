---
title: "SGLang Cross-Request KV Cache Exposure (Cloudflare Workers AI GLM-5.3)"
created: 2026-10-27
updated: 2026-10-27
type: concept
tags:
  - sglang
  - kv-cache
  - disaggregation
  - multi-tenancy
  - isolation
  - vulnerability
  - incident-report
  - inference-engine
  - cloudflare
  - security
sources:
  - raw/articles/2026-10-26_cloudflare_kv-cache-exposure-remediation.md
confidence: high
---

# SGLang Cross-Request KV Cache Exposure

On 2026-10-26 Cloudflare disclosed a **tenant-isolation failure** in its Workers AI serving of `@cf/zai-org/glm-5.3`: between 2026-08-27 and 2026-09-09, **155 responses** returned to customers contained data from *other customers' requests* to the same model. Every affected prompt exceeded **681,280 tokens**. The root cause was a mismatch between a configured context length and the KV cache pool size, combined with an inference-engine bug that turned a rejection into a stale-cache read. ^[raw/articles/2026-10-26_cloudflare_kv-cache-exposure-remediation.md]

It is the cleanest published case study of a class of failure that disaggregated serving makes newly reachable: **KV cache page ownership is a security boundary, and inference engines do not enforce it.**

## Timeline

| Date | Event |
|---|---|
| 2026-08-27 | Bug live in production (GLM-5.3 launch window) |
| 2026-09-08 | Researcher **Gadi Evron (Knostic)** reports via Cloudflare HackerOne |
| 2026-09-09 | Reproduced next morning; model offline within **40 minutes** of incident declaration; patched engine + corrected config; service restored same day |
| 2026-10-26 | Coordinated public disclosure alongside an SGLang post |

Cloudflare's own forensics: excluding its testing and the researcher's traffic, affected requests matched ordinary long-context usage in timing and volume — **no evidence of deliberate exploitation**. No other Workers AI model was affected.

## Root cause: two overlapping faults

**Fault 1 — configuration.** GLM-5.3 was deployed with a **1,048,576-token context window**, but the KV cache pool on the prefill GPUs only fit **681,280 tokens**. Cloudflare knew about the mismatch pre-launch and expected the engine to error on any over-length prompt; long-context tests passed, so the discrepancy was dismissed. Critically, **the pool size is not a configuration value** — SGLang sizes it at startup from whatever GPU memory remains after loading weights, while the advertised context length is a separate config setting. Nothing forces the two to agree.

**Fault 2 — engine bug in disaggregated prefill/decode.** Workers AI runs SGLang with a prefill GPU pool producing the prompt's KV cache, handed by RDMA (via **Mooncake**) to a decode GPU pool. When an over-length prompt arrived:

1. The request was internally marked rejected and replaced with a **one-token placeholder**.
2. Instead of aborting and returning a client error, **prefill generated the KV cache for the placeholder** and transferred it to decode.
3. Decode received "transfer complete" and assumed prefill had **overwritten** the previous request's cache.
4. It had not. Decode then generated a response **attending over stale cache pages still holding earlier requests' data**.

## Why pages leak at all

The KV cache is a shared pool of fixed-size GPU pages, assigned on admission and released on completion. **Pages are not zeroed between requests** — the next occupant simply overwrites. This is common across inference engines and is necessary for performance, but it shifts the entire isolation guarantee onto the engine's bookkeeping of page ownership and lifetime. In disaggregated mode that bookkeeping becomes harder: ownership is simultaneously shared within a node (KV offload and token generation have different lifetimes) *and* with the remote prefill node, which holds a concurrent mutable reference to the page.

## Remediation: belt and suspenders

1. **Config fix** — matched GLM-5.3 to the GLM-5.2 config, freeing GPU memory so the prefill KV pool holds ~**2.04M tokens**, roughly 2× the 1,048,576-token context. A prompt that fits the context now always fits the pool, so the rejection path is never reached for a valid request.
2. **Engine fix** — made the rejection path itself safe, because pool size alone is fragile: any change to quantization, tensor parallelism, CUDA graph sizes, or model version silently changes the pool size. A request with a pending rejection is now retired at the disaggregation admission queue with its original error **before** any bootstrap, allocation, or KV transfer. Proposed upstream as **SGLang #38704** (also adds decode-side verification that transferred token count matches reserved count). A related fix had already landed on main as **#36988** (merged 2026-09-06, unreleased); maintainers additionally merged **#38935**, rejecting such requests even earlier.

Both changes were validated against the researcher's reproduction script and Cloudflare's own **canary-marker tests** before restoring the model.

## Design lessons for harness and inference operators

- **Never treat a derived runtime value as a bound on a configured value.** Assert `pool_size >= max_context` at startup and fail closed, rather than discovering the mismatch through behaviour.
- **Rejection paths need the same audit as success paths.** Every early-exit in a serving engine that still permits a downstream state transition is a candidate isolation bug.
- **Non-zeroed shared pages make the engine the tenant-isolation boundary.** Any component that can mark a request dead without releasing or clearing its pages breaks that boundary.
- **Long-context is the risk surface.** All 155 leaks exceeded 681,280 tokens — the extreme tail of usage is where untested paths live.
- **Canary markers are cheap insurance** for cross-tenant leakage and should be part of any prefill/decode rollout gate.

## See Also

- [[concepts/inference/sglang]] — the engine involved
- [[concepts/kv-cache]] — KV cache fundamentals
- [[concepts/kv-cache-memory-wall]] — why the pool is memory-bound
- [[concepts/abliterated-model-backdoor]] — another open-weight supply-chain security failure
