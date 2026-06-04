# Watchdog Pipeline Pattern — 2-Tier Cron Health Monitoring

> Reference for `cron-job-management` skill. Captures the watchdog architecture designed for the llm-wiki pipeline (2026-05-09).

## Pattern Overview

A 2-tier watchdog system for monitoring multi-stage cron pipelines:

```
Tier 1: Script Watchdog (no_agent, frequent)     Tier 2: Agent Watchdog (LLM, daily)
┌──────────────────────────────┐                ┌─────────────────────────────────┐
│ Silent when healthy           │───alerts────▶│ Reads Tier 1 output +            │
│ Exit 0 + empty stdout = OK    │                │ health/lint reports              │
│ Exit 1 + JSON = issues found  │                │ Auto-fixes resolvable issues     │
│                              │                │ Reports unfixable to Discord     │
│ Checks:                      │                │                                 │
│ • Job last_status & staleness │                │ Fixable patterns:                │
│ • Pipeline chain integrity    │                │ • Pipe table corruption         │
│ • File counts & freshness     │                │ • Line number prefix pollution  │
│ • Git unpushed commits        │                │ • Index duplicate entries       │
│                              │                │ • Count mismatches              │
└──────────────────────────────┘                └─────────────────────────────────┘
```

## Tier 1: Script Watchdog

### Design Principles
- **no_agent** — zero token cost, pure Python
- **Frequent** — 2-hour intervals (matches the article's pattern)
- **Silent when healthy** — exit 0 + empty stdout means no Discord delivery
- **Structured output** — JSON on exit 1 for downstream consumption

### What to Check
```python
# 1. Job status from jobs.json
data = json.loads(jobs_file.read_text())
jobs = data.get("jobs", [])  # NOTE: jobs.json is {"jobs": [...], "updated_at": "..."}

# 2. Per-job: last_status, last_run_at recency, enabled state
# 3. Pipeline chains: ingest → triage → wiki-ingest all ran in order
# 4. Wiki integrity: file counts, index freshness (<48h), log existence
# 5. Git: uncommitted changes, unpushed commits, last push recency
```

### jobs.json Format Pitfall
The `jobs.json` file uses `"id"` not `"job_id"` as the key, and is wrapped in `{"jobs": [...], "updated_at": "..."}` — not a bare array.

## Tier 2: Agent Watchdog

### Design Principles
- **Runs after health checks** — schedule AFTER wiki-health and wiki-health-fix
- **Pre-run context collector** — script gathers Tier 1 output + health reports + graph analysis into JSON payload
- **Auto-fix scope limited** — only fix patterns known to be safe (corruption, dedup, counts). Never delete pages or fix broken wikilinks without human review.

### Pre-run Context Collector Pattern
```python
# Collects context from multiple cron job outputs:
def read_latest_job_output(job_id: str) -> dict | None:
    job_dir = CRON_OUTPUT / job_id
    md_files = sorted(job_dir.glob("*.md"), reverse=True)
    for f in md_files:
        content = f.read_text(encoding="utf-8", errors="replace")
        match = re.search(r"^## Response\s*\n(.*)", content, re.MULTILINE | re.DOTALL)
        if match:
            return {"response": match.group(1).strip()[:8000]}
```

### Auto-Fix Matrix
| Issue Pattern | Source | Auto-Fix | Method |
|---|---|---|---|
| Pipe table corruption `\|- [[...]]` | wiki-health | ✅ | sed/patch |
| Line number prefix `^\s*\d+\|` | wiki-health | ✅ | Python regex |
| Index duplicates | wiki-health | ✅ | Bottom-up dedup |
| Index count mismatch | wiki-health | ✅ | os.walk + patch header |
| Missing `---` separators | wiki-health | ✅ | patch insert |
| Broken wikilinks | wiki-graph-analysis | ❌ | Report only |
| Orphan pages | wiki-graph-analysis | ❌ | Report only |
| Tag violations | wiki-health | ⚠️ | SCHEMA.md proposal |

### Safety Rules
- If a fix would touch 10+ files → stop and report
- Never delete pages → orphans need human review
- Always read SCHEMA.md before any wiki operation
- Always commit + push after fixes

## Schedule Design

Place Tier 2 AFTER the health check chain completes:
```
17:00 — wiki-health
17:10 — wiki-health-plan
17:25 — wiki-health-fix
17:35 — wiki-watchdog-fix (Tier 2) ← reads all above outputs
```

Tier 1 runs independently every 2 hours, including right after the main pipeline:
```
07:00 — blog-ingest
07:10 — newsletter-ingest
07:50 — blog-wiki-ingest (last pipeline stage)
08:00 — pipeline-watchdog (Tier 1) ← immediate post-pipeline check
```

## Source

Based on Matt Van Horn's community analysis article "Hermes Agent: What People Are Actually Using It For" (2026-04-19), Use Case #7 — Agent Watchdog & Auto-Healer pattern:
> "Hermes on a 2-hour cron checks OpenClaw's scanners, logs, and baselines, pushing summaries to Telegram. Geeky-gadgets documents Hermes detecting an OpenClaw failure, patching the broken API key config, and restarting with 11 seconds of downtime."
