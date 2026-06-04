# Corporate Blog Tracking: Sitemap Monitor Integration

## Architecture

```
sitemap_monitor.py (no_agent cron, 06:00 UTC)
  ├── Anthropic Engineering → sitemap.xml → /engineering/ URLs
  └── (extensible: add SOURCES entries)
        │
        ▼ new articles scraped → wiki/raw/articles/
        │
        ▼ dreaming pipeline (18:00 UTC) picks up raw articles → wiki pages
```

## OPML Structure

The OPML at `config/feeds/blogs.opml` uses two groups:

### Individual Blogs (76 entries)
```xml
<outline text="Individual Blogs" title="Individual Blogs">
  <outline type="rss" text="simonwillison.net" ... />
  ...
</outline>
```

### Company Tech Blogs (11 entries)
```xml
<outline text="Company Tech Blogs" title="Company Tech Blogs">
  <!-- RSS-based -->
  <outline type="rss" text="OpenAI News" xmlUrl="https://openai.com/news/rss.xml" ... />
  <outline type="rss" text="Sierra Blog" xmlUrl="https://sierra.ai/rss.xml" ... />
  ...
  <!-- Sitemap-based (no RSS available) -->
  <outline type="sitemap" text="Anthropic Engineering" xmlUrl="https://www.anthropic.com/sitemap.xml" htmlUrl="https://www.anthropic.com/engineering" />
</outline>
```

## sitemap_monitor.py: Adding a New Source

Edit the `SOURCES` list in `~/ai-topics/scripts/sitemap_monitor.py`. Each source uses this template:

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

**Example with real data** (10 sources as of 2026-05-08):
```python
SOURCES = [
    {
        "name": "Anthropic Engineering",
        "url": "https://www.anthropic.com/engineering",
        "sitemap_url": "https://www.anthropic.com/sitemap.xml",
        "url_pattern": "/engineering/",
        "file_prefix": "anthropic-engineering",
        "title_suffixes": [" \\ Anthropic", " | Anthropic"],
        "state_file": os.path.expanduser("~/.hermes/processed_anthropic_engineering.json"),
    },
    {
        "name": "Cohere Blog",
        "url": "https://cohere.com/blog",
        "sitemap_url": "https://cohere.com/sitemap.xml",
        "url_pattern": "/blog/",
        "file_prefix": "cohere",
        "title_suffixes": [" | Cohere"],
        "state_file": os.path.expanduser("~/.hermes/processed_cohere_blog.json"),
    },
    # ... 8 more sources
]
```

**Key fields**:
- `file_prefix` — **required.** Prevents filename collisions between sources. Raw articles saved as `{date}_{file_prefix}_{slug}.md`.
- `title_suffixes` — **optional but recommended.** Many corporate blogs append `" | Company Name"` to `<title>`. Stripping these keeps downloaded article titles clean.
- `url_pattern` — must match blog post URLs exactly. Too broad a pattern (e.g., `/`) matches every page.

After editing:
1. Copy to `~/.hermes/scripts/sitemap_monitor.py`
2. Run once to seed the state file: `/opt/data/.hermes/venv/bin/python ~/.hermes/scripts/sitemap_monitor.py`
3. Add OPML entry with `type="sitemap"`
4. Commit both files

## Real-World RSS Discovery Patterns

| Blog | RSS URL | How Found |
|------|---------|-----------|
| OpenAI Developers Blog | `https://developers.openai.com/rss.xml` | `<link rel="alternate">` in HTML (root-level, NOT `/blog/rss.xml`) |
| OpenAI News | `https://openai.com/news/rss.xml` | Root-level trial-and-error |
| OpenAI Alignment Research | `https://alignment.openai.com/rss.xml` | Root-level trial-and-error |
| Sierra Blog | `https://sierra.ai/rss.xml` | Root-level trial-and-error (not advertised in HTML) |
| Anthropic Engineering | NONE (sitemap-based) | Sitemap at `anthropic.com/sitemap.xml` has `/engineering/` URLs with `lastmod` |

**Key insight**: Corporate blogs often place RSS at the domain root (`/rss.xml`) rather than under the blog subdirectory (`/blog/rss.xml`). Always check root-level paths first.

## Anthropic Engineering: Sitemap → Scrape Pipeline

The sitemap at `https://www.anthropic.com/sitemap.xml` provides:
- All `/engineering/` article URLs
- `lastmod` dates for each URL
- ~24 articles as of 2026-05-08

The `sitemap_monitor.py` script:
1. Parses the sitemap XML
2. Filters to `/engineering/` URLs
3. Compares against `~/.hermes/processed_anthropic_engineering.json` (seen URLs)
4. For new URLs: fetches page, extracts `<article>` content with BeautifulSoup, saves to `wiki/raw/articles/{date}_{file_prefix}_{slug}.md`
5. Updates the seen-URLs state file

## Migration: Scrape-Selector → Sitemap

When a blog was originally added with `--scrape-selector` but has a usable sitemap:

```bash
# 1. Verify sitemap has the blog URLs
curl -s "https://www.anthropic.com/sitemap.xml" | grep "/engineering/" | wc -l

# 2. Remove from blogwatcher DB
/opt/data/bin/blogwatcher-cli remove "Anthropic Engineering" --yes

# 3. Add to sitemap_monitor.py SOURCES

# 4. Update OPML: change type="rss" to type="sitemap", update xmlUrl to sitemap URL

# 5. Seed the state file
/opt/data/.hermes/venv/bin/python ~/.hermes/scripts/sitemap_monitor.py

# 6. Commit
cd ~/ai-topics && git add config/feeds/blogs.opml scripts/sitemap_monitor.py && git commit && git push
```
