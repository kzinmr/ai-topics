#!/usr/bin/env python3
"""
Auto-fix wikilinks detected by wiki_graph.py analysis.

Fixes two categories from the graph analysis report:
  1. bare-wikilink: [[foo]] → [[namespace/foo]] where file exists in a namespace
  2. cross-namespace: [[entities/foo]] → [[concepts/foo]] if file exists in concepts/

Usage:
  python3 scripts/fix_wikilinks.py [--dry-run] [--limit N]

Defaults to /opt/data/ai-topics/wiki as WIKI_ROOT.
Skips raw/ and transcripts/ directories (immutable Layer 1).
"""

import os
import re
import sys
import argparse
from pathlib import Path

WIKI_ROOT = Path(os.environ.get("WIKI_ROOT", "/opt/data/ai-topics/wiki"))
NAMESPACES = ["entities", "concepts", "comparisons", "queries", "events"]


def find_file_in_namespaces(bare_name):
    """Find which namespace a bare wikilink belongs to."""
    for ns in NAMESPACES:
        if (WIKI_ROOT / ns / f"{bare_name}.md").exists():
            return ns
        if (WIKI_ROOT / ns / bare_name / "_index.md").exists():
            return ns
        if (WIKI_ROOT / ns / bare_name / "index.md").exists():
            return ns
    return None


def fix_bare_wikilinks(content):
    """Fix bare wikilinks [[foo]] → [[namespace/foo]]"""
    changes = []

    def replace_bare(match):
        wikilink = match.group(1)
        if "/" in wikilink or wikilink.startswith("#") or wikilink.startswith("^"):
            return match.group(0)
        ns = find_file_in_namespaces(wikilink)
        if ns:
            changes.append((wikilink, f"{ns}/{wikilink}"))
            return f"[[{ns}/{wikilink}]]"
        return match.group(0)

    new_content = re.sub(r'\[\[([^\]|/]+)\]\]', replace_bare, content)
    return new_content, changes


def fix_cross_namespace(content):
    """Fix cross-namespace links: [[entities/foo]] → [[concepts/foo]] if file exists"""
    changes = []

    def replace_cross(match):
        full = match.group(1)
        current_ns, name = full.split("/", 1)
        for ns in NAMESPACES:
            if ns == current_ns:
                continue
            if (WIKI_ROOT / ns / f"{name}.md").exists():
                changes.append((full, f"{ns}/{name}"))
                return f"[[{ns}/{name}]]"
        return match.group(0)

    new_content = re.sub(
        r'\[\[((?:entities|concepts|comparisons|queries|events)/([^\]|]+))\]\]',
        replace_cross,
        content,
    )
    return new_content, changes


def process_file(file_path, dry_run=False):
    """Process a single wiki file. Returns number of changes."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        return 0

    new_content, bare_changes = fix_bare_wikilinks(content)
    new_content, cross_changes = fix_cross_namespace(new_content)
    total = len(bare_changes) + len(cross_changes)

    if total > 0 and not dry_run:
        try:
            file_path.write_text(new_content, encoding="utf-8")
        except Exception as e:
            print(f"Error writing {file_path}: {e}", file=sys.stderr)
            return 0

    if total > 0:
        label = "[DRY-RUN] " if dry_run else ""
        print(f"{label}Fixed {total} links in {file_path.relative_to(WIKI_ROOT)}")
        for old, new in bare_changes[:3]:
            print(f"  bare: [[{old}]] → [[{new}]]")
        for old, new in cross_changes[:3]:
            print(f"  cross: [[{old}]] → [[{new}]]")

    return total


def main():
    parser = argparse.ArgumentParser(description="Auto-fix wikilinks from graph analysis")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without writing")
    parser.add_argument("--limit", type=int, default=0, help="Max files to process (0=all)")
    args = parser.parse_args()

    total_fixed = 0
    files_modified = 0
    count = 0

    for md_file in sorted(WIKI_ROOT.rglob("*.md")):
        rel = str(md_file.relative_to(WIKI_ROOT))
        if rel.startswith(("raw/", "transcripts/")):
            continue
        changes = process_file(md_file, dry_run=args.dry_run)
        if changes > 0:
            total_fixed += changes
            files_modified += 1
        count += 1
        if args.limit and count >= args.limit:
            break

    print(f"\nTotal: Fixed {total_fixed} wikilinks in {files_modified} files")


if __name__ == "__main__":
    main()
