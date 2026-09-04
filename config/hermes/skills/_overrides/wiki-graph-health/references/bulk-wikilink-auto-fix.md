# Bulk Wikilink Auto-Fix Workflow

Procedure for detecting and auto-fixing broken wikilinks across all wiki pages.

## Detection (from wiki-graph-analysis output)

Broken wikilinks fall into 4 categories:

| Type | Count (2026-07-05) | Auto-fixable? |
|------|--------------------|---------------|
| bare-wikilink-missing | 2,684 | No — target page doesn't exist |
| missing (namespaced) | 1,209 | No — target page doesn't exist |
| bare-wikilink | 931 | **Yes** — add namespace prefix |
| cross-namespace | 66 | **Yes** — fix namespace mismatch |

## Fix Script

```python
#!/usr/bin/env python3
"""Fix auto-fixable wikilinks: bare → namespaced, cross-namespace corrections."""
import os, re
from pathlib import Path

WIKI_ROOT = Path("/opt/data/ai-topics/wiki")
NAMESPACES = ["entities", "concepts", "comparisons", "queries", "events"]

def find_file_in_namespaces(bare_name):
    for ns in NAMESPACES:
        if (WIKI_ROOT / ns / f"{bare_name}.md").exists():
            return ns
        if (WIKI_ROOT / ns / bare_name / "_index.md").exists():
            return ns
        if (WIKI_ROOT / ns / bare_name / "index.md").exists():
            return ns
    return None

def fix_bare_wikilinks(content):
    def replace_bare(match):
        wikilink = match.group(1)
        if "/" in wikilink or wikilink.startswith("#") or wikilink.startswith("^"):
            return match.group(0)
        ns = find_file_in_namespaces(wikilink)
        return f"[[{ns}/{wikilink}]]" if ns else match.group(0)
    return re.sub(r'\[\[([^\]|/]+)\]\]', replace_bare, content)

def fix_cross_namespace(content):
    def replace_cross(match):
        full, current_ns, name = match.group(0), match.group(1), match.group(2)
        for ns in NAMESPACES:
            if ns != current_ns and (WIKI_ROOT / ns / f"{name}.md").exists():
                return f"[[{ns}/{name}]]"
        return full
    return re.sub(r'\[\[((?:entities|concepts|comparisons|queries|events)/([^\]|]+))\]\]', replace_cross, content)
```

## Pitfalls

### 1. Scale can be massive
The 2026-07-05 run fixed **14,358 links** across **980 files** — far exceeding the expected 997. This is because cross-namespace fixes cascade (e.g., `[[concepts/concepts/foo]]` → `[[concepts/foo]]` from prior wiki-link correction artifacts).

### 2. Skip raw/ and transcripts/
The script must skip `raw/` and `transcripts/` directories — these are Layer 1 immutable sources.

### 3. verify after commit
Run `git diff --stat` before committing. 980+ files is normal for bulk fixes but may conflict with other pipeline changes. Stash non-wiki changes first:
```bash
git stash push -- config/   # stash non-wiki changes
git pull --rebase origin main
git stash pop
git add wiki/
git commit -m "wiki: fix auto-fixable wikilinks"
git push
```

### 4. Entities index may use bare wikilinks
The `entities/_index.md` often uses bare `[[foo]]` links internally. These are valid within the index but should be namespaced for cross-page consistency. The fix script handles this correctly.

### 5. False positives in cross-namespace fix
If a page exists in BOTH `entities/foo` and `concepts/foo`, the cross-namespace fix picks the FIRST match in NAMESPACES order. This may not be the intended target. After bulk fix, spot-check pages where both namespaces exist.
