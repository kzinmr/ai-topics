---
name: blog-author-thought-analysis
description: Deep analysis of blog authors' recent thoughts, philosophy, and positions. Goes beyond entity page creation to extract cited ideological positions, track thought evolution, and enable ongoing RSS monitoring for thought updates.
version: 1.0.0
metadata:
  hermes:
    tags: [blog-analysis, thought-tracking, wiki-creation, RSS-monitoring, citation-extraction]
    homepage: https://github.com/kzinmr/ai-topics
prerequisites:
  commands: [python3, curl]
  skills: [blogwatcher, llm-wiki]
---

# Blog Author Thought Analysis

Extract and document blog authors' recent philosophical positions, technical stances, and thought evolution with proper citations for the AI topics wiki.

## When to Use
- User requests "analyze author's recent thoughts" or "what's their philosophy?"
- Creating wiki pages that need more than basic bio + recent titles
- Tracking ideological shifts in thought leaders over time
- Building citation-rich analysis pages for the wiki

## Pipeline Overview

```
OPML/Blog List → Check blog_authors.json → RSS Fetch → Article Scraping → Thought Extraction → Wiki Creation → RSS Monitoring
```

## Step 0: Check Pre-Scraped Data First

**Always check `~/scripts/blog_authors.json` before re-scraping.**
The `build_blog_wiki.py` script already scraped all OPML blogs and cached:
- Author name, bio, blog URL, RSS URL
- About page content
- Recent post titles/topics

```python
import json
with open('~/scripts/blog_authors.json') as f:
    authors = json.load(f)
# Search by blog URL or author name
```

If the cached data is sufficient, skip to Step 4 (thought analysis). Only re-scrape if:
- The cached bio is too short or generic
- You need recent article content (not just titles)
- The author has new posts since the last scrape

## Step 1: RSS Feed Discovery & Parsing

**Namespace Handling** (critical pitfall):
- **Atom feeds**: Strip `xmlns="http://www.w3.org/2005/Atom"` before parsing with `ElementTree`
- **RSS 2.0 feeds**: Handle `atom:` namespace prefixes in RSS feeds
- **Regex cleanup**: `re.sub(r'\sxmlns[^"]*"[^"]*"', '', xml_text)` before `ET.fromstring()`

```python
# Atom parsing example
xml_clean = re.sub(r'\sxmlns[^"]*"[^"]*"', '', xml_text)
root = ET.fromstring(xml_clean)
for entry in root.findall('.//entry'):
    title = entry.findtext('title', '').strip()
    link = entry.find('link').get('href', '')
```

## Step 2: Article Selection for Thought Analysis

**Prioritize articles that reveal philosophy/positions:**
- Opinion pieces, essays, "hot takes"
- Technical deep-dives with strong positions
- Responses to industry events
- Avoid: Release notes, tool updates, simple link blogs

**Selection criteria:**
- Recent (last 3-6 months)
- Substantive content (500+ words)
- Clear authorial voice/position

## Step 3: Deep Article Scraping

Use `web_extract` for full article content:
```python
from hermes_tools import web_extract
results = web_extract(urls=[article_url1, article_url2, ...])
```

**What to extract:**
- Key quotes and positions (with exact wording)
- Technical arguments and reasoning chains
- Evolution from previous positions
- References to other thinkers/tools
- Contradictions or nuanced stances

## Step 4: Thought Analysis & Wiki Page Creation

**Structure for thought analysis pages:**

```markdown
---
title: "Author Name"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [person, blogger, thought-analysis, ai]
aliases: ["blog-url-slug"]
---

# Author Name

| | |
|---|---|
| **Blog** | [url](url) |
| **RSS** | feed_url |
| **Social** | handles |

## Core Philosophy

### 1. [Major Position Theme]
> Direct quote with attribution
> Another key quote

Context and analysis...

### 2. [Second Major Theme]
...

## Recent Thought Evolution (YYYY)
- How positions have changed
- Key inflection points
- Emerging themes

## Key Quotes
> "Quote 1" - [Source](url)
> "Quote 2" - [Source](url)

## Related Concepts
- [[concept-1]]
- [[concept-2]]

## Sources
- [Article Title](url)
- [Another Article](url)
```

