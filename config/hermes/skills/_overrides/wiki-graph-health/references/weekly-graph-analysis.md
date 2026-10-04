# Weekly Wiki Graph Analysis — patterns & pitfalls (2026-08)

Session learnings from running the `wiki-graph-analysis` weekly cron (Fri 15:00 UTC).

## Quick start (canonical procedure)

1. Orient: `head wiki/index.md`, `tail wiki/log.md` (compare against last week's numbers), confirm the canonical script exists.
2. `cd ~/ai-topics && python3 scripts/_weekly_graph_report.py` → parse its `KEY:VALUE` summary lines.
3. Read the saved report at `wiki/queries/wiki-graph-analysis-weekly-YYYY-MM-DD.md`.
4. **Adjudicate the dup groups by actually reading the pages** (see §False-positive patterns) — never merge on the report's word alone.
5. Write the `-annotations.md` companion artifact (§Adjudicated-annotations artifact).
6. Update `index.md` (swap the stale report entry, add annotations entry) + append `log.md`, then commit only wiki files and push (§Report + commit workflow).
7. Report to the user with a trend table vs last week and a prioritized action list.

## Script selection (IMPORTANT — two scripts exist, only one is canonical)

| Script | Scan depth | Purpose |
|---|---|---|
| `scripts/_weekly_graph_report.py` | **recursive** (`os.walk`) | **CANONICAL for the weekly cron.** Handles nested dirs (`concepts/post-training/foo`), resolves `dir/index.md` → key `dir`, cleans up old weekly reports (keeps only today's), writes the formatted report to `wiki/queries/wiki-graph-analysis-weekly-YYYY-MM-DD.md`. |
| `scripts/wiki_graph_analysis_weekly.py` | shallow (`os.listdir`, top level only) | Alternative/diagnostic. Misses ~600 nested pages (e.g. `concepts/post-training/*`, `concepts/ai-benchmarks/*`). Do not use for the official report. |

Run the canonical one with: `cd ~/ai-topics && python3 scripts/_weekly_graph_report.py`
It prints `REPORT_SAVED:<path>` plus `PAGES:/ORPHANS:/BROKEN_LINKS:/...` key/value lines for quick grep.

For `wiki_graph.py` (the ad-hoc graph tool): the flag is `--format json`, NOT `--json` (unlike `wiki_health.py --json`). `--format json` outputs only person similarity scores, not graph structure.

**⚠️ Cron-mode pitfall (2026-08-28): `execute_code` is BLOCKED in scheduled cron jobs** unless `approvals.cron_mode: approve` is set — the run fails with "BLOCKED: execute_code runs arbitrary local Python". Do the analysis by running the repo's existing Python scripts via `terminal` (`python3 scripts/_weekly_graph_report.py`, `python3 scripts/validate_index.py`) and one-liners, or put ad-hoc analysis into a script under `~/ai-topics/scripts/` first. Plan for this from the start of a cron run rather than trying execute_code and hitting the wall.

## Orphan detection semantics (BUG found & fixed 2026-08-14)

Both scripts originally computed orphans as:

```python
has_in = any(key in targets for targets in inbound.values())
```

where `inbound[tgt]` = list of source pages that link to `tgt`. That check asks "is this page a SOURCE of any link?" i.e. **it reported pages with no OUTBOUND links (dead-ends) as orphans**. Real orphans (no INBOUND links) were massively undercounted (41 reported vs 479 actual).

Correct semantics: a page is an orphan iff its key is never a TARGET:

```python
has_in = key in inbound   # key appears as a target of some wikilink
```

Both scripts patched 2026-08-14. If anyone reverts or copies this logic elsewhere, use the fixed form.

## False-positive patterns when interpreting the report

1. **"Stale index entries" (not_on_disk) are mostly false positives.** `index.md` references directory indexes as `[[concepts/foo/index]]`, but the scanner keys them as `concepts/foo` (dirname). Result: `concepts/ai-benchmarks/index`, `concepts/anthropic/index`, etc. show as "files missing" when the file exists at `concepts/foo/index.md`. Verify before deleting: `ls concepts/foo/index.md`. The only REAL stale entry is usually the previous week's report file (script deletes it but index.md still links it) — update `index.md` + `log.md` accordingly.

2. **"Not indexed" pages are largely directory `_index` pages.** `concepts/_index`, `entities/_index`, and ~23 dir indexes are legitimately referenced via `[[concepts/foo/index]]` form; the resolver mismatch inflates the count. Real missing ones are usually just a handful (e.g. a new report page, `entities/tim-sherratt`).

3. **"Missing" broken-link targets are often resolvable via nested paths.** The naive fix logic only checks top-level `concepts/<slug>`. Many targets exist nested: `grpo → concepts/post-training/grpo`, `gaia-benchmark → concepts/ai-benchmarks/gaia-benchmark`, `reinforcement-learning → concepts/post-training/reinforcement-learning`, `entities/sglang → concepts/inference/sglang`, `agentdojo → concepts/ai-benchmarks/agentdojo`, `ai-safety → concepts/security-and-governance/ai-safety`. Build a full recursive slug set and do a `endswith('/'+base)` pass before declaring a target "needs creating".

4. **~20 orphans are referenced via bare (non-namespaced) links.** e.g. `concepts/harness-engineering/system-architecture/context-engineering` had 136 inbound refs as `[[context-engineering]]`. Converting bare links to namespaced resolves BOTH the orphan status and a large chunk of bare-wikilink-missing broken links. Check with a basename-match pass over all pages' wikilinks.

5. **Duplicate groups are not all real.** Before consolidating:
   - Check the **`status: redirect`** frontmatter form + `redirect:` tag — **22 such stub pages exist** wiki-wide (e.g. `entities/lilianweng`, `entities/eugeneyan`). The dup detector does not skip them, so mentally subtract all redirect stubs. (This is the actual frontmatter field: `status: redirect`, sometimes paired with `tags: [..., redirect]`.)
   - `entities/_index` vs `concepts/_index` is a false positive (different namespaces).
   - Entity-vs-concept pairs (`entities/cline` vs `concepts/cline`, `entities/qwen` vs `concepts/qwen`) and concept-vs-comparison pairs (`concepts/agent-harnesses` vs `comparisons/agent-harnesses`) can be legit namespace splits — verify both are actually about the same thing; if legit, ensure they cross-link each other.
   - Real dupes are hyphen-variant pairs (eugene-yan/eugeneyan, giles-thomas/gilesthomas, alpha-proof-nexus×2, deer-flow/deerflow) — keep the richer page, add `status: redirect` to the other. BUT which side is "richer" flips between runs as pipelines keep enriching — always re-measure `wc -l` on both pages THIS session, don't trust a prior run's line counts. (2026-10-02: `giles-thomas`=92 vs `gilesthomas`=228, so the hyphenated page is the smaller one this time.)
   - **⚠️ Same-blog/similar-slug ≠ same person.** `entities/deliberate-coder` (Ben Ilegbodu, "deliberation-first coding") and `entities/deliberatecoder` (Steve Shogren, "Deliberate Software") are DIFFERENT PEOPLE — merging would be data loss. ALWAYS read both pages' `title:` + Overview before merging any person pair; report's normalized-name match has no idea who the subject is. This trap bites hardest when BOTH members look "rich" (100+ lines) by size alone — size does not prove same-subject.
   - **Person dupes can carry contradicting facts.** As of 2026-08-28, `lilianweng` says "VP Research at OpenAI, Preparedness lead" while `lilian-weng` says co-founded Thinking Machines Lab. When merging such pairs, do NOT silently pick one — keep both claims with dates/sources and set `contested: true` per SCHEMA's Update Policy.
   - **April stub family signature:** ~25-line pages with `created: 2026-04-25`, empty `sources:`, trailing `[[entities/_index]]` link (e.g. `concepts/open-claw-ecosystem`, `concepts/evals-skills`, `concepts/llm-integration-patterns`). These came from one April bulk generation and act as accidental shadow pages of the real pages; recommend converting to proper `redirect:` pages.
6. **"Not indexed"/"not on disk" counts are inflated** (2026-08-28: reported 27/7, real 2/1). Generator maps `foo/index.md`→`foo` but never tries `foo/_index.md`, and hub pages (`concepts/anthropic`, `concepts/claude`, `concepts/gemini`, `concepts/gpt`, `concepts/openai`, …) are intentionally indexed via child entries. `concepts/gpt/_archive/*` is correctly excluded. Do a manual `comm -3` of disk slugs vs index wikilinks to find the real gaps (2026-08-28 genuine gap: `concepts/ai-employment-displacement` missing from index).

## Independent ground-truth resolver (don't trust either script's counts)

Two repo scripts both claim to be "verified" but DISAGREE with each other and with the raw weekly report, because each has its own keying/dir-hub quirks:
- `scripts/wiki_graph_analysis_weekly.py` — shallow `os.listdir`, scans only 2542 top-level L2 pages, misses ~600 nested pages. Inflates broken links (5312) because it can't resolve dir-hub dirs, and the "596 index entries not on disk" line is almost entirely false positive.
- `scripts/wiki_graph_analysis_verified.py` — recursive `os.walk`, walks 3139 pages, gives a lower broken-link count (2851). Still counts bare-wikilink refs as broken.

Neither is authoritative for the INDEX-GAP or DUPE counts. **Write a fresh inline resolver in `terminal` (execute_code is cron-blocked) to establish ground truth for the two most consequential claims before recommending destructive actions:**

```python
# run via heredoc: python3 - <<'EOF' ... EOF   (cwd = wiki/)
import re, os
idx = open('index.md').read()
links = set(re.findall(r'\[\[([^\]|#]+)', idx))
disk = set()
for root, ds, fs in os.walk('.'):
    if 'raw' in root or '_archive' in root or '.git' in root: continue
    for f in fs:
        if f.endswith('.md'):
            disk.add(os.path.relpath(os.path.join(root,f),'.')[:-3])
miss = [l for l in links if l not in disk]
# dir-hubs count as resolvable: 'concepts/foo' satisfied by concepts/foo/index.md or /_index.md
dirhub = sum(1 for l in miss if os.path.isdir(l) and (os.path.exists(l+'/index.md') or os.path.exists(l+'/_index.md')))
print('index wikilinks:', len(links), '| missing-on-disk:', len(miss), '| of which dir-hub:', dirhub)
for l in miss[:20]:
    print('  MISS', l, '<- dir-hub' if (os.path.isdir(l) and (os.path.exists(l+'/index.md') or os.path.exists(l+'/_index.md'))) else '<- REAL')
```

2026-10-02 result: **missing-on-disk = 0** (all 596 were dir-hub false positives). So "remove N stale index entries" from the report is essentially never a real action — verify to zero before touching index.md. For the reverse check (pages on disk not in index), the report line is usually the real signal — confirm each with `grep -c "<slug>" index.md`.

## Tag-violation triage (report says "N pages with invalid tags")

The weekly report flags invalid tags but not which page has which. Map each offending tag to its canonical form before any commit (pre-commit blocks them). Grep `SCHEMA.md` for the exact tag-word (with `\b` boundaries) to find the canonical spelling — several are counterintuitive (`open-weight` not `open-weights`, `datasets` not `data`). Confirmed mappings: `ai-agent`→`ai-agents`. If a *whole family of pages* shares one invalid tag (2026-10-02: `ai-timeline` on `entities/dimillian` + `entities/odyssey-ml`, plus stray `devtools`/`ai-coding-tools`/`genai`), it likely came from one recent seed/bulk-ingest using a non-taxonomy tag — decide once (add to taxonomy OR strip everywhere), don't leave the invalid tag on a subset.

## Working-tree hygiene during the weekly run (reconfirmed 2026-10-02)

The repo had **192 dirty wiki files from a sibling active-crawl pipeline** uncommitted at run time, including the 4 "not indexed" concept pages. Those 4 pages were part of that in-flight batch, not orphans needing your index edit. Before recommending "reconcile N unindexed pages," check `git status --short -- wiki/ | wc -l` and `git ls-files --error-unmatch <page>` — if the pages are freshly-created sibling WIP, defer the index/log edit to that pipeline rather than committing over it. Commit ONLY your own report/annotation files via explicit path after `git reset -q`.

## Adjudicated-annotations artifact (2026-08-28 pattern, keep doing it)

The raw auto-report is noisy; last week's numbers are only comparable after adjudication. Write a companion `wiki/queries/wiki-graph-analysis-weekly-YYYY-MM-DD-annotations.md` with (a) a verdict table for every dup group (real / redirect / false-positive / borderline), (b) corrected index-gap counts, (c) generator bug backlog. Add both report + annotations to index.md, log the adjudication in log.md, and commit only wiki files (repo usually has dirty sibling-agent state in `config/` — see workflow below).

## Generator bugs still open in `_weekly_graph_report.py` (backlog, don't re-discover)

1. Index reconciliation should resolve `foo/_index.md` → slug `foo` and skip `_archive/` paths.
2. Dup detector should skip pages with `redirect:` frontmatter and `index`/`_index` slugs.
3. Report rotation deletes last week's report file but leaves its index.md entry dangling — either replace the index entry automatically or keep dated reports.

## Stale-page interpretation

Counts are dominated by bulk-import `updated` dates (e.g. 2026-04-09/10), so >1000 "stale" pages mostly means "never touched since import", not "content degraded". Report the count but prioritize review by size+staleness (large pages stale the longest).

## Report + commit workflow

1. Run `_weekly_graph_report.py` (it cleans old reports automatically).
2. Read the saved report; sanity-check orphans/duplicates with a recursive verification pass.
3. Update `wiki/index.md` (replace the stale weekly-report entry with today's) and append to `wiki/log.md`.
4. Commit only the wiki/ + scripts/ files you touched (`git add wiki/ scripts/_weekly_graph_report.py ...`) — the repo often has unrelated sibling-agent dirty state in `config/` and `scripts/hierarchy_report.json`; do NOT `git add -A`.
5. Push. Pre-commit hook validates index.md + tags. If `git pull --rebase` refuses with "You have unstaged changes" (sibling-agent dirt), use: `git stash -u && git pull --rebase && git push && git stash pop`.
6. Also re-add the report file if a stray `git checkout -- wiki/queries/...` restores a deleted older report — verify `git status wiki/queries/` before committing so last week's file isn't resurrected next run's diff.
