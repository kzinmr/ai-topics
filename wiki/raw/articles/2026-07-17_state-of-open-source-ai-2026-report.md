---
title: "The State of Open Source AI — V1.0 · July 2026"
source_url: "https://stateofopensource.ai/"
published_by: "Mozilla"
published_date: 2026-07-16
captured_date: 2026-07-18
type: raw-article
tags:
  - open-source-ai
  - ai-report
  - mozilla
  - open-weights
  - ai-ecosystem
  - 2026
sources:
  - https://stateofopensource.ai/
  - https://hn.algolia.com/api/v1/items/48947825
hn_discussion:
  post_id: 48947825
  points: 453
  author: rellem
status: captured
---

# The State of Open Source AI — V1.0 · July 2026

**Published by Mozilla** | CTO Letter by Raffi Krikorian | Recurring report

> "Open weights closed the capability gap while the price of intelligence collapsed."

---

## Key Statistics (Stat Band)

- **3.3%** — Capability gap to the top closed models (at parity on coding, behind on reasoning)
- **50×** — Fall in GPT-4-class inference cost in 36 months: $20 → $0.40 per 1M tokens

---

## Section 01: The Current State of Open-Source AI

**Headline**: "Parity reached. The contest is one layer up."

Open weights are no longer a compromise. A majority of production tokens now route through them, and the five highest-volume models on OpenRouter are all open. Closed models still lead at the frontier, on reasoning and multimodality, but the frontier is not what most workloads need. Commodity inputs do not hold pricing power. Value moves up, to the agentic harness.

### Capability Gap: 8.04% → 0.5% → 3.3%
- Jan 2024: 8.04% gap (open vs closed on Chatbot Arena)
- Aug 2024: Collapsed to 0.5%
- Feb 2025: DeepSeek-R1 briefly matched top US model
- Mar 2026: Reopened to 3.3% as closed reasoning models pulled ahead
- Open at/near parity on coding, instruction-following, general knowledge
- Gap concentrates in: reasoning, long-context retrieval, agentic tasks

### Inference Cost: 50× in 36 months
- GPT-4-equivalent price per 1M tokens fell 50×
- Faster than dotcom-era bandwidth or PC-compute price curves
- Sources: Stanford HAI AI Index 2025 (280× GPT-3.5-class over 18 months); Epoch AI (9–900× annual decay); MIT Nov 2025 study (5–10×/yr at frontier)

### Token Share: Open Weights Win
- Open-weight models grew from negligible → ~1/3 by late 2025 → majority by mid-2026
- Five highest-volume models on OpenRouter are all open weights
- Chinese-built models: ~18T weekly tokens vs ~5.5T for US-built — more than 3:1 (FT analysis)
- By request count, closed US providers still lead — the open lead is a token-volume lead, concentrated in coding and agentic workloads

### Developer Adoption: Mozilla/SlashData 2026 Survey
- **79%** of developers adding AI use open models; **71%** use closed
- **50%** use both; **29%** open only; **21%** closed only
- Greater China & East Asia: 89% open adoption
- South America & Western Europe: only regions where closed exceeds open

### The Production Gap
- Only **51%** of open-model teams reach production vs **63%** for closed
- Gap is operational tooling and trust, NOT model capability
- Closed climbs 54% → 73% with company scale; open barely moves: 53% → 57%
- "Enterprises can buy their way through closed deployment. Open deployment waits on tooling nobody has finished."

### Churn Challenges (n=1,410)
- Biggest Δ (churned − still using): Performance, Integration, Maintenance — operational, not capability
- Top challenges: Infrastructure cost (27%), Security/compliance (26%), Maintenance (24%), Deployment complexity (23%), Lack of support (22%)
- South Asia: 39% cite security; 31% cite lack of support
- Only North America (21%) and Greater China (16%) have >15% reporting no major challenges


---

## Section 02: The Open-Source AI Stack

**Headline**: "The open stack scores high on capability, low on operations."

Nine layers and 48 components scored across 10 criteria (1–5):
- Strong (≥4.0): capability, community, innovation, documentation
- Weak (<2.5): **standardization** and **enterprise readiness** — "the operational gap"
- Source: Mozilla stack map, June 2026 (48 components, 1,361 projects)

---

## Section 03: Who's Betting on It

**Headline**: "Open source is a business model."

Five revenue models proven at scale: hosted inference, enterprise platforms, on-prem licensing, fine-tuning services, harness tooling.

### Key Company Metrics

