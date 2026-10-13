# LangChain SmithDB — dedicated datastore for agent traces

- Collected: 2026-10-13
- Source: LangChain official site + docs (https://www.langchain.com/langsmith, https://docs.langchain.com/langsmith/self-host-smithdb)
- Trigger: Sarah (@sarahfim) follow-up comment on X Article "How to build an anti-slop software factory for teams of 30+" (2026-10-13):
  > While we're talking about agent tracing, I couldn't help but mention that @LangChain needed to invent an entirely new database, SmithDB, for LangSmith to accommodate agent traces.
  > Why? hundreds of nested spans per trace; huge prompts and tool outputs; runs that stay open for hours; events that keep arriving over time; full-text search + JSON filtering

## Official description (docs.langchain.com/langsmith/self-host-smithdb)

"SmithDB is a columnar datastore built for agent trace data: deeply nested spans,
multi-modal content, and spans that stay open for hours. It keeps durable data in
object storage with a per-pod disk cache, and serves LangSmith trace ingestion and
queries alongside the existing ClickHouse datastore."

- Opt-in on LangSmith 0.17+ (ClickHouse is required on 0.16 and remains default on 0.17).
- ClickHouse support ends in LangSmith v0.19.
- Architecture: durable data in object storage + per-pod disk cache; self-host = "three
  stateless components on object storage and Postgres. No local disks or complex sharding."
  (needs a dedicated PostgreSQL metastore + object storage + cache disk)

## Marketing claims (langchain.com/langsmith SmithDB section)

- "Agent traces are deeply nested with heavy payloads. A single conversation can generate
  megabytes of data across dozens of runs and tool calls. General-purpose databases can
  store trace data, but weren't designed for the way teams query it. SmithDB is
  purpose-built for agent observability."
- Built for agent query patterns: random access on individual runs, full-text search,
  JSON key-path filtering, trajectory queries.
- Sub-second performance across millions of traces.
- Benchmark claims: Trace query 860ms -> 71ms (12x); Thread query 1.16s -> 131ms (9x);
  Full-text search 15x.

## Features that REQUIRE SmithDB (docs: self-host-smithdb-features)

Filter query syntax (`field:value`), current custom dashboard chart editor, Trajectory
view (deduplicated conversation across turns/model calls/tools/subagents), trajectory
evaluators, threads in annotation queues / datasets, thread automation rules, public
thread sharing, large trace actions (paginated trace tree, whole-trace JSON download),
LLM Gateway usage dashboards, agent trace volume charts, feedback in bulk exports.
