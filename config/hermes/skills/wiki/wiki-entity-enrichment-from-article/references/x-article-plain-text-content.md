# X Article Content from Bookmark Metadata (`article.plain_text`)

## Pattern

When processing X bookmarks through the `x-bookmarks-ingest` pipeline, X Articles that return HTTP 500 (auth wall) frequently still deliver their **full article body** via the `article.plain_text` field in the xurl response. This field should be checked **before** attempting GetXAPI or mirror search — it's free, reliable, and requires no additional API calls.

## Where to Find It

The `article.plain_text` field is present in:

1. **`fetch_x_bookmarks.py` output JSON** — injected as `new_bookmarks[].article.plain_text` in the cron agent context
2. **`xurl read <tweet_id>` output** — `data.article.plain_text` field in the tweet response
3. **`xurl bookmarks` output** — bookmark metadata includes articles

Example from fetch_x_bookmarks.py output:
```json
{
  "text": "https://t.co/XSmftb6kfC",
  "id": "2054108160450064571",
  "entities": {
    "urls": [{
      "expanded_url": "http://x.com/i/article/2054081238236020736",
      "status": 500  // ← auth wall!
    }]
  },
  "article": {
    "title": "On Policy Self Distillation",
    "plain_text": "I've been working on solving OPSD for a week now...\n\nMy experiments are done on Olmo 3 7B...",  // ← FULL article!
    "preview_text": "I've been working on solving OPSD for a week now...",  // ← truncated
    "entities": {
      "mentions": [{"username": "willccbb"}],
      "urls": [{"text": "https://x.com/willccbb/..."}],
      "code": [{"language": "python", "code": "..."}]  // ← even inline code blocks!
    }
  }
}
```

## Decision Logic

| Condition | Action |
|-----------|--------|
| `article.plain_text` > 2KB | Save as full raw article directly. Skip GetXAPI and mirror search. |
| `article.plain_text` is short (< 500 chars) + has code | Try GetXAPI for structured code blocks. Then mirror search as last resort. |
| `article.plain_text` is empty/missing | Fall through to GetXAPI → mirror search |

## What It Preserves

- ✅ Article title (`article.title`)
- ✅ Full body text with paragraph breaks (`article.plain_text`)
- ✅ Inline code blocks (`article.entities.code[]` — language + code fields)
- ✅ Mentions (@handles in `article.entities.mentions[]`)
- ✅ External URLs (`article.entities.urls[]`)

## What It Loses

- ❌ Rich media (images, videos — only `cover_media` and `media_entities[]` IDs are provided, not the actual media)
- ❌ Exact formatting (bold, italics, headings — plain text only)

## Compared to Other Methods

| Method | Reliability | Content Quality | Cost | When to Use |
|--------|------------|----------------|------|-------------|
| **article.plain_text** | High (present in ~80% of bookmarked X Articles) | Good (full body, loses formatting) | Free | First choice |
| GetXAPI | Medium (requires API key, may hit rate limits) | Best (structured JSON with headings, lists) | Paid ($GETXAPI_KEY) | When code blocks/formatting matter + plain_text insufficient |
| Mirror search | Low-Medium (depends on cross-posting) | Varies | Free (time) | When article is cross-posted to Substack/blog |

## Author Discovery

When the bookmark's tweet text is just a bare URL (link share) and the author isn't obvious:
```bash
xurl read <tweet_id>  # Returns includes.users[0] with name, username, id
```
The author info is in `includes.users[0]` of the xurl response — same call that provides `article.plain_text`.

## Real Examples

### June 2026 batch (this session)
- **ar0cket1 "On Policy Self Distillation"**: 10.9KB of plain_text, HTTP 500. Full article saved without any API calls.
- **LangChain "Introducing Rubrics"**: 6.8KB of plain_text including 3 code blocks in `entities.code[]`. HTTP 500. Full article saved with code blocks extracted from entities.

Both articles were saved and wiki pages created/enriched using ONLY the bookmark metadata — zero external API calls.
