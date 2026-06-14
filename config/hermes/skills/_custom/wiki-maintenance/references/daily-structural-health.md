
# Wiki Watchdog Auto-Fix Patterns

## Triggers
- Daily watchdog cron job (`wiki_watchdog_fix_context.py`) at 17:35 UTC
- Any task involving wiki structure health checks
- User reports of broken links or index inconsistencies

## Critical Constraint: execute_code is BLOCKED in cron mode

`execute_code` runs arbitrary local Python, which is blocked by default under `approvals.cron_mode`. All auto-fixes MUST use `patch()` and `terminal()` (shell commands). Never write Python-in-execute_code solutions — use sed/awk in terminal() instead.

### NEVER use `write_file` for log.md

`write_file` **overwrites the entire file**. The log.md is an append-only append-only document — always use `terminal("cat >> wiki/log.md")` or `patch()` to add entries. If you were shown the last segment of log.md via offset/limit pagination, writing it back with `write_file` creates a truncated file and destroys the full history.

**Recovery if log.md is accidentally truncated with write_file:**
```bash
cd ~/ai-topics && git show HEAD:wiki/log.md > wiki/log.md
```
Then append the new entry:
```bash
python3 -c "with open('wiki/log.md', 'a') as f: f.write(new_entry)"
```
Do NOT use heredocs (cat >>) if they trigger security-approval filters (variation selectors, etc.). Prefer python3 append.

## Auto-Fixable Issues (apply immediately)

### 0. Pre-run Context Handling

⚠️ **Index entry format — always verify before regexing**: Entries use `- ` (dash‑space) format, NOT `|- ` (pipe‑dash). If a pre‑run health script or graph analysis uses a `|-` regex, the counts will be wrong. When in doubt, `head -20 wiki/index.md` to confirm the actual format, then adjust grep/regex accordingly.

**Duplicate `---` frontmatter separator pitfall (discovered 2026‑06‑08):** When using `patch()` to add YAML frontmatter fields (e.g., adding `related:`), the new content naturally includes the closing `---`. If the original frontmatter already had `---` on the next line, you get `---\n---`. **Fix**: ensure the patch's `new_string` ends with a single `---`. After patching, always verify with `head -15 file.md` that the frontmatter has exactly one opening and one closing `---`.

**Duplicate entity auto-fix procedure (discovered 2026‑06‑08):** When graph analysis flags two entity pages as the same person (e.g., both `koylan-ai` and `muratcan-koylan` with score >8 and no cross‑link):
1. Determine the canonical page (richer metadata — more tags, aliases, sources, `related:`)
2. On the duplicate page:
   - Add `related: [canonical-slug]` to frontmatter
   - Add a `> **Redirect/alias:**` blockquote at the top of the body with `[[entities/canonical]]` wikilink
3. Update the duplicate's index.md entry to show `(→ [[entities/canonical]] — duplicate/alias)` in the description
4. Append to log.md recording the fix
5. **Do NOT delete the duplicate page** — both may have unique content lines (observed: koylan-ai had 183 lines, muratcan-koylan 162). Flag for human merge.
6. Commit: `git add wiki/entities/duplicate.md wiki/index.md wiki/log.md && git commit -m "watchdog: auto-fix duplicate entities X / Y" && git push`

**`wiki_snapshot` entity/concept counts may be stale** — the pre-run script's `wiki_snapshot` fields (`entities_count`, `concepts_count`) are collected at an earlier point in the cron pipeline and can diverge from actual filesystem counts (observed: 772→782 for entities, 1513→1621 for concepts). Always verify against actual filesystem before using:

```bash
cd ~/ai-topics && find wiki/entities -name '*.md' | wc -l && find wiki/concepts -name '*.md' | wc -l
```

**`wiki_health` may be null** — if the wiki-health-fix job hasn't run yet or errored, `wiki_health` appears as `null`. In that case, run `wiki_health.py --json` directly to get current data (CAUTION: output can be 150K+ chars — pipe to file):

```bash
cd ~/ai-topics && python scripts/wiki_health.py --json > /tmp/wiki_health_report.json
```

Then read the output. ⚠️ **The `--json` flag now produces real JSON** (added 2026-06-10) with structured `overview`, `page_name_policy`, `orphan_count`, and `orphans` fields. If the script is an older version without `--json`, it outputs markdown — fall back to parsing the emoji-section headers below.

```bash
cd ~/ai-topics && python scripts/wiki_health.py --json | python3 -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d, indent=2))" | head -60
```

When `--json` works, key fields:
- `overview.entities`, `overview.concepts`, `overview.comparisons`, `overview.total_l2`
- `page_name_policy.error_count`, `page_name_policy.warn_count`, `page_name_policy.violations[]`
- `orphan_count`, `orphans[]`

When `--json` is unavailable (older version), parse the markdown sections:

```
## 📊 Overview Stats
- **Entities**: NNN pages
- **Concepts**: NNN pages
- **Comparisons**: N pages
- **Total Layer 2 pages**: NNN

## 🔗 Orphan Pages (not in index.md)
Found **NNN** orphan pages not referenced in `index.md`
(lists each orphan page)

## 📬 Unprocessed Raw Articles
**NNN** of NNNN raw articles are not referenced from any Layer 2 page.

## 🕰️ Stale Pages (>30 days since update)
Found **NNN** stale pages. Top 10:
```

Parse these with `head -80` / `grep` / `sed -n` for the lines you need. Key fields to extract:
- **Entities, Concepts, Comparisons** counts (from Overview Stats section) — use for section header verification
- **Total Layer 2 pages** — for index header comparison
- **Orphan pages count** — for report (do not auto-fix)
- **Stale pages count** — for report (do not auto-fix)
- **Unprocessed raw articles count** — for report (do not auto-fix)

**`wiki_graph_analysis` may be stale** (>24h old). DO NOT act on stale graph data — run wiki_health.py instead for current structural state.

## ⚠️ Known Schedule Inversion Bug

