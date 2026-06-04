#!/usr/bin/env python3
"""
Auto-fix broken wikilinks: '- — description' missing the [[slug]] before '—'.

Uses fuzzy matching (word-overlap score) against existing wiki pages
to find the best slug for each orphaned description.

Usage:
  python3 scripts/fix_broken_wikilinks.py --dry-run --threshold 0.4
  python3 scripts/fix_broken_wikilinks.py --apply --threshold 0.4

Threshold:
  0.5+  = near-certain matches (page title matches description)
  0.4   = good balance (recommended default)
  0.3   = aggressive (catches more, ~30% risk of wrong match)
  0.25  = very aggressive (high false-positive rate)
"""

import os
import re
import sys
import yaml
from collections import Counter

WIKI_DIR = os.path.expanduser("~/wiki")
ENTITY_DIR = os.path.join(WIKI_DIR, "entities")
CONCEPT_DIR = os.path.join(WIKI_DIR, "concepts")


def parse_frontmatter(filepath):
    with open(filepath) as f:
        content = f.read()
    if not content.startswith('---'):
        return {}, content
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except:
        fm = {}
    body = parts[2].strip()
    return fm, body


def slug_from_path(filepath, base_dir):
    rel = os.path.relpath(filepath, base_dir)
    return rel.replace('.md', '')


def build_slug_index():
    """Build a dict mapping searchable text → (slug, type, title)."""
    index = []
    for root, dirs, files in os.walk(ENTITY_DIR):
        for f in files:
            if not f.endswith('.md'):
                continue
            fp = os.path.join(root, f)
            slug = slug_from_path(fp, ENTITY_DIR)
            fm, body = parse_frontmatter(fp)
            title = fm.get('title', slug)
            aliases = fm.get('aliases', [])
            if isinstance(aliases, str):
                aliases = [aliases]
            tags = fm.get('tags', [])
            if isinstance(tags, str):
                tags = [tags]
            searchable = {title.lower(), slug.lower()}
            for a in aliases:
                if isinstance(a, str):
                    searchable.add(a.lower())
            for t in tags:
                if isinstance(t, str):
                    searchable.add(t.lower())
            body_clean = re.sub(r'[#*\[\]]', '', body[:200]).lower()
            index.append({
                'slug': slug,
                'type': 'entity',
                'title': title,
                'searchable': searchable,
                'body_preview': body_clean,
            })
    for root, dirs, files in os.walk(CONCEPT_DIR):
        for f in files:
            if not f.endswith('.md'):
                continue
            fp = os.path.join(root, f)
            slug = slug_from_path(fp, CONCEPT_DIR)
            fm, body = parse_frontmatter(fp)
            title = fm.get('title', slug)
            aliases = fm.get('aliases', [])
            if isinstance(aliases, str):
                aliases = [aliases]
            tags = fm.get('tags', [])
            if isinstance(tags, str):
                tags = [tags]
            searchable = {title.lower(), slug.lower()}
            for a in aliases:
                if isinstance(a, str):
                    searchable.add(a.lower())
            for t in tags:
                if isinstance(t, str):
                    searchable.add(t.lower())
            body_clean = re.sub(r'[#*\[\]]', '', body[:200]).lower()
            index.append({
                'slug': f'concepts/{slug}',
                'type': 'concept',
                'title': title,
                'searchable': searchable,
                'body_preview': body_clean,
            })
    return index


def tokenize(text):
    text = text.lower()
    tokens = re.findall(r'[a-z0-9]+', text)
    return [t for t in tokens if len(t) > 2 or t.isdigit()]


def compute_word_overlap(desc_tokens, target_text):
    target_tokens = set(tokenize(target_text))
    if not desc_tokens:
        return 0.0
    matches = sum(1 for t in desc_tokens if t in target_tokens)
    return matches / len(desc_tokens)


