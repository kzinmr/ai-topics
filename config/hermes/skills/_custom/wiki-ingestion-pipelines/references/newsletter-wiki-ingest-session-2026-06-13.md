# Newsletter Wiki Ingest Session 2026-06-13: Case C Recovery + Reference Enrichment

## Scenario
- newsletter-triage (07:20 UTC) failed with "failed to parse JSON response from newsletter-triage output"
- Cron runner wrapped the triage agent's JSON response in markdown → JSON parser couldn't extract it
- **BUT**: The checkpoint at `${HERMES_HOME}/cron/data/newsletter/triage_latest.json` was valid (11,922 bytes, 9 decisions) — the triage agent correctly saved JSON to the pipeline path before producing its cron response

## Recovery Flow
1. Checked checkpoint file existence at standard pipeline path (`ls -lt /opt/data/.hermes/cron/data/newsletter/triage_latest.json`)
2. Read the checkpoint JSON — confirmed valid `decisions` array with `checkpoint_run_id`, `summary_ja`, `recommended_action` fields
3. Independent verification: read existing wiki pages (fable-5.md, entities/kimi.md) to confirm triage's coverage assessment
4. Proceeded with minor enrichment despite 0 takes

## Outcome: 0 Takes, 2 References Enriched
| Decision | Action | Lines added |
|----------|--------|-------------|
| ★★★☆☆ Reference: Fable 5 sovereignty risk | 1-line bullet to Significance section | +1 |
| ★★★☆☆ Reference: Kimi K2.7 Code | Full section in entities/kimi.md + timeline table row + References | +35 |

Key insight: **0 takes does not mean [SILENT] if references genuinely fill gaps.** The triage correctly rated these as references (★★★☆☆) — the fable-5.md content was a perspective framing (not new facts), and the Kimi K2.7 Code had a primary source (Fireworks blog) arriving via sitemap-monitor at 06:00. But both justified minor enrichment.

## What Worked
- `patch()` for targeted 1-line insertion into rich wiki pages (fable-5.md, 337 lines)
- `patch()` with `read_file` to find exact insertion points in entity pages
- Log.md prepend via Python script (`write_file` to /tmp/ + `terminal python3`)
- Pre-commit tag validation passed on first commit (43 files, 5,245 insertions)

## Pitfall Encountered: patch() pipe prefix corruption
The first `patch()` call introduced `|-` pipe prefixes on the new lines. **Root cause**: the `new_string` was constructed from read_file offset/limit output that shows `N|` line number prefixes. The pipe prefix was baked into the `new_string` even though the old_string was correct. **Fix**: Use `sed -n 'N,Np' file | cat -A` to verify actual file content before patching. After the patch, fix `|-` → `-` with a second `patch()`.

## Timeline
- 07:24 — newsletter-triage fails (cron output parse error)
- 07:41 — newsletter-wiki-ingest starts recovery
- 07:45 — fable-5.md + kimi.md patches applied
- 07:47 — log.md updated
- 07:48 — commit + push (b50505a9)
