# Blog Wiki-Ingest Direct-Patch Variant (Case C2, Aug 2026)

The Case C2 recovery procedure in the main SKILL.md recommends "process takes via parallel
subagents in 2 batches." A validated alternative when the ingest agent already has **all raw
article bodies + target page contents in context** (typical for 3-5 takes):

## When to use direct patching instead of subagents
- 3-5 takes with full article text already read (raw `read_file` output in context)
- Target pages are rich entities you have already read (frontmatter + insertion anchors known)
- You want deterministic anchor checking without subagent self-report verification overhead

## Pattern
1. Write ONE Python script to `/tmp/` via `write_file` (cron-mode rules: `execute_code` blocked,
   heredocs trigger the homoglyph scanner, unique filename per pipeline — e.g. `/tmp/blog_wiki_ingest_20260811.py`).
2. Run via `terminal python3 /tmp/<script>.py`.
3. For every frontmatter/body edit use a count-checking helper:

```python
def replace_once(path, old, new, must=True):
    with open(path, encoding="utf-8") as f:
        content = f.read()
    count = content.count(old)
    if count == 0:
        if must:
            raise SystemExit(f"ANCHOR NOT FOUND in {path}: {old[:80]!r}")
        return False
    if count > 1:
        raise SystemExit(f"ANCHOR AMBIGUOUS ({count}x) in {path}: {old[:80]!r}")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.replace(old, new, 1))
    print(f"OK {os.path.basename(path)}: replaced 1x anchor")
    return True
```

## What the ambiguity guard caught (real case)
Adding a source to `entities/simon-willison.md` frontmatter `sources:` list:
anchor `...--40d193a4.md]` matched **twice** — once in frontmatter (line 10, `md]` + newline)
and once in the body's `Source: [[raw/articles/...40d193a4.md]]` wikilink (line 822, `md]]`).
The `md]` substring is the first bracket of the body's `]]`. Guard raised SystemExit before
corruption.

**Fix**: disambiguate with trailing newline — `...40d193a4.md]\n` matches frontmatter only
(body is `md]]\n`).

See `wiki-entity-enrichment-from-article/references/frontmatter-patch-pitfalls.md` Pitfall 6
for the full write-up including the simon-willison two-`sources:`-lines quirk
(legacy indented `  sources: [...]` ending `--6340f228.md]` + canonical `sources: [...]`
ending `--40d193a4.md]`; `grep -c` on a filename returns 3; always target the canonical line).

## Verification after enrichment
- `grep -n` for each new section header + `grep -c` on each added source filename
  (expected: 2-3 hits — frontmatter + body Source wikilink + possible body mention)
- Run `python3 scripts/validate_index.py` and `.githooks/pre-commit-tag-validator.py` before commit
- Commit with `git add wiki/` + `git commit` + `git push` (split commands, `&` in message → single quotes)
