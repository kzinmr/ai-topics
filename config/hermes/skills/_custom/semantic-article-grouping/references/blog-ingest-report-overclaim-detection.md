# Blog-Ingest Report Overclaim — Verify Ingest Commits, Not Reports

Validated 2026-08-16. Pattern for blog-triage when the upstream blog-ingest run may have
already performed wiki enrichment before triage executes.

## The Pattern

In this deployment, the blog-ingest run (collection step) can itself commit wiki
enrichment — it reads the batch, identifies AI-relevant articles, updates pages, and
commits (e.g. `495a60c7 wiki: blog-ingest 2026-08-16 — augment auggie CLI v2 + goedecke
watermarking + simonwillison CORS chat`). Blog-triage then runs against a checkpoint
whose "AI-relevant" articles are already captured.

The trap: the run's daily-scan report (`inbox/rss-scans/daily-scan-*.md`) carries a
"Wiki更新" column that can **claim** a page was updated when the actual commit never
touched that file.

## Concrete Case (2026-08-16)

- Report claimed: `entities/simon-willison.md` gained a CORS Chat reference entry.
- Commit `495a60c7` actually changed: `ai-text-watermarking.md` (+21),
  `entities/augment.md` (+35), `entities/seangoedecke-com.md` (+22),
  `inbox/rss-scans/daily-scan-2026-08-16.md`, `wiki/log.md`.
- `entities/simon-willison.md` was **not** in the diff at all — yet the commit message
  title listed "simonwillison CORS chat" and the report listed it under Wiki更新.
- Consequence: the CORS Chat article was a genuine (minor) wiki gap. Triage rated it
  ★★★☆☆ reference for `entities/simon-willison.md` so downstream enrichment actually
  adds it.

## Detection Sequence

```bash
# 1. Find the ingest commit that touched today's articles
git log --oneline -8 -- wiki/concepts/... wiki/entities/...
# 2. See exactly which files the commit changed
git show --stat <ingest-commit>
# 3. Confirm whether a claimed page was really touched
git show --name-only <commit> | grep -i <author>
# 4. If absent from the diff, verify the page content itself still lacks the article
grep -n -i "article-title-keyword" wiki/entities/<entity>.md
```

Rules:
- **Do NOT trust** the report's "Wiki更新" column alone.
- **Do NOT trust** the commit message title — it listed "simonwillison CORS chat" while
  the diff omitted that file.
- Cross-check the page body too: a page with `updated: <today>` in frontmatter may have
  been updated for a *different* reason (e.g. an active-crawl concept page), not for
  this article.

## Decision

- Article truly captured (content section in page body + file in commit diff) → skip.
- Claimed-but-not-committed (report says captured, diff says no, body lacks it) → the
  gap is real; rate on the article's merits (minor tool post → ★★★☆☆ reference for the
  author entity page; substantive content → ★★★★☆ take).

## Relation to Other Same-Day Dedup Patterns

Distinct from:
- `blog-triage-duplicate-invocation-recovery.md` — downstream blog-wiki-ingest consumed
  the batch earlier the same day (triage itself duplicates).
- The standard "blog-wiki-ingest already ran" check — here the *blog-ingest* (upstream
  collection) ran enrichment, so `wiki/log.md` shows a blog-ingest line, not a
  blog-wiki-ingest line.
- Dreaming/blog-overnight dedup — overnight processing by a different pipeline.

This one is specifically: **the collection run enriched the wiki itself, and its own
reporting was inaccurate about what it enriched.**
