# Newsletter Triage Patterns — 2026-08-16

Run: `20260816T102116Z` — 2 newsletters (Latent Space Flue-2 interview uid=508; beehiiv uid=509). Validated patterns below.

## uid=509 = Superintel+ (beehiiv v2/c/ → read.getsuperintel.com)

Third confirmed Superintel+ uid (after uid=443, uid=505). Subject "Nobody Built a Bigger Model" was a GLM-5.3 post-training deepdive on `read.getsuperintel.com/p/nobody-built-a-bigger-model`.

Sampling verdict (all resolved HTTP 200, ~17h after send):
- **Link 1** → main article (`read.getsuperintel.com/p/nobody-built-a-bigger-model`)
- **Link 2** → duplicate of the same article (different tracking token)
- **Link 3** → author X profile @kimmonismus (Chubby Isenberg) → skip
- Remaining links 4-17 assumed footer/social/duplicates → batch skip
- Link 18 `hp.beehiiv.com/<uuid>` → hosted page boilerplate → skip
- Link 19 `email.beehiivstatus.com/<hash>/hclick` → status pixel → skip

Yield: 1 unique article + author profile per newsletter (consistent with uid=386/443/505 Superintel+ format). Article body was partially paywalled ("Subscribe to Superintel+ to read the rest") but the free preview contained concrete claims (Terminal-Bench 3.0 4.6→28.3, same 743B base as GLM-5.2, "post-training is the main event", "capability is now manufactured, one domain at a time", "one company admitted post-training compute exceeded pre-training compute").

## ⚠️ Inbox summary FALSE Cloudflare-blocked claim (new variant of inbox-summary-false-403-claim.md)

Inbox pre-triage for uid=509 said: *"Title indicates analysis of LLM scaling trends... Source newsletter unidentified (beehiiv, Cloudflare-blocked URLs prevent resolution)"* and classified publication as "unknown beehiiv newsletter".

**This was wrong on both counts.** All sampled v2/c/ links resolved HTTP 200 to `read.getsuperintel.com` — no Cloudflare challenge, no 403. The publication was Superintel+ (identifiable by final URL domain).

Lesson: **an inbox "Cloudflare-blocked / cannot resolve / unknown publication" claim is an estimate, not a verdict.** Test ONE v2/c/ link before accepting the blocked classification. If it resolves 200, the whole batch is likely resolvable (matches the existing "test one link, trust the verdict" rule for 403-expiry, but here the inbox mislabeled resolvable links as blocked). Always attempt resolution when the inbox says blocked — the failure mode costs one curl call.

## ⚠️ Inbox summary `new_pages_needed` can be STALE — verify existence first

Inbox for uid=508 (Latent Space Flue-2) listed `new_pages_needed: ["entities/fred-schott.md — Astro creator, Flue creator"]`. But `entities/fred-schott.md` **already existed** (created 2026-05-10, via the X-account skeleton builder). Correct action was **enrichment of the existing page** (Flue 2 hooks/meta-harness details), not creation.

Similarly `existing_wiki_pages` listed only `entities/flue.md` — correct, but the inbox missed fred-schott.md entirely.

Lesson: **never trust inbox `new_pages_needed`/`existing_wiki_pages` as ground truth** — run `ls entities/<slug>.md` (or grep index.md) for each candidate before deciding take-as-create vs take-as-enrich. Stylized filenames (e.g. `entities/fred-schott.md` for Fred K. Schott) are a common false-negative source for summary generators.

## Take-as-existing-page-update (dual-entity enrichment)

Flue-2 article → **take (★★★★☆)** with `candidate_wiki_path: entities/flue.md` + secondary enrichment of `entities/fred-schott.md`. Both pages existed with v1-only content (flue.md created 2026-05-06, fred-schott.md 2026-05-10) and both needed v2 update. The triage JSON can only carry one `candidate_wiki_path` — note the secondary target in `reason_ja` so downstream enrichment covers both.

Body-read confirmation: the Latent Space post page (`www.latent.space/p/flue-2`) is `isAccessibleForFree: true`, JSON-LD present but `body_html: ""` → fell back to `<article>`/`<p>` extraction (42 substantive paragraphs). Standard Substack pattern.
