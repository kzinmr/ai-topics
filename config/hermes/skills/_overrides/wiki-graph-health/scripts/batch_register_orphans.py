#!/usr/bin/env python3
"""
Batch-register orphan L2 pages (files on disk not in index.md)
into the wiki index, alphabetically, with header count correction.

Usage:
  python3 batch_register_orphans.py [--category concepts] [--batch-size 20] [--dry-run]

Reads from stdin or a file:
  entries.txt:
    slug1 — Description for slug1
    slug2 — Description for slug2
    ...

Or pass entries inline:
  echo "my-concept — My Concept Description" | python3 batch_register_orphans.py

Key features:
- Detects and corrects inflated section headers (header may say N but actual count is M < N)
- Updates all three top-level counters: Total pages, Indexed entries, Not in index
- Validates with scripts/validate_index.py after writing
"""

import os, re, sys

WIKI = os.path.expanduser('~/ai-topics/wiki')
INDEX_PATH = os.path.join(WIKI, 'index.md')

def parse_entries(lines):
    """Parse slug — Description entries."""
    entries = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        m = re.match(r'([\w@.-]+)\s*[—–-]\s*(.+)', line)
        if m:
            entries.append((m.group(1), m.group(2).strip()))
        else:
            print(f"⚠️  Could not parse: {line}", file=sys.stderr)
    return entries

def find_actual_count(lines, category):
    """Count actual entries in a section (regex match, not header number)."""
    pattern = re.compile(rf'^- \[\[{category}/([^|\]]+)')
    count = 0
    for line in lines:
        if pattern.match(line.strip()):
            count += 1
    return count

def find_section_boundaries(lines, section_header_prefix):
    """Find start and end line indices for a section."""
    start = end = None
    for i, line in enumerate(lines):
        if line.startswith(section_header_prefix) and start is None:
            start = i + 1  # one line after the header
        elif line.startswith('## ') and start is not None and end is None:
            end = i
            break
    return start, end

def get_header_values(lines):
    """Extract Total pages, Indexed entries, Not in index from top header."""
    vals = {}
    for i, line in enumerate(lines):
        if 'Total pages:' in line:
            m = re.search(r'Total pages: (\d+)', line)
            if m: vals['total'] = (i, int(m.group(1)))
            m2 = re.search(r'Indexed entries: (\d+)', line)
            if m2: vals['indexed'] = (i, int(m2.group(1)))
            m3 = re.search(r'Not in index: (\d+)', line)
            if m3: vals['not_indexed'] = (i, int(m3.group(1)))
            break
    return vals

def find_insertion_pos(section_lines, slug):
    """Find alphabetical insertion position within section."""
    for i, line in enumerate(section_lines):
        m = re.match(rf'- \[\[(?:entities|concepts|comparisons|events|queries)/([^|\]]+)', line.strip())
        if m and slug.lower() < m.group(1).lower():
            return i
    return len(section_lines)

