---
title: Mercury 3 (Inception Labs diffusion LLM)
created: 2026-10-21
updated: 2026-10-21
type: concept
tags: [diffusion, non-transformer, inference, model, benchmark]
sources:
  - raw/articles/2026-10-19_inception-mercury-3-diffusion-llm.md
  - https://www.inceptionlabs.ai/blog/introducing-mercury-3
confidence: high
---

# Mercury 3

**Mercury 3** is a diffusion-based (non-autoregressive) large language model from **Inception Labs**, released October 19, 2026. Marketed as "the most capable diffusion LLM released to date," it is the key data point that text diffusion *scales*: 40× larger than Mercury 1 yet just as fast, with benchmark quality on par with or better than frontier speed-optimized autoregressive models.

## At a glance

| Attribute | Mercury 3 |
|-----------|-----------|
| Architecture | Text diffusion (parallel/iterative decoding) |
| Speed | ~1,068 tokens/sec on NVIDIA GPUs (4–8× faster than comparable AR models) |
| Quality | On par or better than GPT-6 Luna, Claude Haiku 5.5 |
| Context | 1M tokens (up from 260K in Mercury 2.5) |
| Price | $0.20/M input, $0.70/M output (launch promo $0.10 / $0.35; cached input 90% off) |
| Scale | >40× Mercury 1; ~3× intelligence (benchmarks) vs Mercury 1 mini |

## The "diffusion scales" thesis

When Mercury 1 launched it was the first proof point that diffusion LLMs could be built for commercial applications. The open question was whether diffusion could scale to compete with autoregressive models on complex tasks. Inception's answer with Mercury 3: **the scaling laws that drove autoregressive progress hold for diffusion too** — 40× parameter growth raised benchmark intelligence ~3× while preserving speed.

## Why latency matters: the agent wedge

Diffusion decodes many tokens in parallel rather than strictly left-to-right, so per-pass latency is low. This matters most where an agent **waits on the model at every step** and small delays compound:

- **Browser-use / web agents** — on 50 live Mind2Web navigation tasks inside a production web-agent harness, Mercury 3 completed **50%**, significantly more than GPT-6.1-Sol, at the same token volume and the same number of agent steps as a frontier model, at a fraction of the per-token cost (TinyFish AI).
- **Real-time search agents** — search itself took ~80 ms so generation was the bottleneck; Mercury 3 hit median generation 0.9 s / median end-to-end 2.2 s, the best speed/quality balance among fast models (Octen AI).
- **Interactive education** — hints/answers/definitions returned in ~a second, matching or beating prior models, as a drop-in swap (General Learning / RevisionDojo).
- **Customer support** — kept responses conversational without sacrificing accuracy for regulated businesses (Lorikeet).

## Positioning

Mercury 3 competes not with the absolute-slow-but-smart frontier tier but with **speed-optimized frontier models** (GPT-6 Luna, Claude Haiku 5.5) — the tier used for latency-sensitive agent loops, voice, tutoring, and search. Its bet is that diffusion wins this tier on tokens/sec and cost while matching quality.

## Related

- [[concepts/diffusion-language-models]] — the broader architecture family this model belongs to
- [[concepts/transformer-architecture]] — the dominant autoregressive paradigm Mercury 3 competes with
- [[concepts/scaling-laws]] — scaling laws shown to hold for diffusion, per Inception
- [[concepts/llm-inference]] — serving/inference context for the 1,000+ tok/s throughput
- [[concepts/speculative-decoding]] — another family of techniques attacking generation latency
- [[concepts/token-economics]] — the $/M-token positioning against frontier speed models
