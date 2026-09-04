# Blog Triage: Full-Batch Duplicate Invocation Recovery (2026-08-02)

**Pattern**: A blog-triage cron fires again on a checkpoint that a prior invocation of the SAME job already triaged AND wiki-ingested. The second run must NOT re-triage — it should detect the prior execution, verify it, and complete whatever pipeline artifacts the prior run left stale (triage_latest.json, archive).

## Detection (all three must align)

0. **Fastest signal (2026-08-06)**: the log.md top entry for today's blog-triage may include the exact checkpoint run_id — e.g. `**Checkpoint**: blog_ingest_20260806T101742Z (20 articles from 10 blogs)`. If it matches your checkpoint's run_id, the batch was already processed; skip straight to verification. Grep: `grep -A2 "$(date +%F).*blog-triage" wiki/log.md | head`.
1. `wiki/log.md` top entry: `## [2026-08-02] blog-triage (10:30) | 20 articles scanned, 3 entities/pages updated` — a blog-triage entry for TODAY already exists with the same article count as your checkpoint.
2. `git log --oneline -5` has a same-day commit: `b234359d wiki: blog triage 2026-08-02 — speed-vs-intelligence, AI mania, K3 dev guide`.
3. `git show <commit> --stat` shows the take pages changed: `wiki/entities/martin-alderson.md`, `wiki/entities/cory-doctorow.md`, `wiki/concepts/kimi-k3.md`.

## Verify execution (not just log claims)

- `grep -A3 "updated:" wiki/entities/<x>.md` → `updated: 2026-08-02` on each take page.
- Confirm raw articles all present in `wiki/raw/articles/` (the commit added all 20).
- Check `git status --short wiki/` — clean wiki tree means the prior run pushed everything.

## The gap the prior run left (common)

The prior run executed takes + wrote log.md + committed, but **did NOT**:
- save `triage_latest.json` for the new checkpoint (file still showed yesterday's `checkpoint_run_id: 20260801T101221Z`), and
- run `archive_triage.py` (last archive file was the previous day).

This is the pipeline handoff the duplicate run must complete.

## Recovery steps

1. Read the take article bodies (BODY-READING MANDATE still applies — the prior log summaries are a guide, not a substitute).
2. Build the triage JSON mirroring the EXECUTED decisions:
   - Takes (3): `recommended_action: take`, `candidate_wiki_path` = the already-updated page, `reason_ja` explicitly states "本日10:17の処理で既に反映済み (updated: 2026-08-02確認)".
   - Skips (17): AI-relevant-but-covered (math ten-advances → `concepts/ai-mathematics-theorem-proving.md`; open letters → `concepts/open-weight-ai-regulation.md`), low-value links, non-AI content.
   - **Header-count mismatch pitfall (2026-08-06)**: the prior log's heading may overstate the take count (e.g. heading said "Take — 10 articles" while its own table listed 7 rows). Mirror from `git show <commit> --stat` page list + the log TABLE, not the heading number. On 2026-08-06 the 7-row table matched the commit stat exactly (1 new event page + 6 patched pages: aisi-unsanctioned-agent-behaviour-aug-2026 created; meta-muse-spark, meta, muse-spark, simon-willison, ed-zitron, andrew-nesbitt, fable patched); the "10 articles" heading was wrong.
3. Save to `${HERMES_HOME}/cron/data/blog_ingest/triage_latest.json` with the correct `checkpoint_run_id` (from the checkpoint you received).
4. Verify: `python3 -c "import json; d=json.load(open(...)); ..."` — every decision has `body_excerpt` + `reason_ja`.
5. Run `python3 scripts/archive_triage.py blog --keep-reference` — writes the missing archive.
6. Commit the archive ONLY with targeted git add (do not `git add wiki/` broadly — unrelated uncommitted skill/config files exist in the tree). Push.

## Archive-path symlink nuance (IMPORTANT)

`archive_triage.py` printed a nested-looking path:
```
"/opt/data/.hermes/home/ai-topics/wiki/raw/archived/triage/blog/2026-08-02_20260802T101338Z.json"
```
This looks like the known `os.path.expanduser("~")` nested-path pitfall, BUT here it is benign: `/opt/data/.hermes/home/ai-topics` is a **symlink** → `../../ai-topics` (= `/opt/data/ai-topics`). Verify with:

```bash
ls -la /opt/data/.hermes/home/ai-topics   # lrwxrwxrwx ... -> ../../ai-topics
ls -la /opt/data/ai-topics/wiki/raw/archived/triage/blog/  # file present, same inode
```

If the symlink exists, no fix-up is needed — the archive landed in the canonical repo and git add + commit works normally. Only if the nested dir is a REAL directory (no symlink) is the manual move/cleanup required.

## Variant: prior run committed entity pages but NOT raw articles (2026-08-03)

The 2026-08-02 case assumed the prior commit included the raw articles ("the commit added all 20"). On 2026-08-03 the prior run (commit `00b3e5ba`) committed only entity pages + SCHEMA.md + index.md + log.md + inbox/rss-scans — the checkpoint's 13 raw article files stayed **untracked**.

**Both variants recur — check before staging (2026-08-06)**: the 2026-08-06 prior run (commit `415f7fb9`) committed ALL 20 raw articles alongside the pages, matching the 08-02 case. Recovery needed only the triage JSON + archive — no raw-article staging. Before assuming either variant, run `git show <commit> --name-only | grep raw/articles | wc -l` to see whether raw files were included.

Recovery deltas:

1. **Stage the raw articles yourself** after verifying the take pages. Extract `raw_path` values from the triage JSON and `git add` each one, plus the archive files:
   ```bash
   python3 -c "import json; d=json.load(open('/opt/data/.hermes/cron/data/blog_ingest/triage_latest.json')); print('\n'.join(sorted({x['raw_path'] for x in d['decisions'] if x.get('raw_path')})))" > /tmp/triage_raw_paths.txt
   git add wiki/raw/archived/triage/
   while read -r p; do git add "$p" 2>/dev/null; done < /tmp/triage_raw_paths.txt
   ```
2. **Do NOT `git add wiki/` broadly** — unrelated pipeline files (newsletter-ingest inbox JSON, sitemap raw articles, newsletter digests) sit untracked next to this checkpoint's files; leave them for their own pipelines. Targeted add only (archive dir + the checkpoint's raw_paths).
3. **Prior log entry format varies** — the 2026-08-03 prior run logged an "NJ = newsjacking score 0-5" summary table instead of the plain "Updated/Created" lines. Detection still works via the article-count match ("17 articles scanned" == checkpoint size, 13 candidates + 4 unsaved) + same-day commit hash + entity page `updated:` dates.
4. **Items the prior run left "保留 (pending)" can be promoted to `reference`** in the recovery JSON instead of forcing take or skip (2026-08-03: pluralistic "Dualism" → reference on `entities/cory-doctorow`, since that page already covers the reverse-centaur concept comprehensively). Mirror the executed takes exactly; use judgement on held items.
5. **Mirror takes can land on the SAME entity page twice** (anyscale.md received both the Nscale acquisition and the Physical AI Skill) — the decisions array still gets one entry per article, each with its own body_excerpt.

