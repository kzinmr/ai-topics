---
name: cron-job-management
category: productivity
description: "Hermes cron job lifecycle management — creation, model configuration, manual testing, and execution monitoring."
---

# Cron Job Management

## Creating a New Cron Job

```python
cronjob(
    action="create",
    prompt="<self-contained prompt>",
    schedule="0 19 * * *",  # cron expression or '30m', 'every 2h', etc.
    name="descriptive-name",
    skills=["skill-name"],   # optional: pre-load skills
    enabled_toolsets=["web", "file", "terminal"],  # restrict tools to what's needed
    model={"provider": "deepseek", "model": "deepseek-v4-flash"},  # optional: pin model
    deliver="discord:1233771389367095377:1491801814222504169",  # where to send results
    script="optional_pre_run_script.py",  # optional: runs before job prompt
)
```

**Key rules:**
- `prompt` must be fully self-contained — cron runs have no current-chat context
- **Explicitly state environment-specific facts in the prompt** — the subagent has no knowledge of your repo URLs, paths, conventions, or identity. Example: "The GitHub repo is `kzinmr/ai-topics` at `~/ai-topics`, NOT `NousResearch/ai-topics`." Common pitfall: AI may infer incorrect repo names/URLs from training data if not explicitly told.
- If `skills` are provided, the future cron run loads them in order, then follows the prompt
- `enabled_toolsets` restricts which tools the job's agent can use — reduces token overhead
- Cron-run sessions should NOT recursively schedule more cron jobs

## Configuring Model/Provider

Always specify both `provider` and `model` explicitly:

```python
cronjob(
    action="update",
    job_id="<job_id>",
    model={"provider": "deepseek", "model": "deepseek-v4-flash"},
)
```

**Pitfall:** If only `model` is set without `provider`, the provider may default to `custom` which could use the wrong API endpoint. Always set both.

## Cross-Platform Relay Pattern (no_agent Relay)

Route one cron job's output to a different platform without running a second LLM.

### When to Use
- Discord should mirror Slack posts verbatim (or vice versa)
- Telegram should relay a subset of Discord/Slack output
- Any multi-platform delivery where content is identical

### Setup

1. **Source job** (the one doing the work) runs on its schedule and delivers to its primary platform:
   ```
   deliver="slack:C077ACXR5UY"
   ```

2. **Relay job** is a `no_agent=True` job with a small Python script that reads the source job's latest output file and prints its delivered content to stdout:
   ```python
   cronjob(
       action="update",
       job_id="<relay_job_id>",
       no_agent=True,
       script="relay_script.py",     # ~/.hermes/scripts/relay_script.py
       schedule="45 0,4,8,12,16,20 * * *",  # stagger after source job
       deliver="discord:guild:thread",
       skills=[],                    # no skills needed — no LLM invocation
   )
   ```

3. **Relay script** (`~/.hermes/scripts/relay_script.py`):
   ```python
   import re, os, sys
   from pathlib import Path

   hermes_home = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
   source_output = hermes_home / "cron" / "output" / "<source_job_id>"
   files = sorted(source_output.glob("*.md"), reverse=True)
   if not files:
       sys.exit(0)

   content = files[0].read_text(encoding="utf-8", errors="replace")
   # Extract the agent's delivered response section
   match = re.search(r"^## Response\s*\n(.*)", content, re.MULTILINE | re.DOTALL)
   if match:
       print(match.group(1).strip())
   ```

### Regex Pitfall for `## Response` Extraction

When extracting content after a heading with `re.MULTILINE | re.DOTALL`:

```
# WRONG — non-greedy .*? + $ with MULTILINE matches only ONE line:
re.search(r"^## Response\s*\n(.*?)$", content, re.MULTILINE | re.DOTALL)

# RIGHT — greedy .* without $ captures everything to end:
re.search(r"^## Response\s*\n(.*)", content, re.MULTILINE | re.DOTALL)
```

**Why:** `$` with `re.MULTILINE` matches end of *any* line (not end of string). Non-greedy `.*?` stops at the first possible end-of-line. Greedy `.*` with `DOTALL` captures everything to end of string.

### Key Rules
- **Stagger schedule** — relay job runs after source job (e.g., 15-30 min gap)
- **Zero token cost** — no_agent=True jobs do not invoke an LLM
- **Skills and toolsets empty** — relay job needs neither
- **Fails silently** — if no source output exists, `sys.exit(0)` produces no delivery
- **Policy unification** — when merging two similar jobs (e.g., Slack + Discord), merge their skill sets by **union** (not intersection). The merged set ensures both jobs benefit from all loaded knowledge, with the relay inheriting the source's full context.

