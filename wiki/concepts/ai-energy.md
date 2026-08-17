---
title: "AI Energy"
created: 2026-08-08
updated: 2026-08-17
type: concept
tags:
  - concept
  - inference
  - training
  - quantization
  - speculative-decoding
  - distillation
  - data-center
  - sustainability
  - scaling
  - scaling-laws
  - gpu
  - infrastructure
  - economics
  - cost-optimization
  - token-economics
  - training-efficiency
  - frontier-models
  - nvidia
  - ai-hardware
sources:
  - raw/articles/2026-08-05_hn-discussion_ai-energy-data-center-sustainability.md
  - raw/newsletters/2026-08-11-meta-s-big-open-source-comeback.md
  - raw/newsletters/2026-08-16-12b-of-us-ratepayers-money-wasted-on-a-modeling-mistake-and-pjm-wants-to-do-it-a.md
  - https://www.iea.org/reports/electricity-2024
  - https://arxiv.org/abs/2311.16863
  - https://arxiv.org/abs/2211.02001
related:
  - "[[concepts/inference]]"
  - "[[concepts/speculative-decoding]]"
  - "[[concepts/subprime-data-center-crisis]]"
  - "[[concepts/ai-economics]]"
  - "[[concepts/ai-industry-financial-sustainability]]"
  - "[[concepts/cpu-inference-llm]]"
  - "[[concepts/gguf-quantization]]"
  - "[[concepts/model-distillation]]"
  - "[[concepts/ai-infrastructure-circular-financing]]"
  - "[[concepts/ai-memory-crisis]]"
---

# AI Energy

## Executive Summary

AI energy consumption has emerged as one of the most critical constraints on frontier model scaling. As models grow from billions to trillions of parameters and inference becomes a ubiquitous service, the electricity requirements of both training runs and ongoing serving infrastructure are drawing intense scrutiny from researchers, investors, regulators, and the public. The NVIDIA Vera architecture whitepaper (August 2026) brought renewed attention to power envelope concerns, as even next-generation server CPUs must balance performance against thermal and electrical limits. This page surveys the current state of knowledge on AI energy costs across the full lifecycle -- training, inference, and data center operations -- and catalogs the efficiency techniques and sustainability commitments aiming to bend the energy curve.

The central tension: AI capability scaling demands exponentially more compute, but power infrastructure, carbon commitments, and economic viability impose hard physical and financial ceilings. Understanding these constraints is essential to assessing the trajectory of AI development.

---

## Training Energy Costs

Training frontier models requires staggering amounts of electricity, concentrated into weeks- or months-long runs on tens of thousands of GPUs.

### Published and Estimated Figures

| Model | Estimated Training Energy | GPU Configuration | Notes |
|---|---|---|---|
| GPT-3 (175B) | ~1,287 MWh | ~10,000 V100 GPUs | Early benchmark; now dwarfed by subsequent models |
| GPT-4 | ~50+ GWh (estimated) | ~25,000 A100 GPUs, 90-100 days | OpenAI has not disclosed official figures; estimates derived from reported cluster size and runtime |
| Llama 3 405B | ~10-15 GWh | ~16,000 H100 GPUs | Meta reported 30.8M GPU-hours on custom 24K GPU clusters |
| DeepSeek-V3 | ~2.8 GWh | ~2,048 H800 GPUs, ~2 months | Remarkably efficient; DeepSeek claims ~$5.6M training cost, far below Western counterparts |
| Gemini Ultra | Undisclosed | Undisclosed | Google has not released training energy data |

### Scaling Trends

Training energy scales roughly with model size and training tokens. The trend from GPT-3 to GPT-4 represented a ~40x increase in energy consumption over roughly 3 years. If this trajectory holds, a hypothetical GPT-5-scale training run could require 500 GWh to multiple TWh -- equivalent to the annual electricity consumption of a small city.

However, algorithmic and hardware efficiency gains partially offset scaling costs. DeepSeek's architecture demonstrated that multi-token prediction, mixture-of-experts routing, and FP8 mixed-precision training can dramatically reduce per-parameter energy costs compared to dense transformer training.

### Energy Breakdown in Training

A typical large-scale training run's energy is consumed by:
- **GPU compute**: ~60-70% -- the H100 draws ~700W at peak, with DGX systems pulling ~10.2 kW per node
- **Interconnect and networking**: ~10-15% -- InfiniBand/NVLink fabric power for multi-node synchronization
- **Cooling**: ~15-20% -- depending on air vs. liquid cooling
- **Storage and ancillary**: ~5% -- checkpoint I/O, metadata servers, monitoring

---

## Inference Energy Costs

While training energy is a one-time cost, inference energy accumulates continuously for as long as a model is served. For widely deployed models, lifetime inference energy can exceed training energy by orders of magnitude.

