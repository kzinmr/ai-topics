# Watchdog session — 2026-11-08

## Outcome
2 auto-fixes (index.md), both committed+pushed (`6bb4ae55`). Otherwise healthy-baseline run.

## Auto-fixed
1. **Duplicate `[[entities/metR]]` in index.md** — 2 lines, 1 file on disk. Unlike the
   2026-08-19 "redirect stubs are legitimately indexed twice" case, `entities/metR.md` is the
   only file (no stub pair), so this was a genuine duplicate → removed the shorter line.
   Pre-check still mandatory: `ls wiki/entities/<slug>.md` count.
2. **Entity header recount** — `## Entities (966 pages)` → `(965 pages)`. Recount formula that
   matched reality: count lines `l.lstrip().startswith('- [[entities/')` in the Entities section
   (stop at next `## `). Concepts (2318) / Comparisons (35) / Events (51) / Queries (52) headers
   all verified ACCURATE — do not blanket-"fix" every header, verify each against its section.
   Note: index entity lines (965) ≠ filesystem top-level count (957) because 7 nested subdir
   entries + archived slugs are indexed. Section-line count is the right denominator, not `find`.

## Graph report items already closed upstream (verify-then-skip, per skill)
Weekly report was 50.5 h old. Both of its "pending one-line fixes" were done at Nov 6 17:38,
i.e. AFTER the 15:05 report generation:
- `concepts/qwen` → `[[entities/qwen]]` backlink (present, line 81)
- `concepts/agent-harnesses` → `[[comparisons/agent-harnesses]]` (present, line 146)
Also `[[concepts/ai-benchmarks/swe-bench\]]` stray-backslash links: **0 in content pages** —
the 10 refs only appear as *text inside* `queries/wiki-graph-analysis-weekly-*.md`. So the
"mechanical fix" recommendation was already moot. Lesson: always `grep` the claimed defect
outside the report file itself before "fixing" it.

## Clean scans (no action)
- index: 0 pipe-prefix / line-number-prefix / triple-bracket / ghosts (recursive, nested-exempt)
- 0 pages missing frontmatter; 0 missing `sources` (2674 top-level entity+concept pages)
- 0 L2 `|- [` pipe bullets in entities/ + concepts/
- log.md: exactly 1 `# Wiki Log` H1, not buried

## Cron failures — recurring classes (7 jobs errored on last run)
- `Response truncated due to output length limit` — blog-ingest, blog-triage→blog-wiki-ingest
  chain, skeleton-enrich-daily, jp-to-en-translation. **Recurring across sessions.** Triage rule
  (reconfirmed 2026-11-04, 2026-11-08): check the *artifact* before re-running — today's raws
  WERE persisted (`find wiki/raw/articles -mmin -1440` → 23 files) and all 19 sibling dirty
  files were committed by 11:02, so truncation was a reporting failure, not a work loss.
- `HTTP 503: Local LLM server is busy; Hermes should fall back to the external provider` —
  active-crawl, blog-triage, Weekly AI digest. Same message across jobs = one infra event; the
  wording itself indicates missing external-provider fallback config, which is a human fix.
- `dreaming-wiki-ingest` error string is literally the report body (`RuntimeError: # Dreaming
  Report — …`) → wrapper misclassification, not a real failure; downstream output existed.

## Notes
- `hermes` binary is NOT on cron PATH. Use `export PATH="/opt/hermes/bin:$PATH"` first, else
  `hermes: command not found`.
- `execute_code` blocked in cron mode → wrote log-prepend script to /tmp, ran via `python3`.
- Untracked `config/hermes/skills/**` files from sibling pipelines left for those pipelines.