## Manual Testing (Dry Run)

1. **Create/update the job first** with the correct model and prompt
2. **Trigger manual run:**
   ```python
   cronjob(action="run", job_id="<job_id>")
   ```
3. **Monitor execution:**
   ```python
   cronjob(action="list")  # check last_status, last_run_at, last_delivery_error
   process(action="list")  # check for active subprocess sessions
   ```
4. **Check output files** (if applicable):
   - Pre-run scripts save checkpoints to `~/.hermes/cron/data/`
   - Job output logs may be in `~/.hermes/cron/output/`

**Important:** `cronjob action='run'` queues the job for execution in a separate session. Results are delivered asynchronously to the `deliver` target (Discord channel, Telegram, etc.), NOT returned immediately to the current conversation.

## Watchdog Pipeline Pattern (2-Tier)

For monitoring multi-stage cron pipelines with auto-healing capabilities. Full pattern documented in `references/watchdog-pipeline.md`.

Quick reference:
- **Tier 1**: no_agent Python script, every 2h, silent when healthy, JSON output on issues
- **Tier 2**: Agent-driven, daily after health checks, reads Tier 1 output + lint reports, auto-fixes safe patterns, reports unfixable to Discord
- **Schedule**: Tier 2 runs AFTER wiki-health → wiki-health-plan → wiki-health-fix chain

Auto-fixable patterns: pipe table corruption, line number prefix pollution, index duplicates, count mismatches, missing separators. Never auto-fix broken wikilinks or delete orphan pages.

## Monitoring and Debugging

```python
# Check job status
cronjob(action="list")

# Check active subprocesses
process(action="list")

# Poll a specific process for output
process(action="poll", session_id="<session_id>")

# Wait for process completion
process(action="wait", session_id="<session_id>", timeout=300)
```

