# Blog-to-Entity Workflow

When the user provides a blog URL (e.g., `https://thezvi.wordpress.com/`) and asks to "ingest" or "add to wiki", this is a **blog-to-entity** workflow — creating an entity page for the blog/author and adding the RSS feed for ongoing monitoring.

## Workflow

### 1. Fetch RSS Feed + About Page

```bash
# RSS — get recent posts, categories, author name, description
curl -sL "https://example.com/feed/" | head -200

# About page — get author bio, blog description, contact info
curl -sL "https://example.com/about/" | python3 -c "..." # text extraction
```

Key data to extract:
- Blog title and tagline/description
- Author name and background
- Post frequency and content focus
- RSS URL for OPML
- Canonical URL (e.g., Substack primary vs WordPress mirror)
- Categories/tags from recent posts (indicate coverage areas)
- X/Twitter handle, contact info

### 2. Check Existing Wiki (MANDATORY)

```bash
# Search for existing mentions
search_files(path="~/wiki", pattern="author-name|blog-name|domain", target="content")
grep -i "author\|blog" wiki/index.md
```

If the person already has an entity page → use `patch` to add blog info.
If no page exists → create new entity page.

### 3. Create Entity Page

Follow the standard entity template from the main SKILL.md. For blog-author entities, include:

- **Blog section**: URL, RSS, frequency, canonical vs mirror, content focus areas
- **Core Perspectives**: The author's distinctive positions (use quotes from the blog)
- **Writing Style**: Frequency, length, structure, tone
- **Notable Coverage**: Recent posts demonstrating the author's focus areas
- **Related Pages**: Minimum 2 wikilinks to existing wiki pages

### 4. Add RSS to OPML Config

```bash
# Add to ~/ai-topics/config/feeds/blogs.opml
# Insert alphabetically or at end of main section (before YouTube Channels)
```

Check for duplicates first: `grep -c "domain.com" config/feeds/blogs.opml`

### 5. Update index.md + log.md + Commit

Standard wiki update cycle:
1. Insert entry in `index.md` alphabetically under Entities
2. Append entry to `log.md` under today's date
3. `git add wiki/ config/feeds/ && git commit -m "wiki: add X entity page + blog RSS" && git push`

## Pitfalls

- **Tag taxonomy**: Always verify new tags exist in SCHEMA.md before committing. Common mismatches: `forecasting` → `prediction`, `auto-research` → `autoresearch`. Fix: `grep "tag-name" wiki/SCHEMA.md` before committing. The pre-commit hook blocks unknown tags.
- **Substack mirrors**: Many authors have Substack (primary) + WordPress/Ghost mirror. Note both URLs but mark which is canonical in the entity page.
- **OPML duplicates**: Some blogs may already be tracked via build_blog_wiki.py. Check before adding.
- **RSS-only content**: Some WordPress blogs truncate RSS content. Note if full content requires clicking through.
