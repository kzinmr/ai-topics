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
- `last_delivery_error: "no delivery target resolved for deliver=None"` — job ran successfully but had nowhere to send results. Set `deliver` to a valid target.
- Job appears in `list` but `process list` shows nothing — the subagent may have already completed and delivered.
- Token timeouts on long jobs — use `enabled_toolsets` to reduce overhead, or split into smaller batches.

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

### Testing Modifications

```bash
# Run the script directly to verify JSON output
python ~/.hermes/scripts/<name>.py 2>&1 | head -50

# Check for syntax errors
python -c "import ast; ast.parse(open('~/.hermes/scripts/<name>.py').read()); print('OK')"

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

### Cost Reference
- DeepSeek v4-Flash: ~$0.002/$0.008 per 1M tokens (input/output)
- Fireworks qwen3.6-plus: ~$0.003/$0.015 per 1M tokens
- Custom local: free, higher latency

### Maintenance
Monthly review of `~/.hermes/cron/data/token_usage/summary.json`
Flag jobs exceeding $5/month in Discord.
Consider migrating to cheaper alternatives if one provider dominates.