**Citation requirements:**
- Every claim needs a source URL
- Direct quotes must be verbatim with attribution
- Distinguish between author's words and your analysis

## Step 4b: Upgrading Existing Entity Pages (from build_blog_wiki.py)

`build_blog_wiki.py` generates initial entity pages for all OPML blogs, but these often contain only a Bio paste and recent titles. **Upgrade rather than recreate:**

```python
from hermes_tools import patch, read_file

# 1. Check if entity page already exists
existing = search_files(pattern=f"*{author_slug}*.md", target="files", path="~/wiki/entities/")

# 2. Read current page to preserve existing metadata
current = read_file(f"~/wiki/entities/{author_slug}.md")

# 3. Use patch to ADD thought analysis sections (don't overwrite)
patch(path=f"~/wiki/entities/{author_slug}.md",
      old_string="## Recent Posts (topics/interests)\n\n- (no recent posts found)",
      new_string="<thought analysis content>")

# 4. Update tags in frontmatter
patch(path=f"~/wiki/entities/{author_slug}.md",
      old_string="tags: [person, blogger, hn-popular]",
      new_string="tags: [person, blogger, hn-popular, thought-analysis, ai]")
```

**Upgrade priority order:**
1. Authors with known AI/tech opinions (Simon Willison, Mitchell Hashimoto, etc.)
2. Authors with substantial recent essays (not just link blogs)
3. Authors whose work directly impacts AI ecosystem

## Step 5: RSS Monitoring Setup

After creating thought analysis page:
1. Add feed to blogwatcher: `blogwatcher-cli add "Author Name" blog_url --feed-url rss_url`
2. Set up periodic scanning for new thought evolution
3. Link monitoring to wiki update workflow

## Pitfalls & Gotchas

### RSS Namespace Issues
- **Atom**: `xmlns="http://www.w3.org/2005/Atom"` breaks `ET.fromstring()` without stripping
- **RSS with Atom extensions**: Mixed namespaces require careful handling
- **Solution**: Strip all xmlns declarations before parsing

### Feed Parsing Failures
- Some feeds return empty entries due to malformed XML
- Always verify `len(entries) > 0` before proceeding
- Fallback to HTML scraping if RSS fails

### Quote Extraction Quality
- Don't paraphrase - use exact quotes for citations
- Verify quotes against original text
- Include enough context to understand the position

### Wiki Page Conflicts
- Check if entity page exists before creating new one
- If exists, **upgrade** with thought analysis rather than duplicate
- Use `patch` tool to add sections to existing pages
- **Duplicate aliases**: Some authors may have multiple entity files (e.g., `simonw.md` AND `simon-willison.md`). Use the most complete one and consider merging

### Network/Scraping Issues
- `curl` on RSS feeds may return empty due to Cloudflare or rate limiting
- If RSS fetch fails, try `web_extract` with the blog's HTML URL instead
- Some blogs (Substack, Medium) require special handling for RSS vs HTML content

## Example Workflow

```python
# 1. Fetch RSS
rss_urls = extract_from_opml("hn-popular-blogs-2025.opml")

# 2. Select substantive articles
priority_urls = [u for u in rss_urls if is_essay(u)]

# 3. Scrape full content
articles = web_extract(urls=priority_urls[:5])

# 4. Extract quotes and positions
thoughts = analyze_thoughts(articles)

# 5. Create wiki page
create_wiki_page(author, thoughts)

# 6. Set up monitoring
blogwatcher_add(author, rss_url)
```

## Related Skills
- **blogwatcher**: Ongoing RSS monitoring after initial analysis
- **llm-wiki**: Wiki maintenance and cross-referencing
- **arxiv**: For academic paper citations that may inform blog posts
- **youtube-content**: For video-based thought analysis