---
title: "Code Search Indexing for Agent Tools"
created: 2026-08-14
updated: 2026-08-14
type: concept
tags:
  - concept
  - search
  - lexical-search
  - information-retrieval
  - coding-agents
  - developer-tooling
  - code-intelligence
aliases:
  - "regex search indexing"
  - "fast regex search"
  - "sparse n-grams"
related:
  - "[[entities/cursor-ai]]"
  - "[[concepts/lexical-search]]"
  - "[[concepts/agentic-retrieval]]"
  - "[[concepts/code-intelligence-for-llms]]"
  - "[[concepts/semantic-ids]]"
  - "[[concepts/rlm-for-indexing]]"
sources:
  - raw/articles/2026-05-10_cursor_fast-regex-search.md
  - https://cursor.com/blog/fast-regex-search
---

# Code Search Indexing for Agent Tools

## Summary

**Code search indexing for agent tools** is the practice of building inverted indexes over source code so that regex/grep-style lookups — one of the most frequent operations coding agents perform — return candidate files in milliseconds instead of scanning every file in the repository. The approach was brought to agent tooling by [[entities/cursor-ai]] (research post by Vicent Marti, March 2026): most agent harnesses default to `ripgrep` for the search tool, but ripgrep must match against the contents of *all* files, and on large enterprise monorepos `rg` invocations routinely take more than 15 seconds — stalling agent workflows.

