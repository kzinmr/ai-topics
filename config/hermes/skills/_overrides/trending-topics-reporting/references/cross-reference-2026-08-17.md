# Cross-Reference — 2026-08-17 (Weekly Digest Mode)

> Weekly digest for 2026-08-10 → 08-16. Ran as `weekly-ai-digest` cron (Monday 00:00 UTC), delivered to Telegram. Saved to `inbox/rss-scans/weekly-ai-digest-2026-08-17.md`, committed + pushed (76e64e69).

## Environment notes (recurring, non-blocking)
- `hermes-report-quality` again reported "not found and skipped" — the known dual-path collision. Proceeded with trending-topics-reporting Weekly Digest Mode T1-T5. Start response with the brief ⚠️ notice, then continue.
- Bare-name `skill_view` for `wiki-daily-report` AND `trending-topics-reporting` returned "Ambiguous skill name" (local + `_overrides` copies are identical). Workaround: read either file directly with read_file, or use the categorized path (`research/trending-topics-reporting`). Note: `skill_manage` patch accepts the BARE name, not the categorized path.

## Data gathering that worked well
- `git log --since="2026-08-10" --oneline -- wiki/ | wc -l` → 116 commits (week volume).
- New-page enumeration for stats block:
  `git log --since="2026-08-10" --name-status --diff-filter=A --format="" -- wiki/ | grep -E "^A" | awk '{print $2}' | sort -u`
  → 31 new concepts, 15 new entities, 2 new events. Bucket by prefix, ignore `raw/` + `archived/`.
- `--diff-filter=M | grep -cE "^M"` → 1047 modified files.
- `grep -E '^## \[' wiki/log.md | tail -40` = fastest week overview; pair with git log for the full 7-day arc.
- Dedup anchors: previous weekly digest (08-03) + daily reports 08-13/08-15/08-16. Weekly digest does NOT dedupe against dailies — it synthesizes the week; dailies dedupe against it (Monday rule).

## Pitfall caught: fabricated URL
- Draft wrote `https://arxiv.org/abs/2608.0xxxx` for the "Stealing Reasoning Traces" paper. Final review pass flagged it; grep of raw article frontmatter (`wiki/raw/articles/2026-08-11-stealing-reasoning-traces-from-proprietary-llm-apis.md`) showed `paper_url: https://stolen-thoughts.com/paper.pdf` (plus `url: https://stolen-thoughts.com`, `source: x_thread`). Replaced before commit.
- Lesson: raw frontmatter is the URL source of truth; never guess URLs/IDs. Extend the 08-03 date-verification rule to URLs. arXiv IDs especially — do NOT pattern-match them.

## Topic curation notes
- Frontier Model Day cluster (8/13-14, 6 labs) → kept as separate topics per cross-reference-2026-08-13 pattern, but the week's arc was synthesized in the intro: "post-training + speed/price + agent security" rather than "new intelligence".
- Company concentration note in intro: Anthropic 3 topics, OpenAI 3 topics, DeepSeek 2.
- All ~35 wikilinks batch-verified with `for f in ...; do [ -f "wiki/$f.md" ] && echo OK || echo MISS; done` — all OK.

## T4 selection (title + intro)
- Title variants: (A) list-y coverage of top stories; (B) narrative arc "思考を盗まれ、エージェントが暴走し、ラボはIPOへ"; (C) top-2 + security only. Selected B — most specific narrative arc grounded in real events. Rejected A (list-y, weaker hook) and C (dropped economics angle).
- Intro variant B (6-lab concentration note + "主役は新しい知能ではない" framing) selected over a plain stats opener; picked for synthesis + concentration note coverage.
