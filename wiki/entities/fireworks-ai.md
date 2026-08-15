---
title: "Fireworks AI"
type: entity
created: 2026-05-02
updated: 2026-08-15
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
  - raw/articles/2026-05-10_fireworks-ai_kimi-qkclip.md
  - raw/articles/2026-05-29_fireworks-ai_best-llm-api-providers.md
  - raw/articles/2026-06-02_fireworks-ai_Trilogy.md
  - raw/articles/2026-06-15_langchain_building-100x-cheaper-trace-judge-fireworks.md
  - raw/articles/2026-06-12_fireworks-ai_inference-providers-vs-api-routers.md
  - raw/articles/2026-06-25_fireworks-ai_frontier-lab-training-infrastructure-as-a-service.md
  - raw/articles/2026-06-25_fireworks-ai_frontier-open-source-worker-with-closed-source-advisor.md
  - raw/articles/2026-06-27_fireworks-ai_Cursor-Composer-2.md
  - raw/articles/2026-07-01_fireworks-ai_glm-5p2-fast.md
  - raw/articles/2026-07-08_fireworks-ai_glm5p2-fast-an-engineering-productivity-story.md
  - raw/articles/2026-07-10_fireworks-ai_gumloop.md
  - raw/articles/2026-07-11_fireworks-ai_kernel-optimization-for-minimax-m3-on-nvidia-blackwell.md
  - raw/articles/2026-07-10_fireworks-ai_Open-frontier-and-yours-LangChain-Deep-Agents-on-NVIDIA.md
  - raw/articles/2026-07-17_fireworks-ai_series-d-announcement.md
  - raw/articles/2026-07-28_fireworks-ai_fireworks-nexus.md
  - raw/articles/2026-07-28_fireworks-ai_K3-LoRA-Training.md
  - raw/articles/2026-07-31_fireworks-ai_fine-tuning-your-own-embeddings-model.md
  - raw/articles/2026-07-31_fireworks-ai_three-tests-to-run-before-you-switch-from-LoRa-to-FullFT.md
  - raw/articles/2026-05-10_fireworks-ai_best-open-source-llms.md
  - raw/articles/2026-07-27_fireworks-ai_best-open-source-llms-may-2026.md
  - raw/articles/2026-05-21_fireworks-ai_agent-execution-tax.md
  - raw/articles/2026-05-10_fireworks-ai_constrained-generation-with-reasoning.md
  - raw/articles/2026-08-08_fireworks-ai_voyage-ai-models-now-on-fireworks.md
  - raw/articles/2026-08-12_fireworks-ai_meta-muse-glimmer.md
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

### MLA / QK-Clip Technical Explainer (July 2025)

Fireworks published one of the most widely-cited deep-dives on **Multi-Head Latent Attention (MLA)** training/inference asymmetry and **QK-Clip**, the fix introduced by Kimi (Moonshot AI) — starting from a comment exchange on Su Jianlin's kexue.fm blog. The explainer documents why keys are fully materialized during training (permitting RMSNorm) but not during decoding, and how QK-Clip clips Wq/Wk weights at training time when max logits exceed a threshold (root cause: Muon optimizer without weight decay → "MaxLogit explosions"), avoiding runtime normalization that would break MLA inference. Includes an animated visualization of the training vs decoding paths. See [[concepts/attention-mechanism-variants]].

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

### Gumloop — Open-Weight Models for Production Agents (July 2026)

**[[entities/gumloop]]** is an AI workflow automation platform that helps teams build AI-powered agents for complex business tasks. As adoption grew, inference costs became a top concern — every additional workflow meant more model calls and higher inference spend.

Gumloop tested open-weight models internally with their company-wide assistant agent, which employees use to access company data and answer questions. Previous attempts to move this agent from frontier models to open-weight alternatives had failed — employees noticed the difference immediately, and the team reverted to Opus.

**That changed with GLM-5.2 on Fireworks AI.** When Gumloop moved its internal agent from Opus 4.8 to GLM-5.2, nobody noticed the difference. The outputs remained consistent, giving the team confidence to make open-weight models a recommended production option.

