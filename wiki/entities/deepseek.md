---
title: DeepSeek
created: 2026-04-26
updated: 2026-06-26
type: entity
tags: [company, open-source, model, inference, training, benchmark]
sources:
  - raw/articles/2026-04-25-china-ai-robotics-industry-competitive-landscape.md
  - raw/articles/simonwillison.net--2026-apr-24-deepseek-v4--d443e33a.md
  - raw/newsletters/2026-05-02-nvidia-blackwell-vs-huawei-ascend.md
  - raw/newsletters/2026-05-10-spacexai-s-spice-trade-anthropic-targets-the-trillion-and-openai-s-stack-sweep.md
  - raw/articles/2026-05-01_nist-caisi-deepseek-v4-evaluation.md
  - raw/papers/2024-12-27_2412.19437_deepseek-v3-technical-report.md
  - raw/papers/2025-01-22_2501.12948_deepseek-r1.md
  - raw/papers/2025-12-02_2512.02556_deepseek-v3.2-technical-report.md
  - raw/articles/2026-05-08_martinfowler-deepseek-papers.md
  - raw/papers/2026-04-xx_deepseek-v4-technical-report.md
  - raw/newsletters/2026-05-23-ainews-all-model-labs-are-now-agent-labs.md
  - raw/articles/2026-05-22-deepseek-strategy.md
  -   - raw/newsletters/2026-05-27-deepswe-makes-coding-agents-sweat.md
---

# DeepSeek

## Overview

Chinese AI lab and open-source LLM provider that has driven **cost disruption** in the AI industry. Founded as an offshoot of the quantitative hedge fund High-Flyer. Exemplifies China's open-source AI strategy enabling rapid global uptake.

## Technical Evolution & HPC Co-Design Philosophy

The core of DeepSeek's success lies in **HPC Co-Design** (simultaneous optimization of model architecture and hardware infrastructure). According to Martin Fowler's analysis (2026), every architectural decision is designed to **exploit and circumvent** the limitations of the underlying HPC hardware (especially NVIDIA H800 interconnect constraints).

### 3 Research Arcs

| Arc | Key Technologies | Representative Paper |
|-----|------------------|---------------------|
| **Efficiency** | MLA (KV cache compression), FP8 training, DualPipe | V2, V3 |
| **Sparsity** | DeepSeekMoE, Device-Limited Routing, Auxiliary-Loss-Free Gating | V2, V3 |
| **Reasoning** | GRPO, rule-based rewards, multi-stage RL/SFT pipeline | R1 |

### Evolution of Paper Series

```
DeepSeek-LLM (Jan 2024)           Scaling Laws discovery
    ↓                             Redefined scaling via non-embed FLOPs/token
DeepSeek-V2  (Jun 2024)           Architecture efficiency revolution
    ↓                             MLA + DeepSeekMoE + Device-Limited Routing
DeepSeek-V3  (Dec 2024)           Massive-scale HPC Co-Design
    ↓                             671B MoE, FP8, DualPipe, Aux-Loss-Free
DeepSeek-R1  (Jan 2025)           Emergence of reasoning
                                 Pure RL → self-verification, introspection, distillation (Nature)
DeepSeek-V3.2(Dec 2025)           Frontiers of reasoning capability
                                 DSA + scalable RL + agent synthesis
                                 IMO/IOI gold medals, approaching GPT-5/Gemini-3.0-Pro
DeepSeek-V4  (Apr 2026)           Frontier scale
                                 1.6T Pro / 284B Flash, 1M context, Ascend 950
```

Innovation at each stage demonstrated that frontier performance can be reached even with constrained compute resources (H800 GPUs).

## Models

### DeepSeek V4 Series (April 2026)

**[[concepts/deepseek-v4|DeepSeek-V4]]** is an ultra-efficient MoE series processing 1-million-token contexts at practical cost. Key innovations: Hybrid Attention (CSA+HCA+SWA), Manifold-Constrained Hyper-Connections (mHC), Muon Optimizer, MegaMoE, TileLang DSL, On-Policy Distillation, FP4 QAT.

| Model | Total Params | Active Params | Context | Architecture |
|-------|-------------|---------------|---------|-------------|
| **V4-Pro** | 1.6T | 49B | 1M tokens | Mixture of Experts |
| **V4-Flash** | 284B | 13B | 1M tokens | Mixture of Experts |
| **V4-Pro-Max** | 1.6T+ | 49B+ (reasoning) | 1M tokens | MoE + reasoning tokens |

