# Log.md header-burial recovery + parallel-sibling verification (2026-08-13)

Validated during newsletter-wiki-ingest 2026-08-13 (checkpoint-recovery run, 10:37 UTC window, sibling blog-wiki-ingest running in parallel).

## Symptom: `# Wiki Log` header buried below sibling entries

When a sibling pipeline (blog-wiki-ingest, raw-backlog-ingest) commits BEFORE you in the same window, it prepends its entry ABOVE the `# Wiki Log` / `_Log of all wiki changes..._` header. Result: log.md starts with `## [2026-08-13] blog-wiki-ingest ...` and the header sits at line ~9. Naively "prepending after the header line" (the skill's normal guidance) no longer works because the header is not at the top.

Detection: `head -5 wiki/log.md` — if the first line is a `## [date]` entry rather than `# Wiki Log`, the header is buried. Also confirm with `grep -n "^# Wiki Log\|^_Log of all wiki" wiki/log.md` to get the actual line numbers.

## Fix: rebuild log.md in Python (cron-safe, no sed -i)

Write to `/tmp/` via `write_file`, run via `terminal` (execute_code is blocked in cron mode). Script moves the buried header to the top, inserts your new entry after it, then re-appends the entries that were above the header (preserving their order), then the rest of the body:

```python
#!/usr/bin/env python3
"""Rebuild log.md: move buried header to top, insert new entry after header."""
log_path = "/opt/data/ai-topics/wiki/log.md"
entry_path = "/tmp/<pipeline>_wiki_ingest_log_<date>.md"   # your new entry file

with open(log_path, "r") as f:
    lines = f.read().split("\n")

header = ["# Wiki Log", "", "_Log of all wiki changes. Newest entries at top._", ""]
idx_title = lines.index("# Wiki Log")
idx_desc = lines.index("_Log of all wiki changes. Newest entries at top._")

above = lines[:idx_title]                    # sibling entries prepended above header
body_after = lines[idx_desc + 1:]            # everything after header
if body_after and body_after[0] == "":
    body_after = body_after[1:]              # strip the blank line after desc

with open(entry_path, "r") as f:
    entry = f.read().rstrip("\n")

new_content = "\n".join(header + [entry, ""] + above + body_after)
new_content = new_content.rstrip("\n") + "\n"

with open(log_path, "w") as f:
    f.write(new_content)
```

Verify: `head -30 wiki/log.md` → header first, then YOUR entry, then the sibling's entry, then the rest. If a sibling's entry ends with no blank line before the next `##` (seen: `- index.md: 4 entries updated...` directly followed by `## [2026-08-13] raw-backlog...`), the rebuild fixes that too — do not hand-edit with sed.

## Symptom: patch tool sibling-subagent warnings

`patch` returned `_warning: "… was modified by sibling subagent '<uuid>' but this agent never read it"` on `concepts/qwen-3-8.md`, `concepts/synthid.md`, and `wiki/index.md`. These are NOT errors — the patch applied.

Verification procedure (do not trust the warning or dismiss it):
1. `git diff wiki/<file> | head -60` — confirm the diff contains ONLY your intended change and no sibling content was clobbered.
2. Read back the patched section (`sed -n` the lines) to confirm the final state.
3. Check `git log --oneline -5` and `git status --short` to see what the sibling already committed (this tells you which cross-pipeline dedup skips are valid — e.g., blog-wiki-ingest commit `d2b93aaa` containing the DeepSeek V4-Pro-0813 take made the newsletter triage's DeepSeek skip correct).

## Targeted git add in a dirty tree

AGENTS.md canonically says `git add wiki/`, but in the parallel-window the working tree contains many unrelated untracked files (sitemap-monitor raw articles, config/hermes/skills changes, root-level junk like `YnNF55QV0zs`, `log.md`, `raw/`, `fetch_articles.py`). Sweeping `git add wiki/` would pull sitemap raw articles and other pipelines' files into YOUR commit.

Validated pattern (both this session and the sibling's commit `d2b93aaa` used it): targeted `git add` of ONLY the files you changed plus the raw sources you reference in frontmatter:

```bash
git add wiki/events/<new-page>.md wiki/entities/<a>.md wiki/entities/<b>.md \
        wiki/concepts/<c>.md wiki/concepts/<d>.md wiki/index.md wiki/log.md \
        wiki/raw/newsletters/<digest-1>.md wiki/raw/newsletters/<digest-2>.md \
        wiki/raw/inbox/newsletter-ingest/<run>.json
git status --short | grep "^[MADRC]"   # verify exactly your files are staged
```

Include the raw newsletter digests you cite in `sources:` (the triage agent may have failed before committing them — confirmed 2026-08-13: raw digests were untracked because the triage output failed JSON parse). Do NOT stage config/ skills or other pipelines' raw articles.

## Archive double-run is safe

The triage agent already ran `archive_triage.py newsletter --keep-reference` (commit `9a39cc65`). Re-running at ingest time returns `{"ok": true, "message": "All items already archived (dedup)", "archived": 0}` — safe to attempt, and the message confirms completeness. Note the triage agent's archive may contain only a SUBSET of decisions (2 of 6 archive-worthy items on 2026-08-13) — re-run dedups the rest against `archive_index.json`; if it says all-deduped, the remaining URLs were already indexed from prior runs.
