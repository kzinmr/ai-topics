#!/usr/bin/env python3
"""
Tag Audit Script for LLM Wiki
Scans all wiki pages, identifies tag issues, and suggests fixes.

Usage:
  python3 scripts/tag_audit.py              # Dry run: report only
  python3 scripts/tag_audit.py --fix-composites  # Auto-decompose composite tags
  python3 scripts/tag_audit.py --suggest-additions # Suggest tags to add to SCHEMA.md
"""

import os
import re
import json
import argparse
from collections import Counter, defaultdict
from pathlib import Path

WIKI_ROOT = Path.home() / "ai-topics" / "wiki"
SCHEMA_PATH = WIKI_ROOT / "SCHEMA.md"

def load_valid_tags():
    """Extract valid tags from SCHEMA.md taxonomy section.
    
    Handles two SCHEMA formats:
    1. Backtick-quoted: `tag-name`
    2. Bold-category comma-separated: - **Category**: tag1, tag2, tag3
    """
    with open(SCHEMA_PATH) as f:
        content = f.read()
    match = re.search(r'## Tag Taxonomy.*?\n(.*?)(?=^## |\Z)', content, re.DOTALL | re.MULTILINE)
    if not match:
        return set()
    tax_text = match.group(1)
    
    # Format 1: backtick-quoted tags (`tag-name`)
    backtick = set(re.findall(r'`([a-z][a-z0-9_-]+)`', tax_text))
    
    # Format 2: bold-prefixed comma-separated (- **Category**: tag1, tag2, ...)
    bold_lines = re.findall(r'-\s+\*\*[^*]+\*\*:\s*(.+?)$', tax_text, re.MULTILINE)
    plain_tags = set()
    for line in bold_lines:
        for tag in re.split(r',\s*', line):
            tag = tag.strip()
            if tag and re.match(r'^[a-z][a-z0-9_-]+$', tag):
                plain_tags.add(tag)
    
    return backtick | plain_tags

def is_composite_kebab_tag(tag):
    """Check if a tag is a composite kebab-case tag (always an error)."""
    words = tag.split('-')
    return len(words) >= 5 and all(w.isalpha() for w in words)

def decompose_composite_tag(tag):
    """Attempt to decompose a composite tag into individual meaningful tags."""
    # Split on common boundaries
    parts = re.split(r'[-_]', tag)
    
    # Group into meaningful units (simplified - may need manual review)
    decomposed = []
    i = 0
    while i < len(parts):
        # Try to form meaningful 1-2 word tags
        if i + 1 < len(parts):
            two_word = f"{parts[i]}-{parts[i+1]}"
            if len(two_word) <= 20:  # Reasonable tag length
                decomposed.append(two_word)
                i += 2
                continue
        decomposed.append(parts[i])
        i += 1
    
    return list(set(decomposed))  # Unique tags

def scan_all_tags():
    """Scan all wiki pages and collect tag usage.
    
    Handles both tag frontmatter formats:
    1. Inline: tags: [tag1, tag2]
    2. Block: tags:\n  - tag1\n  - tag2
    """
    tag_usage = defaultdict(list)  # tag -> list of files using it
    total_pages_with_tags = 0
    
    for root, dirs, files in os.walk(WIKI_ROOT):
        # Skip non-wiki directories
        skip = {'raw', 'inbox', '.git', 'config', 'scripts', '.hermes', '__pycache__', '_archive'}
        dirs[:] = [d for d in dirs if d not in skip]
        
        for fname in files:
            if not fname.endswith('.md'):
                continue
            fpath = os.path.join(root, fname)
            rel_path = os.path.relpath(fpath, WIKI_ROOT)
            
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract frontmatter
                fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
                if not fm_match:
                    continue
                total_pages_with_tags += 1
                front = fm_match.group(1)
                
                # Format 1: Block format (tags:\n  - tag1\n  - tag2)
                block_match = re.search(r'^tags:\n((?:\s*- .*\n?)+)', front, re.MULTILINE)
                if block_match:
                    for line in block_match.group(1).split('\n'):
                        line = line.strip()
                        if line.startswith('- '):
                            tag = line[2:].strip().strip('"\'')
                            if tag:
                                tag_usage[tag].append(rel_path)
                    continue
                
                # Format 2: Inline format (tags: [tag1, tag2])
                inline_match = re.search(r'^tags:\s*\[(.+?)\]', front, re.MULTILINE)
                if inline_match:
                    for t in inline_match.group(1).split(','):
                        tag = t.strip().strip('"\'')
                        if tag:
                            tag_usage[tag].append(rel_path)
            except Exception as e:
                print(f"Error reading {rel_path}: {e}")
    
    return tag_usage, total_pages_with_tags

