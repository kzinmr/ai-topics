# Comprehensive Single-Pass Graph Analysis

When running a full wiki health audit, avoid calling 5+ separate scripts in sequence.
A single `execute_code` call can scan all pages once and produce a structured report.

## Why Single-Pass?

Sequential script calls (`wiki_health.py --json`, then orphan scan, then tag audit, then
frontmatter validation, then index reconciliation) waste tokens and time re-reading the
same files. A single Python script reads each `.md` file once, extracts all metadata
and links, then performs all analyses against the collected data.

## Full Scan Script

```python
import os, re, json
from collections import defaultdict, Counter

wiki = '/opt/data/ai-topics/wiki'
results = {
    'pages': {},
    'broken_links': [],
    'orphans': [],
    'duplicates': [],
    'index_gaps': [],
    'frontmatter_issues': [],
    'tag_violations': [],
    'stale_pages': [],
    'oversized_pages': []
}

# 1. Read SCHEMA.md for canonical tags
with open(os.path.join(wiki, 'SCHEMA.md')) as f:
    schema_content = f.read()
# Parse taxonomy from schema (handle both backtick and bullet formats)
canonical_tags = set()
for line in schema_content.split('\n'):
    # Backtick format: `tag-name`
    canonical_tags.update(re.findall(r'`([a-z][a-z0-9-]+)`', line))
    # Bullet format: - **Category**: tag1, tag2
    if re.match(r'^- \*\*', line):
        parts = line.split(':', 1)
        if len(parts) == 2:
            canonical_tags.update(t.strip() for t in parts[1].split(','))

# 2. Single pass over all L2 pages
for subdir in ['entities', 'concepts', 'comparisons', 'queries', 'events']:
    dir_path = os.path.join(wiki, subdir)
    if not os.path.isdir(dir_path): continue
    for f in os.listdir(dir_path):
        if not f.endswith('.md'): continue
        path = os.path.join(dir_path, f)
        try:
            with open(path) as fh: content = fh.read()
        except: continue
        
        slug = f.replace('.md', '')
        key = f"{subdir}/{slug}"
        
        # Extract frontmatter
        fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        has_frontmatter = bool(fm_match)
        tags = []
        sources = None
        page_type = None
        created = None
        updated = None
        
        if fm_match:
            fm = fm_match.group(1)
            tags = [t.strip() for t in re.findall(r'- ([a-z][a-z0-9-]+)', fm) if t.strip() not in ('title', 'type', 'created', 'updated', 'sources')]
            # Handle inline format: tags: [tag1, tag2]
            inline_tags = re.search(r'tags:\s*\[([^\]]+)\]', fm)
            if inline_tags:
                tags = [t.strip() for t in inline_tags.group(1).split(',')]
            
            for field in ['sources', 'type', 'created', 'updated']:
                m = re.search(f'^{field}:\s*(.+)$', fm, re.MULTILINE)
                if m: globals()[field] = m.group(1).strip()
        
        # Extract wikilinks
        wikilinks = re.findall(r'\[\[([^\]|]+)', content)
        
        # Store page data
        results['pages'][key] = {
            'path': path,
            'size': len(content),
            'lines': content.count('\n'),
            'tags': tags,
            'sources': sources,
            'type': page_type,
            'created': created,
            'updated': updated,
            'has_frontmatter': has_frontmatter,
            'wikilinks': wikilinks
        }
        
        # Check frontmatter issues
        missing = []
        if not has_frontmatter: missing.append('frontmatter')
        if sources is None: missing.append('sources')
        if page_type is None: missing.append('type')
        if created is None: missing.append('created')
        if updated is None: missing.append('updated')
        if missing:
            results['frontmatter_issues'].append({
                'page': key, 'missing': missing
            })
        
        # Check tag violations
        non_canonical = [t for t in tags if t and t not in canonical_tags]
        if non_canonical:
            results['tag_violations'].append({
                'page': key, 'tags': non_canonical
            })
        
        # Check oversized pages
        if content.count('\n') > 200:
            results['oversized_pages'].append({
                'page': key, 'lines': content.count('\n')
            })

# 3. Build link graph (inbound/outbound)
inbound = defaultdict(list)
all_slugs = set(results['pages'].keys())

for key, data in results['pages'].items():
    for link in data['wikilinks']:
        # Normalize link target
        target = link.split('#')[0].split('|')[0].strip()
        inbound[target].append(key)

# 4. Find orphans (no inbound links, excluding _index)
for key in results['pages']:
    if key.endswith('/_index'): continue
    if not inbound.get(key):
        # Check if page has substantive content
        size = results['pages'][key]['size']
        category = 'content-rich' if size > 500 else 'skeleton' if size > 100 else 'minimal'
        results['orphans'].append({
            'page': key,
            'category': category,
            'outbound': len(results['pages'][key]['wikilinks'])
        })

# 5. Find broken links
for key, data in results['pages'].items():
    for link in data['wikilinks']:
        target = link.split('#')[0].split('|')[0].strip()
        # Skip code artifacts
        if target.startswith(':') or target.startswith('['): continue
        if target in ('wikilinks', 'index'): continue
        
        # Check if target exists
        if target not in all_slugs:
            # Check cross-namespace
            parts = target.split('/')
            if len(parts) == 2:
                ns, slug = parts
                other_ns = 'concepts' if ns == 'entities' else 'entities'
                other_target = f"{other_ns}/{slug}"
                if other_target in all_slugs:
                    results['broken_links'].append({
                        'source': key,
                        'link': f'[[{target}]]',
                        'issue': f'cross-namespace: should be [[{other_target}]]',
                        'fix': other_target
                    })
                else:
                    results['broken_links'].append({
                        'source': key,
                        'link': f'[[{target}]]',
                        'issue': 'missing',
                        'fix': None
                    })
            else:
                # Bare wikilink
                results['broken_links'].append({
                    'source': key,
                    'link': f'[[{target}]]',
                    'issue': 'bare-wikilink',
                    'fix': None
                })

# 6. Index reconciliation
with open(os.path.join(wiki, 'index.md')) as f:
    index_content = f.read()
index_entries = set(re.findall(r'\[\[(entities|concepts|comparisons|queries|events)/([^|\]]+)', index_content))
index_entries = {f"{cat}/{slug.strip()}" for cat, slug in index_entries}

not_indexed = all_slugs - index_entries
not_on_disk = index_entries - all_slugs
results['index_gaps'] = {
    'not_indexed': sorted(list(not_indexed)),
    'not_on_disk': sorted(list(not_on_disk)),
    'gap_count': len(not_indexed)
}

# 7. Duplicate detection
duplicates = defaultdict(list)
for f in os.listdir(os.path.join(wiki, 'entities')):
    if f.endswith('.md'):
        normalized = f.replace('.md', '').lower().replace('-', '').replace('_', '')
        duplicates[normalized].append(f.replace('.md', ''))
results['duplicates'] = {k: v for k, v in duplicates.items() if len(v) > 1}

# 8. Output report
print(json.dumps(results, indent=2))
```

## Usage Pattern

Run as a single `execute_code` call at the start of any wiki health session.
The output is a structured JSON report that can be processed programmatically
or used to guide manual fixes.

## Key Metrics Tracked

- `pages`: Total L2 page count and metadata
- `broken_links`: Links that don't resolve (with cross-namespace detection)
- `orphans`: Pages with no inbound links (categorized by content richness)
- `duplicates`: Entity pages with hyphen-stripped name collisions
- `index_gaps`: Pages on disk not in index.md (and vice versa)
- `frontmatter_issues`: Pages missing required metadata fields
- `tag_violations`: Pages using non-canonical tags
- `stale_pages`: Pages not updated in >90 days (if `updated` field present)
- `oversized_pages`: Pages exceeding 200 lines (split candidates)

## 2026-05-22 Baseline

- **474 orphan pages**: 323 content-rich, 149 skeleton/stub, 2 minimal
- **753 index gaps (38%)**: concepts (632), entities (120), comparisons (1)
- **20 cross-namespace mismatches**: entities↔concepts confusion
- **760 pages missing `sources:`**: systemic gap, set to `[]` if no source
- **47 pages >200 lines**: candidates for splitting