#!/usr/bin/env python3
"""Rebuild wiki index.md from scratch."""

import os
import re
import glob
from datetime import date

WIKI_DIR = os.path.expanduser("~/ai-topics/wiki")
EXCLUDED_DIRS = {".git", "raw"}
EXCLUDED_FILES = {"index.md", "log.md", "log-2026.md", "SCHEMA.md", "_index.md"}

STUB_STATUSES = {"stub", "skeleton"}

def parse_frontmatter(content):
    """Parse YAML-like frontmatter. Returns dict and remaining content."""
    m = re.match(r'^---\s*\n(.*?)\n(?:---|\.\.\.)', content, re.DOTALL)
    if not m:
        return {}, content
    
    fm = {}
    for line in m.group(1).split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip().lower()
            val = val.strip().strip('"').strip("'")
            fm[key] = val
    
    remaining = content[m.end():].strip()
    return fm, remaining

def get_description(content, fm, filename):
    """Extract a one-line description for the page."""
    # Priority 1: description from frontmatter
    desc = fm.get('description', '')
    if desc:
        desc = desc.strip().strip('"').strip("'")
        if desc:
            return desc
    
    # Priority 2: first # heading content
    h_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if h_match:
        heading = h_match.group(1).strip()
        # Use the heading as-is, but prefer next paragraph if available
        after_heading = content[h_match.end():].strip()
        # Get first meaningful paragraph after heading
        para_match = re.search(r'^([^#\n][^\n]{20,})', after_heading, re.MULTILINE)
        if para_match:
            para = para_match.group(1).strip()
            # Clean up markdown links for plain text
            para = re.sub(r'\[\[([^\]]+)\]\]', r'\1', para)
            para = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', para)
            # Truncate to reasonable length
            if len(para) > 200:
                para = para[:197] + '...'
            return para
        return heading
    
    # Priority 3: first line with meaningful text
    for line in content.split('\n'):
        line = line.strip()
        if line and not line.startswith('---') and not line.startswith('#') and len(line) > 20:
            line = re.sub(r'\[\[([^\]]+)\]\]', r'\1', line)
            line = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', line)
            if len(line) > 200:
                line = line[:197] + '...'
            return line
    
    # Fallback: use filename as description
    return filename.replace('-', ' ').title()

def main():
    files = []
    for root, dirs, fnames in os.walk(WIKI_DIR):
        # Skip excluded dirs
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        
        # Determine relative path
        rel_root = os.path.relpath(root, WIKI_DIR)
        
        for f in fnames:
            if not f.endswith('.md'):
                continue
            if f in EXCLUDED_FILES:
                continue
            files.append(os.path.join(root, f))
    
    print(f"Found {len(files)} total .md files to process")
    
    # Categorize pages
    pages = {
        'entity': [],
        'concept': [],
        'comparison': [],
        'event': [],
        'other': []
    }
    stubs = []
    
    for fp in sorted(files):
        rel_path = os.path.relpath(fp, WIKI_DIR)
        slug = os.path.splitext(rel_path)[0]
        filename = os.path.basename(fp)
        basename_noext = os.path.splitext(filename)[0]
        
        with open(fp, 'r', encoding='utf-8', errors='replace') as fh:
            content = fh.read()
        
        fm, remaining = parse_frontmatter(content)
        
        # Determine type
        ptype = fm.get('type', '').lower().strip()
        if not ptype or ptype in ('unknown', ''):
            # Infer from directory
            if rel_path.startswith('entities/'):
                ptype = 'entity'
            elif rel_path.startswith('concepts/'):
                ptype = 'concept'
            elif rel_path.startswith('comparisons/'):
                ptype = 'comparison'
            elif rel_path.startswith('events/'):
                ptype = 'event'
            else:
                ptype = 'other'
        
        # Map to standard types
        type_map = {
            'entity': 'entity',
            'concept': 'concept',
            'comparison': 'comparison',
            'person': 'entity',
            'project': 'concept',
            'event': 'event',
        }
        std_type = type_map.get(ptype, 'other')
        
        # Get status
        status = fm.get('status', '').lower().strip()
        
        # Get description
        desc = get_description(content, fm, basename_noext)
        
        entry = {
            'slug': slug,
            'title': fm.get('title', basename_noext.replace('-', ' ').title()).strip().strip('"').strip("'"),
            'description': desc,
            'type': std_type,
            'status': status,
        }
        
        if status in STUB_STATUSES:
            stubs.append(entry)
        else:
            if std_type in pages:
                pages[std_type].append(entry)
            else:
                pages['other'].append(entry)
    
    # Build index content
    today = date.today().isoformat()
    total_pages = len(files)
    total_full = sum(len(v) for v in pages.values())
    total_stubs = len(stubs)
    
    lines = []
    lines.append("# Wiki Index")
    lines.append("")
    lines.append("> Content catalog. Every wiki page listed under its type with a one-line summary.")
    lines.append("> Read this first to find relevant pages for any query.")
    lines.append(f"> Last updated: {today} | Total pages: {total_pages} | Full entries: {total_full} | Stubs: {total_stubs}")
    lines.append("")
    
    # Helper to format wikilink
    def fmt_wikilink(slug):
        return f"[[{slug}]]"
    
    # Type labels and order
    type_order = [
        ('entity', 'Entities'),
        ('concept', 'Concepts'),
        ('comparison', 'Comparisons'),
        ('event', 'Events'),
        ('other', 'Other'),
    ]
    
    for type_key, type_label in type_order:
        entries = pages.get(type_key, [])
        if not entries:
            continue
        
        lines.append(f"## {type_label} ({len(entries)} pages)")
        lines.append("")
        
        for e in entries:
            desc = e['description']
            # Clean up description - remove leading/trailing pipes, dashes, etc.
            desc = re.sub(r'^\s*[\|\-–—]+\s*', '', desc)
            desc = re.sub(r'\s+', ' ', desc).strip()
            if not desc:
                desc = "(no description)"
            lines.append(f"- {fmt_wikilink(e['slug'])} — {desc}")
        
        lines.append("")
    
    # Stubs section
    if stubs:
        lines.append(f"## Skeletons & Stubs ({len(stubs)} pages)")
        lines.append("")
        lines.append("> Pages marked as `status: stub` or `status: skeleton` — minimal content, placeholder entries.")
        lines.append("")
        
        for e in stubs:
            desc = e['description']
            desc = re.sub(r'^\s*[\|\-–—]+\s*', '', desc)
            desc = re.sub(r'\s+', ' ', desc).strip()
            if not desc or len(desc) < 5:
                desc = "(stub)"
            lines.append(f"- {fmt_wikilink(e['slug'])} — {desc}")
        
        lines.append("")
    
    output = '\n'.join(lines)
    
    index_path = os.path.join(WIKI_DIR, "index.md")
    with open(index_path, 'w', encoding='utf-8') as fh:
        fh.write(output)
    
    print(f"\nWritten to {index_path}")
    print(f"Total pages in index: {total_pages}")
    print(f"  Entities: {len(pages['entity'])}")
    print(f"  Concepts: {len(pages['concept'])}")
    print(f"  Comparisons: {len(pages['comparison'])}")
    print(f"  Events: {len(pages['event'])}")
    print(f"  Other: {len(pages.get('other', []))}")
    print(f"  Stubs/Skeletons: {len(stubs)}")
    print(f"  Sum: {total_full + total_stubs}")

if __name__ == '__main__':
    main()
