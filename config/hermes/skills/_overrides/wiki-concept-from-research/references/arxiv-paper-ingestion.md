# arXiv Paper Ingestion for Concept Pages

When the user provides an arXiv URL and says "wikiに取り込んで" (or "wikiに追加して"), follow this pipeline.

## Pipeline

### 1. Extract paper content

```bash
web_extract on https://arxiv.org/abs/XXXX.XXXXX  # abstract page
web_extract on https://arxiv.org/pdf/XXXX.XXXXX   # PDF (more reliable than HTML)
web_extract on https://huggingface.co/papers/XXXX.XXXXX  # HF papers page (supplementary)
```

The PDF route is more reliable than `arxiv.org/html/` — the abstract page gives a good summary but the PDF gives full content.

**Supplement with HuggingFace papers page.** When a paper has been submitted to HF (most popular recent papers), the `huggingface.co/papers/XXXX.XXXXX` page often contains richer structured metadata than the arXiv abstract: key results tables, ablation study summaries, author affiliations in a clean list, GitHub star counts, "Paper of the Day" ranking, and AI-generated metadata (summary, keywords). Use this as a supplemental source — it saves manual table extraction when the PDF content is truncated by `web_extract`'s character limit.

### 2. Dedup check (CRITICAL — before creating anything)

```bash
cd ~/ai-topics && python3 scripts/papers_index.py --check https://arxiv.org/abs/XXXX.XXXXX
```

- If **DUPLICATE** → update the existing wiki page, do NOT create a new raw paper file
- If **"No duplicate found"** → proceed

### 3. Save raw paper

Filename: `wiki/raw/papers/{YYYY-MM-DD}_{arxiv_id}_{short-title-slug}.md`

Include complete YAML frontmatter: `title`, `source` (arxiv URL), `arxiv_id`, `code` (GitHub URL if available), `date`, `tags`, `authors`, `affiliations`.

Content: full paper summary with abstract, method, experiments, key results tables, significance.

### 4. Register in papers index

```bash
cd ~/ai-topics && python3 scripts/papers_index.py --add wiki/raw/papers/{filename}.md https://arxiv.org/abs/XXXX.XXXXX
```

### 5. Determine page type

- **Model paper** (e.g., "DeepSeek-V3 Technical Report", "Llama 3 Herd of Models") → entity page in `entities/` for the model family. **Landmark model papers that establish a development paradigm also warrant a concept page** (e.g., `concepts/llm-development-paradigm.md` for Llama 3's two-stage pipeline, `concepts/grpo-rl-training.md` for DeepSeek-R1's GRPO). The test: does the paper introduce a reusable development methodology beyond the specific model? If yes → entity + concept.
- **Technique/algorithm paper** (e.g., SDAR, GRPO) → concept page in `concepts/`
- **Benchmark/dataset paper** → concept page in `concepts/`

### 6. Create concept page

Follow the main skill's Step 4 (frontmatter, tags, related pages, sources). Key additions:
- Add `sources:` pointing to `raw/papers/{filename}.md`
- Cross-reference related technique pages (e.g., SDAR → GRPO, OPD, MOPD)
- Include a comparison/relationship table if the paper builds on existing techniques

### 7. Enrich related stub pages

When the paper builds on or relates to existing wiki concepts, check if those pages are stubs:
- Look at existing related pages (from the concept page's `related:` section)
- If a page is ~25-50 lines with `status: stub` → enrich it alongside the new page
- Stub enrichment is high-value: it resolves navigation holes and prevents stale references

### 8. Cross-reference existing pages

Update related concept pages to add `[[wikilinks]]` to the new page:
- Add to `related:` frontmatter
- Add to "Related Pages" section at bottom
- Consider adding a subsection if the new paper is a significant variant (e.g., OPSD vs OPD distinction in `on-policy-distillation.md`)

### 9. Update index.md and log.md

- Add entry to `wiki/index.md` in the correct alphabetical position
- Add entry to `wiki/log.md` using `patch` (append at top, before existing entries)

### 10. Commit and push

```bash
cd ~/ai-topics
git add wiki/
git commit -m "wiki: ingest {paper_title} ({arxiv_id}) — {brief summary of changes}"
git push
```

**Tag taxonomy compliance**: The pre-commit hook validates ALL tags against `wiki/SCHEMA.md`. If blocked:
1. Remove non-canonical tags from your page frontmatter
2. Use only tags from `wiki/SCHEMA.md` taxonomy
3. Do NOT use `--no-verify` — the check prevents tag sprawl

### 11. Post-commit verification

After push, verify:
- `git log --oneline -1` shows your commit
- The new page is accessible at `wiki/concepts/{slug}.md`
- `papers_index.py --check {arxiv_url}` returns "DUPLICATE" (confirms registration)

## Common Patterns

### Technique paper + stub enrichment

Example: SDAR paper (arXiv:2605.15155) required:
- New concept page: `concepts/sdar-self-distilled-agentic-rl.md`
- Stub enrichment: `concepts/grpo-rl-training.md` (26 lines → ~90 lines, stub→complete)
- Cross-reference update: `concepts/on-policy-distillation.md` (added OPSD section + SDAR reference)

### Dedup before create

Always run `papers_index.py --check` first. If the paper was already ingested (e.g., by a cron job), update the existing page rather than creating a duplicate.

### arXiv-only papers

Papers that are arXiv preprints only (not peer-reviewed or tech company reports) should generally be **BLOCKED** unless:
- The user explicitly requests ingestion
- The paper has code released (GitHub repo)
- The paper comes from a known lab/company (DeepSeek, Meituan, Tsinghua, etc.)
- The paper introduces a genuinely novel technique with strong empirical results

## Pitfalls

- **PDF `web_extract` truncation — use `execute_code` to parse the JSON result.** When the PDF content exceeds `web_extract`'s character limit (~140K+ chars), the result is saved to a temp file as a JSON wrapper (`/tmp/hermes-results/call_*.txt`) rather than returned inline. The JSON `content` field holds the full text. Use `execute_code` with `json.load()` to extract it, then search for section headers by character offset. This is more reliable than trying to page through the truncated preview.

- **Bump `updated` on ALL enriched pages, not just the entity page.** When you modify multiple existing pages (entity page, concept pages, comparison pages) to add sources, wikilinks, or new sections, bump the `updated` date in EVERY page's frontmatter — not just the primary entity page. It's easy to forget one. After Step 8, enumerate all pages you touched and verify each one's `updated` date. In one session, `yohei-nakajima.md` was bumped but `agent-statefulness.md` (which also received new sources + wikilinks) was not.

- **index.md alphabetical placement is error-prone.** Step 9 says "in the correct alphabetical position" but wiki index entries can look deceptively close. The index sorts by the text AFTER `[[concepts/` — compare character by character, not by visual similarity. When the new page's slug starts with the same prefix as nearby entries (e.g., `activegraph` vs `activitypub`), use `grep` to find surrounding entries: `grep -n '^- \[\[concepts/a' wiki/index.md`. In one session, `activegraph` was first placed between `agent-orchestration-frameworks` and `agent-statefulness` (wrong — `acti` < `agen`) instead of before `activitypub` (correct — `active` < `activi`). The fix required a remove-then-reinsert cycle.
