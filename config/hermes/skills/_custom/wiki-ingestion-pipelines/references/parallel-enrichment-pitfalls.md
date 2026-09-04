# Parallel Enrichment Pitfalls (June 2026)

Three concrete pitfalls discovered during the blog-wiki-ingest pipeline's parallel enrichment execution pattern.

## 1. Parallel log.md Race Condition (CRITICAL)

**Problem**: When using `delegate_task` with 3 concurrent subagents for parallel wiki enrichment, each subagent independently prepends to `log.md` via a write-to-/tmp/ + terminal Python script. The last subagent to write WINS — its prepend call overwrites the entire file, silently destroying the other subagents' log entries.

**Observed**: June 2026 — 3 parallel subagents enriched voyage-ai, cory-doctorow, and ornith concepts. Subagent 1's Ornith-1.0 log entry was overwritten; only subagent 2's combined entry survived. Required a manual Python consolidation fix.

### Prevention Patterns

**Pattern A — Parent writes log.md (preferred)**: All three subagents enrich pages but do NOT touch log.md. After all parallel tasks complete, the parent agent reads the final state of each enriched file, then writes a single consolidated log.md entry. Add to subagent context: "Do NOT write to log.md — the parent will handle consolidated logging."

**Pattern B — Single subagent designated log writer**: Task 0 gets log-writing responsibility with explicit instructions to include all tasks' results. Tasks 1 and 2 skip log.md entirely.

**Pattern C — Subagent returns log text, parent prepends**: Each subagent returns its log entry text as part of the task summary. The parent concatenates and prepends one consolidated entry.

### Recovery

If the race already happened, write a Python consolidation script to `/tmp/` that:
1. Reads log.md
2. Identifies duplicate entries by timestamp heading
3. Merges all unique entries into one consolidated section
4. Preserves the `# Wiki Log\n\n_Log...` header

Example approach from June 2026:
```python
# /tmp/fix_log.py
consolidated = """## [YYYY-MM-DD HH:MM] — Blog wiki-ingest — Summary

**Source:** blog-triage (recovered from checkpoint)

### New pages created (N):
### Existing pages enriched (N):
"""
newsletter_pos = content.find('## [YYYY-MM-DD HH:MM] — Newsletter wiki-ingest')
new_content = content[:header_end] + '\n' + consolidated + content[newsletter_pos:]
```

## 2. Patch Tool `\n` Literal Character Trap

**Problem**: When passing a multi-line `new_string` to `patch`, the tool interprets `\n` as literal backslash-n characters unless they are real newlines in the parameter value. If your new_string contains literal `\n` escape sequences, the file will contain the visible text `\\n` instead of actual line breaks.

**Observed**: June 2026 — John D. Cook entity page enrichment. The `### LLM Output Verification` heading and body text were concatenated onto `## Key Quotes` as a single line with literal `\\n` sequences. Required a second `patch` call with real newlines to fix.

### Prevention

After EVERY multi-line `patch`, immediately re-read 2-3 lines around the insertion point to check for `\n` literals. If present, do a second `patch` replacing the broken block (including the `\\n` literals) with the correct block using real newlines.

The fix pattern:
```
old_string=the text with literal \n characters
new_string=the same text with actual newlines (press Enter in the parameter)
```

## 3. `replace_all=true` Source List Hazard

**Problem**: When using `patch` with `replace_all=true` to add a new source path to the frontmatter `sources:` list, the tool replaces EVERY occurrence of the target string in the file — not just the frontmatter entry you intended. If the target string appears in both frontmatter AND body text (References section, wikilinks), the body references get corrupted too.

**Observed**: June 2026 — When trying to add a new raw article source to `entities/john-d-cook-applied-mathematics-consulting.md`, `replace_all=true` on the last existing source path replaced the Z3/Python source entry instead of appending to it. The Z3 source was lost and had to be manually restored with a second `patch` call.

### Prevention

Never use `replace_all=true` for sources list manipulation. Instead:

- **To add a source**: Include surrounding YAML context (the `---` delimiter and next heading, or the previous source entry) to make the match unique
- **To replace a source**: Use `patch` with `replace_all=false` (default) and provide enough context for a unique match — include the preceding source entry + `---\n\n# Page Title` to disambiguate frontmatter from body references
- **Verify after patch**: Read the sources list and confirm the correct entry was modified/added
