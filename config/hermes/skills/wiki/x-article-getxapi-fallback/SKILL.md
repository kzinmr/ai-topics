---
name: x-article-getxapi-fallback
description: Fallback approach for retrieving X/Twitter long-form article bodies (x.com/i/article/...) using GetXAPI when xurl cannot access them. GetXAPI bypasses the X auth wall and returns full article content as structured JSON.
trigger: |
  When xurl read <article_id> returns metadata-only or "Could not find tweet" for an X article URL (x.com/i/article/... or x.com/user/status/NNN where the post is just an article link).
environment:
  env_var: GETXAPI_KEY
  api_base: https://api.getxapi.com
---

# GetXAPI Fallback for X Articles

X Articles (long-form posts at `x.com/i/article/<id>`) are **not regular tweets** from the X API's perspective. The X API v2 `/tweets` endpoint cannot resolve article IDs, and xurl returns either:
- `"Could not find tweet with id"` if you query the article ID directly
- Metadata-only (title, author, engagement) without the body if you query the parent tweet

**GetXAPI** (`api.getxapi.com`) provides a dedicated endpoint that returns the full article body as structured JSON blocks (headings, paragraphs, lists, images, inline styles).

## Command

```bash
curl -s -H"Authorization: Bearer $GETXAPI_KEY" \
  "https://api.getxapi.com/twitter/tweet/article?id=<TWEET_ID>"
```

Where `<TWEET_ID>` is the **parent tweet's ID** (the tweet that links to/contains the article), NOT the article ID.

## Response Structure

```json
{
  "status": "success",
  "msg": "success",
  "article": {
    "id": "ArticleEntity:...",
    "author": {
      "userName": "willccbb",
      "name": "will brown",
      "id": "3064259332",
      "isBlueVerified": true,
      "followers": 43172,
      "description": "reward hacking @primeintellect"
    },
    "replyCount": 41,
    "likeCount": 1805,
    "viewCount": 441884,
    "createdAt": "Fri May 01 02:23:07 +0000 2026",
    "title": "On SFT, RL, and on-policy distillation",
    "preview_text": "...",
    "cover_media_img_url": "https://pbs.twimg.com/media/...",
    "contents": [
      {"type": "header-two", "text": "§1 — Section title"},
      {"type": "unstyled", "text": "Paragraph text"},
      {"type": "unordered-list-item", "text": "List item"},
      {"type": "image", "url": "...", "width": 1574, "height": 1306}
    ]
  }
}
```

### Content Block Types

| type | Meaning | Usage |
|------|---------|-------|
| `header-two` | Section heading | `## <text>` in markdown |
| `unstyled` | Paragraph text | Plain paragraph |
| `unordered-list-item` | Bullet point | `- <text>` with raw inline styles |
| `image` | Embedded image | Omit in text version (include URL in frontmatter) |
| `atomic` | Entity block (tables, embeds) | Usually empty text, skip |

### Inline Style Ranges

Each `unstyled` block may have `inlineStyleRanges`:
```json
"inlineStyleRanges": [
  {"length": 49, "offset": 0, "style": "Bold"},
  {"length": 103, "offset": 0, "style": "Italic"}
]
```
Available styles: `"Bold"`, `"Italic"`.

## Retrieval Strategy — Four Tiers

When encountering an X Article URL (`x.com/user/status/NNN` linking to `x.com/i/article/...`):

### Tier 1: xurl metadata (fast, free)
```bash
xurl read <TWEET_ID>
```
Returns: article title, author info, engagement metrics (likes, retweets, bookmarks, impressions). **Does NOT return body text.** Useful for quick triage and raw article frontmatter.

### Tier 2: web_extract preview (medium effort, partial body)
```python
web_extract(url="https://x.com/user/status/<TWEET_ID>")
```
Returns: first several paragraphs of the article text plus metadata. Good enough for wiki summaries and concept extraction when full text isn't critical. **Note:** `xurl /2/tweets/<ID>?tweet.fields=article` times out on long articles — use web_extract instead.

### Tier 3: GetXAPI full body (complete, requires API key)
Use when you need the full structured article content with section headings, inline styles, and image URLs. See the Workflow section below.

**If GETXAPI_KEY is not set**, skip Tier 3 and go directly to Tier 4.

