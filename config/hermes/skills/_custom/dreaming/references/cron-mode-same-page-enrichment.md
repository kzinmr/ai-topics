# Cron-Mode Same-Page Enrichment (Validated 2026-07-30)

When multiple takes from the triage JSON target the **same entity page**, use a single `patch` call instead of `delegate_task` parallel subagents.

## Why

- **Race condition**: Parallel subagents both try to `read_file` + `patch` the same entity page and will collide (second subagent's read doesn't see first subagent's write yet)
- **`execute_code` blocked**: Cron mode blocks `execute_code`, so subagent enrichment requires `delegate_task` — which spawns model calls that take 60-90s per block
- **Overhead**: Each subagent independently reads the file, assesses content, and decides where to insert — redundant when the anchor point is the same

## When to Use

- **Same entity page**: Takes targeting `entities/foo.md`, multiple articles from the same blog
- **Different sections**: The articles cover distinct topics (different subsections), so they don't interfere with each other's content
- **Simple insertions**: You're appending before an obvious anchor (e.g., `---\n\n## Related`)

## How

```python
# For patch tool: use a unique anchor near the insertion point
old_string = "---\n\n## Related"  # Just before the Related section
new_string = "\n### New Section 1\n\nContent 1\n\n### New Section 2\n\nContent 2\n\n---\n\n## Related"

patch(path="/path/to/entities/entity.md", old_string=old_string, new_string=new_string)
```

## Verified Against

- **July 2026**: 2 ElevenLabs takes (Virtual Receptionist + Valiant Finance) → single `patch` call → 59 insertions, 1 file modified, committed in <10 seconds
- Both adds went before the `---\n\n## Related` footer anchor, neither overlapping with the other

## When to NOT Use (stick with `delegate_task`)

- Takes target different entity pages — parallel is correct
- The insertions would be interleaved (Subagent A adds before existing Section X, Subagent B adds after Section X)
- The entity page is 40+ lines and you need to verify each enrichment independently (subagent reads+patches more reliably for complex markdown)
