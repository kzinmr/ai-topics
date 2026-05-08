#!/usr/bin/env python3
"""
Pre-commit hook: validate that all tags in staged wiki pages exist in SCHEMA.md taxonomy.

Usage: Automatically triggered by git commit on wiki/ files.
       Also runnable directly: python3 .githooks/pre-commit-tag-validator.py

Exit codes: 0 = clean (no violations), 1 = violations found (block commit)
"""
import re, os, sys, subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = REPO_ROOT / "wiki"
SCHEMA_PATH = WIKI_DIR / "SCHEMA.md"

def load_valid_tags():
    """Extract all valid tags from SCHEMA.md taxonomy."""
    if not SCHEMA_PATH.exists():
        print("⚠️  SCHEMA.md not found — skipping tag validation")
        return set()
    
    with open(SCHEMA_PATH) as f:
        content = f.read()
    
    m = re.search(r'## Tag Taxonomy.*?\n(.*?)(?=^## |\Z)', content, re.DOTALL | re.MULTILINE)
    if not m:
        return set()
    
    tax_text = m.group(1)
    
    # Backtick-quoted tags: `tag-name`
    backtick = set(re.findall(r'`([a-z][a-z0-9_-]+)`', tax_text))
    
    # Bold-prefixed comma-separated: - **Category**: tag1, tag2
    bold_lines = re.findall(r'-\s+\*\*[^*]+\*\*:\s*(.+?)$', tax_text, re.MULTILINE)
    plain_tags = set()
    for line in bold_lines:
        for tag in re.split(r',\s*', line):
            tag = tag.strip()
            if tag and re.match(r'^[a-z][a-z0-9_-]+$', tag):
                plain_tags.add(tag)
    
    return backtick | plain_tags


def extract_tags_from_file(filepath):
    """Extract all tags from a wiki page's frontmatter."""
    try:
        with open(filepath) as f:
            content = f.read()
    except Exception:
        return []
    
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return []
    
    front = m.group(1)
    tags = []
    
    # Inline: tags: [tag1, tag2]
    inline = re.search(r'^tags:\s*\[(.+?)\]', front, re.MULTILINE)
    if inline:
        tags = [t.strip().strip('"\'').strip() for t in inline.group(1).split(',') if t.strip()]
        return tags
    
    # Block: tags:\n  - tag1\n  - tag2
    block = re.search(r'^tags:\n((?:\s*- .*\n?)+)', front, re.MULTILINE)
    if block:
        for line in block.group(1).split('\n'):
            line = line.strip()
            if line.startswith('- '):
                tag = line[2:].strip().strip('"\'')
                if tag:
                    tags.append(tag)
    
    return tags


def get_staged_wiki_files():
    """Get list of staged wiki .md files (new or modified, not deleted)."""
    try:
        result = subprocess.run(
            ['git', 'diff', '--cached', '--name-only', '--diff-filter=ACM'],
            capture_output=True, text=True, cwd=str(REPO_ROOT)
        )
        files = [f for f in result.stdout.strip().split('\n') 
                 if f.startswith('wiki/') and f.endswith('.md')
                 and not f.startswith('wiki/raw/')  # Skip raw articles
                 and '_index' not in f]  # Skip index files
        return files
    except Exception:
        return []


def is_composite_kebab(tag):
    """Check if tag is a composite kebab-case error (5+ word parts)."""
    parts = tag.split('-')
    return len(parts) >= 5 and all(p.isalpha() or p.isdigit() for p in parts)


def main():
    valid_tags = load_valid_tags()
    if not valid_tags:
        sys.exit(0)  # Can't validate without SCHEMA
    
    staged_files = get_staged_wiki_files()
    if not staged_files:
        sys.exit(0)  # No wiki files staged
    
    violations = []
    for filepath in staged_files:
        full_path = REPO_ROOT / filepath
        tags = extract_tags_from_file(full_path)
        
        for tag in tags:
            # Check composite kebab (always an error)
            if is_composite_kebab(tag):
                violations.append((filepath, tag, "COMPOSITE_KEBAB"))
                continue
            
            # Check if tag is in SCHEMA taxonomy
            if tag not in valid_tags:
                violations.append((filepath, tag, "NOT_IN_SCHEMA"))
    
    if violations:
        # Group by type
        kebab_violations = [(f, t) for f, t, v in violations if v == "COMPOSITE_KEBAB"]
        schema_violations = [(f, t) for f, t, v in violations if v == "NOT_IN_SCHEMA"]
        
        print("\n" + "=" * 70)
        print("🚨 TAG TAXONOMY VIOLATIONS — COMMIT BLOCKED")
        print("=" * 70)
        
        if kebab_violations:
            print(f"\n❌ COMPOSITE KEBAB-CASE TAGS ({len(kebab_violations)}):")
            print("   These are single tags with 5+ hyphen-joined words — always errors.")
            for filepath, tag in kebab_violations:
                print(f"   {filepath}:  {tag}")
            print("\n   Fix: Decompose into individual tags. Example:")
            print("   'ai-agents-autonomy-planning-sandbox' → 'ai-agents', 'autonomy', 'sandbox'")
        
        if schema_violations:
            print(f"\n⚠️  TAGS NOT IN SCHEMA.md TAXONOMY ({len(schema_violations)}):")
            for filepath, tag in schema_violations:
                print(f"   {filepath}:  {tag}")
            print(f"\n   Fix options:")
            print(f"   1. Add '{schema_violations[0][1]}' to SCHEMA.md taxonomy (if it's a valid new category)")
            print(f"   2. Map it to an existing canonical tag in scripts/tag_normalization.py")
            print(f"   3. Use an existing SCHEMA tag instead")
        
        print(f"\n   To override (emergency only):")
        print(f"   git commit --no-verify")
        print(f"\n   SCHEMA.md has {len(valid_tags)} canonical tags.")
        print("=" * 70 + "\n")
        sys.exit(1)
    
    print(f"✅ Tag validation passed — {len(staged_files)} files, all tags in SCHEMA taxonomy")
    sys.exit(0)


if __name__ == '__main__':
    main()
