# Watchdog session — 2026-11-07 (17:35 UTC)

Commit `72fc6106` pushed. 1 auto-fix applied, everything else verified-clean or report-only.

## Key learnings

### 1. "Not indexed" false positives from the drifted recent-additions block (NEW)
The Concepts section of `index.md` has a **recent-additions block at its very top** (immediately after `## Concepts (N pages)`) where new pages are appended chronologically rather than alphabetically. A filesystem-vs-index diff therefore reports these pages as "not indexed" when they ARE indexed — just not in alphabetical position.

On 2026-11-07: 3 of 5 flagged concepts were this false positive (`ai-agent-bureaucracy`, `ai-cost-of-js-frameworks`, `triggerdev-env-var-exposure-2026-11`, all lines 978-985).

**Procedure**: before inserting any orphan candidate, run a whole-file substring check, not an alphabetical-position check:
```python
c = open('wiki/index.md').read()
if f'[[concepts/{slug}' in c: skip()   # also check [[concepts/{slug}| for display-text form
```
Both `[[slug]]` and `[[slug|Display]]` forms must be matched — the recent block heavily uses display-text syntax.

### 2. `grep -c '# Wiki Log'` is NOT a valid log-header check (CORRECTS the skill)
The unanchored `grep -c '# Wiki Log'` (no `^`) returns **4** on a perfectly healthy log.md — the string appears in body prose inside past repair notes ("restored buried `# Wiki Log` header…"). An `assert content.count('# Wiki Log') == 1` guard in a prepend script will fail spuriously.

**Correct guards**:
```python
assert content.startswith("# Wiki Log\n")        # H1 at line 1
assert content.count("\n# Wiki Log") == 0         # no buried duplicate H1
```
The `\n` prefix excludes body-prose mentions, which are always mid-line.

### 3. `sed -i` with `\n` in the replacement literalizes the newline → SyntaxError
Patching a Python source file with `sed -i "s/.../...\n.../"` writes a REAL newline into the file, breaking string literals. Use `write_file` to author helper scripts instead (the "cron: write_file → python3" rule applies to the helper itself, not just to data).

### 4. Log prepend buries the H1 — again (confirms existing reference)
`new_entry + content` puts the entry above `# Wiki Log`. `scripts/fix_log_header_burial.py` referenced in the skill **does not exist** anywhere under `~/ai-topics/scripts/` or `~/.hermes` (verified 2026-11-07). Inlined a 20-line equivalent: pop the H1 line, drop trailing blanks, reinsert at index 0 with one blank line after. Also had to restore the blank line between the entry's `## [...]` H2 and its first `###` subsection, which the blank-collapsing in the H1 fixer consumed — add a trailing blank to the entry template or re-add it after.

### 5. Header counts vs index entry-lines vs filesystem (three different numbers)
- Index entry-lines: Entities 963, Concepts 2312→2313, Comparisons 35, Events 50, Queries 52
- Filesystem top-level (`-maxdepth 1`, excl. `_index.md`): entities 954, concepts 1712, comparisons 35, events 50, queries 53
- Concepts index count (2313) much larger than flat file count (1712) is **expected**: the index also lists nested subdirectory pages and redirect stubs. Do not "correct" header counts to flat `find` counts.

## Pipeline state (report-only, root cause identified)
`blog-triage`, `blog-wiki-ingest`, `newsletter-wiki-ingest` all `last_status: error`.
**Single shared root cause**: `RuntimeError: Response truncated due to output length limit`. The truncation makes the agent's final response non-parseable JSON, which the downstream pre-run script surfaces as `failed to parse JSON response from <upstream> output` — so a *triage* truncation masquerades as a downstream ingest failure. `newsletter-triage` self-reports `ok` while producing unparseable output (status and parseability are decoupled — do not trust `last_status: ok` as evidence of parseable handoff).
Not watchdog-fixable: needs output-budget reduction (smaller batch, terse response template, or checkpoint-file handoff instead of response-embedded JSON) in the triage jobs themselves.

`x_accounts stale(26h)` = false positive, `30 22 */2 * *` every-2-days schedule, last run ok.
