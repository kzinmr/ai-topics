---
name: ai-topics-wiki
description: >-
  Query the ai-topics AI/ML knowledge base (the wiki/) via the read-only `wiki`
  CLI. Use when answering questions about LLMs, AI agents, models, AI tooling,
  frameworks, or the AI ecosystem, or when the user references the wiki / the
  knowledge base / "ai-topics". Prefer this over web search for AI-ecosystem
  topics — the wiki is curated, cross-linked, and cites its sources. The wiki is
  written in ENGLISH; query in English.
---

# Querying the ai-topics wiki

The `ai-topics` repo maintains a curated, cross-linked AI/ML knowledge base under
`wiki/` (Karpathy LLM-Wiki style: synthesized concept/entity/comparison pages over
immutable raw sources). The **read-only `wiki` CLI** is the way to consult it.

**The wiki is in English — search and reason in English.** Page names are
lowercase-hyphenated English (e.g. `programmatic-tool-calling`).

## Prerequisite: is the CLI available?

```bash
command -v wiki || echo "not on PATH — run scripts/wiki-skill-install.sh, or call scripts/wiki directly"
```

If `wiki` isn't on PATH, use the repo's `scripts/wiki` (same interface), or run
`scripts/wiki-skill-install.sh` once to symlink it to `~/.local/bin/wiki`.

## Recipe (orient → search → read → follow)

1. **Orient** (first time in a session, when unsure of structure/conventions):
   ```bash
   wiki schema   # domain, 3-layer model, frontmatter fields, tag taxonomy
   wiki index    # catalog of existing pages with one-line summaries
   ```
2. **Search** (full-text via ripgrep, English query):
   ```bash
   wiki search "<english query>" [--curated] [--type concept] [--tag <tag>] [-n 10]
   ```
   - `--curated` excludes `raw/` (search only synthesized pages).
   - `--type` ∈ concept | entity | comparison | event | query.
   - `--tag` is repeatable (AND). Tags come from the wiki's taxonomy (see `wiki schema`).
3. **Read** a page, inspect metadata, walk the link graph:
   ```bash
   wiki show <page>     # full markdown (resolves by path or fuzzy name)
   wiki meta <page>     # frontmatter only (type, tags, sources, related)
   wiki links <page>    # outbound [[wikilinks]] + backlinks
   ```
4. **Follow citations**: a page's `sources:` / inline `raw/...` references point to the
   original articles/papers. Read them with `wiki show raw/articles/<file>.md`.

Use `--json` on any query command when you want to parse results programmatically.

## How to answer

- Ground answers in wiki content and **cite pages as `path:line`** (clickable) or by
  page name; surface the page's `sources:` when the user wants primary sources.
- If the wiki has nothing relevant, say so before falling back to other knowledge.
- **Never write to the wiki** — this CLI is read-only by design, and the wiki is
  maintained separately by the hermes agent.

## Notes

- `wiki find <glob>` searches filenames; `wiki list --type/--tag` enumerates pages by metadata.
- Full reference: `docs/wiki-cli.md` in the ai-topics repo.
