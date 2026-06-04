---
name: xurl
description: Interact with X/Twitter via xurl, the official X API CLI. Use for posting, replying, quoting, searching, timelines, mentions, likes, reposts, bookmarks, follows, DMs, media upload, and raw v2 endpoint access.
version: 1.4.0
author: xdevplatform + openclaw + Hermes Agent
license: MIT
platforms: [linux, macos]
prerequisites:
  commands: [xurl]
metadata:
  hermes:
    tags: [twitter, x, social-media, xurl, official-api]
    homepage: https://github.com/xdevplatform/xurl
    upstream_skill: https://github.com/openclaw/openclaw/blob/main/skills/xurl/SKILL.md
---

# xurl — X (Twitter) API via the Official CLI

`xurl` is the X developer platform's official CLI for the X API. It supports shortcut commands for common actions AND raw curl-style access to any v2 endpoint. All commands return JSON to stdout.

Use this skill for:
- posting, replying, quoting, deleting posts
- searching posts and reading timelines/mentions
- liking, reposting, bookmarking
- following, unfollowing, blocking, muting
- direct messages
- media uploads (images and video)
- raw access to any X API v2 endpoint
- multi-app / multi-account workflows

This skill replaces the older `xitter` skill (which wrapped a third-party Python CLI). `xurl` is maintained by the X developer platform team, supports OAuth 2.0 PKCE with auto-refresh, and covers a substantially larger API surface.

---

## Secret Safety (MANDATORY)

Critical rules when operating inside an agent/LLM session:

- **Never** read, print, parse, summarize, upload, or send `~/.xurl` to LLM context.
- **Never** ask the user to paste credentials/tokens into chat.
- The user must fill `~/.xurl` with secrets manually on their own machine.
- **Never** recommend or execute auth commands with inline secrets in agent sessions.
- **Never** use `--verbose` / `-v` in agent sessions — it can expose auth headers/tokens.
- To verify credentials exist, only use: `xurl auth status`.

Forbidden flags in agent commands (they accept inline secrets):
`--bearer-token`, `--consumer-key`, `--consumer-secret`, `--access-token`, `--token-secret`, `--client-id`, `--client-secret`

App credential registration and credential rotation must be done by the user manually, outside the agent session. After credentials are registered, the user authenticates with `xurl auth oauth2` — also outside the agent session. Tokens persist to `~/.xurl` in YAML. Each app has isolated tokens. OAuth 2.0 tokens auto-refresh.

---

## Installation

Pick ONE method. On Linux, the shell script or `go install` are the easiest.

```bash
# Shell script (installs to ~/.local/bin, no sudo, works on Linux + macOS)
curl -fsSL https://raw.githubusercontent.com/xdevplatform/xurl/main/install.sh | bash

# Homebrew (macOS)
brew install --cask xdevplatform/tap/xurl

# npm
npm install -g @xdevplatform/xurl

# Go
go install github.com/xdevplatform/xurl@latest
```

Verify:

```bash
xurl --help
xurl auth status
```

If `xurl` is installed but `auth status` shows no apps or tokens, the user needs to complete auth manually — see the next section.

---

## One-Time User Setup (user runs these outside the agent)

These steps must be performed by the user directly, NOT by the agent, because they involve pasting secrets. Direct the user to this block; do not execute it for them.

1. Create or open an app at https://developer.x.com/en/portal/dashboard
2. Set the redirect URI to `http://localhost:8080/callback`
3. Copy the app's Client ID and Client Secret
4. Register the app locally (user runs this):
   ```bash
   xurl auth apps add my-app --client-id YOUR_CLIENT_ID --client-secret YOUR_CLIENT_SECRET
   ```
5. Authenticate (specify `--app` to bind the token to your app):
   ```bash
   xurl auth oauth2 --app my-app
   ```
   (This opens a browser for the OAuth 2.0 PKCE flow.)

   If X returns a `UsernameNotFound` error or 403 on the post-OAuth `/2/users/me` lookup, pass your handle explicitly (xurl v1.1.0+):
   ```bash
   xurl auth oauth2 --app my-app YOUR_USERNAME
   ```
   This binds the token to your handle and skips the broken `/2/users/me` call.
6. Set the app as default so all commands use it:
   ```bash
   xurl auth default my-app
   ```
