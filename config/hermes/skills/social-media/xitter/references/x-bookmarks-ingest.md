# X Bookmarks Ingest Pipeline

Full pipeline details.

## Pre-Run Script: `fetch_x_bookmarks.py`
Location: `~/ai-topics/scripts/fetch_x_bookmarks.py`

Steps:
1. Load processed IDs from `~/.hermes/processed_x_bookmarks.json`
2. Fetch bookmarks: `xurl bookmarks -n 100 --auth oauth2`
3. Dedup: filter tweets whose `id` is in the processed set
4. Extract URLs: collect external URLs (not x.com/twitter.com)
5. Output JSON: `{"new_bookmarks": [...]}`
6. Unbookmark processed: `xurl unbookmark <id> --auth oauth2`
7. Update DB: add all new tweet IDs to processed_x_bookmarks.json

## DB Format
```json
{
  "tweet_ids": ["1234567890", ...],
  "unbookmark_failures": 0
}
```

## Token Expiration
- bookmark.read scope may still work while other scopes fail
- Diagnosis: `timeout 10 xurl --auth oauth2 whoami`
- Fix: user re-authenticates with `xurl --auth oauth2`

## Common Failures
- "No apps registered" → user must run `xurl auth apps add`, then `xurl auth oauth2`, then `xurl auth default`
- X article content: use REST endpoint, not browser
