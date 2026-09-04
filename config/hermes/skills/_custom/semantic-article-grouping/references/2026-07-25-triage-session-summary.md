# Session Insights from Newsletter Triage (2026-07-25)

## What Worked Well

1. **Inbox summary → URL resolution → blog-triage cross-reference** pipeline was effective. Inbox correctly identified 2 critical + 3 high newsletters. URL resolution confirmed content for 4/5 newsletters. Blog-triage cross-reference correctly caught Claude Opus 5 overlap.

2. **Batch efficiency**: 76 candidate links → 13 decisions (82% reduction) by:
   - Filtering substack UI noise (12 UUID links, 7 author profiles, 12 play_card/like/share/comment links per newsletter)
   - Batch-skipping beehiiv after one Cloudflare detection
   - Cross-referencing known-content newsletters (Simon Willison) against existing event pages

3. **Cross-pipeline timestamp check**: Blog-triage JSON had `triage_timestamp` from same day (10:09 UTC). Newsletter-triage at 10:12 UTC correctly used it for dedup.

## Verified Dedup Patterns

| Dedup Pattern | Occurred? | Detail |
|--------------|-----------|--------|
| Same-day blog-triage cross-ref | ✅ | Simon Willison Claude Opus 5 blog (reference) → AINews newsletter (downgraded to reference) |
| Event page dedup | ✅ | OpenAI-HuggingFace incident event page (created Jul 24) caught Simon Willison's entire newsletter |
| sitemap-monitor dedup | ✅ | Harvey Opus 5 article scraped at 06:00, Simon Willison Opus 5 article in raw/articles/ |
| Entity page dedup | ✅ | Simon Willison entity page already had fireside chat content |
| Pure-podcast pattern | ✅ | Hugo Bowne had 10 audio UI links (+ standalone body text, so not skipped) |

## What to Avoid

- **URL-based dedup**: `d.get('url')` collapses items from the same newsletter post URL. Use `d.get('item_id')` instead.
