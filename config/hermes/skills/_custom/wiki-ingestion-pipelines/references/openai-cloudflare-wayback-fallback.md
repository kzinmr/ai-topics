# Recovering blog-ingest "unsaved_articles" (agent-side fallbacks)

When the pre-run `blog_ingest.py` script reports `unsaved_articles`, do NOT just relay them. Try these recovery tiers before giving up:

## Tier A: X/Twitter status URLs (`x.com/user/status/NNN`)
`scrape_url` fails on X (auth wall). Use `xurl read <TWEET_ID>` (terminal, free) — for regular tweets the full `text` + `public_metrics` come back. Save a metadata+text raw article via the same `url_to_filename()`/frontmatter format so downstream triage dedup works. If the tweet has an `article` entity (X long-form), use `xurl --auth oauth2 "/2/tweets/<ID>?tweet.fields=article"` (see x-article-getxapi-fallback skill).

## Tier B: YouTube URLs
`scrape_url` fails (SPA). Run `python3 ~/ai-topics/scripts/youtube_meta.py <ID> --json`. If the video is a comedy sketch / short non-technical clip (check description/keywords), a metadata-only save with a prominent `> **Note**: metadata-only` block is acceptable — full transcript ingestion is not worth it for a viral sketch. Technical talks should go through the `media/youtube-content` skill.

## Tier C: openai.com (and other Cloudflare-challenge pages)
`scrape_url` and plain curl get a ~10KB Cloudflare challenge page (grep for `@keyframes enlarge-appear` or check size <20KB). Recovery: fetch via Wayback Machine —
```bash
curl -sL -A "Mozilla/5.0" "https://web.archive.org/web/2026/https://openai.com/index/<slug>/" -o /tmp/page.html
```
The body is NOT extractable via readability (readability picks an unrelated teaser), but IS in `<article>...</article>` — parse with BeautifulSoup, join `<p>` texts, strip `(opens in a new window)` noise. Note `retrieval: "web.archive.org (direct fetch blocked by Cloudflare challenge)"` in frontmatter. Validated 2026-08-29 on OpenAI "Our decision on Cursor following its acquisition by SpaceX".

## After recovery
1. Append recovered entries to `saved_articles` in BOTH `latest.json` and the run's archive JSON under `${HERMES_HOME}/cron/data/blog_ingest/`, clear `unsaved_articles`, so downstream `blog-triage` sees complete data.
2. Commit only the new raw article files (`git add <specific files>` — the repo working tree often has unrelated dirty skill files). Pre-commit hooks pass on raw articles.
3. Use `terminal` heredoc with `/opt/data/.hermes/venv/bin/python` — system `python3` lacks httpx/readability/bs4, and `execute_code` is blocked in cron mode.
