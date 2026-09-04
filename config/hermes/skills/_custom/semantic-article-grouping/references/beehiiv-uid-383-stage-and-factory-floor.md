# Beehiiv uid=383 — "The Stage and the Factory Floor" (Manu Sharma)

## Publication Identity

| Field | Value |
|-------|-------|
| **uid** | `383` |
| **Publication name** | The Stage and the Factory Floor |
| **Author** | Manu Sharma |
| **Platform** | beehiiv |
| **Subscribers** | ~7K+ |
| **Issues published** | ~139 (as of July 2026) |
| **Theme** | AI capability vs trust gap — AI agents, LLMs, AI-assisted tools |
| **Hosted page** | `the-stage-and-the-factory-floor.beehiiv.com/` — Cloudflare protected (403) |
| **Beehiiv platform URL** | `www.beehiiv.com/p/the-stage-and-the-factory-floor` — Cloudflare protected (403) |

## Observed Access Behavior (2026-07-19)

- **Tracking URLs**: All 20 beehiiv tracking URLs returned **HTTP 403** (expired tracking token pattern)
  - curl confirms: token expired ~12-24h after newsletter delivery
  - No redirect chain — stays at `link.mail.beehiiv.com/v1/c/...`
  - Body: minimal (not Cloudflare "Just a moment...")
- **Hosted subdomain**: `the-stage-and-the-factory-floor.beehiiv.com/` returns 403 (Cloudflare)
- **Beehiiv platform page**: `www.beehiiv.com/p/the-stage-and-the-factory-floor` returns Cloudflare challenge
- **Inbox pre-triage summary**: Correctly identified as priority=low with all links unresolvable
- **Content verdict**: Entirely inaccessible via automated tools. No article content could be retrieved.

## Triage Routing for Future Sessions

When encountered in newsletter triage:

1. All 20 candidates are beehiiv tracking URLs — expect all to return 403 (expired token)
2. The inbox pre-triage summary should already flag the publication as `importance: low` with all links unresolvable
3. The publication URL formats that *might* work (if not Cloudflare-protected):
   - `the-stage-and-the-factory-floor.beehiiv.com` — currently blocked
   - `www.beehiiv.com/p/the-stage-and-the-factory-floor` — currently blocked
4. If content is completely inaccessible: skip all items, using the inbox summary's topic assessment
5. The publication's theme (AI capability vs trust gap) is tangentially relevant to the wiki — it's not a deep technical source but covers the societal/trust dimension
6. Existing wiki coverage: `concepts/dr-manhattan-syndrome-ai.md` already covers the AI trust gap comprehensively

## Future Monitoring

If this publication becomes accessible (e.g., Cloudflare protection removed or newsletter migrates to another platform), re-evaluate its value for:
- An entity page for Manu Sharma (if content quality warrants)
- Concept pages covering the AI trust/capability gap from a practitioner perspective
