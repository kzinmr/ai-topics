---
name: blogwatcher
description: Monitor blogs and RSS/Atom feeds for updates using the blogwatcher-cli tool. Add blogs, scan for new articles, track read status, and filter by category.
version: 2.2.0
author: JulienTant (fork of Hyaxia/blogwatcher)
license: MIT
metadata:
  hermes:
    tags: [RSS, Blogs, Feed-Reader, Monitoring]
    homepage: https://github.com/JulienTant/blogwatcher-cli
prerequisites:
  commands: [blogwatcher-cli]
---

# Blogwatcher

Track blog and RSS/Atom feed updates with the `blogwatcher-cli` tool. Supports automatic feed discovery, HTML scraping fallback, OPML import, and read/unread article management.

## Installation

Pick one method:

- **Go:** `go install github.com/JulienTant/blogwatcher-cli/cmd/blogwatcher-cli@latest`
- **Docker:** `docker run --rm -v blogwatcher-cli:/data ghcr.io/julientant/blogwatcher-cli`
- **Binary (Linux amd64):** `curl -sL https://github.com/JulienTant/blogwatcher-cli/releases/latest/download/blogwatcher-cli_linux_amd64.tar.gz | tar xz -C ~/bin blogwatcher-cli` (use `~/bin/` if `/usr/local/bin/` has permission issues)
- **Binary (Linux arm64):** `curl -sL https://github.com/JulienTant/blogwatcher-cli/releases/latest/download/blogwatcher-cli_linux_arm64.tar.gz | tar xz -C /usr/local/bin blogwatcher-cli`
- **Binary (macOS Apple Silicon):** `curl -sL https://github.com/JulienTant/blogwatcher-cli/releases/latest/download/blogwatcher-cli_darwin_arm64.tar.gz | tar xz -C /usr/local/bin blogwatcher-cli`
- **Binary (macOS Intel):** `curl -sL https://github.com/JulienTant/blogwatcher-cli/releases/latest/download/blogwatcher-cli_darwin_amd64.tar.gz | tar xz -C /usr/local/bin blogwatcher-cli`

All releases: https://github.com/JulienTant/blogwatcher-cli/releases

### Docker with persistent storage

By default the database lives at `~/.blogwatcher-cli/blogwatcher-cli.db`. In Docker this is lost on container restart. Use `BLOGWATCHER_DB` or a volume mount to persist it:

```bash
# Named volume (simplest)
docker run --rm -v blogwatcher-cli:/data -e BLOGWATCHER_DB=/data/blogwatcher-cli.db ghcr.io/julientant/blogwatcher-cli scan

# Host bind mount
docker run --rm -v /path/on/host:/data -e BLOGWATCHER_DB=/data/blogwatcher-cli.db ghcr.io/julientant/blogwatcher-cli scan
```

### Migrating from the original blogwatcher

If upgrading from `Hyaxia/blogwatcher`, move your database:

```bash
mv ~/.blogwatcher/blogwatcher.db ~/.blogwatcher-cli/blogwatcher-cli.db
```

The binary name changed from `blogwatcher` to `blogwatcher-cli`.

## Common Commands

### Managing blogs

- Add a blog: `blogwatcher-cli add "My Blog" https://example.com`
- Add with explicit feed: `blogwatcher-cli add "My Blog" https://example.com --feed-url https://example.com/feed.xml`
- Add with HTML scraping: `blogwatcher-cli add "My Blog" https://example.com --scrape-selector "article h2 a"`
- List tracked blogs: `blogwatcher-cli blogs`
- Remove a blog: `blogwatcher-cli remove "My Blog" --yes`
- Import from OPML: `blogwatcher-cli import subscriptions.opml`

### Scanning and reading

- Scan all blogs: `blogwatcher-cli scan`
- Scan one blog: `blogwatcher-cli scan "My Blog"`
- List unread articles: `blogwatcher-cli articles`
- List all articles: `blogwatcher-cli articles --all`
- Filter by blog: `blogwatcher-cli articles --blog "My Blog"`
- Filter by category: `blogwatcher-cli articles --category "Engineering"`
- Mark article read: `blogwatcher-cli read 1`
- Mark article unread: `blogwatcher-cli unread 1`
- Mark all read: `blogwatcher-cli read-all`
- Mark all read for a blog: `blogwatcher-cli read-all --blog "My Blog" --yes`

## Environment Variables

All flags can be set via environment variables with the `BLOGWATCHER_` prefix:

| Variable | Description |
|---|---|
| `BLOGWATCHER_DB` | Path to SQLite database file |
| `BLOGWATCHER_WORKERS` | Number of concurrent scan workers (default: 8) |
| `BLOGWATCHER_SILENT` | Only output "scan done" when scanning |
| `BLOGWATCHER_YES` | Skip confirmation prompts |
| `BLOGWATCHER_CATEGORY` | Default filter for articles by category |

## Example Output