**Efficiency vs V3.2 (at 1M context):**
| Metric | V4-Pro | V4-Flash |
|--------|--------|----------|
| Single-Token FLOPs | 27% (3.7x lower) | 10% (10x lower) |
| KV Cache Size | 10% (10x smaller) | 7% (14x smaller) |

**Key facts:**
- MIT license, open weights on HuggingFace (Pro: 865GB, Flash: 160GB)
- V4-Pro is the largest open weights model, surpassing Kimi K2.6 (1.1T) and GLM-5.1 (754B)
- **Codeforces 3206** rating (V4-Pro-Max) — equivalent to human rank #23
- White-collar tasks: 63% non-loss rate vs Claude Opus 4.6
- Agent-native: Interleaved Thinking (reasoning retention across tool call boundaries), Quick Instruction
- **SWE-bench Verified: 80.6%** — first open-weight model to exceed 80%
- Trained on 32T+ tokens with Anticipatory Routing + SwiGLU Clamping for stability
- **Local inference**: V4-Flash (~154GB) runs on Mac Studio M3 Ultra (512GB); V4-Pro (~800GB) requires data center VRAM

### Pricing (per million tokens)

| Model | Input | Output |
|-------|-------|--------|
| **V4-Flash** | $0.14 | $0.28 |
| **V4-Pro** | $1.74 | $3.48 |

V4-Flash is cheaper than GPT-5.4 Nano ($0.20/$1.25) and Gemini 3.1 Flash-Lite ($0.25/$1.50). V4-Pro is the cheapest large frontier model, undercutting all Western competitors.

### GPT-5.5 Cost Comparison (May 2026)

Following DeepSeek V4's release, the **South China Morning Post** reported that the cost per conversation on GPT-5.5 is roughly **32x that of DeepSeek-V4**. However, price and cost are not the same thing:

- **Energy cost asymmetry**: SemiAnalysis found that Huawei's CloudMatrix 384 (powering most Chinese AI workloads) draws **4.1x the electricity** of NVIDIA's GB200 NVL72 to deliver the same compute. Every token on Chinese hardware costs more in energy.
- **Subsidy-driven pricing**: The cheap consumer pricing is propped up by state subsidies and near-zero margins
- **Capacity gap**: The Institute for Progress projects US production at **6.89M B300-equivalents in 2026**, while Huawei stays between **62K–160K** — China's chip stack operates at roughly **1% of American output**
- **Market strategy**: China's aggressive pricing reflects operating as a smaller producer with incentives to gain market share quickly, especially in the Global South, Middle East, and Southeast Asia

### Hardware: Huawei Ascend 950 Deployment

DeepSeek V4 is confirmed to run on **Huawei Ascend 950** chips for inference and deployment, manufactured by China's **SMIC** foundry. This is strategically significant:

- Ascend 950 achieved this despite China lacking access to ASML EUV lithography
- SMIC used quadruple-patterning with DUV to work around EUV restrictions
- DeepSeek engineering pushed Huawei chip utilization from ~60% to >85%
- Reports suggest pre-training may still rely on NVIDIA GPUs (ChinaTalk, 04/27/2026), but inference independence is confirmed
- Rumored: former ASML engineers recruited to build EUV prototype in Shenzhen lab

### Earlier Models

- **DeepSeek-LLM** (January 2024) — 67B params. Redefined scaling laws with non-embed FLOPs/token (M). Showed that high-quality data justifies larger models at the same token count. Trained on 2T bilingual tokens, surpassing LLaMA-2 70B on math and coding. Scaling Laws paper.
- **DeepSeek-V2** (June 2024) — Revolution in architecture efficiency. First introduced **MLA** (Multi-Head Latent Attention: low-rank KV cache compression) and **DeepSeekMoE** (shared expert + routed experts, Device-Limited Routing overcoming H800 interconnect constraints). Foundation for all subsequent models.
- **[[concepts/deepseek-v3|DeepSeek V3]]** (December 2024) — 671B total / 37B active params, MoE. Landmark technical report (arXiv:2412.19437): first FP8 training at 671B scale, auxiliary-loss-free load balancing, multi-token prediction, DualPipe. Trained on 14.8T tokens for $5.576M (2.788M H800 GPU hours). Achieved GPT-4o-class performance at <1/20th the training cost. MIT license.
- **[[concepts/deepseek-v3-2|DeepSeek V3.2 / V3.2 Speciale]]** (December 2025) — 685B params. Three innovations: **DSA** (DeepSeek Sparse Attention: learnable sparse attention providing $O(L^2)→O(Lk)$ efficiency), **Scalable RL** (enhanced GRPO: Unbiased KL estimation + Off-Policy Sequence Masking + Keep Routing Mask, post-training budget >10% of pretraining), **Large-scale agent task synthesis** (1,827 environments, 85K prompts). V3.2-Speciale won gold medals at IMO 2025 and IOI 2025, placed 2nd worldwide at ICPC World Finals. Performance approaching GPT-5/Gemini-3.0-Pro. DSA also propagated to V4 and GLM-5.1. Technical report (arXiv:2512.02556).
- **[[concepts/deepseek-r1|DeepSeek R1]]** (January 2025) — Reasoning-focused model. Published in **Nature** (Vol. 645, 2025). First large-scale demonstration of emergent reasoning through pure RL (GRPO). "Aha moment," autonomous acquisition of self-verification and introspection. AIME 2024: 79.8%, MATH-500: 97.3% (comparable to o1-1217). Deployed via distillation to Qwen-1.5B/7B, Llama-8B/70B. Training cost $294K. Reasoning patterns also distilled to V3.