7. Verify:
   ```bash
   xurl auth status
   xurl whoami
   ```

After this, the agent can use any command below without further setup. OAuth 2.0 tokens auto-refresh.

> **Common pitfall:** If you omit `--app my-app` from `xurl auth oauth2`, the OAuth token is saved to the built-in `default` app profile — which has no client-id or client-secret. Commands will fail with auth errors even though the OAuth flow appeared to succeed. If you hit this, re-run `xurl auth oauth2 --app my-app` and `xurl auth default my-app`.

---

## Quick Reference

| Action | Command |
| --- | --- |
| Post | `xurl post "Hello world!"` |
| Reply | `xurl reply POST_ID "Nice post!"` |
| Quote | `xurl quote POST_ID "My take"` |
| Delete a post | `xurl delete POST_ID` |
| Read a post | `xurl read POST_ID` |
| Search posts | `xurl search "QUERY" -n 10` |
| Who am I | `xurl whoami` |
| Look up a user | `xurl user @handle` |
| Home timeline | `xurl timeline -n 20` |
| Mentions | `xurl mentions -n 10` |
| Like / Unlike | `xurl like POST_ID` / `xurl unlike POST_ID` |
| Repost / Undo | `xurl repost POST_ID` / `xurl unrepost POST_ID` |
| Bookmark / Remove | `xurl bookmark POST_ID` / `xurl unbookmark POST_ID` |
| List bookmarks / likes | `xurl bookmarks -n 10` / `xurl likes -n 10` |
| Follow / Unfollow | `xurl follow @handle` / `xurl unfollow @handle` |
| Following / Followers | `xurl following -n 20` / `xurl followers -n 20` |
| Block / Unblock | `xurl block @handle` / `xurl unblock @handle` |
| Mute / Unmute | `xurl mute @handle` / `xurl unmute @handle` |
| Send DM | `xurl dm @handle "message"` |
| List DMs | `xurl dms -n 10` |
| Upload media | `xurl media upload path/to/file.mp4` |
| Media status | `xurl media status MEDIA_ID` |
| List apps | `xurl auth apps list` |
| Remove app | `xurl auth apps remove NAME` |
| Set default app | `xurl auth default APP_NAME [USERNAME]` |
| Per-request app | `xurl --app NAME /2/users/me` |
| Auth status | `xurl auth status` |

Notes:
- `POST_ID` accepts full URLs too (e.g. `https://x.com/user/status/1234567890`) — xurl extracts the ID.
- Usernames work with or without a leading `@`.

---

## Command Details

### Posting

```bash
xurl post "Hello world!"
xurl post "Check this out" --media-id MEDIA_ID
xurl post "Thread pics" --media-id 111 --media-id 222

xurl reply 1234567890 "Great point!"
xurl reply https://x.com/user/status/1234567890 "Agreed!"
xurl reply 1234567890 "Look at this" --media-id MEDIA_ID

xurl quote 1234567890 "Adding my thoughts"
xurl delete 1234567890
```

### Reading & Search

```bash
xurl read 1234567890
xurl read https://x.com/user/status/1234567890

xurl search "golang"
xurl search "from:elonmusk" -n 20
xurl search "#buildinpublic lang:en" -n 15
```

### Users, Timeline, Mentions

```bash
xurl whoami
xurl user elonmusk
xurl user @XDevelopers

xurl timeline -n 25
xurl mentions -n 20
```

### Engagement

```bash
xurl like 1234567890
xurl unlike 1234567890

xurl repost 1234567890
xurl unrepost 1234567890

xurl bookmark 1234567890
xurl unbookmark 1234567890

xurl bookmarks -n 20
xurl likes -n 20
```

### Social Graph

```bash
xurl follow @XDevelopers
xurl unfollow @XDevelopers

xurl following -n 50
xurl followers -n 50

# Another user's graph
xurl following --of elonmusk -n 20
xurl followers --of elonmusk -n 20

xurl block @spammer
xurl unblock @spammer
xurl mute @annoying
xurl unmute @annoying
```

### Direct Messages

```bash
xurl dm @someuser "Hey, saw your post!"
xurl dms -n 25
```

### Media Upload

