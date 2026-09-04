# Cross-Newsletter Event Dedup — July 2026

## Pattern

A beehiiv newsletter arrives in the same batch as a Substack newsletter, both covering the **same event**. The Substack newsletter (AINews) is processed first by newsletter-wiki-ingest, creating a dedicated **event page**. By the time the beehiiv newsletter is triaged, the event page already exists with full coverage.

The inbox pre-triage summary sees the beehiiv subject and tags it as "reference" (high relevance), **unaware that an event page was already created from a different source in the same batch**.

## Concrete Example (2026-07-30)

| Newsletter | Source | Links | Status |
|-----------|--------|-------|--------|
| AINews "Fearing RSI — cosign letter to 'Pace' AI development" | Substack (swyx, pub_id=1084089) | Full body accessible | ✅ **Wiki-processed** → `events/2026-07-29-rsi-pace-letter.md` (136 lines) |
| Beehiiv "🧯 1,000+ AI Insiders Just Asked for a Brake Pedal" | Beehiiv (uid unknown) | All 20 links 403 expired | ❌ Links unreachable, same event already covered |

**Inbox summary**: take=1 (AINews), reference=1 (beehiiv)  
**Correct triage after event-page check**: take=1 (AINews), **skip** (beehiiv — already covered)

## Detection

When a beehiiv newsletter has ALL links returning 403 (expired token pattern) and the inbox summary says "reference":

1. **Extract topic from subject**: e.g., "1,000+ AI Insiders Just Asked for a Brake Pedal" → RSI Pace Letter
2. **Search for existing event page**: `find ~/wiki/events/ -name "*rsi*" -o -name "*pace*" -o -name "*letter*" -mtime -1`
3. **Search log.md**: `grep -i "keyword" ~/wiki/log.md | grep $(date +%F)` and previous day
4. **If event page exists** → the beehiiv newsletter adds no value. Mark all items as skip.
5. **Check event page `sources`** — it likely cites a different newsletter (cross-newsletter dedup confirmed).

## Why This Matters

The inbox pre-triage summary evaluates each newsletter **independently** — it cannot detect that topic from newsletter B is already fully covered by content wiki-processed from newsletter A in the same batch. The triage step must fill this gap.

## Action Logic

```
if (all beehiiv links are 403 expired)
    and (inbox summary says "reference" or "take")
    and (an event page exists for same topic, sourced from DIFFERENT newsletter)
→ Downgrade to skip
```

## Related Patterns

- **Cross-pipeline dedup (blog→newsletter, sitemap→newsletter)** — different pipeline sources
- **Cross-pipeline dedup (newsletter→blog reverse)** — reverse direction
- **Cross-newsletter event dedup (this pattern)** — two newsletters in same batch, same event
