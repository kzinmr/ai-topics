# Supplementing blog_ingest articles dropped by the 20-article fetch cap

Validated 2026-11-14 (run 20261114T100030Z).

## When to use

The blog_ingest checkpoint's `articles.total` is a per-run fetch cap (typically 20), while
`scan.total_new` counts ALL new DB articles (e.g. 29). Articles in the gap are still in the
blogwatcher DB (`/opt/data/.blogwatcher/blogwatcher.db`) — query by
`DATE(a.discovered_date)='<run date>'` or `is_read=0` to find them. If dropped articles are
AI-relevant (vendor blogs, OpenAI/Anthropic posts, agent protocol announcements), save them in
a supplemental pass rather than letting them go unread.

## Recipe — reuse canonical save logic, do NOT write a new scraper

```python
# /tmp/blog_ingest_supplement.py
import json, os, sys
sys.path.insert(0, "/opt/data/.hermes/scripts")
os.environ.setdefault("HERMES_HOME", "/opt/data/.hermes")
import blog_ingest as bi

TARGETS = [
    {"blog": "Sierra Blog", "url": "https://sierra.ai/blog/releasing-poppy"},
    # ... one dict per dropped-but-relevant article
]
saved, unsaved = bi.persist_blog_articles({"blog_articles": TARGETS})
print(json.dumps({"saved": saved, "failed": unsaved}, ensure_ascii=False, indent=2))
```

Run it with:

```bash
cd /opt/data/.hermes/scripts && HOME=/opt/data/.hermes /opt/data/.hermes/venv/bin/python /tmp/blog_ingest_supplement.py
```

## Pitfalls

1. **Interpreter**: the system `python3` lacks `httpx` / `readability` / `bs4` —
   `import blog_ingest` raises ModuleNotFoundError. Always use `/opt/data/.hermes/venv/bin/python`.
   This is an interpreter choice, not a broken script.
2. **HOME**: set `HOME=/opt/data/.hermes` (the cron HOME) so the blogwatcher DB path resolves
   (see blogwatcher-db skill pitfall #12).
3. **Read-marking side effect**: `persist_blog_articles()` marks the items read in the DB —
   desired, prevents re-processing next run.
4. **Checkpoint update**: after saving, update BOTH `cron/data/blog_ingest/latest.json` AND the
   run's archive JSON (`blog_ingest_<run_id>.json`):
   - append entries to `saved_articles` (with `raw_path`),
   - remove now-handled URLs from `unsaved_articles`,
   - record everything under a `supplemental` key: `{"note", "extra_saved": [urls], "blocked": {url: desc}}`
     so the blog-triage stage sees the full picture.
5. **Dedup-then-append bug**: when writing the append script, build the dedup URL set and mutate
   the list in the same pass carefully — a first attempt silently no-op'd because `len(saved_articles)`
   stayed 20. Always print `len(d['saved_articles'])` after the append to confirm it grew.
6. **Blocked sources** (returns None from `scrape_url`, don't retry):
   - openai.com news/customer-story pages — Cloudflare bot block
   - bloomberg.com, wired.com — paywall
   - very short release-announcement posts (e.g. simonwillison datasette release notes) —
     `scrape_url` rejects content < 100 chars; acceptable to leave unsaved.
7. **Scan report**: also write `inbox/rss-scans/daily-scan-YYYY-MM-DD.md` summarizing saved,
   blocked, and highlights; commit raw articles + report together:
   `git add wiki/raw/articles/<new files> inbox/rss-scans/... && git commit -m "wiki: blog ingest supplement YYYY-MM-DD (...)" && git push`.
