---
title: "Fireworks AI"
type: entity
created: 2026-05-02
updated: 2026-07-01
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
  - raw/articles/2026-06-15_langchain_building-100x-cheaper-trace-judge-fireworks.md
  - raw/articles/2026-06-12_fireworks-ai_inference-providers-vs-api-routers.md
  - raw/articles/2026-06-25_fireworks-ai_frontier-lab-training-infrastructure-as-a-service.md
  - raw/articles/2026-06-25_fireworks-ai_frontier-open-source-worker-with-closed-source-advisor.md
  - raw/articles/2026-06-27_fireworks-ai_Cursor-Composer-2.md
  - raw/articles/2026-07-01_fireworks-ai_glm-5p2-fast.md
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

### Cursor Composer 2 Partnership (June 2026)

**[[entities/cursor-3]]** built **Composer 2** based on **Kimi 2.5**, optimized for software engineering inside Cursor. Fireworks provides the distributed RL inference infrastructure that makes these RL loops practical — Cursor runs RL across 3-4 distributed global clusters unified through Fireworks infrastructure.

**Key infrastructure capabilities:**

- **Cross-region model updates** with ~98%+ optimization in transfer size and minutes-level sync staleness
- **Stable rollout fleets** for large Mixture-of-Experts (MoE) models
- **Compressed weight synchronization** instead of full model transfers
- **Production inference reused during training** to accelerate RL runs

**Benchmark results:**

| Benchmark | Score |
|-----------|-------|
| CursorBench | 61.3 |
| Terminal-Bench | 61.7 |
| SWE-bench Multilingual | 73.7 |

**Cost efficiency:** 6-10× lower inference cost compared to comparable frontier models.

> *"We have finite engineers like everybody else. We would prefer to have engineers make training more efficient and more precise rather than spin up an inference effort."*
> — Federico Cassano (Research Lead, Cursor)

This partnership builds on an earlier Fireworks × Cursor collaboration and validates a broader shift: frontier coding performance is increasingly a function of **RL systems**, not just model scale. Cursor combined continual pre-training with large-scale RL and production feedback, with Fireworks providing the critical distributed infrastructure layer.

**Source:** [[raw/articles/2026-06-27_fireworks-ai_Cursor-Composer-2]]

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
- [[entities/cursor-3]] — Major customer; uses Fireworks inference for code completion; Composer 2 RL partnership (June 2026)
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

**Hybrid Harness — GLM 5.1 + Opus 4.7 (May 2026)**:
- 18/100 all-pass at $368 vs Opus 4.7's 14/100 at $954
- "Frontier model as callable tool, not dependency" pattern
- Advisor invoked 0.83x/task average (sparse-but-targeted)

