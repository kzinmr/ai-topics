# Coverage-gap verification heuristics for take decisions (Nov 2026)

Distilled from blog-wiki-ingest run 20261102T101809Z (downstream of semantic-article-grouping triage). Tests for the question "does the existing page really cover this article?" before skipping or downgrading a take.

## 1. Dated stub topic-page ≠ covered
A concept page whose filename matches the topic keyword may be a short page frozen months ago that covers only ONE sub-thesis.
- Concrete: `concepts/ai-alignment.md` was 62 lines, `updated: 2026-05-19`, covering only the Positive Alignment paper (May 2026). Sean Goedecke's Nov 2026 "Reliably aligning LLMs is impossible in principle" (Kripke quaddition, shoggoth/no-fixed-goals, motive-incoherence) was a genuine ★★★★☆ gap despite `grep alignment` matching everywhere.
- Same for `concepts/interpretability.md` — it recorded only *technical* limitations, zero *principled* skepticism. An article supplying the missing angle (counter-thesis, opposing view, adjacent dimension) is a take even when the umbrella page exists and is rich.
- **Test**: read page LENGTH + `updated:` date + actual section headings, then ask whether the article's SPECIFIC argument/data is present. Filename/keyword match is not coverage.

## 2. Tiny quote-post can seed a new entity
A sub-1KB Simon Willison quote-post is legitimate new-entity material when (a) the quoted person is a major figure and (b) the wiki-wide grep finds ≤1 incidental mention.
- Concrete: 831B "A quote from Kyle Kingsbury" → `entities/kyle-kingsbury.md` created; prior footprint was a single Jepsen mention inside `entities/dan-luu.md`.
- Do NOT auto-skip small raw files by size alone — the ~500B guideline is soft.

## 3. One flagship essay → multi-page filing pattern
When one landmark article spans concept territories, file the FULL argument in the primary concept page, an angle-specific condensed section in the secondary concept page, and a Core Ideas section on the author entity — with reciprocal `[[wikilinks]]` (ai-alignment + interpretability + seangoedecke-com for the Goedecke essay). The triage's single `candidate_wiki_path` may under-specify this; downstream ingest should widen it, and triage can hint at it in `reason_ja`.

## 4. Reference items with candidate_wiki_path = null
If a reference's target page doesn't exist and the topic is below the concept threshold (e.g. LWN kernel release with AI-code observations, no kernel/LWN page in wiki), record it as a durable lead line in the log.md ingest entry AND rely on the archive (`archive_triage.py`) for later re-evaluation. Do not force a new thin page.

## 5. Ingest-side git/frontmatter pitfalls (see also wiki-ingestion-pipelines skill)
- `related:` frontmatter lists use PLAIN paths (`- entities/foo`), never `[[wikilinks]]` — only body text uses `[[]]`.
- If `git pull --rebase` is blocked by sibling unstaged files, try plain `git push` first — it succeeds when there's no divergence.
- After commit, grep a distinctive phrase per touched page to verify content actually landed (defense vs sibling overwrites).
- New tags: add to SCHEMA.md first, then use — pre-commit tag validator checks ALL staged files.
