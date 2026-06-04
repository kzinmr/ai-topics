# Dreaming Pipeline Recovery Pattern

## Architecture

The dreaming pipeline runs nightly (18:00 UTC → 18:10 → 18:20) in three stages:

```
dreaming-collect (18:00, no_agent script) 
  → dreaming-group (18:10, agent job)
  → dreaming-wiki-ingest (18:20, agent job)
```

**Key characteristic**: Stage 2 (`dreaming-group`) is a full Hermes agent job that calls the `semantic-article-grouping` skill. Unlike newsletter/blog triage (which runs as `no_agent` scripts or direct `execute_code`), the dreaming-group agent produces JSON output that gets **wrapped by the Hermes cron runner in markdown** — the response has a header, prompt section, and the JSON is embedded inside the `.md` output file.

## Recovery Pattern Validated (May 2026)

### Failure mode: Upstream JSON parse failure

The `dreaming-wiki-ingest` job receives the dreaming-group output via `context_from` cron chaining. When the JSON is embedded in markdown, the downstream gets:

```
{
  "ok": false,
  "error": "failed to parse JSON response from dreaming-group output",
  "output_path": "/opt/data/.hermes/cron/output/<job-id>/<timestamp>.md"
}
```

### Root cause

The `dreaming-group` agent job runs `semantic-article-grouping` which outputs JSON as its response text. The Hermes cron runner wraps this in markdown (`# Cron Job: dreaming-group\n\n## Prompt\n...\n\n## Response\n{...}\n`). The cron chaining's `context_from` tries to parse the full `.md` file as JSON and fails.

### Recovery procedure

Despite the JSON parse failure, the triage checkpoint file was **already saved by the dreaming-group job's internal `execute_code`** before producing the final response:

```
${HERMES_HOME}/cron/data/dreaming/triage_latest.json
```

The downstream `dreaming-wiki-ingest` reads this checkpoint file directly. The file contains the complete decisions array with `take`, `reference`, and `skip` items.

### Procedure for dreaming-wiki-ingest

```python
import json, os

hermes_home = os.environ.get('HERMES_HOME', os.path.expanduser('~/.hermes'))
triage_path = os.path.join(hermes_home, 'cron/data/dreaming/triage_latest.json')

if os.path.exists(triage_path):
    with open(triage_path) as f:
        data = json.load(f)
    decisions = data.get('decisions', [])
    takes = [d for d in decisions if d.get('recommended_action') == 'take']
    print(f"Recovered: {len(takes)} take decisions from checkpoint file")
```

### Secondary fallback (if checkpoint file is also missing)

Read from the cron output file:

```python
# Extract JSON block from markdown-wrapped output
import re
with open(output_path) as f:
    content = f.read()
# Look for JSON block after ## Response
match = re.search(r'## Response\n\n```(?:json)?\n(\{.*\})\n```', content, re.DOTALL)
# Or try to find a raw JSON block
if not match:
    match = re.search(r'\{[^{}]*\}', content)
```

## Distinction from Newsletter/Blog Pipelines

| Aspect | Newsletter | Blog | Dreaming |
|--------|-----------|------|----------|
| Stage 1 output | `no_agent` script saves JSON directly | `no_agent` script saves JSON directly | Agent job wraps JSON in markdown |
| Triage checkpoint | Always pure JSON | Always pure JSON | Pure JSON (saved before response) |
| Downstream consumer | `newsletter-wiki-ingest` | `blog-wiki-ingest` | `dreaming-wiki-ingest` |
| JSON parse failure risk | Low (no_agent) | Low (no_agent) | **High** (agent wraps output) |
| Fallback reliability | Checkpoint path | Checkpoint path | Checkpoint path (same) |

## Why the Checkpoint Survives

The `dreaming-group` agent job's script saves triage JSON to `${HERMES_HOME}/cron/data/dreaming/triage_latest.json` via `execute_code` BEFORE the agent produces its final response. The final response text is a separate output that gets markdown-wrapped. The checkpoint file is written to disk and persists through the cron chaining handoff.

This is the correct design pattern for any cron pipeline with an agent-role upstream: **always save data to a checkpoint file path, then produce a human-readable response.** Downstream consumers always read from the checkpoint path, not from the cron output.

## Key Differences from `newsletter-wiki-ingest` context

When running `dreaming-wiki-ingest` after recovery:

1. The triage checkpoint may have been saved hours earlier — recheck `wiki/log.md` for same-day processing history
2. The checkpoint file structure is identical to newsletter triage: `{checkpoint_run_id, summary_ja, decisions: [{item_id, source, ...}]}`
3. `take` items still need the full wiki processing pipeline (read raw article → check existing pages → create/update → index.md → log.md)
4. After processing, save skip/reference items to archive using the same archive procedure as newsletter/blog
