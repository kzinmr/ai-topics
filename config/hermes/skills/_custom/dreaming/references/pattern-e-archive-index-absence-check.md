# Pattern E — Archive-Index URL-Absence Check (2026-08-11 validation)

## Scenario

dreaming-wiki-ingest received the standard failure signature:
- Pre-run script: `{"ok": false, "error": "failed to parse JSON response from dreaming-group output"}`
- Output file: `/opt/data/.hermes/cron/output/c4a9e8d2f671/2026-08-11_18-15-24.md` (4,677 lines)
- Upstream commit `fc4b3b29` (18:14) already on main: saturation pass, Takes=0, 6 skips, archive 6 decisions
- Output-file analysis + `triage_latest.json` (18:13) BOTH confirmed "saturation, all covered"

## The Gap

Upstream saturation passes evaluate ONLY the checkpoint's candidate list (`articles` from the dreaming checkpoint). They do NOT scan `~/wiki/raw/articles/` for sitemap-monitor scrapes. On 2026-08-11 the 06:00 sitemap batch — Pinecone ×2, Harvey ×2, ElevenLabs ×4 — was scraped but never triaged by blog-triage (its 10:20 JSON covers only the 10:16 RSS batch) nor by the upstream saturation pass.

## Detection Recipe (cheap, decisive)

1. **Check archive-index membership first** — this is the dedup baseline, stronger than log.md grep:
   ```bash
   # Extract URL from each recent raw article frontmatter
   for f in wiki/raw/articles/2026-08-11_*.md; do grep -m1 "^url:" "$f"; done
   # Then test membership against the archive index
   python3 -c "
   import json
   idx = json.load(open('wiki/raw/archived/triage/archive_index.json'))
   urls = set(idx if isinstance(idx, list) else idx.keys())
   for u in ['https://www.pinecone.io/blog/the-ceiling-was-never-the-model/']:
       print(u in urls, u)
   "
   ```
   URL absent from `archive_index.json` = never decided = genuine candidate. (Note: 2498 URLs in index; sitemap article URLs returned False for all 8 candidates → confirmed untriaged.)

2. **Cross-check what blog-triage actually covered**: read `~/.hermes/cron/data/blog_ingest/triage_latest.json` decisions — its titles reveal which batch it handled (10:16 RSS) vs what's on disk (06:00 sitemap).

3. **Verify existing wiki coverage by content grep** (not frontmatter `sources`): e.g. `grep -n "Nexus\|τ-Knowledge\|47.4" wiki/entities/pinecone.md` — entity page had June EA benchmarks but zero Aug 6 GA/τ-Knowledge content → genuine gap.

4. **Dual-enrichment check**: the Pinecone article spanned BOTH `entities/pinecone.md` (company launch) AND `concepts/ai-benchmarks/tau-knowledge.md` (benchmark leaderboard result) — check the partner/benchmark page too before finalizing.

## Outcome

