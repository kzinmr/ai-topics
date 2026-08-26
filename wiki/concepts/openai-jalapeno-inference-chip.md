---
title: "OpenAI Jalapeño Inference Chip"
created: 2026-06-25
updated: 2026-08-26
type: concept
tags:
  - openai
  - broadcom
  - hardware
  - infrastructure
  - llm-inference
  - asic
  - optimization
  - announcement
sources:
  - raw/articles/openai.com--index-openai-broadcom-jalapeno-inference-chip--f8a3b2c1.md
  - raw/articles/2026-06-25_techcrunch-openai-broadcom-jalapeno.md
  - raw/articles/2026-08-25_openai_jalapeno-first-results.md
  - raw/articles/wheresyoured.at--the-ai-haters-manifesto--64310e6c.md
  - https://news.ycombinator.com/item?id=49432879
---

# OpenAI Jalapeño Inference Chip

The Jalapeño chip is OpenAI's first custom-built inference processor, an AI accelerator co-developed with Broadcom (NASDAQ: AVGO) and Celestica. Announced on June 24, 2026, it represents OpenAI's entry into silicon design as part of a multi-generation compute platform strategy. The chip is architected from the ground up around the unique demands of large language model (LLM) inference, informed by OpenAI's deep understanding of model kernels, memory movement, networking, and serving patterns.

## Architecture and Design

Jalapeño was designed from scratch for LLM inference workloads rather than adapted from general-purpose GPU architectures. Key architectural decisions include:

- **Inference-first design**: Unlike GPUs that also serve training workloads, Jalapeño targets the specific computational and memory-access patterns of running pre-built AI models in response to user requests.
- **Reduced data movement**: The architecture minimizes data transfer overhead, balancing compute, memory, and networking to achieve realized utilization close to theoretical peak performance.
- **Broadcom silicon implementation**: Broadcom contributed chip implementation, board and rack system integration, and Tomahawk networking silicon for large-scale production.
- **Celestica manufacturing**: Celestica provided high-performance networking and scalable production systems.

The chip is designed to work flexibly with all LLMs, guided by OpenAI's insights into the inference needs of current and future AI models across the industry.

## Development Timeline

A standout achievement is the **nine-month tape-out cycle**, from design initiation to working silicon. OpenAI's own AI models assisted in accelerating the chip development process. Engineering samples are already running ML workloads in the lab at production target frequency and power, including GPT-5.3-Codex-Spark.

## Performance and Efficiency

Early testing shows that Jalapeño delivers **performance-per-watt substantially better than current state-of-the-art** alternatives. This efficiency gain is critical for inference economics, where even small reductions in per-token cost compound across billions of daily requests. The chip is particularly optimized for real-time coding models and other latency-sensitive inference workloads.

## Strategic Significance

### Reducing NVIDIA Dependency

Jalapeño is widely seen as OpenAI's move to reduce dependence on NVIDIA GPUs for inference. While more performance-intensive tasks like pre-training are expected to continue relying on NVIDIA hardware, inference represents the majority of operational costs for AI service providers.

### Full-Stack Integration

As OpenAI stated: "OpenAI is not only developing frontier models or building products on top of them; it is designing the infrastructure underneath them: chip architecture, kernels, memory systems, networking, scheduling, deployment systems, and product experience." By controlling the full stack, each layer can be optimized around the same goal — making models faster, more reliable, and more affordable.

### Multi-Generation Platform

The companies emphasized that Jalapeño is "the first AI accelerator in a multi-generation compute platform." Deployment is planned at gigawatt scale with data center partners including Microsoft, beginning in 2026.

## Leadership Statements

- **Greg Brockman** (President, OpenAI): "Jalapeño is part of our long-term full-stack infrastructure strategy to make compute more abundant, resulting in AI which is faster, more reliable, more affordable."
- **Richard Ho** (OpenAI Hardware Lead): "We optimized the architecture around the kernels, memory movement, networking, and serving patterns that matter most for frontier AI models."
- **Hock Tan** (President/CEO, Broadcom): "This is just the beginning of a multi-generation roadmap. By co-developing our industry-leading silicon directly with OpenAI, we are enabling the deployment of gigawatt scale data centers."

## First Measured Results (Aug 25, 2026)

