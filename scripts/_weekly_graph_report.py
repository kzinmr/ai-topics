#!/usr/bin/env python3
"""Generate weekly wiki graph analysis report and save to wiki/queries/."""
import os, re, json
from datetime import datetime, timezone
from collections import Counter

wiki = '/opt/data/ai-topics/wiki'

# 1. Read SCHEMA.md for canonical tags
with open(os.path.join(wiki, 'SCHEMA.md')) as f:
    schema_text = f.read()

canonical_tags = set()
idx = schema_text.find('## Tag Taxonomy')
if idx >= 0:
    tax = schema_text[idx:]
    canonical_tags.update(re.findall(r'`([a-z][a-z0-9-]+)`', tax))
    for line in tax.split('\n'):
        if line.strip().startswith('- **') and ':' in line:
            body = line.split(':', 1)[1]
            items = [t.strip().rstrip('.') for t in body.split(',')]
            for item in items:
                if re.match(r'^[a-z][a-z0-9-]+$', item):
                    canonical_tags.add(item)

# 2. Scan all L2 pages
pages = {}
orphans = []
broken_links = []
no_sources = []
skeletons = []
tag_violations = []
oversized = []
stale = []

for subdir in ['entities', 'concepts', 'comparisons', 'queries', 'events']:
    dp = os.path.join(wiki, subdir)
    if not os.path.isdir(dp):
        continue
    for fn in sorted(os.listdir(dp)):
        if not fn.endswith('.md'):
            continue
        path = os.path.join(dp, fn)
        try:
            with open(path, encoding='utf-8', errors='replace') as fh:
                content = fh.read()
        except:
            continue
        slug = fn.replace('.md', '')
        key = f'{subdir}/{slug}'
        lines = content.split('\n')
        fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        tags, sources, page_type, updated, status = [], None, None, None, None
        has_fm = bool(fm_match)
        if fm_match:
            fm = fm_match.group(1)
            in_tags = False
            for line in fm.split('\n'):
                km = re.match(r'^(\w+):', line)
                if km:
                    in_tags = (km.group(1) == 'tags')
                if in_tags:
                    tm = re.match(r'^\s*-\s+([a-z][a-z0-9-]+)', line)
                    if tm:
                        tags.append(tm.group(1))
            inline = re.search(r'tags:\s*\[([^\]]+)\]', fm)
            if inline:
                tags = [t.strip() for t in inline.group(1).split(',') if t.strip()]
            for field in ['sources', 'type', 'updated', 'status']:
                m = re.search(r'^' + field + r':\s*(.+)$', fm, re.MULTILINE)
                if m:
                    v = m.group(1).strip()
                    if field == 'sources':
                        sources = v
                    elif field == 'type':
                        page_type = v
                    elif field == 'updated':
                        updated = v
                    elif field == 'status':
                        status = v

        wikilinks = re.findall(r'\[\[([^\]|]+)', content)
        pages[key] = {
            'path': path, 'size': len(content), 'lines': len(lines),
            'tags': tags, 'sources': sources, 'type': page_type,
            'updated': updated, 'status': status, 'has_fm': has_fm,
            'wikilinks': wikilinks, 'subdir': subdir
        }

        if sources is None or sources == '':
            no_sources.append(key)
        if status == 'skeleton':
            skeletons.append(key)
        non_canon = [t for t in tags if t and t not in canonical_tags]
        if non_canon:
            tag_violations.append({'page': key, 'tags': non_canon})
        if len(lines) > 200:
            oversized.append({'page': key, 'lines': len(lines)})
        if updated:
            try:
                upd = datetime.strptime(updated[:10], '%Y-%m-%d').replace(tzinfo=timezone.utc)
                days = (datetime.now(timezone.utc) - upd).days
                if days > 90:
                    stale.append({'page': key, 'updated': updated, 'days': days})
            except ValueError:
                pass

# 3. Build inbound link graph
all_slugs = set(pages.keys())
inbound = {}
for key, data in pages.items():
    for link in data['wikilinks']:
        tgt = link.split('#')[0].split('|')[0].strip()
        if tgt:
            inbound.setdefault(tgt, []).append(key)

# 4. Orphans
for key in sorted(pages.keys()):
    if key.endswith('/_index'):
        continue
    has_in = any(key in targets for targets in inbound.values())
    if not has_in:
        data = pages[key]
        if data['lines'] >= 20 or data['size'] >= 500:
            cat = 'content-rich'
        elif data['lines'] >= 5:
            cat = 'skeleton'
        else:
            cat = 'minimal'
        orphans.append({
            'page': key, 'cat': cat, 'lines': data['lines'],
            'size': data['size'], 'outbound': len(data['wikilinks'])
        })

