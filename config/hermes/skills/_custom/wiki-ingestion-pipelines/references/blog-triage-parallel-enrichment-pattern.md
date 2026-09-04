# Blog Triage — Parallel Enrichment Pattern

When a blog-triage session identifies multiple wiki-worthy articles (2-5 "take" decisions), parallel subagent enrichment is the most efficient pattern. Each subagent targets a different wiki page, avoiding file conflicts.

## When to Use

- 2-5 articles triaged as "take" (wiki-worthy)
- Each article targets a **different** wiki page (no file overlap)
- Articles are independent (no cross-page dependencies)

## Workflow

### 1. Triage Phase (parent agent)
Read the blog-ingest checkpoint and evaluate each article against the triage heuristics:
```
1. Read checkpoint JSON from blog-ingest
2. For each article:
   a. Check source tier (Tier 1 → always read; Tier 2/3 → scan title)
   b. Read raw article if Tier 1 or title suggests AI relevance
   c. Check wiki/index.md for existing entity/concept pages
   d. Decide: skip | raw-save-only | wiki-update | entity-enrich
3. Collect all "take" decisions with target page paths
```

### 2. Enrichment Phase (parallel subagents)
Delegate each "take" to a separate subagent in a single `delegate_task` call with `tasks` array:

```python
delegate_task(tasks=[
    {
        "goal": "Enrich [page] with [article] data",
        "context": "Raw article at [path]. Target page at [path]. [Specific instructions]",
        "toolsets": ["terminal", "file"]
    },
    # ... one task per "take"
])
```

Each subagent:
1. Reads the raw article fully
2. Reads the existing target page
3. Applies changes via `patch` (never `write_file` on pages >40 lines)
4. Updates frontmatter (`updated` date, `sources` list)
5. Returns summary of changes

### 3. Commit Phase (parent agent)
After all subagents complete:
1. Verify changes with `git diff --stat wiki/`
2. Update `wiki/log.md` with triage summary
3. Single commit: `git add wiki/ && git commit -m "wiki: blog triage — [summary]"`
4. Push: `git push`

## Pitfalls

### Cross-Cron-Job Race Condition
Other cron jobs (tag-audit, wiki-health-fix, dreaming) may modify the same wiki files concurrently. If a concurrent job commits changes to your target files before your commit:
- Your subagents' changes may already be present (idempotent enrichment)
- `git show --stat HEAD` will show fewer files than expected
- **Verification**: Check that target files contain expected content via `grep` or `search_files`
- **Recovery**: If content is missing, re-run the enrichment manually

### Subagent File Overlap
If two subagents target the same file, the second `git add` will stage the first's changes too, leading to commit message confusion. **Always verify target pages are distinct across subagents.**

### Large Page Write-File Ban
Pages with >40 lines must use `patch`, not `write_file`. Subagents must read the page first to determine this. The pre-commit hook will block >50% content reduction.

## Example: 3 Parallel Enrichments (July 27, 2026)

**Articles triaged**: Kimi K3 vs GPT-5.6 Sol (Together AI), LLM Token Relay Market (Simon Willison)

**Subagent 1**: Kimi K3 page — added "DeepSWE vs GPT-5.6 Sol" subsection (46 lines)
**Subagent 2**: DeepSWE benchmark page — updated scoreboard, added routing section
**Subagent 3**: Simon Willison entity page — added relay market commentary entry

**Result**: All 3 completed in ~113s wall-clock. Commit included kimi-k3.md and log.md (deepswe-benchmark.md and simon-willison.md were already committed by a concurrent tag-audit job).

## Related Patterns

- `blog-triage-entity-enrichment-pattern.md` — the 6-step enrichment workflow for single articles
- `parallel-subagent-wiki-commit-pattern.md` — git commit coordination for parallel subagents
- `blog-triage-relevance-heuristics.md` — decision framework for which articles get wiki updates
