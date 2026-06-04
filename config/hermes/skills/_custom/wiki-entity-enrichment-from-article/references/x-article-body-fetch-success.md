# X Article: Successful Body Fetch via xurl

## When the Body IS Available

When the xurl bookmark pipeline successfully fetches the article body (via `tweet.fields=article`), the response includes:

```json
{
  "article": {
    "plain_text": "Full article text here...",
    "preview_text": "Preview excerpt...",
    "title": "Article Title",
    "entities": {
      "urls": [{"text": "https://..."}]
    },
    "cover_media": "3_XXXX",
    "media_entities": ["3_XXXX", ...]
  }
}
```

### What to Do

1. **Save `article.plain_text` directly** as a raw article with frontmatter:
   ```yaml
   type: x_article
   x_article_title: "Article Title"
   x_article_author: "Author Name"
   x_article_url: "https://x.com/i/article/ARTICLE_ID"
   getxapi: false
   source: "X bookmarks ingestion (xurl)"
   ingested: YYYY-MM-DD
   bookmark_tweet_id: "TWEET_ID"
   ```

2. **Do NOT try `web_extract` or `browser_navigate`** on the x.com article URL — the body is already in the data. This saves time and avoids auth walls.

3. **Use `article.title`** for the heading, `article.preview_text` for excerpt, `article.entities` for cross-references.

4. **Process normally** through wiki enrichment workflow (concept pages, entity pages, etc.).

## When Body Fetch FAILS

See the main skill's "X Article Auth Wall & Metadata-Only Fallback" section for the multi-tier fallback workflow (web_extract → GetXAPI → secondary source search).

## Distinction from Auth-Walled Articles

| Case | Signal | Action |
|------|--------|--------|
| Body fetched | `article.plain_text` is present and non-empty | Save directly, process fully |
| Auth wall / metadata-only | `article.title` present but `plain_text` missing or <500 chars | Run fallback tiers |
| No article at all | No `article` field | Skip or treat as regular tweet |