### Tier 4: Secondary source discovery (when GetXAPI unavailable)
When direct retrieval fails (no GETXAPI key, browser unavailable, cookie wall, nitter down), use **web_search** to find news outlets or blogs that published summaries or translations of the article:

```python
web_search(query="<author name> \"<article title>\" <year>")
```

**Effective search patterns:**
- `"<exact article title>" <author handle>` — finds exact matches
- `<author name> <topic keywords>` — finds broader coverage
- Non-English outlets often publish comprehensive summaries (e.g., Chinese tech media like ABMedia 鏈新聞 for high-profile AI articles)

**What to look for in search results:**
- News outlet summaries that reproduce key quotes and structure
- Blog posts that analyze/reference the article with detailed excerpts
- GitHub issues/discussions that quote substantial portions
- Forum threads (Reddit, HN) with user summaries

**Known secondary-source domains for coding-agent articles:**
- **mem0.ai/blog** — Mem0 regularly publishes detailed analysis of agent memory tools (Codex, LangChain, LlamaIndex). When an X Article covers agent memory/harness features, check mem0.ai first — they often republish with full technical depth and working code.
- **blog.langchain.com** — Common mirror for agent engineering articles
- **zylos.ai/research** — Deep architectural analysis of coding agent harnesses
- **abmedia.io** — Chinese tech media with comprehensive English article summaries

**After finding a secondary source:**
1. `web_extract` the secondary article for full content
2. Mark the raw article with `getxapi: false` and `source_fallback: secondary` in frontmatter
3. Add `summary_source: <url>` and `summary_source_name: <outlet name>` to document where the reconstructed content came from
4. Note in the raw article body that content is reconstructed from secondary sources

**Full retrieval chain (tried in order):**
Tier 1 (xurl metadata) → Tier 2 (web_extract tweet URL) → Tier 3 (GetXAPI) → browser_navigate → web_extract article URL → xcancel/nitter → **Tier 4 (web_search → secondary source)** ✅

**Real example (Garry Tan "Meta-Meta-Prompting"):**
- Tiers 1-3 + browser + nitter all failed
- `web_search('Garry Tan "Meta-Meta-Prompting" AI Agents 2026')` → found ABMedia (abmedia.io) Chinese summary
- `web_extract` on ABMedia → comprehensive article with all key concepts, quotes, and architecture details
- Result: produced a complete raw article and concept page from secondary source alone

## Workflow

### Step 0: Quick triage
```bash
xurl read <TWEET_ID>
```
If the response contains `article.title`, it's an X Article (not a regular tweet). Extract the title, author, and engagement metrics from this response.

### Step 1: Extract the tweet ID from the URL
```python
# URL pattern: https://x.com/user/status/2050038277454143918
tweet_id = url.split("/status/")[1].split("?")[0]
```

### Step 2: Fetch article via curl

**⚠️ CRITICAL: Use `terminal` tool with shell variable expansion, NOT `execute_code`.** The `execute_code` tool does NOT inherit environment variables from `${HERMES_HOME}/.env` — `os.environ.get("GETXAPI_KEY")` will return an empty string. The `terminal` tool does inherit shell environment.

**Method A — Terminal (preferred, works reliably):**
```bash
curl -s -H "Authorization: Bearer $GETXAPI_KEY" \
  "https://api.getxapi.com/twitter/tweet/article?id=<TWEET_ID>" \
  > /tmp/hermes_article.json
```
Then process the saved JSON with `execute_code` (no env var needed for file I/O):
```python
import json
with open("/tmp/hermes_article.json") as f:
    data = json.load(f)
article = data["article"]
```

