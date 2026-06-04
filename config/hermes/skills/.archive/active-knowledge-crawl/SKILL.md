---
name: active-knowledge-crawl
description: Daily cron job that proactively researches and ingests new concepts into the LLM Wiki based on config/hot-topics.yaml. For each hot topic with stale last_crawled, crawls prerequisites, laterals, or deep-dives — then creates wiki pages with sources.
version: 2.0.0
author: Hermes Agent
tags: [wiki, knowledge-base, automation, cron]
category: wiki
---

# Active Knowledge Crawl

## Description

Daily cron job that proactively researches and ingests new concepts into the LLM Wiki based on `config/hot-topics.yaml`. For each hot topic with `last_crawled` null or stale (>3 days ago), the agent crawls prerequisites, lateral connections, or deep-dives new developments — then creates wiki pages with sources.

## Trigger

Scheduled cron job (hermes cron), or manual invocation by user.

## Prerequisites

- Wiki at `~/wiki/` (or `wiki.path` from config)
- Hot-topics config at `~/ai-topics/config/hot-topics.yaml`
- Read access to `wiki/SCHEMA.md`, `wiki/index.md`, `wiki/log.md`

## Critical Paths (Environment-Specific)

In this environment, treat `~/ai-topics/` as the canonical repo root and `~/wiki/` as the canonical wiki root.
`~/wiki/` should resolve to `~/ai-topics/wiki/`.
Do not write to `/opt/data/home/wiki/` or any inferred alternate location.

**Always verify paths at session start:**
```bash
realpath ~/wiki   # should resolve to canonical wiki root
realpath ~/ai-topics  # should resolve to git repo root
cat ~/ai-topics/config/hot-topics.yaml | head -5  # verify readability
```
If these resolve differently, stop and fix the environment rather than switching to another wiki path.

## Workflow

### Step 0: Gap Discovery Phase (Optional — Run When No Stale Hot Topics)

Before selecting tracked topics, optionally scan for **entire domains missing from the wiki**. This is the "gap hunting" mode used when there are no stale hot-topics or when you want to expand beyond tracked topics.

**When to do this:** Run at the start of the crawl, in parallel with Step 1. If Step 1 finds 3+ stale topics to crawl, skip gap discovery. If Step 1 finds 0-1 stale topics, run gap discovery concurrently.

#### Gap Discovery Procedure

1. **Survey major AI domains** not in hot-topics.yaml by breadth-searching current developments:
   ```python
   # Search across multiple AI sub-domains to surface topics
   domains = [
       "AI video generation 2026",
       "AI regulation legislation 2026",
       "small language models edge 2026",
       # Add as needed based on recent trends
   ]
   ```

2. **Check each domain against wiki coverage:**
   ```bash
   # For each domain, check if any wiki page exists
   grep -rli "<domain-keyword>" wiki/concepts/ wiki/entities/ | head -5
   # Check for stub-only coverage
   grep -l "status: stub" wiki/concepts/ | xargs grep -l "<domain-keyword>"
   ```

3. **Score each gap by impact:**
   - **Major gap** (no wiki page at all + major industry trend): Create a full concept page and add to hot-topics.yaml
   - **Partial gap** (stub page exists + topic is evolving): Enrich the stub to full entry
   - **Minor gap** (passing mentions exist): Skip or note for later

4. **Acceptable sources for gap pages:** Same as Step 2 — peer-reviewed, tech blogs, official docs, reputable news. Avoid arXiv-only non-peer-reviewed.

5. **Max gaps to fill per run:** Up to 2 major gaps OR up to 3 partial gaps. Combined with tracked topic crawl, max 3 pages total per run.

6. **RECORDING DISCOVERED GAPS:** After creating pages for a gap, add the topic to `config/hot-topics.yaml` so future crawls track it:
   ```yaml
   - slug: new-gap-topic
     title: Gap Topic Title
     crawl_policy: laterals | prerequisites | deepdive | monitor
     priority: high | medium | low
     search_hints:
       - keyword1 keyword2
       - keyword3 keyword4
     wiki_pages:
       - concepts/new-gap-topic
     notes: "Gap discovered by active-crawl YYYY-MM-DD. source_count=N."
     added: YYYY-MM-DD
   ```

### Step 1: Select Topics

Read `config/hot-topics.yaml`. Extract topics where:
- `crawl_policy` is `prerequisites`, `laterals`, or `deepdive`
- `last_crawled` is `null` OR >3 days ago

Sort by priority then by age of `last_crawled`. Select:
- `priority: high` → oldest first, up to 2 topics
- `priority: medium` → oldest first, up to 1 topic
- Total max from Step 0 + Step 1: 3 pages per run

