# Broken Wikilink Repair: Empty Slug Pattern

## The Pattern

Many `## Related` / `## See Also` sections have lines where the `[[slug]]` was lost but the
`— description` text survived:

```markdown
- [[concepts/rlhf]] — Core research area, book author    ← OK
-  — Previous employer, Zephyr and TRL work               ← BROKEN
- [[concepts/post-training]] — His primary research focus ← OK
```

This is caused by a prior script or bulk-edit that stripped `[[slug]]` anchors but left descriptions.

## Detection

```bash
# Count broken links
cd ~/wiki
grep -rn '^-  — ' entities/ concepts/ | wc -l

# Per-file breakdown
cd ~/wiki
grep -rn '^-  — ' entities/ concepts/ | cut -d: -f1 | sort | uniq -c | sort -rn
```

## Auto-Fix with Fuzzy Matching

A script exists at `scripts/fix_broken_wikilinks.py` under the `wiki-graph-health` skill.

### How it works

1. Builds a search index of ALL existing wiki pages (entities + concepts) from frontmatter title,
   slug, aliases, tags, and first 200 chars of body content.
2. For each broken link (line matching `- — description`), tokenizes the description and
   computes word-overlap scores against every indexed page.
3. The best match is selected if its score ≥ threshold.

### Threshold Guide

| Threshold | Fix Rate | False Positives | Use Case |
|-----------|----------|-----------------|----------|
| 0.5       | ~30-40%  | Very low (≈matched title) | Safety-first |
| 0.4       | ~45-50%  | Low | Recommended default |
| 0.35      | ~55-60%  | Moderate | Aggressive bulk fix |
| 0.3       | ~65-70%  | Moderate-High | High volume, review afterward |
| 0.25      | ~75%     | High | Only for desperate cases |

### Usage

```bash
cd ~/ai-topics

# Dry run with default threshold 0.4
python3 scripts/fix_broken_wikilinks.py --dry-run

# Apply fixes with threshold 0.4 (recommended)
python3 scripts/fix_broken_wikilinks.py --apply

# More aggressive (catches more, risk of wrong links)
python3 scripts/fix_broken_wikilinks.py --apply --threshold 0.3
```

### After Fixes

```bash
# Verify remaining count
grep -rn '^-  — ' entities/ concepts/ | wc -l

# Run full graph analysis to confirm
python3 ~/ai-topics/scripts/wiki_graph.py
```

## Manual Fixes (below threshold)

Descriptions that score < 0.3 are usually too specific for keyword matching
(e.g., "Kladov's approach to handling incomplete code in language servers").
These need a human to recognize the intended target slug and add it manually.
Common patterns:
- References to a specific blog post or talk
- Very specific descriptions of one person's work
- Descriptions referencing external people/orgs not tracked in the wiki
