# Bare Wikilink → Prefixed Wikilink Batch Fix

Full procedure and worked example from the 2026-05-08 wiki-graph-analysis remediation session.

## Background

The wiki uses subdirectories (`entities/`, `concepts/`, `comparisons/`) but many wikilinks were created as bare `[[slug]]` without namespace prefixes. These don't resolve because `entities/slug.md` and `concepts/slug.md` are the actual file paths.

## Detection

```python
import re, os
from collections import Counter

wiki = "/opt/data/ai-topics/wiki"
existing = set()
for root, dirs, files in os.walk(wiki):
    for f in files:
        if f.endswith('.md'):
            rel = os.path.relpath(os.path.join(root, f), wiki)
            existing.add(rel[:-3].lower())

missing = Counter()
for root, dirs, files in os.walk(wiki):
    for f in files:
        if f.endswith('.md'):
            path = os.path.join(root, f)
            with open(path) as fh:
                for m in re.findall(r'\[\[([^\]|]+)', fh.read()):
                    slug = m.split('#')[0].split('|')[0].strip()
                    if slug.lower() not in existing:
                        missing[m] += 1

# Filter: real broken = not subdirectory-prefixed, not arxiv ID, not regex artifact
real = [(c,m) for m,c in missing.most_common(100)
        if not m.startswith(('entities/', 'concepts/', 'comparisons/', 'queries/', 'raw/', 'events/'))
        and not (m[:2].isdigit() and len(m) <= 12)]
```

## Mapping Slugs to Namespaces

```python
import os

wiki = "/opt/data/ai-topics/wiki"
for slug in broken_bare_slugs:
    entity_path = os.path.join(wiki, "entities", slug + ".md")
    concept_path = os.path.join(wiki, "concepts", slug + ".md")
    locs = []
    if os.path.exists(entity_path): locs.append("entities")
    if os.path.exists(concept_path): locs.append("concepts")
    prefix = locs[0] if locs else "MISSING"
```

**Rule for entity+concept ambiguity**: If a slug exists in BOTH, prefer `entities/` for person/org names, `concepts/` for topic names. If unsure, use whichever has more content (check `os.path.getsize()`).

## Batch Fix Application

Process in batches of 25-30 slugs. Each batch walks all wiki `.md` files once:

```python
import re, os

wiki = "/opt/data/ai-topics/wiki"
fix_map = {
    "simon-willison": "entities/simon-willison",
    "openai": "entities/openai",
    "anthropic": "entities/anthropic",
    # ... 25-30 entries per batch
}

files_changed = 0
for root, dirs, files in os.walk(wiki):
    for f in files:
        if not f.endswith('.md'): continue
        path = os.path.join(root, f)
        with open(path) as fh: content = fh.read()
        new_content = content
        for bare, prefixed in fix_map.items():
            new_content = re.sub(r'\[\[' + re.escape(bare) + r'\]\]', '[[' + prefixed + ']]', new_content)
            new_content = re.sub(r'\[\[' + re.escape(bare) + r'\|', '[[' + prefixed + '|', new_content)
        if new_content != content:
            with open(path, 'w') as fh: fh.write(new_content)
            files_changed += 1
```

## 2026-05-08 Session Results

| Batch | Slugs Fixed | Files Changed | Broken Links Remaining |
|-------|-------------|---------------|----------------------|
| Start | — | — | 331 unique (939 refs) |
| 1 | 29 (simon-willison, openai, anthropic, ...) | 233 | 97 unique (373 refs) |
| 2 | 19 (china-ai-industry, nathan-lambert, ...) | 117 | 49 unique (206 refs) |
| 3 | 27 (unitree-robotics, dwarkesh-patel, ...) | 117 | 29 unique (133 refs) |
| 4 | 33 (sankalp-sinha, jarred-sumner, ...) | 96 | 35 unique (188 refs) |
| 5 | 27 (walden-yan, agentic-security, ...) | 69 | 32 unique (108 refs) |
| 6 | 29 (agi-bot, anildash, arize, ...) | 62 | — (remaining are code artifacts) |

**Remaining artifacts after fix (DO NOT FIX THESE):**
- `17x [[`:alnum:`]]` — POSIX regex character class in code block
- `8x [[`:space:`]]` — POSIX regex character class in code block
- `[[gnu::packed]]`, `[[fallthrough]]` — C++ attribute syntax
- `[[wikilinks]]` — prose reference, not link target

## Pitfalls

1. **Regex artifacts**: `[[:alnum:]]` and `[[:space:]]` match the wikilink regex `[[...]]` but are POSIX character classes in code blocks. Adding them to fix_map would corrupt the code. Always manually verify top offenders before adding to fix_map.

2. **Display text preservation**: `[[slug|Display Text]]` must become `[[entities/slug|Display Text]]`, not lose the display text. The second `re.sub` pattern handles this.

3. **Batch size**: 25-30 slugs per batch is optimal. Larger batches risk excessive file writes; smaller batches require more re-scans.

4. **Commit after every 2-3 batches**: Don't wait until all batches are done. Incremental commits make it easier to revert if a batch has an issue.
