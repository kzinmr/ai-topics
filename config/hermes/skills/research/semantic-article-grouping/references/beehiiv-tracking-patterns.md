# Beehiiv Tracking URL Patterns (Session Discovery)

Discovered during newsletter-triage sessions on 2026-05-03, 2026-05-06, and 2026-05-07 for Superintel+ (getsuperintel.com) newsletters by Kim "Chubby" Isenberg (@kimmonismus).

## Resolved URL Behaviors (2026-05-06 Session: "Claude Is Coming for Your Company")

| # | Resolved To | Content Type | Action |
|---|-------------|-------------|--------|
| 1 | Full article page (main newsletter post) | Article (main) | Take — this is the canonical newsletter |
| 2 | Same article page (different tracking ID) | Article (duplicate) | Skip — dedup |
| 3 | Author X/Twitter profile (@kimmonismus) | Social profile | Skip |
| 4 | **Wispr Flow** (voice dictation product, $81M raised) | Separate external article | Evaluate independently |
| 5-20 | (not resolved — sample pattern established) | Unknown | Sample-resolve to detect more distinct articles |

## Resolved URL Behaviors (2026-05-07 Session: "GPT-5.5 Instant: Less Fluff, More Facts")

| # | Resolved To | Content Type | Action |
|---|-------------|-------------|--------|
| 1 | GPT-5.5 Instant article (getsuperintel.com) | Article (main) | Take — returned `http_error` on 1st attempt, succeeded on retry |
| 2 | `http_error` (never resolved) | Dead/auth link | Skip — possibly Link 1 duplicate that expired |
| 3 | @kimmonismus X profile | Social profile | Skip |
| 4 | **Wispr Flow** (voice dictation) | External product | Skip |
| 5 | WSJ: Google/MS/xAI share models with U.S. | News article (paywalled preview) | Reference |
| 6 | Anthropic Financial Services page | Platform product page | Reference |
| 7 | FT: Meta plans agentic AI assistant (paywalled) | News article (fully paywalled) | Skip |
| 8 | Chamath Stanford AI Club talk (YouTube) | Video/talk | Reference |
| 9 | Same as 8 (Chamath talk, different tracking ID) | Duplicate | Skip — dedup |
| 10 | Ming-Chi Kuo X post: OpenAI AI agent phone 2027 | X post | Reference |
| 11 | Same as 8 (Chamath talk, 3rd tracking ID) | Duplicate | Skip — dedup |
| 12 | **Wispr Flow** (duplicate of Link 4) | Duplicate | Skip — dedup |
| 13 | **Wispr Flow** (duplicate of Link 4) | Duplicate | Skip — dedup |
| 14 | **FrontierSWE Benchmark** (GitHub) | Benchmark page | **TAKE** |
| 15 | **Workspace-Bench 1.0** (GitHub) | Benchmark page | **TAKE** |
| 16 | Harmonic Security (Claude governance product) | Product LP | Skip |
| 17 | Same as 16 (Harmonic Security) | Duplicate | Skip |
| 18 | getsuperintel.com account/referrals page | Account page | Skip |
| 19 | getsuperintel.com account/referrals page (dup) | Account page | Skip |
| 20 | getsuperintel.site/subscribe | Subscribe page | Skip |

### Key Observations from 2026-05-07
- **Main article at Link 1 failed first try**: The `http_error` was transient — retry succeeded. Beehiiv tracking tokens may expire or be rate-limited.
- **Deduplication density**: 3 different tracking IDs for Wispr Flow (Links 4, 12, 13), 3 for Chamath talk (Links 8, 9, 11), 2 for Harmonic Security (Links 16, 17). ~37% of links were duplicates.
- **New article type discovered**: GitHub benchmark repositories (FrontierSWE, Workspace-Bench) resolved from beehiiv links — previously only saw product pages and news articles.
- **Source diversity**: Of 19 links, only 5 unique content destinations were wiki-worthy (main article, WSJ, Chamath talk, FrontierSWE, Workspace-Bench). The rest were duplicates, social profiles, product LPs, or account pages.

## Corrected Pattern: Not All Links Are Duplicates

**Correction from 2026-05-03 session**: The previous version of this reference assumed links 4+ were all "same article dedup". The 2026-05-06 session proved this is WRONG — beehiiv newsletters contain **genuinely different external articles** at different tracking URL positions. Pattern:

- **Link 1**: The main newsletter post (canonical)
- **Link 2**: Same as Link 1 (email title link, different tracking ID)
- **Link 3**: Author X/Twitter profile (`@handle`)
- **Link 4+**: Other curated articles within the newsletter (may resolve to anything — product pages, other Substack posts, news articles, etc.)

### Recommended Strategy
1. Resolve Link 1 — if `http_error`, **retry once** (transient auth failures are common). If still error, assume it's the main article behind auth and reconstruct from the newsletter subject/`source_name`.
2. Resolve Link 3 to detect author X profile (skip)
3. Sample Links 4-7 to establish the distinct-article pattern
4. If a sample resolves to a new distinct article type (benchmark, news, video, GitHub), continue sampling until you've found all significant targets
5. Once you confirm the pattern (e.g., "link 4 = product, link 5 = news, link 6 = Anthropic page..."), approximate the rest — don't resolve every remaining link
6. **Catch duplicates aggressively**: if the same title/content appears again, skip immediately. Expect ~30-37% duplicate rate
7. Typical yield: 1 main article + 3-5 distinct external articles per beehiiv newsletter of 19-20 links

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
