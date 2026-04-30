---
title: "db9: Filesystem + SQL Pattern for Agent Workflows"
created: 2026-04-30
updated: 2026-04-30
tags: [concept, database, agent-workflow, filesystem, postgresql, sql]
aliases: ["db9", "fs9", "db9-fs-sql-patterns"]
related: [[concepts/ai-agent-memory-middleware]], [[concepts/zero-disk-architecture]], [[concepts/disaggregated-storage]], [[concepts/agent-loop-orchestration]]
sources: ["https://me.0xffff.me/db9-fs-sql-patterns.html"]
---

# db9: Filesystem + Postgres for Agent Workflows

**db9** is a PostgreSQL distribution (wire-compatible) with compiled-in extensions designed specifically for agentic workloads. It unifies file-based artifacts and relational metadata into a single data layer, using **SQL as the glue** — eliminating the need to split state across object storage, vector databases, and application-level orchestration code.

Core philosophy: **Keep agent artifacts as real files** (logs, markdown, diffs, prompts, traces) and **governance/indexes as Postgres tables**.

Source: [me.0xffff.me/db9-fs-sql-patterns.html](https://me.0ffff.me/db9-fs-sql-patterns.html)

## The Problem db9 Solves

Agent systems accumulate two fundamentally different types of state:

1. **Artifacts (File-shaped):** Prompts, plans, execution traces, cached responses, reports, code diffs — human-readable content that benefits from being stored as real files.
2. **Queryable State (Table-shaped):** Metadata, deduplication keys, chunk indexes, run status, governance records — structured data that benefits from SQL queries.

Traditional architectures split these across separate systems (object storage for files, a database for metadata), requiring complex application-level glue code to keep them in sync. db9 brings them together.

## Key Extensions

### fs9 — Filesystem Integration
- Read/write files directly from SQL queries
- Treat CSV, JSONL, and Parquet files as queryable relations
- No need for separate object storage or filesystem APIs in the agent harness

```sql
-- Write and read artifacts
select extensions.fs9_write('/reports/hello.txt', 'hello from db9');
select extensions.fs9_read('/reports/hello.txt');

-- Query files directly as tables
select * from extensions.fs9('/data/users.csv') limit 5;

-- Filter logs stored in JSONL
select _line_number, line
from extensions.fs9('/logs/run.jsonl')
where line ->> 'level' = 'error';
```

### embedding + vector — Server-side Embedding & Search
- Built-in embedding generation via the `embedding()` function
- `pgvector`-compatible HNSW semantic search
- No separate vector database needed

### http + pg_cron + branching
- Integrated API calls from SQL
- Scheduled tasks via pg_cron
- Safe data experimentation with branching

## The Compact Pipeline (RAG-ish Loop)

### Step A: Source Documentation
Store raw documents directly in the db9 filesystem:
```sql
select extensions.fs9_write('/docs/agents/intro.md', $$ # Content here $$);
```

### Step B: Materialize Chunk Index
Use the built-in `CHUNK_TEXT` function, which is **markdown-aware** and respects natural breakpoints (headings, paragraphs):
```sql
insert into doc_chunks (path, chunk_idx, content, meta)
select '/docs/agents/intro.md', c.chunk_index, c.chunk_text,
       jsonb_build_object('source', 'docs', 'chunk_pos', c.chunk_pos)
from CHUNK_TEXT(
  content => extensions.fs9_read('/docs/agents/intro.md'),
  max_chars => 3600,
  overlap_chars => 540,
  title => 'agents/intro'
) as c;
```

### Step C: Retrieval (FTS & Semantic)

**Full-Text Search:**
```sql
select path, content from doc_chunks
where search_vector @@ plainto_tsquery('english', 'filesystem sql agents')
order by ts_rank_cd(search_vector, plainto_tsquery('english', 'filesystem sql agents')) desc;
```

**Semantic Search (Embeddings):**
```sql
-- Generate and store vectors server-side
update doc_chunks set vec = embedding(content)::vector(1024) where vec is null;

-- Search using cosine distance
select path, content from doc_chunks
order by VEC_EMBED_COSINE_DISTANCE(vec, 'how do agents use filesystem?') limit 8;
```

### Step D: Output Management
Write the final agent response to a file while tracking its metadata in a table for governance:
```sql
-- Write the file
select extensions.fs9_write('/reports/output.md', '# Generated Summary...');

-- Log the artifact metadata
insert into artifacts (path, kind, meta)
values ('/reports/output.md', 'report', '{"inputs":["/docs/agents/intro.md"]}'::jsonb);
```

## Why This Composition Works

| Benefit | Explanation |
|---------|-------------|
| **Transparency** | Files keep artifacts human-inspectable and easy to debug |
| **Structure** | Tables enforce schema and allow complex joins/filtering |
| **Efficiency** | SQL handles the entire workflow (filter, join, rank, dedup) close to the data, reducing latency |
| **Observability** | "Why did the agent do that?" becomes a standard SQL query rather than searching through disparate logs |
| **Simplicity** | One database replaces the typical stack of object storage + vector DB + application glue code |

## Relationship to Other Patterns

- **[[concepts/ai-agent-memory-middleware]]**: db9はエージェントのL3（クラウド/共有ストレージ）層における**ローカル統合パターン**。Memory MiddlewareがカバーするS3 Files（ステージ＆コミットモデル）やTigris（グローバル分散）とは対照的に、db9は単一PostgreSQLノード内で完結する軽量アプローチ。エージェントのメモリ層（episodic/semantic/personal）を「fs9=episodicファイル + SQLテーブル=semanticメタデータ」として自然に表現できる。
- **[[concepts/zero-disk-architecture]]**: 両者ともストレージレイヤの単純化を提唱するが、**真逆の方法論**。Zero Diskは「計算をS3にオフロード（完全分離）」、db9は「計算とデータを1つのPostgreSQLに再統合」。Zero Diskが大規模DBベンダー向けなら、db9は個々のエージェント開発者向け。
- **[[concepts/disaggregated-storage]]**: db9は「再統合（re-aggregated）」アプローチ。分離がもたらす複雑性を避け、エージェントワークロードには単一ノードで十分と判断。
- **[[concepts/agent-loop-orchestration]]**: db9はRAGパイプラインのデータ層を提供（source → chunk → retrieve → generate → outputの全工程をSQLで完結）。

## Key SQL Patterns Summary

```sql
-- The db9 unified pattern in one line:
-- Files = artifacts (human-readable), Tables = governance (machine-queryable), SQL = glue
```

## Sources

- [db9: Filesystem + Postgres for Agent Workflows](https://me.0ffff.me/db9-fs-sql-patterns.html) — me.0xffff.me
