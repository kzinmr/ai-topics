# Inbox Summary Overallocates to Pure Link Digests

The inbox pre-triage summary rates newsletters based on subject line and metadata only — it cannot distinguish a substantive editorial roundup from a shallow link digest.

## June 2026 Validation

True Positive Weekly #166 was rated `relevance: "high"` with `action: "scrape_article"` by the inbox, but the actual post body was a 23-paragraph shallow bullet list matching the "pure link digest" skip pattern.

## Action

Always independently verify article body depth before accepting the inbox's "high" or "critical" classification for weekly-roundup style newsletters.
