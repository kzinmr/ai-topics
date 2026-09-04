# Multi-Source Book/Resource Integration

## When to Apply

When integrating a comprehensive external resource (textbook, course, technical report with multiple chapters/sections) into an existing wiki that already has partial coverage of the topic.

## Workflow

### 1. Map the resource structure

Fetch the table of contents / chapter list. For GitHub-hosted books:
```bash
curl -sL "https://api.github.com/repos/OWNER/REPO/contents/PATH" | python3 -c "import json,sys; [print(f['name']) for f in json.load(sys.stdin)]"
```

For web-hosted books, look for `<nav>` elements, `/c/` URL patterns, or `sitemap.xml`.

### 2. Identify relevant chapters (don't ingest everything)

Read chapter titles + abstracts. For each chapter, answer: "Does the wiki already have a page covering this topic?"

| Situation | Action |
|---|---|
| Wiki has **no coverage** of this topic | May warrant a new concept page |
| Wiki has a **stub** on this topic | Enrich the stub from the chapter |
| Wiki has a **rich page** on this topic | Extract only unique insights not already present |
| Chapter covers a topic **outside wiki scope** | Skip |

### 3. Fetch and summarize relevant chapters only

For selected chapters, fetch the raw content and extract:
1. **Unique insights** not present in existing wiki pages
2. **Citable formulations** (precise quotes, formulas, taxonomies)
3. **Practical techniques** with specific model attributions

### 4. Distribute to existing pages (knowledge redistribution)

Follow the knowledge-redistribution-pattern.md — each chapter's insights go to the most appropriate existing page, not all to one place.

### 5. Add source to all affected pages

Every page that received content from the resource gets the resource URL in its `sources:` frontmatter. This creates an audit trail of which pages were influenced by the resource.

### 6. Update entity page if applicable

If the resource has a known author (e.g., Nathan Lambert → rlhfbook.com), check if the author's entity page should be updated with a reference to the resource being used as a wiki source.

## Pitfalls

- **Don't create pages for every chapter**: Most chapters will enrich existing pages, not spawn new ones
- **Don't quote extensively**: Extract the insight, cite the chapter, but write it in wiki voice
- **Don't skip the TOC step**: Jumping straight to chapter content without mapping the structure leads to missing the best chapters
- **Batch commit**: All pages modified by one resource integration should be in a single git commit for traceability
- **CJK in English pages**: When the source material is in Japanese/Chinese, translate insights to English for wiki pages. Raw articles (wiki/raw/) can keep the original language.