| Company | HQ | Layer | Funding | Valuation | Revenue Signal |
|---------|-----|-------|----------|-----------|----------------|
| **Databricks** | USA | Enterprise platform | — | — | $5.4B run-rate |
| **DeepSeek** | China | Frontier open weights | $7.4B | $50B+ | ~$220M ARR |
| **Mistral AI** | France | Open weights + platform | $3.05B | ~$14B (€20B talks) | ~$400M ARR, 20× YoY |
| **Moonshot AI** | China | Open weights (Kimi) | $3.9B | — | — |
| **Zhipu AI** | China | Open weights (GLM) | Undisclosed | Public | HK IPO 2026 |
| **MiniMax** | China | Open weights | Undisclosed | Public | HK IPO 2026 |
| **Cohere** | Canada | Enterprise/on-prem | $1.7B | — | Command A+ open-sourced May 2026 |
| **Cerebras** | USA | Compute | $2.1B | — | — |
| **Reflection AI** | USA | Open weights | $2.13B | — | — |
| **Together AI** | USA | Inference cloud | $1.334B | — | — |
| **Hugging Face** | USA | Hub | $400M | — | — |
| **LangChain** | USA | Harness tooling | $260M | — | 126k+ stars, 60% dev share |

### Pricing Asymmetry
- OpenRouter (May–Sep 2025): closed models ~80% usage, ~96% revenue
- At ~90% parity, closed costs ~6× more per call
- **~$24.8B** in unrealized annual savings (Nagle–Yue study, Linux Foundation)
- "Where developers route by cost, they route to open weights."

---

## Section 04: Sovereignty — Why It's Happening Everywhere

**Headline**: "Open isn't a vendor choice. It's a sovereignty choice."

- 70+ national AI strategies live
- Strategic question shifted: "whether to have AI policy" → "which layer can a country own"

### The Optionality Case
- June 2026: Claude Fable 5 access cut for all foreign nationals after single government export order — no warning
- "A provider can switch off a model. Nobody can switch off a copy already running on a machine you hold."
- Weights on disk = hedge for companies; policy vs. permission for states
- Cloud repatriation: $90–120k to move 1PB from S3; 80% repatriating; 37signals: $3.2M → <$1M
- "Closed model APIs reproduce the same trap. Open weights are exit rights."

### China: Largest Source of Open Weights
- Qwen out-downloaded next 8 organizations combined (Feb 2026)
- Chinese open-weight models: <2% (late 2024) → >45% (Apr 2026) → ~61% among top 10 on OpenRouter
- DeepSeek: 26,000+ enterprise accounts; 58% of new AI startups in 2025
- Policy: State Council "AI Plus" Initiative (Aug 2025), Five-Year Plan (Mar 2026)
- Strategic hedge against semiconductor export controls
- Even Microsoft exploring Azure-hosted DeepSeek V4 for Copilot workloads


---

## Section 05: The Harness Is the New Frontier

**Headline**: "The agentic harness is another user agent."

The browser was the user agent of the open web. The agentic harness recreates that role one layer up: orchestration loop, tools, memory, sandboxes, and permission model. It is where production difficulty concentrates, and where the open-vs-closed, owner-vs-renter contest restarts.

### Harness Architecture Layers
- **Govern**: Stateful policy, registry & lineage, budget & revocation (Omnigent, OPA, Agent governance toolkit)
- **Surface**: Interface (AG-UI, A2UI), Payment & metering (x402, AP2, UCP)
- **Action**: Sandboxes (E2B, Daytona, Modal), Permission & identity, Eval (Langfuse, Phoenix)
- **Reach**: Tools & context (MCP), Agent-to-agent (A2A), Memory (Mem0, Letta, Zep)
- **Control**: Orchestration loop (LangGraph, CrewAI, AutoGen, LlamaIndex) — the reason-and-act cycle

### Key Harness Metrics
- LangChain: 126,000+ GitHub stars, 60% developer share
- MCP: 97M monthly SDK downloads, 10,000+ active servers, 4,750% growth in 16 months
- MCP donated to Linux Foundation's Agentic AI Foundation (Dec 2025)
- Only ~21% of companies report mature agent governance

### Terminal-Bench: The Harness Gap
- **May 2026 (2.0)**: Third-party scaffold 79.8% vs Claude Code 58.0% — 21.8-point spread favoring harness
- **July 2026 (2.1)**: Labs pulled harness in-house; gap compressed to ~3 points at top
- "The model is eating its way up the stack" — weights and scaffold shipped as one product
- On neutral harness (vals.ai Terminus-2): capability gap ~4 points; price gap 5×
- GLM 5.2 lands fraction behind Claude Opus 4.7 at ~1/5 the cost

### The Write Surface: Unsolved Permission Problem
- **Reads**: Reversible, low-consequence — permissible by default
- **Writes**: Costly/irreversible — need confirmation, approval thresholds, cost caps, revocation
- MCP & A2A both stop at authentication — "knowing who an agent is says nothing about what it may do"
- CoSAI MCP threat model: consent fatigue is top-tier threat
- Emerging solution: meta-harness layer (Databricks Omnigent) — stateful, contextual policies above any single harness

### Security: Closed ≠ Secure
- 2025: CVSS 9.3–9.4 authorization failures hit Anthropic, Microsoft, ServiceNow, Salesforce — all closed
- NTIA recommended monitoring open weights, not restricting them
- "Security concerns are best addressed by investing in the harness. They do not require renting a closed model."