> *"When we moved this agent from Opus 4.8 to GLM-5.2, nobody noticed a difference in the experience. The outputs were consistent with what we expected, which gave us the confidence to make GLM-5.2 a recommended model option."*
> — Gonzalo Soto Mallqui, Chief Product Officer, Gumloop

**Key results:**
- **72% cost savings** after moving the internal production agent from Opus 4.8 to GLM-5.2
- **7x growth** in agent chats running on open-weight models in three weeks
- **Reliability** was the deciding factor for choosing Fireworks over other inference providers
- Open-weight models became a **first-class option** in Gumloop's platform for extraction, classification, routing, summarization, and workflow automation

After optimizing its agent harness for open-weight models and partnering with Fireworks for inference, Gumloop validated a broader shift: open-weight models have reached production parity with frontier models for agent workloads, at radically lower cost.

**Source:** [[raw/articles/2026-07-10_fireworks-ai_gumloop]]

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

### GLM 5.2 Fast — GPU Scheduler Reclaim (July 2026)

Fireworks engineer **Rif Rafiq** documented a case study of shipping a GPU scheduler **reclaim capability** using GLM 5.2 Fast via FireConnect on Claude Code. The project delivered what would normally be an **engineer-month** of work in **4 days at $218 inference cost**.

**Workflow breakdown:**
- **Day 1 (0.5 day)**: Design doc — architecture review, GC complexity analysis, KV-aware paging design
- **Day 2 (0.5 day)**: Implementation plan — granular CLs, test strategy, safety rollout
- **Days 3-4 (1.5 days)**: Implementation — 4 PRs, ~3,000 lines, 16 unit tests + 18 integration tests

**Key engineering choices:**
- **CL size discipline**: 4 granular PRs vs one monolith (defeats 80% of agent failure modes per author)
- **Playground-first test pattern**: Unit tests first via CLI, then integrated into full harness
- **Design doc in committed Markdown**: Enabled Claude Code to reference the design throughout implementation without losing context
- **KV-aware preemption**: Thread-level memory accounting before GPU memory preemption — ensures the victim task's KV cache is fully written back before eviction

