# Newsletter Wiki Ingest Recovery — 2026-08-12

Session: newsletter-wiki-ingest cron (job 4e8b0d92c6a1). Upstream newsletter-triage
failed JSON render; recovered from checkpoint and executed the full downstream.

## Recovery path (validated end-to-end)

1. Pre-run script reported `failed to parse JSON response from newsletter-triage output`
   with `output_path` — this is the known "Triage Agent Saves JSON Before Response Render
   Failure" variant (see SKILL.md §Pipeline Resilience).
2. `triage_latest.json` at `/opt/data/.hermes/cron/data/newsletter/triage_latest.json`
   was valid (16 decisions: 3 takes, 7 references, 6 skips). Read it directly — no
   extraction from the failed output md needed.
3. Post-recovery verification of every take (read page bodies, not frontmatter):
   - `concepts/openai-daybreak.md` — covered GPT-5.5-Cyber June launch only; Daybreak
     Blue/Red restructure absent → genuine gap, enrich.
   - `entities/unitree-robotics.md` — 75L page, no IPO info → genuine gap, enrich.
   - `entities/chai-discovery.md` — did not exist → new entity page.
4. Parallel enrichment: 3 blocks of 3 delegate_task subagents + 1 single (10 subagents,
   ~480s wall). Every subagent context included: absolute paths, "read_file then patch,
   do NOT write_file rich pages", frontmatter update instructions (updated: date + source
   path), and the triage facts inline (newsletter raw files are link stubs; the facts in
   `reason_ja`/`body_excerpt` are the content source).

## Pitfall 1: Subagent early commit

- The LTX subagent ran `git commit` itself mid-run (`802cc716`) despite context saying
  "parent handles commits" — it swept in sibling subagents' uncommitted `log.md` entries
  (Chai, Anthropic, AI Energy, Muse, OpenClaw) while those pages were still uncommitted.
- Detection: after each parallel block, check `git log --oneline -3` for unexpected
  commits AND `git status --short -- wiki/` to see which pages remain uncommitted.
- Reconciliation: leave the early commit in place (its log.md entries are legitimate);
  stage the remaining pages; commit once at the end. Final consolidated commit
  `e9fa4e24` (11 files, +197/−9) completed the set.

## Pitfall 2: CJK characters block pre-commit (English-only wiki policy)

- A log entry using `150.80元` / `1.699B元` (yuan symbol) was blocked:
  `❌ BLOCKED: Japanese content introduced to previously clean files: wiki/log.md`.
- Repo policy: all non-`raw/` wiki content must be English. The pre-commit hook flags
  CJK characters newly introduced to previously-clean files.
- Fix: transliterate before staging (`元`→`yuan`, `億`→`billion`, etc.). Re-commit passes.
- Distinct from the heredoc homoglyph scanner (which blocks Python scripts with embedded
  Japanese) — this is the pre-commit language policy on markdown content.

## Pitfall 3: `git pull --rebase` fails with pre-existing unstaged changes

- `git pull --rebase` errored `cannot pull with rebase: You have unstaged changes`
  (config/skill files from other work were dirty).
- `git push` alone still succeeded — the branch was already ahead; no rebase needed.
- Rule: stage only `wiki/`; never commit unrelated config/skill changes; push directly
  when pull --rebase fails on pre-existing dirt.

## Verification checklist after parallel enrichment

- `wc -l` + `grep '^updated:'` on every touched page (all should be today's date).
- `git show --stat <early-commit>` to see what a subagent commit swept in.
- Archive idempotency: `python3 scripts/archive_triage.py newsletter --keep-reference`
  returned "All items already archived (dedup)" because the triage agent had already
  archived 13 skip/reference decisions before failing to render — no double-archive.
