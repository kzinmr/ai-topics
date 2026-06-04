# Google Slides Ingestion Workflow

When the source is a Google Slides / Google Docs presentation.

## Extraction

**DO NOT use `web_extract` on the regular URL or `/htmlpresent`** — both hit the 5,000-char LLM summarization timeout and truncate content.

**Use the `/export/txt` endpoint instead:**

```bash
curl -sL -o /tmp/slides.txt "https://docs.google.com/presentation/d/{DOC_ID}/export/txt"
```

This returns the full slide text (all slides) without truncation. Format: each slide is separated by blank lines, slide titles appear as headers. Tables are rendered as aligned text but may lose structure.

### Alternative: `/export/pdf` for visual slides
If text export loses critical visual information (diagrams, charts, table structure), use:
```bash
curl -sL -o /tmp/slides.pdf "https://docs.google.com/presentation/d/{DOC_ID}/export/pdf"
```
Then extract with `marker-pdf` or `pymupdf`.

### File size limits
- `web_extract` LLM summarization: ~5,000 chars before timeout (config: `auxiliary.web_extract.timeout`)
- `/export/txt`: no practical limit (tested with 73 slides / 13KB)
- **Bottom line**: always prefer `/export/txt` for Google Slides text content

## Raw Article Naming

Per `raw-article-filename-policy`:
- Google Slides rarely embed creation dates → use **ingestion date** as filename date
- Add `date_ingested: YYYY-MM-DD` in YAML frontmatter (NOT `date` or `date_published`)
- Source slug: use the domain/author (e.g., `softwaredoug`)
- Content slug: 2-5 keywords from the title

Example: `2026-05-17_softwaredoug_search-evaluation-ndcg.md`

## Wiki Page Creation

A presentation typically maps to:
1. **Entity page** for the author/presenter — research via web_search + web_extract (website, GitHub, LinkedIn, Maven)
2. **Concept page** for the main topic — synthesize from slide content
3. Optionally: additional concept pages for subtopics covered in depth

## Fallback: Browser Console Extraction

When `/export/txt` returns empty content or is blocked (Google sometimes rate-limits or returns auth walls for certain docs), use the browser console approach:

1. **Navigate**: `browser_navigate` to `https://docs.google.com/presentation/d/{DOC_ID}/htmlpresent`
2. **Extract full text**: `browser_console` with `document.body.innerText.substring(0, N)` — Google Slides `/htmlpresent` renders all slide text into `document.body.innerText`. The text is ordered slide-by-slide. Start with a large substring (e.g., 15000) to see how much content there is.
3. **If truncated**: Call `browser_console` again with a higher offset: `document.body.innerText.substring(15000)` to get the remaining slides.
4. **Note**: This is less efficient than `/export/txt` (requires 2-3 round trips for large decks) but works reliably as a fallback. The `/htmlpresent` page loads all 65+ slides into the DOM, so `innerText` captures everything.

The raw text from this approach preserves slide boundaries (each slide is separated by blank lines and slide number headers like `1 / 65`) but loses rich formatting (bold, colors, layout). For visual-heavy slides, prefer the PDF export path.

## User Signals for Partial Ingestion

If user says "本文はXページ目から始まります" (content starts from page X):
- Pages 1 through (X-1) are typically intro slides: author bio, course promos, agenda
- The `/export/txt` endpoint numbers slides as `# N of Total` — use these to verify
- Skip intro slides when creating concept pages; include them in the raw article for completeness