**Common issues:**
- `jobs.json` format: The file is `{"jobs": [...], "updated_at": "..."}` with each job using `"id"` (not `"job_id"`). Access via `data["jobs"]` not bare iteration.
- `last_delivery_error: "no delivery target resolved for deliver=None"` — job ran successfully but had nowhere to send results. Set `deliver` to a valid target.
- Job appears in `list` but `process list` shows nothing — the subagent may have already completed and delivered.
- Token timeouts on long jobs — use `enabled_toolsets` to reduce overhead, or split into smaller batches.
- **Prompt drifts between runs**: The prompt stored in `jobs.json` may differ from what was actually used last run. The job's prompt can be updated by the cron system via skill injection, script injection, or context enrichment between runs. **Always check the latest output file** (`~/.hermes/cron/output/<job_id>/latest.md`) in the `## Prompt` section to see what the job actually ran with — not just the `jobs.json` definition. The output file is the source of truth for what was delivered to the agent.
- **Pipeline race conditions with fixed schedule offsets**: When jobs in a chain use fixed cron offsets (e.g., `0 17`, `10 17`, `25 17`) without `context_from` or actual data dependencies, slow upstream jobs (>60 min) can displace the entire chain. A downstream job that checks for upstream output at its scheduled start time will find nothing (or yesterday's stale output) if the upstream job hasn't finished. **Detection**: compare `last_run_at` timestamps across the chain — if a downstream job ran BEFORE an upstream job finished, you have a race. **Fix**: widen schedule gaps based on observed worst-case run times, or implement `context_from` with proper data flow. **Example from 2026-05-13**: wiki-health (74 min) → wiki-health-plan (68 min) → wiki-health-fix ran before plan completed, skipped all auto-fix actions. Fixed by moving wiki-health-fix from `25 17` to `50 17`.
- **BLOCKED by cron injection scanner**: If `last_status: error` and the output file shows `Status: BLOCKED` with a threat pattern like `exfil_curl`, the assembled prompt (user prompt + loaded skill content) tripped the `_CRON_THREAT_PATTERNS` check. **Debugging pitfall:** `read_file` masks `$VAR_NAME` patterns as `***` — use `od -c` or `execute_code` for hex inspection. See [[references/cron-injection-scanner]] for full pattern list, debugging workflow, and fix recipes.

## Editing Pre-Run Scripts (`script` parameter)

When a cron job uses `script="name.py"` (resolved from `~/.hermes/scripts/`), the script generates JSON context that gets injected into the job prompt before each run.

### Common Modification Patterns

1. **Adjusting parameters** (time ranges, limits, thresholds):
   - Locate the script at `~/.hermes/scripts/<name>.py`
   - Update `timedelta(days=X)` or `limit=N` values in the relevant function
   - The cron job system does NOT cache the script — next run picks up changes automatically

2. **Removing expensive or unnecessary data sources**:
   - Remove the function definition and delete its key from the `main()` payload dict
   - Check if any other function calls the removed function (imports, callers)
   - Example: removing a `trending_report()` call that runs a heavy subprocess

3. **Adding new data collection functions**:
   - Write a new function that returns a `list[dict[str, str]]` or similar structured data
   - Add its call result to the payload under the appropriate namespace
   - Keep function signatures consistent (`repo: Path` + optional args)
   - Example: `related_wiki_pages()` that parses `[[wikilink]]` patterns for connected content

### Pattern: Wikilink-based Related Page Discovery

To implement "for each recent page, find connected pages":

```
1. Parse outgoing [[links]] from the page content (re.compile(r'\\[\\[([^\\]|]+)(?:\\|[^\\]]+)?\\]\\]'))
2. Search for backlinks via `grep -rl "\\[\\[slug(\\||\\])" wiki/`
3. Deduplicate against recent pages, cap per source and total
4. Build excerpts for the result list
```

### Pattern: Hard Deduplication (Script-Level Filtering)

When a cron reporting job produces duplicate/semantically-overlapping content across
adjacent slots, **filter candidates in the pre-run script** rather than relying on
LLM prompt guidance (`"avoid repeating"`). Soft dedup fails because the LLM sees
the same candidate pool and often re-picks the same topics.

#### When to Use
- Adjacent time slots (e.g., 05:30 and 09:30) report the same topics
- Wiki activity is low between slots → candidate pool unchanged
- Prompt-based `avoid_repeating_recent_posts` guidance is not respected
- Same data source feeds multiple report slots with little turnover

#### Implementation Pattern

1. **Track previous outputs** — the script must have access to what was already reported.
   For Slack/Discord relay pipelines, fetch recent bot posts via API and extract their
   wikilinks/slugs/topic identifiers.

2. **Build a "covered" set** — collect identifiers from the most recent N posts (2-3 is
   usually enough to prevent adjacent-slot duplicates).

   ```python
   def _get_covered_slugs(recently_covered: list[dict], n_posts: int = 2) -> set[str]:
       slugs: set[str] = set()
       for post in recently_covered[:n_posts]:
           for wikilink in post.get("wikilinks", []):
               slugs.add(Path(wikilink).stem)
       return slugs
   ```

3. **Filter the candidate pool** — remove pages/topics whose identifiers match the
   covered set BEFORE passing data to the LLM.

   ```python
   def _dedup_filter(pages: list[dict], covered_slugs: set[str]) -> list[dict]:
       return [p for p in pages
               if Path(p["path"]).stem not in covered_slugs]
   ```

4. **Fallback when exhausted** — if filtering leaves too few candidates (e.g., < 3),
   skip dedup entirely and include a warning in the payload. Never pass an empty
   candidate pool — the LLM will hallucinate.

   ```python
   if len(deduped_candidates) >= 3:
       candidates = deduped_candidates
       dedup_applied = True
   # else: fall through with unfiltered candidates
   ```

5. **Surface dedup in payload** — add transparency fields so the LLM knows what
   was filtered and why:

   ```json
   "dedup": {
       "recently_covered_topics": [...],
       "hard_filter_applied": true,
       "hard_filter_removed_slugs": ["areal", "hybrid-flow", "slime-rl"]
   }
   ```

#### Real Example (Slack hot-posts → Discord relay)

The `ai-topics-slack-hot-posts` job at `5e91a0b47c32` runs every 4 hours (0,4,8,12,16,20
UTC; 9,13,17,21,1,5 JST). The `ai-topics-discord-hot-posts` job (`56548a0ed1bf`) relays
Slack output to Discord verbatim 15 min later.

**Problem:** 05:30 JST (20:30 UTC, "pre-morning") and 09:30 JST (00:30 UTC, "morning")
reported the same RL training library topic because 12 wiki pages were created in one
batch and the soft dedup prompt was ignored.

**Fix:** Modified `ai_topics_slack_hot_posts_context.py` to filter `recent_wiki_pages`
and `related_wiki_pages` against wikilinks from the last 2 bot posts. Since the Discord
relay is a `no_agent` passthrough, fixing the source script fixes both channels.

**Result:** The 09:30 report can no longer pick topics already covered at 05:30.

#### Pitfalls
- **Token availability**: If the API call to fetch previous posts fails (missing token),
  skip dedup gracefully — the `recently_covered_topics` list will be empty and filtering
  is a no-op. Don't crash the script.
- **Slug collision**: File stems like `pi` can be ambiguous (Pinecone vs Pi agent).
  For entity pages, cross-reference by reading the page's title, not just the slug.
  For dedup purposes, slug-based filtering is usually sufficient since adjacent-slot
  duplicates are the exact same wiki pages.
- **Don't filter too aggressively**: 2 recent posts is the sweet spot. Filtering 4+
  posts may exhaust the candidate pool across longer gaps (e.g., overnight when no
  new wiki pages are created).

### Testing Modifications

```bash
# Run the script directly to verify JSON output
python3 ~/.hermes/scripts/<name>.py 2>&1 | head -50

# Check for syntax errors
python3 -c "import ast; ast.parse(open('~/.hermes/scripts/<name>.py').read()); print('OK')"

# Verify git repo changes if the script exists in both locations
diff ~/.hermes/scripts/<name>.py ~/ai-topics/scripts/<name>.py  # sync if different
```

**Location notes:**
- Cron job pre-run scripts live in `~/.hermes/scripts/` (the canonical location)
- Some scripts may also have copies under `~/ai-topics/scripts/` — check and sync if needed
- The cron job references scripts by basename only (e.g., `"script": "ai_topics_slack_hot_posts_context.py"`)

## Pausing/Resuming Jobs

```python
cronjob(action="pause", job_id="<job_id>")
cronjob(action="resume", job_id="<job_id>")
```

## Removing Jobs

```python
cronjob(action="remove", job_id="<job_id>")
```

## Timezone Note

Cron schedules use UTC. JST = UTC + 9 hours.
- JST 04:00 = UTC 19:00 → schedule: `"0 19 * * *"`
- JST 09:00 = UTC 00:00 → schedule: `"0 0 * * *"`

---

## Section: Bias Injection (cron-bias-injection)

Derive filtering criteria from an opinion source and batch-update cron job prompts to inject selection bias.

### When to Use
- User says "Follow X's opinion for topic selection"
- "Apply Y's perspective to the cron jobs"
- "Inject Z filter into the automated workflow"

### Workflow
1. **Source Analysis**: Extract explicit/implicit filtering criteria (SKIP/DEPRIORITIZE, COMPOUND/BOOST, WAIT items)
2. **Map to categories**:
   ```
   SKIP / DEPRIORITIZE (0.3x weight):
   - [specific frameworks, patterns] — [why to skip]

   COMPOUND (3x weight — focus here):
   - [specific patterns] — [why to boost]

   WAIT / OBSERVE:
   - [items to defer until validated]
   ```
3. **Identify target jobs**: trending topics, blog triage, newsletter triage, wiki ingest, X bookmarks
4. **Batch-update prompts**: Include filter as a marked block in each prompt:
   ```
   ## Karpathy's Filter (APPLY THIS)
   [filter content]
   ```
5. **Verify**: Check prompt_preview in cronjob listing

### Common Pattern: Karpathy's AI Twitter Filter
**Skip:** AutoGen/AG2, CrewAI, autonomous agent pitches, agent app stores, SWE-bench chasing, Semantic Kernel, DSPy, horizontal agent platforms, per-seat SaaS pricing
**Compound:** Context engineering, tool design, orchestrator-subagent pattern, eval discipline, harness mindset, MCP, practical production deployment

### Pitfalls
- Prompt survives, re-reads — filter must be IN the prompt
- Full prompt replacement — include everything the job needs
- Test before committing — let one job run with new filter
- Consistent SKIP/COMPOUND labels across all jobs

---

## Section: Output Debugging (cron-output-debugging)

Extract and analyze data from cron job output files.

### Directory Structure
Cron job outputs: `~/.hermes/cron/output/<job_id>/YYYY-MM-DD_HH-MM-SS.md`

Each file has three sections:
1. **Prompt** — system prompt + data from pre-run script
2. **Script Output / Script Error** — raw JSON from pre-run script
3. **Response** — agent's final report output

### Extracting Bookmark Article Data
Parse markdown tables in cron reports:
```python
import re
rows = re.findall(r'\|\\s*\\d{4}-\\d{2}-\\d{2}\\s*\\|\\s*(.+?)\\s*\\|\\s*(.+?)\\s*\\|\\s*[\\d,]+\\s*\\|', content)
```

### Handling Historical Data
Multiple consecutive runs may return `[SILENT]` (no new data). The **last non-SILENT report** is the most recent actual processing.

### Common Errors
- xurl path error: symlink `/opt/data/bin/xurl` → `/opt/data/.hermes/bin/xurl`
- OAuth2 token expired: requires manual re-auth
- Script exit code 1: check stderr for missing modules
- **no_agent Python script failures**: `ModuleNotFoundError` → the script's shebang uses system python but deps are in the venv. Full debugging workflow in `references/debugging-no-agent-scripts.md`. Quick check: `/opt/data/.hermes/venv/bin/python3 ~/.hermes/scripts/<name>.py`

### Job ID Discovery
```python
cronjob(action='list')  # find job_id by name
```

---

## Section: Token Usage Monitor (token-usage-monitor)

Full pipeline for tracking LLM token usage and API costs.

### Step 1: COST_REPORT Hook
Insert at the **top** of the job's prompt:
```
# TOKEN USAGE TRACKING
At the end of your response, print exactly one line:
COST_REPORT: job=<job_name> status=ok input_tokens=0 output_tokens=0 cost=0.0
```

### Step 2: Reporting Cron Jobs
Create 4 types: daily, weekly, monthly, trend
Uses `~/.hermes/scripts/token_usage_collect.py` with the appropriate argument.

### Step 3: Persistent Storage
SQLite3 at `~/.hermes/cron/data/token_usage/token_usage.db`
Scans `~/.hermes/cron/output/<job_id>/` for `COST_REPORT:` lines
Deduplicates via `ingested_files` table.

### Step 4: DO NOT Apply To
- Pure script jobs (blog_ingest.py, fetch_x_*.py, process_email.py)
- Jobs with `deliver: null` (shell-only)
- Jobs using `qwen36-fast` default with minimal LLM usage

### ⚠️ PITFALL: COST_REPORT Parser Failure

The `token_usage_collect.py` parser uses key-value extraction (`parse_cost_report()`) but **fails silently on most real-world COST_REPORT formats**. The DB shows `input_tokens=0 output_tokens=0 cost=0.0` for ~80% of ingested lines. Only the strict `key=value` format (with no pipes, `~` prefixes, or free-text) gets parsed correctly.

**Formats that BREAK the parser (silently produce 0):**
- `COST_REPORT: job=blog-triage | input_tokens=~180K | output_tokens=~4K | model=deepseek-v4-flash`
- `COST_REPORT: job=blog-ingest | total_tokens=45000` (uses `total_tokens` not `input_tokens`/`output_tokens`)
- `COST_REPORT: job=trending-topics | model=deepseek-v4-flash | tokens_in=~85K | tokens_out=~5.5K | cost_estimate=$0.045`
- `COST_REPORT: job=blog-ingest | 17 tool calls (3 web_extract, 8 search_files...) | 2 new concept pages...`
- `COST_REPORT: job=active-crawl | pages_created=5 | raw_articles=5` (no token fields at all)
- `COST_REPORT: job=blog-triage | tokens=52000` (uses bare `tokens` key)

**Format that DOES work:**
- `COST_REPORT: job=blog-triage input_tokens=0 output_tokens=0` (space-separated, no pipes, no `~`)

**Impact:** `summary.json` and `token_usage.db` report total costs of ~$0.002/month when real costs are ~$87/month. The trend data is useless.

**Fix path:** Either (a) enforce a single COST_REPORT format across all cron job prompts, or (b) upgrade `parse_cost_report()` to handle the full variety of formats actually produced. See `references/cost-estimation-manual.md` for the manual estimation methodology used as a fallback.

### Cost Reference
- DeepSeek v4-Flash: ~$0.002/$0.008 per 1M tokens (input/output)
- DeepSeek v4-Pro: roughly 5x v4-Flash pricing
- Fireworks qwen3.6-plus: ~$0.003/$0.015 per 1M tokens
- Custom local: free, higher latency

### Manual Estimation Fallback
When the automated DB is unreliable, use the methodology in `references/cost-estimation-manual.md`:
1. `cronjob list` → get all jobs with schedules, models, providers
2. `grep -r 'COST_REPORT' ~/.hermes/cron/output/` → sample recent per-run costs
3. Multiply by daily/weekly frequency → daily cost per job
4. Sum across jobs → monthly estimate

### Maintenance
Monthly review of `~/.hermes/cron/data/token_usage/summary.json`
Flag jobs exceeding $5/month in Discord.
Consider migrating to cheaper alternatives if one provider dominates.