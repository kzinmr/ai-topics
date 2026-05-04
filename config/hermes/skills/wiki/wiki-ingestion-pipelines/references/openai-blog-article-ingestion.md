# OpenAI Blog Article Ingestion — Full Reference

Simple workflow for ingesting openai.com/blog articles.

1. **Scrape & Save**: `web_extract(url)` → save to `wiki/raw/articles/{date}-{slug}.md`
   with YAML frontmatter (title, url, date, source, author, tags)
2. **Check existing pages** → if exists, add new section; if not, create new concept page
3. **Update index.md** (correct section + alphabetical position)
4. **Update log.md** with date and summary
5. **Commit**: `cd ~/ai-topics && git add wiki/ && git commit -m "wiki: ingest OpenAI blog article - {topic}" && git push`

## Pitfalls
- OpenAI blog URLs may have `/index/` path prefix
- Always search existing wiki first
- Create minimal stub entity pages for newly mentioned people/organizations
- Update `updated` date in frontmatter of modified pages
- Total page count in index.md header must be updated