# 5. Broken wikilinks
bl = []
for key, data in pages.items():
    for link in data['wikilinks']:
        tgt = link.split('#')[0].split('|')[0].strip()
        if tgt.startswith(':') or tgt in ('wikilinks', 'index', 'Index', 'log'):
            continue
        if tgt not in all_slugs:
            parts = tgt.split('/')
            if len(parts) == 2:
                ns, slug = parts
                other = 'concepts' if ns == 'entities' else 'entities'
                ot = f'{other}/{slug}'
                if ot in all_slugs:
                    bl.append({'source': key, 'link': f'[[{tgt}]]', 'fix': ot, 'issue': 'cross-namespace'})
                else:
                    bl.append({'source': key, 'link': f'[[{tgt}]]', 'fix': None, 'issue': 'missing'})
            else:
                found = None
                for pref in ['entities', 'concepts', 'comparisons', 'events', 'queries']:
                    cand = f'{pref}/{tgt}'
                    if cand in all_slugs:
                        found = cand
                        break
                if found:
                    bl.append({'source': key, 'link': f'[[{tgt}]]', 'fix': found, 'issue': 'bare-wikilink'})
                else:
                    bl.append({'source': key, 'link': f'[[{tgt}]]', 'fix': None, 'issue': 'bare-wikilink-missing'})

# 6. Index reconciliation
with open(os.path.join(wiki, 'index.md')) as f:
    idx_content = f.read()
idx_entries = set()
for m in re.finditer(r'\[\[((?:entities|concepts|comparisons|queries|events)/(?:[^|\]]+))\]\]', idx_content):
    idx_entries.add(m.group(1))
not_indexed = sorted(all_slugs - idx_entries)
not_on_disk = sorted(idx_entries - all_slugs)

# 7. Duplicates
dups = {}
for subdir in ['entities', 'concepts', 'comparisons']:
    dp = os.path.join(wiki, subdir)
    for fn in sorted(os.listdir(dp)):
        if fn.endswith('.md'):
            norm = fn.replace('.md', '').lower().replace('-', '').replace('_', '')
            dups.setdefault(norm, []).append(f'{subdir}/{fn.replace(".md", "")}')
dups = {k: v for k, v in dups.items() if len(v) > 1}

# 8. Stats
fixable = [b for b in bl if b.get('fix')]
content_rich_orphans = [o for o in orphans if o['cat'] == 'content-rich']
missing_targets = Counter(b['link'] for b in bl if not b.get('fix'))
cat_ni = Counter(p.split('/')[0] for p in not_indexed)

report_date = datetime.now().strftime('%Y-%m-%d')
report_path = os.path.join(wiki, 'queries', f'wiki-graph-analysis-weekly-{report_date}.md')

# Clean up old report if exists
old_report = os.path.join(wiki, 'queries', 'wiki-graph-analysis-weekly-2026-06-19.md')
if os.path.exists(old_report) and old_report != report_path:
    os.remove(old_report)