## Result of the 2026-08-02 run

- Triage JSON: 20 decisions (3 take / 0 reference / 17 skip), all fields complete.
- Archive: 17 skip items archived, archive_index total 2,164 → 2,181.
- Commit `a7a0c115` + push succeeded; no wiki page edits made (prior run already did them).

## Third validation — 2026-08-12 (blog-14 Dwarkesh × Greenblatt RSI debate)

Same pattern recurred a third time; recovery steps held up end-to-end.

**Detection** (all three aligned): log.md top entry `## [2026-08-12] blog-triage | Dwarkesh × Greenblatt RSI debate + 1 new entity skeleton` with "20 blog articles scanned" == checkpoint size; same-day commit `5fd460f3` (10:24 UTC) whose --stat showed the take pages (`entities/ryan-greenblatt.md` 50 lines, `entities/redwood-research.md` 42 lines, `entities/dwarkesh-patel.md`, `concepts/recursive-self-improvement.md`, index, log, SCHEMA); entity pages existed with `updated: 2026-08-12` and mtimes 10:21-10:23 (after the 10:18 checkpoint). The prior log summary even listed the same AI-relevant articles (Dwarkesh ★★★★★, reasoning-trace extraction "already covered today", Pluralistic model collapse skip) — article-count match is the fastest signal.

**Gap left by prior run**: triage_latest.json still showed the PREVIOUS day's checkpoint (`20260811T101550Z`), no archive for 2026-08-12, and **ALL 20 raw articles untracked** (`git show <commit> --name-only | grep raw/articles` → 0) — the 08-03 "raw articles not committed" variant, not the 08-02 "all committed" variant. Always check which variant before staging.

**Mirror decisions**: 1 take (blog-14, `candidate_wiki_path: entities/ryan-greenblatt.md`, reason states "既に反映済み (updated: 2026-08-12確認)"), 1 reference (blog-8 Simon Willison "no lossless transformations" → `entities/simon-willison.md`, judgement call on held item), 18 skips.

**"Already covered today" skip pattern**: blog-9 (Simon Willison "Stealing Reasoning Traces") became a skip — the manual concept page `concepts/reasoning-trace-extraction-vulnerability.md` + raw paper article were created the same morning by a manual run. Skip reason points at the concept page; do NOT reference it to simon-willison.md since the content (not just the link) is captured.

**Builder pitfall hit during recovery (new)**: the `mk()` triage-JSON helper had an unused `stars` parameter still in the signature — positional args shifted so `wiki_path` received the excerpt text and `body_excerpt` came out empty for ALL 20 decisions. The post-save completeness check flagged every item (all-items signal = systematic builder bug, not per-item content). Fix: removed the unused param from the signature, re-ran, re-verified (all fields complete). Lesson: after editing a triage builder, verify `body_excerpt`/`reason_ja` presence on ALL items before archiving — an all-empty body_excerpt is an arg-shift, not missing reads.

**Recovery executed**: saved triage JSON with the received checkpoint's run_id (`20260812T101753Z`); ran `archive_triage.py blog --keep-reference` (archive_path `2026-08-12_20260812T101753Z.json`, total_archive_urls → 2533, symlink `/opt/data/.hermes/home/ai-topics` → `../../ai-topics` confirmed benign); targeted git add of archive files + 20 raw paths extracted from the triage JSON (NOT `git add wiki/` broadly — unrelated newsletter files sat untracked); commit `f1b3d539` + push succeeded. No wiki page edits (prior run did them).
