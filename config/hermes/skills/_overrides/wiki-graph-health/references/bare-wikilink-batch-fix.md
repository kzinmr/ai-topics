# Bare Wikilink Batch Fix

When a wiki accumulates bare wikilinks (e.g., `[[openai]]`, `[[simon-willison]]`) that lack namespace prefixes, fixing them one-by-one with `patch` is prohibitively slow. Use this batch approach instead.

## The Pattern

Bare wikilinks are wikilinks without `entities/` or `concepts/` namespace prefixes. At scale (300+ bare links across 1,100+ files), they must be fixed programmatically, not manually.

## Three-Phase Batch Fix

### Phase 1: Scan & Map

Scan all wiki files for bare wikilinks, check whether each slug exists as entity or concept, build a fix_map:

```python
import re, os
from collections import Counter

wiki = "/opt/data/ai-topics/wiki"
existing = set()
for root, dirs, files in os.walk(wiki):
    for f in files:
        if f.endswith('.md'):
            rel = os.path.relpath(os.path.join(root, f), wiki)
            existing.add(rel[:-3].lower())  # strip .md

# Find bare links (no namespace prefix)
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

# Filter: real broken = no namespace prefix + not regex artifact + not arxiv ID
real = [(c,m) for m,c in missing.most_common(100) 
        if not m.startswith(('entities/', 'concepts/', 'comparisons/', 'queries/', 'raw/', 'events/'))
        and not (m[:2].isdigit() and len(m) <= 12)
        and m not in (':alnum:', ':space:')]
```

### Phase 2: Resolve Slugs → Paths

For each bare slug, check whether an entity or concept file exists:

```python
fix_map = {}
for slug in bare_slugs:
    entity_path = os.path.join(wiki, "entities", slug + ".md")
    concept_path = os.path.join(wiki, "concepts", slug + ".md")
    comparison_path = os.path.join(wiki, "comparisons", slug + ".md")
    
    if os.path.exists(entity_path):
        fix_map[slug] = f"entities/{slug}"
    elif os.path.exists(concept_path):
        fix_map[slug] = f"concepts/{slug}"
    elif os.path.exists(comparison_path):
        fix_map[slug] = f"comparisons/{slug}"
    else:
        print(f"SKIP: [[{slug}]] — no file found (needs stub creation)")
```

**CRITICAL**: If a slug exists in BOTH `entities/` and `concepts/` (entity/concept duplicate), prefer `concepts/` for general topics and `entities/` for person/org/product names. Check the page content if uncertain.

### Phase 3: Batch Replace

Apply all replacements in one pass across all wiki files:

```python
import re

files_changed = 0
for root, dirs, files in os.walk(wiki):
    # Skip raw/ directory
    if 'raw/' in root:
        continue
    for f in files:
        if not f.endswith('.md'):
            continue
        path = os.path.join(root, f)
        with open(path) as fh:
            content = fh.read()
        
        new_content = content
        for bare, prefixed in fix_map.items():
            # Replace [[bare]] → [[prefixed]]
            pattern = r'\[\[' + re.escape(bare) + r'\]\]'
            new_content = re.sub(pattern, '[[' + prefixed + ']]', new_content)
            # Replace [[bare|display]] → [[prefixed|display]]
            pattern2 = r'\[\[' + re.escape(bare) + r'\|'
            new_content = re.sub(pattern2, '[[' + prefixed + '|', new_content)
        
        if new_content != content:
            with open(path, 'w') as fh:
                fh.write(new_content)
            files_changed += 1

print(f"Fixed {files_changed} files")
```

## Batch Processing Strategy

Process in batches of ~30 slugs per pass. This reduces regex complexity and makes verification easier:

1. **Batch 1**: Top 30 most-referenced bare links (score ≥ 8 refs)
2. **Batch 2**: Next 30 (score 5-7 refs)
3. **Batch 3**: Remaining (score < 5 refs)
4. **After each batch**: Re-run the scan script to verify broken links are decreasing

## Expected Results

At a 1,750-page wiki with ~300 bare wikilinks:
- **Before**: 97 unique bare broken links, ~939 total references
- **After 3 batches**: <10 real broken links (remaining are code artifacts)
- **Files touched per batch**: 50-120 files
- **Time**: ~5-10 seconds per batch (execute_code)

## False Positives to Ignore

These are NOT real wikilinks and should NOT be "fixed":

| Pattern | Source | Example |
|---------|--------|---------|
| `[[:alnum:]]` | POSIX regex character class in code blocks | `17x [[:alnum:]]` |
| `[[:space:]]` | POSIX regex character class in code blocks | `8x [[:space:]]` |
| `[[gnu::packed]]` | C++ attribute syntax `[[gnu::packed]]` | Seen in compiler articles |
| `[[fallthrough]]` | C++17 attribute `[[fallthrough]]` | Seen in code examples |
| `[[wikilinks]]` | Generic markdown documentation term | Usually not intended as actual link |

**Detection tip**: These typically have 3 references each (from the same code block copied across 3 pages) and look "technical" rather than topical.