with open(report_path, 'w', encoding='utf-8') as f:
    f.write(f'''---
title: Weekly Wiki Graph Analysis
created: {report_date}
updated: {report_date}
type: query
tags: [wiki-maintenance, graph-analysis]
sources: []
---

# Weekly Wiki Graph Analysis

**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}

## Summary

| Metric | Value |
|--------|-------|
| Total pages scanned | {len(pages)} |
| Entities | {sum(1 for k in pages if k.startswith('entities/'))} |
| Concepts | {sum(1 for k in pages if k.startswith('concepts/'))} |
| Comparisons | {sum(1 for k in pages if k.startswith('comparisons/'))} |
| Queries | {sum(1 for k in pages if k.startswith('queries/'))} |
| Events | {sum(1 for k in pages if k.startswith('events/'))} |
| Orphans (no inbound links) | {len(orphans)} |
| Content-rich orphans | {len(content_rich_orphans)} |
| Broken wikilinks | {len(bl)} |
| Fixable wikilinks | {len(fixable)} |
| Duplicate groups | {len(dups)} |
| Oversized pages (>200 lines) | {len(oversized)} |
| Missing sources | {len(no_sources)} ({len(no_sources)/len(pages)*100:.0f}%) |
| Tag violations | {len(tag_violations)} |
| Stale pages (>90 days) | {len(stale)} |
| Skeleton pages | {len(skeletons)} |
| Not indexed in index.md | {len(not_indexed)} |
| Stale index entries | {len(not_on_disk)} |

## 1. Orphan Pages

{len(orphans)} pages have zero inbound links from other wiki pages.

### Content-Rich Orphans (top 15)

''')
    for o in sorted(content_rich_orphans, key=lambda x: x['lines'], reverse=True)[:15]:
        f.write(f'- **{o["page"]}** — {o["lines"]} lines, {o["outbound"]} outbound links\n')

    f.write(f'''
### All Orphans by Category
''')
    cat_counts = Counter(o['cat'] for o in orphans)
    for cat, cnt in sorted(cat_counts.items()):
        f.write(f'- {cat}: {cnt}\n')

    f.write(f'''
## 2. Broken Wikilinks

{len(bl)} total broken links.

| Issue Type | Count | Description |
|------------|-------|-------------|
''')
    issue_counts = Counter(b['issue'] for b in bl)
    for issue, cnt in sorted(issue_counts.items(), key=lambda x: x[1], reverse=True):
        descs = {
            'cross-namespace': 'Entity ↔ concept namespace mismatch (auto-fixable)',
            'bare-wikilink': 'Bare name without namespace prefix (auto-fixable)',
            'bare-wikilink-missing': 'Bare name, target page does not exist',
            'missing': 'Namespaced link to a page that does not exist',
        }
        f.write(f'| {issue} | {cnt} | {descs.get(issue, "")} |\n')

    f.write(f'''
### Top Broken Targets (pages that need creating)

''')
    for link, cnt in missing_targets.most_common(15):
        f.write(f'- [[{link}]] — {cnt} references\n')

    f.write(f'''
### Fixable Links (sample)

{len(fixable)} links can be auto-fixed (cross-namespace or bare → namespaced).

''')
    for b in fixable[:10]:
        f.write(f'- `{b["source"]}`: {b["link"]} → [[{b["fix"]}]]\n')
    if len(fixable) > 10:
        f.write(f'- ... and {len(fixable) - 10} more\n')

    f.write(f'''
## 3. Duplicate / Similar Pages

{len(dups)} potential duplicate groups detected by normalized name matching.

''')
    for norm, dps in sorted(dups.items(), key=lambda x: len(x[1]), reverse=True)[:25]:
        f.write(f'- `{norm}`: {", ".join(dps)}\n')

    f.write(f'''
## 4. Index Reconciliation

- **{len(not_indexed)} pages** are on disk but not listed in index.md
- **{len(not_on_disk)} index entries** reference files that no longer exist

### Not-Indexed by Category

''')
    for cat, cnt in sorted(cat_ni.items(), key=lambda x: x[1], reverse=True):
        f.write(f'- {cat}: {cnt}\n')

    f.write(f'''
## 5. Oversized Pages (>200 lines)

{len(oversized)} pages exceed the 200-line threshold.

''')
    for p in sorted(oversized, key=lambda x: x['lines'], reverse=True)[:10]:
        f.write(f'- **{p["page"]}** — {p["lines"]} lines\n')
    if len(oversized) > 10:
        f.write(f'- ... and {len(oversized) - 10} more\n')

    f.write(f'''
## 6. Stale Pages (>90 days since update)

{len(stale)} pages have not been updated in over 90 days.

## 7. Tag Violations

{len(tag_violations)} pages use non-canonical tags.

## 8. Recommended Actions

''')

    recs = []
    if len(not_indexed) > 50:
        recs.append(f'[HIGH] Add {len(not_indexed)} pages to index.md (batch orphan reg script needed)')
    if len(fixable) > 5:
        recs.append(f'[MEDIUM] Fix {len(fixable)} cross-namespace / bare wikilinks')
    if content_rich_orphans:
        recs.append(f'[MEDIUM] Add inbound links to {len(content_rich_orphans)} content-rich orphan pages')
    if dups:
        recs.append(f'[HIGH] Review and consolidate {len(dups)} potential duplicate groups')
    if len(oversized) > 10:
        recs.append(f'[LOW] Consider splitting {len(oversized)} oversized pages (>200 lines)')
    if tag_violations:
        recs.append(f'[HIGH] Fix {len(tag_violations)} pages with non-canonical tags')
    if not_on_disk:
        recs.append(f'[MEDIUM] Remove {len(not_on_disk)} stale index entries (files missing)')
    if len(no_sources) / len(pages) * 100 > 30:
        recs.append(f'[HIGH] {len(no_sources)} pages ({len(no_sources)/len(pages)*100:.0f}%) missing sources field - set to []')
    if stale:
        recs.append(f'[LOW] {len(stale)} pages stale >90 days - review needed')
    if skeletons:
        recs.append(f'[MEDIUM] {len(skeletons)} skeleton pages need enrichment')

    for r in recs:
        f.write(f'- {r}\n')

    f.write(f'''
---
*Generated by `scripts/wiki_graph_analysis_weekly.py`*
''')

print(f'REPORT_SAVED:{report_path}')
print(f'PAGES:{len(pages)}')
print(f'ORPHANS:{len(orphans)}')
print(f'CONTENT_RICH_ORPHANS:{len(content_rich_orphans)}')
print(f'BROKEN_LINKS:{len(bl)}')
print(f'FIXABLE:{len(fixable)}')
print(f'DUPLICATES:{len(dups)}')
print(f'NOT_INDEXED:{len(not_indexed)}')
print(f'NOT_ON_DISK:{len(not_on_disk)}')
print(f'OVERSIZED:{len(oversized)}')
print(f'NO_SOURCES:{len(no_sources)}')
print(f'STALE:{len(stale)}')
print(f'SKELETONS:{len(skeletons)}')
print(f'TAG_VIOLATIONS:{len(tag_violations)}')
print(f'RECOMMENDATIONS:{len(recs)}')
