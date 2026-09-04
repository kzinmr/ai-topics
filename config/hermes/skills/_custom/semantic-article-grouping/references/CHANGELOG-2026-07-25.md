# Newsletter Triage Skills Update — July 2026

## Summary
Patched `semantic-article-grouping` skill based on learnings from 2026-07-25 triage session.

## What Changed

### 1. SKILL.md — "Scheduling race condition" section overhaul
The original rule said "newsletter-triage cannot rely on same-day blog-triage JSON." This was correct for the 07:20 scheduled window but too absolute for off-schedule runs (delays, catch-up at 10:00+ UTC).

**New rule**: Check the blog-triage JSON's `triage_timestamp` field. If today's date + earlier time than newsletter-triage start → valid cross-reference. If yesterday's date → not valid.

This distinction matters because blog-triage ran at 10:09 UTC on July 25, before newsletter-triage at 10:12 UTC. The blog's Claude Opus 5 reference decision was used to correctly downgrade AINews from take to reference.

### 2. New Reference Files Added (4 files)

| File | Purpose |
|------|---------|
| `references/newsletter-triage-off-schedule-dedup-2026-07-25.md` | Concrete off-schedule cross-reference example with all 5 newsletters, timestamps, and dedup table |
| `references/2026-07-25-triage-session-summary.md` | Session-level insights: which dedup patterns fired, batch efficiency, URL vs item_id dedup pitfalls |
| `references/editorial-essay-primary-content.md` | Editorial essay variant — when a newsletter post body IS the primary content (not a link roundup). Detection, triage strategy, contrast with roundup pattern. From July 2026 Signal issue "The good, the bad and the ugly of AI writing." |

### 3. Key Insight for Future Sessions
Always check blog-triage JSON timestamp before deciding dedup validity. The race condition is time-dependent, not hard-coded to the schedule.

### 4. New Pattern: Editorial Essay Variant (July 2026)
The Signal sent an editorial essay about Substack's AI text detection (Pangram) instead of its usual link roundup format. The post body was 40 paragraphs of standalone argument with 7 supporting citations. 

**Key difference from roundup triage**: Create exactly 1 decision for the essay itself (not N decisions for N external links). The essay enriches `concepts/ai-content-transparency.md` with Substack's platform policy. See `references/editorial-essay-primary-content.md` for full detection and triage strategy.
