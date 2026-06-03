#!/usr/bin/env python3
"""Pre-commit hook: detect content regression in wiki entity/concept pages.

Blocks commits that would shrink an existing entity or concept page by >50%
or remove >50 lines — a strong signal that a rich page is being overwritten
with a skeleton or stub.

Exit 0 = pass, Exit 1 = blocked.
"""

import subprocess
import sys
import os

# Thresholds
MIN_LINES_BEFORE = 40       # only protect pages that are already substantial
SHRINK_RATIO = 0.5          # block if new < old * 0.5
ABSOLUTE_LINE_DROP = 50     # block if more than this many lines removed


def staged_entity_concept_files():
    """Return list of staged .md files under wiki/entities/ or wiki/concepts/."""
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
        capture_output=True, text=True
    )
    paths = []
    for line in result.stdout.strip().splitlines():
        if line.startswith(("wiki/entities/", "wiki/concepts/")) and line.endswith(".md"):
            paths.append(line)
    return paths


def file_lines_at_head(path):
    """Return line count of file at HEAD, or 0 if file doesn't exist at HEAD."""
    result = subprocess.run(
        ["git", "show", f"HEAD:{path}"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        return 0
    return len(result.stdout.splitlines())


def staged_file_lines(path):
    """Return line count of the staged (index) version of a file."""
    result = subprocess.run(
        ["git", "show", f":{path}"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        return 0
    return len(result.stdout.splitlines())


def main():
    files = staged_entity_concept_files()
    if not files:
        sys.exit(0)

    violations = []
    for path in files:
        old_lines = file_lines_at_head(path)
        new_lines = staged_file_lines(path)

        if old_lines < MIN_LINES_BEFORE:
            continue  # only protect substantial pages

        if new_lines <= 0:
            continue  # file deletion is a different concern

        line_drop = old_lines - new_lines
        ratio = new_lines / old_lines if old_lines > 0 else 1.0

        if line_drop > ABSOLUTE_LINE_DROP and ratio < SHRINK_RATIO:
            violations.append({
                "path": path,
                "old": old_lines,
                "new": new_lines,
                "drop": line_drop,
                "ratio": ratio,
            })

    if not violations:
        sys.exit(0)

    print("")
    print("🚫 CONTENT REGRESSION DETECTED — rich wiki pages would be overwritten!")
    print("")
    print("   The following staged changes shrink existing pages by >50% or >50 lines.")
    print("   This usually means an ingestion pipeline is overwriting a curated page")
    print("   with a skeleton or stub. Use `patch` to add content, not `write_file`.")
    print("")
    for v in violations:
        print(f"   📄 {v['path']}")
        print(f"      {v['old']} → {v['new']} lines  (−{v['drop']} lines, {v['ratio']:.0%} of original)")
    print("")
    print("   To recover the original content:")
    print("     git show HEAD:<path>  # view the current version")
    print("")
    print("   To bypass this check (NOT recommended):")
    print("     git commit --no-verify")
    print("")
    sys.exit(1)


if __name__ == "__main__":
    main()
