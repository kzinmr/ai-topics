# Newsletter Triage Patterns — 2026-10-21 Batch (run 20261021T101030Z)

6 newsletters / 120 candidates → 12 decisions (3 take, 3 reference, 6 batch-skip). Validated techniques below.

## 1. Custom-domain curl-first batch resolution (fastest path for Substack pubs)

When checkpoint candidates reveal the publication handle from `open.substack.com/pub/{handle}/p/{slug}` links, SKIP the open.substack.com redirect chain entirely and curl the custom domain directly with a desktop UA. All 4 Substack pubs resolved on first attempt with full `<article>` bodies:

| Publication | Working URL | Body |
|---|---|---|
| AINews (swyx, pub 1084089) | `https://www.latent.space/p/ainews-deepseek-deepinfer-open-source` | 159 paras |
| Latent Space podcast | `https://www.latent.space/p/sfcompute2` | 83 paras |
| Latent Space podcast | `https://www.latent.space/p/tenex` | 96 paras |
| Ben's Bites (pub 4379299) | `https://www.bensbites.com/p/how-i-built-my-everything-app` | 27 paras |

Podcast episodes (play_card links) are NOT auto-skippable here — both Latent Space episodes had 80-96 standalone paragraphs. The single-script pattern (write /tmp script with fetch+`<article>`+`<p>` extraction + link filtering, one terminal run) resolved 4 pubs in one call.

## 2. robotic pub 48206 → Interconnects canonical chain

`open.substack.com/pub/robotic/p/latest-open-artifacts-25-deepseek` returns the body (200KB), and its canonical link + extracted external links reveal the real home is `www.interconnects.ai/p/latest-open-artifacts-25-deepseek` (Nathan Lambert / Xeophon). `roboticwaves.com` / `roboticwaves.ai` variants return EMPTY (len 0) — do not try them. Confirms the existing "pub 48206 robotic=Interconnects" note: the checkpoint's `source_name` and robotic subdomain are aliases; author entity pages and `sources:` refs should use Interconnects.

## 3. Beehiiv batch Cloudflare verdict — links 1,2,3 all "Just a moment..." (7KB, 7003 bytes)

The Altman's Three Endgames newsletter (uid=820, `link.mail.beehiiv.com/v2/c/...`, ~15h old) hit the per-LINK kill switch hard: sampled links 1, 2, 3 all returned identical 7,003-byte Cloudflare challenge pages. That is the "all links 1-3 fail → assess at topic level" branch. Inbox summary said importance=high with suggested target `entities/sam-altman.md` — but BODY-READING MANDATE held: no take on unreadable body, downgraded to reference with the inbox metadata quoted in `body_excerpt` (documented as unreadable + reason). Note the inbox-overrate sub-pattern: sam-altman.md (282 lines) may already cover the endgames framing, and the topic (Altman AGI strategy) overlaps existing `concepts/superintelligence.md`.

## 4. log.md "Noted, not ingested" = pre-registered take for the next run

Oct 20 trending-topics entry ended with: "Noted, not ingested: DeepSeek DHS federal-civilian ban (320p, ... candidate for deepseek entity update next run). Reuters 401-blocked; classified from HN/Reuters headline only." The Oct 20 Latest open artifacts #25 newsletter carried the FULL DHS order + MOFCOM pre-approval proposal + Federal Register PDF link (public-inspection.federalregister.gov/2026-21447.pdf) — grep confirmed `concepts/open-weight-ai-regulation.md` and `concepts/ai-regulation-2026.md` had ZERO hits for DHS/MOFCOM. This closed a gap another pipeline had explicitly deferred. Lesson: grep log.md for "noted, not ingested" / "deferred" / "401-blocked" — a later newsletter carrying the same event is a strong take signal, not a duplicate to skip.

## 5. Inbox critical ≠ take — same-day upstream concept creation (DeepInfer)

Inbox rated AINews DeepInfer "critical" and suggested `events/ (new event)`. Cross-check found active-crawl (same day, earlier) had already created `concepts/deepinfer.md` (60 lines, Apache-2.0/kernels/Ascend 950/closed-KV-cache all covered). Downgraded to reference: only the AINews-specific ECONOMICS numbers (155T tok/day/cluster, $38/SM100 card-hr, $5-8 all-in → >80% margin, ~$166B/GW, 81-day payback, 96% cache hit) constitute a real gap → existing-page append, no new event page. The inbox cannot see same-day wiki writes; always check `log.md` + `ls -lt concepts/ events/` for today's creations before accepting the inbox's suggested_wiki_targets.

## 6. Dedup-by-known-event

DeepSeek V4.1 Flash 1017 appeared in BOTH #25 (open artifacts) and AINews subject lines; `events/2026-10-17-deepseek-v4.1-flash-1017-release.md` already existed (and had been registered in index by watchdog). The take for #25 was scoped to the regulatory + model-list delta only, with explicit "do not duplicate the 1017 event page" note in reason_ja. Model-release dedup across multiple newsletters in one batch: check events/ once, scope each decision to its unique delta.
