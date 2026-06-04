# Diff-First Ingestion for Comprehensive Articles

When a single article covers an entire domain exhaustively (exam syllabi, architecture guides, full courses), the standard "create pages for every concept" approach creates 10-20 fragmented pages with high overlap against existing content. Instead, use **diff-first ingestion**:

## When to Use This Pattern

- Article is a **comprehensive reference** (exam guide, full course, architecture overview, best-practices compilation)
- Covers **5+ distinct subtopics** that form a coherent whole
- Wiki already has **10+ existing pages** in the topic area
- User explicitly asks to "integrate the differences" (「差分を取り込んで」)

## The 5-Step Workflow

### 1. Full Content Extraction
Get the complete article content. For X Articles, use `tweet.fields=article` on the parent tweet (NOT `note_tweet` — X Articles require the `article` field). Save raw content to `wiki/raw/articles/`.

### 2. Exhaustive Wiki Survey (CRITICAL — don't skip)
Run a comprehensive filesystem scan for ALL existing pages in the topic area:

```python
import os, re
wiki = "/opt/data/ai-topics/wiki"
all_files = []
for root, dirs, files in os.walk(wiki):
    for f in files:
        if f.endswith('.md') and any(kw in f.lower() for kw in KEYWORDS):
            all_files.append(os.path.join(root, f))
```

Also scan `index.md` for related entries. Skim the most relevant pages (not just filenames) — check their current content depth.

### 3. Diff Analysis
Create a mental (or explicit) diff table:

| Topic | In Article? | In Wiki? | Depth in Wiki | Action |
|-------|-----------|---------|---------------|--------|
| agentic loop stop_reason | ✓ | ✗ (only mentioned in passing) | N/A | NEW |
| hub-and-spoke isolation | ✓ | Partially (subagents.md covers general pattern) | Medium | ENRICH |
| CLAUDE.md hierarchy | ✓ | Partially (claude-md-rules.md covers rules, not hierarchy) | Low | ENRICH |

### 4. Minimal Creation + Selective Enrichment

**Create ONE comprehensive umbrella page** that captures ALL genuinely new knowledge:
- Name: `{topic}-{scope}.md` (e.g., `claude-certified-architect-domains.md`)
- Content: All domains/sections as subsections with cross-references to existing wiki pages
- This keeps the new knowledge coherent and discoverable

**Enrich 2-3 existing pages** with narrow, high-signal additions:
- Add a new subsection at the end of the page
- Keep additions focused on exam/domain-specific knowledge not already covered
- Cross-reference back to the new umbrella page

**Do NOT create individual pages for every subtopic** — it fragments the knowledge and creates thin pages that duplicate existing content.

### 5. Attribution
Create a stub entity page for the article author (if notable and not already in wiki). Link it to the umbrella page.

## Anti-Patterns (Avoid)

- **Creating 10+ thin concept pages** for exam domains — these will have high overlap with existing pages and low individual value
- **Skipping the wiki survey** — leads to duplicate pages that require cleanup
- **Enriching every tangentially related page** — pollutes existing pages with marginally relevant exam trivia
- **Not reading existing page content** — "claude-code.md exists" ≠ "agentic loop mechanics are covered"

## Example Session

Session: @hooeem "I want to become a Claude architect (full course)" — 5 domains, 100K chars

Output:
- **1 new concept page**: `claude-certified-architect-domains.md` (19.7KB, all 5 domains)
- **2 enriched pages**: `subagents.md` (+hub-and-spoke section), `claude-code-best-practices.md` (+hierarchy section)
- **1 entity page**: `hoeem.md` (stub)
- **1 raw article**: `2026-03-15_hooeem_claude-certified-architect-full-course.md`

Token efficiency: ~25K tokens for comprehensive ingestion vs. ~80K+ for per-topic approach.