```bash
# Auto-detect type
xurl media upload photo.jpg
xurl media upload video.mp4

# Explicit type/category
xurl media upload --media-type image/jpeg --category tweet_image photo.jpg

# Videos need server-side processing — check status (or poll)
xurl media status MEDIA_ID
xurl media status --wait MEDIA_ID

# Full workflow
xurl media upload meme.png                  # returns media id
xurl post "lol" --media-id MEDIA_ID
```

---

## Raw API Access

The shortcuts cover common operations. For anything else, use raw curl-style mode against any X API v2 endpoint:

```bash
# GET
xurl /2/users/me

# POST with JSON body
xurl -X POST /2/tweets -d '{"text":"Hello world!"}'

# DELETE / PUT / PATCH
xurl -X DELETE /2/tweets/1234567890

# Custom headers
xurl -H "Content-Type: application/json" /2/some/endpoint

# Force streaming
xurl -s /2/tweets/search/stream

# Full URLs also work
xurl https://api.x.com/2/users/me
```

---

## Global Flags

| Flag | Short | Description |
| --- | --- | --- |
| `--app` | | Use a specific registered app (overrides default) |
| `--auth` | | Force auth type: `oauth1`, `oauth2`, or `app` |
| `--username` | `-u` | Which OAuth2 account to use (if multiple exist) |
| `--verbose` | `-v` | **Forbidden in agent sessions** — leaks auth headers |
| `--trace` | `-t` | Add `X-B3-Flags: 1` trace header |

---

## Streaming

Streaming endpoints are auto-detected. Known ones include:

- `/2/tweets/search/stream`
- `/2/tweets/sample/stream`
- `/2/tweets/sample10/stream`

Force streaming on any endpoint with `-s`.

---

## Output Format

All commands return JSON to stdout. Structure mirrors X API v2:

```json
{ "data": { "id": "1234567890", "text": "Hello world!" } }
```

Errors are also JSON:

```json
{ "errors": [ { "message": "Not authorized", "code": 403 } ] }
```

---

## Common Workflows

### Post with an image
```bash
xurl media upload photo.jpg
xurl post "Check out this photo!" --media-id MEDIA_ID
```

### Reply to a conversation
```bash
xurl read https://x.com/user/status/1234567890
xurl reply 1234567890 "Here are my thoughts..."
```

### Search and engage
```bash
xurl search "topic of interest" -n 10
xurl like POST_ID_FROM_RESULTS
xurl reply POST_ID_FROM_RESULTS "Great point!"
```

### Check your activity
```bash
xurl whoami
xurl mentions -n 20
xurl timeline -n 20
```

### Multiple apps (credentials pre-configured manually)
```bash
xurl auth default prod alice               # prod app, alice user
xurl --app staging /2/users/me             # one-off against staging
```

---

## Auth Mode Diagnosis

When you get 401 errors, identify *which* auth mode is failing. xurl supports three mutually independent auth modes:

| `--auth` flag | Auth type | Token source | Typical expiry | Use case |
| --- | --- | --- | --- | --- |
| `oauth2` (or no flag / default) | OAuth 2.0 PKCE (user auth) | Interactive browser flow, auto-refresh | Long-lived (auto-refreshes) | Interactive CLI, user-scoped API calls |
| `app` | OAuth 2.0 Client Credentials (app-only) | App-level client-id/secret | Shorter TTL, can expire independently | Automated scripts, batch processing |
| `oauth1` | OAuth 1.0a (user auth) | Consumer key/secret + access token | Never expires (unless revoked) | Legacy integration |

**Diagnostic flow — test each mode in isolation:**

```bash
# Test default/OAuth2 mode (usually the most reliable)
xurl user @handle

# Test app-only mode
xurl --auth app user @handle

# Test OAuth1 mode
xurl --auth oauth1 user @handle
```

- If **only one mode returns 401** (e.g., `--auth app` fails but default works), that mode's token/credential is expired or rate-limited. Patch scripts to use a working mode.
- If **all modes return 401**, the issue is broader (network, X API outage, credential deletion).
- If **default/no-flag works but `--auth app` fails**, the app-only OAuth2 Client Credentials token expired. Switch to `--auth oauth2` or omit `--auth` entirely to use the user's PKCE token.