**Observations:**
- GLM 5.2 Fast at $2.80/$8.80 per 1M tokens (input/output) made 50+ agent iterations economical at $218 total
- Author noted that **greenfield projects** (new features like this) have higher agent success rate than rewrites (distinct from [[entities/eli-thegreenplace-net]]'s literature review about rewrite vs greenfield)
- Go as an agent language: 99% reading / 1% writing — the language's simplicity means agents spend more time reasoning about the problem than parsing syntax

**Source:** [[raw/articles/2026-07-08_fireworks-ai_glm5p2-fast-an-engineering-productivity-story]]

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

### Open Source LLM Roundup Series (Jan & May 2026)

Fireworks also maintains a recurring **"Best Open Source LLMs" roundup** series (distinct from the coding-LLM benchmark article above), reviewing 7 leading open-weight models per edition. The January 2026 edition and the May 2026 edition (published 5/19/2026) cover the same seven-model field — Kimi K2.5, Kimi K2 Thinking, Qwen3 VL 235B A22B, GLM-5, DeepSeek v3.2, Google Gemma 3, MiniMax-M2.5 — all offered on Fireworks serverless. The May edition carries the fuller comparison data:

- **MoE dominance**: 6 of 7 models are Mixture-of-Experts activating only 10B-40B parameters per token (Kimi K2.5/K2 Thinking: 1T total / 32B active; DeepSeek v3.2: 671B / 37B; GLM-5: 744B / 40B)
- **Benchmark leaders**: DeepSeek v3.2 tops GSM8K at 96.0%; MiniMax-M2.5 tops SWE-Bench Verified at 80.2% (Claude Opus 4.6 level); Qwen3 VL 235B tops MMLU at 87.1%; GLM-5 leads GPQA-Diamond at 86.0%
- **Licensing nuance**: Kimi K2.5's Modified MIT license adds a commercial attribution clause for hyperscale usage (commonly cited as >100M MAU or >$20M monthly revenue); Apache 2.0 (Qwen3 VL) and MIT (DeepSeek v3.2, GLM-5) impose minimal restrictions
- **Context engineering**: DeepSeek's Sparse Attention and GLM-5's 128K output limit represent distinct approaches to maintaining coherence across long sequences

Sources: [[raw/articles/2026-05-10_fireworks-ai_best-open-source-llms.md]], [[raw/articles/2026-07-27_fireworks-ai_best-open-source-llms-may-2026.md]]

## Agent Execution Tax Benchmark (May 2026)

Fireworks published a browser-agent benchmark report introducing the **Agent Execution Tax** — the ratio of wasted inference (parse retries on malformed structured output) to productive inference in multi-step agent loops. 720 WebVoyager runs across 4 LLMs (GLM-5, MiniMax M2.5, Kimi K2.5 on Fireworks serverless; Gemini 2.5 Flash via OpenRouter as baseline).

- **Headline finding**: agents fail on execution, not intelligence — Gemini 2.5 Flash showed a **22.9% execution tax** (18.6% parse retry rate, 45.0% task accuracy → 34.7% reliability-adjusted accuracy), while all three Fireworks-served models combined retried only 18 times across 2,564 calls (0.7%).
- **Procurement implication**: token pricing misleads — MiniMax M2.5 was **2.3× cheaper per successful task** than Gemini ($0.062 vs $0.142) while 12.5 pp more accurate; Kimi K2.5 delivered zero execution tax and the fastest p50 latency (2.1s).
- **Serving-layer attribution**: tight p95/p50 latency spreads (1.8–2.3×) across heterogeneous MoE architectures and clean retry recovery were attributed to the Fireworks serving stack, not model behavior — supporting the platform's structured-output reliability positioning.

Full details in [[concepts/harness-engineering/agent-execution-tax]].

## Constrained Generation / Reasoning JSON Mode (Feb 2025)

Fireworks documented constrained generation for structured extraction in reasoning models (DeepSeek R1) in an early-2025 technical article, positioning the platform's **Reasoning JSON Mode** as a differentiator for reasoning-model deployments.

- **Mechanism**: constrained decoding restricts next-token predictions to tokens that do not violate the required output structure; in structured tasks it can also *skip* boilerplate token steps, accelerating generation by simplifying the prediction space.
- **R1 pattern**: DeepSeek R1 emits free-form reasoning inside `<think>`/`</think>` tokens followed by a JSON output; Fireworks applies the **JSON schema constraint only to the JSON section after the `<think>` tags**, keeping the reasoning chain unconstrained while guaranteeing schema-valid final output. Callers parse the reasoning section separately.
- **API surface**: OpenAI-compatible `response_format={"type": "json_object", "schema": <Pydantic model_json_schema()>}` with `accounts/fireworks/models/deepseek-r1`.
- **Demonstrated use cases**: structured Q&A (Pydantic `QAResult`), healthcare records (clinical documentation with reasoning), computer system specifications.
- **Positioning**: complements the later Agent Execution Tax work — both argue structured-output reliability is a serving-layer property Fireworks optimizes for.

Sources: [[raw/articles/2026-05-10_fireworks-ai_constrained-generation-with-reasoning.md]]

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

## Meta Muse Glimmer on Fireworks (August 2026)

Fireworks launched **[[entities/muse-glimmer|Meta Muse Glimmer]]** (Meta's 30B open agentic model, Apache 2.0) on **serverless and on-demand** deployments on Aug 10, 2026 — **deliberately a day later than other providers**.

**Why the day-later launch**: Fireworks took the extra day "on purpose" to get the serving right — correcting the model's shipped generation config and wiring **reasoning-effort control end-to-end** (`Reasoning strength: <value>` in the system prompt, low/medium/high/xhigh), so users get the exact performance/control/reliability expected from day one.

**Agent-traffic positioning**: The launch post explicitly targets "always-on agents" — Fireworks autoscales for bursty agent workloads (spike unpredictably, no peak provisioning). Muse Glimmer's architecture (sliding-window attention over 2,048 tokens on most layers, full global attention every fourth layer, 2 KV heads) keeps the KV cache small, making long-context agent sessions economical to serve at high concurrency — including 100K-token accumulated tool output.

**Key data points**:
- Meta-recommended sampling: temperature = 1.0, top_p = 0.95, top_k = 64
- Benchmark leads vs Gemma 4 31B / Qwen 3.6 27B at high reasoning effort: MCP Atlas 75.5, DeepSearch QA 74.6, SWE-Bench Pro 51.2 (Meta-reported)
- DFlash speculative decoding supported for lower latency
- Path symmetry: prototype on the quantized workstation build, deploy the same weights on Fireworks at production concurrency

Source: raw/articles/2026-08-12_fireworks-ai_meta-muse-glimmer.md

## MiniMax M3 Sparse Attention on Blackwell (July 2026)

Fireworks' Performance team built a custom kernel for MiniMax M3 sparse attention on NVIDIA Blackwell (SM100), using a **KV-stationary execution path** that outperforms both the query-stationary baseline (FlashInfer) and MiniMax's open-source MSA kernel.

**Key results** (single B200, fp8):
- Kernel throughput: ~980 TFLOP/s at ~4.1 TB/s HBM bandwidth
- **1.9–2.4×** speedup over FlashInfer (Q-outer baseline)
- **~1.6×** improvement over open-source MSA
- Full module: 1.18–1.43× over FlashInfer, 1.32–1.41× over MSA

**Architecture**: KV-outer kernel with warp specialization (load/MMA/softmax/output warp groups), contiguous partial-O writes with combine-kernel gathered reads, 3-warp cp.async gathered query loads, load-balanced split-Q scheduling with persistent kernel, D2H elimination via fixed per-request shapes, and C++ AOT dispatch.

**Optimizations:**
- Replaced scattered partial-O writes with contiguous TMA bulk writes (deferred to combine kernel)
- Deleted the softmax→store sync dependency (O never rescaled in KV-outer)
- Fixed per-request tensor shapes to eliminate D2H sync per layer
- C++ AOT dispatch removes Python host-side launch overhead

The kernel was written independently before MSA was public (separate implementation of the same MiniMax KV-outer idea), developed with Claude Code and Cursor, and built on the FlashAttention4 CuTe-DSL SM100 kernel.

[[concepts/inference-optimization]] | [[concepts/sparse-attention]] | [[entities/nvidia]] | [[concepts/cuda-kernels]]

**Source:** [[raw/articles/2026-07-11_fireworks-ai_kernel-optimization-for-minimax-m3-on-nvidia-blackwell]]

## LangChain Deep Agents on Nemotron 3 Ultra (July 2026)

Fireworks partnered with LangChain to tune the **Deep Agents** harness for **NVIDIA Nemotron 3 Ultra** (550B), achieving benchmark-leading agent performance among open models at **~10× lower cost** than closed alternatives.

**Key points:**
- LangChain tuned prompts, tools, and middleware (no model retraining) — the result leads all open models on agent performance
- **Cost per task** is the key metric: agent tasks can consume 5–30× (up to 1,000×) the tokens of single-shot equivalents
- Nemotron 3 Ultra runs with day-zero support on Fireworks' Blackwell/B200 inference stack with FireAttention kernels (up to 4× higher throughput)
- **Post-training path**: Users can fine-tune Nemotron 3 Ultra (SFT/DPO with LoRA or full-parameter) on the same Fireworks platform that serves it — the trained model is the deployed model
- Combined with **NVIDIA OpenShell** as the secure agent runtime, forms a complete open stack: open model + open harness + open runtime

**Enterprise adoption**: Teams building agents for coding, deep research, and complex domain workflows are already evaluating. Model is live on Fireworks.

[[concepts/ai-agent-engineering]] | [[concepts/harness-engineering]] | [[entities/nvidia]] | [[entities/langchain]]

**Source:** [[raw/articles/2026-07-10_fireworks-ai_Open-frontier-and-yours-LangChain-Deep-Agents-on-NVIDIA]]

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

## Series D — $1.505B at $17.5B Valuation (July 2026)

In July 2026, Fireworks AI raised **$1.505 billion** in Series D funding at a **$17.5 billion valuation**, led by **Atreides Management**, **Index Ventures**, and **TCV**, with participation from Evantic Capital, Lightspeed Venture Partners, **[[entities/nvidia|Nvidia]]**, 20VC, Bessemer Venture Partners, Menlo Ventures, and others. The round brings Fireworks' total raised to over $1.8B.

The company has surpassed **$1 billion in annualized revenue run rate** (ARR) and serves **more than 40 trillion tokens every day** — more than triple the throughput reported in May 2026. Critically, **more than 95% of those tokens** come from models specialized on customers' proprietary data rather than general-purpose base models, validating Fireworks' thesis that enterprise AI value lies in customization over raw frontier intelligence.

> *"Companies are no longer renting general intelligence. They're building their own."*

The funding will be used to expand compute infrastructure and grow the engineering team, further cementing Fireworks' position as the leading inference infrastructure platform for [[concepts/post-training/reinforcement-fine-tuning|customized open-weight models]] and [[concepts/ai-agent-engineering|production agent workloads]].

**Source:** [[raw/articles/2026-07-17_fireworks-ai_series-d-announcement]]

## Fireworks Nexus

**Fireworks Nexus** is Fireworks' enterprise cost optimization platform that connects AI tools to a managed layer of open-weight models with centralized controls, enabling organizations to optimize inference spend without sacrificing quality.

### Components

**Enterprise Controls & Cost Observability:** Centralized budget, ROI, and policy management across all AI tool usage. Endpoints are hosted exclusively in the US with zero data retention, and the platform runs across 20 global data centers.

**FireConnect:** An open-source (Apache 2.0) one-line install tool that maps models based on harness configurations. Supports Claude Code, Codex, and OpenCode, functioning through the API-compatible Fireworks Serverless endpoint.

**FireRouter:** A custom trained model that scores requests by difficulty. Routine tasks are routed to open-weight models, while difficult tasks pass through to the existing provider (Anthropic key). Currently routes between Opus 5 and GLM 5.2, or K3 and GLM 5.2 for pure open-weight deployments. Delivers **3–5× cost reduction**.

### Validations

- **Faros** — 211 real engineering tasks: GLM-5.2 on Claude Code slightly outperformed Opus 4.8 at half the cost.
- **Arize** — 2,400 agent runs: frontier-priced models offered little advantage on routine work.
- **Notion/Doximity** — cut 1/3 off per-merged-PR costs, with a blended token rate roughly 1/4 that of closed model labs.

Published July 26, 2026.

**Source:** [[raw/articles/2026-07-28_fireworks-ai_fireworks-nexus]]

## K3 LoRA Training on Fireworks

**K3 (2.8T)** is available for Multi-LoRA serving and training in private preview on Fireworks Serverless Training, offering a serverless pay-per-token model for post-training.

### Pricing & Performance

Pay-per-token pricing: $65 for a small RL run (~20 steps, 860K training tokens), completing in 30–60 minutes. LoRA adapters are cheap to train (megabytes in size) and use a rank-r design, best suited for modifying behavior, style, personas, and structured outputs.

### Serving Modes

Two modes are available:

- **Live merge:** Full speed with no overhead, ideal for single-adapter deployments.
- **Multi-LoRA:** Many adapters on one deployment, enabling efficient serving of multiple customized models simultaneously.

### KV-Cache Awareness

Multi-turn agent runs bill at 20% of the standard prefill rate, significantly reducing the cost of conversational and agentic workloads.

### Concrete Tasks

Two example tasks demonstrate the platform:

**Countdown:** Teaches the model a new objective using partial credit as a dense reward signal — reward rises quickly as the model learns.

**Frozen Lake:** Teaches a tool-calling agent loop using a sparse reward — only goal completion pays out. The model's score climbs more slowly, illustrating the difference between reward design strategies. As the article notes, *"The reward is the lever that decides what the model is aiming at."*

### Data Flywheel

The platform enables a complete loop: train adapter → deploy → monitor → collect feedback → trigger a fresh training run. This flywheel ensures consistent numerics alignment between training and inference endpoints.

Published July 26, 2026.

**Source:** [[raw/articles/2026-07-28_fireworks-ai_K3-LoRA-Training.md]]

[[concepts/post-training]] [[concepts/lora]] [[concepts/kimi-k3]] [[concepts/inference-optimization]]

## Embedding Model Fine-Tuning (July 2026)

Fireworks published a practical recipe for **fine-tuning a general-purpose embedding LLM (Qwen3-Embedding-8B) into a domain-specific embedding model via contrastive fine-tuning** — priced under $10 per run. The post is a direct extension of the platform's training story: adapt a strong pretrained model with a contrastive objective instead of training embeddings from scratch.

### Recipe & Method

- **Objective**: Bidirectional **InfoNCE** loss over **in-batch negatives** — a B×B similarity matrix where each query picks its positive among all documents in the batch; symmetric query→doc and doc→query loss with temperature τ=0.02.
- **Training config**: Full-parameter (or LoRA rank 32), ~150 optimizer steps, batch size 64 (batch 8 for 16k-token long-context runs), learning rate 1e-5, epochs 3.
- **Data format**: JSONL of (query, positive) pairs only — negatives are generated automatically in-batch. Trains directly through the Fireworks Training SDK and promotes the checkpoint to a deployable model.
- **Key finding on context length**: A fine-tune trained at a short 512-token window barely beat the base under long-context evaluation — the model must be trained at the context length it will serve at.

### Benchmark Results (base → fine-tuned)

| Task | Metric | Base | Fine-tuned | Gain |
|------|--------|------|-----------|------|
| Legal Citation Retrieval (LegalBench, 4,899 questions / 6,061-case corpus) | nDCG@100 | 0.462 | 0.644 | +39% |
| Legal Citation Retrieval | Recall@100 | 0.540 | 0.758 | +40% |
| Legal Citation Retrieval | nDCG@10 | — | — | +36% |
| Clinical Trial Matching (TREC Clinical Trials, ~63k corpus, ~130 training queries) | nDCG@100 | 0.495 | 0.556 | +12% |
| Clinical Trial Matching | Recall@100 | 0.303 | 0.352 | +16% |
| EU Case-Law Citation Retrieval (LegalPincite, paragraph→paragraph) | nDCG@100 | 0.548 | 0.584 | +7% |
| EU Case-Law Citation Retrieval (LegalPincite, case→case, 16k window) | nDCG@100 | 0.484 | 0.778 | +61% |
| EU Case-Law Citation Retrieval (case→case) | Recall@100 | 0.653 | 0.881 | +35% |

- Gains reproduce with open tooling: a standalone sentence-transformers kit lands within ~0.03 nDCG@100 of the production trainer on most tasks.
- The case→case long-context result roughly **doubles** ranking quality (nDCG@10 0.40→0.72, MRR 0.62→0.89).

Published July 29, 2026.

**Source:** [[raw/articles/2026-07-31_fireworks-ai_fine-tuning-your-own-embeddings-model]]

## LoRA vs Full Fine-Tuning: Three Tests (July 2026)

Fireworks ran controlled SFT experiments on **Qwen3.5-9B** to answer when a FullFT advantage over LoRA is real — and which lever closes it. Three synthetic tasks with automatic checkers (Placement, Register allocation, Nexa VM) let every answer be scored without a human judge. The three tests form a per-gap protocol: **rank test, data coverage test, tuned learning-rate test**.

### Findings

- **Placement — the gap came from data and learning rate, not adapter size.** 10× more unique data on the same 6,000-step budget roughly doubled LoRA validity and cut the FullFT gap in half; quadrupling rank (32→128) moved the result by one point. A tuned rank-32 LoRA (LR 8e-5) reached 82.67% vs FullFT's 83.00% — statistically indistinguishable.
- **Register allocation — rank moved the result.** LoRA-r128 reached 90.5% validity vs FullFT's 93.0%, recovering most of the operational gap, though FullFT retained an advantage in exact trace reproduction (35.5% vs 25.5%).
- **Nexa VM — learning-rate tuning was decisive.** The best LoRA rate (8e-5) sat roughly an order of magnitude above the best FullFT rate (1e-6), consistent with Thinking Machines' *LoRA Without Regret* (2025) and Biderman et al.'s *LoRA Learns Less and Forgets Less* (2024).
- **Bottom line**: when a FullFT beats a simple LoRA run, test coverage, optimization, and rank *before* switching — a fixed-recipe FullFT advantage often erases under recipe tuning.

Published July 2026.

**Source:** [[raw/articles/2026-07-31_fireworks-ai_three-tests-to-run-before-you-switch-from-LoRa-to-FullFT]]

## Voyage AI (MongoDB) Partnership — Native Embeddings & Reranking (August 2026)

Fireworks became the **first and only dedicated inference platform** partnered with **Voyage AI by MongoDB** (announced August 5, 2026), bringing the full Voyage lineup natively onto Fireworks: the **Voyage 4 family** (voyage-4-large, voyage-4, voyage-4-lite, voyage-4-nano), **voyage-multimodal-3.5**, and **rerank-2.5**. The entire retrieval-to-response pipeline (embed → retrieve → rerank → generate) now runs on one platform, one API, one latency domain — alongside Fireworks' open-weight model serving and post-training.

### Core Thesis

> Retrieval quality, not model size, is what limits AI built on your data.

A stronger generalist model does not rescue a weak retrieval layer — accuracy is won or lost at the embedding and reranking stage. The post frames this as half of Fireworks' "specialized intelligence" thesis: a general model spends most of its finite capacity being adequate at tasks you never run, whereas post-training an open base model concentrates capability on your actual work. Voyage AI is the frontier of the retrieval half — grounding intelligence in data only you have.

### Benchmark Position

Average retrieval quality comparison (Voyage 4 series vs competitors) — voyage-4-large is top-performing, surpassing:

| vs Model | Advantage |
|----------|-----------|
| voyage-4 | +1.87% |
| voyage-4-lite | +4.80% |
| Gemini Embedding 001 | +3.87% |
| Cohere Embed v4 | +8.20% |
| OpenAI v3 Large | +14.05% |

### Platform Consolidation Argument

Previously teams faced a tradeoff: route retrieval to a separate specialist vendor (two bills, two latency profiles, an extra network hop per call, wider security/compliance surface) or consolidate on one platform and accept whatever retrieval it happened to offer (capping retrieval quality). Voyage on Fireworks removes the overhead without giving up frontier retrieval quality — proprietary data stays inside fewer trust boundaries under one review.

### Model Tuning per Workload

- **voyage-4-large** — where accuracy matters most
- **voyage-4** — balancing accuracy with speed
- **voyage-4-lite** — optimized for latency and cost
- **voyage-4-nano** — ideal for local development
- **voyage-multimodal-3.5** — interleaved text and visual corpora (multimodal RAG with vision-capable LLMs)
- **rerank-2.5** — refining retrieval results; instruction-following targets long-horizon agents fetching context mid-loop

### Use Cases

1. **Customer-facing support/documentation agents** — voyage-4-large embeddings + rerank-2.5 + LLM on Fireworks (accuracy first)
2. **Internal knowledge assistants** — Voyage 4 Lite + rerank-2.5 (cost-optimized, high volume)
3. **Grounded retrieval inside agentic systems** — rerank-2.5's instruction following suits long-horizon agents; retrieval becomes a tool the agent calls with the reasoning model served on Fireworks, avoiding a per-step hop to another vendor
4. **Embeddings-only workloads** — large-scale semantic search, recommendation, and deduplication run on embeddings/reranking alone at millions of items

This extends Fireworks' earlier embedding work ([[concepts/rag-systems]]), including the July 2026 contrastive fine-tuning recipe for embedding LLMs and the MongoDB Atlas RAG integrations from May 2026. See [[entities/voyage-ai]] for the model provider side.

**Source:** [[raw/articles/2026-08-08_fireworks-ai_voyage-ai-models-now-on-fireworks]]

## Sources

- [Open Source Agents Frontier Advisors](https://fireworks.ai/blog/open-source-agents-frontier-advisors) — Fireworks AI × Harvey, June 2026
- [Software Engineering Daily, Episode 1919: Fireworks AI](https://softwareengineeringdaily.com/2026/04/28/open-weight-ai-models/) — April 28, 2026
- [Fireworks AI Platform](https://fireworks.ai)
- [Fireworks AI Series C Announcement](https://fireworks.ai/blog/series-c)
- [Sacra: Fireworks AI Revenue & Valuation](https://sacra.com/c/fireworks-ai/)
- [Tracxn: Fireworks Company Profile](https://tracxn.com/d/companies/fireworks/)