## V4-Pro Permanent Discount (May 2026)

In May 2026, DeepSeek made a **permanent 75% discount** on V4-Pro pricing, triggering strong market reaction as it materially changes the cost/performance frontier:

| Metric | V4-Pro Price |
|--------|--------------|
| **Input** | **$0.435/M tokens** (was $1.74) |
| **Output** | **$0.87/M tokens** (was $3.48) |
| **Cached Input** | **$0.0036/M tokens** |
| **Blended** | **~$0.18/M tokens** (75% below previous) |

**Cost comparison vs competitors (blended):**
- ~3× cheaper than [[concepts/gemini]]|Gemini 3.1 Pro Preview]]
- ~12× cheaper than GPT-5.5
- ~19× cheaper than [[entities/anthropic|Claude Opus 4.7]]

The discount makes inference "too cheap to meter" at the blended rate, accelerating the trend toward agent-native pricing where model cost becomes a negligible component of total agent operation cost.

## Harness Team Formation (May 2026)

DeepSeek created its first **"Harness team"** — an agent execution environment engineering team — signaling the lab's recognition that the moat is shifting from standalone model performance to the **model + harness + workflow + UI + memory** stack. This follows the same trajectory as OpenAI (Codex harness), Anthropic (Claude Agents SDK), and AI21 Labs (full pivot to agents).

The Harness team's formation validates the "Systems over Models" thesis and represents a strategic response to the industry-wide shift where [[concepts/harness-engineering/agent-harness|agent harness]] infrastructure is becoming a competitive differentiator.