**Method B — execute_code (only if you've confirmed the env var is available):**
First verify: `echo ${GETXAPI_KEY:-(not set)}` in terminal. If set, the key is in `${HERMES_HOME}/.env` but `execute_code` still won't see it — use Method A.

### Step 3: Convert to markdown for raw article
```python
lines = []
for block in article["contents"]:
    t = block["type"]
    text = block.get("text", "").strip()
    if t == "header-two" and text:
        lines.append(f"\n## {text}\n")
    elif t == "unstyled" and text:
        lines.append(f"{text}\n")
    elif t == "unordered-list-item" and text:
        lines.append(f"- {text}")

markdown = "\n".join(lines)
```

### Step 4: Update frontmatter
Mark the article with `getxapi: true` and `source_fallback: false` (to indicate the body WAS retrieved, unlike a pure metadata-only fallback).

## Before/After Comparison

| Aspect | xurl only | xurl + GetXAPI |
|--------|-----------|----------------|
| Article title | ✅ Available in `article.title` field | ✅ Same |
| Author metadata | ✅ Available | ✅ Richer (followers, bio, blue check) |
| Engagement metrics | ✅ like/retweet/reply/quote/bookmark counts | ✅ Same + view count |
| **Article body** | ❌ Not available (auth wall) | ✅ Full text with section structure |
| Inline formatting | N/A | ✅ Bold/italic ranges on each block |
| Embedded images | N/A | ✅ URLs with dimensions |
| Cost | Free with X API credits | Paid (GetXAPI pricing) |

## Pitfalls

- **GetXAPI endpoint may be unavailable** — As of 2026-05-19, `api.getxapi.com/twitter/tweet/article` returned 404 for both tweet IDs and article IDs. The API may have changed. If GetXAPI is down, skip directly to Tier 4 (secondary source discovery). The GitHub repo `xhuisme/getxapi` may have updates.
- **HTTP 500 from X servers** — When the X article itself returns HTTP 500 (X server-side error), ALL direct retrieval methods (xurl, web_extract, GetXAPI, browser) will fail. Go straight to Tier 4 (secondary source discovery via web_search).
- **GetXAPI KEY must be in environment** — Use `$GETXAPI_KEY` which is stored in `${HERMES_HOME}/.env`. Verify it's set before calling: `echo ${GETXAPI_KEY:-(not set)}`. If not set, skip Tier 3 and go directly to Tier 4 (secondary source discovery).
- **`execute_code` does NOT inherit `.env` variables** — `os.environ.get("GETXAPI_KEY")` in Python returns `""` because the `execute_code` sandbox has a clean environment. Always use `terminal` with shell variable expansion (`$GETXAPI_KEY`) for API calls. Save the JSON output to a temp file, then process it with `execute_code` for the conversion step.
- **Secondary sources vary in quality** — Machine-translated summaries may miss nuance. Prefer English-language tech media or bilingual outlets. Always note `summary_source` and `source_fallback: secondary` in frontmatter.
- **Rate limits** — GetXAPI has its own rate limits (typically generous but not unlimited). Cache results on first fetch.
- **Article vs tweet ID confusion** — The endpoint takes the **tweet ID** (the status post that links to the article), NOT the article entity ID. If you pass the article ID, it will fail.
- **Image-only content** — `type: "image"` blocks contain image URLs but no alt text. Just note the URL in the markdown or skip inline rendering.
- **Inline styles need manual reconstruction** — `inlineStyleRanges` are offsets into the raw text. The most reliable approach is to skip complex style reconstruction in the saved raw article and just save the text as-is — the raw article is for reference, not publication.
- **Preview text duplication** — The `preview_text` field often duplicates the first `unstyled` block. Don't double-include it.
- **Compliance note** — GetXAPI is a third-party data broker. Content retrieved this way may have different ToS constraints than direct X API access.
- **Secondary sources vary in quality** — Machine-translated summaries may miss nuance. Prefer English-language tech media or bilingual outlets. Always note `summary_source` and `source_fallback: secondary` in frontmatter.

## Supporting References

- `references/canonical-blog-url-fallback.md` — When an X Article bookmark links to content originally published on the author's blog (Substack, personal site, Medium), skip the X article wrapper and web_search → web_extract the canonical URL instead.
- `references/garry-tan-case-study.md` — Full walkthrough of the 8-step retrieval chain that succeeded via Tier 4 secondary source discovery, with the Garry Tan "Meta-Meta-Prompting" article as a worked example.
- `references/mem0-secondary-source-case-study.md` — Mem0 as a secondary source mirror for coding-agent memory X Articles, with the Codex Memory Pipeline article as a worked example.
- `references/thariq-claude-code-skills-case-study.md` — Clean Tier 3 GetXAPI success path: web_extract → GetXAPI full body → raw article → concept page with mechanism + role taxonomy. Thariq Shihipar's "Lessons from Building Claude Code: How We Use Skills" as a worked example.
