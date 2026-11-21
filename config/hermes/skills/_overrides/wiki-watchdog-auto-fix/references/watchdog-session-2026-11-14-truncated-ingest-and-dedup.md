# Watchdog session 2026-11-14 — index dedup, truncated-ingest orphan recovery, self-buried log header

Three new classes the watchdog handled that neither SKILL.md covered.

## Class 1: "Both standalone" duplicate index lines — redirect-aware scan refinement

A raw duplicate-slug count in index.md returned 29; the 2026-08-19 pre-check ("does the slug have its own .md file?") cleared 28 as redirect stubs. **One residue needed a sharper test**: `concepts/claude/mythos` had a file AND appeared as TWO adjacent standalone entry lines (`^\|?- [[slug]]` with descriptions) — a real duplicate from a double-registration.

Refined scan (implements the 08-19 note's "primary vs inline cross-reference" pre-check mechanically):
```python
import re, os, collections
c = open('wiki/index.md').read()
slugs = re.findall(r'\[\[((?:entities|concepts|comparisons|events|queries)/[^\]|]+)', c)
cnt = collections.Counter(slugs)
suspect = []
for s, n in cnt.items():
    if n < 2: continue
    if not os.path.exists('wiki/' + s + '.md'):
        suspect.append((s, 'no-file')); continue
    occ = [l for l in c.split('\n') if re.search(r'\[\[' + re.escape(s) + r'(\]\]|\|)', l)]
    standalone = [l for l in occ if re.match(r'^\|?- \[\[' + re.escape(s) + r'\]\]', l)]
    if len(standalone) == len(occ) == 2:
        suspect.append((s, 'both-standalone'))  # REAL dupe → merge descriptions into one line
```
`both-standalone` = merge (combine descriptions into one line); `no-file` = investigate namespace error / missing stub; everything else = legit redirect or inline cross-ref. Merging descriptions (not just deleting a line) preserves both facts.

## Class 2: Truncated wiki-ingest runs leave written-but-unindexed pages → watchdog registers them

**Signature**: `last_status: error` with `last_error: "RuntimeError: Response truncated due to output length limit"` on blog-wiki-ingest / newsletter-wiki-ingest (jobs have `max_tokens: 8192`). The agent wrote entity/concept pages + raw articles to disk, then hit the output cap BEFORE updating index.md/log.md → git status shows the pages as `??` untracked.

**Watchdog recovery procedure** (this run recovered 4 pages: perplexity-decider, strands-decider, jepa-planning-methods, smolmaxxing + 5 raw articles):
1. `git status --short wiki/` → untracked pages with today's `created:` dates are candidates.
2. Gate each candidate: frontmatter complete (`head -15`), ≥2 `[[wikilinks]]` (`grep -c '\[\['`), 50+ lines. All pass → register.
3. Tag-gate against SCHEMA (see graph-health A3b parser): this run one page carried one-off non-SCHEMA tag `project` — removed it (canonical `open-source` already present) rather than polluting SCHEMA for a 1x tag.
4. Insert into index.md near alphabetical neighbors; recompute header counts from index lines (Entities/Concepts `^\|? ?- \[\[ns/` counts) and Total; bump `Last updated`.
5. Run `validate_index.py`, log, commit only your files.
- **Do NOT** commit other pipelines' uncommitted wiki edits you find alongside (this run left a sibling's `wiki/SCHEMA.md` + `concepts/unsloth.md` WIP untouched — scope discipline).
- **Escalation for human**: the truncation recurs because `max_tokens: 8192` is too small for batch page-writing; suggest raising it or incremental commits so truncation can't orphan pages.

## Class 3: Your OWN watchdog prepend re-buries the log header — run the check LAST

The heredoc prepend (`python3 - <<'EOF'` with `new_entry + content`) put the watchdog entry above `# Wiki Log` again — same bug class as `log-prepend-rereburial-end-of-run-repair-2026-11-13.md`, this time self-inflicted at the final step. Fix recipe that worked:
```python
header = "# Wiki Log\n\n_Log of all wiki changes. Newest entries at top._\n"
assert c.count("\n# Wiki Log\n") == 1 and c.startswith("## [")
open(p, 'w').write(header + c.replace(header, "", 1))
```
Pitfall: `c.count('# Wiki Log') == 1` FAILS as an assertion because the string appears in historical log-entry *text* (10+ mentions like "header buried at line 8..."). Assert on `"\n# Wiki Log\n"` (line-anchored) and `startswith("## [")` instead. **RULE: after ANY log.md prepend in a session, re-check header-at-line-1 immediately before commit — sibling preps and your own prep both re-bury.**

## Class 4 (NEEDS-HUMAN triage): output-length truncation as a pipeline failure class

Alongside the 2026-11-13 503 class: the 4-job chain now shows TWO distinct error signatures — triage stages = `HTTP 503: Local LLM server is busy` (model/provider null, fallback not engaging), ingest stages = `Response truncated due to output length limit`. Both are NEEDS-HUMAN (config-safety boundary, same rule as 11-13: don't force-rerun, don't auto-set model/provider/max_tokens). Checkpoints unconsumed ⇒ no data loss; but unlike pure 503s, truncation CAN leave half-finished state on disk (see Class 2 — always cross-check `git status --short wiki/` when ingest jobs show truncation errors).

## Verified-clean baseline this run (for future comparison)
index.md 3,484→3,487 lines: 0 pipe/line-number/triple-bracket/space-prefix corruption, validate_index exit 0, header counts exact vs index lines, L2 `|- [` scan 0, no-frontmatter scan 0, tag audit 0, `### 2026-` orphan timestamps 0. The 278 empty-wikilink artifacts are the known multi-line residual class — report, don't auto-fix.
