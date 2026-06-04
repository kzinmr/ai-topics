#!/bin/bash
# Find the richest (longest) historical version of a wiki page in git history.
# Usage: bash references/find-richest-version.sh wiki/entities/someone.md [top_n]
# Run from the wiki repo root (e.g. ~/ai-topics).
#
# Output: top N commits sorted by line count (descending), with dates.
# Use the top commit to restore: git show <commit>:<path> > <path>

PATH_ARG="${1:?Usage: $0 <path> [top_n]}"
TOP_N="${2:-3}"

for commit in $(git log --format=%H -- "$PATH_ARG" | head -20); do
    lines=$(git show "$commit:$PATH_ARG" 2>/dev/null | wc -l)
    date=$(git log --format=%ai -1 "$commit" | cut -d' ' -f1)
    msg=$(git log --oneline -1 "$commit" | cut -c1-80)
    echo "$lines $date $commit $msg"
done | sort -rn | head -"$TOP_N"
