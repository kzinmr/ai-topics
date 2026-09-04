#!/usr/bin/env python3
"""Classify tag_normalization.py --dry-run pages: real violations vs preference rewrites.

tag_normalization.py's TAG_NORMALIZATION dict contains BOTH:
  - mappings for genuine non-SCHEMA tags (violations — should be applied)
  - preference rewrites that map VALID SCHEMA tags to less-specific canonicals
    (e.g. knowledge-graph->rag, gpu->hardware, mixture-of-experts->model,
    google-deepmind->google) — running these degrades tag specificity across
    unrelated pages.

This script imports tag_normalization.py, simulates the per-page tag diffs, and
classifies each page by whether any source tag is absent from SCHEMA.md
(violation) or all source tags are valid (preference rewrite). Run it BEFORE
deciding whether to apply wholesale normalization.

Observed 2026-08-10: 95 dry-run pages, only 3 genuine violations -> wholesale
normalization was skipped; fixes applied manually.

Usage:
    python3 scripts/tag_normalization_diff_scan.py [norm_script_path] [wiki_root]
"""
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
NORM_PATH = os.path.join(HERE, "tag_normalization.py")
if len(sys.argv) > 1:
    NORM_PATH = sys.argv[1]
WIKI = os.path.expanduser("~/wiki")
if len(sys.argv) > 2:
    WIKI = sys.argv[2]

spec = importlib.util.spec_from_file_location("tn", NORM_PATH)
tn = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tn)

schema = open(os.path.join(WIKI, "SCHEMA.md")).read()

violation_pages = {}
preference_pages = {}
for root_dir in ["entities", "concepts", "comparisons", "events", "queries"]:
    for root, dirs, files in os.walk(os.path.join(WIKI, root_dir)):
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            content = open(path).read()
            m = tn.re.match(r"^(---\n)(.*?)(\n---)", content, tn.re.DOTALL)
            if not m:
                continue
            tags = tn.extract_tags_from_frontmatter(m.group(2))
            if not tags:
                continue
            mapped = [tn.TAG_NORMALIZATION.get(t, t) for t in tags]
            if mapped != tags:
                diffs = [(a, b) for a, b in zip(tags, mapped) if a != b]
                rel = os.path.relpath(path, WIKI)
                is_violation = any(
                    re.search(r"\b" + re.escape(a) + r"\b", schema) is None
                    for a, b in diffs
                )
                bucket = violation_pages if is_violation else preference_pages
                bucket[rel] = diffs

print("=== REAL VIOLATION PAGES (source tag not in SCHEMA) ===")
for rel, diffs in sorted(violation_pages.items()):
    print(f"  {rel}: {diffs}")
print("\n=== PREFERENCE-REWRITE PAGES (source tag IS valid SCHEMA) ===")
for rel, diffs in sorted(preference_pages.items()):
    print(f"  {rel}: {diffs}")
print(f"\nTotal violation pages: {len(violation_pages)}")
print(f"Total preference-rewrite pages: {len(preference_pages)}")
