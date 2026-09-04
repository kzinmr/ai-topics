# arXiv Paper → Existing Wiki Page (Append Pattern)

When a user shares an arXiv paper link and the topic already has partial wiki coverage (mentions in other pages, scattered references), prefer **appending a dedicated section to the most relevant existing page** rather than creating a new standalone page.

## Pre-flight: Search for Existing Coverage

```
search_files(pattern="<topic-keyword>", target="content", path="~/wiki")
search_files(pattern="<arxiv-id>", target="content", path="~/wiki")
```

Check:
- `wiki/index.md` for concept/entity pages on the topic
- `wiki/concepts/` and `wiki/entities/` for partial mentions
- `wiki/raw/articles/` for existing raw article scrapes

If coverage exists → append to the most relevant page.
If no coverage → create a new page (standard enrichment flow).

## Workflow

1. **Fetch arXiv metadata**: `curl -s "https://arxiv.org/abs/<ID>" | grep citation_`
2. **Extract PDF**: `python3 -c "import fitz; doc = fitz.open('/tmp/paper.pdf'); print(doc[0].get_text()[:3000])"` (pymupdf)
3. **Identify target page**: Most relevant existing concept/entity page
4. **Append section**: Add `## <Topic Name>` with key innovations, comparison table, results
5. **Update frontmatter**: `sources` += arxiv URL, `updated` = today
6. **Update index if needed**: Check if `wiki/index.md` entry needs updated description
7. **Log + commit**: Append to `wiki/log.md`, `git add + commit + push`

## Pitfalls

- **Don't duplicate**: If the topic is already mentioned in a table or list (e.g., algorithm variants table), update the existing entry AND add a detailed section
- **pymupdf location**: On this server, pymupdf is at `~/.local/lib/python3.13/site-packages/` — use `python3 -c "import fitz; ..."` directly, don't use `execute_code` (may be blocked in some contexts)
- **PDF download**: `curl -sL "https://arxiv.org/pdf/<ID>" -o /tmp/paper.pdf` — the `-L` flag follows redirects

## See also

- `confirmation-update-pattern.md` — when an EXISTING rumor/exploring entry on an
  entity/event page gets CONFIRMED (deal closed, incident post-mortem published).
  Preserve the rumor history, rename the section, append a bolded confirmation
  sub-paragraph, bump `updated:` + add the primary source. Verified 2026-08-27
  (NVIDIA–Hugging Face $13B, AWS–DuckLabs).
