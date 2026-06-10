---
title: Gemini 3.5 Flash
created: 2026-05-22
updated: 2026-05-23
type: entity
tags:
  - entity
  - model
  - google
  - multimodal
  - text-generation
  - agentic-engineering
  - inference
  - agent-sdk
  - coding-agents
  - ai-agents
  - orchestration
  - multi-agent
sources:
  - raw/articles/2026-05-19_google-gemini-3-5-flash.md
  - https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/
  - https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/
  - https://ai.google.dev/gemini-api/docs/antigravity-agent
  - raw/newsletters/2026-05-23-ainews-all-model-labs-are-now-agent-labs.md
---

# Gemini 3.5 Flash

Google DeepMind's frontier model combining intelligence with action. Announced May 19, 2026 at Google I/O. The 3.5 Flash variant leads the Gemini 3.5 family, with 3.5 Pro coming in June 2026.

## Overview

Gemini 3.5 Flash delivers **frontier-level intelligence at Flash-series speed** — 4× faster output tokens per second than other frontier models, while outperforming [[concepts/gemini/index]]-3-1-flash-lite|Gemini 3.1 Pro]] on all major agentic and coding benchmarks. It lands in the top-right quadrant of the Artificial Analysis Index, eliminating the quality-latency tradeoff.

## Key Benchmarks

| Benchmark | Score | vs Previous Best |
|---|---|---|
| Terminal-Bench 2.1 (agentic CLI) | 76.2% | Outperforms Gemini 3.1 Pro |
| GDPval-AA (agentic coding) | 1656 Elo | Outperforms Gemini 3.1 Pro |
| MCP Atlas (tool-use protocol) | 83.6% | Outperforms Gemini 3.1 Pro |
| CharXiv Reasoning (multimodal) | 84.2% | — |
| Cost vs Frontier | <50% | For long-horizon tasks |

## Antigravity Harness

The updated **[[entities/google-antigravity|Antigravity harness]]** powering Gemini 3.5 Flash enables **collaborative subagents** for enterprise-scale multi-step workflows under supervision. Antigravity is Google's agent-first development platform with desktop (Antigravity 2.0), CLI, and SDK surfaces — all sharing the same harness powering [[concepts/gemini/spark|Gemini Spark]] and AI Mode in Search.

### Managed Agents in Gemini API

A single API call provisions an isolated Linux sandbox with code execution, file management, and web access. Agents are customized via AGENTS.md and SKILL.md files. **Automatic context compaction** at ~135K tokens enables long-running sessions. Powered by Gemini 3.5 Flash.

Demo scenarios include:

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

**[[concepts/gemini/spark|Gemini Spark]]** is a 24/7 personal AI agent running on Gemini 3.5 Flash, powered by the Antigravity harness. Cloud-based — continues working even when the user closes their laptop. Deeply integrated with Workspace (Gmail, Docs, Slides). Supports:

- **Recurring tasks**: "Flag hidden subscription fees in monthly credit card statements"
- **Teach new skills**: Custom workflows like school update digesting
- **Complete workflows**: Meeting notes → polished Docs → companion emails
- **Upcoming**: Text/email Spark, custom sub-agents, local browser operation (summer 2026)

Rolling out to Google AI Ultra subscribers (US).

## Safety

Developed under Google's [[concepts/frontier-safety-framework|Frontier Safety Framework]]. Strengthened cyber and CBRN safeguards. Uses **interpretability tools** to check inner reasoning before response generation.

## Tiered Thinking

Gemini 3.5 Flash introduces a **tiered thinking system** with four configurable levels:

| Level | Description | Use Case |
|-------|-------------|----------|
| **Minimal** | Fastest, no explicit reasoning | Simple queries, high-throughput |
| **Low** | Brief reasoning pass | Routine coding, data processing |
| **Medium** | Balanced reasoning depth | Complex debugging, architecture decisions |
| **High** | Maximum deliberation | Multi-step agentic workflows |

This allows developers to trade latency for reasoning depth on a per-request basis, rather than switching between different model sizes.

## Pricing

| Metric | Price |
|--------|-------|
| Input tokens | $1.50 / 1M tokens |
| Output tokens | $9.00 / 1M tokens |

Approximately 4× faster output than competing frontier models at competitive pricing. For long-horizon agentic tasks, the cost is <50% of other frontier models.

## Availability

- Google Antigravity, Gemini API, Google AI Studio, Android Studio
- [[concepts/gemini/enterprise-agent-platform|Gemini Enterprise Agent Platform]] and Gemini Enterprise
- Gemini app and AI Mode in Search (billions of users)
- Now **Generally Available** (GA) as of May 2026
- Coming: Gemini 3.5 Pro (internal use already, public June 2026)


## Mixed Reception & Eval Critique (May 2026)

While Gemini 3.5 Flash shows strong benchmark gains — ranking **16th on Design Arena** (+16 positions) with GDPval improvements — the reception among builders is mixed:

- **@jeremyphoward critique**: The model feels *"optimized for evals, not cooperating with humans"* — suggesting benchmark-focused improvements came at the cost of real-world usability
- **Higher cost than expected**: Despite the "Flash" branding implying affordability, some builders report the real-world cost is significantly higher than claimed benchmarks suggest
- **Benchmark-vs-Reality gap**: The strong eval improvements don't translate proportionally to practical coding or agentic workflows

This pattern echoes broader concerns about benchmark specialization in the model industry, where eval optimization can diverge from human-aligned improvement.

> Source: [AINews May 23, 2026](https://www.latent.space/p/ainews-all-model-labs-are-now-agent)

## Related

- [[concepts/gemini|Google Gemini]] — broader Gemini model family
- [[concepts/gemini/enterprise-agent-platform|Gemini Enterprise Agent Platform]]
- [[concepts/gemini/index]]-3-1-flash-lite|Gemini 3.1 Flash-Lite]]
- [[concepts/coding-agents|Coding Agents]]
- [[concepts/ai-agents|AI Agents]]
- [[concepts/agentic-engineering|Agentic Engineering]]
