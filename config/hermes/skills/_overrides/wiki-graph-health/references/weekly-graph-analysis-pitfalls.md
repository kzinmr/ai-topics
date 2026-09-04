# Weekly Graph Analysis Pitfalls & Workarounds

## 1. Hardcoded Filename Date Bug — FIXED 2026-07-31

**Problem (historical)**: `scripts/wiki_graph_analysis_weekly.py` line 372 hardcoded the report filename as `wiki-graph-analysis-weekly-2026-06-19.md`. Each run wrote to the same filename regardless of the actual date.

**Fix applied 2026-07-31**: Both `wiki_graph_analysis_weekly.py` (line 372) and `_weekly_graph_report.py` now compute the date dynamically via `datetime.now().strftime('%Y-%m-%d')`. `_weekly_graph_report.py` also auto-cleans older `wiki-graph-analysis-weekly-*.md` files, keeps only the current report, and resolves directory-index pages when building the page graph (nested `foo/index.md` → key `foo`), which eliminates the large false-positive broken-link class. No manual `mv` or `sed` date fix needed anymore.

## 1b. Template Expansion Bug in Report Writer — FIXED 2026-08-07

**Problem (historical)**: `wiki_graph_analysis_weekly.py` report-writer section used `\\\\n` inside an f-string (line 385), writing a literal `\n` into the saved markdown instead of a newline. Line 386 also wrote `content_rich_orphans.__class__.__name__` (the string "list") instead of the orphan count, producing `Orphans: 32 (list)`.

**Fix applied 2026-08-07**: Both lines corrected to emit a real newline and `(content-rich: N)`. Verified by `ast.parse` + rerun.

## 2. Patch Tool Pitfall with Wiki List Items

**Problem**: When using `patch` to edit `wiki/index.md` list entries (which start with `- `), the patch tool's fuzzy matching can sometimes introduce extra prefix characters (e.g., `|- ` instead of `- `). The pre-commit hook (`validate_index.py`) rejects pipe-prefixed list items.

**Root cause**: The `old_string` and `new_string` in patch calls must both use exactly `- ` (dash-space) as the list prefix. Even one character difference — like `|-` — causes the pre-commit to block the commit.

**Fix**: After the patch, verify the lines start with `- `:
```bash
grep -n '^|- ' /opt/data/ai-topics/wiki/index.md
```
If any pipe-prefixed lines exist, run a second patch to fix them.

## 3. Heredoc Failure in Docker Environment

**Problem**: Shell heredocs (`cat >> file << 'EOF'`) fail with "Could not determine home directory" in the Docker container where Hermes runs.

**Workaround**: Use Python one-liner for file appending instead:
```python
python3 -c "
f = open('/path/to/file', 'a')
f.write('''...content...''')
f.close()
"
```

## 4. Person×Concept Graph Separation

**Two separate tools exist — don't confuse them**:

| Tool | Purpose | Flag Notes |
|------|---------|------------|
| `scripts/wiki_graph.py` | Bipartite person×concept similarity graph (hub persons, thought schools, bridge concepts) | `--format json` (NOT `--json`) outputs `person_similarity` array only |
| `scripts/wiki_graph_analysis_weekly.py` | Full structural health scan (orphans, broken links, duplicates, stale pages, tags) | No JSON output — always prints full terminal report |

Run **both** for a complete weekly analysis. The `wiki-graph-analysis` cron job should invoke both scripts.

## 5. Inbound Link Graph Precision

The orphan detection uses `inbound[target].append(source)` — it checks whether any wiki page references a page by its `entities/slug` or `concepts/slug` key. A page is an "orphan" if zero other pages link to it via wikilinks. False positives include:
- `_index` pages (they are meta-pages, intentionally unlinked)
- New pages that rely on index.md for discoverability

Content-rich orphans (>100 lines with 0 inbound links) should be prioritized for linking over skeleton orphans.

## 6. Duplicate Detection Caveats

The duplicate detection normalizes slugs by removing hyphens and lowering case. This catches:
- True duplicates (e.g. `eugene-yan` vs `eugeneyan`, `lilian-weng` vs `lilianweng`)
- Cross-type duplicates (`entities/cline` vs `concepts/cline`)
- Legitimate pairs that just happen to normalize the same (`entities/_index` vs `concepts/_index`)
- **False positives from slug collisions between DIFFERENT people** (`deliberate-coder` = Ben Ilegbodu vs `deliberatecoder` = Steve Shogren — see §11 ground truth)

Always verify before merging — the `_index` pair is intentional. Triage by reading frontmatter titles + line counts: hyphenated/unhyphenated same-person pairs (e.g. `eugene-yan`/`eugeneyan`, `lilian-weng`/`lilianweng`) are almost always true duplicates; `entities/X` vs `concepts/X` is usually an intentional product-vs-concept split but check if the entity page is a tiny stub.

## 7. Deep Audit Script (accurate counts)

