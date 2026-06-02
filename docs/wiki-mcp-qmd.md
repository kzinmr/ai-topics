# Wiki MCP — optional full-text & semantic search with qmd

**Optional add-on** to [wiki-mcp.md](wiki-mcp.md). The phase-1 Filesystem MCP lets
agents *browse* the wiki but only does filename globbing — no full-text or
semantic search. [qmd](https://github.com/tobi/qmd) closes that gap: it indexes
markdown into SQLite **FTS5 (BM25)** plus optional **local vector embeddings**,
and ships its own **`qmd mcp`** server. Stand it up **alongside** the read-only
filesystem MCP (they are complementary: qmd finds the right pages, the filesystem
MCP / qmd `get` reads them).

> qmd indexes a *copy* of the content into its own SQLite store; it does not write
> into `wiki/`. The wiki stays untouched.

## Prerequisites

- Node ≥ 22 (this machine: `node v24.12`). Install: `npm install -g @tobilu/qmd`.
- For semantic/hybrid search, the **MCP `query` tool requires embeddings** and
  downloads ~1.8 GB of local GGUF models (EmbeddingGemma-300M, a reranker, a query
  expander) on first use. Lexical-only `qmd search` (CLI) needs no models, but the
  **MCP server only exposes hybrid `query`** — so using `qmd mcp` implies the model
  download. The wiki is English, so the default English embeddings are fine.

## 1. Install

```bash
npm install -g @tobilu/qmd
qmd --version
```

## 2. Create collections

Index the curated layer as the primary searchable corpus, and `raw/` as a second
collection so cited sources resolve via `get` / `multi_get`.

```bash
WIKI="$HOME/ai-topics/wiki"

# Curated layer (Layer 2). Verify against `qmd collection add --help` whether one
# named collection accepts multiple paths; if not, add per-area collections.
qmd collection add "$WIKI/concepts"    --name ai-topics-wiki
qmd collection add "$WIKI/entities"    --name ai-topics-wiki
qmd collection add "$WIKI/comparisons" --name ai-topics-wiki
qmd collection add "$WIKI/events"      --name ai-topics-wiki
qmd collection add "$WIKI/queries"     --name ai-topics-wiki

# Raw sources (Layer 1) — for citation resolution.
qmd collection add "$WIKI/raw" --name ai-topics-raw

qmd collection list
```

## 3. Attach context (this is where "query in English" lives)

`qmd context` descriptions are returned alongside results and surfaced via the MCP
`status` tool, so the agent reads them. This is the qmd equivalent of the priming
the generic filesystem server can't carry.

```bash
qmd context add qmd://ai-topics-wiki \
  "Curated AI/ML knowledge base (concepts, entities, comparisons, events) for LLMs and AI agents. Written in English — ALWAYS issue queries in English; non-English queries return poor results. Start here for synthesized knowledge."

qmd context add qmd://ai-topics-raw \
  "Original source material (articles, papers, newsletters) cited by the curated wiki. Use get/multi_get to resolve [[wikilinks]] and citations. English only."
```

## 4. Index and embed

```bash
qmd update          # build/refresh the FTS5 index
qmd embed           # generate vector embeddings (triggers the ~1.8 GB model download)
qmd status          # confirm collections, doc counts, and context
```

Sanity-check from the CLI before wiring up the MCP:

```bash
qmd search "programmatic tool calling" -c ai-topics-wiki --md   # lexical only, no models
qmd query  "how do agents do programmatic tool calling" --md    # hybrid (needs embeddings)
qmd get <path-or-docid>                                          # read a page / cited source
```

## 5. Register the qmd MCP server with Claude Code

```bash
claude mcp add ai-topics-wiki-search --scope user -- qmd mcp
claude mcp get ai-topics-wiki-search
```

Equivalent `~/.claude/settings.json` (or a project `.mcp.json`):

```json
{
  "mcpServers": {
    "ai-topics-wiki-search": { "command": "qmd", "args": ["mcp"] }
  }
}
```

The qmd plugin is another option: `claude plugin marketplace add tobi/qmd` then
`claude plugin install qmd@qmd`.

**MCP tools exposed by `qmd mcp`:** `query` (BM25 + vector + rerank, hybrid),
`get` (by path/docid), `multi_get` (glob / list / docids), `status` (index health
and the context descriptions above).

## 6. Keep the index fresh

hermes updates `wiki/` continuously, so re-index after changes:

```bash
qmd update && qmd embed
```

Wire this into a cron entry or the repo's git hook (`.githooks/`) if you want it
automatic — left manual here.

## Notes & caveats

- **Search scope vs. citation resolution:** whether the MCP `query` tool can be
  scoped to a single collection depends on qmd's current flags. If it searches all
  collections, raw sources may appear in results too; refine later (e.g. a
  metadata-filtering MCP) if that's noisy. `get`/`multi_get` still resolve raw
  citations regardless.
- **No structured frontmatter filtering** in qmd (`type`, `tags`, dates aren't
  filterable as fields). For that, the pure-Python route — `bm25s` + pandas — gives
  native metadata filtering at the cost of building a small MCP wrapper yourself.
- **Multilingual:** set `QMD_EMBED_MODEL` to a multilingual embedding model if you
  ever index non-English content; not needed for this English wiki.
