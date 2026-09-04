# Historical Article Cross-Analysis Ingestion

> When a user shares a **foundational/older article** and asks to connect it to existing wiki knowledge, then ingest the discussion into the wiki.

## Trigger Pattern

User shares a URL to an older article (often a gist, blog post, or paper) and asks for deep analysis against the wiki knowledge base. The article is historically significant but predates much of what the wiki covers.

## Workflow

### Phase 1: Research & Cross-Analysis

1. **Fetch the source article** (curl the URL)
2. **Search the wiki** for ALL related modern pages:
   - `search_files` in `wiki/entities/`, `wiki/concepts/`, `wiki/index.md`
   - Search by multiple keyword variants (e.g., `rlhf`, `reinforcement-learning`, `reward-model`, `training`, `alignment`)
3. **Read the most relevant pages** (3-5) for cross-reference depth
4. **Produce the analysis** — structured as:
   - Article overview (key claims)
   - Point-by-point mapping: each claim → corresponding wiki page → 2026 status
   - Predictions vs Reality table (author's predictions vs what actually happened)
   - What the author got right, wrong, or couldn't foresee

### Phase 2: Wiki Ingestion

Follow the standard enrichment workflow, but with these specifics:

1. **Save raw article** to `wiki/raw/articles/` with original date prefix:
   - Filename: `YYYY-MM-DD_handle-slug-title.md`
   - Include YAML frontmatter: `title`, `author`, `date`, `source_url`, `type: raw-article`, `fetched`
   - Include full original text

2. **Create concept page** bridging old and new:
   - The concept page should NOT just summarize the old article — it should be a **standalone concept page** that happens to use the old article as historical anchor
   - Structure: Definition → Historical Context (the old article) → Modern Landscape → Key Methods → Cross-References
   - Include a **"Predictions vs Reality"** comparison table if the article made forward-looking claims
   - Link to ALL relevant existing wiki pages (minimum 5-8 cross-references)

3. **Update entity page** for the article's author:
   - Add the article as a key contribution
   - Update tags if needed (e.g., `lab` → `researcher`)

4. **Update existing pages** that gain from cross-referencing:
   - Add `[[wikilinks]]` to/from the new concept page
   - Usually 1-3 existing pages benefit from a cross-reference addition

5. **Standard index/log/schema updates**:
   - Add `on-policy` type tags to SCHEMA.md BEFORE using them (check taxonomy first)
   - Run tag validator: `python3 .githooks/pre-commit-tag-validator.py <new-page>`
   - Update `index.md` (concept entry + entity summary update)
   - Update `log.md` (full operation log)

## Key Distinction from Standard Ingestion

Standard article ingestion creates a page about the article's content. Cross-analysis ingestion creates a **concept page about the topic** that uses the article as a historical anchor and weaves in the full wiki knowledge graph. The deliverable is a knowledge synthesis, not a summary.

## Example Session

Goldberg "RL for LLMs" (2023 gist) →
- Concept page `on-policy-vs-off-policy-rl.md`: Goldberg's hallucination thesis, exposure bias, Brown's α×λ taxonomy, 2026 method landscape (GRPO/OPD/DPO/SDAR)
- Entity update: `yoav-goldberg.md` — added RL gist as key contribution
- Cross-refs: `post-training-distributional-view.md`, `on-policy-distillation.md`

## Pitfalls

- **Don't make the concept page a thin wrapper around the old article.** It must stand alone as a reference for the topic, with the article as one source among many.
- **Don't skip reading modern wiki pages.** The cross-analysis is only valuable if you know what the wiki already covers.
- **Check for existing concept pages on the same topic first.** If `on-policy-vs-off-policy-rl.md` already existed, the right move would be to PATCH it with the Goldberg analysis, not create a duplicate.
