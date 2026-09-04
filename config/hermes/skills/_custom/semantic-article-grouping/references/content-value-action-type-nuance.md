# Content Value vs Action Type — The Enrichment Nuance

When triaging, a ★★★★★ discovery (entirely new mechanism/thesis not in wiki) may map to enriching an existing umbrella page rather than creating a new one.

## Validated Example: "GLM 5.2 Margin Collapse" (Jul 2026)

**Article**: martinalderson.com — GLM 5.2 and the coming AI margin collapse (part 1)
**Star rating**: ★★★★★ (entirely new economic mechanism)
**Action**: Enrich `concepts/ai-industry-economics.md` + `entities/martin-alderson.md`
**Why not a new page**: The umbrella `concepts/ai-industry-economics.md` already houses AI financial economics. The article adds a new mechanism (open-weights drop-in replacement enabling near-zero switching costs → margin collapse) within that umbrella.

## Decision Key

| Content value | Page umbrella | Recommended action |
|---|----|---|
| ★★★★★ | Does not exist | Create new page |
| ★★★★★ | Exists, covers different dimension | Enrich existing page |
| ★★★★☆ | Exists, needs new data/variants | Enrich existing page |
| ★★★☆☆ | Entity page covers the author | Minor reference update |

## Why This Matters

The downstream wiki-ingest pipeline reads `candidate_wiki_path` to determine creation vs enrichment. A ★★★★★ with `candidate_wiki_path` pointing to an existing page correctly triggers enrichment, not creation. The star rating communicates **content priority** (this should be processed before ★★★★☆ items); the `candidate_wiki_path` communicates **action type**. These are independent signals.