### Step 2: Research Each Topic

**prerequisites**: Read existing `wiki_pages` listed in the topic → identify missing foundational concepts → web search for quality sources → ingest.

**laterals**: Read existing `wiki_pages` → identify adjacent/parallel concepts from other domains → web search → ingest.

**deepdive**: Use `search_hints` for web search → find latest developments, case studies, best practices → update existing pages or create new sub-topic pages.

### Step 3: Create Wiki Pages

For each discovered concept:

1. **Web search** for quality sources (peer-reviewed conference papers, tech company blogs (OpenAI, Meta, Google, MS, Anthropic), official docs, HN-famous blogs)
2. **Save raw source** to `raw/articles/crawl-YYYY-MM-DD-<slug>.md`
3. **Create concept page** in `concepts/<slug>.md` with:
   - YAML frontmatter (title, created, updated, tags, sources, status)
   - Core concept explanation
   - Key findings / data
   - Related concepts via `[[wikilinks]]` (minimum 2 outbound links)
   - Sources referencing the raw files
4. **Update `index.md`**: Add entry in appropriate section
5. **Update `log.md`**: Append `## [YYYY-MM-DD] Active Knowledge Crawl: {topics}` with all changes

### Step 4: Update hot-topics.yaml

Set `last_crawled: YYYY-MM-DD` for each crawled topic.

### Step 5: Git Commit and Push

```bash
cd ~/ai-topics && git pull --rebase && git add wiki/ config/hot-topics.yaml && git commit -m "wiki: active-crawl YYYY-MM-DD" && git push
```

### Step 6: Report

Report in Japanese: each concept ingested, why it was chosen, relationship to parent topic.

---

## Critical Lessons Learned

### Lesson 1: Files May Already Be Committed (Duplicate Run Detection)

**Problem**: Running the same crawl task in consecutive cron sessions creates files with identical names and content. On the second run, `git add -A` and `git diff --cached --stat` show NO changes — because the files already exist in git with identical content.

**Diagnosis**:
```bash
# Are the files already tracked?
git ls-files wiki/concepts/<slug>.md
# What's the commit history for these files?
git log --oneline -3 -- wiki/concepts/<slug>.md
# What does git think is different?
git diff HEAD wiki/
```

**Prevention**: Before creating files, check for duplicates:
```bash
grep -rli "<concept-keyword>" wiki/concepts/ wiki/raw/
```

### Lesson 2: Always Verify Files Before Claiming Success

**Problem**: After `delegate_task` or any async operation, files may be written to the wrong path.

**Solution**: Always run explicit verification:
```python
import os
files = ["concepts/vector-db-agent-memory.md", ...]
for f in files:
    path = os.path.join(wiki, f)
    size = os.path.getsize(path) if os.path.exists(path) else 0
    print(f"{'✓' if size > 0 else '✗ MISSING'} {f} ({size} bytes)")
```

### Lesson 3: `git pull --rebase` Fails with Unstaged Changes

**Problem**: Running `git pull --rebase` after `git add -A` fails if there are unstaged changes.

**Solution**: Either:
1. `git stash && git pull --rebase && git stash pop && git add -A && git commit`
2. Or: `git add <specific-files> && git commit && git pull --rebase && git push`

### Lesson 4: Stale Subagent Memory Requires Full Context Pass
When using `delegate_task` for wiki operations, subagents have no memory of the parent session. Always include:
- Full absolute paths (e.g., `/opt/data/wiki/concepts/` or `~/wiki/concepts/`)
- The copy script as a final step if subagent might write to wrong path
- Explicit file verification commands before declaring success

### Lesson 5: YAML Update via Python Replace Is Fragile — Use sed Line Numbers

**Problem**: `str.replace()` for YAML frontmatter updates silently fails when whitespace or quoting doesn't match exactly.

**Diagnosis**: After replacement, always verify:
```bash
grep "last_crawled.*YYYY-MM-DD" config/hot-topics.yaml
```

**Solution**: Use `sed -i` with line numbers instead:
```bash
# Find line numbers first
grep -n "slug: ai-agent-engineering\|slug: harness-engineering\|slug: local-llm" config/hot-topics.yaml
# Then update with sed (last_crawled is 2 lines after slug for these topics)
sed -i "39s/2026-04-19/2026-04-23/; 53s/2026-04-19/2026-04-23/; 108s/2026-04-18/2026-04-23/" config/hot-topics.yaml
```

### Lesson 6: Git Push May Fail in Cron Environments

**Problem**: `git commit` succeeds locally but `git push` fails with one of:
- `fatal: could not read Username for 'https://github.com': No such device or address` — no auth session
- `remote: Invalid username or token. Password authentication is not supported for Git operations` — stale/expired token in git credentials store

