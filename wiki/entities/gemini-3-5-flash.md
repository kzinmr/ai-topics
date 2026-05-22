---
title: Gemini 3.5 Flash
created: 2026-05-22
updated: 2026-05-22
type: entity
tags: [entity, model, google, multimodal, llm, text-generation, agentic-engineering, inference, agent-sdk, coding-agents, ai-agents, orchestration, multi-agent]
sources: [raw/articles/2026-05-19_google-gemini-3-5-flash.md, https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/]
---

# Gemini 3.5 Flash

Google DeepMind's frontier model combining intelligence with action. Announced May 19, 2026 at Google I/O. The 3.5 Flash variant leads the Gemini 3.5 family, with 3.5 Pro coming in June 2026.

## Overview

Gemini 3.5 Flash delivers **frontier-level intelligence at Flash-series speed** — 4× faster output tokens per second than other frontier models, while outperforming [[entities/gemini-3-1-flash-lite|Gemini 3.1 Pro]] on all major agentic and coding benchmarks. It lands in the top-right quadrant of the Artificial Analysis Index, eliminating the quality-latency tradeoff.

## Key Benchmarks

| Benchmark | Score | vs Previous Best |
|---|---|---|
| Terminal-Bench 2.1 (agentic CLI) | 76.2% | Outperforms Gemini 3.1 Pro |
| GDPval-AA (agentic coding) | 1656 Elo | Outperforms Gemini 3.1 Pro |
| MCP Atlas (tool-use protocol) | 83.6% | Outperforms Gemini 3.1 Pro |
| CharXiv Reasoning (multimodal) | 84.2% | — |
| Cost vs Frontier | <50% | For long-horizon tasks |

## Antigravity Harness

The updated **Antigravity harness** powering Gemini 3.5 Flash enables **collaborative subagents** for enterprise-scale multi-step workflows under supervision. Demo scenarios include:

- Paper-to-playable-game synthesis (6 hours, two agents)
- Legacy code migration (messy codebase → Next.js)
- City landscape generation via subagents
- Self-improving game loop (builder + player agents)

## Enterprise Partners (May 2026)

| Partner | Use Case |
|---|---|
| **Shopify** | Parallel subagents for global merchant growth forecasts |
| **Macquarie Bank** | 100+ page document reasoning for customer onboarding |
| **Salesforce Agentforce** | Multi-turn tool calling for enterprise task automation |
| **Ramp** | Multimodal OCR with historical pattern reasoning |
| **Xero** | Autonomous multi-week workflows (1099 forms) |
| **Databricks** | Real-time data monitoring and issue diagnosis |

## Gemini Spark

A personal AI agent running **24/7** on Gemini 3.5 Flash. Takes actions on user's behalf under their direction. Rolling out to Google AI Ultra subscribers (US).

## Safety

Developed under Google's [[concepts/frontier-safety-framework|Frontier Safety Framework]]. Strengthened cyber and CBRN safeguards. Uses **interpretability tools** to check inner reasoning before response generation.

## Availability

- Google Antigravity, Gemini API, Google AI Studio, Android Studio
- [[entities/gemini-enterprise-agent-platform|Gemini Enterprise Agent Platform]] and Gemini Enterprise
- Gemini app and AI Mode in Search (billions of users)
- Coming: Gemini 3.5 Pro (internal use already, public next month)

## Related

- [[entities/google-gemini|Google Gemini]] — broader Gemini model family
- [[entities/gemini-enterprise-agent-platform|Gemini Enterprise Agent Platform]]
- [[entities/gemini-3-1-flash-lite|Gemini 3.1 Flash-Lite]]
- [[concepts/coding-agents|Coding Agents]]
- [[concepts/ai-agents|AI Agents]]
- [[concepts/agentic-engineering|Agentic Engineering]]
