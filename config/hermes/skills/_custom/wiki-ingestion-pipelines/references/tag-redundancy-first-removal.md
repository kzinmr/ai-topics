# Tag Redundancy-First Removal Pattern

## Problem

When a subagent creates a wiki page and the pre-commit hook blocks the commit due to non-canonical tags, the instinct is to add the missing tags to SCHEMA.md. But SCHEMA.md already has 830+ canonical tags — many rejected tags are redundant with existing ones.

## Redundancy-First Decision Flow

```
Tag rejected by pre-commit → Check if canonical equivalents exist → YES → Remove tag (no SCHEMA.md change)
                                                                → NO  → Add to SCHEMA.md
```

## Broad Grep for SCHEMA.md Tags

The pre-commit validator (`pre-commit-tag-validator.py`) recognizes tags in TWO formats:
- Backtick-quoted: `` `tag-name` ``
- Bold-prefixed comma-separated: `- **Category**: tag1, tag2`

A narrow grep like `grep '\`tagname\`' SCHEMA.md` misses bold-prefixed tags. Use a broad pattern:

```bash
grep -oE '`[^`]+`|\*\*[^*]+\*\*:.*' wiki/SCHEMA.md | tr '`,*' ' ' | tr -s ' ' '\n' | grep -xF '<tag>'
```

Or for batch checking:
```bash
for tag in tag1 tag2 tag3; do
  if grep -oE '`[^`]+`|\*\*[^*]+\*\*:.*' wiki/SCHEMA.md | tr '`,*' ' ' | tr -s ' ' '\n' | grep -qxF "$tag"; then
    echo "OK: $tag"
  else
    echo "MISSING: $tag"
  fi
done
```

## Common Redundancy Mappings (July 2026)

| Rejected tag | Canonical equivalents already in SCHEMA.md | Why it's redundant |
|---|---|---|
| `youtuber` | `content-creator`, `youtube`, `video-series` | Three canonical tags cover a YouTube creator |
| `ai-coding` | `coding-agent` | AI-assisted coding is coding-agent territory |
| `codex` (false negative) | `codex` (in bold-prefixed `**Models**:` list) | First grep was narrow; broad grep confirms it exists |

## When to Add to SCHEMA.md Instead

Add when the tag represents a genuinely new category not covered by any existing canonical tag. Example: a new model architecture or a novel methodology. Before adding, search for semantic neighbors — `grep -i 'keyword' wiki/SCHEMA.md` — to verify no near-match exists.

## Concrete Session Example (July 13, 2026)

Session: X bookmarks ingest — Theo Browne entity page creation.

1. Subagent created `entities/theo-browne.md` with tags including `youtuber` and `ai-coding`
2. Pre-commit hook blocked: `youtuber` not in SCHEMA.md taxonomy
3. Broad grep confirmed: `content-creator`, `youtube`, `video-series` all exist → `youtuber` redundant → removed
4. Checked `ai-coding` — also not in SCHEMA.md. `coding-agent` exists → redundant → removed
5. Net: 0 new SCHEMA.md entries, 2 removed from entity page, commit passed