**Common scenario — batch scripts hardcoding `--auth app`:**  
Some internal scripts (e.g., `fetch_x_accounts.py`) explicitly pass `--auth app`. When the app-only credential expires, those scripts fail completely while interactive `xurl` commands still work. Fix: change `--auth app` to `--auth oauth2` in the script (or remove the flag to use the default).

---

## Error Handling

- Non-zero exit code on any error.
- API errors are still printed as JSON to stdout, so you can parse them.
- Auth errors → have the user re-run `xurl auth oauth2` outside the agent session.
- Commands that need the caller's user ID (like, repost, bookmark, follow, etc.) will auto-fetch it via `/2/users/me`. An auth failure there surfaces as an auth error.

---

## Agent Workflow

1. Verify prerequisites: `xurl --help` and `xurl auth status`.
2. **Check default app has credentials.** Parse the `auth status` output. The default app is marked with `▸`. If the default app shows `oauth2: (none)` but another app has a valid oauth2 user, tell the user to run `xurl auth default <that-app>` to fix it. This is the most common setup mistake — the user added an app with a custom name but never set it as default, so xurl keeps trying the empty `default` profile.
3. If auth is missing entirely, stop and direct the user to the "One-Time User Setup" section — do NOT attempt to register apps or pass secrets yourself.
4. Start with a cheap read (`xurl whoami`, `xurl user @handle`, `xurl search ... -n 3`) to confirm reachability.
5. Confirm the target post/user and the user's intent before any write action (post, reply, like, repost, DM, follow, block, delete).
6. Use JSON output directly — every response is already structured.
7. Never paste `~/.xurl` contents back into the conversation.

---

## Retrieving Old Tweets Beyond API Limits (Free Tier)

The X API free tier has a hard time-window limit: `/2/tweets/search/recent` only covers ~7 days, and `/2/users/:id/tweets` is similarly limited to recent tweets. This means **tweets older than ~2 weeks are unreachable via the free API** — `xurl search` returns `result_count: 0` and `xurl /2/users/:id/tweets?start_time=...&end_time=...` returns empty.

### Fallback: Nitter.net via web_extract

**Nitter** (`nitter.net`) is an alternative X/Twitter frontend that renders threads without requiring login. It can be scraped via the `web_extract` tool to retrieve old thread content.

```python
from hermes_tools import web_extract
result = web_extract([f"https://nitter.net/{username}/status/{tweet_id}"])
content = result["results"][0]["content"]
```

**Critical limitation**: `web_extract` uses an LLM summarizer that truncates content at ~5,000 characters. For very long threads (18+ parts), content beyond 5,000 chars will be silently dropped. The raw page may contain 8,500+ chars but only the first 5,000 reach the agent.

**Strategy for threads > 5,000 chars**:
1. Parse the available 5,000 chars to identify what's missing
2. Try alternative mirrors: `xcancel.com` (also truncated), `nitter.poast.org` (has JS challenge → empty body)
3. Use web_search to find compilations/summaries on Reddit, Medium, or the author's blog
4. As last resort, log which parts are missing and note them for later retrieval

### Mirror Reliability Matrix

| Mirror | Access | Content | JS Required | Reliability |
|--------|--------|---------|-------------|-------------|
| `nitter.net` | `web_extract` works | Full thread (≤5K chars) | No (for web_extract) | **Best option** |
| `fxtwitter.com` | `web_extract` works | Individual tweet + metadata | No | **Good for single tweets** |
| `xcancel.com` | `web_extract` works | Very short (~1K chars) | No | Poor — too truncated |
| `nitter.poast.org` | curl returns HTML | JS challenge page | Yes | Useless |
| `nitter.net` RSS | `web_extract` works | Recent tweets only | No | Only last 40 tweets |
| `x.com` via browser | Login wall | Full thread | Yes | Not available headless |
| `x.com` via API (free) | `xurl` commands | Last ~7 days only | N/A | Useless for old tweets |

### Future: Premium API Access

If old-tweet retrieval becomes a recurring need, upgrading to X API Basic ($100/mo) or Pro ($5,000/mo) tiers unlocks 30-day and full-archive search respectively. The `xurl search` command would then work for any date range.

### Thread Reconstruction from Individual Tweet IDs

