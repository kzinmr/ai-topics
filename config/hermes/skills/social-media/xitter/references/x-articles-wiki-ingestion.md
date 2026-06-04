# X Articles Wiki Ingestion — Manual Extraction

Manual extraction of X native article bodies from tweet IDs and wiki page creation.

## When to Use
- User provides tweet IDs for X native articles
- Cron pipeline missed article body extraction
- Raw articles exist but only contain metadata (no full body)

## Workflow
1. Fetch article body: `xurl -X GET "/2/tweets/<TWEET_ID>?tweet.fields=article,entities"`
2. Parse: extract plain_text (full body), title, preview_text, cover_media, entities
3. Save: `~/wiki/raw/articles/<TWEET_ID>_<slug>.md`
4. Create/update wiki entity/concept pages
5. Update index.md and log.md
6. Commit: `cd ~/ai-topics && git add wiki/ && git commit -m "wiki: X bookmark ingest — <N> articles" && git push`

## Edge Cases
- Article body < 1KB → metadata-only, try web_search with title + author handle
- Rate limiting → space requests 2-3s apart
- Auth failures → check `xurl auth status`, re-auth if expired
- Duplicate detection → search entities/ before creating
