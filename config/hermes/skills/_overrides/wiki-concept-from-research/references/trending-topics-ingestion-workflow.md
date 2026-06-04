# Trending Topics → Wiki Ingestion Workflow

## When to Use

When the user says 「trending-topicsの結果をwikiに取り込んで」— process the trending-topics cron job output into wiki pages. This is a recurring workflow that runs after the `trending-topics` job (daily at 12:00 UTC) delivers its report.

## Input Format

The trending-topics report (`/opt/data/.hermes/cron/output/158a461eb520/<date>.md`) contains:
- 5-8 trending topics with Japanese summaries
- Wiki coverage status for each: ✗ 未カバー (not covered), ✓ 一部カバー (partially), △ 更新必要 (needs update)
- A summary table with priority (⭐⭐⭐) and urgency (🔴 緊急)

## Workflow

### Phase 1: Audit existing coverage

```bash
# Check what files already exist (trending report may be wrong)
ls /opt/data/ai-topics/wiki/entities/ | grep -i "<keyword>"
ls /opt/data/ai-topics/wiki/concepts/ | grep -i "<keyword>"
ls /opt/data/ai-topics/wiki/events/ | grep -i "<keyword>"

# Also check index.md entries
grep -i "<keyword>" /opt/data/ai-topics/wiki/index.md
```

**Common trap**: The trending report may say ✗ 未カバー but files already exist under slightly different names (e.g., `concepts/nemotron-labs-diffusion.md` already covers "Nemotron Diffusion LM"). Always verify before delegating.

### Phase 2: Prioritize

| Priority | What | Action |
|----------|------|--------|
| 🔴 緊急 (urgent) | Security incidents, safety issues | Create first, use `event` type for incidents |
| ⭐⭐⭐ 高 | New concepts with no coverage | Create via subagent |
| ⭐⭐ 中 | Smaller concepts | Create directly or last |
| △ 更新必要 | Existing pages need data | Handle yourself (lighter touch) |

### Phase 3: Dispatch parallel subagents for new pages

Use `delegate_task` with `tasks` array for 3 subagents in parallel. **Key pattern**: batch similar work together.

```
Subagent 1: 1 concept page (e.g., abliteration)
Subagent 2: 1 event page (e.g., security incident)
Subagent 3: 2 concept pages (e.g., synthid + custom-ai-silicon)
```

**Context each subagent needs**:
- Absolute wiki paths (`/opt/data/ai-topics/wiki/`)
- SCHEMA.md location for tag taxonomy
- Language rule: ALL wiki content in English
- Target page type (concept/event/entity) and expected sections
- Research queries (specific web_search terms)
- Commit instructions

**Critical**: Remind subagents about:
- Reading SCHEMA.md before writing tags
- Adding new tags to SCHEMA.md if needed (pre-commit blocks otherwise)
- [[wikilinks]] minimum 2 per page
- Updating index.md and log.md
- All content in English

### Phase 4: Handle entity/page updates yourself

For pages that need minor updates (not full creation), handle directly:
- `patch` for targeted content additions
- Bump `updated:` date in frontmatter
- Update index.md and log.md

Entity updates are lightweight compared to concept page creation — don't delegate them.

### Phase 5: Commit and push

All subagents commit independently. After they finish:
1. `git log --oneline -5` to verify all commits
2. Handle your own entity updates + index/log changes
3. Commit with descriptive message
4. Push

**⚠️ PARALLEL SUBAGENT GIT COLLISION (HIGH-IMPACT)**: When 3 subagents run in parallel and all call `git add wiki/`, the first one to commit stages and commits ALL new files — including those created by the other two parallel subagents. This means:
- Subagent 1's commit contains its own files + subagent 2's + subagent 3's (everything)
- Subagent 2's commit is **thin** — only index.md + log.md changes, because its actual files were already committed by subagent 1
- Subagent 3's commit is also **thin** — same problem

**Detection**: After subagents complete, run `git show --stat <commit>` for each subagent commit. If a commit shows only 2 files changed (index.md + log.md) when it should have created concept/event pages, the collision occurred.

**Fix**: `git reset --soft origin/main` to squash all thin commits + your own changes into a single clean commit, then push. The actual page files are already in the first subagent's commit (on origin), so nothing is lost.

**Prevention**: Tell each subagent to `git add` ONLY its own files, not `git add wiki/`. Include this instruction in their context: 
```
⚠️ GIT: Only `git add` YOUR specific files (concepts/<your-page>.md, raw/articles/<your-raw>.md, wiki/index.md, wiki/log.md, wiki/SCHEMA.md). Never `git add wiki/` — other subagents are creating files in parallel and you'll accidentally commit theirs.
```

**Push timeout**: GitHub may timeout or return 500 errors on large pushes. Use `background=true` + `notify_on_complete=true`. If push fails with `Internal Server Error`, `sleep 10` + retry — the 500 is a transient GitHub server issue, not a repo problem.

## Example: 2026-05-27 Session

Input: 8 topics, 5 ✗ 未カバー, 3 ✓ 一部/△ 更新必要

1. **Audit**: Found `concepts/nemotron-labs-diffusion.md` already existed (trending report said ✗ 未カバー)
2. **Subagent 1**: `concepts/abliteration.md` (148 lines, 3 raw articles)
3. **Subagent 2**: `events/trustfall-symlink-rce-2026.md` (196 lines, 3 raw articles)
4. **Subagent 3**: `concepts/synthid.md` + `concepts/custom-ai-silicon.md` (7 raw articles)
5. **Direct updates**: `entities/vera-rubin.md` (new), `entities/grok-build.md` (new), `entities/gemini-3-5-flash.md`, `entities/google-antigravity.md`, `entities/cerebras-systems.md`, `entities/command-a-plus.md`

Result: 4 new concept/event pages + 2 new entity pages + 4 entity updates. All 8 topics covered.
