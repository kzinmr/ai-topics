# Newsletter Wiki Ingest — 2026-08-15 Patterns

Recovery + execution notes from the 2026-08-15 newsletter-wiki-ingest run (5 newsletters, 1 take + 4 references + 1 batch skip).

## Triage render failure → checkpoint recovery (validated again)

Cron wrapper returned `{"ok": false, "error": "failed to parse JSON response from newsletter-triage output"}`. The triage checkpoint at `${HERMES_HOME}/cron/data/newsletter/triage_latest.json` (run 20260815T101720Z) was **already saved and field-complete** (every decision had body_excerpt + reason_ja). Recovery = read the checkpoint directly, skip re-triage, go straight to Post-Recovery Verification. This matches the established "saves JSON before render" pattern — no new failure mode.

## Archive handoff — triage agent already ran archive

`git log --oneline -3` showed commit `943fe60e newsletter-triage: archive 5 skip/reference decisions (2026-08-15)` — the failed triage agent had ALREADY run `archive_triage.py newsletter --keep-reference` and committed before its render failure. **Ingest must NOT re-run archive** when this commit exists; check git log first. (Blog-wiki-ingest same-day commit `41d3db64` also confirmed blog pipeline is separate and non-conflicting.)

## Small-batch sequential enrichment is fine (no parallel needed)

6 page updates (concepts/glm-5-3, entities/nathan-lambert, entities/openai, concepts/ai-consciousness-debate, events/grok-4-6-launch, entities/aakash-gupta) were done **sequentially with direct patch calls by the parent** — no delegate_task. This worked cleanly (~147 lines added) and avoided subagent hazards. The parallel-delegation guidance is for 4-6+ *takes from recovered checkpoints with heavy bodies*; for a 1-take + 4-reference run where the parent already holds all facts in context, sequential patch is simpler and safer. Verify each target page exists + read it before patching (all 6 existed; no index.md additions needed — only the grok-4-6-launch index description line was refreshed).

## pull --rebase failure ≠ push failure

`git pull --rebase` errored `cannot pull with rebase: You have unstaged changes` — caused by sibling-process edits to `config/hermes/skills/` (pre-existing, unrelated). Since the remote had NOT diverged, plain `git push` succeeded (`41d3db64..2207a878`). Verify with `git ls-remote origin main` matching local HEAD before pushing directly; do not let the pull error block delivery.

## Content notes

- GLM-5.3 take was an existing-page update (★★★★☆), not a new page: concepts/glm-5-3.md existed (active-crawl 08-14) with model specs; the genuine gap was Nathan Lambert's strategic analysis (750B params vs Kimi K3 1/3, Z.ai post-training vs Moonshot pretraining, release-cycle advantage, Chinese RL data industry, staged-release + CoT monitoring, open-weights diffusion one-way door). Added as new section + entity entry in nathan-lambert.md.
- events/grok-4-6-launch.md Aug 14 follow-ups (Ben's Bites session #2 file-and-folder substrate; Aakash review: $60B Cursor acquisition closed, persistent cloud computer, approval-gated autonomy) enriched an existing event page — the page already had Aug 13 Grok Bot coverage, so this was a subsection add.
- entities/openai.md Economics Update (Aug 2026): $40B annualized revenue (Bloomberg), both labs filed confidential IPO paperwork — updates the May 2026 economics table ($25B ARR).
- concepts/ai-consciousness-debate.md gained a Human-AI Emotional Attachment & Grief section (Roomba owners Georgia Tech, Tamagotchi effect, catfish analogy, GPT-4o retirement backlash Aug 2025) — the page previously covered the philosophical debate only.
- Frontmatter discipline: updated `updated:` + `sources:` (raw newsletter file) on every touched page; log.md entry written in English (CJK block rule held); commit passed index + tag validators.
