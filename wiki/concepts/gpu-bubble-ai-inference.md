---
title: GPU Bubble (AI Inference)
created: 2026-06-30
updated: 2026-06-30
type: concept
tags: [inference, gpu, hardware, optimization, vram, performance-engineering]
sources: [raw/articles/2026-06-04_moondream_gpu-bubble.md]
---

# GPU Bubble (AI Inference)

A **GPU bubble** is a phenomenon in AI inference where the GPU sits idle waiting for the CPU to dispatch the next unit of work during autoregressive token generation. The GPU has compute capacity available, but it cannot use it because the CPU has not finished the housekeeping needed to launch the next forward pass. This idle time — the "bubble" — directly reduces throughput and increases latency in LLM serving systems.

## The Problem: Autoregressive Generation Creates CPU-GPU Round Trips

When a transformer model generates text, it produces one token at a time. Each token depends on the tokens before it — a property called **autoregressive** generation. You cannot compute token N+1 before you have token N and its associated state (KV cache, attention mask, etc.). This creates a sequential decode loop:

1. **CPU** selects which requests to process, sets up metadata, prepares input buffers
2. **CPU** launches the GPU forward pass (kernel launch)
3. **GPU** executes the forward pass — billions of matmul operations to produce logits
4. **GPU** copies results back to CPU (or into host-accessible buffers)
5. **CPU** reads the sampled token, updates decode state, decides if requests are finished
6. Return to step 1

The challenge is that one token's worth of GPU work is small (a single forward pass over the weight set), while the CPU housekeeping is a fixed cost paid on every trip. If the GPU must wait for the CPU to finish planning and launching before it can start the next token, it sits idle for part of every loop. **This idle time is the GPU bubble.**

In a blocking implementation, every step is a baton pass: CPU plans → GPU runs → CPU synchronizes and waits → CPU plans next step → GPU runs. The GPU is idle during the entire CPU planning and commit phase.

## Why the Bubble Matters

The bubble's impact grows as GPUs get faster. On a slower GPU (e.g., NVIDIA RTX 3090), the forward pass takes longer, so the CPU's bookkeeping is a smaller fraction of total step time. On a faster GPU (e.g., NVIDIA B200), the forward pass shrinks — but the CPU bookkeeping does not. The bubble becomes a larger share of each step, and more throughput is lost to idle cycles.

This means the bubble is a **scaling problem**: as GPU memory bandwidth and compute improve, the relative cost of CPU-GPU synchronization grows. It is also a **model-size problem**: smaller models have shorter forward passes, so they spend proportionally more time in the bubble.

## Moondream's Solution: Photon's Pipelined Decoding

Moondream's inference engine, **Photon**, addresses GPU bubbles through a technique called **pipelined decoding**. The core idea is to overlap CPU and GPU work: launch the GPU forward for token N+1 while the CPU is still committing the results of token N.

This is possible because the token sampled at step N does not need to leave the GPU for the next forward pass — the next forward reads it directly from GPU memory. The CPU's bookkeeping (detokenization, streaming, completion checks) can happen in the background while the next forward is already running.

Photon achieves this through three mechanisms:

### Mechanism 1: Ping-Pong Slots

To run a decode step, the GPU needs a working set of buffers: input staging, logits output, sampled token landing, and KV cache metadata. These buffers stay in use until the step is complete, so you cannot start the next step until the current one finishes — they would collide.

Photon solves this by maintaining **two DecodeSlots** and alternating between them (ping-pong style). While the GPU runs a forward in Slot A, the CPU can safely read and commit results from Slot B. Once Slot B's results are consumed, that slot is released for reuse.

Crucially, all forwards share a single GPU compute stream (the slots are not for GPU parallelism), but the device-to-host copy of results goes on a separate copy stream. This lets the copy run asynchronously while the GPU is busy with the next forward, anchored to an event so it waits only on the specific step's work — nothing queued behind it.

### Mechanism 2: Forward Now, Sample Later

