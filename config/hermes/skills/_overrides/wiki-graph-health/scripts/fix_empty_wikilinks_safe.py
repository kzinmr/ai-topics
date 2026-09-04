#!/usr/bin/env python3
"""Safe empty-wikilink fixer for the ai-topics wiki (entities/ + concepts/).

Fixes lines matching '  - — description' (missing [[slug]] anchor) ONLY when the
proposed target resolves to an existing page. Corrects stale/wrong-namespaced
entries from fix_broken_wikilinks.py's KNOWN_MAPPINGS via an OVERRIDES map.

Why this exists (2026-08-05): the raw `fix_broken_wikilinks.py` proposes 107
fixes of which 78 (73%) point to non-existent files, and its
`line.replace('- — ', ...)` misses the dominant DOUBLE-space `-  — ` format
(phantom fixes). This version is regex-based, target-verified, and dry-run by
default.

Usage:
  /opt/data/.hermes/venv/bin/python fix_empty_wikilinks_safe.py            # dry-run
  /opt/data/.hermes/venv/bin/python fix_empty_wikilinks_safe.py --apply    # write
  /opt/data/.hermes/venv/bin/python fix_empty_wikilinks_safe.py --verify   # count remaining

Requires PyYAML (system python3 lacks it — use the Hermes venv python).
"""
import os
import re
import sys
import importlib.util

# Original script provides KNOWN_MAPPINGS / find_slug_for_description. Its path
# differs from the skill's implied scripts/ location.
for cand in ("/opt/data/scripts/fix_broken_wikilinks.py",
             os.path.expanduser("~/ai-topics/config/hermes/skills/_overrides/wiki-graph-health/scripts/fix_broken_wikilinks.py")):
    if os.path.exists(cand):
        spec = importlib.util.spec_from_file_location("fbw", cand)
        fbw = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(fbw)
        break
else:
    raise SystemExit("ERROR: fix_broken_wikilinks.py not found — cannot load KNOWN_MAPPINGS")

WIKI_DIR = fbw.WIKI_DIR

# Corrected targets for stale / wrong-namespaced KNOWN_MAPPINGS entries.
# Verify each target exists on disk before relying on it (subdirectory org:
# `concepts/evaluation/ai-evals.md`, not `concepts/ai-evals.md`).
OVERRIDES = {
    'concepts/ai-evals': 'concepts/evaluation/ai-evals',
    'concepts/ai-safety': 'concepts/security-and-governance/ai-safety',
    'concepts/agentic-coding': 'concepts/coding-agents/agentic-coding',
    'concepts/chatgpt-memory-bitter-lesson': 'concepts/gpt/chatgpt-memory-bitter-lesson',
    'concepts/google': 'entities/google',
    'concepts/nvidia': 'entities/nvidia',
    'concepts/meta': 'entities/meta',
    'concepts/nous-research': 'entities/nous-research',
}

LINE_RE = re.compile(r'^(\s*)-\s+—\s+(.*)$')


def resolve_target(slug):
    """Resolve slug to a linkable target path that exists (flat file OR subdir).

    Namespaced slug: keep as-is if it resolves. Bare entity slug: resolve to
    entities/<slug> (then concepts/<slug>). Returns None when no existing target.
    """
    if '/' in slug:
        if os.path.exists(os.path.join(WIKI_DIR, slug + '.md')):
            return slug
        if os.path.isdir(os.path.join(WIKI_DIR, slug)):
            return slug
        return None
    for ns in ('entities', 'concepts'):
        cand = f'{ns}/{slug}'
        if os.path.exists(os.path.join(WIKI_DIR, cand + '.md')):
            return cand
        if os.path.isdir(os.path.join(WIKI_DIR, cand)):
            return cand
    return None


def walk_files():
    files = []
    for root in (fbw.ENTITY_DIR, fbw.CONCEPT_DIR):
        for dirpath, dirnames, filenames in os.walk(root):
            if '_archive' in dirpath.split(os.sep):
                dirnames[:] = []
                continue
            for f in filenames:
                if f.endswith('.md'):
                    files.append(os.path.join(dirpath, f))
    return files


def main():
    dry_run = '--apply' not in sys.argv
    verify_only = '--verify' in sys.argv
    files = walk_files()
    total_broken = 0
    total_fixed = 0
    changed_files = []
    skipped = []

    for filepath in sorted(files):
        with open(filepath) as fh:
            content = fh.read()
        lines = content.split('\n')
        file_broken = 0
        file_fixed = 0
        file_skipped = []
        for i, line in enumerate(lines):
            m = LINE_RE.match(line)
            if not m:
                continue
            file_broken += 1
            desc = m.group(2).strip()
            slug = fbw.find_slug_for_description(desc)
            if not slug:
                file_skipped.append((i + 1, desc[:60], 'no-match'))
                continue
            target = OVERRIDES.get(slug, slug)
            resolved = resolve_target(target)
            if not resolved:
                file_skipped.append((i + 1, desc[:60], f'missing:{target}'))
                continue
            lines[i] = f"{m.group(1)}- [[{resolved}]] — {desc}"
            file_fixed += 1
        if file_broken:
            total_broken += file_broken
            total_fixed += file_fixed
            rel = os.path.relpath(filepath, WIKI_DIR)
            if file_fixed:
                changed_files.append(rel)
                if not dry_run and not verify_only:
                    with open(filepath, 'w') as fh:
                        fh.write('\n'.join(lines))
            for ln, desc, why in file_skipped[:2]:
                skipped.append(f"  {rel}:{ln} [{why}] {desc}")

    print(f"Files scanned: {len(files)}")
    print(f"Total broken: {total_broken}")
    print(f"Fixed: {total_fixed}")
    print(f"Skipped: {total_broken - total_fixed}")
    print(f"Files changed: {len(changed_files)}")
    if verify_only:
        print("\n(verify mode — no files written)")
    elif dry_run:
        print("\n(dry-run — pass --apply to write)")
    print("\n=== Skipped detail (up to 60) ===")
    for s in skipped[:60]:
        print(s)


if __name__ == '__main__':
    main()
