# Concept Page Creation from Community Discourse

When a tweet, comment, or short post references a concept that's already discussed across multiple existing raw articles but has **no dedicated wiki page**, the value is in creating a new **concept page** that synthesizes the scattered discussions — not just ingesting the tweet itself.

## Trigger

User shares a short X post, forum comment, or remark that names a concept (e.g., "benchmaxxed", "slop", "vibe coding") and says "取り込んで" / "interpret and add to wiki."

## Decision Flow

```
User shares short post/comment
  ├── Concept already has a wiki page? → Update existing page with new source
  ├── Concept appears in 2+ raw articles but NO page? → CREATE new concept page (this workflow)
  └── Concept is a passing mention, <2 sources → Just add to relevant entity page
```

## Key Distinction from Article Ingestion

Article ingestion = one raw source → entity/concept page.
Community discourse = concept name appears scattered across multiple sources → synthesize into a new concept page.

The short post is the **catalyst**, not the **primary source**. The concept page draws substance from existing raw articles.

## Step-by-Step

### 1. Interpret the post
- Extract the concept name and the claim/observation
- Identify which existing wiki pages and raw articles discuss this concept

### 2. Search existing wiki for the concept
- `search_files` across `wiki/raw/articles/`, `wiki/concepts/`, `wiki/entities/` for the term (and variants: plural, hyphenated, concatenated)
- Check `wiki/SCHEMA.md` taxonomy for existing tags that map to the concept

### 3. Assess page-worthiness (SCHEMA.md Page Thresholds)
- **Create page** if concept appears in 2+ sources OR is central to one source
- **Update existing page** if already covered
- **Skip** if passing mention only

### 4. Save the catalyzing post as raw article
- Even short tweets get a raw article (they're the citation anchor)
- Filename: `{YYYY-MM-DD}_{handle}_{short-slug}.md`
- Type: `x_post` (not `x_note_tweet` — these are short posts)

### 5. Create the concept page
- Synthesize from all discovered sources, not just the catalyzing post
- Include: definition, why it matters, specific examples from raw articles, related concepts
- Cite all relevant raw articles in `sources` frontmatter
- Add wikilinks to related entities/concepts (minimum 2 outbound)

### 6. Update entity pages mentioned in the post
- Use `patch` (not `write_file`) for rich entity pages (>40 lines)
- Add the criticism/observation as a new section with the quote
- Add the new raw article to `sources` frontmatter
- Bump `updated` date

### 7. Update index.md + log.md
- Insert new concept alphabetically in Concepts section
- Update page counts in index header
- Prepend log entry

### 8. Commit + push
```bash
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: add <concept> concept, update <entity> from @<handle>" && git push
```

## Pitfalls

- **Don't just ingest the tweet in isolation** — the value is synthesizing scattered discussions into a coherent concept page
- **Search for spelling variants** — "benchmaxxing", "benchmaxing", "bench-maxed" may all appear; the concept page should note common variants
- **Tag must exist in SCHEMA.md** — if the concept needs a new tag, add it to the taxonomy first
- **Rich entity pages (>40 lines) must NOT be overwritten** — always `read_file` first, then `patch`
- **Concept pages need substance** — don't create a stub. If you can't fill a meaningful page from existing sources, add to an existing entity/concept page instead

## Example: Benchmaxxing concept (2026-06-08)

- **Catalyst**: @xeophon tweet: "Gemini is an amazing model, the benchmarks don't lie... But it is very stubborn... That's why people say it's benchmaxxed."
- **Existing sources found**: 10+ raw articles mentioning "benchmaxxing" (Qwen complaints, Gemini criticism, analyst commentary)
- **Created**: `concepts/benchmaxxing` — synthesized definition, examples, Goodhart's Law connection
- **Updated**: `entities/gemini` (added criticism section), `entities/florian-brand` (added to X Activity Themes)
- **Tags used**: `benchmark-optimization`, `overfitting`, `methodology` (all pre-existing in SCHEMA.md)
