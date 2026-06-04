# X/Twitter Conversation Thread Search

## Use Case
When analyzing X/Twitter discussions — evaluating claims, understanding community reactions, tracing debates — you need the **full conversation thread** with all replies, not just the root tweet. This pattern reconstructs complete threads from a root tweet's `conversation_id`.

## Primary Pattern: `search/recent` with `conversation_id`

```bash
xurl --auth oauth2 "/2/tweets/search/recent?query=conversation_id:<TWEET_ID>&tweet.fields=note_tweet,created_at,author_id&max_results=50"
```

**Parameters:**
- `conversation_id:<TWEET_ID>` — the root tweet's ID (also its conversation_id)
- `tweet.fields=note_tweet` — captures long-form Note Tweets in replies
- `max_results=50` — maximum per page (free tier limit)

**Response:** Array of reply tweets in `data[]`, reverse-chronological (newest first).

### Pagination: `until_id`

When a conversation has more than 50 replies, paginate with `until_id` using the **oldest** tweet ID from the previous page:

```bash
# Page 1
xurl --auth oauth2 "/2/tweets/search/recent?query=conversation_id:2060071701879066626&tweet.fields=note_tweet,created_at,author_id&max_results=50"

# Find the smallest tweet ID in the results → use as until_id for page 2
xurl --auth oauth2 "/2/tweets/search/recent?query=conversation_id:2060071701879066626&tweet.fields=note_tweet,created_at,author_id&max_results=50&until_id=2060153363300286636"
```

**Important:** `until_id` is **exclusive** — tweets with ID ≤ until_id are excluded. Pass the smallest ID from page 1 to get the next batch.

## Real-World Example: a1zhang RLM Debate (May 2026)

Root tweet: `2060071701879066626` — a1zhang's claim that Opus 4.8 + Dynamic Workflows ≈ trained RLM

```bash
# Get root tweet first
xurl --auth oauth2 "/2/tweets/2060071701879066626?tweet.fields=note_tweet,created_at,author_id"

# Get all replies
xurl --auth oauth2 "/2/tweets/search/recent?query=conversation_id:2060071701879066626&tweet.fields=note_tweet,created_at,author_id&max_results=50"
```

Result: ~50+ replies from ~24 hours of discussion, including debate between a1zhang, @willdepue, @lateinteraction, and others.

## Why Not `xurl search` Shortcut?

The `xurl search "..." -n 50` shortcut uses the general search endpoint, not the conversation-specific query. For thread reconstruction, the raw v2 endpoint with `conversation_id` parameter is more reliable — it returns ALL replies to a specific thread, not just keyword matches.

## Limitations (Free Tier)

- **Time window**: `search/recent` covers ~7 days. Threads older than 7 days require direct tweet ID lookups (`/2/tweets/{ID}`) or Nitter fallback.
- **Rate limits**: Standard free-tier rate limits apply.
- **Deleted tweets**: Won't appear in results.

## Integration with Wiki Workflows

When analyzing X/Twitter-based discussions for wiki enrichment:
1. Fetch the root tweet with `tweet.fields=note_tweet` to capture long-form content
2. Fetch the full conversation thread with `conversation_id` search
3. Extract key perspectives, counterarguments, and consensus from replies
4. Cite specific reply IDs in wiki pages for traceability
