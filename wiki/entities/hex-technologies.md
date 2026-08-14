---
title: "Hex Technologies"
type: entity
created: 2026-05-08
updated: 2026-08-14
tags:
  - company
aliases: ["Hex", "Hex Tech"]
sources:
  - https://hex.tech
  - raw/articles/2026-05-23_hex-technologies_evaluate-data-agents.md
  - raw/articles/2026-05-10_hex-technologies_notebook-agent-prompting-guide-agentic-analytics.md
  - raw/articles/2026-08-14_hex-technologies_databench-agentic-analytics-benchmark.md
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

### Notebook Agent Prompting Guide (September 2025)

Authored by Alex Brumas (Product), September 24, 2025 (Olivia Koshy was PM of the team that built the Notebook Agent). The guide codifies prompting patterns for Hex's Notebook Agent — an "analytical partner" that knows data-project best practices and is "really good at writing SQL, Python, and configuring viz." The author's framing explicitly transfers vibe-coding learnings (from Lovable, a Hex customer) to agentic analytics.

**Four key capabilities:**
- **Agentic search** — discovers the right data sources without remembering exact table names/schemas (planned: search across docs, projects, components)
- **Building a plan** — translates business questions into a structured analytical approach
- **Executing analysis** — writes and runs code to transform, visualize, and model data
- **Summarizing results** — explains insights in plain language

**Mental models for prompting:**
- **Structured prompting**: Context / Task / Guidelines / Constraints template (e.g., "You are analyzing customer transaction data to help improve marketing targeting...")
- **Conversational prompting**: DM-style prompts that implicitly carry the same structure — fine for most interactions
- **Meta-prompting**: the biggest piece of advice — have the agent craft a concrete plan, critique/refine it, then feed the plan back to the agent for step-by-step execution
- **Scoping context**: deliberately scope the agent with `@` tags — `@customer_transactions` table references or `[@Prophet Model Components Analysis]` cell references focus the agent on the right context
- **Specify analysis methods**: state the model/technique explicitly (e.g., "Build a random forest classifier... using feature importance") or ask for suggestions first, then narrow down
- **Business-impact framing**: tie analysis to decisions (e.g., "which channels to increase investment in for our Q4 campaign planning")
- **Workspace rules file**: organization-level injected context applied to every agent interaction — PII handling, source-of-truth tables, business definitions (MRR, churn, LTV), required analysis patterns (YoY+MoM together, 13-week rolling forecast baseline), data quality warnings (duplicate rows, delayed feeds), stakeholder preferences, industry benchmarks
- **Treat the agent like an expert consultant**, not a code jockey — ask it for advice, industry standards, and technique explanations

**Copy-paste template categories:** data discovery, notebook cleanup & dependency mapping (orphaned/duplicative cell detection), analyzing teammates' work, **cross-project prompt chaining** (have the agent generate a portable context prompt in one notebook, paste it into a new notebook to seed context), and template-replication prompts (k-means/hierarchical clustering, LTV modeling, geospatial viz, EDA, e-commerce KPIs, cohorts, market basket analysis).

Source: raw/articles/2026-05-10_hex-technologies_notebook-agent-prompting-guide-agentic-analytics.md (published 2025-09-24)

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

### DataBench — Agentic Analytics Benchmark (August 2026)

In August 2026, Hex released **DataBench**, a frontier benchmark for agentic analytics built on the Shorelane environment (see above). It addresses the gap between existing analytics benchmarks (which Hex calls "overspecified pub trivia" — e.g., Sonnet 4.5 at 90% on Spider 2.0, Claude Haiku 4.5 at 89% on DABstep) and realistic user prompts, which are vague, directional, and often unanswerable with the available data.

**Design**: 100 realistic analytical tasks (Q&A + open-ended) in the Shorelane Commerce workspace, judged by a GPT-5.6 Sol LLM judge with plain-language rubric briefs (majority of 3 judge runs, 96% agreement). Ten tasks are deliberately crafted "signature traps" with obvious-but-wrong answers.

**Key findings**:
- No model/effort pair scores below 50%; the analytical floor is higher than expected
- **GPT-5.6 Luna** forms the entire pre-elbow of the Pareto frontier — near-Sol performance at ~1/14th the cost
- **Test-time scaling regressions**: unlike coding benchmarks (CursorBench), higher effort can *hurt* — Opus 5 "gets devastated" at xhigh/max, talking itself past correct simple answers
- **Claude Fable 5 is the exception**: only model where scaling effort consistently buys better outcomes (85/100 top score)
- Task breakdown: 75% Q&A, 66% open-ended, 54% traps — the gap is *judgment*, not evidence gathering
- Failure mode: "manufacturing certainty" — Opus 5 at max effort produced 11 minutes of correct arithmetic then promoted correlation into a causal law and wrote a confident (wrong) recommendation

Hex plans to open-source the Shorelane analytical environment (DataBench itself stays private to avoid training contamination). Full details: [[concepts/ai-benchmarks/databench]].

Source: raw/articles/2026-08-14_hex-technologies_databench-agentic-analytics-benchmark.md

### Hex in Codex Integration (June 2, 2026)

Hex launched as an **OpenAI Codex plugin**, enabling Codex users to invoke Hex for analytics without leaving the coding agent. Three integration modes:

- **Kick off analysis from Codex**: Ask a natural language question → Codex invokes Hex → Hex runs the query and returns results (churn by segment, pipeline performance, product usage trends)
- **Pull Hex Threads into Codex**: MCP connection lets Codex pull existing Hex threads as context for reports and meetings — prior work is available without redoing it
- **CLI control**: Programmatic Hex project/cell creation for automated workflows; Codex can also migrate existing BI projects to Hex

Hex's thesis: "Without context, an agent won't use the right data to answer a business question." The integration extends Hex's Context Studio philosophy — when working in Codex, your Hex analyses, data, and context inform whatever you build. Codex admins can enable the plugin in their workspace.

Hex previously launched **Agent, everywhere** (October 2025) with Slack integration and MCP support, allowing the Hex Agent to operate inside Slack, Claude, and Cursor.

Source: raw/articles/2026-06-03_hex-technologies_hex-in-codex.md

## Related
- [[entities/anthropic]] — customer using Hex for data analytics
- [[entities/palantir]] — founders' previous employer
- [[concepts/data-notebooks]] — notebook paradigm evolution
- [[concepts/ai-benchmarks/databench]] — Hex's agentic analytics benchmark (August 2026)
