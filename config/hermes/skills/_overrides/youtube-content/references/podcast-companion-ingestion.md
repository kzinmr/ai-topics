# Podcast Companion Ingestion Pattern

When the user provides a YouTube podcast episode that is a **companion/discussion** of an already-ingested article (e.g., "this is similar context, add it too"), the workflow differs from standalone ingestion: the focus is on **enriching existing pages**, not creating new ones.

## Recognition Signals

- User says "similar context" / "same topic" / "add this too"
- The podcast guest is the same author as a recently ingested article
- The podcast title/description overlaps with existing wiki concept pages
- The episode was published within days of the related article

## Workflow

### 1. Fetch & Save Raw Transcript
Standard yt-dlp → VTT dedup → save to `wiki/raw/articles/`. Include `host:` and `guest:` in frontmatter for panel/discussion type.

### 2. Parallel Delegate Task (2 subagents)

Send TWO delegate_task subagents concurrently:

**Subagent A — Structured Analysis:**
- Goal: "Extract key new content from [guest]'s [podcast name] appearance that goes beyond the [article name] essay for wiki enrichment"
- Reads raw transcript + the previously ingested article
- Outputs a structured JSON analysis file (`raw/articles/YYYY-MM-DD_slug-analysis.json`)
- Sections: new_predictions, expanded_nuances, key_quotes, data_points

**Subagent B — Entity Page Enrichment:**
- Goal: "Enrich [guest name] and [host name] entity pages with this podcast appearance"
- Reads raw transcript + existing entity pages
- Updates entity pages with podcast appearance, predictions, new quotes
- Updates host's entity page with episode listing

### 3. Parent Enriches Concept Page

After subagents complete, the parent:
- Reads the analysis JSON (from subagent A)
- Adds new sections to the relevant concept page(s):
  - New Nuances/expansions beyond the original article
  - Podcast-specific framing (e.g., "Automation is a lie" vs the essay's "5-step loop")
  - Role predictions, economic arguments, architectural shifts not in the essay
- Updates concept page tags and sources

### 4. SCHEMA Tag Check

The podcast may introduce topics not covered in the original article. Check if new tags are needed in `wiki/SCHEMA.md` before committing.

### 5. Update Metadata & Commit

- `wiki/log.md`: Consolidated entry covering transcript, analysis, entity enrichment, concept enrichment
- `wiki/index.md`: Only if NEW pages were created (usually not for companion ingestion)
- Git commit with a message mentioning both the podcast and the companion relationship

## Example

**Original article**: Dan Shipper's "After Automation" (every.to, 2026-05-21)
**Companion podcast**: Lenny's Podcast Ep.4D3hDmGhFhA (2026-05-24)

Result:
- Raw transcript saved
- Analysis JSON created (12 predictions, 7 new, 6 expanded)
- `dan-shipper.md` enriched with Lenny's Podcast appearance + predictions
- `lenny.md` enriched with episode
- `after-automation.md` expanded with Economic Consequences, 12 Predictions, Role Changes, Architectural Shifts
- New tag `saas` added to SCHEMA

## Pitfalls

- **Don't create duplicate concept pages**: The podcast is a companion, not a standalone topic. Enrich existing pages.
- **Subagent writes need verification**: Subagents enriched entity pages but the parent must verify and also enrich concept pages.
- **Tag sprawl**: The podcast may mention concepts (like SaaS economics) not in any existing page — add tags to SCHEMA first.
- **Log duplication**: When a subagent also writes to log.md, the parent's patch may create duplicate headings. Ensure old_string is unique.