### Where Closed Still Leads
1. Integrated harness (no open model in verified top tier of Terminal-Bench 2.1)
2. Long-context fidelity at 1M tokens (Gemini 3: 89% vs DeepSeek V4-Pro: 41%)
3. Turnkey compliance (SOC 2, HIPAA, zero data retention by default)
4. Accountability (counterparty the customer can hold liable)

---

## Section 06: Opportunities

Five bets that don't require beating the frontier — they require owning the layers above it: the harness, the memory, the permission model — while those layers are still open.

---

## Section 07: The Watchlist

### Capability & Adoption
- **Signal**: 3.3% gap, parity on coding, OpenRouter token share in agentic coding
- **Reverses if**: token share stalls while reasoning gap widens

### The Harness
- **Signal**: Terminal-Bench spread lab-owned vs independent; MCP/A2A governance under AAIF
- **Reverses if**: lab-harness lead widens, or closed platform sets permission standard first

### Market Structure
- **Signal**: Open-lab economics vs metered-pricing breakpoints (~2027–28); sovereign capacity as counterweight
- **Reverses if**: sovereign funding lapses or open-lab economics fail

### Trust & Safety
- **Signal**: NTIA "monitor, don't restrict" holding
- **Reverses if**: major misuse event or shift from monitoring to restriction

> "Look at who is seated in the rooms where AI gets decided, and with what status. The day they seat the people who keep AI open, portable, and widely deployed on equal footing, the shift from renting to owning will have happened. The window is open now."

---

## CTO's Full Letter Highlights

Hugging Face: 2.5M public models, 13M users, 1/3 of Fortune 500. OpenRouter: 25T tokens/week (5× growth in 6 months). Spring 2026: strongest closed model scored 60, strongest open 54 (vs. 22 a year earlier). European Commission proposed "open source first" rule. Canada target: lift business AI adoption from 12% to 60%.

> "None of them asked permission, and none of them could have rented this. They own it — that is the whole idea."

> "We have been here before. Mozilla exists because one company tried to own the front door to the web. Twenty-five years later, someone is running the same play. We bet on open the first time. Open won. Together, we can do it again."


---

## HN Discussion Highlights (Post 48947825, 453 points by rellem)

### Critical Reception
- **Majority complaint**: Font/design choices make reading difficult; prose described as LLM-like and later confirmed AI-generated via pangram.com detection
- **Terminology debate**: Open source vs open weights — report is about open weights, not true open source (no training data/code for most models)

### Substantive Comments
- **GodelNumbering**: OpenRouter market share flipped 60-40 closed to 63-37 open in 4 months; tokens processed 888B to 4.19T/day (~5x in 4 months)
- **babblingfish**: Open models is what will kill Anthropic and OpenAI. Hyperscalers can run models without licensing fees. Apple can make them smaller and put them on device.
- **amanharshx**: Kimi K3 release shows open models getting closer to frontier; 50x inference cost drop is amazing
- **brunooliv** (counterpoint): Open models still not comparable to closed for medium-sized tasks — give any medium task to ANY open-source frontier model and watch them struggle
- **thih9**: Too few mature open source harnesses; wants community-led BYOK modular agent orchestration
- **semiquaver**: No community around truly open models released with source data and training methodology. Term open has been diluted to a shocking extent.
- **paxys**: Concern — all good open models built by private VC-funded companies. How long will they continue to be charitable?
- **mrcwinn**: OpenRouter as biased data source — users there already looking to bypass frontier models
- **draxil**: Almost all about open weight, but the title says Open Source.
- **cuuugi**: That font choice feels aggressive.
- **ProofHouse**: Open Source AI will ultimately win. Think it through.
- **melodyogonna**: Surprised American AI companies are not trying to compete in the open weight market, that is very myopic

### Link Shared
- PDF (easier to read): https://stateofopensource.ai/state-of-open-source-ai-2026.pdf

---

## Key Sources Cited in Report

- Chatbot Arena (Jan 2024 – Mar 2026)
- OpenRouter 100T-token study (Nov 2024–Nov 2025) and live leaderboard
- Stanford HAI AI Index 2025
- Epoch AI cost decay analysis
- MIT Nov 2025 inference cost study
- Mozilla/SlashData 2026 developer survey (MZCS1, n=1,410)
- Mozilla stack map, June 2026 (48 components, 1,361 projects)
- Nagle-Yue study for Linux Foundation (~.8B pricing asymmetry)
- FT analysis of OpenRouter token routing
- Terminal-Bench 2.0 / 2.1 (May/July 2026)
- vals.ai Terminus-2 run
- CoSAI MCP threat model
- NTIA open-weight recommendations
- Open Source AI jurisdictions dataset, July 2026
- DeepSeek-R1 model card
- Future of Life AI Safety Index
- OECD.AI Policy Observatory
- Oxford Insights Gov AI Readiness Index 2024
