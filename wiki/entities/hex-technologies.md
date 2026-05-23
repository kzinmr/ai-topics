---
title: "Hex Technologies"
type: entity
created: 2026-05-08
updated: 2026-05-23
tags:
  - company
aliases: ["Hex", "Hex Tech"]
sources:
  - https://hex.tech
  - raw/articles/2026-05-23_hex-technologies_evaluate-data-agents.md
---

# Hex Technologies

Hex is an AI analytics platform that combines collaborative notebooks, conversational self-serve analytics, and data apps in one connected workspace. It unifies the traditionally fragmented data stack — notebooks, BI, and dashboards — with AI woven throughout.

| | |
|---|---|
| **Type** | AI Analytics Platform |
| **Founded** | 2020 |
| **Leadership** | Barry McCardel (Co-Founder & CEO), Caitlin Colgrove (Co-Founder & CTO), Glen Takahashi (Co-Founder & Chief Architect) |
| **Key Products** | Hex platform (agentic notebooks, conversational analytics, Context Studio, Hex CLI) |
| **Website** | [hex.tech](https://hex.tech) |
| **Tech Blog** | [hex.tech/blog](https://hex.tech/blog) |

## Key Facts
- Founded in 2020 by former Palantir engineers frustrated with fragmented data tools.
- Raised $70M in May 2025; total funding ~$172M.
- Trusted by Reddit, StubHub, HubSpot, Cisco, Figma, Anthropic, Rivian, and the NBA.
- Acquired Hashboard (BI platform) to expand analytics capabilities.

## Products & Technology
- **Agentic Notebooks**: Polyglot notebooks (SQL, Python, R) with a built-in AI agent for deeper analysis.
- **Conversational Self-Serve**: Business users ask questions in plain language against a shared semantic layer.
- **Context Studio**: AI governance and semantic models for trusted, consistent answers.
- **Hex CLI**: Terminal-based analytics control.
- Graph-based execution model for reproducibility at scale.



### Repos as Agent Context (May 2026)

Hex added the ability to attach Git repos to workspaces, enabling the Hex Agent to analyze dbt models and application code. This bridges the gap between data warehouse context and code-level understanding.

- **dbt repo use case**: Self-service users can query high-level tables while the agent crawls upstream dbt logic to understand filtering, collapsing, and category definitions
- **Application repo use case**: Answers questions about tracking implementation, untracked events, and how features relate in the codebase
- **Compounding context**: Repos, projects, warehouse metadata, guides, and semantic models are synthesized by the agent to answer questions that previously only the data team could address
- **Customers**: Underdog (Camden Willeford), Stubhub (Alan Peters) report significantly improved ability to handle "nebulous" queries

Authored by Andrew Lee (May 15, 2026).



## Data Agent Evaluation Lab (Shoebox)

In May 2026, Hex engineer Izzy Miller detailed how Hex evaluates data agents with a custom internal lab called **Shoebox** — originally a hacky trace viewer, evolved into a full-fledged agent observability and evaluation platform.

### Shoebox Architecture

- **Pairwise experiment model**: Every evaluation is designed as a pairwise comparison between a "candidate" run and a "baseline" run, not a standalone test. This biases teams to report treatment matrices and side-by-side trajectories rather than aggregated numbers in isolation.
- **Local + remote hybrid**: Shoebox runs as part of the local Hex dev stack but connects to a shared internal Hex workspace where eval sets run daily to establish "production baselines." Engineers compare locally-executed candidate runs against remotely-executed baselines, with painstaking care to sync environments for apples-to-apples comparison.
- **Custom rubric system**: Core eval sets ship with preconfigured rubrics (ToolEfficiency, SemanticLayerUsage, WorkspaceGuideAdherence) and ground truths. Anyone can configure deterministic, LLM-judged, or hybrid rubrics. Run-scoped "hypothesis objective" rubrics allow pairwise evaluation specific to a single experiment — these consider candidate and baseline trajectories side-by-side at judge time, with access to post-run metadata for speed/cost evaluation.
- **Auto-research loop**: Shoebox exposes agent skills that let coding agents experiment against evals in an auto-research-like loop.

### Shorelane Commerce — Synthetic Evaluation Business

Hex created a fully synthetic B2B2C office-supplies platform called **Shorelane Commerce** to serve as a realistic evaluation environment:

- **Scale**: ~$129M yearly revenue, three revenue streams (direct-to-consumer, business subscriptions with net-30 terms, third-party marketplace with 15-25% cut)
- **Realistic data debt**: Migrated platforms in 2021 losing customer IDs, acquired a competitor (never fully merged data), renamed a sales channel in 2022 without backfilling, restructured plans in 2023 with grandfathered customers, five columns that could plausibly be called "revenue"
- **Source systems**: Stripe, Salesforce, legacy Shopify (mostly red herring), three ad platforms with different conversion totals
- **30,000 lines** of handcrafted data generators, dbt models, warehouse documentation, events, triggers, and stakeholder personas producing six years of realistic data across millions of rows and dozens of tables
- **Evals look like**: "How many support refund requests in the last 30 days haven't been processed yet?" rather than contrived prompt tricks

### Key Design Decisions

- **No eval-reality drift**: Shoebox integrates deeply with the actual Hex application — product improvements automatically take effect in evaluations
- **LLM judge calibration challenges**: Hex biases toward being overly harsh, but struggles with calibration (e.g., a 0.01pp difference accepted 35% of the time by the LLM judge)
- **Environment sync is the hardest problem**: Maintaining consistent eval environments across local dev, shared baselines, and production configs requires a careful maze of export/reset scripts

Authored by Izzy Miller, Engineering (May 22, 2026).


## Related
- [[entities/anthropic]] — customer using Hex for data analytics
- [[entities/palantir]] — founders' previous employer
- [[concepts/data-notebooks]] — notebook paradigm evolution
