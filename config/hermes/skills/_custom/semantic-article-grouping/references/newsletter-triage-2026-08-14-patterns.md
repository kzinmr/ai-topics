# Newsletter Triage 2026-08-14 Patterns

Run: 20260814T102346Z — 3 newsletters (Ben's Bites, True Positive Weekly #173, Superintel+ beehiiv), 60 candidates → 19 decisions (1 take / 8 references / 10 skips).

## Same-event dual-source → take-as-update (primary lesson)

- `events/grok-4-6-launch.md` was created 2026-08-13 from the AINews newsletter (newsletter-wiki-ingest). The SAME event arrived again the next morning via Superintel+ beehiiv "xAI's Grok 4.6 Released: Frontier Intelligence At Insane Pricing".
- Inbox summary classified it "critical" and recommended creating `events/grok-4-6-release` — but the page already existed. The inbox cannot see existing page depth; the discriminator is the page's SPECIFIC claims.
- Verdict: TAKE as existing-page update (★★★★☆), NOT skip, because Superintel+ carried concrete numeric facts the AINews-sourced page lacked:
  - API pricing: **$2/M input, $6/M output** (event page only said "materially below frontier peers")
  - AA Intelligence Index 61, exactly level with GPT-5.6 Sol, 2 points off Claude Opus 5
  - **AA-Briefcase Elo 1577** (2nd, behind Opus 5's 1715, ahead of Fable 5's 1574, clear of Sol's 1502)
  - **Cursor codebase snapshot accidentally included in training → CursorBench being rebuilt** (absent entirely)
- Rule: when a second newsletter covers an event whose page exists, READ the page's numbers first. Page fresh ≠ page complete. Specialized source (Superintel+) tends to add pricing/benchmark/incident detail the bulletin (AINews) summarized qualitatively.

## Superintel+ uid=443: v2/c/ links resolved 200 at ~15h old

- All 20 tracking links returned HTTP 200 (sent Aug 13 19:11 UTC, resolved Aug 14 10:23 UTC ≈ 15h). Reinforces the "previous-day links CAN resolve 200 (uid=443 Superintel+)" counter-case — test one link, trust the verdict, not age.
- Link 1 + Link 2 both resolved to the SAME full 824KB article (duplicate density ~30% confirmed). Link 3 = author X profile (@kimmonismus, Kim 'Chubby' Isenberg) → skip per @handle rule. Remaining 17 links treated as share/like/referral duplicates → batch skip.
- Canonical: `read.getsuperintel.com/p/{slug}` (article content domain, uid=443). Do NOT attempt direct getsuperintel.com (Framer marketing 404).

## Redirect-stub title discovery: Ben's Bites canonical = www.bensbites.com

- `open.substack.com/pub/bensbites/p/grok-bot-is-not-what-you-think` → ~1.3KB stub, `<title>` = `https://www.bensbites.com/p/grok-bot-is-not-what-you-think?triedRedirect=true`. Canonical fetch returned 198KB full article: JSON-LD headline "Grok Bot is not what you think", isFree=true, 32 article paragraphs.
- Same pattern for `aiweekly.substack.com/p/true-positive-weekly-173` (canonical directly on aiweekly.substack.com).
- Note: bensbites canonical uses `www.` prefix; open.substack.com pub handle is `bensbites`.

## TPW #173 (pub 61455, Burkov) — pure link digest reconfirmed

- Inbox summary classified "high" and suggested "Review and ingest curated articles". Body check: 10 paragraphs, shallow bullet list, no editorial analysis → pure link digest → skip. Reconfirms inbox-summary-link-digest-trap (`references/inbox-summary-link-digest-trap.md`).
- Digest items (Claude watermark Ars, font anti-scraper Ars, AI agent legal responsibility Guardian, Erdős Quanta, WASTE Kimi K3 2.78T on 29GB RAM, Qwen3.8-Max) all either already covered (Qwen3.8-Max in `concepts/qwen-3-8.md` + raw article 2026-08-03) or 1-line mentions without analysis.

## Ben's Bites curated-link yield (post body extraction → references)

- Main article (Grok Bot hands-on: personify agents with system prompts, agent-to-agent messaging, watchable virtual computers, $200 plan requirement) → reference for `events/grok-4-6-launch.md` Grok Bot section.
- Curated links yielded 4 references: SSI small reasoning engine (→ `entities/ilya-sutskever.md`, stale since 2026-05), ChatGPT import from Claude Code (→ `concepts/session-portability.md`, grep confirmed absent), Vercel agent factory 35% PRs (→ `entities/vercel.md`), seangoedecke "how-to-keep-thinking" (→ `entities/seangoedecke-com.md`).
- Low-value links (Claude WiFi anecdote 200→810 Mbps, Pangram detection avoidance, "everything hackable" essay, arc-code) → batch skip. No individual URL resolution needed — curated links live in the post body.

## Inbox summary recommended_wiki_updates slug drift

- Inbox summary recommended `events/grok-4-6-release`; actual page slug on disk is `events/grok-4-6-launch.md`. Use the summary for priority ordering and publication identification, but verify the actual slug via find before trusting candidate_wiki_path.

## Archive: targeted git add only

- Repo had many pre-existing unrelated modified skill files (`config/hermes/skills/_custom/...`). Committed ONLY the archive JSON via `git add wiki/raw/archived/triage/newsletter/2026-08-14_20260814T102346Z.json` — never `git add -A` in triage runs.
- archive_triage.py output: 8 newly archived, 11 dedup_skipped (Superintel+ items share same URL), total archive URLs 2,641. Idempotent second run: "All items already archived (dedup)".
