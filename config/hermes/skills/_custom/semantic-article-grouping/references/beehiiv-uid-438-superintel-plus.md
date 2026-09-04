# Beehiiv uid=438 — Superintel+ (getsuperintel.site, Kim "Chubby" Isenberg)

Validated July 30-31, 2026 during newsletter-triage run 20260731T102556Z.

## Identification
- Raw newsletter frontmatter `source_label: "uid=438"` (source unknown from the email itself)
- Publication: **Superintel+** on getsuperintel.site (beehiiv-hosted), author **Kim "Chubby" Isenberg**
- Canonical bio: getsuperintel.site/authors/kim-chubby-isenberg; author X: @getsuperintel
- Format: ~1 unique exclusive editorial article per issue (e.g., "🔁 GPT-5.6 Just Made Itself 15% More Efficient" = OpenAI serving self-optimization report: Sol rewrote own GPU kernels → 20% lower serving costs; redesigned own draft model → 15%+ token generation efficiency), plus a "In Today's Issue" TOC of curated links

## Token persistence vs other uids
| uid | Behavior |
|-----|----------|
| 266 | 403 after ~12-24h (expired tracking token) |
| 383 | The Stage and the Factory Floor (Manu Sharma) |
| 386 | Superintelligence — tokens persist 16-24h+, all links HTTP 200, ~1 unique article/issue |
| **438** | **Tokens persist 17h+ (tested: sent Jul 30 17:32 UTC, resolved full article Jul 31 10:25 UTC). Do NOT assume expired.** |

## ⚠️ Cloudflare challenge is per-LINK, not per-NEWSLETTER (corrects the kill-switch rule)
- Link 1 of the tracking batch → HTTP 200, title "Just a moment..." (Cloudflare challenge)
- Link 2 (same newsletter, same day) → **full 810KB article HTML** with JSON-LD `isAccessibleForFree: true`, 66+ `<p>` paragraphs
- The main exclusive article was at Link 2, not Link 1. Different tracking URLs route through different destinations/CDN states.
- Action: when Link 1 challenges, still sample Link 2 (and Link 3 if needed) before concluding the newsletter is unreachable. Only when links 1-3 ALL return the challenge, fall back to subject-line-only assessment.
- Other batch links: sponsor (goldcast webinar, gladly.ai demo), SNS follow links (x.com/getsuperintel, LinkedIn, Instagram, TikTok, YouTube), subscribe forms, and the author bio page — same ~30-40% noise rate as other getsuperintel newsletters.

## open.substack.com empty-redirect signal (?triedRedirect=true) — applies to ALL substack pubs
When `open.substack.com/pub/{handle}/p/{slug}` returns ~1.3KB of HTML whose `<title>` is the URL itself with `?triedRedirect=true` appended (no article content, no JSON-LD), the open-domain redirect bounced — this is NOT a Cloudflare challenge. Retry with the publication's custom subdomain: `{handle}.substack.com/p/{slug}`.
- Validated Jul 2026: `bensbites.substack.com/p/1-billion-chatgpt-users` (Ben's Bites) and `aiweekly.substack.com/p/true-positive-weekly-171` (AI Weekly / Andriy Burkov) both required this retry.
- The JSON-LD `url` field inside the resolved page confirms the canonical domain (e.g., `https://www.bensbites.com/p/...`).

## Cross-newsletter dedup note
Superintel+ content overlaps heavily with AINews same-day bulletins (both covered the GPT-5.6 price cuts + Sol self-optimization on Jul 30-31). The beehiiv version is the exclusive/interview source; rate as reference when AINews already took the topic. Unique OpenAI business facts from this issue (useful for `entities/openai.md` reference enrichment):
- OpenAI July ARR topped all of Q2 (CNBC, Jul 29)
- 100,000 academic researchers get free frontier access (openai.com/index/chatgpt-for-academic-researchers/)
- Altman briefed US senators on the rogue-agent incident (Reuters, Jul 29)
- InSilico's rentosertib (first AI-designed drug) reached Phase III
