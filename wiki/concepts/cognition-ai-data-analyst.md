---
title: "Cognition AI Data Analyst — Turning Devin into a Data Analysis Agent"
type: concept
aliases:
  - cognition-data-analyst
  - devin-data-analyst
  - ai-data-analyst-pattern
created: 2026-04-13
updated: 2026-05-26
tags:
  - concept
  - cognition
  - coding-agents
  - data-science
  - mcp
  - ai-agent-engineering
status: complete
sources:
  - https://devin.ai/ai-data-analyst-1
  - https://devin.ai/ai-data-analyst-2
  - https://cognition.ai/blog/how-cognition-uses-devin-to-build-devin
related:
  - code-execution-with-mcp
  - cognition-devin-philosophy
  - closing-agent-loop
---

# Cognition AI Data Analyst — Turning Devin into a Data Analysis Agent

An approach advocated by the Cognition team for leveraging AI software engineers (Devin) as 24/7 on-demand data scientists. Rather than an SQL-only tool, this is an integrated agent design combining **codebase-level context understanding + data analysis + visualization.**

## Core Insight

> "Previously, knowledge fragmentation made it extremely difficult to trace data anomalies back to their source... Getting answers often took days or weeks. Now, it takes minutes."

> "If you assume that every question would take an hour to answer, we estimate that it would take a data team **150+ hours per month** to do this work manually. With Devin, we can do it in minutes."

## Why Use an AI Software Engineer for Data Analysis?

The decisive difference from SQL-only tools: **Devin understands the complete lineage of data.**

| Capability | SQL-Only Tool | Devin (AI Software Engineer) |
|---|---|---|
| Data exploration | Only materialized table results | Searches product code, instrumentation events, ETL pipelines, final transformations |
| Context retention | Reset per session | Learns company/product-specific knowledge across sessions |
| Self-verification | Human-performed | Executes SQL and validates results against live data |
| Async collaboration | Synchronous query execution | Iterative workflow (query → verify → visualize → discuss) |
| Output verifiability | Results only | Presents final SQL query + dashboard link + visualization |

## Architecture: MCP + Knowledge

### Role of MCP (Model Context Protocol)

MCP serves as a secure, standard bridge between Devin and external data services:

- **Secure access:** Connects to data warehouses without exposing credentials
- **Schema exploration:** Maps table structures, relationships, and data types
- **Query execution:** Runs SQL with appropriate permissions
- **Result processing:** Formats/outputs in agent-optimized form
- **Autonomous tool selection:** Devin automatically decides which MCP tools to use when. No manual workflow definitions needed

### Built-in MCP Support

Pre-configured MCP tools in Devin:

- **Google's MCP Toolbox for Databases** — Standard inclusion
- **Supported databases:** PostgreSQL, Firestore, Looker, SQL Server
- **Metabase MCP Server** (open-source) — 80+ tools (DB exploration, dashboards, cards, queries)
- **Long-tail DBs:** Manually inject credential files (`Modify repo setup`)

## Knowledge Configuration — Designing the Agent's "Prior Knowledge"

The most critical factor determining Devin's data analysis accuracy. Shared context templates across the team:

### Knowledge Configuration Components

1. **Purpose:** Define the agent's role (e.g., "Querying Redshift Data Warehouse")
2. **Guidelines:** Data access priorities and exploration procedures
3. **Output Format:** Enforce human-verifiable output formats
4. **Macro:** Shortcuts like `!analytics` for instant team-wide invocation

### Key Configuration Template Patterns

```markdown
## Purpose:
Clearly state the query target and agent's role

## Guidelines:
- Fetch the complete DB schema first (`database://structure`)
- Reference analytics repo README/docs.yml
- When in doubt, read analytics repo code to check column computation methods
- **Prefer mart models** (no int_/stg_ prefixes)
- **Prefer analytics schema** (before billing/raw schemas)
- If uncertain, ask the user. Present candidate tables for selection

