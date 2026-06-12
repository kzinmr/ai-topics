---
title: "Fireworks AI"
type: entity
created: 2026-05-02
updated: 2026-06-02
tags:
  - entity
  - company
  - open-source
  - fine-tuning
  - training
aliases:
  - Fireworks
  - Fireworks AI Inc.
sources:
  - raw/articles/2026-04-28_fireworks-ai-open-weight-models-sed.md
  - raw/articles/2026-05-10_fireworks-ai_best-llms-for-coding.md
  - raw/articles/2026-05-29_fireworks-ai_best-llm-api-providers.md
  - raw/articles/2026-06-02_fireworks-ai_Trilogy.md
  - https://fireworks.ai
  - https://softwareengineeringdaily.com/2026/04/28/open-weight-ai-models/
---

# Fireworks AI

**Fireworks AI** is an AI inference and model customization platform focused on serving **open-weight models** at production scale. Founded roughly six months before the launch of ChatGPT (circa late 2022), the company processes over **13 trillion tokens per day**, rivaling the scale of major closed-source providers like OpenAI and Google.

The platform is co-founded by **Benny Chen** (formerly of Meta's ML infrastructure team) and CEO **Lin Qiao** (formerly head of PyTorch at Meta), and differentiates through multi-hardware support (NVIDIA + AMD), custom inference kernels, and advanced Reinforcement Fine-Tuning (RFT) capabilities.

## Key Facts

| Field | Detail |
|-------|--------|
| **Tech Blog** | [fireworks.ai/blog](https://fireworks.ai/blog) |
| **Founded** | 2022 (Redwood City, CA) |
| **CEO** | Lin Qiao |
| **Total Raised** | ~$327M across 3 rounds |
| **Latest Round** | $250M Series C (Oct 2025) at $4B valuation |
| **Lead Investors** | Benchmark (Series A), Sequoia (Series B), Lightspeed/Index/Evantic (Series C) |
| **Annualized Revenue** | ~$315M (Feb 2026), up 416% YoY |
| **Customers** | 10,000+ companies (Oct 2025), including Uber, DoorDash, Shopify, Cursor, Perplexity, Notion, Sourcegraph |
| **Employees** | ~189 (Mar 2026) |
| **Acquisitions** | Hathora (Mar 2026) — real-time AI capabilities |

### Paraform Context

Fireworks AI is representative of the hypergrowth AI infrastructure companies that fuel demand on recruiting platforms like [[entities/paraform]]. With nearly 200 employees and rapid scaling from $305M to $315M+ in annualized revenue over just a few months, Fireworks competes aggressively for ML engineering and systems talent alongside peers like [[entities/together-ai]], [[entities/anyscale]], and [[entities/modal-labs]]. Paraform's recruiter marketplace connects companies of this profile with specialized recruiters, and Fireworks' growth trajectory — 10× customer growth in one year — mirrors the hiring intensity seen across the AI infrastructure sector.

## Key Differentiators

### Multi-Hardware Strategy
Fireworks has made a deliberate and expensive commitment to support both **NVIDIA** and **AMD** GPUs. This provides supply chain resilience — if one vendor's hardware is unavailable or too expensive, workloads can shift to the alternative.

### FireAttention
Custom in-house inference kernels developed to ensure **numerical consistency between training and inference**. This is especially critical for reinforcement learning pipelines, where even small numerical discrepancies between training-time and inference-time computation can cause training to fail or degrade.

### 3D FireOptimizer
An internal database and automation system that predicts optimal deployment configurations by analyzing trade-offs across three dimensions: hardware type, cache hit rate, and workload patterns. For each customer use case, it recommends the best deployment strategy.

### Custom Speculator Training
Fireworks helps customers train **custom draft models (speculators)** for their fine-tuned models. Unlike generic speculative decoding, a speculator trained on the fine-tuned model's specific output distribution achieves significantly higher token acceptance rates, directly translating to faster inference.

## Model Customization

### Reinforcement Fine-Tuning (RFT)
Fireworks offers RFT as an alternative to traditional Supervised Fine-Tuning (SFT). Instead of requiring expensive human-labeled datasets and MLE-managed quality control, RFT uses **production traces** and a **Language Model as a Judge** to automate model improvement.

#### Vercel Case Study
Vercel used Fireworks RFT to achieve **40x faster code fixing** with improved output quality. By capturing production traces of good/bad code fix attempts and using an LLM-as-Judge to score them, Vercel bootstrapped a reinforcement learning loop without requiring a dedicated team of ML engineers.

### The "Eval Protocol"
Fireworks open-sourced the **Eval Protocol**, a framework focused on authoring evaluations for reinforcement learning. The core thesis: **"Traces are all you need"** — if a product manager can articulate what a good or bad output looks like, they can use production traces to rank models and bootstrap RL without a massive MLE team. Once an organization owns its evaluation suite, it gains the power to switch between model providers without sacrificing quality.


## AI Infra Decacorn Status (May 2026)

By May 2026, Fireworks AI had reached **decacorn status** ($10B+ valuation), joining [[entities/baseten]] as one of the new AI infrastructure decacorns. [[entities/openrouter]] is reportedly on a similar trajectory. This reflects the broader market recognition of AI inference infrastructure as a critical layer in the AI stack, with Fireworks processing 13 trillion+ tokens/day at production scale.

## Enterprise Case Studies

### Trilogy (June 2026)

**Trilogy** — a portfolio operating group overseeing hundreds of companies — validated open-weight AI models for enterprise workloads using Fireworks AI. The case study demonstrates production viability of open models at enterprise scale.

**Key metrics:**
- **93.6% prompt cache hit rate** (12K cached tokens/sec) via Fireworks' prompt caching infrastructure
- **150 tokens/sec** throughput at **75K tokens/request**
- Open-weight models reached parity with proprietary models at **1/5 the cost**
- **OpenSymphony** multi-agent orchestration system deployed on Fireworks

The case study also includes comparisons to [[entities/cerebras-systems]] and [[entities/openrouter]] for enterprise inference workloads, positioning Fireworks as competitive across both throughput and cost dimensions.

## Coding Benchmarks & Model Comparison (March 2026)

Fireworks publishes a comprehensive **coding LLM benchmark roundup** comparing 11 models across the AA Coding Index, SWE-Bench Verified, pricing ($/1M tokens), and licensing. This establishes Fireworks as a benchmark aggregator alongside model provider.

### Key Benchmark Findings

| Model | AA Coding Index | SWE-Bench Verified | Context | License | Input $/1M | Output $/1M |
|-------|----------------|-------------------|---------|---------|-----------|------------|
| **GPT-5.5 (xhigh)** | 59.1 | — | 1M | Proprietary | $5.00 | $30.00 |
| **GPT-5.4 (xhigh)** | 57.3 | — | 1M | Proprietary | $2.50 | $15.00 |
| **Claude Opus 4.7 (max)** | 52.5 | 87.6% | 200K | Proprietary | $15.00 | $75.00 |
| **Claude Sonnet 4.6 (max)** | 48.1 | 84.1% | 200K | Proprietary | $3.00 | $15.00 |
| **DeepSeek V4-Pro** | 47.5 | — | 1M | MIT | $1.74 | $3.48 |
| **Kimi K2.6** | 47.1 | — | 128K | Modified MIT | $0.95 | $4.00 |
| **GLM-5.1 (Reasoning)** | 45.8 | — | 1M | MIT | $0.85 | $2.55 |
| **Qwen3.6 Plus** | 44.2 | — | 1M | Proprietary | $1.60 | $4.80 |
| **DeepSeek V4-Flash** | 38.7 | — | 1M | MIT | $0.14 | $0.28 |
| **gpt-oss-120B (high)** | 37.9 | — | 131K | Apache 2.0 | $0.15 | $0.60 |
| **Gemini 3.1 Pro Preview** | 35.6 | — | 1M | Proprietary | $2.50 | $10.00 |

### Fireworks-Specific Performance Metrics

- **Kimi K2.6**: ~85 tok/s throughput on Fireworks Serverless
- **gpt-oss-120B**: 70 tok/s on Fireworks (lowest-cost open-weight option at $0.15/$0.60 per 1M)
- **DeepSeek V4-Pro**: ~38 tok/s on DeepSeek's direct API; Fireworks throughput not yet published
- **V4-Flash**: Not yet on Fireworks catalog at time of publication

### Licensing Positioning

Fireworks emphasizes **MIT-licensed open-weight models** (DeepSeek V4-Pro, V4-Flash, GLM-5.1) as the most permissive for commercial fine-tuning and RFT. The platform supports both LoRA and RFT workflows for these models.

**Key insight**: Fireworks positions itself as the inference platform where **open-weight models become production-viable** — not just cheaper, but capable of matching closed models through post-training (RFT) on domain-specific data. The benchmark article notes that once a workload is validated, open models on Fireworks can cost "6x to ~100x less per output token" depending on model choice.

## Related Entities & Concepts

- [[entities/benny-chen]] — Co-Founder of Fireworks AI
- [[entities/lin-qiao]] — CEO, former head of PyTorch at Meta
- [[entities/openai]] — Key competitor in inference; Fireworks processes 13T+ tokens/day, rivaling closed providers
- [[entities/anthropic]] — Competitor in model serving and frontier models
- [[entities/deepseek]] — Open-weight model competitor
- [[entities/together-ai]] — Peer in open-weight inference platform space
- [[entities/anyscale]] — Peer in scalable AI inference
- [[entities/modal-labs]] — Peer in serverless AI infrastructure
- [[entities/cursor-3]] — Major customer; uses Fireworks inference for code completion
- [[entities/perplexity]] — Major customer; uses Fireworks for conversational AI search
- [[entities/meta]] — Co-founders' former employer; PyTorch lineage
- [[entities/amd]] — Hardware partner alongside NVIDIA for multi-vendor GPU strategy
- [[entities/paraform]] — Recruiting platform context; Fireworks competes for ML talent
- [[concepts/post-training/reinforcement-fine-tuning]] — RFT methodology detailed
- [[concepts/fine-tuning]] — Broader fine-tuning landscape
- [[concepts/speculative-decoding]] — Inference acceleration via draft models
- [[concepts/ai-benchmarks/legal-agent-benchmark]] — Harvey LAB benchmark joint research partner (June 2026)
- [[concepts/harness-engineering]] — GLM 5.1 + Opus 4.7 advisor hybrid harness pattern

## LAB Benchmark Joint Research (June 2026)

Fireworks AI is a research partner of [[entities/harvey|Harvey]]'s Legal Agent Benchmark (LAB). In June 2026, Fireworks published joint results demonstrating two approaches to close the open-vs-closed performance gap:

**Hybrid Harness** (GLM 5.1 worker + Claude Opus 4.7 advisor):
- 18/100 all-pass at $368 vs Opus 4.7's 14/100 at $954
- "Frontier model as callable tool, not dependency" pattern
- Advisor invoked 0.83x/task average (sparse-but-targeted)

**Post-training** (Kimi K2.6 on Fireworks):
- SFT: 11→15/100 all-pass, mean 0.863→0.876
- RFT: 46 rollout steps, mean 0.863→0.886
- Bit-for-bit handoff from training to serving endpoint

This positions Fireworks as more than an inference provider — the platform enables the full loop from fine-tuning → evaluation → production serving on the same infrastructure.

## Sources

- [Open Source Agents Frontier Advisors](https://fireworks.ai/blog/open-source-agents-frontier-advisors) — Fireworks AI × Harvey, June 2026
- [Software Engineering Daily, Episode 1919: Fireworks AI](https://softwareengineeringdaily.com/2026/04/28/open-weight-ai-models/) — April 28, 2026
- [Fireworks AI Platform](https://fireworks.ai)
- [Fireworks AI Series C Announcement](https://fireworks.ai/blog/series-c)
- [Sacra: Fireworks AI Revenue & Valuation](https://sacra.com/c/fireworks-ai/)
- [Tracxn: Fireworks Company Profile](https://tracxn.com/d/companies/fireworks/)