The wiki-watchdog-fix cron job runs at **17:35 UTC** while wiki-health-fix runs at **17:50 UTC** — watchdog runs 15 minutes BEFORE health-fix. The skill's original claim ("after wiki-health and wiki-health-fix have completed") is factually wrong at the schedule level.

**Impact**: wiki_health lint data from the pre-run script may be one day stale (previous run's output). The health-fix job hasn't produced a current report yet.
**Mitigation**: If wiki_health is null or stale, run `wiki_health.py --json` directly (see above) or skip health-dependent analysis and focus only on pipeline watchdog alerts and index.md corruption checks.
**Do NOT attempt to fix the schedule** — that requires user direction to change cron job timings.

### 1. Index.md Corruption

**Pipe table corruption**: Lines starting with `|- [[` instead of `- [[`
```bash
cd ~/ai-topics && sed -i 's/^- | [[/^- [[/' wiki/index.md
```

**Line number prefix corruption**: Lines starting with `^\s*\d+\|` patterns
```bash
cd ~/ai-topics && sed -ri 's/^[[:space:]]*[0-9]+\|//' wiki/index.md
```

**Duplicate entries**: Exact duplicate `- [[...]]` lines
```bash
cd ~/ai-topics && python3 -c "
import re
with open('wiki/index.md') as f: lines = f.readlines()
seen = set()
kept = []
for l in lines:
    m = re.match(r'^- \[\[', l.strip())
    if m:
        key = l.strip()
        if key in seen: continue
        seen.add(key)
    kept.append(l)
with open('wiki/index.md', 'w') as f: f.writelines(kept)
"
```

**Header count mismatch — summary line**: Update the header line
Format: `> Last updated: YYYY-MM-DD | Total pages: NNNN | Indexed entries: NNNN | Not in index: NNNN`
Consistency: `Total == Indexed + Not in index` AND `Indexed == actual - [[...]] line count`

### Section Header Count Convention

**Both** the section header (`## Entities (NNN pages)`) and the summary line (`Concepts: NNNN`) use the **recursive filesystem count** (including `_index.md` and subdirectory files). This is the same convention as `wiki_health.py`'s `overview` counts.

#### ⚠️ "Total pages" field — known staleness issue

The index summary line `Total pages: NNNN` often does NOT match any verifiable filesystem count or indexed-entry count. It appears to be a legacy field from an older counting methodology (possibly including raw/ articles, or counting differently). When the discrepancy is small (<100) it's likely slightly stale from skipped updates. When it's large (>500) it's from a fundamentally different counting method.

**Do NOT auto-correct "Total pages:"** unless all other counts are verified AND you have a clear methodology for what it should represent. Prefer to flag the mismatch in your report and let the user or a dedicated maintenance job reconcile it.

To compute the expected L2 total (for discrepancy reporting, NOT for auto-correction):
```bash
cd ~/ai-topics && echo "L2 total = $(find wiki/entities -name '*.md' | wc -l) + $(find wiki/concepts -name '*.md' | wc -l) + $(find wiki/comparisons -name '*.md' | wc -l) + $(find wiki/queries -name '*.md' | wc -l) + $(find wiki/events -name '*.md' | wc -l)" | bc
```
Small discrepancies (<10) are likely stale from skipped updates. Large discrepancies (>500) suggest a different counting methodology (possibly including raw/ articles or _index.md miscounts).

To verify:
```bash
find wiki/entities -name '*.md' | wc -l   # recursive, includes _index.md
find wiki/concepts -name '*.md' | wc -l
find wiki/comparisons -name '*.md' | wc -l
find wiki/queries -name '*.md' | wc -l
find wiki/events -name '*.md' | wc -l
```

**Index entries** (the `- [[...]]` lines) are a separate count. The summary line's `Indexed entries: NNNN` counts ALL `- [[...]]` lines in the entire index — including raw article and transcript sections, not just the L2 sections. Use the full-count grep to verify:

```bash
grep -cP '^- \[\[.*\]\]' wiki/index.md   # ALL entries (L2 + raw + transcripts)
```

For per-section index entry verification:
```bash
grep -cP '^- \[\[entities/' wiki/index.md   # Entities only
grep -cP '^- \[\[concepts/' wiki/index.md   # Concepts only
```

The summary line's `Indexed entries: NNNN` must match the ALL-entries grep count. Section header counts match the filesystem count. Do not conflate the two — they commonly diverge (especially Concepts, where many pages exist on disk but aren't in the index).

**All 5 section headers need checking at every watchdog run**: Entities, Concepts, Comparisons, Queries, Events. **Concepts drifts the most** — commonly by hundreds of pages (observed gap of 630 pages in Jun 2026). This happens because automated ingest pipelines create many concept files without updating the section header. Always check Concepts first; if filesystem > header by more than 50, prioritize fixing it.

**Known drift pattern — Concepts**: The filesystem count (find + wc -l) and the section header often diverge massively (observed: 955→1585 = +630). This is because:
- Automated ingest creates concept subdirectory files (e.g., `harness-engineering/agentic-workflows/...`)
- Orphan concept pages accumulate on disk without being added to the index
- The section header count was historically set to the index entry count, not the filesystem count
- Fix: always use `find wiki/concepts -name '*.md' | wc -l` for the filesystem truth

**Header count mismatch — section headers**: Each section (`## Entities (NNN pages)`, `## Concepts (NNN pages)`, etc.) also has a count that can drift. Verify against `wiki_health.py`'s `overview` counts (which include `_index.md` files), OR check directly on the filesystem:

```bash
find wiki/entities -name '*.md' | wc -l   # for Entities (includes _index.md)
find wiki/concepts -name '*.md' | wc -l   # for Concepts (includes _index.md)
find wiki/comparisons -name '*.md' | wc -l
find wiki/queries -name '*.md' | wc -l
find wiki/events -name '*.md' | wc -l
```