## Output Format:
- Always display the final query alongside results (human-verifiable)
- Generate Metabase Playground links (`get_metabase_playground_link`)
- Present single-number results prominently
- Charts/tables in markdown format
```

## Data Structure Prerequisites

> "Having a legible and structured data setup is strongly recommended for using Devin as an AI data analyst. It's impossible for anyone, let alone an AI, to understand your data if it's not structured in a way that's easy to parse and understand."

**Requirements:**
- **Infrastructure as Code:** Version-control data models and pipelines with DBT
- **Pre-mapping:** Document data flows, models, and databases
- **Read-only:** Restrict production DB to read-only user credentials

## Practical Workflow

```
User (Slack) → "!analytics What's our conversion rate by industry?"
                        ↓
                   Devin (connects to DB via MCP)
                        ↓
              Schema exploration → identify appropriate mart model
                        ↓
              SQL generation → execution → result validation
                        ↓
              Visualization generation + final SQL presentation + Metabase link
                        ↓
User ← Verifiable answer (numbers + charts + SQL + links)
```

## Cognition's Data Analysis Agent Design Principles

1. **Software Engineer > SQL Tool:** An agent with codebase-level context understanding yields deeper insights than a dedicated tool looking only at table results
2. **Verifiable Outputs:** Always present the final SQL. Output in a human-verifiable, reusable format
3. **Knowledge as Infrastructure:** Macro-enabled Knowledge configuration acts as a team-wide accelerator
4. **Self-Correction Loop:** The agent executes its own queries and validates results (the data analysis version of closing the agent loop)
5. **Progressive Disclosure:** Explore in priority order: mart models → intermediate models → raw data
6. **Async-First:** Fire-and-forget via Slack. Agents processing 24/7

## Connections to Related Cognition Philosophy

- [[concepts/closing-agent-loop]] — Write→Catch→Fix→Merge loop. Data analysis version: Query→Validate→Visualize→Report
- [[concepts/harness-engineering/system-architecture/code-execution-with-mcp]] — Pattern exposing MCP as a code API. In data analysis, acts as the SQL execution environment
- [[concepts/cognition-devin-philosophy]] — Single-agent context continuity. Same principle applies to data analysis (explore→analyze→visualize in the same context)
- [[concepts/harness-engineering/system-architecture/ai-memory-systems]] — Knowledge configuration functions as the agent's "file-based memory"

## Business Impact

| Metric | Traditional | Devin |
|---|---|---|
| Question response time | Days to weeks | Minutes |
| Team hours/month | 150+ hours | Minutes × number of questions |
| Knowledge fragmentation | Spread across 5 teams (Product Eng, Data Eng, DS, BI, Finance) | Centralized |
| Output verifiability | Low (black-box process) | High (SQL + links provided) |

## DANA (Data Analyst Agent) — Devin's Dedicated Data Analysis Agent

Within Cognition, Devin's data analysis role has been formalized as **DANA (Data Analyst Agent).**

### Features
- **Access method:** Simply type `/dana` or `@Devin !dana` in Slack
- **Supported DBs:** Redshift, Snowflake, BigQuery
- **Visualization:** Chart generation with Seaborn, dashboard building
- **Target users:** Accessible to non-engineers. Answer ad-hoc questions like "Why did signups drop on Tuesday?" without pulling engineers away

### DANA and Devin Role Division

```
@Devin       → General software engineering (code fixes, PRs, reviews)
@Devin !dana → Data analysis only (queries, visualizations, dashboards)
```

This is a practical example of **Agent Specialization** — defining different Knowledge, MCP, and behavior profiles per role on the same agent foundation.

### Related
- [[concepts/harness-engineering/agent-patterns]] — Practical examples of agent specialization patterns
- [[concepts/closing-agent-loop]] — Closed-loop specialized for data analysis

## End-to-End Bug Debugging — Merging Data Analysis and Engineering

Cognition has extended DANA's data analysis capabilities to **bug triage and end-to-end fixes.**

### Workflow
1. **Trigger:** Linear's `Bug` label triggers the process
2. **Investigation:** Access Datadog (logs) + read-only DB replica to identify root cause
3. **Trace:** Identify the offending commit from git history
4. **Fix:** Code fix + create regression tests
5. **PR:** Auto-open a pull request

### Key Connections

This workflow demonstrates the **integration** of data analysis agents and software engineering agents:

```
Data analysis (DANA): Why are numbers off? → Identify code-level root cause
Bug fix (Devin):      Code fix + add tests
```

By completing workflows that traditionally required separate teams (Data + Engineering) on a single agent foundation, **lead time from cause discovery to fix is dramatically shortened.**

### Technical Foundation
- Datadog integration (via MCP)
- Read-only DB replica (data integrity verification)
- Git history walk (identifying offending commits)
- Playbook (custom system prompt for bug triage)
