# Hub Page Enrichment from Child Pages

## Pattern
When a wiki has a **hub/index page** (e.g., `concepts/claude/system-cards.md`) that references individual sub-pages (e.g., `concepts/claude/opus-4-8.md`, `concepts/claude/fable-5.md`), the hub page can be enriched by:

1. **Scanning child pages** for details not yet reflected in the hub
2. **Updating the hub's index table** with missing entries
3. **Adding a milestone/evolution summary** synthesized from child page content

## Example: System Cards Index Update (2026-06-10)

**Hub page**: `concepts/claude/system-cards.md` — Anthropic System Cards index
**Child pages**: `concepts/claude/fable-5.md`, `concepts/claude/mythos.md`, `concepts/claude/opus-4-8.md`

### Steps
1. Read hub page to identify what's already indexed
2. List child pages under the same directory (`ls`, `search_files`)
3. Read each child page looking for:
   - Entries missing from the hub's table/list
   - Key milestones or structural innovations
   - Cross-references that should be bidirectional
4. Update hub page:
   - Add missing entries to the index table
   - Add a "Milestone Evolution" or "Key Trends" section synthesizing child page content
   - Remove any stale notes (e.g., "X is not listed as of Y")
5. Update `index.md` entry for the hub page (refresh description, counts)

## Pitfalls
- **Don't overwrite rich hub pages**: Hub pages often accumulate analysis over time. Use `patch`, not `write_file`.
- **Cross-reference consistency**: If child pages link to the hub, ensure the hub links back.
- **Count accuracy**: When updating index.md, count carefully (e.g., "17 system cards" not "15").
- **Stale notes**: Remove temporal notes like "as of Jun 2026" after updating — they become misleading.
