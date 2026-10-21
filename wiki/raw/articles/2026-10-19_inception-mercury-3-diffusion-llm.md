---
title: "Diffusion at Scale: Introducing Mercury 3 (Inception Labs)"
url: https://www.inceptionlabs.ai/blog/introducing-mercury-3
source: inceptionlabs.ai
date: 2026-10-19
fetched_at: 2026-10-21
type: raw-article
tags: [diffusion, non-transformer, inference, model, benchmark]
confidence: high
---

# Diffusion at Scale: Introducing Mercury 3 (Inception Labs, Oct 19 2026)

Source: https://www.inceptionlabs.ai/blog/introducing-mercury-3

## Summary
Mercury 3 is the most capable diffusion LLM released to date. It outperforms GPT-6 Luna and Claude Haiku 5.5 while running 4–8x faster at 1,000+ tokens per second.

## Key content
Mercury 3 is the most capable diffusion-based LLM released to date. Across a range of benchmarks, Mercury 3 outperforms GPT-6 Luna and Claude Haiku 5.5, while running 4–8x faster at 1,000+ tokens per second.

Mercury 3 demonstrates that text diffusion scales. It's more than 40x larger than Mercury 1 and is vastly more intelligent, but just as fast.

### Mercury 3 at a glance
- **Quality**: On par or better than frontier speed-optimized models like GPT-6 Luna and Claude Haiku 5.5.
- **Speed**: 1,068 tokens per second on NVIDIA GPUs.
- **Context**: 1M tokens, up from 260K for Mercury 2.5.
- **Price**: $0.20 per million input and $0.70 per million output tokens. At launch 50% off at $0.10 per 1M input and $0.35 per 1M output. Cached tokens 90% off the input price.

### Diffusion at scale thesis
When Mercury 1 launched, it was the first proof point that diffusion LLMs could be built for commercial applications. The open question was whether diffusion LLMs could scale to compete with autoregressive models on complex use cases. Mercury 3 answers: they can. Scaled more than 40x in total parameters; intelligence across standard benchmarks risen 3x from Mercury 1 (mini) to Mercury 3. **The scaling laws that drove progress in autoregressive models hold for diffusion too.**

Early-access partners use Mercury 3 for voice and chat support, real-time tutoring, data engineering, and web navigation.

### Production use cases (with partner quotes)
- **Browser Use Agents**: Agents wait on the model at every step, so small delays compound. Mercury keeps each pass fast. Benchmarked inside a production web-agent harness against frontier models on 50 live Mind2Web navigation tasks: Mercury 3 completed 50% of them, significantly more than GPT-6.1-Sol, using the same token volume and the same number of agent steps as a frontier model, at a fraction of the per-token cost. — Shuhao Zhang, Cofounder, TinyFish AI.
- **Interactive Education**: Near real-time reasoning; hints/answers/definitions come back in ~a second, quality as good or better than prior models; drop-in swap. — Michael Tong, Co-founder/CTO, General Learning (RevisionDojo).
- **Real-time search agents**: In Octen's Sense API tests, search took ~80ms; model generation was the bottleneck. Mercury 3 delivered the best speed/quality balance among fast models, median generation time 0.9s, median end-to-end response 2.2s. — Kuan Zou, Founder & CEO, Octen AI.
- **Customer support**: For regulated businesses (Lorikeet), Mercury kept responses conversational without sacrificing accuracy; beat other models on latency while performing higher on evals.

## Notes
- Inception Labs (inceptionlabs.ai) is the company behind the Mercury diffusion-LLM line; Mercury 3 is a major non-autoregressive / text-diffusion architecture release.
- Latency-sensitive agent workloads (browser use, search, tutoring, support) are the strategic wedge for diffusion LLMs vs autoregressive frontier models.
