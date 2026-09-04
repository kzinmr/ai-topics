# Reddit URL Resolution Pattern

When a user provides a Reddit URL (especially short `/s/` format), Reddit often blocks automated access (JSON API, RSS, old.reddit.com all return "Blocked" or verification pages). Use this resolution pattern to get the actual content.

## Short URL Resolution

Reddit short URLs use format: `https://www.reddit.com/r/{subreddit}/s/{id}`

**Step 1: Resolve the redirect**
```bash
curl -s -I -L "https://www.reddit.com/r/LocalLLaMA/s/RMqtna7JMK" 2>/dev/null | grep -i "location"
```
This returns the canonical URL: `https://www.reddit.com/r/LocalLLaMA/comments/1u6s6pm/stop_using_ollama/?share_id=...`

**Step 2: Extract the post ID**
From the canonical URL, extract the post ID (e.g., `1u6s6pm`).

## Finding the Source Article

Reddit posts often link to external articles. The Reddit post itself is usually a discussion wrapper.

**Step 3: Check HN for the same content**
Many popular Reddit posts get discussed on HN. Search the HN API:
```bash
# Search HN for the article title or keywords
curl -s "https://hacker-news.firebaseio.com/v0/topstories.json" | python3 -c "
import json, sys
# Get top stories, then search for matching titles
"
```

Or use Algolia HN search API:
```bash
curl -s "https://hn.algolia.com/api/v1/search?query=TITLE_KEYWORDS&tags=story" | python3 -c "
import json, sys
data = json.load(sys.stdin)
for hit in data.get('hits', []):
    print(f\"ID: {hit['objectID']} | Title: {hit['title']} | URL: {hit.get('url','')}\")
"
```

**Step 4: Get the source article from HN**
```bash
curl -s "https://hacker-news.firebaseio.com/v0/item/{HN_ID}.json" | python3 -c "
import json, sys
data = json.load(sys.stdin)
print(f\"Title: {data['title']}\")
print(f\"URL: {data.get('url','')}\")
print(f\"Score: {data['score']} | Comments: {data['descendants']}\")
"
```

**Step 5: Scrape the actual article**
Use `curl` on the source URL (not Reddit) to get the full article content.

## Fallback: Direct Reddit Access (Usually Fails)

If the above doesn't work, try these in order (most will fail):
1. `curl -s -L -A "Mozilla/5.0" "https://www.reddit.com/r/{sub}/comments/{id}/.json"` — JSON API
2. `curl -s "https://old.reddit.com/r/{sub}/comments/{id}/"` — old Reddit
3. `curl -s "https://www.reddit.com/r/{sub}/comments/{id}/.rss"` — RSS feed
4. `web_extract()` on the Reddit URL — browser-based extraction

All of these are typically blocked by Reddit's network policy.

## Key Insight

**Don't fight Reddit's blocks.** The short URL redirect (`curl -I -L`) always works because it's a 302 redirect that happens before the block page. Once you have the canonical URL and post ID, use external sources (HN API, Algolia search, web search) to find the actual content being discussed.

## Example Session (June 2026)

User provided: `https://www.reddit.com/r/LocalLLaMA/s/RMqtna7JMK`

1. `curl -s -I -L` → redirect to `/comments/1u6s6pm/stop_using_ollama/`
2. Searched pullpush.io for post ID `1u6s6pm` → returned empty (post too new or archived differently)
3. Searched HN via Algolia for "stop using ollama" → found HN post 47788385 (648 points)
4. HN API returned source URL: `https://sleepingrobots.com/dreams/stop-using-ollama/`
5. Scraped sleepingrobots.com → got full article (34KB HTML, 18K chars of content)
6. Also retrieved top HN comments for community perspective

Total time: ~5 tool calls to go from blocked Reddit URL to full article content.
