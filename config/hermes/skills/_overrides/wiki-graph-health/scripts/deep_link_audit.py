#!/usr/bin/env python3
"""Deep wiki link audit — accurate broken-link / orphan / stale counts.

Why this exists: scripts/_weekly_graph_report.py (and wiki_graph_analysis_weekly.py)
only scan top-level files per namespace and resolve links against that shallow page
set. That overstates broken links (dir-index pages, _index links, raw/ targets,
bare links to nested pages) and understates orphans (nested pages never counted).
This script walks ALL depths, resolves every target (exact / dir-index / _index /
basename-across-namespaces / raw+transcripts), and reports true numbers.

Usage:
  python3 scripts/deep_link_audit.py            # full report to stdout
  python3 scripts/deep_link_audit.py --json     # also write /tmp/wiki_deep_audit.json

Cron note: do NOT pipe this (or wiki_graph.py) into python3/jq inside a cron job —
the security scanner blocks 'python3 | python3' (HIGH: pipe to interpreter). Write
output to a file first, then read/parse it in a separate command.
"""
import argparse
import json
import os
import re
from collections import Counter
from datetime import datetime, timezone

WIKI = '/opt/data/ai-topics/wiki'
L2 = ['entities', 'concepts', 'comparisons', 'queries', 'events']
ALL_NS = L2 + ['raw', 'transcripts']


def collect_pages():
    pages = {}
    for ns in ALL_NS:
        dp = os.path.join(WIKI, ns)
        if not os.path.isdir(dp):
            continue
        for root, _dirs, files in os.walk(dp):
            for fn in files:
                if fn.endswith('.md'):
                    rel = os.path.relpath(os.path.join(root, fn), WIKI).replace('.md', '')
                    pages[rel] = os.path.join(root, fn)
    return pages


def build_resolver(pages):
    by_base = {}
    for rel in pages:
        by_base.setdefault(rel.split('/')[-1], []).append(rel)

    def resolve(tgt):
        if tgt in pages:
            return tgt
        if tgt + '/index' in pages:
            return tgt + '/index'
        if tgt + '/_index' in pages:
            return tgt + '/_index'
        # bare wikilink: match basename anywhere under an L2 namespace
        if '/' not in tgt:
            for cand in by_base.get(tgt, []):
                if cand.split('/')[0] in L2:
                    return cand
        return None

    return resolve


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args()

    pages = collect_pages()
    resolve = build_resolver(pages)
    l2_pages = {rel: p for rel, p in pages.items() if rel.split('/')[0] in L2}

    # --- inbound graph (L2 sources only) ---
    inbound = {rel: [] for rel in l2_pages}
    for rel, path in l2_pages.items():
        try:
            content = open(path, encoding='utf-8', errors='replace').read()
        except Exception:
            continue
        for m in re.finditer(r'\[\[([^\]|]+)', content):
            tgt = m.group(1).split('#')[0].split('|')[0].strip()
            if not tgt or tgt.startswith(':') or tgt in ('wikilinks', 'index', 'Index', 'log'):
                continue
            r = resolve(tgt)
            if r and r != rel and r in inbound:
                inbound[r].append(rel)

    orphans = []
    for rel in sorted(inbound):
        if rel.endswith('/_index') or rel.endswith('/index'):
            continue
        if not inbound[rel]:
            try:
                lines = len(open(pages[rel], encoding='utf-8', errors='replace').read().split('\n'))
            except Exception:
                continue
            if lines >= 20:
                orphans.append((rel, lines))

    # --- broken links (L2 sources) ---
    broken = []
    crossns = []
    for rel, path in l2_pages.items():
        try:
            content = open(path, encoding='utf-8', errors='replace').read()
        except Exception:
            continue
        for m in re.finditer(r'\[\[([^\]|]+)', content):
            tgt = m.group(1).split('#')[0].split('|')[0].strip()
            if not tgt or tgt.startswith(':') or tgt in ('wikilinks', 'index', 'Index', 'log'):
                continue
            if not resolve(tgt):
                broken.append((rel, tgt))

    # --- stale by category ---
    stale = Counter()
    for rel, path in l2_pages.items():
        try:
            content = open(path, encoding='utf-8', errors='replace').read()
        except Exception:
            continue
        m = re.search(r'^updated:\s*(.+)$', content, re.MULTILINE)
        if not m:
            continue
        try:
            dt = datetime.strptime(m.group(1).strip()[:10], '%Y-%m-%d').replace(tzinfo=timezone.utc)
            days = (datetime.now(timezone.utc) - dt).days
        except ValueError:
            continue
        if days > 90:
            stale[rel.split('/')[0]] += 1

    print(f"Pages scanned (all depths, incl raw/transcripts): {len(pages)}")
    print(f"L2 pages: {len(l2_pages)}")
    print(f"\nTRUE broken links (L2->any, unresolvable): {len(broken)}")
    ns = Counter(t.split('/')[0] if '/' in t else '(bare)' for _s, t in broken)
    print("  target namespace:", dict(ns.most_common(10)))
    for t, c in Counter(t for _s, t in broken).most_common(15):
        print(f"    {c:5d}  {t}")
    print(f"\nTRUE orphans (>=20 lines, no inbound, excl index pages): {len(orphans)}")
    cat = Counter(p.split('/')[0] for p, _l in orphans)
    print("  by category:", dict(cat))
    for p, l in sorted(orphans, key=lambda x: x[1], reverse=True)[:20]:
        print(f"    {l:5d}  {p}")
    print(f"\nStale (>90d) by category: {dict(stale)}")

    if args.json:
        with open('/tmp/wiki_deep_audit.json', 'w') as f:
            json.dump({
                'pages': len(pages),
                'broken': len(broken),
                'broken_top': Counter(t for _s, t in broken).most_common(30),
                'orphans': orphans[:100],
                'stale': dict(stale),
            }, f, indent=2)
        print("\nJSON written to /tmp/wiki_deep_audit.json")


if __name__ == '__main__':
    main()
