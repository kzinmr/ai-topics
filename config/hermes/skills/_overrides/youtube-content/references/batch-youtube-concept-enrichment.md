# Batch Concept Page Enrichment from Video Series

When ingesting a multi-episode YouTube series, Phase 3 enriches EXISTING concept pages — not creating new ones. This reference covers the parent-agent-side pattern for efficiently patching multiple concept pages with cross-episode insights.

## When to Use

- 2+ episodes ingested with raw articles saved
- Entity pages already created/enriched by parallel subagents (Phase 2)
- Concept pages already exist — this is enrichment, not creation
- Cross-episode patterns have emerged that individual subagents can't see

## Pattern: Read → Patch → Repeat

The parent agent enriches concept pages sequentially (not parallel subagents) because:
1. Concept pages are shorter than transcripts — reading them is cheap
2. The parent has the full cross-episode picture
3. Patches are small, targeted additions

### For each concept page:

**1. Read** the current page with `read_file` (or rely on earlier read in the session).

**2. Update frontmatter** — two targeted patches:
```
updated: YYYY-MM-DD  (update date)
Add new sources (episode raw articles)
```

**3. Add new principles/sections** — patch new numbered items into the existing principle list:

Example (agentic-engineering.md):
```
old_string: "Slow coding represents the opposite of 10× productivity..."
new_string: "Slow coding represents...\n\n### 7. New Pattern Name\n\nContent..."
```

**4. Extend the Key Practitioners list** — patch new entries at the end of the list:
```
old_string: "- **[[entities/last-existing-practitioner]]** — description"
new_string: "- **[[entities/last-existing-practitioner]]** — description\n- **[[entities/new-person]]** — new description"
```

**5. Verify** by reading the updated file's Key Practitioners section to confirm all entries landed.

## Commonly Enriched Concept Pages

For agent/engineering-focused series (like "Show Us Your (Agent) Skills"):

| Concept Page | Typical Additions |
|---|---|
| `agentic-engineering.md` | New numbered principles (7-11), 6+ new practitioners |
| `agent-skills.md` | Skills ecosystem section (skepticism, security, capabilities, self-updating) |
| `coding-agents.md` | Paradigm shift table, "coding agents are dead" thesis |
| `ai-safety.md` | Skills supply chain security, hidden HTML attack, lethal trifecta |
| `reward-hacking.md` | Agent-level reward hacking (bare excepts, LLM judge manipulation) |
| `context-engineering.md` | Effective context window findings, multi-pass architecture |

## Pitfalls

### Smart Quotes in patch()
Files may contain smart/curly quotes (" ") that look identical to straight quotes (" ") but cause `escape-drift` errors in the `patch` tool. When `patch` fails with "Escape-drift detected":
1. `read_file` the target region at the exact offset
2. Copy the line verbatim (smart quotes and all) into `old_string`
3. The error message is about backslash-escaping, not the quotes themselves — the fix is to match the file's exact characters

### Pagination Trap
After reading a file with `offset`/`limit`, the `patch` tool warns "_warning: file was last read with offset/limit pagination". This is advisory only — patches still apply correctly, but re-read the whole file before any `write_file` overwrite.

### Stale Page Reads
The parent's cached read of a concept page may be stale if a subagent modified it. Always re-read before patching if subagents ran. The `patch` tool detects conflicts gracefully.