OpenAI published its first benchmark results for Jalapeño ([openai.com/index/jalapeno-first-results](https://openai.com/index/jalapeno-first-results/), HN [514 pts](https://news.ycombinator.com/item?id=49434378) via SemiAnalysis "OpenAI Jalapeño: Better than Nvidia Blackwell"). Key numbers, measured on SemiAnalysis's public **InferenceX** benchmark at matched user experience (throughput × latency × power):

| Model | Comparison system | Jalapeño advantage |
|-------|-------------------|--------------------|
| GPT-OSS 120B | GB200 (1,200 W TDP) | ~2.7× lower TBT (0.69 vs 1.87 ms; 1,459 vs 535 tok/s/user); ~53.7× more throughput at the TBT GB200 previously achieved (22,935 vs 427 mixed tok/s/kW) |
| DeepSeek R1 670B (MXFP4) | GB300 (1,400 W TDP) | ~1.7× peak throughput (19,641 vs 11,781 mixed tok/s/kW); ~3.6× lower end-to-end latency (1.65 s vs 5.99 s); ~4.1× lower min TBT |
| Kimi K2.5 1T (MXFP4) | GB300 (1,400 W TDP) | Pareto frontier across operating points |

- **Package TDP**: Jalapeño 700 W vs GB200/GB300 1,200–1,400 W — the per-kilowatt framing is central to the claim.
- **Aggregate**: 1.5–1.9× more AI work per watt at peak throughput, 1.7–3.6× lower end-to-end latency, 2.1–4.1× higher performance on highly interactive workloads, **across all three public models** (GPT-OSS 120B, DeepSeek R1 670B, Kimi K2.5 1T) — evidence the architecture generalizes beyond OpenAI's own models.
- **Methodology note**: OpenAI evaluates "at matched user experience" (how much useful AI work per unit of power while meeting required latency) rather than raw per-chip FLOPS; it explicitly says agent workloads compound latency across sequential steps, which favors low-TBT designs.
- **Development closed-loop**: "We used AI to design the chip, and designed the chip so AI could program it" — earlier OpenAI generations helped design/bring-up the chip; current models accelerate kernel optimization and programming.
- **Roadmap**: Gen 2 "deep in development," Gen 3 "taking shape." OpenAI states it will continue widely deploying NVIDIA and other partners' accelerators for training and inference — Jalapeño is additive, not a replacement.

**Caveats**: results are OpenAI-published with comparison systems chosen by OpenAI; no independent replication as of Aug 26, 2026. The SemiAnalysis HN thread (514 pts, 326 comments) is the main skeptical cross-check — several commenters question whether the TDP-normalization methodology is favorable to a 700 W package.

## Demand-side read: the same week (Aug 24-26)

Jalapeño's efficiency story lands against a demand backdrop that is simultaneously getting more price-sensitive. Three data points:

- **ChatGPT Plus 5-hour Codex/Work caps restored** after weeks of weekly-only limits (Tibo Sottiaux, Aug 24; 9to5Mac; HN 116 pts, https://news.ycombinator.com/item?id=49432879). OpenAI is rate-limiting the product that burns its inference budget — a direct symptom of inference cost per active user.
- **GPT-5.6 Sol promotional pricing** extended to at least Nov 21 (OpenAI pricing page; HN 336 pts, https://news.ycombinator.com/item?id=49421074) — price cuts on the newest tier days after the GPT-5.6 family's restricted release.
- Ed Zitron's "AI Hater's Manifesto" (Aug 26, https://www.wheresyoured.at/the-ai-haters-manifesto/) reads the pattern: token-billed enterprise customers cut budgets; subsidized consumer plans are evidence "regular people won't pay the actual cost of AI"; and GPT-5.6 Sol "burns more than twice the amount of tokens" at the same sticker price as GPT-5.5. (Zitron's broader bubble claims — NVIDIA +17% price hikes, $1.1T in open commitments, $10T/yr revenue requirement per BCA Research — are his analysis, not established fact.)

Net: the custom-silicon bet is a supply-side answer to exactly the demand-side squeeze visible in these three moves. See [[concepts/deepseek-v4]] for the competing cost path (open weights on commodity hardware) that bypasses custom silicon entirely.

## Open Questions

- What is the absolute performance (tokens/second, latency) compared to NVIDIA H100/H200/B200 for equivalent models?
- How does Jalapeño handle the diverse model architectures that may emerge over the next hardware generation?
- What are the software ecosystem and toolchain requirements for developers targeting this chip?
- How does Broadcom's involvement compare to other custom chip partnerships (e.g., Google's TPU development)?

## Related Pages

- [[entities/openai]] — OpenAI company page
- [[concepts/ai-affordability-crisis]] — Economic pressures driving custom silicon investment
- [[entities/nvidia]] — Primary GPU supplier and competitive context
- [[concepts/kv-aware-routing]] — Complementary inference optimization technique