def batch_insert(entries, category='concepts', dry_run=False):
    """Batch-insert entries into index.md."""
    with open(INDEX_PATH) as f:
        lines = [l.rstrip('\n') for l in f.readlines()]

    section_prefix = f'## {category.capitalize()}'
    if category == 'queries':
        section_prefix = '## Queries'

    start, end = find_section_boundaries(lines, section_prefix)
    if start is None or end is None:
        print(f"❌ Could not find section '{section_prefix}' in index.md")
        return False

    # Get actual entry count (not trusting header)
    actual_count = find_actual_count(lines, category)
    header_count_idx = None
    for i, line in enumerate(lines):
        if line.startswith(section_prefix) and '(' in line:
            header_count_idx = i
            m = re.search(r'\((\d+) pages\)', line)
            if m:
                declared = int(m.group(1))
                if declared != actual_count:
                    print(f"⚠️  Header declares {declared} but actual count is {actual_count}")
                    print(f"   Will correct to {actual_count + len(entries)}")
            break

    # Get top-level header values
    header_vals = get_header_values(lines)

    # Build entry lines
    entry_lines = [f"- [[{category}/{slug}]] — {desc}" for slug, desc in entries]

    # Insert into section (working copy)
    section = lines[start:end]
    for slug, entry_line in zip([e[0] for e in entries], entry_lines):
        pos = find_insertion_pos(section, slug)
        section.insert(pos, entry_line)

    # Rebuild full line list
    new_lines = lines[:start] + section + lines[end:]

    if dry_run:
        print(f"🔍 DRY RUN — would add {len(entries)} entries to {category}")
        print(f"   Current {category} entries: {actual_count}")
        print(f"   New {category} entries: {actual_count + len(entries)}")
        for slug, desc in entries:
            print(f"   + {slug}")
        return True

    # Update section header count
    if header_count_idx is not None:
        new_count = actual_count + len(entries)
        old_line = new_lines[header_count_idx]
        new_line = re.sub(r'\(\d+ pages\)', f'({new_count} pages)', old_line)
        new_lines[header_count_idx] = new_line
        print(f"✅ Updated header: {actual_count} → {new_count} ({category})")

    # Update top-level counters
    if header_vals:
        n = len(entries)
        total_idx, total_old = header_vals['total']
        new_lines[total_idx] = new_lines[total_idx].replace(
            f'Total pages: {total_old}', f'Total pages: {total_old + n}')

        idx_idx, idx_old = header_vals['indexed']
        new_lines[idx_idx] = new_lines[idx_idx].replace(
            f'Indexed entries: {idx_old}', f'Indexed entries: {idx_old + n}')

        not_idx, not_old = header_vals['not_indexed']
        new_lines[not_idx] = new_lines[not_idx].replace(
            f'Not in index: {not_old}', f'Not in index: {not_old - n}')

        print(f"✅ Top counters: Total {total_old}→{total_old+n}, "
              f"Indexed {idx_old}→{idx_old+n}, "
              f"Not-in-index {not_old}→{not_old-n}")

    # Write
    with open(INDEX_PATH, 'w') as f:
        f.write('\n'.join(new_lines) + '\n')

    print(f"✅ Wrote {len(entries)} entries to {category} section")
    return True

def validate():
    """Run validate_index.py."""
    import subprocess
    result = subprocess.run(
        ['python3', os.path.expanduser('~/ai-topics/scripts/validate_index.py')],
        capture_output=True, text=True, cwd=os.path.expanduser('~/ai-topics')
    )
    print(result.stdout.strip())
    if result.returncode != 0:
        print(f"❌ Validation FAILED: {result.stderr}")
        return False
    return True


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Batch-register orphan wiki pages')
    parser.add_argument('--category', '-c', default='concepts',
                        choices=['concepts', 'entities', 'comparisons', 'events', 'queries'])
    parser.add_argument('--batch-size', '-b', type=int, default=20)
    parser.add_argument('--dry-run', '-n', action='store_true')
    parser.add_argument('--skip-validation', '-s', action='store_true')
    parser.add_argument('entries_file', nargs='?', help='File with slug — Description entries')
    args = parser.parse_args()

    if args.entries_file:
        with open(args.entries_file) as f:
            entries = parse_entries(f.readlines())
    elif not sys.stdin.isatty():
        entries = parse_entries(sys.stdin.readlines())
    else:
        print("❌ No entries provided. Pipe entries via stdin or pass a file path.")
        sys.exit(1)

    if not entries:
        print("❌ No valid entries parsed.")
        sys.exit(1)

    entries = entries[:args.batch_size]
    print(f"📋 Processing {len(entries)} entries for '{args.category}'...")

    if not batch_insert(entries, args.category, args.dry_run):
        sys.exit(1)

    if not args.dry_run and not args.skip_validation:
        if not validate():
            print("⚠️  Validation failed — restore with: git checkout ~/ai-topics/wiki/index.md")
            sys.exit(1)

    print("✅ Done.")
