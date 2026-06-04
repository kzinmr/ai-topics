# X Article Processing: Body Already Fetched vs. Auth Wall

This reference distinguishes two distinct X Article processing cases and when to use each approach.

## Case A: Body Already Fetched (Cron Bookmark Pipeline)

**When `article.plain_text` is already populated in the bookmark data.**

The `fetch_x_bookmarks.py` cron script fetches article bodies via `tweet.fields=article`. When `article.plain_text` is present, the full article content is already available.

### Workflow

1. Save the `article.plain_text` content directly as a raw article — **do NOT web_extract or browser_navigate to the x.com URL**
2. Frontmatter:
   ```yaml
   type: x_article
   x_article_title: "Article Title"
   x_article_author: "Author Name"
   x_article_url: "https://x.com/i/article/NNN"
   getxapi: false
   date: YYYY-MM-DD
   ```
3. Use `article.title` for the title, `article.preview_text` for excerpt, `article.entities` for mentions/links
4. Proceed to normal wiki enrichment workflow

### Detection

- `article.plain_text` field is populated (non-null, non-empty)
- Often 10KB+ of content
- `article.title` and `article.preview_text` are also typically available

## Case B: Body NOT Fetched (Auth Wall / Metadata-Only)

**When `article.plain_text` is missing, empty, or too short (<1KB).**

This is the case covered in the main skill's "X Article Auth Wall & Metadata-Only Fallback" section.

### Detection

- `article.plain_text` is null/empty/very short
- Check `_article_fetch_error_category` and `_retrieval_hints` fields
- `article.title` may still be available

### Fallback Tiers (from the main skill)

1. Tier 2: `web_extract(url="https://x.com/i/status/{tweet_id}")` 
2. Tier 3: GetXAPI via `curl`
3. Tier 4: Secondary source search (Substack mirrors, etc.)

## Key Pitfall

**Do NOT attempt web_extract on the x.com article URL when Case A applies.** The content is already in `article.plain_text` — scraping the same URL will fail (returns HTTP 500 for auth-walled X articles) and waste API calls.
