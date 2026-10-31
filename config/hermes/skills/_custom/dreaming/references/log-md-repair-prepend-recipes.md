# Canonical log.md Header Repair / Prepend (cron-safe, no execute_code)

Two shapes, both safe against the sibling-prepend corruption states a dreaming
or wiki-ingest run hits (header buried mid-file, DUPLICATE header injected by a
sibling, italic intro line buried deep). Both keep blank-line count stable —
NEVER do a global `re.sub(r'\n{3,}', '\n\n', log)` over the whole file (that
strips thousands of legitimate blank lines; the 2026-08-24 run blew a 16-line
insert into +157/-86).

The skill also ships `repair_log_md_header.py` at
`config/hermes/skills/_custom/dreaming/scripts/repair_log_md_header.py`
(canonical path — NOT repo-root `scripts/`). This note covers the prepend variant.

## Shape A — clean file (exactly one `# Wiki Log` at L1, italic at ~L2): prepend

Write the entry to a time-stamped `/tmp/dreaming_log_<pipeline>_<YYYYMMDD>_<HHMM>.md`
(ASCII body only; em-dashes fine), then:

```python
LOG = "/opt/data/ai-topics/wiki/log.md"; ENTRY = "/tmp/dreaming_log_entry_....md"
lines = open(LOG).read().split("\n")
entry = open(ENTRY).read().strip("\n")
hdrs = [l for l in lines if l.strip() == "# Wiki Log"]
assert len(hdrs) == 1, f"header count {len(hdrs)} — use Shape B"
assert lines[0].strip() == "# Wiki Log" and lines[1].strip().startswith("_Log of all wiki changes")
subj = "## [<date> <hh>:<mm> UTC] dreaming wiki-ingest"   # idempotency guard
assert subj not in "\n".join(lines), "entry already present"
body = "\n".join(lines[2:])
new = lines[0] + "\n" + lines[1] + "\n\n" + entry + "\n\n" + body.lstrip("\n")
open(LOG, "w").write(new)
```

## Shape B — dirty file (header count ≠ 1 OR italic buried): repair + prepend

Triggered when `grep -c '^# Wiki Log'` returns 2 (sibling injected a second
header mid-file, validated 2026-10-29: L1 real + L17 dup, italic buried at L78),
or when `grep -n '^# Wiki Log'` returns 1 but NOT at L1.

```python
LOG = "/opt/data/ai-topics/wiki/log.md"; ENTRY = "/tmp/dreaming_log_entry_....md"
ITALIC = "_Log of all wiki changes. Newest entries at top._"
lines = open(LOG).read().split("\n"); entry = open(ENTRY).read().strip("\n")
stripped = [l.strip() for l in lines]
skip = {i for i,s in enumerate(stripped) if s in ("# Wiki Log", ITALIC)}
rest = [l for i,l in enumerate(lines) if i not in skip]
while rest and rest[0].strip() == "": rest.pop(0)         # LEADING blanks only
new = ["# Wiki Log", "", ITALIC, "", entry, ""] + rest
open(LOG, "w").write("\n".join(new))
```

This strips EVERY header/italic line wherever it sits, rebuilds the head,
prepends the entry, appends the rest. Idempotent on a clean file.

## Post-verify (cheap, no full read)

```bash
grep -n '^# Wiki Log' wiki/log.md     # exactly 1, at L1
grep -n '^_Log of all' wiki/log.md    # ~L3
grep -c '^$' wiki/log.md              # before vs after: delta of a few lines only
grep -c '^## \[<date>' wiki/log.md    # your entry appears once
git diff --stat wiki/log.md           # insertions should DOMINATE a prepend
```
Healthy 2026-10-29 signal: blanks 371→383 for a 31-line entry; diff `+31/-2`.
A large deletion count = over-collapse; `git checkout -- wiki/log.md` and re-run
the (no-collapse) script.

## Concurrency note

A sibling commit can land YOUR entry in HEAD mid-run — after editing, check
`git show HEAD:wiki/log.md | grep -c "<your ascii entry prefix>"`; if already 1,
your job is to DEDUP not re-prepend. Re-verify the worktree right before
committing (the patch tool's "modified since last read" warning is the tell).
