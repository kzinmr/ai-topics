# blog-wiki-ingest patterns — 2026-11-18 (run 20261118T100050Z)

Session: blog-wiki-ingest downstream job, 20 candidates → 12 triage decisions (6 take / 5 reference / 1 batch-skip). All 6 takes were **enrichments of existing pages** (every `candidate_wiki_path` already existed on disk) — no new-page creation. Validated the checkpoint-recovery path end to end.

## 1. "failed to parse JSON response from blog-triage output" — script error is benign, checkpoint is authoritative

The pre-run script wrapper reported `{"ok": false, "error": "failed to parse JSON response from blog-triage output", "output_path": ".../cron/output/<jobid>/<ts>.md"}`. This is the **known markdown-wrap problem**: the cron runner wraps the triage agent's response in markdown, so the downstream JSON parser chokes on the embedded JSON block. It is NOT a data-loss event.

**Recovery (always try first, no retry of the upstream job needed):** read `~/.hermes/cron/data/blog_ingest/triage_latest.json` directly. It carried a complete, clean `decisions` array (6 take / 5 reference / 1 skip) with all required fields (`body_excerpt`, `reason_ja`, `candidate_wiki_path`). The checkpoint survives independently of the `.md` output file. Same pattern as the dreaming-pipeline recovery doc.

Corollary: trust `triage_latest.json`'s `Counter(recommended_action)` over the human-readable `summary_ja` narrative. The summary said "take 6 / reference 5 / skip 9" but the array had **1** skip decision — a single batch-skip entry whose `item_id` was `"blog-7,8,9,10,11,12,13,14,15,17b"` covering 10 raws. The summary counts raw articles, the array counts decisions. Neither is wrong; don't reconcile them by editing.

## 2. archive_triage.py `--keep-reference` count = references-with-content + skips, NOT references-with-URL

`python3 ~/ai-topics/scripts/archive_triage.py blog --keep-reference` returned `candidates: 6, new_archived: 6` — but the triage had **5 references + 1 skip = 6** decisions... wait, that's 6, matches. The earlier apparent mismatch was summary-vs-array (see #1). The real lesson: reference items whose `candidate_wiki_path` is `None` (e.g. RSS-only OpenAI ChatGPT-for-Sales / Le Figaro stubs) **are still archived** by `--keep-reference` — they have `body_excerpt` (the RSS one-liner) so they qualify. Do not expect them to be dropped for lacking a wiki path. `total_archive_urls` is the running dedup total (was 3277).

## 3. Sibling subagent write-warning fires on ~EVERY patch in the 07:00–18:00 UTC parallel window — benign, verify don't panic

7 of 7 `patch` calls on wiki pages returned `_warning: ... was modified by sibling subagent '<uuid>' but this agent never read it`. These were **stale/false-positive sibling signals**, not real concurrent mutation — `readlink`/re-read each time showed the file was exactly as I'd left it, line counts grew monotonically, no content was lost. The blog pipeline runs sibling-ingest jobs (newsletter-triage, active-crawl, etc.) in the same window that touch the shared `/tmp` and git tree.

**Correct mitigation:** on each warning, immediately re-verify the specific file with a cheap `grep -n "<your new heading>" <file>` + `wc -l <file>` before the next patch — confirm your prior edit survived and the next anchor still resolves. Do NOT re-read the whole file, do NOT abort. Only treat as real corruption if line count DROPS or your heading disappears.

## 4. Frontmatter `sources:` dedup — body `^[raw/...]` cites collide with frontmatter entries, patch needs a unique longer anchor

For pages like `entities/simon-willison.md`, the same raw hash (e.g. `datasette-maplibre--936b12b2.md`) appears BOTH as the last entry in the YAML `sources: [...]` array AND inside one or more body `^[raw/articles/...]` citation blocks. A `patch` whose `old_string` is just that path matches **2–3× → "Found N matches" error**. Even `...,hash.md]` can match twice if a body cite also ends with `]`.

**Fix:** anchor with enough surrounding context to be unique — for the frontmatter append, include the preceding sibling entry AND the line after the array:
```
old: ".../nov-15-datasette-agent--00814a21.md, .../nov-15-datasette-maplibre--936b12b2.md]\ntags: [person, blogger]"
new: ".../nov-15-datasette-agent--00814a21.md, .../nov-15-datasette-maplibre--936b12b2.md, <NEW1.md>, <NEW2.md>, <NEW3.md>]\ntags: [person, blogger]"
```
The trailing `]\ntags:` (or `]\n---`) is the discriminator that separates the frontmatter array from body cites.

## 5. wikilink targets — validate slug against disk before commit, two common broken forms

The pre-commit hooks validate index.md structure + tag taxonomy but **NOT `[[wikilinks]]`**. When enriching with `[[]]` links, resolve targets against the actual `wiki/` tree first. This session's broken guesses and their real slugs:
- `[[concepts/agent-safety-incidents]]` → real: `[[concepts/ai-agent-safety-incidents]]`
- `[[concepts/security-and-governance/prompt-injection]]` → real: `[[concepts/prompt-injection]]`
- `[[entities/prime-radiant]]` → no entity page exists; Prime Radiant content lives under `[[entities/superpowers]]` (Jesse Vincent's lab). Use `[[entities/superpowers]]`.

Quick check (no execute_code in cron): `find wiki -iname "*prompt-injection*"` and `grep -niE "ai-agent-safety" wiki/index.md` to confirm the canonical slug before writing. A dangling wikilink won't block the commit but creates a broken link the wiki-graph-health job later flags.

## Commit/push outcome (reference)

Targeted `git add` of only the 9 wiki files I touched (left the unrelated modified `config/hermes/skills/...` siblings unstaged). Pre-commit passed (`index.md clean`, `Tag validation passed — 9 files`). `git pull --rebase` failed with "cannot pull with rebase: You have unstaged changes" because of the sibling's unstaged skill files — but **plain `git push` succeeded** (`e6d217dc..9ee370b2 main -> main`). Per AGENTS.md: when rebase is blocked by a sibling's unstaged file, push standalone rather than stashing someone else's work.
