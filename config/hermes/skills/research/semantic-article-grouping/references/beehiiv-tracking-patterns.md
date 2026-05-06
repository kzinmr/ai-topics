# Beehiiv Tracking URL Patterns (Session Discovery)

Discovered during newsletter-triage sessions on 2026-05-03 and 2026-05-06 for Superintel+ (getsuperintel.com) newsletters by Kim "Chubby" Isenberg (@kimmonismus).

## Resolved URL Behaviors (2026-05-06 Session: "Claude Is Coming for Your Company")

| # | Resolved To | Content Type | Action |
|---|-------------|-------------|--------|
| 1 | Full article page (main newsletter post) | Article (main) | Take — this is the canonical newsletter |
| 2 | Same article page (different tracking ID) | Article (duplicate) | Skip — dedup |
| 3 | Author X/Twitter profile (@kimmonismus) | Social profile | Skip |
| 4 | **Wispr Flow** (voice dictation product, $81M raised) | Separate external article | Evaluate independently |
| 5-20 | (not resolved — sample pattern established) | Unknown | Sample-resolve to detect more distinct articles |

## Corrected Pattern: Not All Links Are Duplicates

**Correction from 2026-05-03 session**: The previous version of this reference assumed links 4+ were all "same article dedup". The 2026-05-06 session proved this is WRONG — beehiiv newsletters contain **genuinely different external articles** at different tracking URL positions. Pattern:

- **Link 1**: The main newsletter post (canonical)
- **Link 2**: Same as Link 1 (email title link, different tracking ID)
- **Link 3**: Author X/Twitter profile (`@handle`)
- **Link 4+**: Other curated articles within the newsletter (may resolve to anything — product pages, other Substack posts, news articles, etc.)

### Recommended Strategy
1. Resolve Links 1-4 to establish the pattern
2. If Link 4 resolves to a DIFFERENT article than Link 1, resolve a few more (5, 6, 7) to enumerate all distinct articles
3. Once you've identified all unique article URLs, skip the remaining tracking links
4. Typical yield: 1 main article + 1-3 additional curated articles per beehiiv newsletter

## Efficiency Comparison: Substack vs Beehiiv

| Dimension | Substack | Beehiiv |
|-----------|----------|---------|
| **Post page cost** | 1 `web_extract(post_url)` gets ALL curated links | N/A — no single post URL |
| **External article cost** | Links extracted from post body, resolved individually | Each tracking URL = 1 `web_extract` |
| **Noise ratio** | ~13/20 UI elements, 1 post body URL | ~16/20 tracking URLs, most resolve to 1-2 unique articles |
| **Efficiency** | Very high (1 call → rich post body) | Lower (3-6 calls needed to find all distinct articles) |
| **Verification** | Post body text is human-readable and link-rich | Each resolved URL must be independently assessed |

**Bottom line**: Beehiiv is the most costly newsletter format to triage. Plan for 3-6 `web_extract` calls vs Substack's 1-2.

## Key Insights

1. **Tracking URL ≠ Article URL**: A single beehiiv newsletter can have 16+ tracking URLs pointing to 1-4 unique destinations. Most are redundant tracking links for share buttons, like buttons, subscribe CTAs, etc.

2. **Auth state variation**: The same article URL with different tracking IDs can resolve to different auth states (e.g., public preview vs. login prompt vs. full article if logged in). web_extract may get different results depending on session state — treat the most content-rich result as canonical.

3. **Source identification**: The newsletter subject line (e.g., "NVIDIA Blackwell vs. Huawei Ascend") is NOT the source name — it's the article title. The actual publication (e.g., "Superintel+ / getsuperintel.com") must be extracted from the rendered page content.

4. **Beehiiv hosted pages** (`hp.beehiiv.com/<uuid>`) are dangerous: they look like they might contain newsletter content but always resolve to Terms of Use boilerplate.

## Cost: Resolving Trackers vs Post Pages

For 20 candidates, resolving 3-6 tracking URLs costs 3-6 web_extract calls. Strategy: resolve Links 1-3 first to detect the pattern (main article + possible dupe + author profile), then sample Links 4+ to find distinct articles before batch-skipping the rest.
