#!/usr/bin/env python3
"""
Quick script to validate and optionally fix the wiki_graph_analysis_weekly.py bugs.
Usage:
  python3 scripts/fix-weekly-graph-analysis-script.py  # dry-run, shows what to fix
  python3 scripts/fix-weekly-graph-analysis-script.py --apply  # applies fixes
"""
import os, re, sys

SCRIPT_PATH = os.path.expanduser('~/ai-topics/scripts/wiki_graph_analysis_weekly.py')
DRY_RUN = '--apply' not in sys.argv

def check_and_fix():
    with open(SCRIPT_PATH) as f:
        content = f.read()
    
    fixes = []
    
    # Bug 1: Hardcoded date in filename (line ~372)
    m = re.search(r"report_path = .*?wiki-graph-analysis-weekly-\d{4}-\d{2}-\d{2}", content)
    if m and 'datetime.now()' not in content[m.start():m.end()+100]:
        fixes.append(('hardcoded date in filename', 
                      "Replace with: report_path = f'/opt/data/ai-topics/wiki/queries/wiki-graph-analysis-weekly-{datetime.now().strftime(\"%Y-%m-%d\")}.md'"))
    
    # Bug 2: Template expansion error (line ~386)
    if 'content_rich_orphans.__class__.__name__' in content:
        fixes.append(('template expansion error',
                      "Replace 'content_rich_orphans.__class__.__name__' with 'len(content_rich_orphans)'"))
    
    return fixes

fixes = check_and_fix()
if not fixes:
    print("✅ No issues found")
    sys.exit(0)

print(f"Found {len(fixes)} issue(s) in {SCRIPT_PATH}:")
for issue, fix in fixes:
    print(f"\n  🔴 {issue}")
    print(f"     Fix: {fix}")
    
if DRY_RUN:
    print("\n⚠️  Dry-run mode (use --apply to fix)")
else:
    # Apply fixes
    with open(SCRIPT_PATH) as f:
        content = f.read()
    content = content.replace(
        "content_rich_orphans.__class__.__name__",
        "len(content_rich_orphans)"
    )
    with open(SCRIPT_PATH, 'w') as f:
        f.write(content)
    print("\n✅ Fixes applied")
