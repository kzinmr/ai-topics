# User-Provided Analysis Enrichment Pattern

When the user sends their own analysis/attachment (Discord, text file, etc.) to be integrated into the wiki, the workflow differs from both "create from web research" and "enrich from external article":

## Distinctive Signals
- User says 「添付の考察を既存の概念ページと関連づける/補強する形で取り込んで」
- User says 「添付した別の人の分析も取り込んで」
- User provides a `.txt` or markdown attachment with their own structured analysis
- The analysis typically offers a **complementary perspective** on an existing concept (not a correction or replacement)

## Two Variants

### Variant A: Single-Page Enrichment (most common)
The analysis deepens one existing concept. Add as a new section — don't create new pages.

### Variant B: Multi-Page Creation (comprehensive analysis)
**Trigger**: The analysis is 5,000+ words, covers multiple distinct concepts, cites 15+ external sources, and introduces new terminology not yet in the wiki. **In this case, create new concept pages in parallel via `delegate_task`, then enrich related entity pages.**

The Variant B workflow was proven in the 2026-05-25 SaaS-FDE-AI Agent session (one 9,700-byte analysis → 4 new concept pages + 5 entity enrichments).

## Workflow (Variant A — Single Page)
```
wiki/raw/articles/YYYY-MM-DD_<author>_<short-slug>.md
```
Preserve the full analysis with frontmatter (`title`, `source`, `author`, `date`, `type: analysis`, relevant tags).

### 2. Identify Target Page(s)
- The analysis usually targets an **existing concept page** — not creating a new one
- Search for the concept with `search_files` in `wiki/concepts/`
- Read the existing page fully to understand current structure and coverage

### 3. Enrich, Don't Replace
- Add the analysis as a **new section** — do NOT rewrite the entire page
- Title the section to clearly signal it's a complementary perspective (e.g., "Execution Semantics: The Control System Layer" vs the existing "Anatomy" infrastructure view)
- Use tables, diagrams, and comparison structures from the user's analysis verbatim where possible
- Keep existing content intact; the new section adds depth, not correction

### 4. Update Summary/Frontmatter
- Broaden the page's Summary to acknowledge the new perspective
- Add the raw article to `sources:` in frontmatter
- Update `updated:` date
- Add any new aliases if the analysis introduces alternative naming

### 5. Cross-Reference Related Pages
The user's analysis often clarifies relationships between concepts. Update related pages:
- Add a new short section (e.g., "Harness vs Runtime: The Critical Distinction" in `agent-harness.md`)
- Update "See Also" or "Relationship to Other Concepts" sections
- Add new `[[wikilinks]]` to pages that should be connected

### 6. Standard Wiki Hygiene
- Update `wiki/index.md` — expand the entry description to reflect the page's broadened scope
- Update `wiki/log.md` — prepend a log entry with `**New sections added**`, `**Updated pages**`, and `**Key insight**`
- `git add` only the changed files (don't accidentally commit unrelated dirty files)
- Commit with `git commit -m 'wiki: <summary>'`
- Push

## Pitfalls
- **Don't create a new page when an existing one works** — unless the analysis is comprehensive enough (5,000+ words, multiple distinct concepts) to warrant Variant B. When in doubt, use Variant A.
- **Don't delete or replace existing content** — the user's analysis is additive, not corrective (unless explicitly stated)
- **Check tags against SCHEMA.md** — new tags need SCHEMA.md additions first, or use existing canonical tags. For Variant B, identify ALL needed new tags before creating any pages, add them to SCHEMA.md, THEN create pages in parallel.
- **Update BOTH the enriched page and its cross-referenced pages** — the analysis almost always clarifies relationships, not just deepens one page
- **Include the "Key insight" in log.md** — future sessions need to understand why the page was restructured around a dual perspective
- **Variant B pitfall — subagents may independently determine tags** — when creating multiple pages via parallel `delegate_task`, each subagent independently checks SCHEMA.md for tag validity. If you add new tags to SCHEMA.md before dispatching subagents, they'll find them. Otherwise, they'll remove non-canonical tags from their output.
- **Variant B pitfall — index.md insertion after parallel writes** — after subagents create pages, the parent must insert all entries into index.md. Use individual `patch` calls with unique multi-line anchors (see §"Index.md Insertion After Parallel Creation" below). Process bottom-up (highest line number first) to preserve line offsets.

## Example Session (Variant A)
User sent "agent-runtime execution semantics" analysis → saved as `raw/articles/2026-05-15_kzinmr_agent-runtime-execution-semantics.md` → enriched `concepts/agent-runtime.md` with §"Execution Semantics" → added §"Harness vs Runtime" to `concepts/agent-harness.md` → updated index.md and log.md → committed.

## Example Session (Variant B)
User sent "SaaS-FDE-AI Agent時代の構造分析" (9,700 bytes, 19 sources cited) → saved as `raw/articles/2026-05-25_saas-fde-ai-agent-era_career-strategy.md` → identified 4 new concept pages + 5 existing pages to enrich → added 7 new tags to SCHEMA.md (proactive) → Round 1: 3 parallel concept page creations via `delegate_task` → Round 2: 1 concept page + 2 entity enrichments via `delegate_task` → Round 3: 2 entity enrichments via `delegate_task` → parent inserted 4 entries into index.md (4 separate `patch` calls, bottom-up order) → prepended log.md via `execute_code` → committed 13 files (698 insertions).

## Index.md Insertion After Parallel Creation

When multiple new concept pages are created by subagents, the parent must insert them into index.md alphabetically:

1. **Identify insertion points**: Use `execute_code` with Python to scan the Concepts section, sort existing slugs, and find the alphabetical neighbors for each new slug
2. **Verify anchors**: `sed -n 'M,Np'` the 2-3 lines around each insertion point to get clean content (not `read_file` with line-number prefixes)
3. **Insert bottom-up**: Start with the highest line number entry, then work up — this preserves line offsets
4. **Use unique multi-line anchors**: Each `patch` should include 1 preceding line + insertion + 1 following line to ensure uniqueness
5. **Update header counts**: After all insertions, update both the section count (`## Concepts (N pages)`) and the index header (`Total pages:`, `Indexed entries:`, `Not in index:`)
6. **Verify**: `python3 scripts/validate_index.py` after all insertions