def suggest_taxonomy_additions(tag_usage, valid_tags, min_usage=3):
    """Suggest tags to add to SCHEMA.md based on frequent usage."""
    suggestions = []
    for tag, files in sorted(tag_usage.items(), key=lambda x: len(x[1]), reverse=True):
        if tag not in valid_tags and not is_composite_kebab_tag(tag) and len(files) >= min_usage:
            suggestions.append((tag, len(files)))
    return suggestions

def main():
    parser = argparse.ArgumentParser(description='Wiki Tag Audit Tool')
    parser.add_argument('--fix-composites', action='store_true', help='Auto-decompose composite tags')
    parser.add_argument('--suggest-additions', action='store_true', help='Suggest tags for SCHEMA.md')
    parser.add_argument('--min-usage', type=int, default=3, help='Minimum tag usage for suggestions')
    args = parser.parse_args()
    
    print("🔍 Loading valid tags from SCHEMA.md...")
    valid_tags = load_valid_tags()
    print(f"   Found {len(valid_tags)} valid tags")
    
    print("📊 Scanning all wiki pages...")
    tag_usage, total_pages = scan_all_tags()
    print(f"   Scanned {total_pages} pages with tags")
    print(f"   Found {len(tag_usage)} unique tags in use")
    
    # Identify issues
    composite_tags = [(tag, files) for tag, files in tag_usage.items() if is_composite_kebab_tag(tag)]
    invalid_tags = [(tag, files) for tag, files in tag_usage.items() if tag not in valid_tags and not is_composite_kebab_tag(tag)]
    
    print(f"\n{'='*60}")
    print(f"TAG AUDIT REPORT")
    print(f"{'='*60}")
    
    # Composite tags (always errors)
    print(f"\n🚨 COMPOSITE KEBAB-CASE TAGS (always errors): {len(composite_tags)}")
    for tag, files in sorted(composite_tags, key=lambda x: len(x[1]), reverse=True)[:10]:
        print(f"   {tag[:60]}{'...' if len(tag)>60 else ''} (used in {len(files)} files)")
        if len(tag) > 80:  # Only show decomposition for very long ones
            decomposed = decompose_composite_tag(tag)
            print(f"     → Suggest: {', '.join(decomposed[:5])}")
    
    # Invalid tags
    print(f"\n⚠️  TAGS NOT IN SCHEMA TAXONOMY: {len(invalid_tags)}")
    for tag, files in sorted(invalid_tags, key=lambda x: len(x[1]), reverse=True)[:20]:
        print(f"   {tag} (used in {len(files)} files)")
    
    # Suggestions
    if args.suggest_additions:
        suggestions = suggest_taxonomy_additions(tag_usage, valid_tags, args.min_usage)
        print(f"\n💡 SUGGESTED ADDITIONS TO SCHEMA.md (usage >= {args.min_usage}):")
        for tag, count in suggestions:
            print(f"   - {tag} ({count} uses)")
    
    # Summary stats
    print(f"\n📈 SUMMARY:")
    print(f"   Total pages with tags: {total_pages}")
    print(f"   Unique tags in use: {len(tag_usage)}")
    print(f"   Tags in SCHEMA taxonomy: {len(valid_tags)}")
    print(f"   Tags NOT in taxonomy: {len(invalid_tags)}")
    print(f"   Composite tags (errors): {len(composite_tags)}")
    print(f"   Coverage: {len(valid_tags)/max(len(tag_usage),1)*100:.1f}% of used tags are valid")

if __name__ == '__main__':
    main()
