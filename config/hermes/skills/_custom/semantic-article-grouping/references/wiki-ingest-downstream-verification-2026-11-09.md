# Downstream (wiki-ingest) Verification Patterns — validated 2026-11-09

Applies to `newsletter-wiki-ingest` / `blog-wiki-ingest` / `dreaming-wiki-ingest` consuming a
triage JSON. The triage agent evaluates the *article*; it does not reliably know the *wiki tree*.
Everything below is what the ingest step must verify for itself.

## 1. Never trust triage `candidate_wiki_path`

Observed: a `reference` decision targeting `concepts/llm-vendor-lock-in` — **no such page exists**,
and no dedicated lock-in concept page exists anywhere (`find wiki -name "*vendor-lock*"` → 0).
Triage paths for `reference` items are guesses.

Before acting:
```bash
find ~/ai-topics/wiki/concepts -maxdepth 2 -name "{slug}.md"   # a hit is required
grep -rli "vendor lock-in" ~/ai-topics/wiki/concepts/*.md       # find the real adjacent page
```
If absent, do **not** create the page merely because triage named it. Instead:
- attach content to an existing adjacent page (here: `ai-supply-chain-security`,
  `ai-lab-subscription-vs-api-economics`, `harness-engineering`), **and**
- record the gap in `queries/unresolved-newsletter-leads.md` verbatim: "no dedicated page exists;
  natural home would be `concepts/llm-vendor-lock-in` (register tags in SCHEMA.md first)".

Same discipline for every `[[wikilink]]` you add during enrichment — grep before linking. Broken
links added now are invisible until the Friday `wiki_graph.py` run.

## 2. Patching structural sections: replace the heading ONLY

Inserting a new section before `## Related` / `## Sources`: `old_string` = bare heading,
`new_string` = new section + same heading re-emitted. If you pull the first list item into
`old_string` and omit it from `new_string`, you have silently deleted a curated link.

Observed twice in one run:
- `entities/openai.md` — deleted the `OpenAI Agents SDK Blog` Sources bullet (caught, restored).
- `entities/anthropic.md` — deleted `## Related` heading + `[[entities/anthropic]]` backlink
  (caught, restored).

Both were self-inflicted while *inserting*, not while editing content. Recovery:
```bash
cd ~/ai-topics && git diff --stat wiki/
git diff wiki/entities/<page>.md      # look for '-' lines that are not yours
```
⚠️ A delete-then-restore cycle makes `git diff --stat` show **empty** for that file. Empty is not
"safe" — re-grep for the addition you intended to make and confirm it survived.

## 3. Sibling subagent interference (parallel pipeline window)

`patch` warns: `... was modified by sibling subagent '<uuid>' but this agent never read it`.
Treat as a hard stop for that file: `read_file` / `git diff` it, then re-issue the patch.
Sibling jobs also `git commit` mid-run, so an early `git diff --stat` is stale by commit time —
re-check `git status --short -- wiki/` immediately before `git add`.

## 4. `execute_code` is fully blocked in cron mode (including pure stdlib)

Not just `subprocess`: a script that only called `subprocess.run(["sed", ...])` was rejected with
"execute_code runs arbitrary local Python (including subprocess calls...) — cron jobs run without
a user present to approve it." Even `read_file`-equivalent file reads via `subprocess` are gone.

Cron-mode replacement for reading a single long line out of a raw article (raw Substack saves are
often 1–2 lines of 12KB, so `read_file` truncates them mid-sentence):
```bash
sed -n '1p' wiki/raw/articles/<file>.md | cut -c 1-7000
```
Repeat with advancing offsets. This is the reliable way to satisfy the BODY-READING MANDATE on
single-line raw files.

## 5. log.md prepend: no H1, no fixed insert index

`log.md` opens with the **newest `## [` heading**, and the `# Wiki Log` marker sits ~25 lines down
(mid-file artefact, not a header line). So:
- Anchor the insert on `body.find("## [")` — never on a line starting with `# ` (matches the mid-file
  marker and buries the previous entry's heading).
- Snapshot first: `cp wiki/log.md /tmp/log_backup_$(date +%Y%m%d).md`.
- Verify after: `grep -c '^# Wiki Log'` == 1, `grep -n '^# Wiki Log'` still mid-file, and the
  `## [` heading count increased by exactly 1.

## 6. Contested-number handling when a newer number conflicts (AGENTS.md compliant)

A second source reporting the SAME metric with a different number (here: Anthropic amended S-1
"Q3 revenue $16.96B / Q2 $11.56B" vs an existing page's "~$17B Q3 / $67.8B ARR") is **not** a
correction — likely different period/metric (quarterly revenue vs annualised run-rate). Add a dated
subsection, state explicitly that it does not reconcile with the earlier figure and why, keep both.
Never overwrite. Flag with ⚠️ inline so a later reader doesn't "helpfully" dedupe them.

## 7. Pre-commit hook location

The tag validator is at `.githooks/pre-commit-tag-validator.py` (**not** `scripts/`). Running
`python3 scripts/pre-commit-tag-validator.py` fails with ENOENT — that is a wrong path, not a
broken validator. `python3 scripts/validate_index.py` is the correct index check.

## 8. Truncation guard: budget for commit + archive

The enrichment work completed but hit the max-iteration cap before `git commit`/`push` and
`archive_triage.py newsletter --keep-reference`. If the batch needs 9+ page edits, do the archive +
commit **early** (right after the first few takes) rather than treating them as a closing step —
an uncommitted wiki run loses everything to the next job's `git pull --rebase`.