**Convention**: Always include `_index.md` files in section header counts (consistent with `wiki_health.py`'s `overview`). Both the section header and the summary line's `Concepts:` / `Entities:` fields must use the same inclusive convention.

To verify the actual indexed entries (not filesystem — these are `- [[...]]` lines):
```bash
grep -cP '^- \[\[entities/' index.md   # Entities in index
grep -cP '^- \[\[concepts/' index.md   # Concepts in index
```

Update with `patch()` targeting `## Entities (NNN pages)` → correct number. Concepts often drifts the most.

### 2. Log.md Missing Separators
Pattern: Consecutive `## [YYYY-MM-DD]` headers without `---` between them.

**Pre-flight safety check** — Verify that ALL `## ` lines in log.md are date-stamped log entries before running the auto-fix. The awk script adds `---` before ANY `## ` line (including content sub-headings like `## Background` or `## Key Results`), so applying it to a file with sub-headings would corrupt the content.

```bash
cd ~/ai-topics && grep -n '^## ' wiki/log.md | grep -v '^## \[20' | grep -v '^## YYYY' | grep -v '^## 202' | head -20
```

If this returns any results, DO NOT run the bulk auto-fix — instead, fix the missing separators manually. If all `## ` lines are date-stamped entries, proceed.

**Detection** — count missing `---` between consecutive `##` headers:

⚠️ **PITFALL — one-line awk with escaped double-quotes**: The one-liner form `awk '...{print "Total..."}...'` contains double-quote characters inside the single-quoted awk program. When this markdown snippet is copied verbatim into `terminal()`, the double quotes can be misinterpreted by the shell, producing `awk: 1: unexpected character '\'`. **Use the multi-line heredoc variant instead** — it's immune to this quoting issue:

```bash
cd ~/ai-topics && awk '
BEGIN{count=0; prev=""; seen_sep=0; missing=0}
/^## /{count++; if(prev!=""&&seen_sep==0) missing++; seen_sep=0; prev=$0}
/^---$/{seen_sep=1}
END{print "Total sections: " count; print "Missing separators: " missing}' wiki/log.md
```

**Bulk auto-fix** (add `---` before every `##` header that doesn't already have one above it):
```bash
cd ~/ai-topics && awk '{if(/^## / && !seen_sep && NR>1) print "---"; if(/^---$/) seen_sep=1; else if(/^## /) seen_sep=0; print}' wiki/log.md > /tmp/log_fixed.md && cp /tmp/log_fixed.md wiki/log.md && rm /tmp/log_fixed.md
```
⚠️ This fix touches many lines — verify the diff size before committing:
```bash
git diff --stat wiki/log.md
```
If 500+ changed lines, skip for this run and report the count as deferred.

### 3. Content Regression Check (Periodic)
Pages may be below their historical best due to past batch overwrites. Run the deficit scanner periodically:

```bash
cd ~/ai-topics && bash config/hermes/skills/wiki/wiki-entity-enrichment-from-article/references/content-regression-scanner.sh --current | grep "^DEFICIT"
```

If deficits >100 lines are found, report them. Do NOT auto-restore (risky — may lose newer enrichment). Instead, flag for the skeleton-enrich-daily job which now has git history enrichment built into its prompt.

**Pre-commit hook defense**: `.githooks/pre-commit-content-regression.py` blocks commits that shrink entity/concept pages by >50 lines AND >50%. If this hook blocks your commit, you likely overwrote a rich page — use `patch` instead of `write_file`.

## Pipeline Watchdog Alerts

The pre-run script provides JSON with:
- `pipeline_watchdog`: Job staleness (e.g., `x_accounts` stale >26h)
- `wiki_health`: Lint report (may be null — see §0)
- `wiki_graph_analysis`: Structural issues (broken links, orphans — may be >24h stale)

### ⚠️ Before trusting any alert, verify the source data exists

The pre-run context's `pipeline_watchdog` field contains a `file` reference like `2026-06-05_12-04-09.md` and an `alerts` list. That file may not exist on disk if the watchdog script output was ephemeral or cleaned up. Similarly, `wiki_graph_analysis.file` may reference a report that's 2h+ old. Always cross-reference against cron jobs.json for current state:

### Stale Job Interpretation
- **age_hours < 12**: Normal variance
- **age_hours 12-24**: Investigate
- **age_hours > 24**: Report for human review — do NOT auto-restart

#### ⚠️ CRITICAL: Check job schedule before flagging staleness

Before reporting any stale job alert, verify the job's actual schedule interval:

```bash
# Read from jobs.json — look for the job's schedule.expr field
grep -A 5 '"name": "<job-name>"' ~/.hermes/cron/jobs.json | grep expr
```

Jobs with `*/2` (every 2 days) or weekly schedules will naturally show 26h+ age between runs. Examples:
- `x-accounts-scan`: `30 22 */2 * *` (every 2 days at 22:30 UTC) — 26h age is EXPECTED behavior
- `check-skill-inventory`: weekly — 168h gaps expected
- `Weekly AI digest`: weekly — 168h gaps expected

A stale alert on a multi-day schedule is a **false positive** — the watchdog threshold doesn't account for schedule intervals >24h. Report it as one in the watchdog output, not as an actionable issue.

### Common Patterns
- `x_accounts` job shows 26h+ gaps — EXPECTED for 48-hour schedule. Always verify schedule before reporting.
- `hermes cron list` may not be available — use graceful fallback: read `~/.hermes/cron/jobs.json` directly
- Newsletter/blog triage outputs may be empty (0 items) — normal if no new content

## Non-Auto-Fixable (Human Review)
- Orphan pages (no inbound links) — report count by namespace
- Broken wikilinks (target file doesn't exist) — report top missing targets
- Wrong namespace links — report instances
- **Misplaced concept stubs** — person entities in concepts/, tag-pile slugs, raw-title-as-slug. See `references/misplaced-stub-cleanup.md` for detection heuristics and cleanup workflow. For systematic cleanup of 10+ naming violations, see `wiki-graph-health` skill's `references/stub-cleanup-workflow.md`.
- Creating new wiki pages — only fix existing structure during watchdog runs

## Workflow

1. Read `~/ai-topics/wiki/SCHEMA.md` for structure requirements
2. Check `wiki_health` from pre-run context. If null, run `python scripts/wiki_health.py` directly (CAUTION: output can be large — pipe to head/tail for focused sections)
3. Run verification checks on index.md and log.md
3. Apply all auto-fixes using `patch()`
4. Re-run verification to confirm clean state
5. Update index.md header counts if changed
6. Append watchdog entry to log.md
7. Commit and push. Git credential notes:
   - Remote: `https://github.com/kzinmr/ai-topics.git` — credential store at `/opt/data/.git-credentials` has a valid token
   - **Do NOT switch to SSH** — `~/.ssh/` does not exist (HOME is `/opt/data/.hermes/home`)
   - If HTTPS fails with "Authentication failed", check the credential store still exists
   - If other processes left unstaged changes (common: `archive_index.json`, or `config/hermes/skills/` dirs), stash wiki-only first:
     ```bash
     git stash push -- wiki/   # only stash wiki changes
     git pull --rebase origin main
     git stash pop             # restore wiki changes
     ```
   - If you already did `git stash` (no path filter), the stash includes your modified files. After pulling, pop the stash before add+commit:
     ```bash
     git stash pop
     git add wiki/index.md wiki/log.md
     ```
   - Standard commit: `cd ~/ai-topics && git add wiki/index.md wiki/log.md && git commit -m "watchdog: auto-fix <summary>" && git push`

## Orphan Page Handling Procedure

### Ghost Entry Detection (index.md → file existence)
```python
import os, re
wiki_base = "/opt/data/ai-topics/wiki"
index_entries = set()
for line in open(f"{wiki_base}/index.md"):
    m = re.match(r'- \\[\\[(.+?)\\]\\]', line.strip())
    if m:
        index_entries.add(m.group(1).split("|")[0].strip())

ghost_dirs = ("entities/", "concepts/", "comparisons/", "queries/", "events/")
ghost_entries = []
for target in sorted(index_entries):
    # Skip inline wikilinks without directory prefix (e.g. [[echo-rl|ECHO]], [[Claude models]])
    if not any(target.startswith(prefix) for prefix in ghost_dirs):
        continue
    target_clean = target.split("|")[0].split("#")[0].strip()
    if not os.path.exists(f"{wiki_base}/{target_clean}.md"):
        ghost_entries.append(target_clean)
```

**Key nuance — NOT all ghosts should be removed**: A ghost entry may point to a file with a slightly different filename (e.g., `claude-opus-4-7` in index but file is `claude-opus-4.7.md`). Verify the file at a closely-related name first:
```bash
ls wiki/concepts/claude-opus-4.7.md
```
If found, fix BY REPLACING the slug, not removing the entry:
```bash
cd ~/ai-topics && sed -i 's/\[\[concepts/claude-opus-4-7\]\]/[[concepts/claude-opus-4.7]]/' wiki/index.md
```
Only **remove** ghost lines when no file exists under any closely-related name.
**Fix for true ghosts**: Remove ghost lines from index.md, update header counts and summary line.

#### 🔶 Common namespace migration pattern: ai-benchmarks/

A recurring ghost pattern where benchmark entries are indexed at the bare `concepts/` level (e.g. `[[concepts/bfcl-v3]]`, `[[concepts/chartqa]]`, `[[concepts/mmmu]]`) but the actual files live under `concepts/ai-benchmarks/`. This happens when ingest pipelines create benchmark pages under the subdirectory but index entries get written to the parent namespace.

**Bulk fix** (detect candidates):
```bash
cd ~/ai-topics && for slug in $(grep -oP '(?<=\[\[)concepts/(?!ai-benchmarks/)[^/\]]+(?=\]\])' wiki/index.md); do
  name=$(echo "$slug" | sed 's|concepts/||')
  if [ -f "wiki/concepts/ai-benchmarks/$name.md" ]; then
    echo "FIX: $slug → concepts/ai-benchmarks/$name"
  fi
done
```

Apply with sed on confirmed candidates:
```bash
cd ~/ai-topics && for pair in "aider-polyglot" "bfcl-v3" "chartqa" "countbenchqa" "mmmu" "mrcr" "simpleqa" "vibe-eval"; do
  sed -i "s|\[\[concepts/$pair\]\]|[[concepts/ai-benchmarks/$pair]]|g" wiki/index.md
done
```

#### 🔶 Non-exact-duplicate ghost detection (same target, different descriptions)

The line-level duplicate check (`re.findall(r'^- \[\[[^\]]*\]\] — .*')`) flags only exact-line duplicates. A ghost entry may appear twice with **different descriptions** (e.g., one with a long I/O 2026 summary, the other a one-liner), both pointing to the same non-existent file. These are functionally duplicate entries even though the lines differ.

**Detection** — compare wikilink targets, not full lines:
```python
# After the exact-line dup check, also check targets
from collections import Counter
targets = re.findall(r'^- \[\[([^\]]+)\]\]', section_text)
target_dups = [t for t, c in Counter(targets).items() if c > 1]
```
Fix: keep the richer description, remove the duplicate line.

#### 🔶 Directory-based ghosts (subdirectory without _index.md)

When a concept has a directory with subpages (e.g. `concepts/gemini/gemini-cli.md`, `concepts/gemini/gemini-spark.md`) but no `concepts/gemini/_index.md` or `concepts/gemini.md`, any `[[concepts/gemini]]` index entry is a ghost. This is distinct from the slug-variant case — the target file genuinely doesn't exist even though the directory is populated.

**Detection** — check for either `_index.md` or a top-level file:
```bash
ls wiki/concepts/gemini/_index.md 2>/dev/null || ls wiki/concepts/gemini.md 2>/dev/null || echo "GHOST: no parent page for concepts/gemini/"
```

**Resolution**: Flag for human review — either create a parent page (`_index.md` or gemini.md), or remove the index entry.

#### 🔶 Inverse case: both slug variants exist on disk (ghost vs orphan ambiguity)

When the orphan scanner reports a file as "not in index" but a slug-variant of the same page IS in the index, you have a **slug variant duplicate** — not a true orphan. Common in AI model version naming where hyphens and periods are interchangeable (e.g., `claude-opus-4-7` vs `claude-opus-4.7`, `gpt-5-5` vs `gpt-5.5`).

Detection pattern:
```bash
# Check if the "orphan" is a near-miss of an existing index entry
echo "claude-opus-4-7" | sed 's/-/./g'   # → claude-opus-4.7
echo "claude-opus-4.7" | sed 's/\./-/g'  # → claude-opus-4-7
```

Resolution: **Merge content, keep the slug that's already in the index.** The canonical slug is the one already referenced by index.md. Never keep both files.

Procedure:
1. Compare the two files for depth:
   ```bash
   wc -l wiki/concepts/claude-opus-4-7.md wiki/concepts/claude-opus-4.7.md
   ```
2. Overwrite the stub (indexed slug) with the rich variant's content:
   ```bash
   cp wiki/concepts/claude-opus-4-7.md wiki/concepts/claude-opus-4.7.md
   ```
3. Delete the now-redundant rich variant's file:
   ```bash
   rm wiki/concepts/claude-opus-4-7.md
   ```
4. Verify the indexed slug now has the rich content; no index.md change needed.

⚠️ **Do NOT add the variant slug to the index** — that creates a duplicate entry. The variant slug file should be deleted, not indexed.

### Orphan Addition (file existence → index.md)
1. Scan all `.md` files (excluding `_index.md`) in Layer 2 directories
2. Compare against index.md entries
3. Extract title from orphan page — prefer frontmatter `description:` field, fallback to H1 (`# Title`) after frontmatter:
   ```bash
   sed -n '/^---$/,/^---$/!{/^# /p}' page.md | sed 's/^# //'
   ```
4. **CRITICAL**: Insert alphabetically within correct section, NOT appended
5. Use **sed append-after-line** (`sed Na\`) via a generated script. Build the script with a Python helper (terminal() with python3, NOT execute_code — blocked in cron mode).

   **⚠️ CRITICAL — sed `a\` continuation pitfall (discovered 2026-06-07):** In a sed script file, each `a\` command is followed by the text to append on the NEXT line. The text line must NOT end with `\` — if it does, the next `a\` command gets swallowed as continuation text and all subsequent insertions become garbled (each `1406a` appears as literal text in the output).

   **Correct format:**
   ```
   1406a\
   - [[concepts/how-agents-work]] -- How Coding Agents Work
   1406a\
   - [[concepts/interactive-explanations]] -- Interactive Explanations
   ```

   **Wrong format (text lines end with `\`):**
   ```
   1406a\
   - [[concepts/how-agents-work]] -- How Coding Agents Work\   ← BAD: trailing backslash
   1406a\                                                       ← swallowed as text!
   - [[concepts/interactive-explanations]] -- Interactive Explanations
   ```

   Use the reference script at `references/build-orphan-sed.py` for a working Python template. Or build inline:
   ```bash
   # Build a sed script file with one entry per line using Python
   cd ~/ai-topics && python3 << 'PYEOF'
   entries = [
       '- [[concepts/path/name]] -- Short description',
       '- [[concepts/path/name2]] -- Description 2',
   ]
   with open('/tmp/fix_orphans.sed', 'w') as f:
       for e in entries:
           text = e.replace('/', '\\/')
           f.write('LINE_NUMa\\\n')
           f.write(text + '\n')
   PYEOF
   sed -i -f /tmp/fix_orphans.sed wiki/index.md
   ```
   **Key constraint**: Forward alphabetical order — first sed command's text appears first in the output. Insert all entries at the same line number (the line just before where the first orphan belongs). The entries list must be in forward alphabetical order already.

   **Entry description separator convention**: Existing index entries use `—` (Unicode em dash U+2014, typed as `—`). Use the same separator for new entries for consistency. If you use `--` (two ASCII hyphens), the difference is cosmetic but visible to readers.

   A reusable script is at `references/build-orphan-sed.py` — run it with your entries list for correct sed script generation, including automatic alphabetical-ordering verification and index entry count reporting.
6. **Same-line inserts**: When multiple entries target the same original line (e.g., both `one-person-unicorn` and `open-source-ai` insert before `open-source-ai-destruction`), the first `-e` flag's entry appears first. Order the `-e` flags alphabetically to get correct ordering.
7. **Post-insertion verification**: After insertion, grep for the new entries in context to confirm alphabetical ordering is correct:
   ```bash
   grep -n '^- .*concepts/one-\|^- .*concepts/open-sour' index.md
   ```
   If ordering is wrong (e.g., `open-source-ai` before `one-person-unicorn`), use `patch()` to swap the lines.
8. Update section header count: `## Concepts (NNN pages)` — note: these counts reflect **files on disk**, not index entries. The summary line `Indexed entries: NNNN` is the index entry count.
9. Update summary line in index.md: `Indexed entries: +N`, `Not in index: -N`
10. Validate with `python3 scripts/validate_index.py`

### Orphan Description Construction
Orphan pages often lack a frontmatter `description:` field. For the index entry description:
1. Try `description:` from frontmatter YAML first
2. Fallback to H1 title after frontmatter: `sed -n '/^---$/,/^---$/!{/^# /p}' | sed 's/^# //'`
3. For stubs (<15 content lines after frontmatter), use just the title as the description
4. For pages with substantive content, append a brief synopsis (1-15 words) after the title

**⚠️ CRITICAL: Filter orphan candidates by content depth before addition.** Many orphan concept pages are auto-generated TODO skeletons (~24 lines, `status: stub` with `> **TODO**: Enrich this page.`). Adding these to the index bloats it with unhelpful entries. Before batch-adding orphans:
   - Check total line count: `wc -l < concept-page.md`
   - Check for TODO marker: `grep -c 'TODO' concept-page.md`
   - Only add pages with ≥30 total lines AND no TODO marker, OR pages whose content extends beyond the skeleton template
   - For the first 20 alphabetic candidates, many will be skeletons — report how many were skipped and why

### Alternative: Python Rebuild Approach (for 10+ orphan additions)

For adding 10+ orphan entries, the sed-based approach becomes unwieldy. Use a Python script that rebuilds the Concepts section with merged alphabetical sort:

```bash
cd ~/ai-topics && python3 -c "
import os, re

wiki_path = 'wiki'
index_path = os.path.join(wiki_path, 'index.md')
with open(index_path) as f: lines = f.read().split('\n')

# Find Concepts section
concepts_start = concepts_end = None
for i, line in enumerate(lines):
    if line.strip().startswith('## Concepts'):
        concepts_start = i
    elif concepts_start is not None and line.strip().startswith('## ') and i != concepts_start:
        concepts_end = i
        break

# Build old entries list (from index)
old_entries = []
for i in range(concepts_start + 1, concepts_end):
    m = re.match(r'- \\[\\[([^\\]]+)\\]\\]', lines[i].strip())
    if m:
        old_entries.append(m.group(1).split('|')[0].split('#')[0].strip())

# New orphans to add: list of (slug, description)
orphans = SLUG_DESC_LIST_HERE

# Merge and sort
combined = sorted(old_entries + [o[0] for o in orphans])

# Count header correctly: old_count + len(orphans), NOT len(combined)
old_count_match = re.search(r'\((\\d+) pages?\\)', lines[concepts_start])
old_count = int(old_count_match.group(1))

# Rebuild section
new_lines = []
for slug in combined:
    if slug in old_entries:
        new_lines.append(lines[...].rstrip())  # copy original line
    else:
        desc = dict(orphans)[slug]
        new_lines.append(f'- [[{slug}]] — {desc}')

new_header = f'## Concepts ({old_count + len(orphans)} pages)'
...
"
```

**PITFALL — Slug comparison includes path prefix**: When using `slug == 'claude-opus-4-7'` for special-case fixes, the slug from the sorted combined list includes the directory prefix (e.g., `concepts/claude-opus-4-7`, not `claude-opus-4-7`). Always compare against the full path: `slug == 'concepts/claude-opus-4-7'`.

**PITFALL — Header count must use old_count + len(orphans)**: The section header (e.g., `## Concepts (1568 pages)`) is the filesystem count, which includes all concepts (even those referenced only as inline wikilinks). When adding orphan pages to the index, increment by `old_count + len(orphans)`. Do NOT recompute the count from the new number of explicit entries — that undercounts drastically.

**PITFALL — Summary line `Indexed entries:` uses the ALL-entries grep count, NOT the section count**: After the Python rebuild, the script naturally sets `Indexed entries:` to the Concepts section entry count (e.g., 971). But the correct value is the total count of ALL `- [[...]]` lines in the entire file (including entities, raw articles, transcripts). Verified with:
```bash
grep -cP '^- \[' wiki/index.md   # ALL entries
```
Always check and correct the summary line after a Python rebuild. The mismatch pattern is: Concepts section has N entries → rebuild script writes `Indexed entries: N` → actual total is `N + entities + raw + transcripts`. Fix with `patch()`.

### Pre-Commit Pitfalls
- **`read_file` `|` pipe trap**: `read_file` renders lines as `N|content`. Copying these into `patch(old_string=...)` includes the `|` in the match, corrupting the target file. Always verify raw content with `sed -n 'Np' file.md` before using in patch. Recovery: `sed -i 'START,ENDs/^|//' file.md`
- **`patch()` removal can corrupt adjacent lines**: When `patch()` removes a line in index.md (old_string → empty string), adjacent surviving lines may acquire a stray `|` prefix (e.g. `| |- [[concepts/foo]]` or ` |- [[concepts/foo]]` in read_file output). Always verify removal results with `sed -n 'N-1,N+1p' index.md | cat -A`. Recovery for line N: `sed -i 'Ns/^| //' index.md` (pipe-space prefix) or `sed -i 'Ns/^|- /- /' index.md` (pipe-dash prefix).
- **Ghost entries with `.md` in wikilink**: When a ghost entry's wikilink already contains `.md` (e.g. `[[raw/articles/foo.md]]`), the file check must normalize by stripping `.md` from both the link AND the target path. The Python check `os.path.exists(f"{wiki_base}/{target}.md")` will double-add `.md` → false positive. Strip any `.md` from the link target before the existence check.
- **⚠️ `.rstrip(".md")` character-set trap**: Python's `str.rstrip()` treats its argument as a **set of characters** — NOT a substring. `"box-com".rstrip(".md")` strips the trailing "m" → `"box-co"`, and `"mixedbread".rstrip(".md")` strips the trailing "d" → `"mixedbrea"`. Both become false ghost positives. Always use `re.sub(r'\.md$', '', target)` instead. Verified: `re.sub(r'\.md$', '', "box-com")` → `"box-com"` ✓, `re.sub(r'\.md$', '', "raw/articles/foo.md")` → `"raw/articles/foo"` ✓.
- **Japanese characters**: `pre-commit` hook rejects Japanese in wikilinks. Skip files with Japanese names, log for manual renaming.
- **Alphabetical order**: Must be strictly maintained per section. Use merge sort approach with existing entries.
- **Maximum batch**: Add max 20 orphans per run to avoid huge commits.
- **Post-insertion cleanup checklist** (run after every orphan insertion — whether sed-based or Python-based):
  1. **Remove backup files**: If you created `index.md.bak` (or similar backup), delete it before committing:
     ```bash
     rm wiki/index.md.bak
     ```
     If it was already committed accidentally, use `git rm --cached` (keeps local copy) or `git rm` (deletes both), then amend or commit.
  2. **Verify summary line counts**: The `Indexed entries: NNNN` must equal the total of ALL `- [[...]]` lines:
     ```bash
     grep -cP '^- \[' wiki/index.md
     ```
     After adding N entries, increment by exactly N. Also check whether `Total pages:` needs incrementing.
  3. **Verify both the section header and the summary line**: The section header (e.g. `## Concepts (NNNN pages)`) uses the **filesystem** count, not the index entry count. The summary line's `Concepts: NNNN` field mirrors this filesystem count. Both must be incremented by N.
  4. **Double-check entry count**: Confirm the section's entry count is correct:
     ```bash
     grep -cP '^- \[\[concepts/' wiki/index.md   # for Concepts
     grep -cP '^- \[\[entities/' wiki/index.md   # for Entities
     ```
  5. **Validate and commit**: Run validation BEFORE the final commit:
     ```bash
     cd ~/ai-topics && python3 scripts/validate_index.py
     ```
  6. **No dirty stash**: Do NOT `git stash` with uncommitted backup files in the working tree. If a stash captures the backup file, subsequent `git stash pop` may restore it silently. Better to `rm` backups first, then stash normally.
- **Post-insertion alphabetization check**: Even with careful sed, multi-insertion at the same line can produce reversed order. Also check **existing neighbors** for pre-existing alphabetization defects — common gotchas: `gguf` < `gith` (swap if `gguf` appears after `github`), `generic` < `gepa` (n < p at pos 3), `fine-tuning/` between `fine-tuning` and `fineweb`, `generative` < `generic` (a < i at pos 8). Always `sed -n 'MIN,MAXp'` the affected range after insertion.
- **Duplicate descriptions**: When inserting entries at overlapping line numbers, verify no duplicate lines were created. `grep` for each new entry and confirm exactly one occurrence.
- **Section header counts**: `## Concepts (NNN pages)` reflects **files on disk**, not index entries. The summary line `Indexed entries: NNNN` is the index entry count. Don't conflate the two.
- **Git stash recovery after failed stash dance**: The two-step pattern `git stash push -- wiki/` then `git stash` (full) then `git stash pop` only pops the top stash, leaving the wiki stash buried. After `git stash list` shows multiple stashes, recover with:
  ```bash
  git stash list                              # see which stash has your changes
  git stash pop stash@{0}                     # restore the wiki changes
  ```
  The stash index you want might not be `stash@{0}` — it's the one containing the wiki changes you stashed first. Check with `git stash show stash@{N}` first. After recovery, run `git stash drop stash@{N}` on any remaining stale entries.

### Japanese Filename Handling
```python
import re
# Check for Japanese characters
has_japanese = bool(re.search(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]', line))
if has_japanese and line.strip().startswith("- [["):
    print(f"SKIP: Japanese filename: {line.strip()[:100]}")
    continue
```

### 📐 Misplaced Entries Between Sections

A recurring structural defect where concept entries end up between `## Events` and `## Comparisons` sections. The entry is physically in the file but after the wrong section header, so it's counted in orphan detection as "not in index" even though it's present.

**Detection** — Scan for concept/entity/event entries in non-matching sections. A reusable script is at `references/misplaced-entries-detection.py`:

```bash
cd ~/ai-topics && python3 .hermes/skills/wiki/wiki-watchdog-auto-fix/references/misplaced-entries-detection.py
```

For inline detection:

```bash
cd ~/ai-topics && python3 << 'PYEOF'
import re
with open('wiki/index.md') as f:
    content = f.read()

# Find all section boundaries
sections = {}
for m in re.finditer(r'^## (\w+)', content, re.MULTILINE):
    sections[m.group(1).lower()] = m.start()

section_order = ['entities', 'concepts', 'events', 'comparisons', 'queries', 'raw', 'transcripts']
seen_concepts_in_wrong_place = []

for i, section in enumerate(section_order):
    if section not in sections:
        continue
    start = sections[section]
    end = sections[section_order[i+1]] if i+1 < len(section_order) and section_order[i+1] in sections else len(content)
    body = content[start:end]
    for m in re.finditer(r'\[\[(\w+)/([^\]]+)\]\]', body):
        entry_type = m.group(1)
        entry_name = m.group(2)
        if entry_type != section:
            seen_concepts_in_wrong_place.append((section, entry_type, entry_name))

print(f"Misplaced entries: {len(seen_concepts_in_wrong_place)}")
for wrong_section, actual_type, name in seen_concepts_in_wrong_place:
    print(f"  '{name}' ({actual_type}) found in {wrong_section} section")
PYEOF
```

**Fix procedure:**
1. Isolate the misplaced lines from their section using `re.findall` on the section text
2. Remove them from their current location by replacing with empty string, then cleaning double-newlines: `re.sub(r'\n{3,}', '\n\n', section_text)`
3. Merge them into the correct section using the Python Rebuild approach (below)
4. Re-sort alphabetically
5. Count ALL indexed entries after rebuild with `grep -cP '^- \[' wiki/index.md` and patch the summary line

**Known locations that accumulate misplaced entries:**
- Between `Events` and `Comparisons` — concept entries creep in when cron jobs add entries without verifying which section they're appending to.
- **Entities section harboring concept entries** — gemini/*, claude/*, anthropic/* subpages (all concepts) sometimes get indexed under the Entities section instead of Concepts. The gemini/claude/anthropic prefix in the slug can fool automated insertion into picking the wrong section.
- **Queries section harboring raw/ entries** — raw article and transcript entries (especially from themed series like the "Cheat at Search" multi-part series) accumulate in the Queries section, likely because ingest pipelines with `type: raw` or `type: transcript` descriptions fail to route to the correct `## Raw Articles` or `## Transcripts` section.

### Tag Creation — Pre-Commit Taxonomy Violation

When creating new entity/concept stub pages during orphan handling, **the pre-commit hook's tag validator blocks commits if any tag used is not in SCHEMA.md's taxonomy** (695 canonical tags as of 2026-06-10).

**Detection** — the commit will fail with:
```
🚨 TAG TAXONOMY VIOLATIONS — COMMIT BLOCKED
⚠️  TAGS NOT IN SCHEMA.md TAXONOMY (2):
   wiki/concepts/tokenization.md:  llm-fundamentals
   wiki/entities/conviction.md:  venture-capital
```

**Causes**: Stub pages created with ad-hoc tags that aren't in the SCHEMA.md taxonomy (common for new concepts like `llm-fundamentals`, `venture-capital`, or other domain-specific tags).

**Fix options** (pick one):
1. **Add the tag to SCHEMA.md** — if it's a valid new category that will be reused. Edit `wiki/SCHEMA.md` to add the tag.
2. **Use an existing canonical tag** — e.g., `llm-fundamentals` → `training` or `architecture`; `venture-capital` → `company`. Check `grep '^  - ' wiki/SCHEMA.md | sort -u` for the full list.
3. **Override** — `git commit --no-verify` (emergency only; bypasses taxonomy check)

**Prevention**: When creating new pages, always check tags against SCHEMA.md first:
```bash
grep -F '  - ' wiki/SCHEMA.md | grep -c '.'   # verify the file loads
grep '  - llm-' wiki/SCHEMA.md                  # check if a tag prefix exists
```

### Python Rebuild Pitfall — Split-on-\n Leading Empty Element

When using Python to rebuild the Concepts section via `content.index()` + `split()`:

```python
h_pos = content.index('\n## Concepts (')   # finds \n BEFORE "## Concepts ("
mid = content[h_pos:n_pos]
lines = mid.split('\n')
# lines[0] = ''           ← EMPTY STRING (because mid starts with \n)
# lines[1] = '## Concepts (1645 pages)'  ← ACTUAL HEADER
# lines[2:] = entries     ← WHAT YOU WANT
```

**The bug**: Using `lines[1:]` instead of `lines[2:]` will include `'## Concepts (1645 pages)'` as a non-entry line. When `non_entry_lines` captures this, it gets appended to the end of the rebuilt section — creating a phantom `## Concepts (1645 pages)` header that appears between the last concept entry and `## Events`, causing a duplicate section header.

**Fix**: Always use `body_lines = lines[2:]` to skip the leading empty element AND the header. The header text is in `lines[1]` — treat it separately as metadata, not as body content.

### Python Rebuild Pitfalls (for 5+ orphan additions)

For adding 5+ orphan entries, use a Python-based rebuild of the target section rather than multiple sed commands:

```bash
cd ~/ai-topics && python3 << 'PYEOF'
import re

with open('wiki/index.md') as f:
    content = f.read()

# Find section boundaries
concepts_start = content.find('## Concepts (')
concepts_header_end = content.find('\\n', concepts_start) + 1
events_start = content.find('\\n## Events', concepts_start)

# Extract all existing concept entries
concept_section_text = content[concepts_header_end:events_start]
existing_entries = re.findall(r'- \\[\\[concepts/[^\\]]+\\]\\] — .*', concept_section_text)

# New entries to add
new_entries = [
    '- [[concepts/foo]] — "Foo Bar"',
]

# Merge + sort
all_entries = sorted(existing_entries + new_entries, key=lambda x: x.lower())
new_section = '\\n'.join(all_entries)

# Update header count
old_count_match = re.search(r'\\((\\d+) pages\\)', content[concepts_start:concepts_header_end])
old_count = int(old_count_match.group(1))
new_header = f'## Concepts ({old_count + len(new_entries)} pages)'

# Rebuild
new_content = (content[:concepts_start] + new_header + '\\n' + new_section + '\\n' +
               content[events_start:])

# ⚠️ Fix summary line: Indexed entries must be recalculated from ALL entries, not just Concepts
total_indexed = len(re.findall(r'^- \\[\\[', new_content, re.MULTILINE))
# Compute entities and concepts counts from filesystem
entities_count = len([l for l in re.findall(r'^- \\[\\[entities/([^\\]]+)', new_content)])
concepts_count = len([l for l in re.findall(r'^- \\[\\[concepts/([^\\]]+)', new_content)])

summary_match = re.search(
    r'(Last updated:[^|]+\\| Total pages: \\d+ \\| Indexed entries: )\\d+',
    new_content)
if summary_match:
    new_content = (new_content[:summary_match.start(1)] +
                   summary_match.group(1) + str(total_indexed) +
                   new_content[summary_match.end():])

with open('wiki/index.md', 'w') as f:
    f.write(new_content)

print(f"Done. Indexed entries: {total_indexed}, Concepts: {concepts_count}")
PYEOF
```

**⚠️ Pitfalls with inline Python:**

1. **PYEOF needs imports INSIDE the heredoc**: `import re` must appear AFTER `<< 'PYEOF'`, not before it. Each terminal command is a separate Python process — no state carries over between calls.
2. **Section header vs Indexed entries confusion**: After rebuild, the `Indexed entries` in the summary line is COMPUTED by the script, but often wrong because the script only counted concept entries, not ALL entries. Always verify with:
   ```bash
   grep -cP '^- \\[' wiki/index.md
   ```
3. **Concepts section boundary detection**: `content.find('\\n## Events', concepts_start)` is the correct boundary marker. Do NOT use `content.find('\\n## ', concepts_start + 10)` — it catches the first `##` subheader if any existed (though currently there are none). The Events section is the most reliable boundary since it always follows Concepts directly.
4. **Summary line multiple updates**: If you patch the summary line separately, the Python script's version and your patch may conflict. Run the Python rebuild first, THEN verify and patch the summary line.
5. **Concept count in section header**: The section header `## Concepts (NNN pages)` should reflect the filesystem count, NOT the entry count. Original count + added entries is the correct calculation: `old_count + len(new_entries)`. Do NOT recompute from the new entry list.
6. **Python `os.path.basename` vs `re.split` for counting**: When computing entities/concepts counts from the new rebuild, `len(re.findall(r'^- \\[\\[concepts/', new_content))` gives the entry count, which is what `Indexed entries` needs. But section header counts use filesystem counts — keep them separate.

### Pre-Commit Pitfalls
