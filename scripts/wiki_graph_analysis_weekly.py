#!/usr/bin/env python3
"""Weekly wiki graph analysis: orphans, broken links, duplicates, stale pages, tag violations."""

import os, re, json
from collections import defaultdict, Counter
from datetime import datetime, timezone

wiki = '/opt/data/ai-topics/wiki'

def main():
    results = {
        'pages': {},
        'broken_links': [],
        'orphans': [],
        'duplicates': [],
        'frontmatter_issues': [],
        'tag_violations': [],
        'stale_pages': [],
        'oversized_pages': [],
        'no_sources_pages': [],
        'status_skeleton_pages': [],
        'index_gaps': {}
    }

    # 1. Read SCHEMA.md for canonical tags
    with open(os.path.join(wiki, 'SCHEMA.md')) as f:
        schema_content = f.read()

    # Parse canonical tags from Tag Taxonomy section
    canonical_tags = set()
    # Method 1: backtick-wrapped tags (Core Types section)
    idx = schema_content.find('## Tag Taxonomy')
    if idx >= 0:
        tax_section = schema_content[idx:]
        canonical_tags.update(re.findall(r'`([a-z][a-z0-9-]+)`', tax_section))
        # Method 2: comma-separated lists in category bullet points
        for line in tax_section.split('\n'):
            if line.strip().startswith('- **') and ':' in line:
                parts = line.split(':', 1)
                body = parts[1]
                items = [t.strip().rstrip('.') for t in body.split(',')]
                for item in items:
                    if re.match(r'^[a-z][a-z0-9-]+$', item):
                        canonical_tags.add(item)

    # 2. Single pass over all L2 pages
    for subdir in ['entities', 'concepts', 'comparisons', 'queries', 'events']:
        dir_path = os.path.join(wiki, subdir)
        if not os.path.isdir(dir_path):
            continue
        for f in sorted(os.listdir(dir_path)):
            if not f.endswith('.md'):
                continue
            path = os.path.join(dir_path, f)
            try:
                with open(path, encoding='utf-8', errors='replace') as fh:
                    content = fh.read()
            except:
                continue

            slug = f.replace('.md', '')
            key = f"{subdir}/{slug}"
            lines = content.split('\n')

            # Extract frontmatter
            fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            has_frontmatter = bool(fm_match)
            tags, sources, page_type, created, updated, status = [], None, None, None, None, None

            if fm_match:
                fm = fm_match.group(1)
                # Extract tags ONLY from the tags: section (not sources, aliases, etc.)
                tags = []
                in_tags_section = False
                for line in fm.split('\n'):
                    # Detect if we're entering a top-level key
                    key_match = re.match(r'^(\w+):', line)
                    if key_match:
                        in_tags_section = (key_match.group(1) == 'tags')
                    # Capture list items only if in tags section
                    if in_tags_section:
                        tag_match = re.match(r'^\s*-\s+([a-z][a-z0-9-]+)', line)
                        if tag_match:
                            tags.append(tag_match.group(1))
                # Also handle inline format: tags: [tag1, tag2]
                inline_tags = re.search(r'tags:\s*\[([^\]]+)\]', fm)
                if inline_tags:
                    tags = [t.strip() for t in inline_tags.group(1).split(',') if t.strip()]
                # Extract scalar fields via pattern matching
                for field_name in ['sources', 'type', 'created', 'updated', 'status']:
                    m = re.search(r'^' + field_name + r':\s*(.+)$', fm, re.MULTILINE)
                    if m:
                        val = m.group(1).strip()
                        if field_name == 'sources':
                            sources = val
                        elif field_name == 'type':
                            page_type = val
                        elif field_name == 'created':
                            created = val
                        elif field_name == 'updated':
                            updated = val
                        elif field_name == 'status':
                            status = val

            wikilinks = re.findall(r'\[\[([^\]|]+)', content)

            results['pages'][key] = {
                'path': path, 'size': len(content), 'lines': len(lines),
                'tags': tags, 'sources': sources, 'type': page_type,
                'created': created, 'updated': updated, 'status': status,
                'has_frontmatter': has_frontmatter, 'wikilinks': wikilinks
            }

            missing = []
            if not has_frontmatter:
                missing.append('frontmatter')
            if sources is None or sources == '':
                missing.append('sources')
                results['no_sources_pages'].append(key)
            if page_type is None:
                missing.append('type')
            if created is None:
                missing.append('created')
            if updated is None:
                missing.append('updated')
            if missing:
                results['frontmatter_issues'].append({'page': key, 'missing': missing})

            if status == 'skeleton':
                results['status_skeleton_pages'].append(key)

            non_canonical = [t for t in tags if t and t not in canonical_tags]
            if non_canonical:
                results['tag_violations'].append({'page': key, 'tags': non_canonical})

            if len(lines) > 200:
                results['oversized_pages'].append({'page': key, 'lines': len(lines)})

            if updated:
                try:
                    updated_dt = datetime.strptime(updated[:10], '%Y-%m-%d').replace(tzinfo=timezone.utc)
                    now = datetime.now(timezone.utc)
                    days_stale = (now - updated_dt).days
                    if days_stale > 90:
                        results['stale_pages'].append({'page': key, 'updated': updated, 'days_stale': days_stale})
                except ValueError:
                    pass

    # 3. Build inbound link graph
    inbound = defaultdict(list)
    all_slugs = set(results['pages'].keys())

    for key, data in results['pages'].items():
        for link in data['wikilinks']:
            target = link.split('#')[0].split('|')[0].strip()
            if target:
                inbound[target].append(key)

    # 4. Orphans (no inbound links from other pages)
    for key in sorted(results['pages'].keys()):
        if key.endswith('/_index'):
            continue
        # Orphan = page never targeted by any wikilink (no inbound links).
        # Fixed 2026-08-14: previous `any(key in targets ...)` checked source
        # membership (outbound links), reporting dead-ends instead of orphans.
        has_inbound = key in inbound
        if not has_inbound:
            lines = results['pages'][key]['lines']
            size = results['pages'][key]['size']
            if lines < 5 and size < 100:
                category = 'minimal'
            elif lines < 20 and size < 500:
                category = 'skeleton'
            else:
                category = 'content-rich'
            results['orphans'].append({
                'page': key, 'category': category, 'lines': lines,
                'size': size, 'outbound': len(results['pages'][key]['wikilinks'])
            })

    # 5. Broken wikilinks
    for key, data in results['pages'].items():
        for link in data['wikilinks']:
            target = link.split('#')[0].split('|')[0].strip()
            if target.startswith(':') or target in ('wikilinks', 'index', 'Index', 'log'):
                continue
            if target not in all_slugs:
                parts = target.split('/')
                if len(parts) == 2:
                    ns, slug = parts
                    other_ns = 'concepts' if ns == 'entities' else 'entities'
                    other_target = f"{other_ns}/{slug}"
                    if other_target in all_slugs:
                        results['broken_links'].append({
                            'source': key, 'link': f'[[{target}]]',
                            'issue': 'cross-namespace', 'fix': other_target
                        })
                    else:
                        results['broken_links'].append({
                            'source': key, 'link': f'[[{target}]]',
                            'issue': 'missing', 'fix': None
                        })
                else:
                    found = None
                    for prefix in ['entities', 'concepts', 'comparisons', 'events', 'queries']:
                        candidate = f"{prefix}/{target}"
                        if candidate in all_slugs:
                            found = candidate
                            break
                    if found:
                        results['broken_links'].append({
                            'source': key, 'link': f'[[{target}]]',
                            'issue': 'bare-wikilink', 'fix': found
                        })
                    else:
                        results['broken_links'].append({
                            'source': key, 'link': f'[[{target}]]',
                            'issue': 'bare-wikilink-missing', 'fix': None
                        })

    # 6. Index reconciliation
    with open(os.path.join(wiki, 'index.md')) as f:
        index_content = f.read()
    index_entries = set()
    for m in re.finditer(r'\[\[((?:entities|concepts|comparisons|queries|events)/(?:[^|\]]+))\]\]', index_content):
        index_entries.add(m.group(1))

    not_indexed = sorted(all_slugs - index_entries)
    not_on_disk = sorted(index_entries - all_slugs)
    results['index_gaps'] = {
        'not_indexed': not_indexed,
        'not_on_disk': not_on_disk,
        'not_indexed_count': len(not_indexed),
        'not_on_disk_count': len(not_on_disk)
    }

    # 7. Duplicate detection
    duplicates = defaultdict(list)
    for subdir in ['entities', 'concepts', 'comparisons']:
        dir_path = os.path.join(wiki, subdir)
        for f in sorted(os.listdir(dir_path)):
            if f.endswith('.md'):
                normalized = f.replace('.md', '').lower().replace('-', '').replace('_', '')
                duplicates[normalized].append(f"{subdir}/{f.replace('.md', '')}")
    results['duplicates'] = {k: v for k, v in duplicates.items() if len(v) > 1}

    # --- OUTPUT ---
    print("=" * 72)
    print("  WIKI GRAPH ANALYSIS REPORT")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
    print("=" * 72)

    print("\n--- PAGE COUNTS ---")
    print(f"Total pages scanned: {len(results['pages'])}")
    for subdir in ['entities', 'concepts', 'comparisons', 'queries', 'events']:
        cnt = sum(1 for k in results['pages'] if k.startswith(subdir + '/'))
        print(f"  {subdir}: {cnt}")

    print("\n--- FRONTMATTER HEALTH ---")
    missing_fm = sum(1 for p in results['frontmatter_issues'] if 'frontmatter' in p['missing'])
    total = len(results['pages'])
    ns = len(results['no_sources_pages'])
    print(f"  Missing frontmatter:        {missing_fm:>5}  ({missing_fm/total*100:5.1f}%)")
    print(f"  Missing sources:            {ns:>5}  ({ns/total*100:5.1f}%)")
    print(f"  Missing type:               {sum(1 for p in results['frontmatter_issues'] if 'type' in p['missing']):>5}")
    print(f"  Missing created:            {sum(1 for p in results['frontmatter_issues'] if 'created' in p['missing']):>5}")
    print(f"  Missing updated:            {sum(1 for p in results['frontmatter_issues'] if 'updated' in p['missing']):>5}")
    print(f"  Status skeleton:            {len(results['status_skeleton_pages']):>5}")

    print("\n--- ORPHAN PAGES (no inbound links) ---")
    print(f"  Total orphans: {len(results['orphans'])}")
    cat_counts = Counter(o['category'] for o in results['orphans'])
    for cat, cnt in sorted(cat_counts.items()):
        print(f"    {cat}: {cnt}")

    if results['orphans']:
        content_rich = [o for o in results['orphans'] if o['category'] == 'content-rich']
        content_rich.sort(key=lambda x: x['lines'], reverse=True)
        print(f"\n  Top content-rich orphans (need linking):")
        for o in content_rich[:10]:
            print(f"    {o['page']} ({o['lines']} lines, {o['outbound']} outbound links)")

    print("\n--- BROKEN WIKILINKS ---")
    bl = results['broken_links']
    print(f"  Total broken links: {len(bl)}")
    issue_counts = Counter(b['issue'] for b in bl)
    for issue, cnt in sorted(issue_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"    {issue}: {cnt}")

    fixable = [b for b in bl if b.get('fix')]
    print(f"\n  Fixable (cross-namespace / bare → namespaced): {len(fixable)}")
    for b in fixable[:20]:
        print(f"    {b['source']:50s} [[{b['link']}] → [[{b['fix']}]]")

    missing_targets = Counter(b['link'] for b in bl if not b.get('fix'))
    if missing_targets:
        print(f"\n  Top missing targets (no page exists):")
        for link, cnt in missing_targets.most_common(15):
            print(f"    [[{link}]] → {cnt} references")

    print("\n--- DUPLICATE / SIMILAR PAGES ---")
    print(f"  Potential duplicate groups: {len(results['duplicates'])}")
    for norm, pages in sorted(results['duplicates'].items(), key=lambda x: len(x[1]), reverse=True)[:25]:
        print(f"    {norm}: {pages}")

    print("\n--- INDEX RECONCILIATION ---")
    print(f"  Pages not in index.md:   {results['index_gaps']['not_indexed_count']}")
    print(f"  Index entries not on disk: {results['index_gaps']['not_on_disk_count']}")
    if results['index_gaps']['not_indexed']:
        cat_ni = Counter(p.split('/')[0] for p in results['index_gaps']['not_indexed'])
        print(f"  Not-indexed by category:")
        for cat, cnt in sorted(cat_ni.items(), key=lambda x: x[1], reverse=True):
            print(f"    {cat}: {cnt}")
        print(f"  Sample (first 20):")
        for p in results['index_gaps']['not_indexed'][:20]:
            print(f"    {p}")

    print(f"\n--- OVERSIZED PAGES (>200 lines) ---")
    print(f"  Total: {len(results['oversized_pages'])}")
    for p in sorted(results['oversized_pages'], key=lambda x: x['lines'], reverse=True)[:20]:
        print(f"    {p['page']:55s} {p['lines']} lines")
    if len(results['oversized_pages']) > 20:
        print(f"    ... and {len(results['oversized_pages'])-20} more")

    print(f"\n--- STALE PAGES (>90 days) ---")
    print(f"  Total: {len(results['stale_pages'])}")
    for p in sorted(results['stale_pages'], key=lambda x: x['days_stale'], reverse=True)[:20]:
        print(f"    {p['page']:55s} last updated {p['updated']} ({p['days_stale']}d ago)")
    if len(results['stale_pages']) > 20:
        print(f"    ... and {len(results['stale_pages'])-20} more")

    print(f"\n--- TAG VIOLATIONS (non-canonical tags) ---")
    print(f"  Pages with invalid tags: {len(results['tag_violations'])}")
    itc = Counter()
    for v in results['tag_violations']:
        for t in v['tags']:
            itc[t] += 1
    print(f"  Most common invalid tags:")
    for tag, cnt in sorted(itc.items(), key=lambda x: x[1], reverse=True)[:20]:
        print(f"    '{tag}': {cnt} pages")

    print(f"\n--- RECOMMENDED ACTIONS ---")
    recs = []
    if results['index_gaps']['not_indexed_count'] > 50:
        recs.append(f"[HIGH]    Add {results['index_gaps']['not_indexed_count']} pages to index.md (batch orphan reg script)")
    if len(fixable) > 5:
        recs.append(f"[MEDIUM]  Fix {len(fixable)} cross-namespace / bare wikilinks")
    content_rich_orphans = [o for o in results['orphans'] if o['category'] == 'content-rich']
    skeleton_orphans = [o for o in results['orphans'] if o['category'] == 'skeleton']
    if content_rich_orphans:
        recs.append(f"[MEDIUM]  Add inbound links to {len(content_rich_orphans)} content-rich orphan pages")
    if skeleton_orphans:
        recs.append(f"[LOW]     {len(skeleton_orphans)} skeleton orphans exist - enrich or clean up")
    if results['duplicates']:
        recs.append(f"[HIGH]    Review and consolidate {len(results['duplicates'])} potential duplicate groups")
    if len(results['oversized_pages']) > 10:
        recs.append(f"[LOW]     Consider splitting {len(results['oversized_pages'])} oversized pages (>200 lines)")
    if results['tag_violations']:
        recs.append(f"[HIGH]    Fix {len(results['tag_violations'])} pages with non-canonical tags (pre-commit blocks)")
    if results['index_gaps']['not_on_disk_count'] > 0:
        recs.append(f"[MEDIUM]  Remove {results['index_gaps']['not_on_disk_count']} stale index entries (files missing)")
    pct_no_sources = ns / total * 100 if total > 0 else 0
    if pct_no_sources > 30:
        recs.append(f"[HIGH]    {ns} pages ({pct_no_sources:.0f}%) missing sources field - set to []")
    if results['stale_pages']:
        recs.append(f"[LOW]     {len(results['stale_pages'])} pages stale >90 days - review/revision needed")
    if results['status_skeleton_pages']:
        recs.append(f"[MEDIUM]  {len(results['status_skeleton_pages'])} skeleton pages need enrichment")
    for r in recs:
        print(f"  {r}")
    if not recs:
        print("  ✅ Wiki is in good health - no significant issues found")

    # Save report JSON
    report_path = f'/opt/data/ai-topics/wiki/queries/wiki-graph-analysis-weekly-{datetime.now().strftime("%Y-%m-%d")}.md'
    with open(report_path, 'w') as f:
        f.write(f"---\n")
        f.write(f"title: Weekly Wiki Graph Analysis\n")
        f.write(f"created: {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write(f"updated: {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write(f"type: query\n")
        f.write(f"tags: []\n")
        f.write(f"sources: []\n")
        f.write(f"---\n\n")
        f.write("# Weekly Wiki Graph Analysis\n\n")
        f.write(f"**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}\n\n")
        f.write("## Summary\n\n")
        f.write(f"- Total pages: {len(results['pages'])}\n")
        f.write(f"- Orphans: {len(results['orphans'])} (content-rich: {len(content_rich_orphans)})\n")
        f.write(f"- Broken links: {len(bl)}\n")
        f.write(f"- Duplicate groups: {len(results['duplicates'])}\n")
        f.write(f"- Index gaps: {results['index_gaps']['not_indexed_count']}\n")
        f.write(f"- Tag violations: {len(results['tag_violations'])}\n")
        f.write(f"- Stale pages: {len(results['stale_pages'])}\n\n")
        f.write("## Recommended Actions\n\n")
        for r in recs:
            f.write(f"- {r}\n")
        f.write("\n")

    print(f"\n  Report saved: {report_path}")

if __name__ == '__main__':
    main()
