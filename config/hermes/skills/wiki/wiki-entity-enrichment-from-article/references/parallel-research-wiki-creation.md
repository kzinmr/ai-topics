# Parallel Research via delegate_task for Wiki Page Creation

When multiple independent wiki pages need web research before creation (e.g., the user asks for 3+ related concepts simultaneously), use parallel `delegate_task` calls to research all topics at once, then create wiki pages sequentially from the research files.

## When to Use

- 2+ independent concept pages need comprehensive web research
- Each topic requires 5-15 web searches + content extraction
- The topics are semantically related but research tasks are independent

## Workflow

### 1. Launch parallel research tasks

```python
delegate_task(tasks=[
    {"goal": "Research topic A...", "context": "..."},
    {"goal": "Research topic B...", "context": "..."},
    {"goal": "Research topic C...", "context": "..."},
])
```

Each task writes its findings to `/opt/data/<topic>-research.md`.

### 2. Read research files and create wiki pages

Read each research file sequentially, then create wiki pages:

```
read_file("/opt/data/topic-a-research.md")
→ write_file("wiki/concepts/topic-a.md", ...)

read_file("/opt/data/topic-b-research.md")
→ write_file("wiki/concepts/topic-b.md", ...)
```

### 3. Update index, log, SCHEMA, commit

Batch all wiki updates into a single commit:
- Add new tags to `wiki/SCHEMA.md`
- Insert entries into `wiki/index.md` (alphabetically)
- Prepend log entry to `wiki/log.md`
- `git add wiki/ && git commit && git push`

## Pitfalls

- **Pre-commit tag validation**: The git hook blocks commits with non-canonical tags. Always add new tags to SCHEMA.md BEFORE committing wiki pages that use them. Check the taxonomy: `search_files("tag-name", path="wiki/SCHEMA.md")`.
- **Stale index entries**: When creating a page that replaces stale/ghost entries (e.g., `mcp-protocol` and `model-context-protocol-mcp` → `mcp`), remove the old entries from index during insertion.
- **delegate_task research file location**: Subagents write to `/opt/data/` by default. Verify the path before reading.
- **Time efficiency**: 3 parallel research tasks complete in ~6 minutes vs ~18 minutes sequential.

## Example Session

User request: "RLVR, o1/o3→GPT-5, MCP実用的起源の3つをWikiに追加して"

```
# Step 1: 3 parallel research tasks (6 min)
delegate_task → /opt/data/rlvr-research.md (27KB)
delegate_task → /opt/data/o1-o3-gpt5-integration-timeline.md (15KB)
delegate_task → /opt/data/mcp-practical-origins-research.md (19KB)

# Step 2: Create wiki pages from research
concepts/rlvr.md ← rlvr-research.md
concepts/openai-o-series-gpt5-unification.md ← o1-o3-gpt5-integration-timeline.md
concepts/mcp.md ← mcp-practical-origins-research.md

# Step 3: SCHEMA + index + log + commit
SCHEMA: + rlvr, test-time-scaling
index: + 3 new entries, - 2 stale MCP entries
commit: "wiki: add RLVR concept, o1/o3→GPT-5 timeline, MCP with practical origins (3 new pages)"
```