### Per-Query Estimates

| Model | Energy per Query (est.) | Comparison |
|---|---|---|
| Standard Google Search | ~0.3 Wh | Baseline |
| ChatGPT query (GPT-3.5) | ~2.9 Wh | ~10x a Google search |
| ChatGPT query (GPT-4) | ~3-10 Wh | Higher for longer reasoning chains |
| Llama 3 70B (local) | ~0.1-0.5 Wh | Depends on quantization and batch size |

### The Inference Multiplier Problem

For models like ChatGPT, which serve hundreds of millions of queries per day, inference energy dominates total lifecycle costs. Consider:
- 100 million queries/day at 3 Wh/query = 300 MWh/day = ~110 GWh/year
- This is roughly 2x the estimated GPT-4 training energy, every year, for a single product

The inference energy problem is compounded by:
- **Longer reasoning chains**: Chain-of-thought, agentic loops, and deep research queries can consume 10-100x more tokens than simple Q&A
- **Multi-model serving**: Providers typically run multiple model sizes simultaneously (free tier, plus tier, pro tier)
- **Redundant capacity**: Data centers must over-provision for peak load, wasting energy during low-utilization periods
- **Always-on agent workloads**: Autonomous coding agents, monitoring systems, and continuous research agents run 24/7

---

## Data Center Infrastructure

### Power Density Trends

AI data centers differ fundamentally from traditional cloud data centers in power density:

| Metric | Traditional DC | AI DC (2024) | AI DC (2026+) |
|---|---|---|---|
| Rack power density | 5-10 kW | 40-60 kW | 100+ kW |
| Facility total | 10-50 MW | 100-300 MW | 500 MW - 1 GW |
| Cooling type | Air | Air + rear-door HX | Direct-to-chip liquid |

The shift from H100 (700W) to B200 (1,000W) to Vera-era GPUs pushes rack power densities beyond what air cooling can handle. NVIDIA's Grace-Hopper and Vera architectures explicitly target power efficiency as a first-class design constraint -- Vera's LPDDR5X memory subsystem draws only ~50W for 1.2 TB/s of bandwidth, a conscious tradeoff against DDR5 DIMMs.

### Geographic Distribution and Grid Impact

AI data centers are increasingly sited based on power availability rather than network latency:
- **Northern Virginia**: The world's largest data center market; Dominion Energy projects data center load could reach 30+ GW by 2035
- **Ireland**: Data centers consumed 21% of the country's electricity in 2023; moratoriums debated
- **Singapore**: Lifted its 2019 data center moratorium in 2023 but with strict power efficiency requirements
- **Nordics**: Attracting AI DCs for abundant hydropower and natural cooling

The IEA projected in its Electricity 2024 report that global data center electricity consumption could double from ~460 TWh in 2022 to over 1,000 TWh by 2026, with AI workloads as the primary growth driver. AI-specific data center demand alone could reach 200-350 TWh annually by 2030.

### Moratoriums and Regulatory Pushback (2026)

The regulatory climate for data center siting hardened sharply in 2026, extending the earlier Ireland and Singapore debates to the United States:

- **New York (August 2026)**: Governor Kathy Hochul imposed a one-year moratorium on data center construction -- the most high-profile state-level restriction to date, signaling that grid and water constraints have become a political liability in major markets
- **100+ local jurisdictions**: More than 100 local governments have enacted similar construction restrictions or moratoriums, reflecting grassroots opposition in grid- and water-stressed communities
- **The data center fight**: Ezra Klein and Jasmine Sun's reporting on the data center fight (including Midwest field reporting) documents how local opposition has moved from noise to binding policy, forcing developers to negotiate with communities rather than only with utilities (per Superintel+, 2026-08-11)

These restrictions compound the power-delivery bottlenecks below: even where transformers and transmission capacity could be secured, permitting and political approval are now an additional multi-year risk for new AI data center projects.

### Grid Infrastructure Bottlenecks

Power delivery, not GPU availability, is increasingly the binding constraint:
- **Transformer lead times**: Large power transformers for data center substations have 2-3 year manufacturing backlogs
- **Transmission capacity**: Interconnection queues in major markets (PJM, ERCOT) stretch 3-7 years
- **On-site generation**: Microsoft, Google, and Amazon are contracting directly with nuclear and geothermal providers to bypass grid constraints
- **Gas peaker plants**: Some developers propose behind-the-meter gas turbines as bridge power, undermining sustainability claims

### PJM Capacity Market & Ratepayer Costs (Aug 2026)

