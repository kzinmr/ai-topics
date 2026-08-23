# Reference Verification Report Format

Standardized table format for reporting reference candidate verification in Takes=0 saturation scenarios.

## Full Example (from 2026-07-14 dreaming-wiki-ingest)

```
## Verification of 5 Reference Candidates

All 5 reference candidates were **verified against actual wiki content** and found already covered or marginal:

| Candidate | Status | Details |
|-----------|--------|---------|
| Martin Alderson margin collapse pt 2 | ✅ Already covered | entities/martin-alderson.md lines 96-110 — Grok 4.5 pricing, Bezos quote, market bifurcation, xAI/Cursor acquisition analysis |
| Merge AI agent governance | ✅ Already covered | entities/merge-dev.md Refs section (line 85) — governance concepts documented |
| Hebbia data integrations | ✅ Already covered | entities/hebbia.md Data Integrations section (lines 49-68) — all 12+ sources listed |
| ElevenLabs AI Calling | ❌ Marginal gap | entities/elevenlabs.md covers ElevenAgents architecture well (lines 105-136). Generic AI calling data (9x cheaper, 680ms latency, $80B savings) absent but marginal |
| DOOMQL (Simon Willison) | ❌ Marginal value | Fun demo (SQLite as game engine via GPT-5.6 Sol) — not wiki-worthy as substantive entry |
```

## Decision Criteria for Each Status

### ✅ Already covered
- The entity/concept page has **substantive matching content** at the specific-claim level
- The article's central thesis, data points, and conclusions are present
- Line ranges can be cited (e.g., "lines 96-110")
- The source may already be listed in frontmatter `sources`
- **Action**: Skip enrichment. Note line ranges in the report.

### ❌ Genuine gap
- The entity/concept page exists but its body lacks the article's specific claims, metrics, or data
- The article adds novel information not present in any wiki page
- May overlap with a broader section but provides distinct new detail
- **Action**: Enrich existing page or create new page. File a `take` in the log.

### ❌ Marginal value
- The article aligns with existing content but adds only generic/contextual/overview data
- The gap is real but the information is introductory (how-to guides, marketing explainers, fun demos)
- Adding it would not materially improve the wiki's research value
- **Action**: Skip enrichment. Note marginal reason and move on.

### ❌ Already covered + source in sources
- The entity page both has the content AND lists the article URL in its sources frontmatter
- Maximum coverage signal — no enrichment needed
- **Action**: Confirm by cross-referencing line content with article body. Skip.

## Verification Workflow

1. Locate raw article: `find ~/ai-topics/wiki/raw/articles -name "*keyword*"`
2. Read article body (first 40+ lines minimum)
3. Locate entity/concept page: `find ~/ai-topics/wiki -name "*slug*" -type f`
4. Read entity page body sections in full
5. grep for specific claims/numbers in entity page
6. If claims found → note line ranges → ✅ Already covered
7. If claims absent → ❌ Genuine gap (enrich) or ❌ Marginal value (skip)
