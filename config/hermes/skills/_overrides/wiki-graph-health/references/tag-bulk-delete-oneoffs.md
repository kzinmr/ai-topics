# Bulk-Delete One-Off Non-SCHEMA Tags

When >500 unique non-SCHEMA tags remain after `tag_normalization.py` and >80% are one-off (appear on exactly one page), bulk-delete them before mapping multi-occurrence tags.

## Detection

```python
import os, re
from collections import Counter, defaultdict

wiki = os.path.expanduser('~/ai-topics/wiki')
valid_tags = set()  # populate from SCHEMA.md (see tag_audit.py's load_valid_tags())

file_tags = defaultdict(list)
tag_count = Counter()

for root, dirs, files in os.walk(wiki):
    rel = os.path.relpath(root, wiki)
    if rel.startswith(('.git', 'raw', 'queries', '_archive')):
        continue
    for f in files:
        if not f.endswith('.md') or f in ('index.md', 'log.md', 'log*.md', 'SCHEMA.md'):
            continue
        path = os.path.join(root, f)
        content = open(path).read()

        # Block format: tags:\n  - tag1\n  - tag2
        m = re.search(r'^tags:\s*\n((?:[ \t]*- .*\n?)+)', content, re.MULTILINE)
        if m:
            for line in m.group(1).split('\n'):
                ls = line.strip()
                if ls.startswith('- '):
                    tag = ls[2:].strip().strip('"\'').strip()
                    if tag and tag not in valid_tags:
                        file_tags[path].append(tag)
                        tag_count[tag] += 1
        else:
            # Inline format: tags: [tag1, tag2]
            m2 = re.search(r'^tags:\s*\[(.+)\]', content, re.MULTILINE)
            if m2:
                for t in m2.group(1).split(','):
                    tag = t.strip().strip('"\'').strip()
                    if tag and tag not in valid_tags:
                        file_tags[path].append(tag)
                        tag_count[tag] += 1
```

## Bulk Removal

Delete only one-off tags (count == 1). Handle both block and inline formats:

```python
for path, bad_tags in sorted(file_tags.items()):
    one_offs = [t for t in bad_tags if tag_count[t] == 1]
    if not one_offs:
        continue
    with open(path) as fh:
        content = fh.read()

    m = re.search(r'^tags:\s*\n((?:[ \t]*- .*\n?)+)', content, re.MULTILINE)
    if m:
        block = m.group(1)
        kept = [l for l in block.split('\n')
                if not (l.strip().startswith('- ') and
                        l.strip()[2:].strip().strip('"\'').strip() in one_offs)]
        kept_lines = [l for l in kept if l.strip()]
        if kept_lines:
            content = content.replace(block, '\n'.join(kept_lines) + '\n', 1)
        else:
            content = re.sub(r'^tags:\s*\n(?:[ \t]*- .*\n?)+', 'tags: []\n', content, 1, re.MULTILINE)
    else:
        m2 = re.search(r'^tags:\s*\[(.+)\]', content, re.MULTILINE)
        if m2:
            all_tags = [t.strip().strip('"\'').strip() for t in m2.group(1).split(',')]
            kept = [t for t in all_tags if t not in one_offs]
            new_val = ', '.join(kept) if kept else ''
            content = content.replace(f'tags: [{m2.group(1)}]', f'tags: [{new_val}]', 1)

    with open(path, 'w') as fh:
        fh.write(content)
```

## Verification

After bulk-delete, re-run `tag_audit.py`. If 0-5 violations remain, they're likely `_index.md` inline-format tags needing individual handling.

### Assertion Pitfall

Verify against the `tags:` line specifically, not the entire file content:
```python
tags_line = re.search(r'^tags:\s*\[(.+)\]', content, re.MULTILINE)
assert tags_line and 'offending-tag' not in tags_line.group(1)
```

### Heuristic

If unique non-SCHEMA tags > 500 and >80% are one-offs, bulk-delete first. In the 2026-05-11 session this removed 913 one-off tags from 847 files in one pass. In the 2026-05-25 session, all 199 were one-offs — removed from 89 files.