When you have specific tweet IDs (e.g., from the user or from a partial nitter.net scrape), you can retrieve each tweet individually via the raw v2 API — **even for old tweets**:

```bash
xurl "/2/tweets/{TWEET_ID}?tweet.fields=note_tweet,public_metrics,created_at,entities&expansions=attachments.media_keys&media.fields=url,preview_image_url"
```

This works because `/2/tweets/:id` is a lookup endpoint, not a search endpoint — it has no time-window limitation. The free tier allows retrieving any public tweet by ID.

**Workflow for reconstructing a thread**:
1. Get tweet IDs from the user or from a partial nitter.net scrape
2. Fetch each tweet individually via `xurl "/2/tweets/{ID}?tweet.fields=..."`
3. Download attached images from `pbs.twimg.com/media/{media_key}?name=orig`
4. Assemble the full thread content in a raw article file
5. Use `fxtwitter.com/{handle}/status/{ID}` via `web_extract` as a secondary verification if needed

---

## Troubleshooting

| Symptom | Cause | Fix |
| --- | --- | --- |
| `xurl search` returns `result_count: 0` for known tweets | Tweets older than ~7 days (free tier limitation) | Use nitter.net fallback via `web_extract` (see above). For bulk old-tweet needs, upgrade API tier. |
| `xurl /2/users/:id/tweets` returns empty with start_time | Tweets older than ~2 weeks | Same as above — free tier time window is limited. |
| Auth errors after successful OAuth flow | Token saved to `default` app (no client-id/secret) instead of your named app | `xurl auth oauth2 --app my-app` then `xurl auth default my-app` |
| `unauthorized_client` during OAuth | App type set to "Native App" in X dashboard | Change to "Web app, automated app or bot" in User Authentication Settings |
| `UsernameNotFound` or 403 on `/2/users/me` right after OAuth | X not returning username reliably from `/2/users/me` | Re-run `xurl auth oauth2 --app my-app YOUR_USERNAME` (xurl v1.1.0+) to pass the handle explicitly |
| 401 on every request | Token expired or wrong default app | Check `xurl auth status` — verify `▸` points to an app with oauth2 tokens |
| `client-forbidden` / `client-not-enrolled` | X platform enrollment issue | Dashboard → Apps → Manage → Move to "Pay-per-use" package → Production environment |
| `CreditsDepleted` | $0 balance on X API | Buy credits (min $5) in Developer Console → Billing |
| `--auth app` returns 401 but default/no-flag commands work | App-only OAuth2 Client Credentials token expired (independent from PKCE user token) | Test with `xurl --auth oauth2 user @handle` instead; patch any scripts hardcoding `--auth app` to use `--auth oauth2` or omit the flag |
| `media processing failed` on image upload | Default category is `amplify_video` | Add `--category tweet_image --media-type image/png` |
| Two Client Secret values in X dashboard | UI bug — first is actually Client ID | Confirm on the Keys and tokens page; ID ends in `MTpjaQ` |
| `tweet.fields=article` returns `article.title` but no `article.plain_text` | Mixed `note_tweet` and `article` in `tweet.fields` — the fields interact poorly | Use `tweet.fields=article` alone (no `note_tweet`). Separate calls if you need both. |
| `article.fields` param returns `not one of [id,expansions,...]` error | `article.fields` is NOT a valid X API v2 query parameter | All article fields come through `tweet.fields=article` — no separate `article.fields` needed. |

---

## Note Tweets (Long-Form Tweets with "Show More") — Retrieval Pattern

Note Tweets are X's long-form tweet feature where the tweet body exceeds the standard display limit and shows a "Show more" expander. They are **not** X Articles — they are regular tweets whose full text is stored in the `note_tweet.text` field of the API response.

**Critical pitfall**: `xurl read <tweet_id>` returns only the **truncated** text (typically the first ~140 characters with an ellipsis). The full content is lost unless you explicitly request the `note_tweet` field.

### Retrieving Full Note Tweet Content

Use the raw v2 API endpoint with `tweet.fields=note_tweet`:

```bash
xurl "/2/tweets/{TWEET_ID}?tweet.fields=note_tweet,public_metrics,created_at"
```

This returns the full body in `data.note_tweet.text`:

```json
{
  "data": {
    "id": "2052100726608781363",
    "text": "Strong Opinions, Loosely Held on... (truncated)",
    "note_tweet": {
      "text": "Strong Opinions, Loosely Held on Agent + Harness Engineering:\n\n1. You can outperform any default harness+model..."
    },
    "public_metrics": { "bookmark_count": 542, "like_count": 377 }
  }
}
```

You can also include additional fields for context:

```bash
xurl "/2/tweets/{TWEET_ID}?tweet.fields=note_tweet,public_metrics,created_at&expansions=referenced_tweets.id"
```

### How to Detect if a Tweet Has a Note

- `xurl read <id>` returns text ending with an ellipsis (`...`) or that feels abruptly cut off
- The tweet has high engagement (500+ bookmarks is a strong signal)
- The author is known for long-form content (opinion pieces, manifestos, analysis threads)

### Recommended Workflow for Wiki Ingestion (Note Tweets)

1. Read the tweet with `xurl read <url>` to confirm it's truncated
2. Fetch the full content via raw v2 API with `tweet.fields=note_tweet`
3. Save full content as a raw article with `type: x_note_tweet` frontmatter
4. Enrich entity/concept pages using the full text

### Comparison: Note Tweets vs X Articles

| Aspect | Note Tweets | X Articles (`x.com/i/article/...`) |
|--------|-------------|-------------------------------------|
| API field | `note_tweet.text` in tweet response | Separate resource, no direct API access |
| Retrievable via xurl? | **Yes** (raw v2 endpoint with `tweet.fields=note_tweet`) | **No** (auth wall; need GetXAPI fallback) |
| Content type | Plain text (Markdown-like, line breaks) | Structured (headings, paragraphs, inline styles) |
| Auth needed | Standard OAuth2 PKCE (already configured) | Auth wall + third-party service |
| Typical use | Opinion pieces, manifestos, analysis threads | Blog-style long-form articles |

## X Articles (x.com/i/article/...) — Full Retrieval via API

X Articles (long-form posts at `x.com/i/article/<id>`) are **not regular tweets** from the API's perspective, but the **full article body can be retrieved** by requesting the `article` field on the parent tweet:

### Primary Method: `tweet.fields=article` (RECOMMENDED)

The parent tweet that shares an X Article contains the full article body in `data.article.plain_text` when `tweet.fields=article` is requested. This works with standard OAuth2 PKCE auth — no third-party service needed.

**CRITICAL**: Use `tweet.fields=article` **alone**. Do NOT mix with `note_tweet` — the two fields interact poorly and `article.plain_text` may be silently dropped from the response. If you need both article body and note_tweet data, make two separate API calls.

```bash
xurl "/2/tweets/{TWEET_ID}?tweet.fields=article,public_metrics,created_at,entities"
```

This returns the full article in `data.article`:
```json
{
  "data": {
    "id": "2045935785661349956",
    "text": "https://t.co/CaQZZwqXeu",
    "article": {
      "title": "Hermes Agent: What People Are Actually Using It For",
      "plain_text": "1. 📞 Pre-call client research\n...",
      "entities": {
        "mentions": [...],
        "urls": [...]
      },
      "cover_media": "3_2045935278511263744",
      "preview_text": "..."
    },
    "public_metrics": {...}
  }
}
```

**Key facts:**
- `article.plain_text` contains the **full article body** (plain text with emoji, line breaks, list markers)
- `article.title` gives the article title
- `article.entities.mentions` lists @mentioned users (username only, no user ID)
- `article.entities.urls` lists external URLs referenced in the article
- `article.preview_text` is a truncated excerpt
- `article.cover_media` references a media key for the cover image

### Fallback: `xurl read <tweet_id>` (metadata only)

`xurl read 2045935785661349956` returns the tweet metadata including `article.title` but NOT `article.plain_text`. The body is only available via the raw v2 endpoint with explicit `tweet.fields=article`.

### Edge Cases

- **`xurl read <article_id>` fails** — returns `"Could not find tweet with id"`. The article ID (from the URL path) is NOT a tweet ID. Always use the **parent tweet's ID** (the tweet that shared the article link).
- **`xurl tweet <id>` may fail** — use `xurl read <id>` or the raw v2 endpoint instead.
- **X Article IDs differ from tweet IDs** — An article ID (e.g., `2045934869629521920`) cannot be read via any tweet endpoint. It's a separate resource.

