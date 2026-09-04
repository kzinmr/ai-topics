# Direct Article Ingestion Pattern

**When to use**: Simple article ingestion where the source is a single web page, the topic fits an existing wiki structure, and no multi-source enrichment is needed. Lighter alternative to the full enrichment workflow in SKILL.md.

**Trigger signals**: User says "ingest this article" or "add this to wiki" with a single URL. Topic maps cleanly to an existing or new concept/entity page.

## Workflow (7 steps)

### 1. Extract article content
```bash
curl -sL --max-time 30 "URL" -o /tmp/article.html
python3 -c "
from bs4 import BeautifulSoup
with open('/tmp/article.html') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
for tag in soup(['script', 'style', 'nav', 'footer', 'header']):
    tag.decompose()
main = soup.find('article') or soup.find('main') or soup.body
print(main.get_text(separator='\n', strip=True)[:15000])
"
```
- For Apple ML Research: `article` tag works well
- For SPA/JS-rendered sites: fall back to `delegate_task` with browser toolset
- If content truncated: try `execute_code` + httpx/BS4 for larger extraction

### 2. Check existing pages
- `search_files` in `wiki/index.md` with `target=content` for topic keywords
- `search_files` in `wiki/entities/` and `wiki/concepts/` with `target=files` for filename matches
- **Read existing pages before modifying** — respect 40+ line pages (no overwrite, use patch)

### 3. Save raw article
- Path: `wiki/raw/articles/YYYY-MM-DD_slug.md`
- Include: source URL, date, fetched date, full extracted content
- Filename policy: see `raw-article-filename-policy` skill

### 4. Create new page OR update existing
- Check SCHEMA.md tags taxonomy first (read tag section, not whole file)
- For new concept pages: frontmatter with `type: concept`, required tags, sources, related
- For comparison additions to existing pages: add section before Sources heading
- Minimum 2 outbound wikilinks per new page
- Use `patch` for existing rich pages (>40 lines), never `write_file`

### 5. Update index.md
- Insert entry in alphabetical order under correct section
- Update header counts (Total pages, section counts)
- Format: `- [[path/slug]] — One-line summary`

### 6. Update log.md
- Append-only (never overwrite)
- Format: `- YYYY-MM-DD: Description of change`

### 7. Commit and push
```bash
cd ~/ai-topics && git add wiki/ && git commit -m 'wiki: <summary>' && git push
```
- Pre-commit hooks validate tags and index structure
- If tag blocked: add tag to SCHEMA.md first, then recommit

## Pitfalls

- **`search_files` with glob patterns on `wiki/` root**: Use `target=files` with specific subdirectory (e.g., `wiki/entities/`) not `wiki/` — broader paths may miss matches
- **Comparison tables in existing pages**: Insert before `## Sources` section, not at end
- **Apple ML Research pages**: Use `curl` + BS4 (SSR pages). Avoid `web_extract` which may timeout on large pages
- **Index line format**: Check if lines have `NNN|` prefix (baked-in corruption) before patching — use raw `head -N` to verify
