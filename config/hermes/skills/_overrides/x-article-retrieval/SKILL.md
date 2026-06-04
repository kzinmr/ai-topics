---
name: x-article-retrieval
description: Retrieve full content from X/Twitter's non-standard tweet types — Note Tweets (long-form truncated tweets) and X Articles. Covers detection, field requirements, the critical incompatibility between note_tweet and article fields, and fallback tiers.
trigger: When asked to extract long-form tweet content (Note Tweet or X Article), when fetch_x_bookmarks.py or fetch_x_accounts.py hits _article_fetch_error, when a tweet's text appears truncated (ends with "..."), OR when the user provides an X Article/tweet URL and says "wikiに取り込んで."
---

# X Tweet Content Retrieval — Note Tweets & X Articles

X has two non-standard tweet types that require special retrieval:

| Type | Detection | Full Content Location | Extra API Call? |
|------|-----------|----------------------|-----------------|
| **Note Tweet** | `tweet.text` is truncated (ends with `...`); `note_tweet.text` exists | `note_tweet.text` | **No** — available inline with `tweet.fields=note_tweet` |
| **X Article** | `tweet.article.title` exists | `article.plain_text` | **Yes** — requires separate call with `tweet.fields=article` |

## ⚠️ CRITICAL: Field Incompatibility

**Do NOT mix `note_tweet` and `article` in the same `tweet.fields` request.**

```bash
# ❌ WRONG — article.plain_text may be silently dropped
xurl "/2/tweets/ID?tweet.fields=note_tweet,article"

# ✅ CORRECT — two separate requests
xurl "/2/tweets/ID?tweet.fields=note_tweet"    # for Note Tweets
xurl "/2/tweets/ID?tweet.fields=article"        # for X Articles
```

This is a known X API behavior. The fields interact poorly and `article.plain_text` is silently dropped from the response when both are requested. All scripts (`fetch_x_bookmarks.py`, `fetch_x_accounts.py`) intentionally request only `note_tweet` in their main fetch and make a separate `tweet.fields=article` call for article body retrieval.

---

## Note Tweets (Long-Form Tweets)

Note Tweets are regular tweets whose body exceeds the standard display limit. The API returns a truncated `text` (typically ~140 chars with `...`) and the full content in `note_tweet.text`.

### Detection

```python
def _has_note_tweet(tweet):
    nt = tweet.get("note_tweet") or {}
    return bool(nt.get("text"))
```

### Retrieval

Add `note_tweet` to `tweet.fields` in ANY tweet endpoint:

```bash
xurl "/2/tweets/<TWEET_ID>?tweet.fields=note_tweet"
xurl "/2/users/<USER_ID>/tweets?tweet.fields=note_tweet"
xurl "/2/users/<USER_ID>/bookmarks?tweet.fields=note_tweet"
```

Response includes full text in `data.note_tweet.text`:

```json
{
  "data": {
    "id": "2052100726608781363",
    "text": "Strong Opinions, Loosely Held on... (truncated)",
    "note_tweet": {
      "text": "Strong Opinions, Loosely Held on Agent + Harness Engineering:\n\n1. You can outperform any default harness+model..."
    }
  }
}
```

### Key Facts
- **No extra API call needed** — `note_tweet.text` comes inline when the field is requested
- **Works on all tweet endpoints** — bookmarks, user timelines, search, single tweet lookup
- **`xurl read <ID>` returns TRUNCATED text** — must use raw v2 endpoint with `tweet.fields=note_tweet`
- **Signal**: High bookmark count (500+), author known for long-form analysis

---

## X Articles (x.com/i/article/...)

X Articles are a separate long-form content type. The tweet that shares an article contains `article.title` in the basic response, but `article.plain_text` (the full body) requires an explicit `tweet.fields=article` request with OAuth2 user auth.

### Detection

```python
def _is_article_tweet(tweet):
    article = tweet.get("article") or {}
    return bool(article.get("title"))
```

### Retrieval — Primary Method

```bash
xurl --auth oauth2 "/2/tweets/<TWEET_ID>?tweet.fields=article"
```

Returns:

```json
{
  "data": {
    "article": {
      "title": "...",
      "plain_text": "full article body...",
      "preview_text": "first few lines...",
      "cover_media": "media_id",
      "entities": { "mentions": [...], "urls": [...] }
    },
    "text": "https://t.co/...",
    "id": "TWEET_ID"
  }
}
```

### ❌ What Does NOT Work

```bash
# Gives only title, no body
xurl read <TWEET_ID>

# Returns 404 or empty
web_extract "https://x.com/i/article/<ARTICLE_ID>"

# Returns 453 (insufficient access) for app-only bearer tokens
curl "https://x.com/i/api/2/tweets/<TWEET_ID>/article?..."
```

### Additional Response Fields

Beyond `plain_text` and `title`, the X Article response includes useful structured metadata in `article.entities`:

```json
{
  "article": {
    "entities": {
      "hashtags": [
        {"start": 0, "end": 13, "text": "productivity"},
        {"start": 14, "end": 22, "text": "machine"}
      ],
      "mentions": [
        {"start": 7, "end": 16, "username": "cyrilXBT"}
      ]
    }
  }
}
```

