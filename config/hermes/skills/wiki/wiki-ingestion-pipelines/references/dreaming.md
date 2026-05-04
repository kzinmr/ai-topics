# Dreaming — Knowledge Consolidation Cycle (Full Reference)

## Step 0: Duplicate Check (MANDATORY)
Before processing, review adjacent scheduled jobs:
1. Daily Inbox Update (23:00 JST) — RSS scan + Newsletter triage + Wiki ingest
2. Daily Wiki Update Report (20:00 JST)
3. Daily Active Knowledge Crawl (00:00 JST)
4. Skill Inventory Check (01:00 JST)

Rules: Don't re-process, don't duplicate concept pages, reference existing assessments.

## Phase 1: Light Sleep — Screening & Grouping
Group articles by semantic themes. Flag articles appearing in multiple sources (higher significance).

## Phase 2: REM — Flat Synthesis
Weighted scoring WITHOUT newsjacking bias:
- relevance (0.30), frequency (0.25), query_diversity (0.15), recency (0.15), consolidation (0.10), conceptual_richness (0.05)
- ≥ 0.65: Create/update wiki page
- 0.45-0.65: Add to existing page or log for review
- < 0.45: Skip

## Phase 3: NJ Delivery Filter
| Score | Presentation |
|-------|-------------|
| ≥ 4 | Lead story |
| 3 | Secondary |
| 2 | Brief mention |
| ≤ 1 | Omit from delivery (wiki still updated) |

## Phase 4: Deep Sleep — Replay-Safe Integration
Check existing pages, create/update, cross-references (≥2), index/log update, commit.

## Sub-Patterns
- **A (Depth check)**: Read existing page before updating — don't update if already covered
- **B (Newsletter noise)**: Filter Substack UI elements before scoring
- **C (Batch entity)**: Create missing entity pages for recurring people/companies
- **D (Dedup matrix)**: Check filename, index entry, content grep, session_search before creating

## Pitfalls
- Duplicate detection is MANDATORY
- Always check existing pages first (don't trust 0.65 threshold alone)
- Log.md corruption via patch (accidental `|` prefix)
- Pre-run script timeout → fallback file at `/opt/data/.hermes/cron/data/dreaming/grouped_themes_latest.json`
- Stale dreaming themes (2-3 days old) may already be processed by daily pipelines
