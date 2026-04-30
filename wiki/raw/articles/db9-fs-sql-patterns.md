---
title: "db9: Filesystem + Postgres for Agent Workflows"
source: "https://me.0ffff.me/db9-fs-sql-patterns.html"
scraped: 2026-04-30
---

# db9: Filesystem + Postgres for Agent Workflows

**Source:** [me.0ffff.me](https://me.0ffff.me/db9-fs-sql-patterns.html)
**Core Philosophy:** Keep agent artifacts as **real files** (logs, markdown, diffs) and governance/indexes as **Postgres**, using **SQL as the glue** to unify them.

---

## 1. What is db9?
db9 is a PostgreSQL distribution (wire-compatible) with compiled-in extensions specifically designed for agentic workloads. It eliminates the need to split state across object storage, vector DBs, and application glue code.

### Key Extensions:
*   **fs9**: Read/write files from SQL; treat CSV, JSONL, and Parquet as relations.
*   **embedding + vector**: Server-side embedding generation and `pgvector` search (HNSW).
*   **http + pg_cron + branching**: Integrated API calls, scheduling, and safe data experimentation.

---

## 2. The Core Pattern: Files + SQL
Agent systems accumulate two types of state that db9 unifies:
1.  **Artifacts (File-shaped):** Prompts, plans, traces, cached responses, reports.
2.  **Queryable State (Table-shaped):** Metadata, deduplication keys, chunk indexes, run status.

### File Operations via SQL
Files are treated as queryable relations rather than opaque blobs:
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

---

## 3. The Compact Pipeline (RAG-ish Loop)

### Step A: Source Documentation
Store raw documents directly in the db9 filesystem.
```sql
select extensions.fs9_write('/docs/agents/intro.md', $$ # Content here $$);
```

### Step B: Materialize Chunk Index
Use the built-in `CHUNK_TEXT` function, which is markdown-aware and respects natural breakpoints.
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
**Full-Text Search (FTS):**
```sql
select path, content from doc_chunks
where search_vector @@ plainto_tsquery('english', 'filesystem sql agents')
order by ts_rank_cd(search_vector, plainto_tsquery('english', 'filesystem sql agents')) desc;
```

**Semantic Search (Embeddings):**
db9 generates embeddings server-side via the `embedding()` function.
```sql
-- Generate and store vectors
update doc_chunks set vec = embedding(content)::vector(1024) where vec is null;

-- Search using cosine distance
select path, content from doc_chunks
order by VEC_EMBED_COSINE_DISTANCE(vec, 'how do agents use filesystem?') limit 8;
```

### Step D: Output Management
Write the final agent response to a file while tracking its metadata in a table for governance.
```sql
-- Write the file
select extensions.fs9_write('/reports/output.md', '# Generated Summary...');

-- Log the artifact metadata
insert into artifacts (path, kind, meta)
values ('/reports/output.md', 'report', '{"inputs":["/docs/agents/intro.md"]}'::jsonb);
```

---

## 4. Why This Composition Works
*   **Transparency:** Files keep artifacts human-inspectable and easy to debug.
*   **Structure:** Tables enforce schema and allow complex joins/filtering.
*   **Efficiency:** SQL handles the entire workflow (filter, join, rank, dedup) close to the data, reducing latency and architectural complexity.
*   **Observability:** "Why did the agent do that?" becomes a standard SQL query rather than a search through disparate logs.
