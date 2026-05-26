#!/usr/bin/env python3
"""
Pre-commit Japanese character detection hook.
Blocks introduction of Japanese text into previously JP-clean wiki files.
Warns (but allows) JP changes to files still in the translation backlog.
"""

import subprocess
import sys
import re
import os

JP_PATTERN = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF]')
REPO_ROOT = subprocess.check_output(
    ['git', 'rev-parse', '--show-toplevel'], text=True
).strip()

# Mapping: (repo_root, subpath) -> (pre-commit, post-commit) JP char count
# Returns None if error; returns (count, None) if file doesn't exist in that ref
def count_jp(ref, filepath):
    try:
        content = subprocess.check_output(
            ['git', 'show', f'{ref}:{filepath}'],
            stderr=subprocess.DEVNULL, text=True
        )
    except subprocess.CalledProcessError:
        return None  # file doesn't exist in that ref
    
    lines = content.split('\n')
    # Skip YAML frontmatter
    body_start = 0
    fm_count = 0
    for i, line in enumerate(lines):
        if line.strip() == '---':
            fm_count += 1
            if fm_count == 2:
                body_start = i + 1
                break
    if fm_count < 2:
        body_start = 0
    body = '\n'.join(lines[body_start:])
    return len(JP_PATTERN.findall(body))


def main():
    # Get staged wiki files (excluding raw/)
    staged = subprocess.check_output(
        ['git', 'diff', '--cached', '--name-only', '--diff-filter=ACM'],
        text=True
    ).strip().split('\n')
    
    wiki_files = [
        f for f in staged
        if f.startswith('wiki/') and f.endswith('.md') and not f.startswith('wiki/raw/')
    ]
    
    if not wiki_files:
        return 0
    
    blocks = []
    warnings = []
    
    for filepath in wiki_files:
        # Count JP chars before and after this commit
        before = count_jp('HEAD', filepath)
        after = count_jp(':0', filepath)  # :0 = staged version
        
        if before is None:
            # New file - check if it introduces JP
            if after is not None and after > 0:
                blocks.append((filepath, 0, after, "NEW FILE with Japanese content"))
            continue
        
        if after is None:
            continue
        
        if before == 0 and after > 0:
            # Previously clean file now has JP → BLOCK
            blocks.append((filepath, before, after, "NEW Japanese introduced to clean file"))
        elif before > 0 and after > before:
            # JP increased in file still in backlog → WARN
            warnings.append((filepath, before, after))
    
    # Report
    if warnings:
        print("⚠️  WARNING: Japanese content increased in files still in translation backlog:")
        for fp, before, after in warnings:
            print(f"   {fp}: {before} → {after} JP chars (+{after-before})")
        print("   These files are being actively translated and will be cleaned by cron job.")
        print()
    
    if blocks:
        print("❌ BLOCKED: Japanese content introduced to previously clean files:")
        for fp, before, after, reason in blocks:
            print(f"   {reason}: {fp}")
        print()
        print("   Wiki language policy: All non-raw/ wiki content must be in English.")
        print("   To skip this check: git commit --no-verify")
        return 1
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
