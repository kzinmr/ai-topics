# X Article plain_text Pre-Check

## When to Use
When processing X bookmarks that link to X Articles (x.com/i/article/...), BEFORE attempting any API fallback or web extraction.

## The Plain-Text Shortcut

The `fetch_x_bookmarks.py` pre-run script (Section I of wiki-ingestion-pipelines skill) already fetches article content via `xurl --auth oauth2 "/2/tweets/<ID>?tweet.fields=article"` — the equivalent of Tier 1.5 in the x-article-getxapi-fallback skill. When the bookmark metadata shows `article.plain_text` with substantial content (>2KB), the full article body is available directly — no GetXAPI, no web_search, no mirror hunting needed.

## Checklist

Before processing an X Article bookmark:

1. **Check `article.plain_text` size**: If >2KB, the full body is available. Save directly as raw article.
2. **Check `article.title`**: The article title is in the bookmark metadata.
3. **Identify the author**: Use `xurl read <TWEET_ID>` to get the `includes.users[0].username` and `name` fields.
4. **Extract linked references**: `article.entities.urls[]` contains referenced URLs (blogs, papers, documentation).
5. **Check engagement**: `public_metrics` (bookmark_count, like_count, etc.) provides signal strength.

## Successful Session (June 23, 2026)

**Article**: Drew Breunig, "The Problem is Prompt Debt" (tweet ID: 2069455716478603536)
- `article.plain_text`: 10KB of full article body — no API fallback needed
- `article.entities.urls[]`: 20 referenced URLs (arxiv papers, blog posts, documentation)
- Author resolved via simple `xurl read <TWEET_ID>` → Drew Breunig (@dbreunig)
- Engagement: 75 bookmarks, 48 likes, 10 retweets
- **Total processing time**: ~4 minutes from bookmark to committed wiki pages

## Pitfall to Avoid
Don't reach for GetXAPI, web_search mirrors, or browser-based extraction when `article.plain_text` already has the full content. The Tier 1.5 xurl call has already been done by the pre-run script — the content is right there in the bookmark JSON.

## Pitfall: Invisible Unicode in `article.plain_text`

X Article `plain_text` frequently contains invisible Unicode (U+200B zero-width space, etc.) from copy-pasted content. These trigger the cron injection scanner, blocking the entire run. The `fetch_x_bookmarks.py` script now sanitizes article content via `_sanitize_dict()` (recursive Unicode stripping). If the scanner blocks again, see `references/cron-injection-unicode-block.md` for diagnostics and fix procedure.
