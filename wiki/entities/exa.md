---
title: "Exa"
type: entity
created: 2026-05-22
updated: 2026-07-08
tags:
  - company
  - search
  - ai-agents
  - platform
  - infrastructure
aliases:
  - "Exa AI"
  - "Exa Labs"
sources:
  - https://exa.ai/
  - https://exa.ai/about
  - raw/newsletters/2026-05-22-ainews-new-ai-infra-unicorns-exa.md
---

# Exa

**Exa** is an applied AI lab building AI-native search infrastructure for the agentic era — a "search engine for AI agents." It provides a comprehensive search API purpose-built for agentic workloads, powering search for Cursor, Cognition, HubSpot, OpenRouter, Monday.com, and over 400,000 developers.

| | |
|---|---|
| **Type** | AI Search Infrastructure / Applied AI Lab |
| **Founded** | ~2023 |
| **Co-founders** | Will Bryk (CEO), Jeff Wang |
| **Key Products** | Search API, Contents API, Deep API, Agent API, Monitors, Exa Connect |
| **Index Size** | 500B+ webpages |
| **Valuation** | $2.2B (May 2026) |

## Key Facts

- Raised **$250M Series C at $2.2B valuation** (May 2026)
- Positions as **search lab for AI agents** — search infrastructure purpose-built for agentic workloads
- Powers search for [[entities/cursor]], [[entities/cognition]], HubSpot, OpenRouter, Monday.com
- Trains SOTA embedding models on custom **H200 cluster** (exa-cluster)
- Advisors include **Tal Broda** (former VP of Compute, OpenAI) and key Google/Bing researchers
- Competes alongside turbopuffer and Weaviate in AI-native search infrastructure

## Founders

### Will Bryk (CEO)
Will was one of the first engineers at Cresta, building real-time AI products, after studying CS and Physics at Harvard University.

### Jeff Wang (Co-founder)
Jeff spent 3 years building data and web infrastructure at Plaid after studying CS & Philosophy at Harvard, where he ran a GPU cluster in his dorm room.

## Product Suite

### Search API
The core product — a high-quality search API designed for AI agents. Features include:
- **Neural search** with SOTA embedding models trained on Exa's own H200 cluster
- **Content retrieval** with token-efficient output (90% token reduction vs raw HTML)
- **Structured output** via schema definition — agents receive clean JSON rather than raw text
- **Crystal** embedding model for high-quality semantic search

### Contents API
Direct content retrieval from the Exa index — fetch the full text of specific webpages.

### Deep API
Deep research capability — agentic multi-step search that synthesizes information across sources.

### Agent API
A purpose-built search agent API for autonomous AI agents, with configurable effort levels (Auto/Low/Medium/High).

### Monitors
Continuous monitoring API — detect changes across tracked webpages and domains.

### Exa Connect (June 2026)
Access leading data providers through a unified API, expanding Exa from search infrastructure into a data marketplace.

## Technical Architecture

- **Web-scale index**: 500B+ webpages tracked, crawled, and indexed
- **Custom embeddings**: End-to-end neural architectures trained on hundreds of H200 GPUs
- **Token-efficient retrieval**: Highlights API reduces token consumption by ~90% vs raw page content
- **Embedded in agents**: Directly integrated into Cursor's coding agent for search across docs and repos

## Related

- [[entities/turbopuffer]] — Competitor in AI search infrastructure
- [[entities/weaviate]] — Competitor in vector/hybrid search
- [[entities/cursor]] — Customer (powers coding agent search)
- [[entities/cognition]] — Customer (powers Devin)
- [[concepts/agentic-search]] — AI agent search paradigm
