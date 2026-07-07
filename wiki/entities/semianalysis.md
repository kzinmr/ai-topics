---
title: "SemiAnalysis"
type: entity
created: 2026-05-20
updated: 2026-07-07
tags:
  - company
  - lab
  - infrastructure
  - blog
  - economics
aliases: [semianalysis-research]
related:
  - [[entities/dylan-patel]]
  - [[concepts/gpu-cloud-rankings]]
  - [[concepts/compute-scaling-bottlenecks]]
  - [[concepts/gpu-cluster-tco-goodput]]
  - [[concepts/ai-lab-subscription-vs-api-economics]]
  - [[concepts/post-training/grpo-infrastructure]]
  - [[concepts/post-training/asynchronous-rl]]
sources:
  - raw/articles/2026-05-20_semianalysis_clustermax-2-gpu-cloud-ratings.md
  - raw/articles/substack.com--app-link-post--1509e963.md
  - raw/articles/2026-06-10_semianalysis_subscription-vs-api-business-model.md
  - raw/articles/2026-06-16_semianalysis_rl-systems-throughput.md
  - raw/newsletters/2026-06-18-stop-saying-half-of-2026-us-datacenter-capacity-is-canceled.md
  - raw/newsletters/2026-07-06-nvidia-gpu-debt-backstop-unleashes-the-ai-project-trinity-capital-offtake-and-da.md
  - https://semianalysis.com/
---

# SemiAnalysis

**SemiAnalysis** is a boutique AI and semiconductor research firm founded by [[entities/dylan-patel|Dylan Patel]] in 2020. It has grown from a solo research blog into a 12-person global team providing data-driven analysis of semiconductor supply chains, AI compute economics, and cloud infrastructure.

## Key People

- **Dylan Patel** — Founder, CEO, and Chief Analyst. Started SemiAnalysis in 2020 as a one-person blog.
- **Myron Xie** — Lead Analyst. Covers GPU economics, AI training infrastructure, and semiconductor supply chain.
- **Daniel Nishball** — Analyst. Covers AI infrastructure, cloud economics, and RL training systems.
- **Matej Sirovatka** — Collaborator at [[entities/prime-intellect|Prime Intellect]], co-author on RL systems analysis.
- **Ameen Patel** — Collaborator at Prime Intellect, co-author on RL systems analysis.
- **Sami Jaghouar** — Collaborator at Prime Intellect, co-author on RL systems analysis.
- **Peyton Walters** — Collaborator at [[entities/modal|Modal]], co-author on RL systems sandbox analysis.
- **Nan Jiang** — Collaborator at Modal, co-author on RL systems sandbox analysis.
- **Erik Dunteman** — Collaborator at Modal, co-author on RL systems sandbox analysis.

## Key Research Areas

### Core Research
- Subscription-based deep-dive reports for the finance industry
- Covers semiconductor supply chains, AI compute, hardware economics
- Trusted by the world's largest GPU buyers and financial leaders

### ClusterMAX™ GPU Cloud Rating System
- Industry-standard benchmark for evaluating GPU cloud providers
- Evaluates 209 providers across 10 criteria (Security, Lifecycle, Orchestration, Storage, Networking, Reliability, Monitoring, Pricing, Partnerships, Availability)
- Rating tiers: Platinum → Gold → Silver → Bronze → Not Recommended
- Based on hands-on testing and 140+ end user interviews
- Live at https://www.clustermax.ai/

### AI Accelerator & HBM Model
- Tracks GPU buyers with estimated quarterly GPU counts
- Covers NVIDIA, AMD, Intel, TSMC, ASML, SK Hynix, Micron supply chain
- Used by industry participants for capacity planning

### AI Tokenomics Model
- Tracks compute supply flow and demand across token factories
- Covers AI labs (OpenAI, Anthropic), cloud providers, inference workloads

### Datacenter Industry Model

SemiAnalysis maintains a **proprietary three-model architecture** for datacenter analysis, covering 550+ suppliers and 6,000+ facilities:

| Model | Scope | Inputs |
|-------|-------|--------|
| **Datacenter Industry Model** | Capacity tracking, deployment timelines, commitments | 550+ suppliers, 6,000+ facilities, 75+ equipment categories |
| **Energy Model** | Power availability, grid interconnection, permitting timelines | Regional utility data, transmission build schedules, regulatory timelines |
| **Industrials Model** | Construction materials, labor availability, supply chain bottlenecks | HVAC, generators, switchgear, cooling equipment supply chains |

#### Key Methodological Insight

Bloomberg/Sightline's claim that "half of 2026 US datacenter capacity is canceled" was debunked by SemiAnalysis's proprietary model in June 2026:

- **Denominator error**: Sightline tracks only large-scale projects ($100M+), missing the majority of datacenter capacity in planning. SemiAnalysis's broader dataset reveals a denominator 2-3× larger.
- **Cancellation misinterpretation**: The majority of tracked "cancellations" are projects in the **speculative pre-construction phase** — land options, feasibility studies, preliminary permitting — not active construction sites being abandoned. This is standard industry practice where 30-40% of early-stage projects never break ground.
- **Active construction tracking**: SemiAnalysis's model distinguishes between speculative land banking (common among REITs and investment funds) and shovel-ready/under-construction capacity. The latter shows minimal cancellation rates.
- **Actual impact**: Genuine delays are concentrated among smaller, under-capitalized developers. Tier 1 hyperscaler projects (AWS, Microsoft, Google, Meta) continue on schedule.

Tracks datacenter capacity, deployments, and commitments for CoreWeave, Nebius, Oracle, and other Neocloud analysis.

### GPU Economics
- Detailed NVIDIA GPU cost modeling and margin analysis
- H100/H200/B200/B300 TCO and supply chain tracking
- Blackwell architecture reliability and deployment analysis

### AI Infrastructure
- GPU cloud provider evaluation via ClusterMAX
- Neocloud economics and hyperscaler margin analysis
- Datacenter capacity and deployment tracking

### RL Training Systems
- Generator/trainer throughput matching framework
- PipelineRL asynchrony and policy staleness analysis
- Sandbox startup latency and scalability optimization
- Early pruning and adaptive sampling for throughput

## Key Publications

### ClusterMAX 2.0 (November 2025)
- 46,000+ word comprehensive review of 84 providers (up from 26 in v1.0)
- CoreWeave retained Platinum tier (only member)
- Nebius, Oracle, Azure, Fluidstack, Crusoe in Gold tier
- Google, AWS, together.ai, Lambda in Silver tier
- 37 total clouds achieved medallion rating

### GB200 NVL72 Hardware Architecture (August 2025)
- Component supply chain and BOM analysis
- NVLink reliability issues, firmware bugs, backplane/cable cartridge problems

### Compute Bottlenecks Analysis (March 2026)
- Three-bottleneck framework (Logic → Memory → ASML EUV)
- Dwarkesh Podcast appearance became most-cited infrastructure analysis

### RL Systems: Mind the Gap (June 2026)
- Deep analysis of RL training infrastructure for LLM post-training
- Key thesis: system efficiency depends on matching generator and trainer throughput
- Introduces **PipelineRL** asynchrony — trainer pushes weights while rollouts in progress, tolerating policy staleness
- **Three-actor model**: generator (produces rollouts), RL environment/sandbox, trainer (consumes rollouts)
- **Queue model**: generator → queue → trainer, where effective generation rate = acceptance rate × generation rate
- Group size analysis: N=8 for easy tasks, N=16 for medium, N=64 for hard reasoning
- Sandbox challenges: startup latency (Modal optimizations), concurrency scaling, robustness against model misbehavior
- Throughput optimizations: early pruning, adaptive sampling, concurrency tuning
- Collaborators: [[entities/prime-intellect|Prime Intellect]] (Matej Sirovatka, Ameen Patel, Sami Jaghouar), [[entities/modal|Modal]] (Peyton Walters, Nan Jiang, Erik Dunteman)
- See [[concepts/post-training/grpo-infrastructure]] and [[concepts/post-training/asynchronous-rl]] for detailed frameworks

