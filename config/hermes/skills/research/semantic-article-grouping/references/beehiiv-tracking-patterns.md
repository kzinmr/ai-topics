# Beehiiv Tracking URL Patterns (Session Discovery)

Discovered during newsletter-triage on 2026-05-03 for the "NVIDIA Blackwell vs. Huawei Ascend" newsletter (Superintel+ / getsuperintel.com).

## Resolved URL Behaviors

| # | Input Pattern | Resolved To | Content Type |
|---|---|---|---|
| 1 | `link.mail.beehiiv.com/v1/c/...` (long base64-encoded payload) | Full article page (preview behind paywall) | Article content |
| 2 | `link.mail.beehiiv.com/v1/c/...` (different tracking ID) | Same article with login interstitial | Article content (different auth state) |
| 3 | `link.mail.beehiiv.com/v1/c/...` (third tracking ID) | Author X/Twitter profile (`@kimmonismus`) | Social profile |
| 4-14 | `link.mail.beehiiv.com/v1/c/...` (more tracking IDs) | Same article / UI element | Noise (same article dedup) |
| 15 | `hp.beehiiv.com/<uuid>` | beehiiv Terms of Service | Boilerplate — skip |
| 16 | `email.beehiivstatus.com/<hash>/hclick` | Tracking pixel (0-content) | Pixel — skip |

## Key Insights

1. **Tracking URL ≠ Article URL**: A single beehiiv newsletter can have 16+ tracking URLs pointing to only 1-2 unique destinations. Most are redundant tracking links for share buttons, like buttons, subscribe CTAs, etc.

2. **Auth state variation**: The same article URL with different tracking IDs can resolve to different auth states (e.g., public preview vs. login prompt vs. full article if logged in). web_extract may get different results depending on session state — treat the most content-rich result as canonical.

3. **Source identification**: The newsletter subject line (e.g., "NVIDIA Blackwell vs. Huawei Ascend") is NOT the source name — it's the article title. The actual publication ("Superintel+ / getsuperintel.com") must be extracted from the rendered page content.

4. **Beehiiv hosted pages** (`hp.beehiiv.com/<uuid>`) are dangerous: they look like they might contain newsletter content but always resolve to Terms of Use boilerplate.

## Cost: Resolving 1 Tracking URL = 1 web_extract Call

For 16 candidates, resolving even 3-4 tracking URLs (to detect patterns) costs 3-4 web_extract calls. Strategy: resolve only enough to identify the unique article(s), then batch-skip the rest.
