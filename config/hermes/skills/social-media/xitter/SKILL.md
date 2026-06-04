---
name: xitter
description: Interact with X/Twitter via the x-cli terminal client using official X API credentials. Use for posting, reading timelines, searching tweets, liking, retweeting, bookmarks, mentions, and user lookups.
version: 1.0.0
author: Siddharth Balyan + Hermes Agent
license: MIT
platforms: [linux, macos]
prerequisites:
  commands: [uv]
  env_vars: [X_API_KEY, X_API_SECRET, X_BEARER_TOKEN, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET]
metadata:
  hermes:
    tags: [twitter, x, social-media, x-cli]
    homepage: https://github.com/Infatoshi/x-cli
---

# Xitter — X/Twitter via x-cli

Use `x-cli` for official X/Twitter API interactions from the terminal.

This skill is for:
- posting tweets, replies, and quote tweets
- searching tweets and reading timelines
- looking up users, followers, and following
- liking and retweeting
- checking mentions and bookmarks

This skill intentionally does not vendor a separate CLI implementation into Hermes. Install and use upstream `x-cli` instead.

## Important Cost / Access Note

X API access is not meaningfully free for most real usage. Expect to need paid or prepaid X developer access. If commands fail with permissions or quota errors, check your X developer plan first.

## Install

Install upstream `x-cli` with `uv`:

```bash
uv tool install git+https://github.com/Infatoshi/x-cli.git
```

Upgrade later with:

```bash
uv tool upgrade x-cli
```

Verify:

```bash
x-cli --help
```

## Credentials

You need these five values from the X Developer Portal:
- `X_API_KEY`
- `X_API_SECRET`
- `X_BEARER_TOKEN`
- `X_ACCESS_TOKEN`
- `X_ACCESS_TOKEN_SECRET`

Get them from:
- https://developer.x.com/en/portal/dashboard

### Why does X need 5 secrets?

Unfortunately, the official X API splits auth across both app-level and user-level credentials:

- `X_API_KEY` + `X_API_SECRET` identify your app
- `X_BEARER_TOKEN` is used for app-level read access
- `X_ACCESS_TOKEN` + `X_ACCESS_TOKEN_SECRET` let the CLI act as your user account for writes and authenticated actions

So yes — it is a lot of secrets for one integration, but this is the stable official API path and is still preferable to cookie/session scraping.

Setup requirements in the portal:
1. Create or open your app
2. In user authentication settings, set permissions to `Read and write`
3. Generate or regenerate the access token + access token secret after enabling write permissions
4. Save all five values carefully — missing any one of them will usually produce confusing auth or permission errors

Note: upstream `x-cli` expects the full credential set to be present, so even if you mostly care about read-only commands, it is simplest to configure all five.

## Cost / Friction Reality Check

If this setup feels heavier than it should be, that is because it is. X’s official developer flow is high-friction and often paid. This skill chooses the official API path because it is more stable and maintainable than browser-cookie/session approaches.

If the user wants the least brittle long-term setup, use this skill. If they want a zero-setup or unofficial path, that is a different trade-off and not what this skill is for.


## Where to Store Credentials

`x-cli` looks for credentials in `~/.config/x-cli/.env`.

If you already keep your X credentials in `~/.hermes/.env`, the cleanest setup is:

```bash
mkdir -p ~/.config/x-cli
ln -sf ~/.hermes/.env ~/.config/x-cli/.env
```

Or create a dedicated file:

```bash
mkdir -p ~/.config/x-cli
cat > ~/.config/x-cli/.env <<'EOF'
X_API_KEY=your_consumer_key
X_API_SECRET=your_secret_key
X_BEARER_TOKEN=your_bearer_token
X_ACCESS_TOKEN=your_access_token
X_ACCESS_TOKEN_SECRET=your_access_token_secret
EOF
chmod 600 ~/.config/x-cli/.env
```

## Quick Verification

```bash
x-cli user get openai
x-cli tweet search "from:NousResearch" --max 3
x-cli me mentions --max 5
```

If reads work but writes fail, regenerate the access token after confirming `Read and write` permissions.

## Common Commands

### Tweets

```bash
x-cli tweet post "hello world"
x-cli tweet get https://x.com/user/status/1234567890
x-cli tweet delete 1234567890
x-cli tweet reply 1234567890 "nice post"
x-cli tweet quote 1234567890 "worth reading"
x-cli tweet search "AI agents" --max 20
x-cli tweet metrics 1234567890
```

### Users

```bash
x-cli user get openai
x-cli user timeline openai --max 10
x-cli user followers openai --max 50
x-cli user following openai --max 50
```

### Self / Authenticated User

```bash
x-cli me mentions --max 20
x-cli me bookmarks --max 20
x-cli me bookmark 1234567890
x-cli me unbookmark 1234567890
```

### Quick Actions

```bash
x-cli like 1234567890
x-cli retweet 1234567890
```

## Output Modes

Use structured output when the agent needs to inspect fields programmatically:

```bash
x-cli -j tweet search "AI agents" --max 5
x-cli -p user get openai
x-cli -md tweet get 1234567890
x-cli -v -j tweet get 1234567890
```

Recommended defaults:
- `-j` for machine-readable output
- `-v` when you need timestamps, metrics, or metadata
- plain/default mode for quick human inspection

## Agent Workflow

1. Confirm `x-cli` is installed
2. Confirm credentials are present
3. Start with a read command (`user get`, `tweet search`, `me mentions`)
4. Use `-j` when extracting fields for later steps
5. Only perform write actions after confirming the target tweet/user and the user's intent