## Industry Influence

SemiAnalysis has established itself as a trusted independent voice in the AI infrastructure space. ClusterMAX is cited by:

- **OpenAI** (Peter Hoeschele, GM Stargate): "valuable tool for data-driven decisions"
- **Meta** (Santosh Janardhan, Head of Global Infrastructure): "industry can rely on"
- **Dell** (Michael Dell, CEO): "shines a light on what truly matters"
- **HPE** (Hunter Almgren, Distinguished Technologist): "go-to benchmark for GPU clouds"
- **Atreides Management** (Gavin Baker, CIO): "industry standard for evaluating GPU clouds"
- **CoreWeave**: Used as TCO justification for pricing premiums
- **Nebius**: Used to demonstrate engineering maturity
- **Fluidstack**: Used to validate "Forward Deployed Engineering" ethos


### AI Tokenomics: AWS Bedrock Margin Analysis (May 2026)

In May 2026, SemiAnalysis published a deep-dive analysis of AWS cloud margins, revealing that **AWS Bedrock is the only CSP with rising margins** (EBIT +213bp Q/Q in 1Q26) while Azure, GCP, Oracle, and CoreWeave see flat or declining margins. Key findings:

| Metric | Value |
|--------|-------|
| Bedrock EBIT margin | ~55% at ~$26M/MW Anthropic ARR on Bedrock compute in 1Q26 |
| Bedrock run rate (1Q26) | $5.5B |
| Bedrock mix growth | 9% of AWS AI revenue in 1Q25 → 37% in 1Q26 |
| Customer Anthropic model usage | 80-90% of Bedrock customers use Anthropic models |
| Anthropic total ARR | $30B ($21B net new ARR added in recent period) |
| Anthropic inference gross margin | Mid-60% (improved from 38% in 2025) |

The core driver is **TaaS (Token-as-a-Service)** economics — TaaS revenue generates far higher margins than traditional IaaS. AWS's vertical integration advantage (Trainium/Graviton processors) enables this margin profile. SemiAnalysis also exposed **Google's margin inflation** — GCP's reported margins exclude $5.4B in training costs, artificially boosting numbers.

This analysis includes the first detailed tokenomics model for AWS's AI business, showing how Anthropic's growth through Bedrock reshapes CSP economics.

### GPU Cluster TCO & Goodput Framework (April 2026)

SemiAnalysis released a comprehensive framework for evaluating GPU cluster costs beyond headline $/GPU-hr pricing. The framework decomposes TCO into **8 line items** (GPUs, Storage, Networking, Control Plane, Support, Goodput Expense, Setup Expense, Debugging Expense) and provides scenario analysis across 3 workload types (Large LLM Pretrain, Multimodal RL Research, Inference Endpoints) and 3 provider tiers (Gold/Hyperscaler/Silver).

