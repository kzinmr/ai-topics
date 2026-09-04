# Parallel Subagent Wiki Enrichment — Commit Collision Pattern

When processing a batch of raw articles into wiki pages, it's common to delegate to multiple subagents working on different pages in parallel. A critical git interaction can occur if one subagent commits changes that include another subagent's work.

## The Problem

Two subagents modify different wiki files:
- **Subagent A**: Creates `events/2026-07-08-openai-gpt-live.md`, updates `entities/simon-willison.md`
- **Subagent B**: Updates `concepts/agentic-engineering.md`, updates `entities/gilesthomas.md`

Subagent A runs `git add wiki/ && git commit`. Since `git add wiki/` stages **all** changes in the wiki directory, Subagent B's changes are silently included in Subagent A's commit. The commit message only describes Subagent A's work.

**Result**: Commit message "wiki: add GPT-Live event, update simon-willison" also contains the agentic-engineering case study and gilesthomas update — invisible in the commit message.

## Solutions

### Option 1: Explicit file paths in git add (Recommended for subagents)
Each subagent stages only its specific files:
```bash
git add wiki/events/2026-07-08-openai-gpt-live.md wiki/entities/simon-willison.md wiki/index.md wiki/log.md
git commit -m "wiki: add GPT-Live event, update simon-willison"
```

### Option 2: Parent agent handles all commits (Recommended for batch enrichment)
Don't give subagents commit instructions. Instead:
1. Subagents make changes and return summary
2. Parent agent verifies all changes with `git diff --stat wiki/`
3. Parent writes a single comprehensive commit message covering all changes
4. Parent commits and pushes once

This is cleaner because the parent has full context of all changes.

### Option 3: Separate git add with pathspec
```bash
git add wiki/events/ wiki/entities/simon-willison.md
git commit -m "wiki: GPT-Live event + simon-willison update"
# Subagent B separately:
git add wiki/concepts/agentic-engineering.md wiki/entities/gilesthomas.md
git commit -m "wiki: Bun-in-Rust case study, gilesthomas 34b"
```

## When to Use Each

| Scenario | Best Option |
|----------|-------------|
| 2-3 subagents, distinct file sets | Option 1 (explicit paths) |
| Complex enrichment with interdependent changes | Option 2 (parent commits) |
| Large batch with 3+ independent enrichment targets | Option 3 (separate commits) |

## Verification After Parallel Commits

Always check what actually ended up in the commit:
```bash
git show --stat HEAD
git diff HEAD~1 --stat -- wiki/
```

If a commit contains unexpected files, the commit message is already wrong. Either:
- Amend: `git commit --amend -m "wiki: comprehensive message covering all changes"`
- Or accept it and note in the next log.md entry what was actually included

## Cross-Cron-Job Race Condition

A variant of this problem occurs when **different cron jobs** modify the same wiki files concurrently. For example:

- **blog-triage** (07:30 UTC) spawns subagents targeting `deepswe-benchmark.md` and `simon-willison.md`
- **tag-audit** (10:00 UTC) runs and commits changes to the same files
- blog-triage's `git add wiki/` stages nothing for those files (already committed by tag-audit)

**Symptoms**: `git show --stat HEAD` shows fewer files than expected. Target files contain expected content but weren't in your commit.

**Diagnosis**:
```bash
git log --oneline -3 -- wiki/path/to/file.md  # Who last committed this file?
git show <other-commit> --stat | grep file.md  # What did they change?
```

**Resolution**: Verify content is correct via `grep` or `search_files`. If correct, no action needed — the enrichment was idempotent. If missing, re-run enrichment manually.

**Prevention**: Use explicit file paths in `git add` to avoid staging unrelated changes from concurrent jobs.

## Related Patterns

- `blog-wiki-ingest.md` — the pipeline that triggers this enrichment pattern
- `blog-triage-coverage-verification.md` — how to determine which articles need wiki pages
- `blog-triage-parallel-enrichment-pattern.md` — parallel enrichment workflow for blog triage
- `wiki-entity-enrichment-from-article.md` — the main skill for article → wiki page conversion