## Section: Bookmark Ingestion Pipeline (x-bookmarks-ingest)

See `references/x-bookmarks-ingest.md` for full pipeline details.

Automated bookmark ingestion pipeline using xurl. Runs as a cron job with pre-run script.

### Architecture
Three complementary components:
| Component | Script | Purpose |
| --- | --- | --- |
| Entity Skeleton Builder | `build_x_wiki.py` | One-time: entity pages from X account profiles |
| Bookmark Ingest | `fetch_x_bookmarks.py` | Periodic: fetch new bookmarks, process articles |
| Account Posts Scan | `fetch_x_accounts.py` | Periodic: fetch latest tweets from tracked accounts |

### Pre-Run Script (fetch_x_bookmarks.py)
Steps: load processed IDs → fetch bookmarks (`xurl bookmarks -n 100`) → dedup → extract URLs → output JSON → unbookmark processed → update DB.

### Dedup Safety Net
Two layers: X-side (unbookmark removes from list) + local DB (`~/.hermes/processed_x_bookmarks.json`).

### Cron Setup
`schedule: 30 23 * * *`, deliver to Discord.

### Agent Prompt — Karpathy Filter
Classify each bookmark into three tiers:
- **Tier 1 (COMPOUND — 3x)**: Context engineering, tool design, orchestrator-subagent, eval discipline, harness mindset, MCP, production deployment
- **Tier 2 (Relevant)**: Local model capability, LLM infrastructure
- **Tier 3 (DEPRIORITIZE)**: AutoGen/AG2, CrewAI, autonomous agent pitches, SWE-bench chasing, DSPy, viral frameworks, per-seat SaaS

### X Native Articles (REST endpoint)
```bash
xurl -X GET "/2/tweets/<tweet_id>?tweet.fields=article,entities"
```
**NEVER use `-v` flag** — it outputs HTTP headers to stdout.
**CRITICAL:** Always process `data.article.plain_text` — it's the full article body.

### Common Issues
- Auth failures on unbookmark, token expiration, empty new_bookmarks
- "No apps registered" → user needs to re-auth with `xurl auth apps add`

### Batch-Scale Execution
For 10+ bookmarks, use `execute_code` for bulk operations:
1. Save all articles
2. Create/update all wiki pages
3. Update index.md and log.md
4. Single git commit

## Section: Manual X Article → Wiki Ingestion (x-articles-wiki-ingestion)

See `references/x-articles-wiki-ingestion.md` for full procedure.

When X native article bodies need manual extraction from tweet IDs.

### Workflow
1. Fetch article body: `xurl -X GET "/2/tweets/<TWEET_ID>?tweet.fields=article,entities"`
2. Parse response: extract `plain_text` (full body), title, preview_text
3. Save raw article to `~/wiki/raw/articles/<TWEET_ID>_<slug>.md`
4. Create/update wiki entity/concept pages
5. Update index.md and log.md

### JSON Parse Pitfall
xurl appends `\nError: request failed` even on success. Strip before parsing:
```python
output = result.get("output", "")
error_idx = output.rfind("\nError")
json_str = output[:error_idx] if error_idx > 0 else output
data = json.loads(json_str)
```

### Common Patterns by Article Type
| Type | Action |
|------|--------|
| Person's opinion/thesis | Create/update entity page |
| Company announcement | Create company entity page |
| New concept/framework | Create new concept page |
| Tool comparison | Update comparison page |

## Section: X Account & Wiki Management (x-account-wiki-management)

See `references/x-account-wiki-management.md` for full procedure.

### Workflow
1. Add to `config/feeds/x-accounts.yaml`
2. Generate skeleton: `python ~/scripts/build_x_wiki.py --handle @Username`
3. Enrich entity page (remove `status: skeleton`, add bio, contributions, cross-references)
4. Update index.md and commit

### Key Concepts to Cross-Link
- Multi-agent patterns → `[[back-of-house-multi-agent-patterns]]`
- Single-agent limitations → `[[single-agent-ceiling]]`
- Orchestration → `[[session-hierarchy-management]]`

### YAML Multi-Line Notes Fragility
Edit x-accounts.yaml via execute_code with yaml.safe_load, not patch:
```python
with open('config/feeds/x-accounts.yaml', 'r') as f:
    data = yaml.safe_load(f)
# ... edit ...
with open('config/feeds/x-accounts.yaml', 'w') as f:
    yaml.dump(data, f, allow_unicode=True, sort_keys=False, width=1000)
```

## Pitfalls (common to all sections)

- **Paid API access**: many failures are plan/permission problems, not code problems.
- **403 oauth1-permissions**: regenerate the access token after enabling `Read and write`.
- **Reply restrictions**: X restricts many programmatic replies. `tweet quote` is often more reliable than `tweet reply`.
- **Rate limits**: expect per-endpoint limits and cooldown windows.
- **Credential drift**: if you rotate tokens in `~/.hermes/.env`, make sure `~/.config/x-cli/.env` still points at the current file.
- **X article body plain_text**: NEVER skip this field — it's the full article body
- **-v flag**: NEVER use with xurl for JSON endpoints — breaks JSON parsing
- **Auth on empty bookmarks**: Check `xurl auth status` first — "No apps registered" is #1 cause of empty returns

## Notes

- Prefer official API workflows over cookie/session scraping.
- Use tweet URLs or IDs interchangeably — `x-cli` accepts both.
- If bookmark behavior changes upstream, check the upstream README first:
  https://github.com/Infatoshi/x-cli
