# Log Header Burial Fix — 2026-08-09 Worked Example

## Symptom
`# Wiki Log` at line 39; entries (raw-backlog-ingest 14:00, newsletter-wiki-ingest, blog-wiki-ingest, raw-backlog 04:00, raw-backlog 22:00) prepended above the header. Metadata line `_Log of all wiki changes. Newest entries at top._` at line 47 — BELOW the first `## [` entry (active-crawl) in the buried file.

## Root cause
raw-backlog-ingest (and other prepend-based pipelines) insert entries at absolute position 0 instead of after the `# Wiki Log` header block. 3rd recurrence: 07-31, 08-08, 08-09. Pipeline-level fix recommended: prepend after the header block, not at position 0.

## Fix sequence (cron-safe — write scripts to /tmp, run via `python3 /tmp/script.py`)

1. **Restore header**:
   ```bash
   python3 config/hermes/skills/_overrides/wiki-graph-health/scripts/fix_log_header_burial.py
   ```
   Output: "Header buried at line N; restoring to line 1", N entries preserved, 0 pipe corruption.
   ⚠️ Leaves `log.md.bak` — remove it before `git add wiki/`.

2. **Relocate stranded metadata** (script doesn't move it when it sits below the first entry):
   ```python
   with open('wiki/log.md') as f: lines = f.readlines()
   meta_idx = next(i for i,l in enumerate(lines) if l.strip() == '_Log of all wiki changes. Newest entries at top._')
   if meta_idx > 5:
       lines.pop(meta_idx)
       if meta_idx < len(lines) and lines[meta_idx].strip() == '': lines.pop(meta_idx)
       elif meta_idx > 0 and lines[meta_idx-1].strip() == '': lines.pop(meta_idx-1)
       lines.insert(2, '_Log of all wiki changes. Newest entries at top._\n')
       if lines[1].strip() == '' and lines[2].strip() == '': lines.pop(1)
       open('wiki/log.md','w').writelines(lines)
   ```
   Verify: `head -5` shows `# Wiki Log`, blank, metadata, blank, first entry.

3. **Insert missing separators** (skip first entry after metadata; 103 before `## [date]` entries, then a second pass for 5 non-bracket `## YYYY-MM-DD —` tail headers):
   ```python
   import re
   with open('wiki/log.md') as f: lines = f.readlines()
   targets = []
   headers = [(i, l) for i, l in enumerate(lines) if re.match(r'^## ', l)]
   for idx, (ln, text) in enumerate(headers):
       if idx == 0: continue  # never before the first entry after metadata
       prev = ln - 1
       while prev >= 0 and not lines[prev].strip(): prev -= 1
       if prev < 0 or lines[prev].strip() != '---': targets.append(ln)
   for ln in sorted(targets, reverse=True): lines.insert(ln, '---\n')
   open('wiki/log.md','w').writelines(lines)
   ```

4. **Collapse double separators**: `content.replace('---\n\n---\n', '---\n')` (3 collapsed in this run). Re-scan for `---\n---\n` (no blank) too.

5. **Verify**:
   - `head -1 wiki/log.md` == `# Wiki Log`; metadata at line 3.
   - awk missing-separator count == 0 (use `^## ` scan, not `^## \[`).
   - `grep -cP '^\|$' wiki/log.md` == 0.
   - `git diff --stat wiki/log.md` — ~110 insertions is under the 500-line defer threshold.

6. **Append watchdog entry AFTER header block** (NOT at position 0 — that re-buries the header):
   ```python
   lines = content.split('\n')
   header_idx = next(i for i,l in enumerate(lines) if l.rstrip() == '# Wiki Log')
   first_entry_idx = next(i for i in range(header_idx+1, len(lines)) if lines[i].startswith('## ['))
   header_block = lines[:first_entry_idx]; rest = lines[first_entry_idx:]
   result = '\n'.join(header_block) + '\n' + new_entry + '\n'.join(rest)
   ```
   Re-verify `head -1` after the write — assert `# Wiki Log`.

7. Commit: `watchdog: fix log header burial + N missing separators (date)`. This run: `8b27aa2e`, pushed clean (tag validator passed, 1 file).
