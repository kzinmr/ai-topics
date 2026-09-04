# Newsletter Triage 2026-08-12 Patterns

Run: 20260812T102618Z — 5 newsletters (AINews bulletin, Ben's Bites, Superintel+ beehiiv, Latent Space Chai Discovery podcast, Lenny's Newsletter). Yield: 3 take / 7 reference / 6 skip (16 decisions).

## Manual same-day ingest dedup — bulletin main story already concept-paged (CRITICAL)

AINews bulletin "[AINews] How to steal a Reasoning Trace" (2026-08-12) covered the "Stealing Reasoning Traces from Proprietary LLM APIs" paper (Panfilov et al.) — the SAME paper a user-requested manual ingest had already processed earlier the same morning:

- log.md entry: `## [2026-08-12] Manual: Stealing Reasoning Traces paper — raw article + concept page` created `concepts/reasoning-trace-extraction-vulnerability.md` + `raw/articles/2026-08-11-stealing-reasoning-traces-from-proprietary-llm-apis.md` (from viral X post + stolen-thoughts.com).
- The concept page already carried the specific finding (182 credentials = 62 API keys, 33 emails, 33 passwords) — the bulletin's recap added ZERO new info → skip.

Detection: when grep'ing log.md for same-day entries, match `Manual:` entries too, not just pipeline names. A manual (user-requested) ingest frequently covers the same paper/tweet a daily bulletin will recap. Verify the manual page's body actually has the specific claims before skipping — fresh manual pages are usually complete (this is the inverse of the stale-`sources` nuance: `sources` listed ≠ content captured applies to OLD pages; same-day manual pages are typically exhaustive).

## Superintel+ beehiiv batch — one-link 200 verdict + multi-decision editorial yield

"Meta's Big Open Source Comeback" (getsuperintel.com Superintel+, sent 2026-08-11 15:52 UTC, triaged ~18.5h later) — all 20 links are `link.mail.beehiiv.com/v2/c/...`:

- Test Link 1 → HTTP 200, full 804KB HTML, 57 `<article>` paragraphs, JSON-LD `isAccessibleForFree: true`. Batch resolvable — resolve normally. Confirms the v2/c/ pattern from `newsletter-wiki-ingest-2026-08-11-patterns.md`; add this uid to the 200-verdict list alongside uid=443/470/480.
- **Multi-decision yield**: a rich editorial roundup article is NOT one decision. Each major section maps to a distinct wiki page and gets its own take/reference:
  - Daybreak Blue/Red restructure + GPT-5.6-Cyber → take, `concepts/openai-daybreak.md` (page had GPT-5.5-Cyber only)
  - Unitree STAR Market IPO ~$9B → take, `entities/unitree-robotics.md` (page had no IPO)
  - Muse Glimmer benchmarks (MCP Atlas 75.5, SWE-Bench Pro 51.2, Openness Index 5.0→8.0, Apache 2.0 vs Llama Community License differences) → reference, `entities/muse-glimmer.md`
  - OpenClaw gym-booking authz hack → reference, `concepts/openclaw-ecosystem.md` (agent-safety incident: "The API has zero authorisation checks on cancelling other people's reservations"; "Nobody wrote an exploit. An errand found one.")
  - Claude Riemann zeta 41.6%→67.2% → reference, `entities/anthropic.md` (page has the section but no concrete numbers)
  - LTX-2.5 open-weights video model → reference, `concepts/ai-video-generation-2026.md` (page lacks LTX)
  - NY data-center 1-year moratorium (Hochul, 100+ local) → reference, `concepts/ai-energy.md`
  - Sonnet 5 permanent pricing → skip (already in `concepts/claude/sonnet-5.md`, sourced from AINews 2026-08-11)

Section-level triage test that worked: does the target page contain the SPECIFIC number/claim from the article's section? Page exists ≠ section data captured. Muse Glimmer page exists but lacks benchmark numbers → reference. Sonnet 5 page has the exact pricing → skip.

## Lenny's Newsletter paid non-AI — confirmed skip

"How to make people care about your startup" (Lenny's, pub 10845) — `isAccessibleForFree: false`, 101 paragraphs of founder-comms/marketing content; AI appears only as "soulless AI slop" context. Non-AI → skip (inbox summary agreed: low). No need to resolve the redirect UUID links.

## Latent Space podcast article with free full body → new entity take

"The BioAI Phase Shift" (Chai Discovery, pub 1084089) — podcast email (all play_card UI links) but post page has 24 substantive paragraphs, `isAccessibleForFree: true` → standalone article. No `entities/chai-discovery.md` → ★★★★★ new-entity take ($400M Series C, Eli Lilly/Novartis/argenx deals, structural→binding model shift, Biobucks 2-5% upfront). Confirms the podcast-substantive-body nuance; audio UI links batch-skipped.

## Redirect-stub title discovery re-validated

All 4 substack posts (latent.space ×2, bensbites.com, lennysnewsletter.com) returned the ~1.3KB `?triedRedirect=true` stub; canonical-domain re-fetch via the `<title>` worked for all 4. Consistent with `references/substack-redirect-stub-title-discovery.md`.
