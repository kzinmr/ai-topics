# The Signal Subdomain Bypass (confirmed July 2026)

## Discovery

When `open.substack.com/pub/thesignal/p/{slug}` returns a Cloudflare challenge page ("Just a moment..."), the publication's **native Substack subdomain bypasses** the protection entirely.

**Confirmed working**: `thesignal.substack.com/p/{slug}` resolves directly with full article body (49 paragraphs, 12,825 chars in July 2026 test).

## Resolution Order

When encountering a The Signal newsletter during triage:

1. **Try `thesignal.substack.com/p/{slug}` first** — this bypasses Cloudflare on `open.substack.com` and `thesignal.substack.com` itself is not Cloudflare-protected (as of July 2026)
2. **Fall back to `open.substack.com/pub/thesignal/p/{slug}`** — may be Cloudflare-blocked
3. **Last resort**: `substack.com/home/post/p-{post_id}` — generic Substack internal page

## Article Body Characteristics (observed July 2026)

| Characteristic | Value |
|----------------|-------|
| isAccessibleForFree | `true` (fully public, no paywall) |
| Body length | ~12,825 characters, 49 paragraphs |
| JSON-LD metadata | Full (headline, author, date, isAccessibleForFree) |
| Curated external links | ~18 per issue |
| Author "take" blockquotes | 8+ per issue (marked as "Alex's take") |
| Page HTML size | ~246KB |

**Contrast with paywall pattern**: Earlier observations (June 2026) suggested The Signal was paywalled with only ~1,000 chars of free preview. The July 2026 issue was fully free — paywall status may vary per issue. Always check `isAccessibleForFree` in JSON-LD rather than assuming paywall status.

## Link Extraction

External curated links are embedded in the body HTML `<a>` tags within `<article>` content. They include:
- Official company blog posts (google, NYT, Yahoo Finance, Axios, thinkingmachines.ai, etc.)
- X/Twitter posts from notable figures (Demis Hassabis, Dario Amodei, David Sacks, etc.)
- Academic/think tank papers (Harvard Salata Institute, EPRI/arxiv, OPB)
- Article anchor text may be truncated because Substack uses inline word-level <span> wrapping — one link may have multiple `<a>` elements covering individual words

## Verification Procedure

When triaging a The Signal newsletter:
1. Fetch via `thesignal.substack.com/p/{slug}` using `curl -sL -A 'Mozilla/5.0'`
2. Extract JSON-LD to check `headline`, `isAccessibleForFree`, `datePublished`, `author`
3. Extract `<article>` tag for body paragraphs
4. Extract external `<a href>` links from article body for curated source list
5. Cross-reference each curated link against wiki coverage (most topics are company-blog announcements already captured by sitemap-monitor)
6. ~85-90% of curated topics are already covered — focus triage effort on the ~10-15% of genuinely new content (deals, policy analysis, unique data points)
