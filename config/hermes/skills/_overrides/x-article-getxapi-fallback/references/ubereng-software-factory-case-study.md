# Case Study: Clean Tier 1.5 Success on a Corporate-Account X Article (Uber Engineering, Aug 2026)

**Source tweet:** https://x.com/ubereng/status/2093444169037762840
**Article:** "Running a Software Factory Efficiently at Uber Scale" (Uber Engineering, @udaykiran, published 2026-08-28, companion to their AI Engineer 2026 talk). 10,751 bookmarks at ingest time.

## What happened

1. User pasted an `x.com/user/status/...` URL with tracking params (`?s=46&t=...`) and asked to ingest it (Japanese request: 以下記事を取り込んで).
2. Stripped the query string, extracted tweet ID `2093444169037762840`.
3. Ran Tier 1.5 directly (no bookmark JSON available — this was an interactive manual request, not the x-bookmarks-ingest pipeline):
   ```bash
   xurl --auth oauth2 "/2/tweets/2093444169037762840?tweet.fields=article" > /tmp/uber_article.json
   ```
4. `data.article.plain_text` contained the FULL ~18.4KB article body. Zero fallbacks needed — no GetXAPI, no web_extract, no Tier 4.
5. Saved the plain_text to `wiki/raw/articles/2026-08-28_ubereng_running-software-factory-efficiently-at-uber-scale.md` with standard frontmatter (title, source URL, author, engagement metrics from the same response).

## Key takeaways

- **Corporate/brand accounts (e.g. @UberEng) work fine with Tier 1.5** — long-form X Articles from org accounts are not gated differently from personal accounts. Don't assume brand accounts need GetXAPI.
- **One xurl call gets both body AND frontmatter metadata** (title, engagement counts, preview_text, cover_media) — do a single Tier 1.5 call and reuse the response for both the raw file body and its frontmatter, instead of a separate Tier 1 `xurl read`.
- **Ingestion pattern for high-value articles**: this article was ingested not as a standalone page but by *enriching two existing concept pages* (`enterprise-ai-cost-management`, `dark-factory-software-factory`) with dated case-study sections + comparison tables, following the existing-page-first rule in AGENTS.md. The raw article carries the full text; concept pages carry the synthesized sections. index.md descriptions and log.md were updated in the same commit.
- Tier 1.5 is confirmed working as of 2026-09-01 with the profile's OAuth2 credentials — if a future session hits Tier 1.5 failures, suspect credential expiry rather than endpoint unavailability.