**Diagnosis**: Check the error message to distinguish the cause.

**Remediation for stale token**: If push fails with "Invalid username or token" (not "could not read Username"), the git credentials store has an expired PAT. The user needs to refresh their GitHub token.

**Solution**:
1. Always report git status clearly: committed locally but push unavailable.
2. Do NOT retry push in the same session — it will keep failing.
3. The user will need to push manually or in a session with credentials.
4. All wiki changes are safe in the local commit — no data loss.

### Lesson 7: Git Pull --Rebase Fails with Unstaged Changes (Sibling Agents)

When `git pull --rebase` fails due to unstaged changes — and those changes may include files written by OTHER sibling cron jobs writing to the same repo:

```bash
# Option 1: stash → pull → pop → commit
git stash && git pull --rebase && git stash pop && git add -A && git commit -m "..."

# Option 2: add specific files → commit → pull → push (SAFER with sibling agents)
git add <specific-files> && git commit -m "..." && git pull --rebase && git push
```

**Prefer Option 2** when the wiki is written to by multiple cron jobs. `git stash pop` restores ALL unstaged changes — including files created by other subagents that you didn't write and shouldn't commit. Selective `git add` ensures you only commit your own work.

### Lesson 8: `git stash pop` Restores Foreign Files from Sibling Agents
 
**Problem**: Multiple cron jobs (wiki-periodic-enrichment, active-knowledge-crawl, newsletter-wiki-ingest) write to the same `~/ai-topics/wiki/` repo. When one job uses `git stash` to `pull --rebase`, `git stash pop` restores ALL files from the stash — including concept/entity pages created by another subagent that the current job has nothing to do with.
 
**Symptom**: After `git stash pop`, `git status` shows untracked `.md` files in `wiki/concepts/` or `wiki/entities/` that you didn't create. `git add -A` would commit these foreign files, creating a messy commit mixing multiple agents' work.
 
**Solution**:
1. **List what's changed** before staging: `git status`
2. **Only add your own files**: `git add config/hot-topics.yaml wiki/log.md wiki/index.md wiki/raw/articles/crawl-*.md wiki/concepts/inference/llama-cpp.md` (be specific)
3. **Do NOT use** `git add -A` or `git add wiki/` when sibling agents may have left files
4. **Verify** your commit only contains your changes: `git diff --cached --stat`
 
**Prevention**: At session start, check if sibling agent files exist in the workspace:
```bash
git status --short | grep "^??" | grep -v "raw/articles/"
```
If foreign untracked files exist, note them as sibling artifacts and stage selectively.
When `git pull --rebase` fails due to unstaged changes:
```bash
# Option 1: stash → pull → pop → commit
git stash && git pull --rebase && git stash pop && git add -A && git commit -m "..."

# Option 2: add specific files → commit → pull → push
git add <specific-files> && git commit -m "..." && git pull --rebase && git push
```

## Constraints

- Max 2 concepts per topic, max 6 concepts total per run
- Source file in `raw/articles/` is REQUIRED before creating a concept page
- Only depth-1 concepts (direct prerequisites/laterals); grandchildren are out of scope
- Domain: LLM/AI Agent technologies per SCHEMA.md — reject off-topic concepts
- Do not add topics to `hot-topics.yaml` without user approval — **Exception**: Topics discovered during the **Gap Discovery Phase** (Step 0) may be added to hot-topics.yaml with proper fields (slug, title, crawl_policy, search_hints, wiki_pages, notes, added). This is the only case where auto-addition is allowed.
- **Gap topic quality gate**: Only add a gap topic to hot-topics.yaml if its wiki page is comprehensive (not a stub, not skeleton) and covers at least 3+ sources. Stub/skeleton gap pages should NOT be added to hot-topics.yaml — they're not ready for tracked crawling.
- If no good concepts found for a topic, report "該当なし" and exit normally
- **Source quality**: arXiv-only (not peer-reviewed) papers are FORBIDDEN as sources. Only use:
  - Peer-reviewed venue papers (NeurIPS, ICML, ICLR, ACL, CVPR, etc.)
  - Tech company tech reports / tutorials (OpenAI, Meta, Google, MS, Anthropic)
  - Well-known personal blogs (Simon Willison, Andrej Karpathy, Antirez, etc.)
  - Official documentation and reputable news sources
  - When unsure, check peer-review via Semantic Scholar `publicationVenue` or abstract page "Published in"

## Related Skills

- `llm-wiki` — Core wiki operations (ingest, query, lint)
- `wiki-entity-enrichment-from-article` — Processing raw articles into wiki pages
