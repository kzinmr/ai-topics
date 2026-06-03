---
title: Branch-Aware Search
created: 2026-06-03
updated: 2026-06-03
type: concept
tags: [vector-search, retrieval, branching, versioning, design-patterns, information-retrieval, architecture]
sources:
  - raw/articles/2026-06-03_zayarni-qdrant-branch-aware-vector-search.md
  - https://qdrant.tech/documentation/tutorials-search-engineering/branch-aware-search/
  - https://neon.com/docs/introduction/branching
---

# Branch-Aware Search

**Branch-aware search** is a design pattern for scoping search results to a specific version or branch of a data corpus, preventing cross-branch leakage. It applies git-style versioning concepts to data retrieval systems, ensuring that queries return only the "live view" relevant to the current branch context.

## Problem

Most search systems assume a flat corpus — one collection, one version of each document, one truth. Real systems are versioned:

- **Documentation** has draft and published branches
- **Policy repositories** have jurisdictional/regional forks
- **Feature branches** need their own view of the codebase
- **RAG systems** serve different users who should see different content versions

Without scoping, semantic search returns results leaking from the wrong branch — old versions, deleted files, or content that only exists on a different fork.

## Core Pattern: MVCC for Vector Search

The key insight (articulated by Andre Zayarni / Qdrant) is to apply **MVCC (Multi-Version Concurrency Control)** principles to vector search:

1. **Each version = a separate point** — tagged with branch name and commit sequence number
2. **Old points are never deleted** — they are marked as superseded via a nested payload field (`overwritten_in: [{by: branch, seq: N}]`)
3. **Query-time visibility filter** — includes current branch + ancestors, excludes anything the branch has replaced

### Filter Construction

For a branch `A` with ancestry `[(root, fork_seq)]`:

```
filter: {
  should = [                          # OR across branches
    { must: [branch == "A"] },        # A's own commits
    { must: [branch == "root"] }      # inherited from root
  ]
  must_not = [                        # exclude superseded
    { nested: overwritten_in { by == "A" } },
    { nested: overwritten_in { by == "root" } }
  ]
}
```

### Scalability Properties

- **Filter grows with lineage depth, not corpus size** — each ancestor adds one candidate clause and one exclusion
- **Deterministic point IDs** — `uuid5(branch | seq | path)` makes replay idempotent
- **Nested filters** bind `by` and `seq` on the same overwrite record, preventing false exclusions

## Implementation in Qdrant

Qdrant published a full tutorial implementing this pattern:

- Uses `sentence-transformers/all-MiniLM-L6-v2` (384-dim) via Cloud Inference
- Payload indexes on `path`, `branch`, and `overwritten_in[].by`
- `scroll` API with `visibility_filter` for scoped retrieval
- Steps: add file → update file → delete file → branch off → change inherited file → merge

See: [[qdrant]] tutorial at [qdrant.tech](https://qdrant.tech/documentation/tutorials-search-engineering/branch-aware-search/)

## Parallel: Neon's Database Branching

[[neon-database]] implements the same branching concept at the database layer:

| Dimension | Qdrant Branch-Aware Search | Neon Database Branching |
|---|---|---|
| **Layer** | Vector index (search/retrieval) | Postgres database (storage/query) |
| **Branching model** | Git-style: parent + fork seq | Git-style: copy-on-write clone |
| **Data sharing** | Points inherited via visibility filter | Pages shared via copy-on-write (no data duplication) |
| **Write isolation** | New points tagged with branch | Writes saved as delta, isolated from parent |
| **Merge** | Replay commits as new seq on parent | Manual (schema diff + data merge) |
| **Time travel** | Ancestry chain up to fork point | Instant restore, Time Travel queries, history window (up to 30 days) |
| **Use case** | Scoped semantic search across versioned docs | Dev/test environments, CI/CD branching, schema migration |
| **Performance impact** | Filter adds O(depth) clauses to HNSW | Creating branches has zero impact on parent performance |

### Shared Design Principle

Both systems apply **"branch your data like you branch your code"**:

- **No duplication**: shared underlying data (points / pages) until divergence
- **Isolation**: changes on a branch don't affect the parent
- **Deterministic forking**: explicit fork point recorded
- **Cleanup**: branches can be deleted without affecting the source

## Use Cases

1. **Documentation staging** — draft → review → published, each branch sees its own version
2. **Compliance repos** — regional policy forks with jurisdictional differences
3. **RAG personalization** — different users see different corpus views
4. **Code search** — feature branch search scoped to its own + main's view
5. **Dev/test environments** — database branches for safe schema experimentation (Neon)
6. **CI/CD pipelines** — ephemeral database branches per PR (Neon + Vercel integration)

## Open Questions

- **Recall degradation**: On long-lived branches, most points become superseded. The visibility filter excludes most of the corpus — does filtered HNSW stay in-graph or fall back to exact search? (raised by Kayhan Babaee)
- **Merge conflicts**: Neither system has automated merge conflict resolution for divergent edits to the same document/row
- **Deep ancestry cost**: While filter grows linearly with depth, very deep branch trees (10+) may degrade query latency

## Related Concepts

- [[vector-search]] — the base retrieval mechanism being scoped
- [[rag-systems]] — primary application domain for branch-aware retrieval
- [[agentic-retrieval]] — agents may need branch-scoped search for version-aware tasks
- [[multitenancy]] — branch isolation parallels tenant isolation patterns
