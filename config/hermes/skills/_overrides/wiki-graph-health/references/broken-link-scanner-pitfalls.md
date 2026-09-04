# Broken-Wikilink Scanner — Corrected Version & Pitfalls

Canonical corrected scanner for the wiki-graph-health §4 Sub-pattern C
"find genuinely missing pages" analysis. Two pitfalls were discovered live
during the 2026-08-06 watchdog run — both were bugs in the skill's own
inline script and produced garbage numbers.

## Pitfall 1: Path-normalization bug (CRITICAL)

The old inline script built `existing` like this:

```python
existing = set()
for root, dirs, files in os.walk('wiki'):
    for f in files:
        existing.add(os.path.splitext(f)[0])
```

`os.walk('wiki')` yields paths like `wiki/entities/foo.md`, so
`os.path.splitext(f)[0]` → `wiki/entities/foo` (WITH the `wiki/` prefix).
Wikilink slugs are `entities/foo` (WITHOUT the prefix). Result: **every
prefix-style link appears missing** — observed 6,260 phantom refs / 0 REAL
missing. The wiki looked 100% broken. Fix: normalize to the wiki root with
`os.path.relpath`.

## Pitfall 2: Dir-index resolution (`dir/_index.md`)

Links like `[[concepts/post-training]]` are **VALID** when
`concepts/post-training/_index.md` exists. The old scanner reported them as
missing because the flat file `concepts/post-training.md` doesn't exist.

Confirmed `_index.md` subdirectories (2026-08-06):
`post-training`, `coding-agents`, `multi-agents`, `security-and-governance`,
`evaluation`, `harness-engineering`, `local-llm` — and this list grows as
new topic dirs are created.

Without handling this, `[[concepts/post-training]]` (14 refs in 2026-08-06
scan) and similar dir links falsely report as broken.

## Corrected Scanner (use this)

```python
import re, glob, os
from collections import Counter
all_links = []
for f in (glob.glob('wiki/entities/*.md') + glob.glob('wiki/concepts/*.md')
          + glob.glob('wiki/comparisons/*.md') + glob.glob('wiki/events/*.md')
          + glob.glob('wiki/queries/*.md')):
    with open(f) as fh:
        for m in re.findall(r'\[\[([^\]|]+)', fh.read()):
            all_links.append(m)

existing = set()
for root, dirs, files in os.walk('wiki'):
    for f in files:
        # Must be relative to wiki/ root — see Pitfall 1
        rel = os.path.splitext(os.path.relpath(os.path.join(root, f), 'wiki'))[0]
        existing.add(rel)
        # Dir-index resolution — see Pitfall 2
        if f.startswith('_index'):
            existing.add(rel.rsplit('/', 1)[0])

missing = Counter()
for l in all_links:
    slug = l.split('#')[0].split('|')[0]
    if slug not in existing:
        missing[l] += 1

real, prefix_ns = Counter(), Counter()
for m, count in missing.most_common(300):
    is_prefix = m.startswith(('entities/', 'concepts/', 'comparisons/',
                              'raw/', 'queries/', 'events/'))
    is_arxiv = (m[:2].isdigit() and len(m) <= 12)
    if is_prefix:
        prefix_ns[m] += count
    elif not is_arxiv:
        real[m] += count

print(f'Total unique missing targets: {len(missing)}  (refs: {sum(missing.values())})')
print(f'  prefix-style: {sum(prefix_ns.values())} refs, {len(prefix_ns)} unique')
print(f'  REAL bare/missing: {sum(real.values())} refs, {len(real)} unique')
for m, count in real.most_common(60):
    print(f'{count:3d}x  [[{m}]]')
```

## 2026-08-06 Reference Output (sanity baseline)

After the fix, on the live wiki (~2,894 L2 pages):
- Prefix-style misses: ~1,530 refs / 750 unique — these are namespace errors
  (`[[entities/dspy]]` → `concepts/dspy`), subdir/flat confusion
  (`[[concepts/claude-code/claude-code]]` → `entities/claude-code`), and
  genuinely-missing entity stubs. Needs a >10-file batch pass → ESCALATE,
  do not auto-fix in watchdog.
- REAL bare/missing: ~219 refs / 67 unique (top: `grpo` 13, `reinforcement-learning`
  11, `verifiers-rl` 7, `echo-rl` 7, `enterprise-ai` 6, `cursor` 3, `rag` 4,
  `reasoning` 4). Includes case-sensitivity false positives
  (`[[Cerebras Systems]]` → `entities/cerebras-systems`, `[[Hack Club]]` →
  `concepts/hack-club`) — try case-insensitive matching before reporting.

## Verification pattern for index.md ghost scans

The same relpath rule applies to the index-ghost check: slugs in index.md are
`entities/foo` relative to `wiki/`, so compare against
`os.path.splitext(os.path.relpath(path, 'wiki'))[0]`, not the raw walked path.
