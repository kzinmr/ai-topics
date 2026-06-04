#!/usr/bin/env python3
"""
Fix log.md header burial: orphaned entries sitting before the # Wiki Log header.

Detection: head -1 wiki/log.md does NOT start with '# Wiki Log'

Pattern: Prepend operations (bookmark-ingest, active-crawl, dreaming, etc.)
push new entries at position 0, burying the '# Wiki Log' header below.
The header still exists (grep -c returns 1) but at line 30-35 instead of line 1.

Usage:
  python3 scripts/fix_log_header_burial.py [--path PATH] [--dry-run]

  Default PATH: ~/ai-topics/wiki/log.md
  --dry-run: Print what would be done without modifying the file.
  --no-backup: Skip writing a .bak backup file.
"""

import os
import sys
import shutil

def fix_log_header_burial(log_path, dry_run=False, backup=True):
    if not os.path.exists(log_path):
        print(f"ERROR: File not found: {log_path}")
        return False

    with open(log_path) as f:
        lines = f.readlines()
    total = len(lines)
    print(f"Total lines: {total}")

    # Find the # Wiki Log header
    header_idx = None
    for i, line in enumerate(lines):
        if line.rstrip() == '# Wiki Log':
            header_idx = i
            break

    if header_idx is None:
        print("ERROR: No '# Wiki Log' header found in file.")
        return False

    if header_idx == 0:
        print("✅ Header already at line 1 — no burial detected.")
        return False

    print(f"Header buried at line {header_idx + 1} (expected line 1)")
    orphaned = lines[:header_idx]
    
    # Determine header block extent: find the blank line after header metadata
    block_end = header_idx + 1
    while block_end < len(lines) and lines[block_end].strip():
        block_end += 1
    block_end += 1  # include the trailing blank line
    
    header_block = lines[header_idx:block_end]
    chrono_entries = lines[block_end:]
    
    # Clean trailing blank from orphaned
    while orphaned and orphaned[-1].strip() == '':
        orphaned.pop()
    
    # Scan all blocks for standalone pipe corruption
    pipe_fixes = 0
    for block, name in [
        (orphaned, 'orphaned'), (header_block, 'header'), (chrono_entries, 'chrono')
    ]:
        for i, line in enumerate(block):
            if line.strip() == '|':
                if not dry_run:
                    block[i] = '\n'
                pipe_fixes += 1
                print(f"  Pipe corruption in {name} block")
    
    # Reconstruct
    separator = '---\n'
    new_lines = header_block + ['\n'] + orphaned + ['\n', separator, '\n'] + chrono_entries
    
    if dry_run:
        print(f"\nDRY RUN — would fix:")
        print(f"  - Move {len(orphaned)} orphaned lines after header")
        print(f"  - Remove {pipe_fixes} standalone pipe corruption(s)")
        print(f"  - New file: {len(new_lines)} lines (was {total})")
        return True
    
    # Write backup
    if backup:
        backup_path = log_path + '.bak'
        shutil.copy2(log_path, backup_path)
        print(f"Backup: {backup_path}")
    
    # Write fix
    with open(log_path, 'w') as f:
        f.writelines(new_lines)
    print(f"Fixed: {len(new_lines)} lines written")
    
    # Verify
    with open(log_path) as f:
        first = f.readline().rstrip()
    assert first == '# Wiki Log', f"VERIFY FAILED: First line is '{first}', not '# Wiki Log'"
    
    with open(log_path) as f:
        remaining_pipes = sum(1 for line in f if line.strip() == '|')
    assert remaining_pipes == 0, f"VERIFY FAILED: {remaining_pipes} pipe corruption(s) remain"
    
    print("✅ Verification passed — header at line 1, no pipe corruption")
    print(f"\nSummary:")
    print(f"  - Header moved from line {header_idx + 1} to line 1")
    print(f"  - {len(orphaned)} orphaned lines moved after header")
    print(f"  - {pipe_fixes} pipe corruption(s) removed")
    return True


if __name__ == '__main__':
    log_path = os.path.expanduser('~/ai-topics/wiki/log.md')
    dry_run = '--dry-run' in sys.argv
    no_backup = '--no-backup' in sys.argv
    
    for i, arg in enumerate(sys.argv):
        if arg.startswith('--path='):
            log_path = os.path.expanduser(arg.split('=', 1)[1])
        elif arg == '--path' and i + 1 < len(sys.argv):
            log_path = os.path.expanduser(sys.argv[i + 1])
    
    print(f"Log: {log_path}")
    print(f"Dry run: {dry_run}")
    print(f"Backup: {'no' if no_backup else 'yes'}")
    print()
    
    result = fix_log_header_burial(log_path, dry_run=dry_run, backup=not no_backup)
    sys.exit(0 if result else 1)