Constrained decoding (required for Moondream's structured outputs like point coordinates, detect boxes, and segmentation outlines) introduces a dependency: which tokens are allowed at step N+1 depends on which token was sampled at step N. This dependency is in **sampling**, not in the forward pass.

Photon splits each scheduler tick into three phases:
- **Launch** the forward for step N+1 immediately (no dependency on the mask)
- **Commit** step N: wait for the in-flight copy and advance decode state (this determines the mask for N+1)
- **Finalize** sampling for N+1: with the state current, build the mask and sample

This "commit-before-finalize" ordering means the GPU runs the N+1 forward through steps 2 and 3, so the commit disappears from the critical path. For plain text generation (no mask), both forward and sampling can run a step ahead. One loop handles both cases.

### Mechanism 3: Zombies — Finalize Early, Release Late

What happens when a sequence hits its stop token at step N, but was already included in step N+1's forward (launched before N's commit)? You cannot un-launch GPU work. The sequence is finished but still physically present in an executing batch.

Photon calls these **zombies** and handles them with two per-sequence fields:
- `finalized`: true after the sequence hits EOS or its length cap
- `inflight_refs`: the number of in-flight steps that still reference this sequence (0, 1, or 2)

When step N commits and detects EOS, the sequence is marked finalized and its result is emitted — but it is not torn down because `inflight_refs` is still nonzero. At step N+1's commit, the sequence is already finalized, so the commit is skipped: no token is appended, no state mutates. The zombie harmlessly rides along, occupying its slot and writing KV entries nobody will read. Only when `inflight_refs` reaches 0 are its KV pages and resources released.

This refcounting approach avoids complex cancellation logic and works uniformly for both decode and prefill steps.

## Prefill Integration

Photon does not separate prefill (processing a new request's prompt) and decode into different pipelines. A prefill is just another launch in the same two-slot pipeline. This is especially important for workloads with short outputs — a request that emits three tokens spends almost all of its life in prefill, so overlapping prefill GPU work with decode CPU bookkeeping keeps the pipeline full and the GPU busy.

## Performance Gains

Moondream measured the impact of pipelined decoding on two GPU classes (NVIDIA RTX 3090 and B200) across different batch sizes. Results show:

| Configuration | Blocking (ms) | Pipelined (ms) | Observed Speedup |
|---|---|---|---|
| 3090, 1 stream | 5.44 | 5.10 | +6.5% |
| 3090, 8 streams | 7.52 | 6.97 | +7.8% |
| 3090, 32 streams | 11.74 | 10.52 | +11.6% |
| B200, 1 stream | 3.11 | 2.63 | +17.6% |
| B200, 8 streams | 4.04 | 3.30 | +21.9% |
| B200, 32 streams | 5.55 | 3.98 | +35.4% |

Key takeaways:
- **The win grows with GPU speed.** Same workload, +12% on a 3090 but +35% on a B200 at 32 streams. As GPUs get faster and models get smaller, pipelining becomes more important.
- **The "zombie tax" is real but small** and amortizes at batch. At a single stream, wasted forwards cost about 1% at typical generation lengths. At batch, the zombie is just one more row in a memory-bound step, so it costs almost nothing.
- **Pipelining enables near-realtime VLM inference.** Photon achieves approximately 33ms per token on NVIDIA B200.

## Broader Context

GPU bubbles are not unique to Moondream. This is a fundamental inference optimization pattern relevant to **all LLM serving systems**. Any system with CPU-GPU communication overhead during autoregressive decode faces this problem. The techniques Photon uses — ping-pong buffers, asynchronous copies, forward/sample splitting — are generalizable.

Related optimization areas include the [[concepts/kv-cache]], which reduces redundant computation during decode, and [[concepts/kv-cache-compression]], which addresses GPU memory pressure from growing caches. The economics of GPU efficiency directly impact [[concepts/ai-economics|AI inference economics]], as idle GPU cycles translate directly to wasted compute cost. For smaller models where GPU bubbles are proportionally larger, [[concepts/cpu-inference-llm|CPU-based inference]] may become a viable alternative by eliminating the GPU bubble entirely. The drive to optimize inference is itself a consequence of [[concepts/scaling-laws|scaling laws]] — as models grow and serving costs dominate, every percentage point of throughput matters.
