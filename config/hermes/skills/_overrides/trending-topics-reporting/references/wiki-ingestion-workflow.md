# Trending Topics Report → Wiki Ingestion Workflow

> How to process a trending-topics cron job output into actual wiki page changes.
> Covers the full cycle: locate output → deduplicate → delegate → validate → commit.

## Step 1: Locate the Report Output

The trending-topics cron job saves output to:
```
~/.hermes/cron/output/158a461eb520/YYYY-MM-DD_HH-MM-SS.md
```

Also saved to: `~/ai-topics/inbox/rss-scans/trending-topics-YYYY-MM-DD.md`

The report includes a `📊 推奨Wikiアクション` table at the bottom with specific page recommendations.

## Step 2: Check Which Actions Are Already Done

**Critical deduplication step.** Most recommended wiki actions are already handled by other pipelines:

| Pipeline | Schedule | What it does |
|----------|----------|-------------|
| `blog-wiki-ingest` | 07:50 UTC daily | Ingests blog articles into wiki pages |
| `newsletter-wiki-ingest` | 07:40 UTC daily | Ingestes newsletter articles |
| `dreaming-wiki-ingest` | 18:20 UTC daily | Nightly knowledge consolidation |
| `x-bookmarks-ingest` | 11:30/23:30 UTC | X bookmarks → wiki |
| `skeleton-enrich-daily` | 19:00 UTC | Enriches skeleton entity pages |
| `raw-backlog-ingest` | every 4h | Processes raw article backlog |

**Before creating any page**, check if it already exists:
```bash
# Check for existing pages matching the recommendation
find ~/ai-topics/wiki/entities/ ~/ai-topics/wiki/concepts/ -name "*PATTERN*" 2>/dev/null

# Check if content was already added (search for key terms)
grep -rl "KEY_TERM" ~/ai-topics/wiki/entities/ ~/ai-topics/wiki/concepts/ 2>/dev/null
```

**Common patterns:**
- Entity pages for major companies (DeepSeek, Cloudflare, etc.) — almost always already exist with recent updates
- Concept pages for trending techniques (speculative decoding, MCP) — often already enriched
- Raw articles referenced in the report — usually already in `wiki/raw/articles/`

**Only proceed with pages that are genuinely missing or outdated.**

## Step 3: Read Existing Pages Before Modifying

For pages that need updates:
1. Read the full existing page content
2. Check the `updated:` date in frontmatter
3. Verify the new information isn't already covered
4. Use `patch` (not `write_file`) for updates — never overwrite rich pages

## Step 4: Delegate Parallel Updates

Use `delegate_task` with batch mode for independent wiki updates. Each subagent handles one page creation/update.

**Template context for subagent:**
```
Wiki path: ~/ai-topics/wiki (= /opt/data/ai-topics/wiki)
AGENTS.md rules: YAML frontmatter required, min 2 wikilinks, update index.md and log.md.
Tags must be from SCHEMA.md taxonomy. Do NOT edit raw/ files.
Use patch (not write_file) to update existing pages.
```

**Batch size:** Up to 3 parallel subagents (delegation.max_concurrent_children).

**What to delegate per subagent:**
- Read source raw articles
- Create or update the wiki page
- Update `index.md` with new entry
- Append to `log.md`

## Step 5: Post-Delegation Validation

After subagents complete, validate before committing:

### Tag Taxonomy Check
Subagents frequently introduce invalid tags. Check all modified files:
```bash
cd ~/ai-topics
# List staged files
git diff --cached --name-only

# Check tags in new/modified concept files
grep -h "tags:" wiki/concepts/NEW_FILE.md wiki/concepts/MODIFIED_FILE.md
```

Compare against SCHEMA.md taxonomy. Common violations:
- `model-quantization` → should be `quantization`
- `ai-slop` → not in taxonomy (use `content-creator` or remove)
- `content-quality` → not in taxonomy (use `methodology` or remove)
- `data-science` → not in taxonomy (use `scaling-laws` or remove)

Fix invalid tags before committing.

### Subagent Side-Effect Check
Subagents may modify files outside the requested scope (e.g., fixing wikilinks in related pages, updating SCHEMA.md). Review all staged changes:
```bash
git diff --cached --stat
git diff --cached -- FILENAME  # review unexpected changes
```

Include legitimate side-effect changes in the commit if they're correct.

## Step 6: Selective Git Staging

When the working directory has many unrelated changes (common with cron jobs running concurrently):
```bash
# Reset all staging
git reset HEAD

# Stage only the files related to this ingestion
git add wiki/concepts/NEW_FILE.md wiki/concepts/MODIFIED_FILE.md \
        wiki/raw/articles/REPORT_FILE.md wiki/index.md wiki/log.md

# Verify staged files
git diff --cached --name-only
```

## Step 7: Commit and Push

```bash
cd ~/ai-topics && git commit -m "wiki: ingest trending-topics report YYYY-MM-DD" && git push
```

The pre-commit hook will validate:
- index.md line count matches actual pages
- All tags are in SCHEMA.md taxonomy
- No rich pages were overwritten (>50% content reduction)

## Pitfalls

1. **Duplicate pages**: Other pipelines may have already created/updated the recommended pages between the report generation and ingestion. Always check first.

2. **Invalid tags from subagents**: Subagents don't always have SCHEMA.md loaded. They may invent tags that sound reasonable but aren't in the taxonomy. Always validate after delegation.

3. **Subagent file scope creep**: Subagents may modify `SCHEMA.md`, `ai-policy.md`, or other files while "fixing related issues." Review these changes before committing.

4. **Missing raw articles**: Some sources in the report (e.g., LWN/SFC articles) may not have been scraped into `wiki/raw/articles/`. The subagent will need to work from the report summary alone.

5. **Rich page overwrite**: If a subagent uses `write_file` on an existing rich page (40+ lines), the pre-commit hook blocks the commit. Always instruct subagents to use `patch` for updates.

6. **Working directory state**: Cron jobs and other sessions may leave uncommitted changes. Use `git reset HEAD` + selective staging to avoid committing unrelated changes.