def find_best_slug(description, slug_index, threshold=0.4):
    desc_tokens = tokenize(description)
    if not desc_tokens:
        return None, 0.0
    best_slug = None
    best_score = 0.0
    for entry in slug_index:
        target = ' '.join(entry['searchable'])
        score = compute_word_overlap(desc_tokens, target)
        body_score = compute_word_overlap(desc_tokens, entry['body_preview'])
        score = max(score, body_score * 0.8)
        if score > best_score:
            best_score = score
            best_slug = entry['slug']
    if best_score >= threshold:
        return best_slug, best_score
    return None, best_score


def find_broken_links(filepath):
    """Find lines with '- — description' missing [[slug]]."""
    broken = []
    with open(filepath) as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        stripped = line.rstrip()
        if re.match(r'^\s*-\s+—\s', stripped):
            desc = re.sub(r'^\s*-\s+—\s*', '', stripped)
            broken.append((i, desc.strip(), stripped))
    return broken


def fix_broken_links(filepath, slug_index, dry_run=True, threshold=0.4):
    with open(filepath) as f:
        lines = f.readlines()
    fixes = []
    for idx, desc, original in find_broken_links(filepath):
        slug, score = find_best_slug(desc, slug_index, threshold)
        if slug:
            new_line = original.replace('- — ', f'- [[{slug}]] — ', 1)
            fixes.append((idx, desc, slug, score, original, new_line))
            lines[idx] = new_line
    if not dry_run and fixes:
        with open(filepath, 'w') as f:
            f.writelines(lines)
    return fixes


def main():
    dry_run = '--dry-run' in sys.argv or '-n' in sys.argv
    threshold = float(sys.argv[sys.argv.index('--threshold') + 1]) if '--threshold' in sys.argv else 0.4
    apply = '--apply' in sys.argv
    if apply:
        dry_run = False

    print(f"Building slug index...")
    slug_index = build_slug_index()
    print(f"Indexed {len(slug_index)} pages")

    all_files = []
    for root, dirs, files in os.walk(ENTITY_DIR):
        for f in files:
            if f.endswith('.md'):
                all_files.append(os.path.join(root, f))
    for root, dirs, files in os.walk(CONCEPT_DIR):
        for f in files:
            if f.endswith('.md'):
                all_files.append(os.path.join(root, f))

    total_broken = 0
    total_fixed = 0
    unfixable_list = []
    fix_details = []

    for filepath in sorted(all_files):
        relpath = os.path.relpath(filepath, WIKI_DIR)
        broken = find_broken_links(filepath)
        if not broken:
            continue
        total_broken += len(broken)
        fixes = fix_broken_links(filepath, slug_index, dry_run=dry_run, threshold=threshold)
        total_fixed += len(fixes)
        unfixable = [(idx, desc) for idx, desc, raw in broken
                     if not find_best_slug(desc, slug_index, threshold)[0]]
        for idx, desc in unfixable:
            _, score = find_best_slug(desc, slug_index, 0)
            unfixable_list.append((relpath, idx+1, desc, score))
        for idx, desc, slug, score, old, new in fixes:
            fix_details.append((relpath, idx+1, desc, slug, score))

    files_with_broken = len(set(r for r,_,_,_ in unfixable_list) | set(r for r,_,_,_,_ in fix_details))
    print(f"\n=== Threshold: {threshold} ===")
    print(f"Files with broken links: {files_with_broken}")
    print(f"Total broken links: {total_broken}")
    print(f"Auto-fixable: {total_fixed}")
    print(f"Unfixable ({threshold} threshold): {len(unfixable_list)}")
    if fix_details:
        print(f"\n=== Fix examples (first 20) ===")
        for relpath, ln, desc, slug, score in fix_details[:20]:
            print(f"  [{score:.2f}] {relpath}:{ln} → [[{slug}]] — {desc[:70]}")
    if unfixable_list:
        print(f"\n=== Unfixable examples (first 20) ===")
        for relpath, ln, desc, score in sorted(unfixable_list, key=lambda x: -x[3])[:20]:
            print(f"  [{score:.2f}] {relpath}:{ln} — {desc[:80]}")
    if dry_run:
        print(f"\nRun with --apply to fix files. Adjust threshold with --threshold 0.3 (more aggressive).")


if __name__ == '__main__':
    main()
