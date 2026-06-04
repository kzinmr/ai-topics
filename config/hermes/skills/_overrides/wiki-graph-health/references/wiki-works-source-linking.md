# Wiki Works Source Linking Lint

Ensure person entity pages link original sources for all works.

## Rule
Every work mentioned MUST have at least one clickable link to its original source:
- Books: Amazon + publisher or Goodreads
- Papers: arXiv, SSRN, journal URL
- Blog posts: Direct URL
- Podcasts/Videos: Platform URL
- Open source: GitHub repo URL

## Format
`_Title_ ([Amazon](url) · [Goodreads](url), Publisher, Year)`

## Common Fixes
```markdown
# BEFORE
**Book:** _Co-Intelligence_ (Penguin Random House, 2024)

# AFTER
**Book:** _Co-Intelligence_ ([Amazon](url) · [Goodreads](url), Penguin Random House, 2024)
```

## Batch Execution (weekly lint)
```bash
cd ~/ai-topics
grep -l "tags: \[person\]" wiki/entities/*.md | while read f; do
    if grep -P '_[^_]+_' "$f" | grep -qv ']\('; then
        echo "REVIEW: $f (has unlinked works)"
    fi
done
```

## Priority Entities
simon-willison.md, antirez-com.md, ethan-mollick.md, karpathy.md
