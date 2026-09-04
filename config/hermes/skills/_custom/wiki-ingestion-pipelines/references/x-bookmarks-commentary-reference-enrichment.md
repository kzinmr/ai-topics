# Commentary Bookmark on an Already-Documented Topic → Reference Enrichment (★★☆☆☆)

Decision rule for x-bookmarks-ingest (and any ingestion pipeline) when a bookmark/tweet is a notable figure's *commentary* about a model/event the wiki ALREADY covers comprehensively.

## Detection signal

- The event is 1-2 days old.
- `log.md` already shows the same topic ingested via other pipelines (blog-ingest, newsletter-ingest, x-accounts-scan, fireworks/sitemap, etc.).
- An entity page already exists with 100+ lines AND multiple raw articles + newsletter digests already reference it.
- The bookmark text is the author's *framing/opinion*, not a new factual release.

In this case the bookmark is **reference-level**, not a new discovery. Do NOT create new pages.

## Correct action — reference-level enrichment (3 steps)

1. **Save the tweet as a raw article.** Filename per [[raw-article-filename-policy]] (actual `created_at` date, handle without `@` as source-slug). If X truncated the text mid-sentence, add `status: TRUNCATED` in frontmatter and note the full text is unrecoverable. **A single truncated tweet qualifies — not just a thread** (broadens the existing "truncated thread" pitfall).
2. **Add a "Community Reception" section** to the model/entity page. Capture only the commentary's *framing* that is NOT already in the factual specs — e.g. an architectural characterization ("Gemma-like architecture") or a historical claim ("first open-weight release since the good old Llama days"). Keep it 1-3 sentences with the source link.
3. **Add a one-bullet commentary entry** to the commenter's own entity page (e.g. `sebastian-raschka.md`). When the existing section header is month-scoped (e.g. `### New Publications and Insights (July 2026)`) but already contains cross-month items, rename it to drop the stale month label.

Also: add the raw article path to `sources:` frontmatter on BOTH pages, and bump `updated:` dates.

## Worked example (2026-08-12)

rasbt's tweet: "Meta released a new open-weight LLM... 30B multimodal reasoning model with a Gemma-like architecture design... first since the good old Llama days."

- Muse Glimmer was already covered by 4 prior sources (Meta official intro, Simon Willison, Fireworks AI, newsletter digest) and `entities/muse-glimmer.md` was 156 lines.
- Action taken: raw article `2026-08-11_rasbt_meta-muse-glimmer-gemma-like.md` → "Community Reception" section in `entities/muse-glimmer.md` (Gemma-like + first-since-Llama framing, linking `[[entities/gemma-4]]` and `[[entities/muse-spark]]`) → commentary bullet in `entities/sebastian-raschka.md` + header rename.
- No new pages, index.md unchanged.

## Pitfall reinforced this session

- `search_files(target="files")` on `wiki/entities` returned a FALSE NEGATIVE for `rasbt|sebastian-raschka|Raschka` (0 results) even though `sebastian-raschka.md` and `sebastian-ramirez.md` both exist. Always confirm entity existence with `ls wiki/entities/ | grep -i <name>` before concluding a page is missing — see the pre-creation verification checklist in [[wiki-entity-enrichment-from-article]].
