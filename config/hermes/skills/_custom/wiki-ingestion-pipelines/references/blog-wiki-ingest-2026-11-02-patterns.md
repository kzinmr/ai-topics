# blog-wiki-ingest patterns — 2026-11-02 (run 20261102T101809Z)

## Recovery context (validated again)
blog-triage cron response failed JSON parse (`failed to parse JSON response from blog-triage output`), but `triage_latest.json` at `${HERMES_HOME}/cron/data/blog_ingest/` contained valid JSON with a fresh `checkpoint_run_id` matching the day's `blog_ingest_20261102T101809Z.json`. Read the checkpoint directly; the failed output file's `## Response` section even contained the human-readable triage report — useful cross-check of take/ref/skip counts and expected `candidate_wiki_path`s, but the checkpoint JSON is authoritative. Verify the prior consumption commit with `git log --oneline -3` + check the archive dir (triage run had already archived skip+reference items; re-running `archive_triage.py blog --keep-reference` printed "All items already archived (dedup), archived: 0" — that's correct, not a failure).

## Take verification lessons
- **"sources listed / entity exists" checks matter**: Kyle Kingsbury quote-post was a legitimate new-entity take — `search_files`-style content grep found only ONE incidental mention (in `entities/dan-luu.md`). A tiny raw file (831B quote-post) is still valid new-entity material when the quote is distinctive and the person is a major figure (Jepsen author).
- **Dated stub ≠ covered**: `concepts/ai-alignment.md` (62 lines, updated May 2026) only covered the Positive Alignment paper; the Goedecke alignment-impossibility essay (Kripke quaddition, shoggoth, motive-incoherence) was a genuine gap even though the topic keyword "alignment" matched everywhere. Same for `concepts/interpretability.md` — it had only technical limitations, zero principled-skepticism coverage.
- **Dual concept-page filing works well**: one flagship essay can warrant a full section in TWO concept pages (ai-alignment + interpretability) with cross-wikilinks, plus a Core Ideas section on the author entity. Keep the full argument in the primary page; the secondary page gets the angle specific to it plus a pointer.

## Git pitfalls hit this session
1. **`related:` frontmatter lists use plain paths, NOT `[[wikilinks]]`** — a patch adding `- [[entities/anthropic]]` to the `related:` block is wrong syntax (that block wants `- entities/anthropic`). Only body text uses `[[...]]`. Revert immediately if the patch diff shows `[[]]` appearing in frontmatter.
2. **`git pull --rebase` blocked by sibling unstaged files** — sibling subagents/pipelines had unstaged `?? raw/newsletters/...` files. `git push` alone still succeeded (fast-forward, no divergence). Pattern: if pull --rebase fails with "unstaged changes", check `git push` directly before stashing anything — only rebase when push actually rejects as non-fast-forward.
3. **Post-apply grep verification**: after commit, grep a distinctive phrase per touched page (`grep -c "Autodoxing" wiki/...`) to confirm content actually landed — cheap defense against sibling overwrites and subagent false-success.

## Other notes
- log.md prepend via `cat entry.md log.md > merged && mv` worked clean; log.md has no H1 title line, so prepending at byte 0 is safe.
- New SCHEMA tag (`philosophy-of-mind`) added to Domain Concepts BEFORE using it in pages — pre-commit tag validator then passed all 12 staged files.
- `execute_code` is blocked in cron mode (approvals); use patch/write_file/terminal tool calls directly instead.
