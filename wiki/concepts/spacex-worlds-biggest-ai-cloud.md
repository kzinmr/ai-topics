---
title: "SpaceX as World's Biggest AI Cloud"
type: concept
created: 2026-11-05
updated: 2026-11-05
tags:
  - infrastructure
  - data-center
  - ai-infrastructure
  - economics
  - ai-hardware
sources:
  - raw/articles/2026-11-03_semianalysis_spacex-worlds-biggest-ai-cloud.md
  - https://newsletter.semianalysis.com/p/elon-is-doing-it-again-spacex-will
aliases:
  - spacex-ai-cloud
  - minihard
  - macrohard
related:
  - entities/semianalysis
  - entities/dylan-patel
  - concepts/google-spacex-ai-compute-deal
  - concepts/xai-anthropic-colossus-deal
  - concepts/gpu-cloud-rankings
  - concepts/ai-bubble-economics
---

# SpaceX as World's Biggest AI Cloud

SemiAnalysis (Dylan Patel & Jeremie Eliahou Ontiveros, November 3, 2026) argues SpaceX — post-xAI merger — is becoming **the fastest and possibly largest AI datacenter builder on Earth**, revising its 2027 forecast from 10 GW to **~13 GW** of capacity. For scale: SemiAnalysis equates ~13 GW built in 1.5 years to roughly *all of Google's datacenter capacity added from 1999–2026*. Two months after publishing the original "10 GW in 2027" piece (widely dismissed), SemiAnalysis reports **3.6 GW already under construction** across sites and >9 GW of capacity identified.

> **Source status**: free preview of a paywalled SemiAnalysis report (30 substantive paragraphs extracted). All capacity/site claims are SemiAnalysis' proprietary Datacenter/Energy Model estimates, many labeled with the authors' own confidence levels. **Confidence: medium.**

## Key Claims

### Build speed records (all self-held)

| Site | Milestone | Time |
|------|-----------|------|
| Colossus 1 retrofit | 150 MW | 122 days |
| Colossus 2 | 210 MW | 91 days |
| "MiniHard" (Memphis) | ~450 MW | ~5 months |
| "Gun Range" (Mississippi, greenfield) | new plot south of state line | ~4 months — would be fastest greenfield DC ever at scale |
| "Project SPAM" (mid-Colossus-2 building) | first tranches online Dec 2026 | construction start Oct 5, 2026 — targets beating the 91-day record |
| Colossus 2 expansion | ~2 Stargate Abilenes (2 GW) added | just under one year |

Industry norm is 8–12-month build times; SpaceX is "cutting them in half." Labor runs at ~3,000 workers per GW, and SemiAnalysis attributes the speed partly to **Tesla manufacturing modular MEP equipment** (mechanical/electrical/plumbing) — analogous to Crusoe self-manufacturing switchgear, but at scale.

### Starbase, Texas goes datacenter

The rocket-building site will now host **two datacenters**, going from ground-clearing (late Aug 2026) to full vertical construction (late Sep 2026), with datahall fit-out expected within weeks. SemiAnalysis estimates the site could exceed **1 GW**, powered by **APRs (advanced pressurized water reactors) deployed one month after vertical construction began** (>1 GW APRs possible), plus multiple GWs via pipelines and turbines. A fiber channel through the Port of Brownsville and possible waterfront leasing were flagged by the local mayor.

### Power orchestration at Colossus 2

- >8 GW of behind-the-meter power identified (FTAI, Solaris, etc. — subscriber-only detail).
- TVA grid requests: **Macrohard (700 MW)** and **MiniHard (450 MW)**; a 500 kV GIS substation finishes Dec 31, 2026, connecting to Freeport substation.
- Southaven turbines: legally 2.7 GW nameplate now but only **1.24 GW by July 2027** under a binding July 30, 2026 agreement (MDEQ) — leaving a possible **~300 MW shortfall**.
- SemiAnalysis' resolution: the **largest BESS field in the USA (~5.9–6 GWh)** orchestrating gas + storage (turbines cycle to charge), ultralow PUE ~1.10–1.15, mixed inference/training and customer/internal workloads, and SLA uptime tiering.
- **TeraFab** (the 10 GW, 100M sq ft chip-fab venture) likely hosts a datacenter too — it *started as a datacenter before quietly pivoting to TeraFab*; representatives didn't confirm exclusive SpaceX use, leaving third-party neocloud renting on the table.

### Economics

Prior SemiAnalysis work (cited in this piece) holds that the Anthropic and Google compute deals turned SpaceX into "the most profitable neocloud on earth" — see [[concepts/xai-anthropic-colossus-deal]] and [[concepts/google-spacex-ai-compute-deal]] ($920M/month from Google). The revised 13 GW trajectory underpins a **$300B+ ARR** scenario.

## Assessment

- Every number here flows through SemiAnalysis' proprietary models and satellite/construction surveillance; the "medium-high confidence" TeraFab-datacenter claim is explicitly probabilistic. Treat as informed forecasting, not reporting.
- The regulatory edges are load-bearing: behind-the-meter turbines bypassing grid queues, JETI/TCEQ permitting pauses acknowledged for TeraFab, Southaven nameplate curtailment. The build-speed thesis is inseparable from permitting arbitrage — a recurring theme in [[concepts/ai-bubble-economics]] critiques.
- Counter-frame worth tracking: no independent power-interconnection or utility filing audit of the 13 GW figure has been published.

## Related

- [[entities/semianalysis]] — publisher; Datacenter Industry Model / Energy Model
- [[concepts/google-spacex-ai-compute-deal]] — $920M/month Google compute contract (June 2026)
- [[concepts/xai-anthropic-colossus-deal]] — Anthropic/Google deals behind the neocloud profitability claim
- [[concepts/gpu-cloud-rankings]] — ClusterMax ratings context
- [[concepts/space-gpus]] — the orbital extension of the same vertical-integration logic

## Sources

- [Elon Is Doing It Again: SpaceX Will Be The World's Biggest AI Cloud](https://newsletter.semianalysis.com/p/elon-is-doing-it-again-spacex-will) — Dylan Patel & Jeremie Eliahou Ontiveros, SemiAnalysis, Nov 3, 2026 (paywalled; free preview scraped)
- Raw: `raw/articles/2026-11-03_semianalysis_spacex-worlds-biggest-ai-cloud.md`