The techniques used (n-gram inverted indexes, trigram decomposition, sparse n-grams) date back to information-retrieval research from the 1990s (Zobel, Moffat & Sacks-Davis 1993; popularized by Russ Cox's 2012 post after Google Code Search shut down). Cursor's contribution is applying them to agent context gathering, deploying the indexes **client-side** with a git-commit-based sync model, and reporting that "instant grep" creates a qualitative difference in agentic workflows.

## Key Ideas

### The Agent Grep Problem

- Agent harnesses (including Cursor's) default to `ripgrep` (Andrew Gallant) for text search because of its speed and sensible defaults
- However, ripgrep scans all files; latency scales with repository size and complexity — one of the few agent operations that does
- Cursor sees `rg` invocations >15s on large Enterprise monorepos; this stalls users interactively guiding agents
- Regex search is a distinct retrieval mode from semantic search: some queries can *only* be resolved by regular expressions

### Classic Algorithm: N-Gram Inverted Indexes

- First published 1993 by Zobel, Moffat and Sacks-Davis: "Searching Large Lexicons for Partially Specified Terms using Compressed Inverted Files"
- Approach: n-grams (fixed-width character segments) as index keys; regexes decomposed into a tree of n-grams that can be looked up in the index
- Popularized for code search by Russ Cox's 2012 blog post (written shortly after the shutdown of Google Code Search)
- **Inverted index**: documents split into tokens → tokens become keys → values are posting lists (document IDs); search intersects posting lists for all required tokens

### Trigram Decomposition

- A traditional trigram index extracts every consecutive 3-character sequence
- Regexes are decomposed into a set of required trigrams that can be intersected against the index to scope candidate documents
- Candidate files still need per-file scanning — the index only narrows the candidate set, it does not replace the regex engine

### Suffix Arrays: A Detour

- The article explores suffix arrays as an alternative index structure (compact, powerful for exact substring search) before settling on n-gram approaches for the production design

### Trigram Queries with Probabilistic Masks

- Intermediate optimization where trigram posting lists are combined using probabilistic bitmask techniques to reduce memory and intersection cost

### Sparse N-Grams: Smarter Trigram Selection

- Used by ClickHouse (regex operator) and GitHub's new Code Search (shipped a couple of years ago)
- Instead of extracting every consecutive 3-char sequence (heavy redundancy — adjacent trigrams duplicate characters), extract n-grams of **variable, random-but-deterministic length**
- Each character pair gets a deterministic weight (e.g., CRC32 hash of the two chars); sparse n-grams are all substrings whose edge weights are strictly greater than all interior weights
- `build_all` at index time extracts every sparse n-gram; at query time a `build_covering` algorithm generates only the minimal n-grams needed to match in the index — very high specificity with fewer postings
- Trade-off: higher upfront indexing cost for very fast queries

## Client-Side Deployment ("All this, in your machine")

Cursor deliberately builds and queries regex indexes **on the user's machine**, unlike semantic indexes which are server-side:

- **Freshness**: the index must reflect the agent's own writes — a missing match sends the agent on a wild goose chase and wastes tokens (semantic indexes tolerate stale embeddings; text indexes cannot)
- **Latency**: Composer's high TPS makes network roundtrips the bottleneck; the model uses search constantly, often in parallel
- **Privacy/security**: client-side storage sidesteps data-storage concerns; files never leave the machine
- **Sync model**: index state is based on a Git commit; user and agent changes are a layer on top — quick to update, fast to load on startup
- **Storage layout**: two files — (1) postings file flushed directly to disk during construction; (2) sorted lookup table of n-gram hashes → offsets into the postings file; only the lookup table is mmap'd into the editor process; queries are binary search + direct offset read; hash collisions can only broaden a posting list (safe), never produce incorrect results

## Impact & Results

- Providing text search indexes to fast models (Composer 2) "creates a qualitative difference for Agentic workflows"
- Impact is much more pronounced in large Enterprise repositories — grep is one of the few agent operations whose latency scales with codebase size
- Example workflows (bug investigation in `chromium`, refactoring in `chromium` and `cursor`) show large time savings when grep time is removed entirely
- Continuing research direction: optimizing semantic indexes further and new context-gathering approaches, with the constraint of working in the largest repositories

## Relationship to Semantic Indexes

Semantic (embedding) indexes and regex indexes are **complementary** retrieval layers for agents:

| Dimension | Semantic Index | Regex/Text Index |
|-----------|---------------|------------------|
| Query type | Fuzzy / meaning-based | Exact pattern / regular expression |
| Freshness tolerance | High (stale embeddings still point in right direction) | Low (missing text = wild goose chase) |
| Deployment | Server-side (Cursor) | Client-side (Cursor) |
| Latency profile | Network roundtrip acceptable | Must be local — model calls constantly, in parallel |
| Lineage | Embedding nearest-neighbor | 1993 Zobel/Moffat n-grams; Russ Cox 2012; ClickHouse / GitHub sparse n-grams |

## Graph Structure Query

```
[this-concept] ──embodies──→ [concept: lexical-search]
[this-concept] ──relates-to──→ [concept: agentic-retrieval]
[this-concept] ──implemented-by──→ [entity: cursor-ai]
[this-concept] ──extends──→ [concept: code-intelligence-for-llms]
[this-concept] ──contrasts──→ [concept: semantic-ids]
```

This section informs graph queries: implemented by [[entities/cursor-ai]], embodies [[concepts/lexical-search]], relates to [[concepts/agentic-retrieval]] and [[concepts/rlm-for-indexing]], contrasts with embedding-based approaches like [[concepts/semantic-ids]] and extends the broader practice of [[concepts/code-intelligence-for-llms]].

## Related Concepts

- [[entities/cursor-ai]] — Implementer; research published on cursor.com blog by Vicent Marti (March 2026)
- [[concepts/lexical-search]] — The retrieval family this technique belongs to (BM25, inverted indexes)
- [[concepts/agentic-retrieval]] — How agents gather context during tool use
- [[concepts/code-intelligence-for-llms]] — Broader practice of pre-computed code analysis data for LLMs
- [[concepts/semantic-ids]] — Embedding-based approach contrasted with exact text indexing
- [[concepts/rlm-for-indexing]] — Recursive language model applied to indexing tasks

## Sources

- [Fast regex search: indexing text for agent tools — Cursor Blog](https://cursor.com/blog/fast-regex-search) (Vicent Marti, Mar 23 2026) — raw: `raw/articles/2026-05-10_cursor_fast-regex-search.md`