- **`hashtags`**: All hashtags found in the article body with character offsets — useful for auto-tagging wiki pages
- **`mentions`**: All @mentions with usernames — useful for cross-referencing entity pages
- **`cover_media`**: Media ID for the article cover image
- **`preview_text`**: First few lines, useful for summaries without fetching the full body

To also get `created_at` (publication date for wiki filenames), make a **separate** request with `tweet.fields=created_at,author_id` (not `tweet.fields=article`). When fetching metadata-only, the `article.title` is still present but `article.plain_text` is NOT — confirming the field incompatibility is real and consistent.

### Confirmed Working Example (2026-05-27)

```bash
# Step 1: Fetch article body
xurl --auth oauth2 "/2/tweets/2058373087330959829?tweet.fields=article"
# → article.plain_text: full 5000+ word Obsidian vault guide

# Step 2: Fetch metadata (separate call, different tweet.fields)
xurl --auth oauth2 "/2/tweets/2058373087330959829?tweet.fields=created_at,author_id"
# → created_at: "2026-05-24T02:22:41.000Z", author_id: "1373665408193036293"
```

### Error Categories (from fetch_x_bookmarks.py)

| Error Category | Meaning | Action |
|---|---|---|
| `http_5xx` | X API server error (500) | Retry once. If persistent, fall back to Tier 4. |
| `timeout` | Request timed out | Retry once with longer timeout. If persistent, fall back to Tier 4. |
| `no_plain_text` | Article field present but body missing | Article may be too new (not yet processed). Wait and retry. |
| `no_article_field` | Response has no article field at all | Not an X Article tweet. Check tweet type. |
| `xurl_error` | Other xurl error | Fall back to Tier 4. |
| `parse_error` | JSON parse failure | Fall back to Tier 4. |

### Fallback Tiers

- **Tier 2**: `web_extract` on `https://x.com/i/status/<TWEET_ID>` — may get partial body for embedded article tweets
- **Tier 3**: GetXAPI — `curl "https://api.getxapi.com/twitter/tweet/article?id=<TWEET_ID>" -H "Authorization: Bearer $GETXAPI_KEY"` (requires subscription)
- **Tier 4**: `web_search` for `"<article title>" <author_handle>` — secondary sources, mirrors, or summaries

---

## Decision Flow: Note Tweet vs X Article

```
Tweet received
  ├── note_tweet.text present? → Note Tweet → use note_tweet.text (no extra call)
  ├── article.title present?   → X Article → fetch with tweet.fields=article
  └── neither                   → Regular tweet → use text field
```

---

## Script Integration

### fetch_x_bookmarks.py
- Requests `tweet.fields=created_at,entities,referenced_tweets,note_tweet`
- Note Tweets: `note_tweet.text` comes inline — counted as `note_tweets_found`
- X Articles: detected via `_is_x_article()`, separate `fetch_article_body()` call
- Counters in summary: `note_tweets_found`, `x_articles_fetched`, `x_articles_failed`

### fetch_x_accounts.py
- Requests `tweet.fields=created_at,entities,referenced_tweets,note_tweet`
- Note Tweets: `note_tweet.text` used in `compact_post()` via `_get_full_tweet_text()`
- X Articles: detected via `_is_article_tweet()`, separate `fetch_article_body()` call
- `content_type` tag in compact post: `"note_tweet"`, `"x_article"`, or `"tweet"`
- Counters in scan_meta: `note_tweets_found`, `articles_fetched`, `articles_failed`

---

## Reference Implementation

### Note Tweet extraction (no extra API call)
```python
def _get_full_tweet_text(tweet):
    if tweet.get("note_tweet", {}).get("text"):
        return tweet["note_tweet"]["text"]
    return tweet.get("text", "")

# Usage in compact_post / is_substantive_post:
text = " ".join((_get_full_tweet_text(tweet) or "").split())
```

### X Article body fetching (separate API call)
```python
def fetch_article_body(tweet_id):
    """Fetch full X Article body via tweet.fields=article."""
    try:
        resp = json.loads(
            run(f"/2/tweets/{tweet_id}?tweet.fields=article")
        )
        article = resp.get("data", {}).get("article")
        if article and article.get("plain_text"):
            return article, None, None
        if article:
            return None, "no_plain_text", "article field present but plain_text missing"
        return None, "no_article_field", "response has no article field at all"
    except XurlError as e:
        msg = str(e)
        if "500" in msg:
            return None, "http_5xx", msg
        if "timeout" in msg.lower() or "timed out" in msg.lower():
            return None, "timeout", msg
        return None, "xurl_error", msg
    except json.JSONDecodeError as e:
        return None, "parse_error", str(e)
```

---

## Pitfalls

- **Mixing `note_tweet` + `article` in tweet.fields → silent data loss** — `article.plain_text` is dropped. Always use separate requests.
- **`xurl read` does NOT fetch Note Tweet full text or Article body** — always use raw v2 endpoint with explicit `tweet.fields`.
- **OAuth2 is mandatory for X Article body** — app-only bearer tokens get 453.
- **Article ID ≠ Tweet ID** — `x.com/i/article/ID` is the article resource, not the tweet.
- **New articles may not have plain_text yet** — X processes asynchronously. Retry after a few minutes.
- **`note_tweet` field works on ALL tweet endpoints** — bookmarks, timelines, search, single lookup. No special endpoint needed.
