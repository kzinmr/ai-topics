#!/usr/bin/env python3
"""Add `updated` date to wiki pages that have frontmatter but lack the field.

Usage:
    python3 add_updated_dates.py [--date YYYY-MM-DD]

Default date is today. Only processes entities/, concepts/, comparisons/ (skips raw/, _index.md, and permission-denied files).
"""

import re, os, sys
from datetime import date

WIKI = "/opt/data/ai-topics/wiki"
DIRS = ['entities', 'concepts', 'comparisons']

def main():
    today = date.today().isoformat()
    if '--date' in sys.argv:
        idx = sys.argv.index('--date')
        today = sys.argv[idx + 1]
    
    fixed = 0
    for subdir in DIRS:
        path = os.path.join(WIKI, subdir)
        if not os.path.isdir(path):
            continue
        for root, dirs, files in os.walk(path):
            for f in files:
                if not f.endswith('.md'):
                    continue
                if f == '_index.md':
                    continue
                filepath = os.path.join(root, f)
                try:
                    with open(filepath) as fh:
                        content = fh.read()
                except PermissionError:
                    continue
                
                if not content.startswith('---'):
                    continue
                
                if re.search(r'^updated:', content, re.MULTILINE):
                    continue
                
                # Add updated field after created field
                if 'created:' in content[:500]:
                    new_content = re.sub(
                        r'(created:\s*\S.*)',
                        r'\1\nupdated: ' + today,
                        content,
                        count=1
                    )
                else:
                    # No created field — add before closing ---
                    fm_end = content.index('---', 3)
                    new_content = content[:fm_end] + f'updated: {today}\n' + content[fm_end:]
                
                with open(filepath, 'w') as fh:
                    fh.write(new_content)
                fixed += 1
    
    print(f"Added updated: {today} to {fixed} pages")

if __name__ == '__main__':
    main()
