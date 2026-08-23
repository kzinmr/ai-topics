# Dreaming Triage Checkpoint Recovery (Validated June 2026)

## Two-Tier Failure Recovery

The dreaming pipeline has two upstream failure modes, each with a different recovery source:

### Mode 1: dreaming-collect pre-run script fails
- **Symptom**: Script outputs `{"ok": false, "error": "..."}`, no collected data
- **Recovery**: Read `grouped_themes_latest.json` at `${HERMES_HOME}/cron/data/dreaming/grouped_themes_latest.json`
- **This file may not exist** if the script timed out before saving
- **If absent**: Proceed with 0-Article Recovery Workflow (scan raw articles directly)

### Mode 1b: Checkpoint JSON valid but articles empty (collection failure)
- **Symptom**: `latest.json` has `"ok": true` but `articles: []`, `total_articles: null` (or 0 or `None` in Python repr), `recent_raw_articles: N`
- **Cause**: dreaming.py completed without error but found no articles to collect (possible RSS feed issues, date range mismatch, or filter bug)
- **Recovery**: Do NOT treat as "nothing to do" — articles likely exist on disk from other pipelines
  1. Verify: `python3 -c "import json; d=json.load(open('...latest.json')); print(d['total_articles'], d['recent_raw_articles'])"`
  2. If `recent_raw_articles > 0`: articles are on disk but were not collected by dreaming.py
  3. Proceed with filesystem-based recovery (see Workflow below)
- **Validated**: June 29, 2026 — checkpoint had 0 articles but 211 raw articles on disk. Cross-pipeline dedup yielded 9 themes (1 take, 7 references, 1 skip).

### Mode 2: dreaming-group agent fails JSON render (MOST COMMON)
- **Symptom**: Pre-run script output shows `{"ok": false, "error": "failed to parse JSON response from dreaming-group output", "output_path": "..."}`
- **Recovery**: Check `triage_latest.json` at `${HERMES_HOME}/cron/data/dreaming/triage_latest.json` FIRST
- The triage agent saved the checkpoint BEFORE attempting to render its cron response
- If valid JSON with decisions array → read directly, no re-triage needed
- Proceed directly to Post-Recovery Verification

### Mode 3: Both fail
- **Symptom**: No valid checkpoint, no grouped themes, no triage decisions
- **Recovery**: Parse the cron output file at the `output_path` from the error
- Search for embedded JSON block (look for `"checkpoint_run_id"` or `"summary_ja"`)
- Save recovered JSON to `triage_latest.json`

## Filesystem-Based Recovery Workflow (Mode 1b)

When the checkpoint JSON is valid but contains 0 articles, recover by scanning the filesystem directly:

### Step 1: Count unprocessed articles on disk
```python
import json, os, time
raw_dir = os.path.expanduser("~/wiki/raw/articles")
week_ago = time.time() - 7*86400
recent = [(f, os.path.getsize(os.path.join(raw_dir, f)))
          for f in os.listdir(raw_dir) if f.endswith('.md') and os.path.getmtime(os.path.join(raw_dir, f)) >= week_ago]
print(f"Recent articles on disk: {len(recent)}")
```

### Step 2: Cross-reference against ALL pipeline triage decisions
```python
processed = set()
for triage_path in [
    '/opt/data/.hermes/cron/data/blog_ingest/triage_latest.json',
    '/opt/data/.hermes/cron/data/newsletter/triage_latest.json',
    '/opt/data/.hermes/cron/data/dreaming/triage_latest.json',
]:
    try:
        d = json.load(open(triage_path))
        for dec in d.get('decisions', []):
            rp = dec.get('raw_path', '')
            if rp: processed.add(os.path.basename(rp))
    except: pass
unprocessed = [(f, sz) for f, sz, _ in recent if f not in processed and sz > 400]
print(f"Unprocessed (>400B): {len(unprocessed)}")
```

### Step 3: Read key articles, group by theme
- Focus on AI-relevant content (>400B files)
- Use `read_file` with `limit=50` to assess each article's topic
- Group by semantic themes (same approach as normal dreaming grouping)

### Step 4: Check existing wiki coverage
- `find ~/ai-topics/wiki -name "*topic-keyword*"` for filename matching
- `grep "YYYY-MM-DD" ~/ai-topics/wiki/log.md` for same-day processing
- Read entity/concept pages to verify actual content coverage (not just existence)

### Step 5: Score and output
- Use standard dreaming scoring (relevance 0.30, frequency 0.25, etc.)
- Save grouped themes to `${HERMES_HOME}/cron/data/dreaming/grouped_themes_latest.json`
- Expected yield: ~200 raw articles → 8-15 genuinely unprocessed → 3-5 takes, 3-5 references

### Mode 1b-variant: Stale triage JSON from prior run
- **Symptom**: Checkpoint has `total_articles: 0`, `triage_latest.json` exists with decisions, but those decisions are from a **previous run already consumed** by `dreaming-wiki-ingest`
- **Detection**: Check `grep "Dreaming wiki-ingest\|dreaming.*consolidation" wiki/log.md | head -5`
  - If a dreaming-wiki-ingest entry exists AFTER the triage JSON's timestamp → prior triage consumed → safe to overwrite
  - If no entry exists → prior triage may be pending → use it as-is
- **Validated**: July 2026 — checkpoint had `total_articles: 0`, `triage_latest.json` had 50 decisions from prior run. `log.md` confirmed "Dreaming wiki-ingest — 2 takes + 2 references enriched" from July 1 → prior triage consumed → fresh triage saved with 9 new decisions
- **Action**: Overwrite `triage_latest.json` with fresh decisions from filesystem-based recovery

## Post-Recovery Verification

After recovering the triage JSON, independently verify each reference recommendation:
1. Read the target entity/concept page (all >40-line pages must use `patch` not `write_file`)
2. Check if the article's specific claims/data are present, not just URL in sources
3. In a June 2026 run, 2/8 reference items (25%) were false positives — already covered

If verified-false, skip enrichment. Downgrade from Reference to Skip with reason.
If genuine gap, proceed with enrichment.

## Verification Pattern

```python
# Check existing page depth before confirming triage recommendation
import os, sys
page_path = "/opt/data/ai-topics/wiki/entities/page-name.md"
if os.path.exists(page_path):
    with open(page_path) as f:
        content = f.read()
    if "target-keyword-from-article" in content:
        print("ALREADY COVERED — skip enrichment")
    else:
        print("GAP FOUND — proceed with enrichment")
else:
    print("PAGE MISSING — check if this is a genuine gap")
```