- 4 pages enriched (pinecone, tau-knowledge, harvey, elevenlabs — 3 customer stories in one page)
- Triage JSON: 6 upstream skips + 8 new decisions (6 reference, 2 skip)
- Archive: re-ran `archive_triage.py dreaming --keep-reference` — 8 new decisions archived, dedup_skipped=6 (upstream's already-committed URLs), total_archive_urls 2498→2506. Idempotent — safe to re-run after appending decisions.
- Commit `f749c39f`, tag + language hooks passed cleanly. Selective staging used: content pages + log.md + archive files ONLY (stale skill-file changes from other jobs left untouched).

## Key Numbers

- Pinecone Nexus GA (Aug 6): τ-Knowledge agent+Nexus **47.4% vs best frontier 46.4% at 74% less cost**; GPT-5.2 +12% accuracy at 80% lower cost; GPT-5.5 held accuracy at 77% lower cost; tool calls 42.5→17.7 / 28.6→16.0; model calls 81.7→42.6 / 60.9→39.4; task cost $1.45→$0.53; 96/97 tasks; own support queue 24.6%→55.1%; 800+ orgs early access; 3.5M chunks→26K artifacts; KnowQL query language.
- Harvey Corporate Compliance AI (Aug 10): 6-stage regulatory change management table (monitoring→interpretation→obligation mapping→gap analysis→policy updates→audit trail); compliance-AI vs AI-governance distinction.
- ElevenLabs: Admiral (90% FCR, sentry sub-agent, French-native prompting), Deutsche Telekom (Magenta AI Call Assistant — first network-integrated AI call assistant), Finch Legal (call success 59%→93%, 500→3,800+ calls/week).

## Rule

When `recent_raw_articles > 0` (or checkpoint `total_articles == 0` with recent files), ALWAYS run the archive-index URL-absence check over the last 2-3 days of `raw/articles/` before accepting a saturation verdict — regardless of what the upstream output file claims.

## 2026-08-12 validation — upstream's explicit batch-skip table was incomplete

Same failure signature (render failure, `triage_latest.json` saved with `decisions: []`), same lesson, ONE new twist: the upstream output file EXPLICITLY enumerated its Pattern E scan results — "Hex Technologies ×3, Hebbia ×7 → 10 → Skip (product marketing)" — yet the SAME 06:00 sitemap batch contained **Fireworks × Muse Glimmer, Factory × DGX Spark, Harvey ×3, ElevenLabs ×2** that its top-40-by-mtime scan never listed at all. The upstream's own table was the evidence it HAD scanned the batch — but its scan was incomplete, and Fireworks/Factory turned out to be the session's two genuine enrichment gaps.

**New rule**: an explicit batch-skip table in the upstream analysis is NOT ground truth. The archive-index absence list is. Run the probe, then read bodies only for the never-archived files — including ones the upstream table didn't mention.

**Reusable probe**: `scripts/check_archive_index_absence.py` in this skill (cron-safe, no pipes). On 2026-08-12 it returned 37 never-archived files from a 3-day window; body reads + entity greps narrowed to 2 references (Fireworks, Factory) + 15 skips (Hex ×13 batch, Hebbia ×10 batch, Harvey ×3 covered, ElevenLabs ×2, Martin Alderson covered at entity L206-218, GitHub Models covered at concepts/github-models.md, X articles/manual ingest done today).

**New contentless-scrape signature**: sitemap scrapes can fail with `Scrape failed: brotli: decoder process called with data when 'can_accept_more_data()' is False` — the file is <500 bytes with no body → skip without body-reading (ElevenLabs ai-call-center-technology, 472 bytes, 2026-08-12).

**Empty-triage overwrite detail**: when the upstream triage is `decisions: []` (not stale skips — literally empty) because the upstream decided "saturation, nothing to archive", the downstream's Pattern E decisions MUST overwrite it before `archive_triage.py` runs — otherwise the archive records nothing and the "why dismissed" record for 37 articles is lost. This matches the 2026-08-06 "persist the never-archived decisions" variant; an empty decisions array is the strongest form of the trigger.

**Dual-enrichment reconfirmed**: Fireworks × Meta Muse Glimmer spanned BOTH `entities/muse-glimmer.md` (architecture specs, benchmark table vs Gemma 4 / Qwen 3.6, reasoning-effort control) AND `entities/fireworks-ai.md` (day-later launch decision, agent-traffic autoscaling) — zero Muse coverage on the platform page. Same pattern as the 2026-08-09 Fireworks × Voyage AI case.

**Outcome**: 3 pages enriched (muse-glimmer, fireworks-ai, factory-ai), 19-decision triage (2 reference / 17 skip), archive 17 new URLs (2550→2567), commit `0dd0a3b8`, tag + language hooks passed cleanly. Also repaired log.md single-header burial (see SKILL.md Pitfall #14).