### Fallback: GetXAPI (alternative, requires third-party key)

If `tweet.fields=article` doesn't return `article.plain_text` (rare), the third-party **GetXAPI** service can retrieve it:

```bash
curl -s -H"Authorization: Bearer $GETXAPI_KEY" \
  "https://api.getxapi.com/twitter/tweet/article?id=<TWEET_ID>"
```

### Recommended Workflow for Wiki Ingestion (X Articles)

1. **Get the parent tweet ID** from the X URL (`x.com/user/status/{TWEET_ID}`)
2. **Fetch with `tweet.fields=article`** — the raw v2 endpoint gives full body + metadata in one call. **Critical: do NOT use `tweet.fields=note_tweet` for X Articles** — that field only works for Note Tweets (long-form tweets), not X Articles. Using `note_tweet` on an X Article returns only `article.title` without `article.plain_text`.
3. **One-shot combined call (recommended)**: Get article body, metrics, AND author info in a single request:
   ```bash
   xurl "/2/tweets/{TWEET_ID}?tweet.fields=article,public_metrics,created_at,entities,author_id&expansions=author_id&user.fields=name,username,description,public_metrics"
   ```
   This returns `data.article.plain_text` (full body), `data.public_metrics` (likes/bookmarks/impressions), and `includes.users[]` (author name, handle, bio, follower count) — everything needed for a raw article + entity enrichment in one API call.
4. **Save as raw article** with `type: x_article` frontmatter, using the `article.plain_text` content. Include metrics from `public_metrics` in the frontmatter.
5. **Enrich concept/entity pages** using the article content
6. **Cross-reference** people mentioned in `article.entities.mentions`

## Conversation Thread Retrieval

To reconstruct a full discussion thread from a root tweet (all replies, debate, community reaction):

```bash
xurl --auth oauth2 "/2/tweets/search/recent?query=conversation_id:<TWEET_ID>&tweet.fields=note_tweet,created_at,author_id&max_results=50"
```

Paginate with `&until_id=<oldest_id_from_previous_page>`. See `references/conversation-thread-search.md` for the full pattern with real-world example and wiki integration.

## Notes

- **Rate limits:** X enforces per-endpoint rate limits. A 429 means wait and retry. Write endpoints (post, reply, like, repost) have tighter limits than reads.
- **Scopes:** OAuth 2.0 tokens use broad scopes. A 403 on a specific action usually means the token is missing a scope — have the user re-run `xurl auth oauth2`.
- **Token refresh:** OAuth 2.0 tokens auto-refresh. Nothing to do.
- **Multiple apps:** Each app has isolated credentials/tokens. Switch with `xurl auth default` or `--app`.
- **Multiple accounts per app:** Select with `-u / --username`, or set a default with `xurl auth default APP USER`.
- **Token storage:** `~/.xurl` is YAML. Never read or send this file to LLM context.
- **Cost:** X API access is typically paid for meaningful usage. Many failures are plan/permission problems, not code problems.
- **Old tweet retrieval (critical pitfall):** `xurl search` and `/2/tweets/search/recent` only return tweets from the last ~7 days on the free tier. `xurl /2/users/ID/tweets` with `start_time`/`end_time` params also only returns recent tweets on free tier. For tweets older than 7 days, you MUST use direct tweet ID lookups: `xurl read <TWEET_ID>` or `xurl "/2/tweets/<TWEET_ID>?tweet.fields=..."`. The tweet text is always available via direct ID lookup regardless of age. If you don't know the tweet IDs, fall back to `web_extract` on `https://fxtwitter.com/user/status/<ID>` which returns the tweet content without a login wall. `nitter.net` frequently returns empty bodies (JS challenge), and `xcancel.com` works but may truncate content. `fxtwitter.com` is the most reliable web-based fallback.

---

## Attribution

- Upstream CLI: https://github.com/xdevplatform/xurl (X developer platform team, Chris Park et al.)
- Upstream agent skill: https://github.com/openclaw/openclaw/blob/main/skills/xurl/SKILL.md
- Hermes adaptation: reformatted for Hermes skill conventions; safety guardrails preserved verbatim.
