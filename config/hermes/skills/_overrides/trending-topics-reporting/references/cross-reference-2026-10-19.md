# Weekly Digest Worked Example — 2026-10-19

Run: weekly-ai-digest cron, Monday 00:00 UTC. Produced `inbox/rss-scans/weekly-ai-digest-2026-10-19.md` (commit `8a051aa2`), T1-T5 gates all passed.

## Gap-week handling

Previous weekly digest was **2026-09-14** — a ~5-week gap (09-21, 09-28, 10-05, 10-12 digests never produced). Per the existing pitfall ("previous weekly digest may NOT be last Monday"), the dedup anchor became:

1. Most recent DAILY reports: `trending-topics-2026-10-{14,15,16,17}.md` — these covered 10-12→10-17 well, so the digest window stayed 7 days (10-12→10-19), NOT the 5-week span.
2. `head -120 wiki/log.md` — gave the full pipeline activity for the window in one read (active-crawl created pages, blog-ingest, x-accounts-scan, newsletter triage).
3. The gap itself (09-15→10-11) was NOT re-covered — noted in the stats block as a one-line disclaimer pointing to daily reports. Re-summarizing 4 weeks would have blown the report length budget.

**Lesson**: a multi-week digest gap does NOT mean a multi-week window. Keep the 7-day window; the dailies already covered the gap. Mention the gap, don't fill it.

## Stats enumeration — documented git recipe is WRONG for renames

The SKILL.md recipe:
```bash
git log --since="7 days ago" --name-status --diff-filter=A --format="" -- wiki/ | grep -E "^A" | awk '{print $2}' | sort -u
```
Worked for Added files, but pages created via rename/move are reported as `R100 old new` lines and `grep -E "^A"` drops them entirely. If a bucket count looks suspiciously low, cross-check with `--name-only` (which lists only the new path for renames) and eyeball:

```bash
git log --since="7 days ago" --name-only --diff-filter=AR --format="" -- wiki/ | grep -vE "raw/|archived/" | sort -u
```

Also on this run: queries/ pages dominated the new-file count (21 of ~75 — a user-driven "modernization reading guide" workstream flooded queries/). Bucket by prefix (concepts/ entities/ events/ queries/) and report each bucket separately, else one workstream distorts the headline number. `--diff-filter=M | wc -l` for 更新 and `--oneline -- wiki/ | wc -l` for 総コミット worked as documented (58 commits, 289 new raw).

## HN re-calibration catches stale point claims in prior dailies

The 10-14 daily reported "Gemini 4 Argon HN 1339pts/933c". `scripts/hn_calibrate.py "Gemini 4 Argon"` on 10-19 could NOT reproduce it — best in-window hit was a derivative "Show HN: plays StarCraft" at 248pts/111c; the model-launch posts themselves had 2-3pts. Single-day front-page aggregate scans sometimes attribute combined engagement to one story, or points get edited down/flagged.

**Rule**: for any point figure carried forward from a prior daily into the weekly digest, re-query via `scripts/hn_calibrate.py "Topic" "Topic2" ...` (argv override, one call, ~10 queries) and cite the live per-story number. If unreproducible, either report the reproducible derivative with its own number or mark 「数値は一次ソース再確認要」 — never launder the stale figure.

Verified-good on this run: Muse Spark Open 916/477, DeepSeek 1017 935/704, Goodfire clean 821/336, Anthropic ECDSA 1050/388, Mercor 614/567, OpenCode 2.0 886/393. Also note HN title-substring queries return many 1-4pt spam hits around launch stories — filter by points before eyeballing "top hit".

## hn_calibrate.py argv usage

`python3 config/hermes/skills/_overrides/trending-topics-reporting/scripts/hn_calibrate.py` with no args runs a stale hardcoded default list (Gemini 3.7 Flash, RSP, etc. — mostly no-hits for current topics). ALWAYS pass the week's topic strings as argv. Path is repo-relative (`config/hermes/skills/_overrides/...`), not `~/.hermes/skills/...`.

## Weekly-specific quality gates that paid off (re-confirmations)

- T5 batch wikilink check with `[ -f wiki/$f.md ] || [ -f wiki/$f/$f... _index ]` — one loop caught MISSes for dir-index pages (`concepts/multi-agents/` → `_index.md`) and pages that log.md claims were created under a different path (`liquid-ai-lfm2-5-24b-a2b` doesn't exist; content went into `entities/liquid-ai.md` as a section). Trust `ls` over log.md claims for link targets.
- T1 slop grep: `NO_SLOP_FOUND` on first pass — the firing-order rule (T1 last) held.
- Typo grep `ウィクション` (the SKILL template itself carries this typo in its table header example) — write `ウィキ推奨アクション`.
- Newsletter files in `wiki/raw/newsletters/` carry useful subjects in filenames (`...coreweave-sell-off-looks-more-like-the-telecom-bust-than-dotc.md`) but bodies are pure Substack redirect junk — scan subjects only; get substance from HN re-calibration + raw articles, or the open.substack.com full-text recipe (`references/ainews-fulltext-extraction.md`).
- Vendor-reported benchmark tables (DeepSeek 1017): copy verbatim from the event page's frontmatter-sourced content and label 「ベンダー申告（未独立検証）」 — never retype from memory.
