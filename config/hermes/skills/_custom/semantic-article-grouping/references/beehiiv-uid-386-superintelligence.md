# Beehiiv uid=386 — Superintelligence (getsuperintel.site)

## Publication Identity

| Field | Value |
|-------|-------|
| **uid** | `386` |
| **Publication name** | Superintelligence |
| **Author** | Kim "Chubby" Isenberg (@kimmonismus) |
| **Platform** | beehiiv |
| **Hosted domain** | `getsuperintel.site` (beehiiv-hosted publication page) |
| **Marketing site** | `getsuperintel.com` (Framer site, returns 404 for `/p/...` paths) |
| **Canonical article URL** | `getsuperintel.site/p/{slug}` |
| **Typical content** | Weekly deep-dive articles on AI infrastructure, GPU optimization, data layer, compute economics. Exclusive interviews with industry CTOs. |

## Distinctive Behavior vs uid=266

Superintelligence operates under **two beehiiv UIDs** with different access characteristics:

| Characteristic | uid=266 (getsuperintel.com) | uid=386 (getsuperintel.site) |
|----------------|----------------------------|------------------------------|
| Newsletter sender | Unknown (possibly deprecated) | Confirmed active (July 2026) |
| Tracking token expiry | Expires ~12-24h (403 Cloudflare challenge) | **Persists 16-24h+** (all 20 links returned HTTP 200) |
| Article content route | Via beehiiv redirect chain only | Via `getsuperintel.site/p/{slug}` directly |
| Hosted page accessibility | Cloudflare challenge on direct access | Full article body accessible via `getsuperintel.site` |

**Key insight**: uid=386 tracking tokens have a longer expiry window than uid=266. As of July 2026, all 20 tracking URLs resolved successfully ~16h after newsletter delivery (none expired, none Cloudflare-blocked).

## Link Composition Pattern (July 2026 Observation)

From a 20-link batch (2026-07-19):

| Link Range | Content Type | Count |
|------------|-------------|-------|
| Link 1-2 | Main article (interview/text + TTS variant) | 2 |
| Link 3 | Author X/Twitter profile | 1 |
| Link 4 | Sponsored ad (domain registrar) | 1 |
| Link 5 | Subscription/whitelist page | 1 |
| Link 6-7 | YouTube video (same interview, 2 variants) | 2 |
| Link 8-14 | Social media profiles (X, Instagram, Threads, YouTube, TikTok, LinkedIn x2) | 7 |
| Link 15, 19 | Advertise page (duplicate) | 2 |
| Link 16, 20 | Subscription preferences (duplicate) | 2 |
| Link 17-18 | Company social pages (LinkedIn, X) | 2 |

**Typical yield**: ~1 unique article per newsletter. Rest are social links, subscriptions, and ads. No distinct external articles from other sources.

## Author Profile Location

Unlike getsuperintel (uid=266) where the author X/Twitter profile appears at Link 2 or 3, uid=386 places it at **Link 3** consistently. The canonical bio page is at `getsuperintel.site/authors/kim-chubby-isenberg`.

## Batch Sampling Strategy

For uid=386 newsletters:
1. Resolve Link 1 (main article — always the interview/feature)
2. Resolve Link 3 (author profile — skip)
3. If Link 1 returns full body, stop sampling — all remaining links are social/subscribe/ad/duplicate
4. Validate with Link 4 (sponsored ad) and Links 6-7 (YouTube duplicates) as spot-checks

## Triage Routing

- The main article is usually an **exclusive interview** with deep technical content on AI infrastructure
- Article body is ~10,000+ chars with substantive technical claims (model specs, benchmark numbers, architecture details)
- Author entity page `entities/kim-isenberg.md` exists (May 2026) — update `updated` date and add new articles to `Key Writings` section
- For company interview articles (VAST Data, NVIDIA, etc.): create/update the company entity page, not the author page
- Social profile links can be batch-skipped without resolution
- **No distinct external articles** — the newsletter curates only its own exclusive content