**Key contribution**: SemiAnalysis developed the **Goodput Expense** formulae quantifying the hidden cost of GPU failures across three fault-tolerance approaches (TorchFT, AWS Checkpointless, TorchPass). They demonstrated that for large training jobs, Gold-tier TCO can be 10-15% lower than Silver-tier despite identical GPU pricing, and that inference workloads are effectively indifferent to provider reliability. The framework is supported by free [TCO Calculator](https://www.clustermax.ai/) and [Goodput Calculator](https://www.clustermax.ai/) tools on ClusterMAX.

### AI Lab Subscription vs API Economics (June 2026)

SemiAnalysis conducted an empirical study of AI lab subscription economics by purchasing every tier of both Anthropic and OpenAI subscription plans and running long horizon coding tasks until exhausting weekly limits. Key findings:

- **Common assumption debunked:** The $200/month plan does not max out at ~$2,000/month in API-equivalent value — subscriptions are "far more generous"
- **Margin pressure:** If both labs have 75% API gross margins, subscription margins for heavy users are significantly worse (potentially negative)
- **Strategic prediction:** Labs will **withhold new models/features from subscription tiers** rather than explicitly nerf usage limits (which triggers public backlash)
- **Mythos test case:** Anthropic's upcoming "Mythos" model may launch as API-only, signaling a permanent shift toward feature-gated subscriptions
- **Cost trajectory:** Opus 4.8-level models will be profitable at $20/month "in the near future" as inference costs continue falling

This analysis positions SemiAnalysis as a key voice in the AI business model debate, extending their infrastructure expertise into platform economics. See [[concepts/ai-lab-subscription-vs-api-economics]] for the full framework.

### GPU Debt Backstop: AI Project Trinity (July 2026)

In July 2026, SemiAnalysis published a groundbreaking analysis of NVIDIA's GPU debt backstop program and its implications for AI infrastructure financing:

#### AI Project Trinity

SemiAnalysis identified three converging forces — **Capital + Offtake + Datacenter** — that form "AI Project Trinity":

1. **Capital**: Institutional debt financing for GPU procurement — a multi-trillion-dollar credit market emerging
2. **Offtake**: Hyperscaler take-or-pay commitments guaranteeing GPU capacity utilization
3. **Datacenter**: Physical infrastructure buildout to house the GPUs

#### Key Findings

| Metric | Value |
|--------|-------|
| Projected AI debt outstanding (2029) | **$7.1 trillion** |
| Annual AI Capex (2028) | **Well north of $2 trillion** |
| Mechanism | NVIDIA backstop = take-or-pay commitment to Neoclouds |

#### NVIDIA's Backstop Program

NVIDIA introduced a **GPU debt backstop** that transforms the GPU leasing market:

- NVIDIA provides **minimum revenue guarantees** on GPU capacity to Neocloud providers
- This de-risks Neocloud financing, enabling them to secure debt for GPU purchases
- The program effectively creates a **secondary market for GPU capacity** with NVIDIA as the insurer

#### Three Obstacles to Market Maturity

SemiAnalysis identified three structural obstacles before the GPU debt market can mature:

1. **Hyperscaler backstops are not infinite** — the major cloud providers have limits on how much GPU capacity they will guarantee
2. **Lenders are on a learning curve** — financial institutions lack the expertise to evaluate GPU-as-collateral risk
3. **Capital providers lack pricing tools** — no GPU price index exists, making it impossible to value GPU-backed debt instruments accurately

#### Market Implications

- The GPU debt market creates a new asset class: **GPU-backed securities**
- **Neoclouds cannot offer short-term rentals** because their financing depends on long-term GPU utilization guarantees
- The absence of a **GPU price index** makes the market opaque — SemiAnalysis calls for a standardized pricing tool similar to the ClusterMAX GPU Cloud Rating system
- This analysis positions NVIDIA as not just a hardware supplier but a **financial infrastructure provider** for the AI industry

Source: raw/newsletters/2026-07-06-nvidia-gpu-debt-backstop-unleashes-the-ai-project-trinity-capital-offtake-and-da.md

## Contact
- clustermax@semianalysis.com
- https://semianalysis.com/

## Creator

Founded and led by [[entities/dylan-patel|Dylan Patel]] (Founder, CEO, Chief Analyst). Patel started SemiAnalysis as a one-person blog in 2020 and grew it into a recognized industry authority known for contrarian, data-grounded analysis that challenges prevailing narratives about AI compute scaling.

## Sources

- [SemiAnalysis](https://semianalysis.com/)
- [ClusterMAX](https://www.clustermax.ai/)
- "ClusterMAX 2.0: The Industry Standard GPU Cloud Rating System" — SemiAnalysis (November 2025)
- Dwarkesh Podcast — Dylan Patel episode (March 2026)
