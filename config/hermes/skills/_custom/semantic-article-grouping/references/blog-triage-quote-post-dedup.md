# Blog Triage — Author-Quote Dedup (Curator Quote-Post Cross-Reference)

Discovered: June 2026 session (blog-triage of 19 candidates).
Extended: July 2026 — added Primary Source counter-pattern.

## Pattern A: Quote Post of Another Author's Published Article (Skip)

When a blog triage candidate from a link-blog curator (Simon Willison, Daring Fireball) is a **"quote post"** that links to an original article by another author, check the **original author's entity page** before deciding. The original author's entity page may have already been enriched with the quoted content from a prior pipeline run (dreaming, raw-backlog-ingest, or manual enrichment) — even if the curator's entity page has never seen this article.

### Detection

- Title prefix `"A quote from <Author Name>"` (Simon Willison's link-blog convention)
- Body marked with `(via)` link and `— Author Name` attribution
- Short extract format: the blog post is a curated quote, not original analysis
- Common for Simon Willison to post daily link-blog items referencing Nesbitt, Dean W. Ball, Timothy B. Lee, and other authors whose entity pages already exist in the wiki

### Concrete Example (June 2026)

| Dimension | Detail |
|-----------|--------|
| Candidate | `simonwillison.net--2026-jun-26-incident-report--9b705a15.md` |
| Original author | Andrew Nesbitt (entities/andrew-nesbitt.md) |
| Content in blog post | Short quote: "Two AI review agents...enter a disagreement loop over whether the package is malicious. After 340 comments and $41,255 in inference spend..." |
| Content in entity page | Full 30-line "Incident Report: CVE-2026-LGTM — AI Security Gate Satire" section (lines 371-400) with 7-gate failure analysis table |
| Entity page enrichment origin | dreaming pipeline enriched from nesbitt.io original article days prior |
| **Verdict** | **Skip** — curator adds no original commentary beyond the quote itself |

### Action

1. **If the original author's entity page has the specific content** (check body sections, not just `sources` frontmatter): Mark candidate as `skip` with reason `"原著者entityページで既カバー（curator引用ポスト）"`
2. **If the entity page lists the URL in References only** without substantive summary: Downgrade to `reference` — the content is partially captured but the curator's framing may add value. Do NOT assign `take` since the curator adds minimal original commentary.

### Why This Is Different from Existing Cross-Pipeline Dedup

| Existing patterns | This pattern |
|-------------------|--------------|
| Checks newsletter-vs-blog pipeline overlap | Within blog-triage only — no other pipeline needed |
| Checks the curator's entity page | Checks the **original author's** entity page |
| Applies when pipelines ran same-day | Applies even when enrichment happened days/weeks prior |
| Requires article to be discovered by two different ingestion methods | Works from a single blog-ingest candidate |
| Content came from different delivery mechanism | Content came from the original author's own blog |

---

## Pattern B: Primary Source Quote Post — Legal Discovery / Historical Document (Take)

**Counter-pattern to Pattern A.** When the quote post contains a **primary source document** (not a curator's excerpt of another author's published article), treat it as a genuine take for entity enrichment. The quoted document IS the content — there is no original author's entity page to check because the source is a private document (email, internal memo, contract) that was never published on a blog.

### Detection

- Title follows the same Simon Willison convention (`"A quote from <Person>"`)
- Body is attributed with `— Person Name, context (e.g., "Email to Board, Date — exposed in Lawsuit Year")`
- The quote is self-contained — it does NOT link to an external article by the quoted person (it links to the curator's blog about the document)
- The source attribution references **legal discovery, court filings, leaked documents, or FOIA requests** rather than a blog URL
- The curator's role is **publishing the document** not summarizing it

### Concrete Example (July 2026)

| Dimension | Detail |
|-----------|--------|
| Candidate | `simonwillison.net--2026-jul-20-sam-altman--c4ba859f.md` (915 bytes) |
| Quoted person | Sam Altman |
| Document type | Email to OpenAI's board, October 1, 2022 |
| Provenance | Exposed in Musk v. Altman trial (2026) |
| Content | Internal OpenAI strategy: release GPT-3-level local model to pre-empt competitors ("before Stability or someone else does") and discourage similarly-powerful models from being funded |
| Wiki coverage | NOT captured — entities/sam-altman.md mentions Musk lawsuit in passing (line 90: "basis for Elon Musk's lawsuit") but has zero content from the 2022 email |
| Original author entity page | N/A — the email was never a blog post. There is no "original author's entity page" to dedup against |
| **Verdict** | ★★★★☆ **Take** — enrich `entities/sam-altman.md` (OpenAI Leadership or Major Controversies section) with the email content and strategic implications |

### Action

1. **Confirm no existing coverage**: Search the person's entity page and the organization's entity page for the specific document content. Do NOT rely on `sources` frontmatter — check body sections.
2. **Determine the best target page**: Usually the person's entity page (who wrote/created the document) is the right target. For organizational strategy documents, the company entity page may also need enrichment.
3. **Rate based on gap**: 
   - Document reveals new strategic/competitive information not in any wiki page → ★★★★☆ (existing page update)
   - Document confirms known information without adding detail → ★★☆☆☆ (reference)
4. **Treat the quote as the primary source**: Unlike Pattern A where the curator's excerpt is thin, here the quoted text IS the source artifact. Use the full quote text in the enrichment.

### Distinguishing Pattern A vs B at a Glance

| Criterion | Pattern A (Skip) | Pattern B (Take) |
|-----------|-----------------|------------------|
| Source of quoted content | Another author's published blog/article | Private document (email, memo, contract, court filing) |
| Provenance marker | `(via)` link to blog URL | `— Person, context — exposed in [venue]` |
| Existing coverage check target | Original author's entity page | Quoted person's entity page + company entity page |
| Curator's value-add | Minimal (just excerpt) | Significant (publishing/contextualizing the document) |
| Content depth in raw article | Short excerpt of a longer published piece | Full or near-full text of the document itself |