```
$ blogwatcher-cli blogs
Tracked blogs (1):

  xkcd
    URL: https://xkcd.com
    Feed: https://xkcd.com/atom.xml
    Last scanned: 2026-04-03 10:30
```

```
$ blogwatcher-cli scan
Scanning 1 blog(s)...

  xkcd
    Source: RSS | Found: 4 | New: 4

Found 4 new article(s) total!
```

```
$ blogwatcher-cli articles
Unread articles (2):

  [1] [new] Barrel - Part 13
       Blog: xkcd
       URL: https://xkcd.com/3095/
       Published: 2026-04-02
       Categories: Comics, Science

  [2] [new] Volcano Fact
       Blog: xkcd
       URL: https://xkcd.com/3094/
       Published: 2026-04-01
       Categories: Comics
```

## Reddit RSS Feeds

Reddit subreddits expose RSS feeds at: `https://www.reddit.com/r/SUBREDDIT/.rss`
These work like any other blog feed — add with `blogwatcher-cli add "r/Name" "https://www.reddit.com/r/Name/.rss"`

## YouTube Channel Monitoring

YouTube channels expose standard Atom/RSS feeds at `https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID`. These work with blogwatcher-cli like any other feed — each new video becomes a discoverable article with its description as content. The daily `blog-ingest` cron job picks up new videos automatically.

For deep transcript ingestion of individual videos, use the `youtube-content` skill workflow (`yt-dlp` → transcript → structured raw article → entity/concept enrichment).

### Adding a YouTube Channel to Monitoring

When the user asks to add a YouTube channel to monitoring:

1. **Get the channel ID** via yt-dlp:
   ```bash
   /opt/data/bin/yt-dlp --print channel_id --playlist-end 1 "https://www.youtube.com/@HANDLE"
   ```

2. **Test the RSS feed**:
   ```bash
   curl -s "https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID" | head -20
   ```

