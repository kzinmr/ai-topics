# log.md Prepend & Header Fix — Verified Recipe (2026-11-06 session)

## Context

`wiki/log.md` has a recurring bug: pipelines prepend new entries with `new_entry + content`
WITHOUT leaving the `# Wiki Log` H1 on line 1, burying it at ~line 10 under the prepended entry.
The health-fix cron job (this session 2026-11-06) hit exactly this while prepending its own entry.

## Verified two-pass fix (Python, run via `terminal` + heredoc, NOT `execute_code` in cron mode)

```python
import os, re
p = os.path.expanduser("~/ai-topics/wiki/log.md")

# Pass 0: prepend entry BEFORE fixing header (header fix goes AFTER prepend)
with open(p) as f:
    content = f.read()
if not content.startswith("# Wiki Log"):
    new_entry = "## [YYYY-MM-DD] health-fix | ...\n- ...\n\n---\n\n"
    content = new_entry + content

# Pass 1: delete ALL duplicate header lines, keep first occurrence only.
# Use fullmatch(r'\s*# Wiki Log\s*') — NOT plain == '# Wiki Log' — leading
# whitespace variants exist. This step alone is NOT sufficient: after deleting
# dups, the surviving header may still sit at line ~10 under the prepended entry.
lines = content.split('\n')
keep, seen = [], False
for l in lines:
    if re.fullmatch(r'\s*# Wiki Log\s*', l):
        if seen:
            continue
        seen = True
    keep.append(l)

# Pass 2: MOVE the surviving header to index 0 (this is the step that's easy to miss).
idxs = [i for i, l in enumerate(keep) if re.fullmatch(r'# Wiki Log\s*', l)]
if idxs:
    header = keep.pop(idxs[0])
    keep.insert(0, header)

c = '\n'.join(keep)
assert c.startswith('# Wiki Log')
assert len(re.findall(r'^# Wiki Log\s*$', c, re.M)) == 1
with open(p, 'w') as f:
    f.write(c)
```

## Pitfalls encountered (2026-11-06)

1. **Single assertion `c.count('# Wiki Log') == 1` gives false confidence.** After
   dedup-only (Pass 1), count is 1 but header is buried at line 10 — assertion passes,
   bug remains. ALWAYS assert `c.startswith('# Wiki Log')` as well.

2. **Three sequential failed assertion attempts before the working recipe.** Failed
   patterns: (a) `assert lines[9] == '# Wiki Log'` — positional assumption breaks after
   prepend shifted lines; (b) `marker = "---\n\n# Wiki Log\n"` string splice — assert
   `c2.count(...)==1` fired because the header still existed once at line 10, splice
   didn't produce expected shape; (c) dedup-only pass — see pitfall 1. The fix was to
   locate headers by regex, not position or literal marker strings.

3. **`grep -c '^# Wiki Log'` returned 1 but 3 other lines contain "Wiki Log" as prose**
   (past log entries describing prior header-burial fixes: lines like
   `- log.md: restored buried '# Wiki Log' header ...`). Don't use
   `content.count('# Wiki Log')` as the sole health check — use
   `re.findall(r'^# Wiki Log\s*$', c, re.M)` (anchored, line-level).

4. **`wiki_health.py --json` timeout.** Default `terminal(timeout=60)` is too short —
   the scan timed out at 60s, needed 300s. Use `timeout 300 python3 ...` or set
   `timeout=320` in the terminal call.

5. **Pre-commit + push succeeded cleanly** with:
   `git add wiki/log.md && git commit -m "wiki: ..."` (hooksPath=.githooks active,
   tag validator passes, validate_index.py clean on index.md untouched).

## Canonical commit message pattern

`wiki: health-fix log entry YYYY-MM-DD (all clean) + restore log header to line 1`

When nothing else was fixed and only the header was repositioned, this single-commit
form is correct — the daily-report job is still expected to emit a visible log entry.

## Reference: expected final shape

```
# Wiki Log
## [2026-11-06] health-fix | daily auto-fix scan — all clean, no changes
- ...
- ...

---

## [2026-11-06] watchdog | auto-fix: ...
- ...
```

Header on line 1, immediately followed by the newest entry (no blank line between
header and first `## [` entry — that is the historical format in this repo, preserve it).
