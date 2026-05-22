---
title: "Harvey"
type: entity
created: 2026-05-08
updated: 2026-05-22
tags:
  - security
  - company
  - ai-adoption
  - model
aliases:
  - "Harvey Agentic SOC" ["Harvey AI", "Counsel AI Corporation"]
sources:
  - https://www.harvey.ai/
  - https://www.harvey.ai/blog
---

# Harvey

Harvey is a domain-specific AI platform for the legal and professional services industry. Built on customized large language models, it provides tools for contract analysis, legal research, due diligence, drafting, and end-to-end legal workflow automation for law firms and corporate legal departments.

| | |
|---|---|
| **Type** | AI Platform / Vertical SaaS (Legal) |
| **Founded** | 2022 (San Francisco, CA) |
| **Leadership** | Winston Weinberg (Co-founder & CEO), Gabriel Pereyra (Co-founder & President) |
| **Key Products** | Harvey Assistant, Harvey Vault, Harvey Knowledge, Harvey Workflow Agents, Harvey Mobile, Contract Intelligence |
| **Website** | [harvey.ai](https://www.harvey.ai) |
| **Blog** | [harvey.ai/blog](https://www.harvey.ai/blog) |
| **Tech Blog** | [harvey.ai/blog](https://www.harvey.ai/blog) |

## Key Facts

- Founded by Winston Weinberg (former O'Melveny litigator) and Gabriel Pereyra (former DeepMind/Google Brain research scientist)
- One of the first recipients of investment from the OpenAI Startup Fund
- Valuation reached $8 billion by October 2025; backed by Sequoia, Andreessen Horowitz, GV, Kleiner Perkins, Coatue
- Adopted by 100,000+ lawyers across 1,400+ customers in 60 countries; 60%+ of AmLaw 100 firms
- Revenue reached ~$190M in 2025

## Products & Technology

Harvey's platform includes: Assistant for document Q&A and drafting, Vault for secure document storage and bulk analysis, Knowledge for complex legal research, and Workflow Agents for end-to-end legal task execution (e.g., due diligence, compliance reviews). Named after Harvey Specter from the TV show *Suits*. Integrates with law firm workflows and existing practice management tools.



## Agentic Security Operations Center (May 2026)

Harvey's security team, led by **Mike Parowski**, built an agentic SOC — a system of always-on AI agents that hunt, triage, investigate, author detections, and learn from one another. Built on a persistent, machine-readable **security world model** of Harvey's threat surface.

### Architecture

- **Security world model**: Petabytes of historic data, ~5,300 persistent memories, 2,500+ investigations/30 days, 400+ production detections. Comprises: (1) a raw analytics corpus (TBs/day telemetry in optimized ClickHouse tables), (2) an MCP server via RunReveal for agent-accessible tools, (3) a threat model system prompt structured as paths to crown jewels, (4) a self-improving intelligence layer of hunting/alerting agents.
- **Data layer first**: Semantically-enriched, column-pruned ClickHouse tables with normalized fields (e.g., `isProdCluster` derived from raw JSON). "Invest in your log warehouse before you invest in your agents" — the difference between 200ms and 2s per query is the difference between 3 and 30 hypotheses explored.
- **Round-the-clock operation**: Daily reports (alert volume, detection performance), hourly alert triage (semantic clustering + auto-escalation), threat-watch workflow ingesting CISA KEV and cross-referencing against deployed coverage.
- **Persistent memory**: Postgres-backed knowledge base with categorized facts (entity, finding, baseline), TTLs, Jaccard dedup, per-profile injection budgets. Human analyst annotations persist as agent memories with `source='analyst'`.

### Results
- Coverage expanded from 75 → **400+ deployments** (5.7x increase)
- Weekly alert volume reduced from ~300,000 → **~20,000** (95% reduction)
- CVE/breach response from hours/days → **minutes** (one-button push investigation)
- Detection pipeline uses four-phase agent pipeline: research → consolidate → validate → finalize with human review on every PR

### Design Principle
The agentic SOC operates on top of Harvey's trust boundary, separate from Spectre (product agent platform), to prevent privilege escalation — SOC knowledge of detections/internal topology is isolated from product agent access.


## Related

- [[entities/openai]] — early investor via OpenAI Startup Fund; built on GPT technology
- [[entities/voyage-ai]] — partnered to build custom legal embedding models
- [[entities/anthropic]] — competitor in the enterprise AI deployment space
- [[entities/hebbia]] — serves overlapping legal/financial professional services customers