> Source: [AINews May 23, 2026](https://www.latent.space/p/ainews-all-model-labs-are-now-agent)

## Updated Pricing Table
The pricing table in the Models section (pre-discount) should be read in context with the permanent discount above. The current API pricing is:

| Model | Input | Output |
|-------|-------|--------|
| **V4-Flash** | $0.14 | $0.28 |
| **V4-Pro** | ~~$1.74~~ → **$0.435** (75% off) | ~~$3.48~~ → **$0.87** (75% off) |

## Strategy

### Core Thesis: 10 Trillion USD Hardware Ecosystem Play

The key to understanding DeepSeek's strategy is not short-term revenue (such as selling coding plans) but rather the perspective that they are playing a **$10 trillion game to create an entire China-originated AI hardware ecosystem** (@bookwormengr, May 2026). CEO Liang Wenfeng's vision, as expressed in "AGI for everyone," targets a much larger prize.

- **Consistent choice to forgo short-term revenue**: No multimodal model, no voice model, no video model. Until May 2026, no harness team even existed (recruitment recently began)
- **All innovations aim to alleviate hardware constraints**: MoE, MLA, DSA, CSA, HSA, Engram, mHC — all oriented toward "achieving more with less HW resources"
- **Open-source commitment**: Accelerating global adoption through open publication, aiming for de facto standard status in the ecosystem

### KV Cache Economics: Creating a Memory Industry

DeepSeek's KV cache compression innovations act as a catalyst for the entire Chinese memory industry:

| KV Cache at 1M Context | HBM Consumption |
|------------------------|-----------------|
| **DeepSeek V4 (1.6T)** | **5.48 GB** |
| GLM5 (~700B, using MLA+DSA) | 60 GB |
| Qwen3-235B-A22B (GQA) | 89 GB |

**Strategic implications:**
- Ultra-small KV cache → offloading to SSD becomes economically viable → **explosive increase in NAND demand**
- China's YMTC (Yangtze Memory Technologies) is emerging as a 3D NAND giant. DeepSeek creates a massive market for NAND
- DeepSeek's cache hit price is **less than 3%** of Sonnet 4.6, and persists for multiple hours → the extraordinary low pricing is underpinned by KV cache efficiency
- Dual Path paper technology also enables fast KV cache reload from SSD

### Memory-Compute Trade-offs: LPDDR + Engram

Due to the absence of EUV lithography, Chinese GPUs/ASICs will **permanently lag behind the West in transistor density**. DeepSeek overcomes this structural constraint with a strategy of **replacing computation with memory**:

- **LPDDR memory**: CXMT (ChangXin Memory Technologies) trails by only 0.5 generations in speed and 1 generation in density — a catchable distance
- **Engram** (Q1 2026): A module that converts N-gram embeddings into O(1) hash lookups. Replaces knowledge retrieval that Transformers simulate through computation with memory references → a highly favorable trade-off: "one LPDDR lookup vs a full Transformer forward pass"
- **SGLang approach**: Keep weights in LPDDR, stream to HBM as needed. DeepSeek's 4-bit weights + many-expert MoE architecture is naturally suited to this approach

**Conclusion**: Abundant NAND and LPDDR memory compensates for the computational deficit of Chinese GPUs/ASICs, enabling AI infrastructure independent of Western hardware.

### Hardware Enablement: Lifting the Entire Chinese Semiconductor Ecosystem

Under US export controls, all of DeepSeek's innovations have the **secondary effect of making the entire Chinese hardware industry competitive**:

| DeepSeek Innovation | Reduction Target | Beneficiary Chinese HW Industry |
|--------------------|-----------------|--------------------------------|
| MLA + CSA + HSA | HBM demand (up to 98% reduction) | YMTC (NAND/SSD), CXMT (LPDDR) |
| Engram | Computation FLOPs | CXMT (LPDDR), ASIC manufacturers |
| TileLang DSL | CUDA dependency | Moore Threads, MetaX, Biren, Iluvatar CoreX (all GPU/ASICs) |
| MoE + 4-bit Weights | HBM bandwidth | Network chip manufacturers |
| MegaMoE + Dual Pipe | Interconnect bandwidth | Chinese NVLink-equivalent chips |

**Strategic significance of TileLang**: Write a kernel once and it runs on all hardware platforms → bypasses the CUDA moat. Complements the CUDA compatibility layers of Chinese GPU makers (Moore Threads, MetaX, Biren, Iluvatar CoreX). Also facilitates adoption of Western alternative GPUs like AMD.

### Equity-Collaboration Model: OpenAI-AMD Style Capital Partnership

DeepSeek's monetization model is expected to follow the same warrant agreement structure that OpenAI signed with AMD/Cerebras:

> "AMD has issued OpenAI a warrant for up to 160 million shares of AMD common stock, structured to vest as specific milestones are achieved." — AMD Press Release, Oct 2025

- OpenAI: Acquires shares upon achieving AMD/Cerebras consumption milestones → partner success directly links to self-interest
- DeepSeek: Expected to sign similar agreements with Chinese memory, ASIC, CPU, and networking companies, closely collaborating to develop the HW stack for AI workloads
- Total market cap of Western AI stocks exceeds $10T → equivalent industrial creation is possible in China
- DeepSeek itself could achieve **$1T valuation** while realizing "AGI for everyone"

### Long Game: RL Post-Training + RSI

With expanded hardware options and reduced compute demand, DeepSeek can pursue more ambitious training projects:

- **Large-scale RL post-training**: Generating trillions of tokens of trajectory data. Training at 1M context enables long-horizon tasks
- **RSI (Recursive Self-Improvement)**: AI designing and running its own experiments. Trial-and-error requires enormous computation, but is necessary for AGI → ASI. Freeing hardware constraints makes RSI achievable

### Open-Source Feedback Loop

- Open-source models with widespread free accessibility (MIT license)
- Radical cost undercutting: API prices 90-97% lower than Western alternatives
- Open-source feedback loop: adoption → rapid iteration → further adoption → reinforced industrial dominance
- Rapid global uptake via open-source channels (available on OpenRouter, HuggingFace)
- **Standardization strategy**: Innovations like MLA, DSA, and GRPO propagate across Chinese AI labs (GLM, Kimi, etc.) → DeepSeek architecture becomes the de facto standard for Chinese AI industry

### Contrarian Nature

DeepSeek's history of "contrarian" bets (from @bookwormengr's Hero's Journey analysis):

| Industry Norm | DeepSeek's Choice |
|--------------|-------------------|
| Build dense models | MoE (hard to train but efficient) |
| PPO (standard RL algorithm) | GRPO (novel invention, no Critic needed) |
| Incremental improvement | Reinvent from first principles |
| Sell applications for immediate revenue | Long game of cultivating hardware ecosystem |
| Keep source closed for competitive advantage | Open-source for de facto standardization |

> Source: [@bookwormengr "DeepSeek's 10 trillion USD grand strategy"](https://x.com/bookwormengr/status/2057909493250539891) (May 22, 2026)

## Market Impact

- Cost disruption in AI model pricing — V4 series dramatically undercuts all Western frontier models
- Part of China's broader open-source AI ecosystem alongside Alibaba's Qwen (100,000+ HuggingFace derivatives)
- Recognized in U.S. congressional hearings on national security risks of PRC AI (March 2026)
- V4 deployment on domestic Huawei chips demonstrates partial decoupling from Western hardware

### $7.4B Funding Round & Aggressive Expansion (June 2026)

On June 26, 2026, the Wall Street Journal reported that DeepSeek raised **$7.4 billion** in new funding, with plans to **double its workforce**. This represents one of the largest funding rounds in AI history and signals a major escalation in the competitive landscape:

- **Scale**: $7.4B places DeepSeek in the same funding tier as Anthropic ($7.5B+ total) and well above Mistral (~$1B)
- **US Enterprise Adoption**: US firms are increasingly turning to DeepSeek as a lower-cost alternative to OpenAI and Anthropic, accelerating the open-weight model's enterprise penetration
- **Staffing**: Plans to double headcount suggest aggressive hiring across research, engineering, and go-to-market
- **Competitive Signal**: DeepSeek is no longer just a research lab — it's scaling into a full-stack AI company competing directly with US frontier labs
- **Geopolitical Dimension**: The funding comes amid US export controls and growing concerns about Chinese AI capabilities. DeepSeek's ability to raise this amount underscores investor confidence in China's AI sector despite regulatory headwinds


### DeepSeek OCR: Text Compression via Visual Representation (May 2026)

DeepSeek developed a technique achieving **9-12x text compression** by using visual representations as a compressed medium for long text, with high OCR precision. This research direction reduces token waste, which translates to faster inference, cheaper API pricing, and competitive pressure on other providers.

## Relationships

- [[entities/china-ai-industry]] — Key company driving China's AI competitiveness
- [[nvidia]] — Competitor in AI hardware; DeepSeek reducing dependence on NVIDIA
- [[open-source-ai]] — Leading open-source AI model provider
- [[concepts/deepseek-v3]] — Predecessor model series
- [[concepts/deepseek-v3-2]] — Intermediate model (DSA, scalable RL, agent synthesis)
- [[concepts/deepseek-v4]] — Latest model series (1M context, Hybrid Attention, mHC)
- [[concepts/deepseek-r1]] — Reasoning model (Nature 2025)
- [[concepts/post-training/grpo]] — RL algorithm introduced in R1
- [[token-economics]] — Pricing disruption context
- [[concepts/inference]] — Efficiency innovations in V4 architecture
- [[entities/simon-willison]] — Covered V4 technical details
- [[entities/kimi]] — Competitor (K2.6 at 1.1T)

## Independent Evaluation: NIST CAISI (May 2026)

On May 1, 2026, the **Center for AI Standards and Innovation (CAISI)** at NIST published an independent evaluation of DeepSeek V4 Pro. Key findings:

- **8-month capability gap vs US frontier** — CAISI's IRT analysis estimates V4 Pro at Elo 800 vs GPT-5.5 xhigh at 1260
- **Benchmark contamination suspected** — DeepSeek's self-reported parity with GPT-5.4 may reflect public benchmark contamination; CAISI's private benchmarks (PortBench, CTF-Archive-Diamond) reveal larger gaps
- **Strengths**: Mathematics (OTIS-AIME-2025: 97%), PUMaC 2024: 96%
- **Weaknesses**: Abstract reasoning (ARC-AGI-2 private: 46% vs GPT-5.5 79%), Cybersecurity (CTF: 32% vs 71%), Software engineering (PortBench: 44% vs 78%)
- **Cost efficiency confirmed**: V4 Pro is 53% cheaper than GPT-5.4 mini on certain benchmarks ($1.74/$3.48 per M tokens vs $0.75/$4.50)
- **Verdict**: Most capable PRC model to date, but not yet frontier-competitive despite aggressive marketing claims

Sources: [NIST CAISI Report](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro)

## Open Questions

- Can DeepSeek fully train on Ascend chips, or does training still depend on NVIDIA GPUs?
- Will the SMIC quadruple-patterning approach scale to next-generation chips?
- How sustainable is the extreme price undercutting strategy?
- How will Western export controls evolve in response to V4 running on domestic Chinese hardware?
