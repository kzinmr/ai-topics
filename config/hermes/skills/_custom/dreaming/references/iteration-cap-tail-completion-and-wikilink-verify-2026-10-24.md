# Dreaming wiki-ingest — iteration-cap recovery & outbound-wikilink verification (validated 2026-10-24)

## 1. Finish the mechanical tail BEFORE writing the report

The dreaming-wiki-ingest cycle has a fixed mechanical tail that is easy to leave undone when
context/iteration budget runs out:

1. index.md entries + `Total pages` / section-count bumps
2. `log.md` prepend (single `# Wiki Log` header, entry after it)
3. `python3 scripts/archive_triage.py dreaming --keep-reference`
4. `git add <explicit files>` + commit + push

Content enrichment (the interesting part) consumes most of the tool-call budget. On 2026-10-24
the run hit the **maximum tool-calling-iteration cap** with all 5 new pages + 2 enrichments +
index.md + log.md written and verified, but the **archive never ran and nothing was committed**.
The next session inherits an uncommitted tree and must redo the tail blind.

Rules that prevent this:
- Once takes/references are written, run archive + index/log + commit as ONE idempotent batch.
  Write the human-readable report LAST — a report describing uncommitted work is an incomplete
  deliverable.
- Pre-delivery gate: `cd ~/ai-topics && git status --short | grep wiki/` — if any of your files is
  still `M`/`??`, or today's `wiki/raw/archived/triage/dreaming/YYYY-MM-DD_*.json` is absent, you
  are not done. Include the exact `git add ... && git commit ... && git push` command in the report
  so the next session (or the user) can finish it verbatim.
- Build the commit command with EXPLICIT paths (never `git add wiki/`) — see the
  wide-sibling-dirty-tree staging caution in SKILL.md. The sibling tree (skills/, AGENTS.md,
  jobs.json) is permanently dirty between sessions.

## 2. Valid prior-day triage_latest.json is a legitimate recovery source

On 2026-10-24 the upstream `dreaming-group` render failed (`output_path` present, 1744-line
output file) and `triage_latest.json` carried a PRIOR `triage_run_id` (20261022T181000Z) with 12
valid decisions (3 take / 5 reference / 4 skip). Rather than rebuild decisions by reading the
output-file tail (expensive, error-prone, and the source of the wrong-page-pointer pitfall),
read `triage_latest.json` directly when it has a valid `decisions` array — it is already the
structured triage. Confirm it wasn't consumed (`grep "dreaming.*wiki-ingest" wiki/log.md`) before
trusting it. Quick shape probe (no pipe-to-interpreter):

    python3 -c "import json; d=json.load(open('/opt/data/.hermes/cron/data/dreaming/triage_latest.json')); print(d['triage_run_id'], {a: sum(1 for x in d['decisions'] if x['recommended_action']==a) for a in ('take','reference','skip')})"

## 3. Outbound-wikilink verification is the highest-value cheap gate

Every new/enriched page this session contained GUESSED wikilinks to nonexistent pages. All were
caught by one batch sweep and fixed to real pages:

- `concepts/inference-optimization` -> `concepts/inference`
- `concepts/self-improving-agents` -> `concepts/self-evolving-agents`
- `entities/pi-coding-agent` -> `entities/mario-zechner-badlogicgames`
- `concepts/the-culture-funnel` -> (no page; dropped the Related bullet entirely)

Pre-commit hooks do NOT check wikilink targets, so broken links silently pollute the graph for
the weekly graph-analysis job. Run this sweep after writing every page, before commit:

    cd ~/ai-topics
    for f in wiki/concepts/<new>.md wiki/entities/<new>.md ...; do
      grep -oE "\[\[[^]]+\]\]" "$f" | sed 's/\[\[//;s/\]\]//;s/|.*//' | sort -u | while read t; do
        [ -f "wiki/$t.md" ] || [ -f "wiki/$t/_index.md" ] || [ -f "wiki/$t/index.md" ] || echo "MISS $f -> $t"
      done
    done

Fix each MISS by re-pointing at the closest EXISTING page (found via
`find wiki/concepts wiki/entities -iname '*<kw>*'`) or dropping the bullet — do NOT create a stub
just to satisfy a Related link.

## 4. log.md prepend when the header is NOT at line 1

The watchdog auto-fix can leave entries ABOVE the `# Wiki Log` header (observed 2026-10-24:
a watchdog entry occupied L1-12, the header was at L14). The documented "insert after the italic
line" anchor breaks in this state. Robust approach: locate the header by line prefix
(`[i for i,l in enumerate(lines) if l.startswith('# Wiki Log')]`) and insert the entry as
`lines[:hi+1] + [''] + entry + [''] + lines[hi+1:]`, after asserting exactly one header line and
that your entry title is absent (idempotency guard). This preserves the header-first invariant and
is idempotent on re-run. The canonical repair script
(`config/hermes/skills/_custom/dreaming/scripts/repair_log_md_header.py`) handles the fully-buried
case; this inline pattern handles the single-header-with-stray-entries-above case.
