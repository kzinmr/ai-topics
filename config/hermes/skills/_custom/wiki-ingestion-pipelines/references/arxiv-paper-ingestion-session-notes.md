# arXiv Paper Ingestion — Session Notes (2026-08-19, arXiv:2607.28802)

Reference example of a clean end-to-end arXiv ingest via user request. Useful as a worked template.

## Working Sequence (what actually ran)
1. `curl -sL "https://arxiv.org/abs/{id}" | grep -E 'citation_|<title>'` → title, authors, date, abstract, category, arXiv id, pdf_url. (No API needed, no rate limit.)
2. `curl -sL "https://r.jina.ai/https://arxiv.org/html/{id}"` → full markdown to `/tmp/paper_*.txt`. For 2607.28802 this was ~211KB / 738 lines. Read in slices with `read_file` offset/limit (file too big for one read).
   - **Strip the 4 Jina header lines** (`Title:`, `URL Source:`, `Published Time:`, `Markdown Content:`) before embedding into the raw paper file.
3. Semantic Scholar API for `publicationVenue` / `citationCount` — **returned 429** (rate-limited, no key). Treated as "no venue confirmed via S2", fell back to abstract-page meta tags for venue detection. Abstract page had **no "Comments:" field** → arXiv-only.
4. Triage: all 7 authors at Scale AI → tech-company tech report → ✅ OK per matrix. (Even if treated as arXiv-only, user explicitly requested → user override, noted in raw frontmatter `venue:` as `...; ingested via user request — user override`.)
5. Save raw to `wiki/raw/papers/{YYYY-MM-DD}_{arxiv_id}_{short-title}.md` with `type: paper`, `arxiv_id`, `venue`, `published`, `authors`, `affiliation`, `abstract`, `sources`. Add a provenance note in the body stating the extraction method + triage decision.
6. Create concept page `wiki/concepts/{descriptive-slug}.md`:
   - frontmatter: `type: concept`, `created`/`updated`, `tags` (all verified against SCHEMA.md), `aliases`, `related`, `sources` (raw paper + arxiv URL).
   - body: definition, mechanism, full failure-mode table(s), worked examples, validation results, significance/positioning, limitations, related pages (≥2 wikilinks), sources.
7. **Verify wikilink targets against `wiki/index.md`** before committing — `[[concepts/llm-trace-judge]]` links to a page whose file is `concepts/evaluation/llm-trace-judge.md`. Index keys by display name, not file path. Grep index.md for each slug you link.
8. `patch` the owning entity page (e.g. `entities/scale-ai.md`): add the paper to Key Facts + bump `updated:`. Use `patch`, not `write_file` (page is rich, >40 lines).
9. Update `index.md` (add entry under correct lettered section, keep alphabetical) and `log.md` (append entry).
10. `cd ~/ai-topics && git add wiki/ && git commit && git push`. Pre-commit runs index.md validation + tag validation — both passed.

## Pitfalls hit this session
- **arXiv API was NOT used at all** — abstract-page meta tags + Jina HTML were sufficient. The `export.arxiv.org/api/query` endpoint is unnecessary for a single known ID; prefer the direct `/abs/` scrape.
- **Semantic Scholar 429 without API key** — don't block on it. Venue can be confirmed from abstract-page meta tags; S2 is a nice-to-have for citation count.
- **Jina output is large** — save to `/tmp` and read in slices; do not pipe straight into context.
- **Wikilink path vs index-name mismatch** — always grep `index.md` to confirm the link form before writing `[[...]]`.
- **Tag validation**: all tags in frontmatter must exist in `wiki/SCHEMA.md` or the pre-commit tag validator blocks the commit. Verify each tag with `grep -o "{tag}" wiki/SCHEMA.md` (note: SCHEMA.md is one long taxonomy line, so use `-o` count, not `-c` line-count).

## Triage outcome for arXiv:2607.28802
- Tech-company report (Scale AI), arXiv-only, no peer-reviewed venue found.
- Ingested via user request (override). Raw frontmatter `venue:` documents the override.