SemiAnalysis's reverse-engineered model of PJM (America's largest electricity market, 66M residents) documents how **grid modeling errors compound AI-load economics**. PJM's capacity market was designed two decades ago and never experienced demand growth until the AI data center boom; it is now **structurally anti-growth** with a governance "vetocracy" (rule changes need a two-thirds majority across five equally weighted member sectors, so any two sectors can veto):

- **Modeling errors (~$12B waste)**: PJM underestimates its existing fleet by ~**4 GW** because its methodology (2024 shift from EFORd to Reserve Requirement Study) ignores winter cold-air efficiency gains (gas turbines produce up to 25% more power in cold, dense air) and post-Storm Elliott winterization (400 of ~700 gas plants invested in reliability measures by 2024). SemiAnalysis estimates this overstated the supply/demand shortfall, wasting **~$12B of ratepayer money from 2025-2027** — better modeling would have saved **$6.7B (2025/26)** and **$4.9B (2026/27)** with only 14MW less power procured.
- **Auction economics**: Four record-breaking auctions since July 2024 procured 134-138 GW/year each at prices jumping from **$28.92 to $270-333 per MW-day**, totaling **$63.6B** — yet only **4.8 GW of new capacity** was procured. Existing generators bid at $8-14/MW-day (PJM's own monitor) vs GB's $18/MW-day comparison; the median existing combined-cycle plant made 407% of its going-forward costs in energy+ancillary markets alone. PJM cut new-generation lead time from 36 to 10 months (now 23), making new builds near-impossible.
- **Emergency auction risk**: PJM plans a **Reliability Backstop Auction (Sep 30 - Oct 21, results Dec 2)** signing contracts to 2043 for new large loads (datacenters) with **no committed counter-parties**; every PJM state must pass cost-allocation policy (none have). Interconnection fast-tracks are failing: RRI (51 projects, 31.5% of MW withdrawn, first output 2030) and the Expedited Track (10 units/year, opened Jul 31 2026) have energized zero MW; a 220 GW interconnection application window reopened April 2026 after no study path since Oct 2021.
- **AI relevance**: This is the clearest quantified case of **AI data center load growth colliding with legacy grid market design** — ratepayer costs, emergency auctions, and interconnection failure directly constrain the AI infrastructure buildout. See [[concepts/subprime-data-center-crisis]] and [[concepts/ai-economics]] for adjacent analyses.

---

## Efficiency Techniques

A growing toolkit of techniques aims to reduce both training and inference energy per unit of model capability.

### Quantization

Reducing numerical precision cuts both memory and compute energy:

| Precision | Memory vs FP32 | Energy vs FP32 | Use Case |
|---|---|---|---|
| FP16/BF16 | 2x reduction | ~2x reduction | Training, standard inference |
| INT8 | 4x reduction | ~3-4x reduction | Inference (llama.cpp, vLLM) |
| INT4 | 8x reduction | ~5-7x reduction | Edge/CPU inference |
| FP4/NF4 | 8x reduction | ~6-8x reduction | Extreme compression (QLoRA) |

[[concepts/gguf-quantization]] enables CPU-based inference at acceptable quality, drastically reducing the energy cost of serving smaller models. Bonsai 27B demonstrated that aggressive quantization can run a capable model entirely on-phone.

### Speculative Decoding

[[concepts/speculative-decoding]] uses a small draft model to propose multiple tokens, which a large target model verifies in parallel. This achieves 2-4x throughput improvement -- and corresponding energy reduction -- for output-heavy workloads. DeepSeek's DeepSpec framework reports 60-85% faster generation.

### Model Distillation

[[concepts/model-distillation]] trains a smaller "student" model to replicate a larger "teacher," preserving capability while reducing inference energy by 10-100x. DeepSeek-R1's distilled variants (1.5B to 70B) demonstrate that reasoning capability can survive aggressive compression.

### Mixture-of-Experts (MoE)

MoE architectures (used by DeepSeek-V3, Mixtral, and reportedly GPT-4) activate only a fraction of parameters per token, reducing per-token compute by 5-10x relative to dense models of equivalent total parameter count.

### Sparse Attention and KV Cache Optimization

- **Sparse Attention**: FlashAttention, sliding window, and sparse patterns reduce the O(n^2) attention memory footprint
- **KV Cache Compression**: Quantizing or evicting KV cache entries reduces memory pressure and allows larger batches
- **Multi-Query / Grouped-Query Attention**: Reduces KV cache size by 4-8x with minimal quality loss

### Hardware Efficiency

- **NVIDIA H100/B200**: FP8 tensor cores deliver 2x training throughput vs FP16 at iso-power
- **Apple Silicon**: Unified memory and efficiency cores enable local inference at laptop-scale power budgets
- **LPUs (Language Processing Units)**: Groq's deterministic architecture claims 10x energy efficiency vs GPU inference for specific workloads
- **CPU Inference**: [[concepts/cpu-inference-llm]] demonstrates that quantized models on consumer CPUs can serve at <50W total system power

---

## Sustainability Commitments

### Major Lab Pledges

| Organization | Commitment | Status (2026) |
|---|---|---|
| Microsoft | Carbon negative by 2030; zero-waste by 2030 | Emissions up ~30% since 2020 due to AI DC expansion; investing in nuclear (Three Mile Island restart) and fusion |
| Google | 24/7 carbon-free energy by 2030 | Data center emissions up ~48% since 2019; signed 500 MW SMR nuclear deal with Kairos Power |
| Amazon (AWS) | Net-zero carbon by 2040 | Pledged to be water-positive by 2030; data center water use up significantly |
| Meta | Net-zero emissions across value chain by 2030 | Llama training powered by renewable energy; geothermal contracts |
| OpenAI | No public sustainability commitment | Sam Altman personally invested in fusion (Helion Energy) |
| Anthropic | No public sustainability commitment | Has not published energy or carbon data for Claude training |
| DeepSeek | No public sustainability commitment | Lower absolute energy use due to efficiency, but China's grid is coal-intensive |

### The Carbon Accounting Problem

Several structural issues complicate AI sustainability claims:

- **Renewable Energy Certificates (RECs)**: Purchasing RECs does not mean the data center actually runs on renewables; it is an accounting mechanism that critics equate to indulgences
- **24/7 matching**: Google's approach of hourly matching of consumption with carbon-free sources is more rigorous but harder to achieve
- **Scope 3 emissions**: GPU manufacturing, data center construction, and embodied carbon of concrete/steel are rarely reported
- **Induced demand**: Jevons paradox -- efficiency improvements that lower per-query costs may increase total consumption by expanding access

---

## Economic Angle: Energy as a Constraint

### The Inference Subsidy Model

[[concepts/ai-economics]] documents the inference-subsidizes-training thesis: frontier labs lose money on inference to capture users and data, while investors fund training runs. This model is viable only as long as inference energy costs remain manageable relative to expected future revenue. If inference energy costs grow faster than willingness to pay, the economics break.

### AI Industry Financial Sustainability

[[concepts/ai-industry-financial-sustainability]] explores whether the current AI business model is viable. Energy costs are a significant and growing line item:
- At $0.08/kWh industrial rates, a 100 MW data center costs ~$70M/year in electricity alone
- Frontier training runs can add $10-50M in electricity costs per run
- These costs must be amortized over inference revenue, which currently operates at negative gross margins for most providers

### The Subprime Data Center Dimension

[[concepts/subprime-data-center-crisis]] argues that data center construction has overshot actual AI demand by ~15x, with Special Purpose Vehicle (SPV) debt structures creating systemic financial risk. The energy dimension compounds this: overbuilt data centers represent not just stranded financial assets but wasted embodied energy in cement, steel, semiconductors, and ongoing parasitic power draw even when underutilized.

### Power as the Ultimate Scaling Limit

Physical constraints on power delivery may impose a harder ceiling on AI scaling than algorithmic progress or capital availability:
- A 1 GW data center requires a dedicated power plant or major substation -- there are few sites globally that can accommodate this
- Transformer and switchgear supply chains are capacity-constrained
- Public opposition to data center construction is growing in water-stressed and grid-constrained regions
- Regulatory interventions (moratoriums, efficiency mandates) are increasing, particularly in Europe

---

## Open Questions

- Can efficiency gains (quantization, sparsity, MoE) outpace scaling-driven demand growth, or is Jevons paradox inevitable?
- Will the power grid be the binding constraint on AGI development?
- How much of current data center construction represents genuine demand vs. speculative overbuilding?
- What role should government play in mandating AI energy transparency and efficiency standards?
- Can nuclear (fission and fusion) scale fast enough to meet AI's near-term power needs?

---

## Related Pages

- [[concepts/inference]] -- LLM inference engines and their tradeoffs
- [[concepts/speculative-decoding]] -- Accelerating inference via draft-then-verify
- [[concepts/subprime-data-center-crisis]] -- Financial risks of data center overbuilding
- [[concepts/ai-economics]] -- Economics of AI, including inference cost models
- [[concepts/ai-industry-financial-sustainability]] -- Whether AI business models are viable
- [[concepts/cpu-inference-llm]] -- Energy-efficient local inference on consumer hardware
- [[concepts/gguf-quantization]] -- Quantization formats and their efficiency gains
- [[concepts/model-distillation]] -- Training smaller models from larger ones
- [[concepts/ai-infrastructure-circular-financing]] -- How GPU vendors finance data center buildout
- [[concepts/ai-memory-crisis]] -- HBM supply constraints as an AI scaling bottleneck
