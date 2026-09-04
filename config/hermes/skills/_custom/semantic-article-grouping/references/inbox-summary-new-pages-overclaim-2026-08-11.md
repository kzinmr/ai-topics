# Inbox Summary `new_pages_to_create` Overclaim (2026-08-11)

## Pattern

The inbox pre-triage summary's `new_pages_to_create` array is generated **without filesystem awareness** — it cannot see `wiki/entities/`, `wiki/events/`, or `wiki/log.md`. It regularly suggests creating pages that **already exist**, so its new-page suggestions must never be taken at face value.

This is distinct from `inbox-summary-coverage-overrate-pattern.md` (inbox overrates coverage *gap* of a correctly-identified topic). Here the inbox invents *new pages* that are already on disk.

## Concrete case (2026-08-11, 5-newsletter batch)

Inbox summary suggested 3 new pages:

| Suggested page | Reality | Triage result |
|---|---|---|
| `concepts/posttrainbench.md` | Genuinely absent | Valid take signal (PostTrainBench+ from Intology, 51.6% vs human baseline with 4000+ H100 hours) |
| `events/meta-muse-glimmer-spark-release.md` | WRONG — `entities/muse-glimmer.md` + `entities/muse-spark.md` already existed (created 2026-08-10 by sitemap/raw pipeline from research.meta.ai) | Cross-pipeline dedup → skip (AINews coverage added nothing beyond Artificial Analysis index detail) |
| `entities/vercel-eve.md` | WRONG — already existed since 2026-06-28 (also `entities/eve-legal-ai.md` exists for the legal-tech Eve) | Downgraded to reference (Merge Mommy case study) |

Result: **2/3 suggested "new pages" already existed.** The take decision on Muse Glimmer was correctly avoided by checking log.md first (grep for 2026-08-10 showed muse-glimmer/muse-spark entity creation).

## Rule

Before elevating any inbox-suggested `new_pages_to_create` item to a take:
1. `ls entities/` + `ls events/` + `ls concepts/` for the slug (true filename lookup, not `search_files` regex)
2. `grep "$(date +%F)" wiki/log.md` for recent creates by other pipelines (sitemap-monitor 06:00, raw-backlog 0/4/8/12/16/20, dreaming 18:00)
3. If the page exists → decide dedup/skip or reference-level enrichment. The inbox suggestion itself is evidence the topic matters, but **not** evidence of a coverage gap.

## Companion observations (same batch)

- **Beehiiv `/v2/c/` tracking path**: Superintel+ (uid=443) "The Model OpenAI Won't Release" used `link.mail.beehiiv.com/v2/c/...` (not v1) and resolved **200 at ~20h old** (previous-day token still valid). Same test-one-link-verdict logic as v1 — the path version doesn't matter, the expiry window does. This batch confirmed the "200 → resolvable, trust the verdict" side (see `newsletter-triage-2026-08-07-patterns.md` / `-2026-08-09-patterns.md`).
- **Substack redirect-stub → canonical re-fetch worked for 4 pubs at once**: `open.substack.com/pub/{pub}/p/{slug}` returned the ~1.3KB `?triedRedirect=true` stub for importai / swyx (latent.space) / robotic (interconnects.ai) / lenny (lennysnewsletter.com). Re-fetching the canonical domain (from `<title>`) returned full bodies with JSON-LD. See `references/substack-redirect-stub-title-discovery.md`.
- **Lenny's "How I AI" podcast section yields reference-grade body content**: post page had 77 substantive `<p>` paragraphs despite being a pure-podcast publication. Merge Mommy (Vercel Eve PR-review bot, 6-dimension risk model, Intercom 5x faster, SOC 2 + auto-approval) → vercel-eve.md reference; Grace Clarke (3 Claude skills, intent engineering, voice guide, Gmail rebuild) → claude-code.md reference. Confirms the pure-podcast counter-nuance: read the body before skipping.
- **Entity-consumed-newsletter dedup (RLHF book)**: Interconnects "5 useful things you'll learn in my post-training textbook" was already fully captured in `entities/nathan-lambert.md` (RLHF Book section, "RLHF Book Completed", rlhfbook.com, Manning, chapter list). The newsletter was a promo/shipping announcement → reference (status bump: shipping now, 50% off until Aug 19) at most, not take.
- **Yield**: 5 newsletters → 3 takes / 11 refs / 10 skips. Inbox rated 2 critical + 3 high; actual takes: OpenAI Astra Critical cyber grading (Superintel+ — first model treated as "Critical" in Preparedness Framework, `entities/openai-astra.md` gap since that page covered only the math story), IFP 23 RSI ideas + PostTrainBench+ (Import AI 468), GPT-5.6-Cyber restricted release (AINews, `entities/openai.md` Daybreak section covered GPT-5.5-Cyber only).
