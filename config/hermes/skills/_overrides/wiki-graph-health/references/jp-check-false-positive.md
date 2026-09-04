# Pre-Commit JP Check False Positive on log.md (fixed 2026-08-03)

Session detail: wiki-watchdog-fix run, 2026-08-03. A legitimate watchdog commit
(restoring `# Wiki Log` header + index header count corrections) was blocked by
`.githooks/pre-commit-jp-check.py`:

```
❌ BLOCKED: Japanese content introduced to previously clean files:
   NEW Japanese introduced to clean file: wiki/log.md
```

## Root cause — hook bug, not a real violation

`count_jp()` in `pre-commit-jp-check.py` used the first two `---` lines as YAML
frontmatter boundaries:

```python
for i, line in enumerate(lines):
    if line.strip() == '---':
        fm_count += 1
        if fm_count == 2:
            body_start = i + 1
            break
body = '\n'.join(lines[body_start:])
```

In `log.md`, `---` lines are **entry separators / horizontal rules**, not
frontmatter. The JP content (a blog-triage summary table in Japanese) sat BEFORE
the second `---` separator in HEAD but AFTER it in the staged version once entry
positions shifted. Result: `before(HEAD) = 0` but `after(staged) = 48` →
position-dependent false positive. The same 48 JP chars were already committed
in HEAD (`git show HEAD:wiki/log.md` confirmed the table at line 65).

## Debugging path (reuse this)

1. **Don't `--no-verify` immediately.** Verify the claim with git:
   ```bash
   git diff --cached wiki/log.md | grep -P '[\x{3040}-\x{30FF}\x{4E00}-\x{9FFF}]'
   # empty → the diff itself introduces no JP
   git show HEAD:wiki/log.md > /tmp/log_head.md
   grep -n 'ソース' /tmp/log_head.md   # JP table ALREADY in HEAD
   ```
2. **Run the hook's exact count logic** on HEAD vs staged to find the asymmetry:
   ```python
   # body_start lands at the 2nd `---` line; JP before it is skipped for HEAD,
   # counted for staged → before=0, after=48
   ```
3. **Check when the hook was added** relative to the JP content:
   ```bash
   git log --oneline -3 -- .githooks/pre-commit-jp-check.py
   git merge-base --is-ancestor <hook-commit> HEAD && echo "hook predates content"
   ```
   Content pre-existing in HEAD ⇒ the block is a false positive.

## Fix (applied to the repo hook)

Only treat the first two `---` lines as frontmatter when the file **actually
starts with** `---`:

```python
lines = content.split('\n')
if lines and lines[0].strip() == '---':
    body_start = 0
    fm_count = 0
    for i, line in enumerate(lines):
        if line.strip() == '---':
            fm_count += 1
            if fm_count == 2:
                body_start = i + 1
                break
    body = '\n'.join(lines[body_start:])
else:
    body = content   # log.md / log-2026.md / index.md: count whole file
return len(JP_PATTERN.findall(body))
```

After the fix, body-less files (log.md, index.md, log-2026.md) are counted
whole, so HEAD/staged JP counts are position-independent. Commits pass without
`--no-verify` when JP count is unchanged; genuine NEW JP still blocks, and JP
increase in backlog files still warns.

## Verification after fix

```bash
python3 .githooks/pre-commit-jp-check.py && echo "HOOK EXIT=$?"   # 0 = pass
# Whole-file JP count must be identical for HEAD and staged version when the
# diff introduces no JP: git show HEAD:wiki/log.md vs working tree count.
```

## Rules of thumb

- JP chars appearing in `log.md` from pipeline entries (blog-triage tables,
  newsletter-triage summaries) are **legitimate pre-existing content** — the
  user-facing triage tables are intentionally Japanese. Do NOT delete them, and
  do NOT `--no-verify` to force them out.
- If the JP check blocks and the diff adds no JP, it's a hook miscount — fix the
  hook, don't bypass it. `--no-verify` also skips `validate_index.py` and tag
  validation, so it should only be the last resort.
