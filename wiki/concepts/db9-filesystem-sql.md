---
title: "db9 Filesystem + SQL Pattern for Agent Workflows"
type: concept
description: "Agent workflow architecture pattern using PostgreSQL with filesystem extensions (fs9) — files for artifacts, tables for queryable state, SQL as the glue"
category: concepts
sub_category: AI Agent Architecture
tags: [db9, postgresql, filesystem, agent-workflows, RAG, data-architecture]
status: complete
created: 2026-04-30
updated: 2026-04-30
---

# db9 Filesystem + SQL Pattern for Agent Workflows

## TL;DR

**db9** is a PostgreSQL-based pattern for agent workflows that unifies file artifacts and queryable state under SQL:

- **Files for artifacts**: prompts, plans, logs, traces, cached responses, patches, reports
- **Tables for governance**: metadata, dedup keys, chunk indexes, run status
- **SQL as the glue**: query, rank, dedup, schedule — all within a single database

This eliminates the traditional stack split of object storage + DB + vector DB + queue, replacing it with **files + Postgres, unified by SQL**.

## Core Architecture

```
┌─────────────────────────────────────────────────┐
│                     db9                          │
│                                                  │
│  ┌─────────────────┐   ┌─────────────────────┐   │
│  │  fs9 Extension  │   │  Tables (SQL)       │   │
│  │                 │   │                     │   │
│  │  File read/write│   │  Metadata           │   │
│  │  CSV/JSONL as   │   │  Dedup keys         │   │
│  │  relations      │   │  Chunk indexes      │   │
│  │  File existence │   │  Run status         │   │
│  │  & size queries │   │  JSONB/FTS/vectors  │   │
│  └────────┬────────┘   └──────────┬──────────┘   │
│           │                       │               │
│  ┌────────▼───────────────────────▼──────────┐   │
│  │          SQL Query Engine                  │   │
│  │  ┌──────────────────────────────────┐     │   │
│  │  │ embedding() — server-side vector │     │   │
│  │  │ CHUNK_TEXT() — markdown-aware    │     │   │
│  │  │ pgvector + HNSW indexing         │     │   │
│  │  │ FTS with tsvector/ts_rank_cd     │     │   │
│  │  │ http extension for API calls     │     │   │
│  │  │ pg_cron for scheduling           │     │   │
│  │  └──────────────────────────────────┘     │   │
│  └──────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
```

## Why This Pattern Works for Agents

### 1. Files Are Not Blobs
Agent outputs are naturally file-shaped (logs, markdown, diffs, patches). With fs9, files become **queryable relations**:

```sql
-- Write an artifact
SELECT extensions.fs9_write('/reports/analysis.md', '# Agent Report\n...');

-- Read and query a JSONL log file as a table
SELECT _line_number, line
FROM extensions.fs9('/logs/run.jsonl')
WHERE line->>'level' = 'error';

-- Treat CSV as a relation
SELECT * FROM extensions.fs9('/data/users.csv') LIMIT 5;
```

### 2. Debugging Becomes SQL
When agent artifacts are queryable from SQL, debugging stops being a bespoke UI problem and becomes a **query problem**:

```sql
-- Find all runs that failed in the last hour
SELECT * FROM agent_runs
WHERE status = 'failed'
  AND created_at > NOW() - INTERVAL '1 hour';

-- Check which prompts led to the most retries
SELECT prompt_hash, COUNT(*) as retry_count
FROM agent_runs
WHERE retries > 0
GROUP BY prompt_hash
ORDER BY retry_count DESC;
```

### 3. RAG Pipeline in Pure SQL
The minimal RAG loop — docs → chunks → retrieval → report — runs entirely within db9:

```sql
-- Step A: Source docs as files
SELECT extensions.fs9_write('/docs/agents/intro.md', $$
# Agents + Files + SQL
Agents produce artifacts (plans/logs/reports).
$$);

-- Step B: Chunk index in Postgres
INSERT INTO doc_chunks (path, chunk_idx, content, meta)
SELECT '/docs/agents/intro.md',
       c.chunk_index,
       c.chunk_text,
       jsonb_build_object('source', 'docs')
FROM CHUNK_TEXT(
  content => extensions.fs9_read('/docs/agents/intro.md'),
  max_chars => 3600,
  overlap_chars => 540,
  title => 'agents/intro'
) as c;

-- Step C: Retrieval with FTS
SELECT path, chunk_idx, content
FROM doc_chunks
WHERE search_vector @@ plainto_tsquery('english', 'filesystem sql agents')
ORDER BY ts_rank_cd(search_vector, plainto_tsquery('english', 'filesystem sql agents')) DESC
LIMIT 8;
```

### 4. Server-Side Embeddings
db9 supports `embedding()` for server-side vector generation — no separate embedding service needed:

```sql
-- Generate embeddings for all chunks
UPDATE doc_chunks
SET vec = embedding(content)::vector(1024)
WHERE vec IS NULL;

-- Semantic search with cosine distance
SELECT path, chunk_idx, content
FROM doc_chunks
ORDER BY vec <-> embedding('agent workflow patterns')::vector(1024)
LIMIT 5;
```

## Relationship to Agent Architecture

### vs. Traditional Stack
| Traditional Stack | db9 Pattern |
|-----------------|-------------|
| Object Storage (S3) | fs9 filesystem |
| Database (Postgres) | Postgres tables |
| Vector DB (Pinecone, Milvus) | pgvector + embedding() |
| Queue (Redis, RabbitMQ) | pg_cron + tables |
| Application glue code | SQL queries |

### Advantages
- **Single system to operate** — no distributed consistency concerns
- **SQL as universal interface** — debugging, monitoring, and querying all use the same language
- **File-native** — agent outputs stay as real files, accessible outside the database
- **Built-in scheduling** — pg_cron for periodic agent runs

### Limitations
- **Scale ceiling** — works well for single-team workloads, may need sharding for enterprise scale
- **Postgres expertise required** — the pattern assumes comfort with SQL and Postgres extensions
- **fs9-specific** — not all Postgres distributions include filesystem extensions

## Implications for Team Architecture

As discussed in Slack (2026-03-30):
> 「OpenClaw+OpenCodeベースでDiscord経由操作組んでたけど一瞬でいらなくなった」

The db9 pattern makes Discord/Slack-based agent orchestration **trivial** — you don't need custom integration code. Just:
1. Write agent outputs to files
2. Query them with SQL
3. Use pg_cron for scheduling
4. Expose results via http extension

## See Also

- [[concepts/generative-app-evolution]] — Backend patterns that support generative apps
- [[concepts/agent-iam]] — Identity management for agent workflows
- [[concepts/harness-engineering]] — Agent orchestration infrastructure
