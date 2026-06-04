# X Article Body Fetch

Fetch full article body from X native articles.

## Method
```bash
xurl -X GET "/2/tweets/<TWEET_ID>?tweet.fields=article,entities"
```
⚠️ NEVER use `-v` flag. 

## Response Fields (extract ALL)
| Field | Description | Always process? |
|-------|-------------|-----------------|
| `plain_text` | **Full article body** | ✅ ALWAYS |
| `title` | Article title | ✅ |
| `preview_text` | Short preview | ✅ |
| `cover_media` | Cover media ID | Optional |
| `entities` | Tweet metadata (mentions, urls) | ✅ For links |

## Fallback
If API fails, use browser: `https://x.com/i/article/<article_id>`

## Known Issues
- `-v` flag breaks JSON parsing
- `article.fields=content` is invalid — use `plain_text`
- tweet ID and article ID may differ for the same content
