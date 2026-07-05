---
title: "Microsoft"
type: entity
created: 2026-04-29
updated: 2026-07-05
tags:
  - company
  - infrastructure
  - cloud
  - model
aliases: ["Microsoft Corporation", "MSFT", "Microsoft AI"]
sources:
  - raw/newsletters/2026-04-28-openai-breaks-free-from-microsoft.md
  - raw/articles/2026-06-03_microsoft-mai-thinking-1-tech-report.md
---

# Microsoft

| | |
|---|---|
| **Type** | Technology Corporation |
| **Founded** | 1975 |
| **Leadership** | Satya Nadella (CEO) |
| **Key Products** | Azure, Copilot, GitHub, Windows, Office 365, MAI Models |
| **Website** | [microsoft.com](https://microsoft.com) |
| **Cloud** | Azure (2nd largest cloud provider) |

## Overview

Microsoft is a global technology corporation and the second-largest cloud provider (Azure). Historically known for Windows and Office, Microsoft has pivoted heavily toward AI infrastructure and enterprise software through its partnership with OpenAI and its Copilot product line. In 2026, Microsoft deepened its internal AI research with the **Microsoft AI (MAI)** team developing frontier reasoning models.

## OpenAI Partnership & Azure Exclusivity (2019–2026)

Microsoft was OpenAI's primary strategic partner and exclusive cloud distribution provider for years. The partnership included:
- **Investment**: Billions in funding rounds for OpenAI
- **Azure Integration**: OpenAI models exclusively distributed via Azure
- **Copilot**: AI features built on GPT models across Microsoft's product suite

### Partnership Renegotiation (Apr 2026)

In April 2026, Microsoft and OpenAI renegotiated their partnership, ending the exclusive distribution arrangement:

**Key Terms:**
- **Multi-Cloud Access**: OpenAI can now sell directly on AWS, Google Cloud, and Oracle — ending Microsoft's monopoly on OpenAI model distribution
- **IP License**: Microsoft retains a nonexclusive license to OpenAI IP through 2032
- **Revenue Share**: Microsoft receives a guaranteed 20% revenue share through 2030 (now subject to a cap)
- **Azure Model Resale**: Microsoft no longer pays OpenAI a revenue share for reselling models on Azure
- **AGI Clause Scrapped**: The controversial "AGI escape clause" (which could have allowed OpenAI to stop payments upon reaching AGI) replaced with fixed timelines

**Strategic Implications:**
- Microsoft gains financial certainty and freedom to focus on internal AI models (Copilot strategy)
- OpenAI gains enterprise reach across all major cloud platforms
- Anthropic captured over 30% of API market share during this period, pressuring OpenAI's position

See [[entities/openai]] for OpenAI's perspective on the renegotiation.

## Internal AI Research: Microsoft AI Team (MAI)

Microsoft has been building its own in-house AI research division, the **Microsoft AI (MAI) Team**, responsible for developing frontier reasoning models:

- **MAI-Thinking-1** (June 2026): A 35B active / 1T total parameter MoE model designed as a "hill-climbing machine" for STEM reasoning and coding. Uses reinforcement learning to iteratively improve capabilities.
- **MoE Architecture Exploration**: Research into sparse expert-based architectures for large-scale modeling.

See [[entities/microsoft-ai-team]] for the full Microsoft AI Team profile.

## AI Safety & Government Contracts (Apr 2026)

Microsoft continues to participate in the broader AI governance conversation. Meanwhile, competitor Google signed a classified Pentagon AI deal despite internal protests from 600+ employees (reversing Google's 2018 Project Maven exit). Anthropic remains a holdout on classified military contracts, leading the Pentagon to designate them a "supply chain risk."

## Related Entities
- [[entities/openai]] — Strategic partner, now multi-cloud
- [[entities/microsoft-ai-team]] — Internal AI research division
- [[entities/mai-thinking-1]] — MAI flagship reasoning model
- [[concepts/ai-agent-engineering]] — Copilot integrates agent architectures
- [[concepts/serving-llms-vllm]] — Azure hosts vLLM inference infrastructure

## Sources
- **OpenAI-Microsoft Renegotiation Report (2026-04-28)** — Beehiiv newsletter digest
- **Market Analysis: NVIDIA GPU dominance** — ~20M B200/B300 GPUs installed by Q4 2025, Azure is a major consumer
- **MAI-Thinking-1 Technical Report (June 2026)** — Microsoft AI

## References

- devblogs.microsoft.com--oldnewthing-20260427-00--f99d4946
- devblogs.microsoft.com--oldnewthing-20260428-00--7333bbac
- crawl-2026-04-24-microsoft-red-teaming-agents