**Hybrid Harness — GLM 5.2 + Opus 4.8 (June 2026)** — updated benchmarks with advisor pattern on new models/benchmarks:
- **SWE-bench Pro**: GLM-5.2 59% → 66% (+7 pp); Kimi-K2.6 55% → 59% (+4 pp)
- **Terminal-Bench 2.1**: GLM-5.2 76% → 80% (+4 pp); Kimi-K2.6 64% → 72% (+8 pp)
- **Legal Agent Benchmark**: GLM-5.2 12% → 16% (+4 pp); Kimi-K2.6 8% → 9% (+1 pp, within noise)
- **Cost**: GLM-5.2 + advisor matches Opus on Terminal-Bench at ~half cost ($3.50 vs $6.61); beats Opus on Legal Agent at ~40% lower cost; ~3× cheaper than Opus on SWE-bench ($6.09 vs $18.28)
- **Sparse calls**: advisor invoked ~1x/task (review-only) — plan+review tested but didn't pay off (as good or better in 5/6 experiments)
- **Same-model reviewer fails**: GLM-5.2 self-review produces no lift (58% vs 59% on SWE-bench); frontier judgment is essential
- **Open-source**: advisor released as a single file in [fireworks cookbook](https://github.com/fw-ai/cookbook/tree/main/advisor)

**Post-training** (Kimi K2.6 on Fireworks):
- SFT: 11→15/100 all-pass, mean 0.863→0.876
- RFT: 46 rollout steps, mean 0.863→0.886
- Bit-for-bit handoff from training to serving endpoint

This positions Fireworks as more than an inference provider — the platform enables the full loop from fine-tuning → evaluation → production serving on the same infrastructure.

## Frontier Training Infrastructure (June 2026)

Fireworks launched a **managed RL training service** for GLM 5.2, providing infrastructure previously available only to the largest frontier labs. The core challenge: keeping training and inference numerically identical so reinforcement learning converges.

### The Numerics Problem

RL on an LLM is a loop: the model generates responses → scored → trainer nudges weights. The loop works only if the probability the trainer thinks the model assigned to each token matches the probability the serving engine actually used to generate it. When this holds, learning signal flows. When it doesn't, the optimization targets noise.

The root cause is **non-associativity of floating-point addition**: `(a + b) + c` ≠ `a + (b + c)` at the bit level, so the order GPUs add numbers changes results. A frontier Mixture-of-Experts model like GLM 5.2 changes this order constantly due to:

- **Multi-head Latent Attention (MLA)**: reduction chunk boundaries shift with concurrent batch traffic
- **Sparse attention indexer**: selected token order varies, shifting attention sum
- **Expert matmul tiling**: GPU kernel varies by token count per expert (which depends on other requests)
- **Router near-ties**: rounding-error sized fluctuations flip expert selection
- **Cross-GPU all-reduce**: algorithm switches by message size

Without this infrastructure, a "temperature 0" model on a busy server is quietly **nondeterministic** — the same prompt co-batched with different traffic produces different results. This silently turns on-policy RL off-policy.

### Fireworks Solution

Fireworks pinned every source of nondeterminism so decisions depend only on the individual request:

1. **Fixed reduction order in attention** regardless of batch composition
2. **One settled kernel choice for expert matmuls** regardless of token counts
3. **Deterministic tie-break in the router**
4. **Single fixed cross-GPU reduction path**

### Zero-KLD Validation

The article shows validation runs on the GLM countdown reasoning task:

| Run | Train-inference KL | Clipped tokens | Reward behavior |
|-----|-------------------|----------------|-----------------|
| Without Fireworks stack | ~0.013 and drifting | ~45% | Collapses ~step 20 (0.9→0.2) |
| With Fireworks stack | 0 | 0% | Stays healthy across full 25-step run |

With importance-sampling and clipping (the industry crutch), ~45% of every batch's tokens were discarded as learning signal — a tax, not a fix. Without it, reward collapsed around step 20 as the policy chased a non-matching target.

### Performance

- **GLM trainer throughput**: ~3,500 tokens/sec per node (on par with OSS TileLang implementation)
- **Rollout generation**: ~1.8× faster on GLM 5.2 vs GLM 5.1 (~5,000 tokens/sec per node)
- **Speed penalty for determinism**: conventional open-source deterministic modes run 35-60% slower (SGLang); Fireworks pays "virtually none" of this tax
- **Supported methods**: SFT, DPO, RL through Training API
- **Co-located**: trainer and deployment on managed infrastructure for fast weight sync

**Sources:** [[raw/articles/2026-06-25_fireworks-ai_frontier-lab-training-infrastructure-as-a-service]]

### GLM 5.2 Fast (June 2026)

Fireworks launched **GLM 5.2 Fast**, a speed-optimized inference tier for GLM 5.2, on June 30, 2026. The Fast path runs 2-3x faster than the Standard path on shared serverless infrastructure without reserved GPUs, achieving a peak of 446 tok/sec on Artificial Analysis.

**Key specifications:**
- Full 1M-token context window
- Prompt caching at $0.14/1M cached input tokens (90% discount vs fresh)
- OpenAI- and Anthropic-compatible APIs
- Structured outputs (JSON-schema mode, full BNF grammar mode)
- Supported on Serverless Priority for stronger admission under congestion

**Agent loop optimization:** Average prompt length on Fireworks public endpoints is ~90k tokens — GLM 5.2 Fast is designed for coding agents with long context loops. Factory's Droid offers GLM 5.2 hosted on Fireworks.

**Pricing:** $2.80/$0.28/$8.80 per 1M tokens (input/cached/output), about 2x Standard throughput.

**Architecture:** GLM 5.2 combines an MoE MLP stack (~98% of params in experts) with DeepSeek Sparse MLA Attention with IndexShare. Expert parallelism frees HBM for KV cache; attention uses data-parallel sharding across requests. Cached prefix reuse avoids compete between prefill and decode each turn.

**Benchmark:** 77.8% on SWE-bench Verified at a fraction of closed-model token cost.

Source: raw/articles/2026-07-01_fireworks-ai_glm-5p2-fast.md

## LangChain Trace Judge Partnership (June 2026)

Fireworks AI partnered with LangChain to build a **100x cheaper trace judge** using fine-tuned open models. The collaboration addresses the challenge of efficiently mining signals from LangSmith's billions of daily production trace tokens.

### Perceived Error Detection

The joint study focused on detecting **"Perceived Error"** — instances where users correct the assistant, reject agent actions, repeat requests, or when assistants acknowledge errors. Unlike objective correctness, perceived error captures user-facing quality signals that matter for production agent improvement.

### Training Approach

- **Base model**: Qwen-3.5-35B selected for its balance of strength and cost
- **Training method**: LoRA SFT via Fireworks managed training
- **Datasets**: Two internal LangChain tracing datasets:
  - **chat-langchain**: 885 traces (707 train / 178 holdout) — Docs Q&A agent
  - **Fleet**: 911 traces (727 train / 184 holdout) — No-code agent creation tool
- **Label generation**: Model-assisted labeling with human review — panel-of-models consensus, then escalation to human annotation for disagreements
- **Key design choice**: Training used only Human and AI messages (tool calls excluded), hypothesizing that conversational signals carry most perceived-error information

### Results

| Model | chat-langchain accuracy | Fleet accuracy |
|-------|------------------------|---------------|
| Base Qwen-3.5-35B | 90.5% | 83.2% |
| Chat-langchain SFT | 96.1% | 90.8% |
| Fleet SFT | 92.7% | 91.3% |
| Claude Opus | 91.6% | 90.2% |
| GPT-5.5 | 98.9% | 89.1% |

**Key findings:**
- Fine-tuned Qwen matched or exceeded frontier model (Opus, GPT-5.5) performance
- Model trained ONLY on chat-langchain data transferred well to Fleet (unseen dataset), outperforming all frontier models
- Serving a fine-tuned open model is 10-100x cheaper than frontier alternatives
- Smaller open models (Haiku-class) were consistently outperformed by Qwen-3.5-35B out-of-the-box

### Significance

This partnership demonstrates Fireworks' thesis that **open models + fine-tuning infrastructure** can replace expensive frontier models for high-volume evaluation workloads. The perceived-error judge is positioned as a general-purpose evaluator — the signals (corrections, rejections, repetitions) are universal across applications.

**Authors:** Vivek Trivedy (@Vtrivedy10, LangChain), Jake Broekhuizen (LangChain), Harrison Chase (LangChain), Chahat Vij (Fireworks), Yi Su (Fireworks)

**Source:** [[raw/articles/2026-06-15_langchain_building-100x-cheaper-trace-judge-fireworks]]

## Inference Providers vs API Routers

Fireworks published a detailed analysis distinguishing **inference providers** (companies that secure dedicated GPU compute and serve models directly from their own infrastructure) from **API routers** (aggregation layers that forward requests to upstream providers without operating any GPU hardware of their own). The article draws a sharp line between the two categories, with direct implications for latency, data sovereignty, compliance, and reliability.

### The Core Distinction

| Category | Description | Signal |
|----------|-------------|--------|
| **Inference Providers** | Secure dedicated GPU compute; the company controlling the API endpoint also controls the hardware processing your tokens | "our clusters / our GPUs" language in docs; GPU region status pages; company-owned ASNs |
| **API Routers** | Aggregate access across multiple providers via a unified interface; forward requests upstream and never touch GPUs directly | "access 200+ models from leading providers" language; sub-processor references in DPAs; proxy-hop latency overhead |

The article uses an **Airbnb analogy**: a router is like a travel booking platform that handles reservations, but the actual service delivery (hospitality / token generation) is the responsibility of the upstream provider. Another analogy: a direct provider is farm-to-table; a router is DoorDash.

### Performance

- **Proxy hops are always additive.** Routing through an intermediary can never improve median TTFT compared to calling the same inference API endpoint directly.
- **Routers improve p95 reliability.** Services like OpenRouter maintain dozens of endpoints for popular models and can automatically reroute around overloaded or degraded endpoints, reducing tail-latency disasters.
- **Routers have zero visibility** into GPU-level decisions (KV cache configuration, batch scheduling, custom kernels) that determine inference quality.

**TL;DR:** Routers cannot improve median latency; they are a reliability layer, not a performance layer.

### Data Sovereignty — The Shadow Traffic Problem

The article highlights a structural limitation of routers:

> **A router can only bind itself.**

A zero-retention DPA with a router protects data only at the router's layer. The request still lands at an upstream provider whose policies the user has not reviewed or signed. The agreement does not follow the data.

**Shadow traffic** — duplicating live requests for model evaluation or dataset collection — is identified as a standard industry practice, especially among newer or smaller routers offering free tiers and below-cost pricing. Shadow traffic is invisible in the response and leaves no trace in application logs.

For **compliance-sensitive workloads** (HIPAA, GDPR, SOC 2, PII), the article recommends minimizing middleware layers and negotiating DPAs directly with the entity whose hardware handles the data.

### When to Use Each

| | Few models | Many models |
|---|---|---|
| **High data sensitivity** | Direct provider only. No exceptions. Negotiate DPAs directly. | Negotiate DPAs directly with each provider. |
| **Low data sensitivity** | Either works. Direct preferred at scale. | Router is ideal: one API key, multi-provider fallback, broad model access. |

Routers are a **convenience tax** — worth paying when the convenience (one API key, automatic fallback, broad model access) is genuinely valuable.

### How to Verify as a Developer

1. **Read the Terms & DPAs** — "our clusters / our GPUs" → provider; "access 200+ models from leading providers" → router. Sub-processor language in DPAs is a router tell.
2. **ASN lookup** — whois on the endpoint IP: is it a company-owned ASN or a generic cloud block?
3. **Latency fingerprinting** — a consistent 20–80ms overhead vs. a known direct provider is the proxy-hop signature.
4. **Status pages** — real providers list GPU regions and infrastructure incidents; routers only show API uptime.
5. **Response headers** — `x-served-by`, `x-upstream`, or similar may leak the actual serving provider.

### Popular Providers

| Provider | Type | Signal |
|---|---|---|
| **Fireworks AI** | Direct provider | Secured GPU clusters, FireAttention kernel, hardware SLAs |
| **Together AI** | Direct provider | Secured data centers, custom inference kernels |
| **Baseten** | Direct provider | Dedicated model replicas on secured infrastructure |
| **Groq** | Direct provider | Proprietary LPU silicon — definitionally can't be a router |
| **Cerebras** | Direct provider | Wafer-scale chips — same logic as Groq |
| **Replicate (Cloudflare)** | Direct provider | Secured GPU fleet; cold start behavior confirms real infra |
| **OpenRouter** | API Router | Multi-provider routing; model list maps to upstream APIs |
| **Not Diamond** | Gateway Router | Task-aware routing layer, no infrastructure claims |
| **Martian** | Router | Adaptive routing, same architecture |
| **LiteLLM (cloud)** | Router | OSS gateway turned managed service |

### Before You Ship

The article's central question:

> *Where does my token actually get processed?*

If answering requires reading another company's DPA to complete, you are talking to a router. That may be fine for the use case — but the distinction should be explicit before production deployment.

**Source:** [[raw/articles/2026-06-12_fireworks-ai_inference-providers-vs-api-routers]]

## Sources

- [Open Source Agents Frontier Advisors](https://fireworks.ai/blog/open-source-agents-frontier-advisors) — Fireworks AI × Harvey, June 2026
- [Software Engineering Daily, Episode 1919: Fireworks AI](https://softwareengineeringdaily.com/2026/04/28/open-weight-ai-models/) — April 28, 2026
- [Fireworks AI Platform](https://fireworks.ai)
- [Fireworks AI Series C Announcement](https://fireworks.ai/blog/series-c)
- [Sacra: Fireworks AI Revenue & Valuation](https://sacra.com/c/fireworks-ai/)
- [Tracxn: Fireworks Company Profile](https://tracxn.com/d/companies/fireworks/)
