#!/bin/bash
# Scan git history for commits that shrank entity/concept pages by >50 lines and >50%.
# Also optionally report pages currently below their historical best.
#
# Usage:
#   bash references/content-regression-scanner.sh              # scan commit history
#   bash references/content-regression-scanner.sh --current    # also show current deficits
#
# Run from the wiki repo root (e.g. ~/ai-topics).

MODE="${1:-history}"

# Phase 1: Scan commit history for regression events
COMMITS=$(git log --oneline --diff-filter=M -- 'wiki/entities/*.md' 'wiki/concepts/*.md' | awk '{print $1}')

for commit in $COMMITS; do
    FILES=$(git diff-tree --no-commit-id --name-only -r "$commit" -- 'wiki/entities/*.md' 'wiki/concepts/*.md' 2>/dev/null)
    
    for path in $FILES; do
        OLD=$(git show "$commit^:$path" 2>/dev/null | wc -l)
        NEW=$(git show "$commit:$path" 2>/dev/null | wc -l)
        
        [ "$OLD" -lt 40 ] && continue
        [ "$NEW" -eq 0 ] && continue
        
        DROP=$((OLD - NEW))
        IS_REGRESSION=$(awk "BEGIN { ratio=$NEW/$OLD; print (ratio < 0.5 && $DROP > 50) ? 1 : 0 }")
        
        if [ "$IS_REGRESSION" = "1" ]; then
            RATIO=$(awk "BEGIN { printf \"%.0f\", ($NEW/$OLD)*100 }")
            MSG=$(git log --oneline -1 "$commit")
            echo "REGRESSION|$path|$OLD|$NEW|$DROP|${RATIO}%|$MSG"
        fi
    done
done

# Phase 2: Report pages currently below their historical best (if --current)
if [ "$MODE" = "--current" ]; then
    echo ""
    echo "=== CURRENT DEFICIT CHECK ==="
    
    for path in $(find wiki/entities wiki/concepts -name '*.md' -not -name '_index.md' 2>/dev/null); do
        current=$(wc -l < "$path" 2>/dev/null || echo 0)
        [ "$current" -lt 30 ] && continue
        
        # Find richest version (check top 15 commits for speed)
        best=0
        for commit in $(git log --format=%H -- "$path" 2>/dev/null | head -15); do
            lines=$(git show "$commit:$path" 2>/dev/null | wc -l)
            [ "$lines" -gt "$best" ] && best=$lines
        done
        
        if [ "$best" -gt 0 ]; then
            deficit=$((best - current))
            if [ "$deficit" -gt 50 ]; then
                ratio=$(awk "BEGIN { printf \"%.0f\", ($current/$best)*100 }")
                echo "DEFICIT|$path|$current|$best|$deficit|${ratio}%"
            fi
        fi
    done
fi
