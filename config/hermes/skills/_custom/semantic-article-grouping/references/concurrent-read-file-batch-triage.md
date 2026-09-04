# Concurrent read_file for Batch Article Assessment

## Pattern

When assessing 15-20+ raw articles in a triage session (dreaming, blog, newsletter), reading them sequentially is slow. The `read_file` tool supports parallel invocation — call 2-3 `read_file` in a single function_calls block to read concurrently.

## When to Use

- Dreaming 0-article recovery: scanning 15-20 unprocessed raw articles
- Blog triage: reading 10-20 blog checkpoint candidates
- Newsletter triage: reading resolved article bodies after URL extraction
- Any batch where you need to assess 10+ files for wiki relevance

## Concrete Example (3 concurrent reads)

Call 3 read_file invocations in parallel — each with `limit=40` to get the frontmatter + first ~30 lines of body content, which is sufficient for triage-level relevance assessment:

```
read_file(path="article-1.md", limit=40)
read_file(path="article-2.md", limit=40) 
read_file(path="article-3.md", limit=40)
```

All three return simultaneously. Process results, then batch the next 3.

## Batch Size Guidance

- **2-3 concurrent**: Safe, fast, no risk of tool call limits
- **4-5 concurrent**: Works but diminishing returns (context window fills fast)
- **6+ concurrent**: Avoid — results flood context, harder to track which article is which

## Triage Workflow Integration

1. **Identify unprocessed articles** (find + grep -rl against log.md + entities/ + concepts/)
2. **Batch read 3 at a time** with `limit=40` (frontmatter + opening paragraphs)
3. **Quick-classify each**: skip (non-AI/markedeting), reference (already covered), take (genuine gap)
4. **Deep-read only take candidates** with full `read_file` (no limit) to get body_excerpt
5. **Build triage JSON** with all decisions

## Key Pitfall: Context Flooding

Reading 20 articles at 40 lines each = 800 lines of context. This is manageable but leaves less room for reasoning. For large batches:
- Process in waves of 3-5 articles
- Classify each wave before reading the next
- Only deep-read articles that pass initial screening

## Cron-Mode Note

In cron mode, `execute_code` is blocked. You cannot use a Python loop to read files programmatically. The concurrent `read_file` pattern is the ONLY way to batch-read files efficiently in cron mode — it's not just faster, it's the only option besides sequential read_file calls.
