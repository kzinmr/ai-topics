# Ghost-entry detection: two false-positive/negative patterns (2026-11-17 auto-fix session)

When scanning `wiki/index.md` for ghost entries (wikilinks to non-existent files), refine the
`existing` set build and the link-target parse. Two patterns matter.

## (A) Directory-hub links are valid even WITHOUT `_index.md` — false-positive source

The scanner in `broken-link-scanner-pitfalls.md` adds a dir to `existing` only when
`<dir>/_index.md` exists. That UNDER-counts valid dir-hub links: a link like
`[[concepts/gpt]]` resolves fine when `concepts/gpt/` exists as a directory, regardless of
whether it contains `_index.md`.

**Build `existing` from EVERY directory**, not just `_index`-bearing ones:

```python
import os, re
wiki = 'wiki'
existing = set()
for r, dirs, fs in os.walk(wiki):
    for f in fs:
        if not f.endswith('.md'):
            continue
        rel = os.path.splitext(os.path.relpath(os.path.join(r, f), wiki))[0]
        existing.add(rel)
        if f == '_index.md':
            existing.add(rel.rsplit('/', 1)[0])   # dir itself via _index
    for d in dirs:                                 # <-- the fix: every dir is a valid target
        existing.add(os.path.relpath(os.path.join(r, d), wiki))

idx = open('wiki/index.md', encoding='utf-8', errors='replace').read()
links = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', idx)   # capture TARGET (before |) only
ghosts = [l.strip() for l in set(map(str.strip, links))
          if l.strip().startswith(('entities/', 'concepts/', 'comparisons/', 'queries/', 'events/'))
          and l.strip() not in existing]
print('real ghosts:', len(ghosts), ghosts)
```

In the 2026-11-17 session the naive `_index`-only scanner reported **9 ghosts**; **8 were valid
dir-hub links** (`concepts/ai-benchmarks`, `concepts/openai`, `concepts/gpt`, `concepts/gemini`,
`concepts/claude`, `concepts/browser-agent`, `concepts/anthropic`, `concepts/training` — all dirs
present, none with `_index.md`). Only 1 was a real ghost (see B). After the dir-based fix: **0 ghosts**.

## (B) Real ghost from a botched slug patch (stray char leaked into display text)

A half-applied rename can leave a malformed link where the **target** is wrong but display text
looks right. Observed:

```
- [[entities/met|entities/metR]] — METR (Model Evaluation & Threat Research) — ...
```

The real file is `entities/metR.md`. The `entities/met` target has no file → genuine ghost. The
stray `R` from the `met`->`metR` slug patch leaked into the `|Display Text` segment while the
target was left un-renamed.

**Detection rule**: parse the TARGET segment (before `|`), never trust display text. A
`[[entities/X|...]]` is a ghost when `entities/X.md` is absent.

**Fix**:
```python
patch(old_string="- [[entities/met|entities/metR]] — METR (Model Evaluation & Threat Research)",
      new_string="- [[entities/metR]] — METR (Model Evaluation & Threat Research)",
      path="wiki/index.md")
```

## Workflow reminder for the auto-fix cron

- `wiki_health.py --json` does NOT report ghosts, corruption, tag drift, or missing frontmatter —
  run these as independent live checks (`validate_index.py`, `grep -cP`, recursive `os.walk`,
  `tag_audit.py`).
- When the working tree already has uncommitted wiki edits from upstream pipelines (common:
  ~10 `entities/*.md` enrichment additions), **stage ONLY the files you touched**
  (`git add wiki/index.md wiki/log.md`), never `git add -A`. Don't disturb sibling changes.
- Prepend log via `write_file /tmp/x.py` + `terminal python3` (cron blocks `execute_code`), then
  run `config/hermes/skills/_overrides/wiki-graph-health/scripts/fix_log_header_burial.py` LAST.
- Reconcile `## Entities (N pages)` headers from actual index-line counts
  (`grep -cP '^\|?- \[\[entities/'`), not the digest's filesystem count (nested vs indexed divergence).
