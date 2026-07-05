---
title: Branch-Aware Search
created: 2026-06-03
updated: 2026-06-03
type: concept
tags:
  - search
  - rag
  - branching
  - versioning
  - methodology
  - architecture
sources:
  - raw/articles/2026-06-03_zayarni-qdrant-branch-aware-vector-search.md
  - https://qdrant.tech/documentation/tutorials-search-engineering/branch-aware-search/
  - https://neon.com/docs/introduction/branching
  - https://turbopuffer.com/docs/branching
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

See: [[entities/qdrant]] tutorial at [qdrant.tech](https://qdrant.tech/documentation/tutorials-search-engineering/branch-aware-search/)

## Parallel: Neon's Database Branching

[[entities/neon-database]] implements the same branching concept at the database layer:

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

## Parallel: turbopuffer's Namespace Branching

[[entities/turbopuffer]] implements branching at the **search infrastructure** layer — closer to Qdrant's domain but with a fundamentally different architecture:

| Dimension | Qdrant Branch-Aware Search | turbopuffer Namespace Branching |
|---|---|---|
| **Layer** | Vector index (search/retrieval) | Search engine on object storage |
| **Branching model** | Application-level MVCC pattern in payload | Native infrastructure primitive (`branch_from` API) |
| **Branch scope** | Per-document visibility within a collection | Entire namespace (all documents + indices) |
| **Creation cost** | Zero (filter logic at query time) | Constant-time, regardless of namespace size |
| **Data sharing** | Points shared via filter; no physical duplication | Copy-on-write over object storage; shared until divergence |
| **Independence** | Read-only scoping (writes always go to branch) | Fully independent — reads, writes, queries, deletes on either side |
| **Chain depth** | Unlimited (ancestry list) | Unlimited (branch from branches) |
| **Branches per parent** | Unlimited | Unlimited |
| **Pricing** | No branching cost (filter overhead only) | Flat $0.032/branch + standard storage per logical bytes |
| **Use case** | Scoped search across versioned document corpus | Per-developer sandboxes, test pipelines, RL training reproducibility, snapshots |

### Architectural Contrast

- **Qdrant** treats branching as an **application-level pattern**: you build the MVCC logic yourself using payload fields, nested filters, and sequence numbers. Flexible but requires implementation effort.
- **turbopuffer** treats branching as a **native infrastructure primitive**: one API call (`branch_from`) creates a fully independent namespace clone. Simpler but scoped to namespace-level granularity.
- **Neon** treats branching as a **database-layer feature**: copy-on-write at the page level with git-like CLI/API integration.

### Key Insight

turbopuffer's approach is the most "batteries-included" — branching is a first-class API, not a pattern you implement. This reflects its object-storage-native architecture: since all data lives in S3, creating a CoW clone is a metadata operation on the storage layer. Qdrant's approach gives more fine-grained control (per-document visibility within a collection) but requires the developer to manage the versioning logic.

### Shared Design Principle

All three systems apply **"branch your data like you branch your code"**:

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
7. **Codebase indexing** — embed once, branch per local checkout so only changed files need re-indexing (turbopuffer)
8. **RL training reproducibility** — branch corpus for exact training environment preservation during ablation studies (turbopuffer + SID AI)
9. **Snapshots** — capture state of a changing namespace at a point in time, query the immutable snapshot (turbopuffer)

## Open Questions

- **Recall degradation**: On long-lived branches, most points become superseded. The visibility filter excludes most of the corpus — does filtered HNSW stay in-graph or fall back to exact search? (raised by Kayhan Babaee)
- **Merge conflicts**: Neither Qdrant nor Neon has automated merge conflict resolution for divergent edits to the same document/row
- **Deep ancestry cost**: While filter grows linearly with depth, very deep branch trees (10+) may degrade query latency
- **Storage billing at scale**: turbopuffer bills each branch as a full namespace (logical bytes). As branches diverge, storage costs could grow faster than expected — reduction planned after production observation
- **Pattern vs primitive tradeoff**: When should you build MVCC yourself (Qdrant pattern) vs use a native branching API (turbopuffer/Neon)? Depends on whether you need per-document granularity or namespace-level isolation

## Related Concepts

- [[concepts/vector-search]] — the base retrieval mechanism being scoped
- [[concepts/rag-systems]] — primary application domain for branch-aware retrieval
- [[concepts/agentic-retrieval]] — agents may need branch-scoped search for version-aware tasks
- [[multitenancy]] — branch isolation parallels tenant isolation patterns
- [[concepts/zero-disk-architecture]] — turbopuffer's object-storage-native model enables cheap branching
