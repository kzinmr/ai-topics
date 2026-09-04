# Dual-Layer Raw + Event Enrichment Pattern

## Problem

When a rebuttal, follow-up, or response article arrives for an existing event (e.g., OpenAI responding to Apple's lawsuit), both the raw article AND the event page need updating. Agents often update only one layer, leaving inconsistencies.

## Pattern

### Detection
- A new article is a direct response/rebuttal to a prior event already documented in `wiki/events/`
- The new article provides evidence (transcripts, emails, documents) that corrects or supplements the existing event narrative

### Workflow

1. **Check for existing event page**: `search_files(path="wiki/events", pattern="<event-keyword>", target="content")`
2. **Check for existing raw article**: `search_files(path="wiki/raw/articles", pattern="<article-slug>", target="files")`
3. **Update raw article**: Add evidence sections (transcripts, correspondence, documents) with clear section headers
4. **Update event page**:
   - Fix factual errors exposed by the new evidence (wrong names, incorrect sequences)
   - Add new sections for the rebuttal's claims with supporting evidence
   - Update the `sources:` frontmatter to include the new raw article
   - Update the `updated:` date
5. **Cross-check person names**: Verify names are consistent across raw article, event page, and related pages
6. **Update log.md**: Single entry covering both updates

### Example (OpenAI-Apple Conflict, 2026-08-05)

New article: OpenAI's "Apple is getting this wrong" rebuttal

Changes across both layers:
- `raw/articles/2026-08-03_openai_apple-is-getting-this-wrong.md`: Added iMessage transcript summary and email correspondence evidence
- `events/openai-apple-conflict-2026.md`: 
  - Fixed "Chang Li" → "Chang Liu" (name error from initial ingestion)
  - Rewrote section 4 from "Open-Source Work" to "Departure and Residual Access" (corrected characterization based on new evidence)
  - Added Tang Tan defense section
  - Updated `updated:` date

## Pitfall: Name Inconsistency Across Pages

When an event page was created from one source and the rebuttal comes from another, person names may differ (e.g., "Chang Li" vs "Chang Liu"). Always verify names against the primary source (the company's own statement). Use `grep -rn "PersonName" wiki/events/ wiki/raw/articles/` to find all occurrences and fix in one pass.

## Pitfall: Overcorrecting the Narrative

When a rebuttal provides new evidence, don't simply replace the original allegations with the rebuttal's version. The wiki should present both sides:
- Keep the original allegations (from the lawsuit) as stated
- Add the rebuttal's counter-evidence with attribution ("OpenAI claims...", "According to OpenAI's published emails...")
- Note where facts are disputed vs. where one side has conceded
