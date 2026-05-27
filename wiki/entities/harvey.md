---
title: "Harvey"
type: entity
created: 2026-05-08
updated: 2026-05-27
tags:
  - security
  - company
  - ai-adoption
  - model
  - agent-evaluation
  - benchmark
aliases:
  - "Harvey Agentic SOC" ["Harvey AI", "Counsel AI Corporation"]
sources:
  - https://www.harvey.ai/
  - https://www.harvey.ai/blog
  - raw/articles/2026-05-26_harvey-ai-initial-results-legal-agent-benchmark.md
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

## Legal Agent Benchmark (LAB) — May 2026

Harvey released the **Legal Agent Benchmark (LAB)**, an open-source benchmark for evaluating AI agents on complex, long-horizon legal tasks. See [[concepts/legal-agent-benchmark]] for full details.

### Key Highlights
- **All-pass grading**: Expert-curated rubrics require every criterion to pass — mirroring strict legal review standards
- **Behavioral traces**: LAB captures agent action sequences (Read → Search → Execute → Write → Validate → Edit) for behavioral analysis
- **Initial results**: Frontier models complete <10% of legal tasks end-to-end (Opus 4.7 leads at 7.1%)
- **Jagged intelligence**: Different models lead different practice areas — GPT-5.5 in research-heavy groups, Opus 4.7 in analytical work, Sonnet 4.6 in structured comparison
- **Cost at frontier**: Opus 4.7 costs ~$50.90/task at ~22 min latency; GPT-5.5 is ~3x cheaper
- **Self-correction is the strongest signal**: Agents that verify AND revise after drafting improve by +1.5 points on all-pass
- **Partnership with Artificial Analysis** for a regularly-updated leaderboard

### Behavioral Findings
- **Positive behaviors**: Thorough research (+0.4), post-draft validation (+0.8), verifying and revising (+1.5), targeted retrieval (+0.3), structured analysis (+0.3)
- **Negative behaviors**: Noisy tool fan-out (-0.5), drafting without review (-1.2)
- Opus 4.7: Most self-corrective (more drafting + validation). GPT-5.5: Heaviest search user (wider document coverage)

## Related

- [[entities/openai]] — early investor via OpenAI Startup Fund; built on GPT technology
- [[entities/voyage-ai]] — partnered to build custom legal embedding models
- [[entities/anthropic]] — competitor in the enterprise AI deployment space
- [[entities/hebbia]] — serves overlapping legal/financial professional services customers
