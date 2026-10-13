---
title: "SmithDB — Purpose-Built Datastore for Agent Traces"
tags:
  - infrastructure
  - ai-agents
  - developer-tooling
sources:
  - "[[raw/articles/langchain-smithdb-agent-trace-datastore-2026-10]]"
created: 2026-10-13
updated: 2026-10-13
type: concept
---

# SmithDB — Purpose-Built Datastore for Agent Traces

## Definition

SmithDB is a **columnar datastore purpose-built by LangChain for agent trace data**, created because LangSmith's previous store (ClickHouse) could not serve agent trace workloads. Official description: "an optional columnar datastore built for agent trace data: deeply nested spans, multi-modal content, and spans that stay open for hours." Available opt-in on LangSmith 0.17+ (ClickHouse is required on 0.16 and remains the default on 0.17; **ClickHouse support ends in LangSmith v0.19**).

## Why a general-purpose DB wasn't enough

Sarah (@sarahfim, Composio) highlighted this in a follow-up comment on her agent-tracing piece: LangChain "needed to invent an entirely new database, SmithDB, for LangSmith to accommodate agent traces," because of five workload properties:

| Property | Traditional traces (APM) | Agent traces |
|----------|--------------------------|--------------|
| Nesting | Few flat parent/child spans | **Hundreds of nested spans per trace** (LLM call → tool → subagent) |
| Payload | KB-scale metadata | **Huge prompts and tool outputs**, multi-modal content; one conversation can be megabytes across dozens of runs |
| Lifecycle | Spans close when the request ends | **Runs that stay open for hours** (long-running agents) |
| Data arrival | Complete shortly after the request | **Events that keep arriving over time** (append continues) |
| Queries | Time range + metadata filters | **Full-text search + JSON key-path filtering + trajectory queries + random access to individual runs** |

ClickHouse is a general OLAP columnar DB; the combination of "append-growing deeply nested documents queried by full-text and JSON paths" fits neither classic OLTP nor classic OLAP designs. That is the structural reason a new database was needed.

## Architecture

- Durable data lives in **object storage** (S3/GCS/Azure Blob) with a **per-pod disk cache**.
- Self-hosted deployment is "three stateless components on object storage and Postgres. No local disks or complex sharding" (PostgreSQL serves as a dedicated metastore).
- Runs alongside ClickHouse during migration: dual ingestion → validate → switch queries → backfill history.
- Vendor benchmark claims: trace query 860ms → 71ms (12x); thread query 1.16s → 131ms (9x); full-text search 15x.

## LangSmith features that require SmithDB

Trajectory view (deduplicated conversation across turns, model calls, tools, subagents), trajectory evaluators, `field:value` filter query syntax, the current custom dashboard chart editor, threads in annotation queues/datasets, thread automation rules, public thread sharing, large-trace actions (paginated trace tree, whole-trace JSON export), LLM Gateway usage dashboards. In other words, **product development itself was blocked by the old datastore** — the new features could not be built on ClickHouse.

## Analysis

- A textbook case of **workload diversity forcing a new database category** — the same narrative as vector databases. AI observability generates data shapes (huge payloads + deep nesting + long-lived mutable spans + search-oriented queries) that existing storage engines were not designed for. Pairs with Braintrust's Brainstore as the second documented instance of the "AI observability is a database problem" thesis (see [[concepts/ai-observability]]).
- In the context of sarahfim's anti-slop software factory article, it underscores a **hidden infrastructure cost of scaling agent teams**: as contributor counts (and their agents) grow, trace volume explodes, and the observability layer must be re-architected just like lint rules and CI are.
- Caveats: benchmark numbers are vendor marketing claims without independent verification; "entirely new database" here means a custom columnar/trace engine on object storage with Postgres as metastore — a re-design of the storage hierarchy rather than a from-scratch storage engine in the vintage sense.

## Related Pages

- [[concepts/ai-observability]] — parent concept; includes the Brainstore "database problem" argument
- [[concepts/agent-trace-integrity]] — trace fidelity/auditing
- [[concepts/coding-agents/lint-rules-as-agent-feedback-loop]] — sarahfim's anti-slop factory article (source of the comment)
- [[entities/composio]] — sarahfim's employer
