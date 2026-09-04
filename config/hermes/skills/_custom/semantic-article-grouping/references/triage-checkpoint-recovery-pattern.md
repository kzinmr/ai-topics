# Triage Checkpoint Recovery Pattern

**Problem**: The downstream wiki-ingest pipeline receives `"failed to parse JSON response from <pipeline>-triage output"` — the upstream triage agent's cron response wrapped JSON in markdown and Hermes couldn't parse it.

**Common cause**: The triage agent saves the checkpoint file **before** attempting to render its markdown cron response. If the JSON parse fails on the wrapper, the data is already safe on disk. The error is on the markdown-serialization step, not the triage logic.

## Recovery Procedure

### Step 1: Check triage_latest.json first (fastest path)

```bash
ls -la /opt/data/.hermes/cron/data/{newsletter,blog_ingest,dreaming}/triage_latest.json
```

If the file exists, **read it directly** — no extraction, no script needed:
```bash
# Read with terminal for quick size check
wc -l /opt/data/.hermes/cron/data/newsletter/triage_latest.json

# Or use Python for verification
python3 -c "import json; d=json.load(open('/opt/data/.hermes/cron/data/newsletter/triage_latest.json')); print(f'Decisions: {len(d.get(\"decisions\",[]))}'); print(f'Summary: {d.get(\"summary_ja\",\"none\")[:200]}')"
```

For small files (<200 lines), `read_file` works directly — the JSON is human-readable and all fields (`decisions[].recommended_action`, `candidate_wiki_path`, `reason_ja`, `body_excerpt`) are accessible.

### Step 2: Verify decisions are appropriate

After loading, confirm:
- Decisions match the expected pipeline (check `source_checkpoint` or `generated_at` field)
- `take` items reference the correct `candidate_wiki_path` entities
- No decisions are stale (from a previous run — verify date matches today)

### Step 3: Proceed with ingestion

After recovery, the triage JSON is identical to a successfully-parsed run. Use it the same way:
1. Process `take` items first (enrich/update entity pages)
2. Process `reference` items (minor enrichment or cross-reference)
3. Run archive (the archive script reads from `triage_latest.json` too)
4. Commit

## Pitfall: Empty or stale checkpoint

If `triage_latest.json` doesn't exist (first run of the day, skipped pipeline step) or contains stale data from yesterday:
- Check `ls -la /opt/data/.hermes/cron/output/<job-id>/` for the raw agent output file
- Extract JSON from the markdown wrapper (look for the `{...}` block after `## Response`)
- As a last resort, run the triage manually using the newsletter-ingest checkpoint

## Concrete Example (June 2026)

Newsletter-triage at 07:20 UTC reported `"failed to parse JSON response from newsletter-triage output"`. Checkpoint at `/opt/data/.hermes/cron/data/newsletter/triage_latest.json` contained:
- 9 valid decisions (3 takes, 3 references, 3 skips)
- All fields well-formed with no corruption
- The triage agent had saved the JSON before the markdown wrapper failed to serialize
- Recovery took ~30 seconds (one `read_file` call + verification)
