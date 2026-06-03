# Branch-Aware Search Over Versioned Documents

**Source**: [Andre Zayarni on LinkedIn](https://www.linkedin.com/posts/zayarni_most-vector-search-examples-assume-a-flat-share-7467850718553759744-Rg7U/) + [Qdrant Tutorial](https://qdrant.tech/documentation/tutorials-search-engineering/branch-aware-search/)
**Author**: Andre Zayarni (Qdrant)
**Date**: 2026-06-03

## Problem

Most vector search examples assume a flat corpus — one collection, one version of each document, one truth. But real systems are versioned:
- Documentation has draft and published branches
- Policy repos have regional forks
- Feature branches need their own view of the codebase

When you search across a versioned corpus without scoping the query, you get results leaking from the wrong branch — old versions, deleted files, content that only exists on a different fork.

## Solution: Branch-Aware Search (MVCC for Vector Index)

The core idea is essentially MVCC (Multi-Version Concurrency Control) applied to a vector index:

1. **Each version of a document is a separate point** in Qdrant, tagged with the branch that wrote it and the commit sequence number
2. **Updates don't remove old points** — they mark them as superseded with a nested `overwritten_in` payload field recording `{by: branch, seq: commit_seq}`
3. **Deletes are commits too** — they mark the point as superseded with no replacement
4. **Query-time visibility filter** builds a scope that:
   - Includes points from the current branch plus all its ancestors (up to each ancestor's fork point)
   - Excludes anything the branch has already overwritten or deleted

### Key Implementation Details

- **Point IDs are deterministic**: derived from `uuid5(branch | seq | path)`, so replaying history is fully idempotent — rebuild via upsert without duplicates
- **Filter scales with lineage depth, not corpus size**: each ancestor adds one candidate clause and one exclusion
- **Qdrant nested filters** handle the binding of `by` and `seq` on the same overwrite record — no false exclusions from partial matches
- **Visibility filter** uses `should` (OR across branches) + `must_not` (exclude superseded versions)

### Ancestry Model

```python
# Branch ancestry: list of (parent_branch, fork_seq) pairs
root_ancestry = []  # root has no parents
A_ancestry = [("root", 2)]  # A forked at root seq 2

# Each branch gets: one candidate selector + one exclusion per ancestor
# Total filter clauses = 2 × (ancestry_depth + 1)
```

## Use Cases

- Documentation sites with staged publishing (draft → review → published)
- Compliance repos with jurisdictional branches
- RAG systems where different users should see different versions of the same content
- Code search across feature branches
- Policy documents with regional forks

## Tutorial Steps (from Qdrant)

1. **Add a file** — upsert point with (branch, seq, path) payload
2. **Update a file** — mark old point as superseded, insert new point
3. **Delete a file** — mark as superseded with no replacement
4. **Branch off** — fork records parent + fork_seq; view begins as parent's state at fork
5. **Change inherited file** — mark on ancestor's point with `by: child_branch`; each branch resolves differently
6. **Merge branch** — replay commits from child onto parent, each as new seq; visibility filter resolves both

## Key Insight (from LinkedIn discussion)

Kayhan Babaee noted: "The data model is MVCC for a vector index. At production depth, on a long-lived branch most points are superseded, so the visibility filter excludes most of the corpus, and filtered HNSW either stays in-graph or falls back to exact." This is a real performance consideration for production deployments.