3. **Add to OPML** in the "YouTube Channels" section (create the section if it doesn't exist):
   ```xml
   <outline text="YouTube Channels" title="YouTube Channels">
     <outline type="rss" text="Channel Name" title="Channel Name" xmlUrl="https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID" htmlUrl="https://www.youtube.com/@HANDLE" />
   </outline>
   ```
   Insert before `</body>` in `config/feeds/blogs.opml`. Validate: `python3 -c "import xml.etree.ElementTree as ET; ET.parse('config/feeds/blogs.opml'); print('OK')"`

4. **Add to blogwatcher DB** with explicit `--feed-url` (auto-discovery won't work on YouTube's JS-heavy pages):
   ```bash
   blogwatcher-cli add "Channel Name" "https://www.youtube.com/@HANDLE" --feed-url "https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID"
   ```

5. **Verify scan works**:
   ```bash
   blogwatcher-cli scan "Channel Name"
   # Expected: Source: RSS | Found: N | New: N
   ```

6. **Mark initial backlog as read** (prevents re-processing hundreds of historical videos):
   ```bash
   blogwatcher-cli read-all --blog "Channel Name" --yes
   ```

7. **Create wiki entity page** for the channel under `wiki/entities/<channel-name>.md`:
   - Frontmatter: `type: entity`, `tags: [youtube, …]`
   - Include: subscriber count, video count, content themes, notable talks table, RSS feed URL
   - Link to related entities (speakers) and concepts
   - Add to `wiki/index.md` (alphabetical order) and `wiki/log.md`

8. **Commit config + wiki**:
   ```bash
   cd ~/ai-topics && git add config/feeds/blogs.opml wiki/entities/ wiki/index.md wiki/log.md
   git commit -m "config: add Channel Name YouTube channel to RSS monitoring + entity page"
   git push
   ```

### Pitfalls

- **YouTube RSS returns only the 15 most recent videos**. Historical content beyond 15 videos is not captured on initial scan — this is acceptable since the goal is ongoing monitoring.
- **Channel ID is NOT the @handle**. Always use `yt-dlp --print channel_id` to resolve. Example: `@aidotengineer` → `UCLKPca3kwwd-B59HNr-_lvA`.
- **RSS entries are video descriptions only** — not full transcripts. For transcript-level analysis, use the `youtube-content` skill on individual videos.
- **High-volume channels** (3+ videos/day) will produce many raw articles in the daily blog-ingest pipeline. The `blog-triage` step filters by importance before wiki ingestion.
- **OPML section naming**: Use `<outline text="YouTube Channels">` as a top-level group, not mixed into "Individual Blogs" or "Company Tech Blogs". This keeps the OPML organized by source type.

## Environment-Specific Notes (exe.dev VM)

- Binary installed at: `/opt/data/bin/blogwatcher-cli` (Hyaxia/blogwatcher v0.0.2, NOT JulienTant fork)
- OPML source: `~/ai-topics/config/feeds/blogs.opml` (~87 blogs as of 2026-05-08)
  - **OPML is structured in three groups**: `<outline text="Individual Blogs">` (84 personal blogs), `<outline text="Company Tech Blogs">` (RSS + sitemap-based), and `<outline text="YouTube Channels">` (YouTube RSS feeds)
  - Corporate blogs use `type="rss"` for RSS-based or `type="sitemap"` for sitemap-based (e.g., Anthropic Engineering)
- Database: `/opt/data/.blogwatcher/blogwatcher.db` (NOT `~/.blogwatcher-cli/` — uses the original Hyaxia/blogwatcher path)
- **⚠️ Cron HOME mismatch**: In cron, `HOME=/opt/data/.hermes/home` but DB is at `/opt/data/.blogwatcher/`. The `daily_inbox_collect.py` script must use `PROFILE_ROOT` instead of `Path.home()` for DB path resolution, and `run_blogwatcher_scan()` must set `HOME=str(PROFILE_ROOT)` in the subprocess env. See `blogwatcher-db` skill's `references/cron-home-fix.md` for the exact patch.
- To query the DB directly: `python3 -c "import sqlite3; conn = sqlite3.connect('/opt/data/.blogwatcher/blogwatcher.db'); ..."`
- Cron jobs:
  - `blog-ingest` (Job ID: `1bf4c6492c1e`) runs at `0 7 * * *` UTC = JST 16:00 — RSS blog scan via blogwatcher
  - `sitemap-monitor` (Job ID: `c7890b6e0e19`) runs at `0 6 * * *` UTC = JST 15:00 — sitemap-based monitoring for corporate blogs without RSS
- First scan detected ~2,045 articles across 87 feeds

## YouTube Channel Monitoring

YouTube channels expose RSS feeds at a predictable URL pattern and can be monitored via blogwatcher just like blogs. Use this workflow when the user asks to add a YouTube channel to monitoring.

### YouTube RSS URL Pattern

```
https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID
```

To find the channel ID:
```bash
/opt/data/bin/yt-dlp --print channel_id --playlist-end 1 "https://www.youtube.com/@channelhandle" 2>/dev/null
```

### Add to OPML

Add a new "YouTube Channels" section to `config/feeds/blogs.opml` before `</body>`:
```xml
    <outline text="YouTube Channels" title="YouTube Channels">
      <outline type="rss" text="Channel Name" title="Channel Name" xmlUrl="https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID" htmlUrl="https://www.youtube.com/@channelhandle" />
    </outline>
```

### Add to blogwatcher DB

```bash
blogwatcher-cli add "Channel Name" "https://www.youtube.com/@channelhandle" \
  --feed-url "https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID"
```

### Verify and mark backlog

```bash
blogwatcher-cli scan "Channel Name"       # Verify scan works
blogwatcher-cli read-all --blog "Channel Name" --yes  # Mark initial backlog as read
```

### Create wiki entity page

Create an entity page under `wiki/entities/` with channel overview, key facts, content themes, notable talks, and monitoring info. The RSS feed URL and blogwatcher pipeline details should be documented in the Monitoring section.

### Pitfalls

- **YouTube RSS returns video descriptions, NOT transcripts**. The blog-ingest pipeline will capture video titles and descriptions for daily awareness. For full transcript ingestion of high-signal talks, use the [[youtube-content]] workflow on individual videos.
- **High-volume channels**: AI Engineer posts 3-5 videos/day during conference seasons. The initial scan will find 15+ entries — always mark as read to avoid re-processing.
- **Channel ID is stable**: Unlike channel handles which can change, channel IDs are permanent. Prefer the ID-based RSS URL over handle-based alternatives.

## Check-and-Add Single Feed (One-Off Request)

When the user asks "Xのブログが監視対象に含まれているか確認し、なければ追加して" (check if X blog is monitored, add if not):

### Workflow

1. **Check OPML**: `grep -i "keyword" /opt/data/ai-topics/config/feeds/blogs.opml`
   - Case-insensitive search. Try both blog name and domain.
   - If found → report to user: "すでに含まれています ✅" and done.

2. **Discover RSS feed**: If not in OPML, find the feed URL.
   - Priority order: check HTML `<link>` tags → try root-level paths → try blog-subdirectory paths
   - **Root-level paths FIRST** (corporate blogs often put RSS at domain root):
     ```bash
     curl -sI "https://example.com/rss.xml" | head -1      # ← TRY FIRST
     curl -sI "https://example.com/feed.xml" | head -1
     curl -sI "https://example.com/atom.xml" | head -1
     curl -sI "https://example.com/index.xml" | head -1
     ```
   - **Then blog subdirectory**:
     ```bash
     curl -sI "https://example.com/blog/rss.xml" | head -1
     curl -sI "https://example.com/blog/feed.xml" | head -1
     curl -sI "https://example.com/feed" | head -1
     ```
   - Fall back to `references/feed-discovery-patterns.md` for platform-specific patterns, or `references/corporate-blog-tracking.md` for corporate blog-specific approaches (sitemap, scrape-selector).
   - **Check sitemap** as an alternative discovery method for blogs without RSS:
     ```bash
     curl -s "https://example.com/sitemap.xml" | grep -i "blog\|engineering"
     ```

3. **Verify feed content**: `curl -s "FEED_URL" | head -30`
   - Check for valid RSS/Atom XML (`<rss`, `<feed`, `<channel>`, `<item>` elements)
   - If 404 or non-XML response → try different URL, or fall back to `--scrape-selector`

4. **Insert into OPML**: Add an `<outline>` entry in the correct group.
   - **Individual blog** → `<outline text="Individual Blogs">` group (lines ~7-109)
   - **Company/org blog** → `<outline text="Company Tech Blogs">` group (lines ~110-135)
   - For company blogs with RSS: add at end of group with `type="rss"`
   - For company blogs without RSS (sitemap-based): add with `type="sitemap"` and `xmlUrl` pointing to the sitemap URL
   - Format RSS: `<outline type="rss" text="Blog Name" title="Blog Name" xmlUrl="FEED_URL" htmlUrl="SITE_URL" />`
   - Format sitemap: `<outline type="sitemap" text="Blog Name" title="Blog Name" xmlUrl="SITEMAP_URL" htmlUrl="SITE_URL" />`
   - Verify with: `grep -n "Blog Name" blogs.opml`

5. **Add to blogwatcher DB AND scan + cleanup**:
   ```bash
   # Add (RSS): 
   blogwatcher-cli add "Blog Name" "https://example.com/blog" --feed-url "FEED_URL"
   # OR Add (scrape):
   blogwatcher-cli add "Blog Name" "https://example.com/blog" --scrape-selector "article a"
   
   # Verify scan works:
   blogwatcher-cli scan "Blog Name"
   
   # Mark initial backlog as read (FOUND: N / NEW: N → all historical):
   blogwatcher-cli read-all --blog "Blog Name" --yes
   ```

6. **Commit config change**:
   ```bash
   cd ~/ai-topics && git add config/feeds/blogs.opml && git commit -m "config: add Blog Name RSS feed" && git push
   ```

7. **(If author has existing wiki entity page) — Enrich the entity page**:
   - Check: `search_files path=~/wiki/entities pattern="author-name"` — if found, enrich the existing page
   - **Blog URL in infobox**: Update stale blog URLs (e.g., deleted WordPress → active Medium)
   - **Add Monitoring section** at an appropriate point in the page structure:
     ```markdown
     ## Monitoring

     | Source | Method | Status |
     |--------|--------|--------|
     | RSS Feed | [feed-url](FEED_URL) | ✅ Active (added YYYY-MM-DD; RSS → blogwatcher → daily `blog-ingest` pipeline) |
     | X/Twitter | [@handle](https://x.com/handle) | Tracked in `x-accounts.yaml` (if applicable) |
     ```
   - **Recent notable work**: Scan the RSS feed output (`curl -s "FEED_URL" | head -30`) for significant recent posts. If something substantial is found (major technical post, research result, framework release), add a relevant section to the entity page with key details. Don't add trivial posts.
   - **Update frontmatter**: Bump `updated:` date, add new sources, add any new tags
   - **Update Related/Sources sections**: Add cross-links to new concepts, append new source URLs
   - **New tags → SCHEMA.md**: If a genuinely new tag is added to frontmatter, add it to SCHEMA.md taxonomy FIRST
   - **Update index.md**: Enrich the entity's index entry with new monitoring/blog info and notable work
   - **Update log.md**: Prepend log entry (use `execute_code` + Python `with open()` prepend to avoid `---` anchor trap — see wiki-graph-health skill §H5)
   - **Commit everything together**: `cd ~/ai-topics && git add config/feeds/ wiki/ && git commit -m "config+wiki: add Blog Name RSS + entity enrichment" && git push`

### Pitfalls

- **OPML is NOT the blogwatcher DB**: Adding to OPML does NOT add to the blogwatcher SQLite database. The next full scan will auto-discover it.
- **Blogwatcher-cli does NOT follow HTTP redirects**: If the feed URL redirects, it will fail at scan time. Verify the final destination URL.
- **Webflow sites**: Often serve RSS at `/blog/rss.xml` rather than root-level paths. The HTML `<head>` may not include a `<link type="application/rss+xml">` tag even though the feed exists.
- **Corporate blogs: RSS at root, not under /blog/**: Sierra (`sierra.ai/rss.xml`) and OpenAI (`developers.openai.com/rss.xml`) both serve RSS from the domain root. Always check root-level paths (`/rss.xml`, `/feed.xml`) BEFORE checking blog subdirectories.
- **Engineering blogs on separate subdomains**: Some companies host their engineering blog on a different subdomain from their marketing blog (e.g., Ramp's engineering blog is at `builders.ramp.com`, not `ramp.com/blog`). Always check the company's job postings, GitHub org, or search `"company engineering blog"` to discover these before concluding no blog exists.
- **Scrape-selector blogs: skip OPML**: If a blog has no RSS feed and uses `--scrape-selector`, do NOT add it to the OPML. OPML requires `xmlUrl`. Track it only in the blogwatcher DB. Consider migrating to sitemap-based monitoring (see Sitemap-Based Monitoring section) for greater reliability.
- **Always mark initial backlog as read**: After adding a new blog, run `read-all --blog "Name" --yes` to prevent the daily scan from re-processing hundreds of historical articles.
- **Migrate scrape-selector → sitemap when possible**: HTML scraping is fragile. If the site has a sitemap with blog URLs and `lastmod` dates, migrate to `sitemap_monitor.py`. Remove from blogwatcher DB, add to sitemap_monitor SOURCES list, and add to OPML Company group with `type="sitemap"`.
- **Commit only `config/feeds/`**: Adding a blog is a config change, not a wiki change. Do not `git add wiki/` unless you also made wiki changes this session.

## Corporate Tech Blog Feed Discovery

Corporate tech blogs (Anthropic Engineering, OpenAI Developers, Sierra, etc.) often have non-standard RSS setups. Follow this extended discovery workflow:

For **single-blog discovery**, use the workflow below. For **batch discovery** across dozens of URLs (e.g., when ingesting a curated company list), use the parallel curl approach in `references/rss-batch-discovery.md`.

### Discovery Priority (updated)

1. **Check HTML `<link>` tags** for `application/rss+xml` or `application/atom+xml`
2. **Try root-level paths FIRST** — corporate blogs often place feeds at the domain root, NOT under `/blog/`:
   ```bash
   curl -sI "https://example.com/rss.xml" | head -1      # ← TRY THIS FIRST
   curl -sI "https://example.com/feed.xml" | head -1
   curl -sI "https://example.com/atom.xml" | head -1
   curl -sI "https://example.com/index.xml" | head -1
   ```
3. **Then try the blog subdirectory**:
   ```bash
   curl -sI "https://example.com/blog/rss.xml" | head -1
   curl -sI "https://example.com/blog/feed.xml" | head -1
   ```
4. **Check the sitemap** for blog post URLs — many corporate sites expose all blog URLs with `lastmod` dates:
   ```bash
   curl -s "https://example.com/sitemap.xml" | grep -i "blog\|engineering"
   ```
5. **Fall back to HTML scraping** with `--scrape-selector` if no RSS exists.

### Real-World Examples

| Blog | RSS URL | Discovery Method |
|------|---------|-----------------|
| OpenAI Developers Blog | `https://developers.openai.com/rss.xml` | `<link rel="alternate">` in HTML head (root-level, not `/blog/rss.xml`) |
| Sierra Blog | `https://sierra.ai/rss.xml` | Root-level trial-and-error (not advertised in HTML) |
| Anthropic Engineering | NONE | HTML scrape-selector (`article a`) — sitemap at `anthropic.com/sitemap.xml` has all `/engineering/` URLs |

### HTML Scrape-Selector Fallback

When no RSS feed exists, use blogwatcher-cli's `--scrape-selector`:

```bash
blogwatcher-cli add "Blog Name" "https://example.com/blog" --scrape-selector "article a"
```

**Selector guidance:**
- Start broad (`article a`) and verify with a scan
- If the selector catches too many non-article links, refine it
- Test immediately after adding: `blogwatcher-cli scan "Blog Name"`
- Common selectors that work: `article a`, `a[href^="/blog/"]`, `h2 a`, `.post-title a`

**Successful examples:**
- `article a` → Anthropic Engineering (found 27 articles)
- `article h2 a` → typical blog listing pattern

### Post-Addition: Mark Initial Backlog as Read

After adding a new blog, the first scan finds ALL historical articles. Mark them as read so future scans only highlight new content:

```bash
blogwatcher-cli read-all --blog "Blog Name" --yes
```

### Sitemap-Based Monitoring (Advanced)

For high-value corporate blogs without RSS (e.g., Anthropic Engineering), sitemap monitoring is more reliable than HTML scraping. The `sitemap_monitor.py` script handles this automatically.

**Script**: `~/ai-topics/scripts/sitemap_monitor.py` (source of truth) → `~/.hermes/scripts/sitemap_monitor.py` (cron execution copy)

**How it works**:
1. Fetches the site's `sitemap.xml`
2. Filters URLs matching a pattern (e.g., `/engineering/`)
3. Compares against previously seen URLs stored in `~/.hermes/processed_{name}.json`
4. Scrapes new articles with BeautifulSoup + httpx
5. Saves raw articles to `wiki/raw/articles/`
6. Outputs checkpoint JSON to `~/.hermes/cron/data/sitemap_monitor/latest.json`

**Cron integration**: `sitemap-monitor` job (ID: `c7890b6e0e19`) runs daily at `0 6 * * *` UTC (JST 15:00) with `no_agent=True`. Raw articles are later picked up by the dreaming pipeline (18:00 UTC).

**Single script, multiple companies**: The `SOURCES` list supports unlimited companies in one script. Each source gets its own `state_file` for independent deduplication. No per-company script needed.

**SOURCE config template** (each company gets one entry):

```python
{
    "name": "Company Blog",                   # Display name for logging
    "url": "https://company.com/blog",         # Blog homepage
    "sitemap_url": "https://company.com/sitemap.xml",  # Sitemap URL
    "url_pattern": "/blog/",                   # URL filter (e.g. "/blog/", "/engineering/", "/news/")
    "file_prefix": "company-name",             # Used in raw article filenames: {date}_{prefix}_{slug}.md
    "title_suffixes": [" | Company", " - Company"],  # Patterns to strip from <title> tags
    "state_file": os.path.expanduser("~/.hermes/processed_company_blog.json"),
}
```

**Field notes**:
- `file_prefix` — **required.** Prevents filename collisions between sources.
- `title_suffixes` — **optional but recommended.** Many corporate blogs append `" | Company Name"` to `<title>`. Stripping these keeps downloaded article titles clean.
- `url_pattern` — **must match blog post URLs exactly.** If the blog is at `/blog/post-slug`, use `/blog/`. If at `/news/post-slug`, use `/news/`. Too broad a pattern (e.g., `/`) matches every page on the site.
- `state_file` — **one per source, unique paths.** Two sources sharing one file corrupt dedup.

**Adding a new sitemap-based source**:
1. Edit `sitemap_monitor.py` — add an entry to the `SOURCES` list following the template above. Verify `url_pattern` by checking the sitemap.
2. Add to OPML Company group with `type="sitemap"`
3. Do NOT add to blogwatcher DB (sitemap monitor is independent)
4. Copy updated script to `~/.hermes/scripts/`
5. Commit: `cd ~/ai-topics && git add config/feeds/ scripts/ && git commit && git push`
6. First run scrapes ALL historical articles (state file seeds the seen-URL set). Subsequent cron runs only find new posts.

### Company Blog Monitoring Tiers

When ingesting a large list of companies (e.g., from Paraform Talent Density Index, YC batches, startup rankings), prioritise by tier:

**Tier 1 — AI core companies (monitor with RSS or sitemap immediately)**:
Frontier labs, AI infrastructure, coding agents, embedding/voice models. These blogs produce content directly relevant to the wiki domain.

**Tier 2 — Important but lower AI density**:
Autonomous vehicles, defense AI, legal AI, recruiting AI, dev-tool-adjacent. Add to sitemap monitor in the next batch. Worth monitoring but yield is lower.

**Tier 3 — Non-AI companies on the list**:
E-commerce, wholesale marketplaces, billing platforms, generic analytics. Skip or add scrape-selector if they occasionally publish AI content.

**Tier X — No blog found**:
Some companies simply don't have a tech blog. Mark as `no_blog` in the entity page and move on.

**Batch ingestion workflow**:
1. Run `references/rss-batch-discovery.md` on all blog URLs → get RSS found/not-found split
2. Add RSS-found blogs to blogwatcher DB + OPML in one batch (chain `blogwatcher-cli add` commands)
3. For RSS-not-found, check sitemaps → add Tier 1/2 to `sitemap_monitor.py` SOURCES
4. Add sitemap sources to OPML Company group with `type="sitemap"`
5. Run a manual first scan to seed state files
6. Commit config + scripts together

### Migrating from scrape-selector to sitemap
```bash
# 1. Remove from blogwatcher DB
blogwatcher-cli remove "Anthropic Engineering" --yes

# 2. Add to sitemap_monitor.py SOURCES list
# 3. Add to OPML Company group with type="sitemap"
# 4. Run sitemap_monitor.py to seed the state file
/opt/data/.hermes/venv/bin/python sitemap_monitor.py
```

This avoids the fragility of CSS selectors breaking on site redesigns.

## Bulk Adding Blogs from Curated Lists

When a reference article or newsletter recommends blogs to add, follow this workflow to keep both the blogwatcher DB and the OPML in sync.

### Workflow Steps

1. **Extract blog recommendations** from the source article using `web_extract` or `curl`.
2. **Compare against current blogwatcher DB**: `/opt/data/bin/blogwatcher-cli blogs` — produce a list of missing blogs.
3. **For each missing blog, add to blogwatcher DB**:
   ```bash
   /opt/data/bin/blogwatcher-cli add "Blog Name" "https://example.com"
   ```
   blogwatcher-cli auto-discovers RSS at scan time, but the DB stores `feed_url=None` until then.
4. **Discover RSS/Atom feed URLs** for each new blog. See `references/feed-discovery-patterns.md` for platform-specific patterns.
   ```bash
   # Quick check: look for <link> tags
   curl -sL https://example.com | grep -iE '(rss|atom|feed)' | grep -oP 'href="[^"]*\.(xml|rss|atom)"'
   ```
5. **Update the OPML** at `~/ai-topics/config/feeds/blogs.opml` with proper `<outline>` entries including the discovered `xmlUrl`. Use `patch` to insert entries before the closing `</outline>` tag:
   ```xml
   <outline type="rss" text="Blog Name" title="Blog Name" xmlUrl="https://example.com/feed.xml" htmlUrl="https://example.com/" />
   ```
6. **Verify OPML validity**:
   ```bash
   python3 -c "import xml.etree.ElementTree as ET; ET.parse('~/ai-topics/config/feeds/blogs.opml')"
   ```
7. **Commit and push**:
   ```bash
   cd ~/ai-topics && git add config/feeds/blogs.opml && git commit -m "wiki: add N blogs from <source>" && git push
   ```

### Pitfalls

- **blogwatcher-cli add does NOT discover feeds immediately**. It sets `feed_url=None` until the next `scan`. The OPML should still have the explicit `xmlUrl` to serve as the source of truth.
- **Blogger/Blogspot feeds** sometimes use an ID-based path (`feeds/posts/default`) rather than the blog name. The `?alt=rss` query param also works.
- **Substack feeds** accept both `https://name.substack.com/feed` and `https://name.substack.com/feed.xml`.
- **Inactive blogs** (no posts in 3+ years) should be skipped — mark them as blocked and note the reason.
- **Not all blogs have RSS**. For these, either skip or use `--scrape-selector` if the site has a predictable HTML structure.
- **Keep the OPML and blogwatcher DB in sync manually** — they are independent stores. Adding to one does not update the other.

### Reference

See `references/feed-discovery-patterns.md` for detailed platform feed URL patterns and the full ClickHouse curated list feed table.

## Troubleshooting Feed Failures

Common issues when scanning feeds:
- **301/302/308 redirects**: blogwatcher-cli does NOT follow redirects. Fix by removing the old entry and re-adding with the correct URL (often `www.` prefix or different path).
- **406 Forbidden / 404 Not Found**: The feed URL in OPML may be wrong. Try discovering the actual feed URL via `curl -sL <blog_url>` and looking for `<link type="application/rss+xml">` or `<link type="application/atom+xml">` tags.
- **Connection timeout**: The site may be down or blocking the request. Consider removing from the tracking list.

### Quarto on GitHub Pages: False Positive RSS Feeds

Quarto blogs with `feed: true` in `_quarto.yml` generate a `<link rel="alternate" type="application/rss+xml" href="index.xml">` tag in the HTML `<head>`. However, the actual `index.xml` file may **not exist** on the deployed `gh-pages` branch — the Quarto build sometimes omits it even though it is configured.

**Key insight**: This is a false positive, not a regular broken feed. The HTML actively advertises an RSS feed that was never produced by the build.

**Detection workflow:**
1. Check the feed URL: `curl -sI https://blog.example.com/index.xml | head -5` — if 404, the feed does not exist despite the HTML `<link>` tag.
2. Verify the deployed branch: `curl -sL "https://api.github.com/repos/owner/repo/git/trees/gh-pages?recursive=1" | python3 -c "import sys,json; [print(t['path']) for t in json.load(sys.stdin).get('tree',[]) if 'xml' in t['path'].lower()]"` — if `index.xml` is absent from the tree, the build never produced it.
3. Confirm by checking the site config: `_quarto.yml` listing section with `feed: true` + URL base path.

**Action**: If confirmed broken, consider:
- Re-adding with `--scrape-selector` fallback if the blog has predictable HTML structure
- Filing an issue with the blog author about the missing feed
- Removing from OPML if scraping is not viable

## Important: OPML vs DB are independent

**blogwatcher-cli maintains its own SQLite database** at `~/.blogwatcher-cli/blogwatcher-cli.db`. This is separate from the OPML file. Two critical implications:

1. **Removing a URL from the OPML does NOT remove it from the blogwatcher-cli DB.** The DB still tracks and scans it independently.
2. **Importing an OPML adds feeds but does NOT remove feeds no longer in the OPML.** Each `blogwatcher-cli import` is additive.

If a feed fails in the daily RSS scan, check the blogwatcher-cli DB, not just the OPML:
```bash
# Check if a blog is in the DB
blogwatcher-cli blogs | grep "failing-blog.com"

# Remove from DB
blogwatcher-cli remove "failing-blog.com" --yes
```

## Troubleshooting: When CLI Commands Return Empty/Unreadable Output

Sometimes `blogwatcher-cli blogs` or `blogwatcher-cli articles` return empty or garbled output (encoding issues, terminal rendering problems). Fall back to direct SQLite queries:

```bash
# List all tracked blogs with last scan date
sqlite3 ~/.blogwatcher-cli/blogwatcher-cli.db \
  "SELECT name, url, feed_url, last_scanned FROM blogs ORDER BY name;"

# List articles for a specific blog (newest first)
sqlite3 ~/.blogwatcher-cli/blogwatcher-cli.db \
  "SELECT a.title, a.url, a.published_date, a.is_read FROM articles a JOIN blogs b ON a.blog_id = b.id WHERE b.name = 'blogname.com' ORDER BY a.published_date DESC LIMIT 20;"

# Count articles per blog
sqlite3 ~/.blogwatcher-cli/blogwatcher-cli.db \
  "SELECT b.name, COUNT(a.id) as article_count FROM blogs b LEFT JOIN articles a ON b.id = a.blog_id GROUP BY b.name ORDER BY article_count DESC;"

# Find unread article count
sqlite3 ~/.blogwatcher-cli/blogwatcher-cli.db \
  "SELECT COUNT(*) FROM articles WHERE is_read = 0;"

# Check DB schema
sqlite3 ~/.blogwatcher-cli/blogwatcher-cli.db ".schema"
```

**Tables**: `blogs` (id, name, url, feed_url, scrape_selector, last_scanned), `articles` (id, blog_id, title, url, published_date, discovered_date, is_read, categories), `schema_migrations`.

## Fix workflow for broken feeds

```bash
# 1. Remove the broken entry from the DB (not just OPML)
blogwatcher-cli remove "broken-blog.com" --yes

# 2. Verify the correct feed URL
curl -sL -o /dev/null -w "%{http_code}" "https://blog.com/feed.xml"

# 3. Re-add with correct URL
blogwatcher-cli add "broken-blog.com" "https://blog.com" --feed-url "https://blog.com/correct-feed.xml"
```

## Excluding Blogs for Content Reasons (Off-Domain)

When a tracked blog's content is rarely or never relevant to the wiki domain (e.g., no AI/LLM content from a systems-programming blog), exclude it from RSS monitoring while preserving any wiki entity pages. This is distinct from broken-feed removal — the feed works, but the signal-to-noise ratio is too low.

### Full Removal Workflow

1. **Verify the blog is in OPML and DB**: `grep -n "blog-name" ~/ai-topics/config/feeds/blogs.opml` and `/opt/data/bin/blogwatcher-cli blogs | grep "blog-name"`

2. **Remove from OPML**: Use `patch` to delete the `<outline>` line. After removal, validate:
   ```bash
   python3 -c "import xml.etree.ElementTree as ET; ET.parse('/opt/data/ai-topics/config/feeds/blogs.opml'); print('OPML OK')"
   ```

3. **Remove from blogwatcher DB** (always do both — OPML and DB are independent):
   ```bash
   /opt/data/bin/blogwatcher-cli remove "Blog Name" --yes
   ```

4. **Check for entity page**: `search_files path=~/wiki/entities pattern="author-or-domain-name"`
   - **If entity page exists**: update it with a Monitoring section marking RSS as excluded
   - **If no entity page**: skip — nothing to update in wiki

5. **Update entity page** (if one exists):
   - Remove the RSS URL from the infobox if present
   - Add or update a Monitoring section:
     ```markdown
     ## Monitoring

     | Source | Method | Status |
     |--------|--------|--------|
     | RSS Feed | — | ❌ Excluded (YYYY-MM-DD) — AI content is rare; RSS removed from blogwatcher + OPML to reduce noise |
     ```
   - Bump `updated:` date in frontmatter

6. **Update wiki/index.md**: Append exclusion note to the entity's index entry (e.g., `RSS excluded (YYYY-MM-DD, AI content rare)`)

7. **Update wiki/log.md**: Prepend a log entry documenting what was removed and why. Use `python3` prepend to avoid `---` frontmatter anchor traps:
   ```bash
   python3 -c "
   with open('/opt/data/wiki/log.md') as f: content = f.read()
   entry = '## [YYYY-MM-DD] config | RSS exclusion — Name\n\n...\n\n'
   with open('/opt/data/wiki/log.md', 'w') as f: f.write(entry + content)
   "
   ```

8. **Commit and push**:
   ```bash
   cd ~/ai-topics && git add config/feeds/blogs.opml wiki/ && git commit -m "config: exclude Blog Name from RSS monitoring (off-domain content)" && git push
   ```

### Pitfalls

- **OPML and blogwatcher DB are independent** — removing from one does NOT remove from the other. Always do both steps.
- **Don't delete entity pages** — the exclusion is at the RSS level only. The entity page records that the person/org exists and why they're excluded.
- **Don't use `blogwatcher-cli read-all` before removing** — since the blog is being removed entirely, there's no need to mark old articles as read.
- **Exclusion is reversible** — if the author later starts writing AI content, re-add by following the Check-and-Add workflow. The entity page's Monitoring section documents the exclusion reason and date, making it easy to revisit.
- **Commit includes `wiki/`** when entity/index/log were updated, unlike simple OPML-only config commits.

- Auto-discovers RSS/Atom feeds from blog homepages when no `--feed-url` is provided.
- Falls back to HTML scraping if RSS fails and `--scrape-selector` is configured.
- Categories from RSS/Atom feeds are stored and can be used to filter articles.
- Import blogs in bulk from OPML files exported by Feedly, Inoreader, NewsBlur, etc.
- Database stored at `~/.blogwatcher-cli/blogwatcher-cli.db` by default (override with `--db` or `BLOGWATCHER_DB`).
- Use `blogwatcher-cli <command> --help` to discover all flags and options.
- **blogwatcher-cli does NOT follow HTTP redirects** — this is the #1 cause of scan failures when importing from OPML files with outdated URLs.