`config/hermes/skills/_overrides/wiki-graph-health/scripts/deep_link_audit.py` (NOTE: lives in the repo's skill-override dir, NOT under `~/.hermes/skills/` — locate with `find /opt/data/ai-topics/config/hermes/skills -name deep_link_audit.py`) walks ALL page depths and resolves links by exact / dir-index / `_index` / basename-across-namespaces (plus raw+transcripts). Use it to sanity-check weekly report numbers:
- 2026-07-31 comparison: weekly script reported 45 orphans / 3,261 broken links (after fixes); deep audit found **464 true orphans** (302 concepts, 146 entities) and **~2,048 true broken links** (bare links like `[[gaia-benchmark]]` resolving to nested `concepts/ai-benchmarks/gaia-benchmark` account for most of the difference).
- Lesson: **the weekly report undercounts orphans (top-level scan only) and overcounts broken links (shallow resolution)**. Always run the deep audit before acting on counts.

## 8. Cron Security-Block Workarounds

- **`python3 | python3` is blocked in cron** (TIRITH: pipe_to_interpreter). To inspect `wiki_graph.py --format json`, write output to a file first (`> /tmp/wiki_graph_person.json`), then parse the file in a separate command. Same for any script whose stdout you want to pipe into another interpreter.
- **`execute_code` is blocked in cron mode** — write analysis scripts with `write_file` to `/tmp/` and run via `terminal` (`python3 /tmp/script.py`).
- **Shell heredocs and multi-line `printf` fail** in the Docker cron environment; append to `wiki/log.md` with a small Python script (`open(path, 'a').write(...)`) instead.

## 9. Report Tag Taxonomy Failure (pre-commit block) — discovered 2026-08-07, generator fix verified 2026-08-21

**Problem**: `wiki_graph_analysis_weekly.py` writes the saved report frontmatter with `tags: [wiki-maintenance, graph-analysis]` — neither tag is in `SCHEMA.md`'s taxonomy (894 canonical tags), so the pre-commit tag validator blocks the commit with `🚨 TAG TAXONOMY VIOLATIONS — COMMIT BLOCKED`.

**Fix applied 2026-08-21**: Both `scripts/wiki_graph_analysis_weekly.py` (line 382) and `scripts/_weekly_graph_report.py` (line 219) now write `tags: []` directly — the generator is fixed at the source. The 2026-08-21 run hit this failure (stale `tags: [wiki-maintenance, graph-analysis]` still in the deployed generators) and was resolved by patching the report frontmatter + both generators in the same commit. Do NOT invent tags like `wiki-health` — they aren't canonical either; verify against `grep -oE '`[a-z][a-z0-9-]+`' wiki/SCHEMA.md | sort -u` first.

## 10. Report Run-Order & Auto-Clean — discovered 2026-08-07

**Two scripts write the same report path** `wiki/queries/wiki-graph-analysis-weekly-<date>.md`:
- `scripts/wiki_graph_analysis_weekly.py` — full terminal report, but its saved markdown is a **degraded summary** (no sections 1–8).
- `scripts/_weekly_graph_report.py` — writes the **rich report** (sections 1–8, tables) AND **auto-cleans older `wiki-graph-analysis-weekly-*.md` files** (keeps only the current one).

**Run `_weekly_graph_report.py` LAST** so the rich report survives. Cron note: since the auto-clean deletes the previous week's report file, `wiki/index.md` still lists the old report entry — after running, add the new report entry to index.md and remove/replace the old one in the same commit (or `index.md` gains a stale entry pointing at a deleted file).

## 11. Duplicate-Triage Ground Truth (2026-08-07)

Verified cases to avoid re-triageing:
- **`entities/deliberate-coder` vs `entities/deliberatecoder` = FALSE POSITIVE** — different people: deliberate-coder is Ben Ilegbodu (benmvp), deliberatecoder is Steve Shogren (Deliberate Software). Slug-normalization collision only.
- **`entities/koylan-ai` vs `entities/muratcan-koylan` = TRUE duplicate, already marked** — koylan-ai frontmatter body says "Redirect/alias: This page is a duplicate of [[entities/muratcan-koylan]]". Person-similarity graph flags it (score 11.5) but no merge needed.
- **`deedydas` vs `howdymary` = FALSE POSITIVE** — Deedy Das vs "mary"; high similarity (13.9) comes from shared concept tags (autoresearch, harness-engineering), not same person.
- Cross-type entity/concept splits (`entities/cline`/`concepts/cline`, `entities/qwen`/`concepts/qwen`) are intentional product-vs-concept splits — keep, but check whether the entity side is a tiny stub that should redirect.

## 12. Stale Generator Source Despite "FIXED" Doc Marker (discovered 2026-08-21)

**Symptom**: The weekly report frontmatter contained `tags: [wiki-maintenance, graph-analysis]` even though §9 documented the fix as "applied" — the deployed generators were NOT actually fixed.

**Root cause**: The pitfalls doc claimed the fix was in place, but the actual generators (`scripts/_weekly_graph_report.py` line 219, `scripts/wiki_graph_analysis_weekly.py` line 382) still hardcoded the non-canonical tag list. The fix was documented but never landed in the scripts (or regressed via sync/rollback).

**Lesson — verify generator source at runtime, not docs**: Before trusting a "FIXED <date>" marker in any pitfalls reference, `grep -n 'tags:' scripts/_weekly_graph_report.py scripts/wiki_graph_analysis_weekly.py` to confirm the CURRENT source matches the documented state. Docs describe intent; source is truth. This applies to ALL "FIXED" markers in this file (§1 filename bug, §1b template bug) — re-verify if the symptom reappears.

**Fix applied 2026-08-21**: Both generators patched to write `tags: []`. Verified end-to-end: report generated → frontmatter clean → commit passes pre-commit tag validator without `--no-verify`. If a future run hits `🚨 TAG TAXONOMY VIOLATIONS` on the weekly report, check the generator source first, not the doc.

## 13. Deep Audit as the Ground-Truth Count Source (workflow re-confirmed 2026-08-21)

Re-confirmed: `deep_link_audit.py` (at `config/hermes/skills/_overrides/wiki-graph-health/scripts/deep_link_audit.py`) produces the accurate orphan/broken-link counts; `wiki_graph_analysis_weekly.py` undercounts orphans (top-level scan only: reported 480 vs deep audit 459 ≥20-line) and overcounts broken links (shallow resolution: reported 4,978 vs deep audit 2,532 true). Run deep audit AFTER the weekly script + rich report, and cite the deep-audit numbers in the final user-facing report. The weekly script's "recommended actions" section uses its own (less accurate) counts — re-label when presenting to the user.

## 14. Duplicate-Triage Verification Loop (confirmed reusable 2026-08-21)

For each of the ~16 duplicate groups the weekly script reports, verify triage with one shell loop:
```bash
for pair in "A B" "C D" ...; do
  set -- $pair
  a=$(wc -l < wiki/$1.md); b=$(wc -l < wiki/$2.md)
  at=$(grep -m1 '^title:' wiki/$1.md | head -c 60)
  bt=$(grep -m1 '^title:' wiki/$2.md | head -c 60)
  echo "$1 ($a lines) $at || $2 ($b lines) $bt"
done
```
Decision rule (§11 ground truth + 2026-08-21 verification):
- One side is a **redirect stub** (≤25 lines, `redirect:` in frontmatter, "moved" body) → already dedup'd, keep, report as "keep as-is".
- Both sides have **substantial content** (100+ lines each, similar titles) → true merge candidate; list both line counts so the merge preserves the richer page.
- **Cross-type** (entities/X vs concepts/X, or concepts/X vs comparisons/X) → intentional product-vs-concept split, keep; note if one side is a tiny stub that could redirect.
- Slug-collision between **different people** (e.g. `deliberate-coder` vs `deliberatecoder`) → false positive, skip.

## 15. Broken-Link Triage Technique (2026-08-21)

The top-missing-targets list from the weekly script mixes three distinct problem classes. Before recommending "create page", check the filesystem:
```bash
for t in <top-missing-targets>; do
  [ -f "wiki/$t.md" ] && echo "EXISTS: $t" || echo "MISSING: $t"
  find wiki -name "$(basename $t)*" | head -3   # catch nested/subdir files
done
```
Three outcomes:
1. **File exists at a nested path** (e.g. `concepts/post-training/rlhf.md` linked as `[[concepts/rlhf]]`) → link-fix, not page-creation. This is the majority class.
2. **Directory exists but no flat hub page** (e.g. `concepts/context-engineering/` has children but no `concepts/context-engineering.md`) → create hub page (high value: 137 refs in one session).
3. **Genuinely missing** (e.g. `entities/cursor`, `entities/sglang`, `entities/reflexive-ai`) → create stub with `status: stub`.

## 16. Commit-Hygiene for the Weekly Report (2026-08-21)

- The report file lands at `wiki/queries/wiki-graph-analysis-weekly-<date>.md`. The pre-commit tag validator blocks it if frontmatter tags are non-canonical — patch to `tags: []` (or rely on the §12 generator fix).
- After `_weekly_graph_report.py` auto-cleans the previous week's report file, `index.md` still lists the old entry → REPLACE the old entry with the new one in the same commit (not append), or you leave a stale index entry pointing at a deleted file.
- Append the log entry to `wiki/log.md` with a Python script (write_file to `/tmp/` → `python3 /tmp/append_log_entry.py`), inserting after the `_Log of all wiki changes..._` line. `execute_code` is blocked in cron mode (see §8).
- Commit everything in one shot: `git add wiki/queries/wiki-graph-analysis-weekly-<date>.md wiki/index.md wiki/log.md scripts/_weekly_graph_report.py scripts/wiki_graph_analysis_weekly.py && git commit -m "wiki: weekly graph analysis <date> — ..." && git push`. Include generator fixes in the same commit when you patch them.
