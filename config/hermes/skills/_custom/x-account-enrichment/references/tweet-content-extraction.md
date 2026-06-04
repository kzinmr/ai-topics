# Tweet Content Extraction — Tiered Fallback Strategy

When researching tweets for wiki ingestion, the vision API may fail (DeepSeek, some providers don't support image analysis). Use this tiered approach:

## Tier 1: Full API Extraction (PREFERRED)

```bash
xurl --auth oauth2 "/2/tweets/<TWEET_ID>?tweet.fields=article,author_id,entities,referenced_tweets&expansions=attachments.media_keys,author_id,referenced_tweets.id&media.fields=url,alt_text&user.fields=username,name,description,public_metrics&tweet.fields=public_metrics,created_at,conversation_id" | python3 -m json.tool
```

This returns:
- Full tweet text + metrics (likes, bookmarks, retweets, impressions)
- Author profile (username, name, description, follower count)
- Quoted/referenced tweets (full text + metrics)
- Media attachments (URLs, types, alt text)
- Article field (for X Note Tweets / long-form content)

Use `python3 -m json.tool` for readability in terminal output.

## Tier 2: Minimal API (Fallback)

```bash
xurl --auth oauth2 "/2/tweets/<TWEET_ID>?tweet.fields=article&expansions=attachments.media_keys&media.fields=url" | python3 -m json.tool
```

## Tier 3: CLI Read (Metadata Only)

```bash
xurl read <TWEET_ID>
```

Returns `{title}` only — useful for triage, insufficient for wiki ingestion.

## User Profile Lookup

```bash
xurl --auth oauth2 "/2/users/by/username/<handle>?user.fields=description,url,public_metrics" | python3 -m json.tool
```

## Thread/Replies Search (May Return Empty)

```bash
xurl --auth oauth2 "/2/tweets/search/recent?query=conversation_id:<CONVERSATION_ID>&tweet.fields=author_id,created_at&expansions=author_id&user.fields=username&max_results=10"
```

Note: Recent search has a 7-day window. Older threads return empty. Workaround: check `referenced_tweets` in the main tweet's Tier 1 response for quoted tweets.

## Image Extraction (When Vision Unavailable)

If the vision API rejects images (DeepSeek: `unknown variant image_url` error):
1. Use Tier 1 to get `media[].url` — this gives the raw image URL (e.g., `https://pbs.twimg.com/media/HFPDOKNboAEgr9m.jpg`)
2. Save the URL for reference or pass to a vision-capable model later
3. Focus on text content + author research + linked repos for wiki page content

## Common Pitfalls

- **`--auth oauth2` is CRITICAL**: without it, `tweet.fields=article` returns null even for tweets with articles
- **`referenced_tweets.id` must be in expansions** for quoted tweet content to appear in `includes.tweets`
- **`python3 -m json.tool` may fail on API errors**: wrap with `2>/dev/null || echo "FALLBACK" && xurl read <ID>` for resilience
