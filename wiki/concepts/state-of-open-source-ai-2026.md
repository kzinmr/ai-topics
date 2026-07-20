---
title: State of Open Source AI 2026
created: 2026-07-20
updated: 2026-07-20
type: concept
tags:
  - open-source
  - ai-economics
  - token-economics
  - inference
  - sovereign-ai
  - frontier-models
  - ai-adoption
  - agent-harness
  - china
  - geopolitics
  - cost-optimization
  - ecosystem
sources:
  - raw/articles/2026-07-17_state-of-open-source-ai-2026-report.md
---

# State of Open Source AI 2026

The **State of Open Source AI V1.0** is Mozilla's inaugural recurring report on the [[concepts/open-source-ai]] ecosystem, published July 2026. Authored by CTO Raffi Krikorian, it provides a comprehensive snapshot of open-weight model capabilities, adoption, economics, and geopolitics.

> "Open weights closed the capability gap while the price of intelligence collapsed."

## Capability Gap: 3.3% Behind Closed Models

The report tracks the capability gap between open-weight and closed models over two years:

| Date | Gap | Context |
|------|-----|---------|
| Jan 2024 | 8.04% | Chatbot Arena baseline |
| Aug 2024 | 0.5% | Rapid convergence |
| Feb 2025 | ~0% | DeepSeek-R1 briefly matched top US model |
| Mar 2026 | 3.3% | Closed reasoning models pulled ahead |

Open-weight models are at or near parity on coding, instruction-following, and general knowledge. The remaining gap concentrates in reasoning, long-context retrieval, and agentic tasks. On neutral harnesses (vals.ai Terminus-2), the capability gap is approximately 4 points while the price gap is 5x.

## Inference Cost: 50x Reduction in 36 Months

GPT-4-class inference cost fell from ~$20 to ~$0.40 per 1M tokens over 36 months — a 50x decline faster than dotcom-era bandwidth or PC-compute price curves. Supporting data points include Stanford HAI AI Index 2025 (280x for GPT-3.5-class over 18 months), Epoch AI estimates (9-900x annual decay), and an MIT November 2025 study finding 5-10x/year at the frontier.

See also: [[comparisons/llm-api-pricing]], [[concepts/token-economics]], [[concepts/ai-economics]].

## Token Share: Open Weights Now Majority

Open-weight models grew from negligible share to ~1/3 by late 2025 to a majority by mid-2026. The five highest-volume models on [[entities/openrouter]] are all open weights.

**Geography matters**: Chinese-built open-weight models account for ~18 trillion weekly tokens versus ~5.5 trillion for US-built models — a ratio exceeding 3:1. [[entities/deepseek]] alone serves 26,000+ enterprise accounts and powered 58% of new AI startups in China during 2025. By request count, closed US providers still lead; the open lead is a token-volume lead concentrated in coding and agentic workloads.

## Developer Adoption

From the Mozilla/SlashData 2026 developer survey (n=1,410):

- **79%** of developers adding AI use open models; **71%** use closed
- **50%** use both; **29%** open only; **21%** closed only
- Greater China & East Asia: 89% open adoption
- South America & Western Europe: only regions where closed exceeds open

## The Production Gap

Despite high adoption, only **51%** of open-model teams reach production versus **63%** for closed-model teams. The gap is operational tooling and trust, not model capability. Closed climbs from 54% to 73% with company scale; open barely moves (53% to 57%). As the report puts it: "Enterprises can buy their way through closed deployment. Open deployment waits on tooling nobody has finished."

Top challenges cited by developers (n=1,410):
1. Infrastructure cost (27%)
2. Security/compliance (26%)
3. Maintenance (24%)
4. Deployment complexity (23%)
5. Lack of support (22%)

## The Open-Source AI Stack

Mozilla's stack map (June 2026, 48 components, 1,361 projects) scored nine layers across ten criteria. Strong scores (>=4.0) in capability, community, innovation, and documentation. Weak scores (<2.5) in **standardization** and **enterprise readiness** — the "operational gap."

## Sovereignty

The report frames open weights as a sovereignty choice, not merely a vendor decision. With 70+ national AI strategies active, the strategic question has shifted from "whether to have AI policy" to "which layer can a country own." See [[concepts/sovereign-ai]].

Key events: Claude Fable 5 access was cut for all foreign nationals in June 2026 after a single government export order with no warning. "A provider can switch off a model. Nobody can switch off a copy already running on a machine you hold."

China has become the largest source of open weights. Qwen out-downloaded the next eight organizations combined (Feb 2026). Chinese open-weight models rose from <2% (late 2024) to >45% (Apr 2026) to ~61% among the top 10 on OpenRouter. Policy drivers include the State Council "AI Plus" Initiative (Aug 2025) and the Five-Year Plan (Mar 2026), serving as a strategic hedge against semiconductor export controls.

## The Harness Is the New Frontier

The report identifies the agentic harness as the next battleground. The browser was the user agent of the open web; the agentic harness recreates that role one layer up — orchestration loop, tools, memory, sandboxes, and permission model. See [[concepts/harness-engineering/agent-harness]].

Highlights from Terminal-Bench:
- **May 2026 (2.0)**: Third-party scaffold 79.8% vs Claude Code 58.0% — 21.8-point spread favoring harness
- **July 2026 (2.1)**: Labs pulled harness in-house; gap compressed to ~3 points at top
- "The model is eating its way up the stack"

## Pricing Asymmetry

On OpenRouter (May-Sep 2025), closed models captured ~80% of usage but ~96% of revenue. At ~90% capability parity, closed costs ~6x more per call. The Nagle-Yue study for the Linux Foundation estimated **~$24.8 billion** in unrealized annual savings from routing to open weights.

## Key Companies

| Company | HQ | Role | Revenue Signal |
|---------|-----|------|----------------|
| Databricks | USA | Enterprise platform | $5.4B run-rate |
| DeepSeek | China | Frontier open weights | ~$220M ARR, $50B+ valuation |
| Mistral AI | France | Open weights + platform | ~$400M ARR, 20x YoY |
| Together AI | USA | Inference cloud | $1.334B funding |
| Hugging Face | USA | Hub | 2.5M models, 13M users, 1/3 Fortune 500 |

## Where Closed Still Leads

1. **Integrated harness** — no open model in verified top tier of Terminal-Bench 2.1
2. **Long-context fidelity** at 1M tokens (Gemini 3: 89% vs DeepSeek V4-Pro: 41%)
3. **Turnkey compliance** (SOC 2, HIPAA, zero data retention by default)
4. **Accountability** — a counterparty the customer can hold liable
