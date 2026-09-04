# Unclosed Frontmatter (missing closing `---`) — Detection & Fix

Discovered 2026-08-20 during a wiki-watchdog run: 3 pages had frontmatter that
opened with `---` at line 1 but never closed — no second `---` line. The body
(e.g. `# Title` + `**Bold** prose`) got swallowed into the YAML block and
parsing fails. All 3 were bulk-pipeline pages created in the same commit
(2026-05-31): `entities/uipath.md`, `concepts/cursor-automations.md`,
`concepts/mistral-medium-3-5.md` — all with inline-format tags
(`tags: [entity, company, ...]`) on the last frontmatter line.

## Why it evades normal checks

- `wiki_health.py`-style "missing `sources:`" scans use a plain substring
  search over the whole file, so the (present-but-inside-broken-YAML)
  `sources:` field is found and reported clean.
- `head -5` looks fine — the corruption is the *absence* of a line, not a
  visible one.
- Symptom: `grep -c '^---' file.md` returns **1** instead of 2.

## Detection

```python
import re, yaml, os
for subdir in ['entities', 'concepts', 'comparisons', 'events', 'queries']:
    for r, ds, fs in os.walk(f'wiki/{subdir}'):
        for f in fs:
            if not f.endswith('.md'):
                continue
            p = os.path.join(r, f)
            c = open(p).read()
            m = re.match(r'^---\n(.*?)\n---', c, re.S)
            if not m:
                print('UNCLOSED FM:', p)
                continue
            try:
                yaml.safe_load(m.group(1))
            except Exception as e:
                print('YAML ERROR:', p, e)
```

Signature when unclosed: the non-greedy `.*?` stretches to EOF (no closing
`---`), so `yaml.safe_load` receives the entire file and fails on the first
`**` in prose with "while scanning an alias / expected alphabetic or numeric
character, but found '*'".

## Fix

Insert a `---\n` line after the last frontmatter field (typically
`status: active` — check the file, it's not always the last key):

```python
lines = open(p).readlines()
assert lines[7].startswith('status:')  # adjust index to the actual last FM field
lines.insert(8, '---\n')
open(p, 'w').writelines(lines)
```

Verify: (1) `re.match(r'^---\n(.*?)\n---', c, re.S)` matches and `yaml.safe_load`
succeeds; (2) frontmatter contains `title`, `type`, `created`, `updated`,
`tags`, `sources`.

## Pitfalls

- Date sourcing for any follow-up frontmatter fields: bulk-pipeline pages share
  a creation commit — use `git log --diff-filter=A --format='%ai' -- <path>`
  (tail = creation date), not the file mtime.
- Do NOT use the naive `sources:` substring scan as the sources-gap detector —
  it false-negatives on exactly this corruption class. Use the frontmatter
  regex above.
- After fixing, run `python3 scripts/tag_audit.py` + `validate_index.py` —
  unclosed-FM pages sometimes carry tag violations that were invisible while
  the frontmatter was broken.
