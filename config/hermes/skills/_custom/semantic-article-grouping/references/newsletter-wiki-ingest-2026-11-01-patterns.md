# Newsletter Wiki-Ingest Patterns — 2026-11-01 (run 20261101T101032Z, Takes=0 recovery)

Downstream half of the uid=861 "Two AI Labs Say They Refuted ETH" case. Triage saved a
valid `triage_latest.json` but the cron response failed to render (`failed to parse JSON
response from newsletter-triage output`). Recovered by reading the checkpoint directly
(skill §Pipeline Resilience variant) — 1 newsletter, 3 decisions, 0 takes.

## Pattern A: reference-with-candidate_wiki_path that is a verified no-op → create a durable lead page

The single `reference` pointed at `concepts/openai-eth-refutation-verification-crisis.md`.
Per Post-Recovery Verification, the page body was read (not just `sources:`): it already
carries the OpenAI 67-page preprint, the Impagliazzo/Paturi/Williams shepherd group, the
`oai-math-revised` fork and the Lean caveat, from 3 primary sources, `confidence: medium`.
→ no page change. Correct.

But a no-op reference should not end there when the newsletter's claim is genuinely
*page-changing* if true. Here the subject said **two** labs while the page documents
exactly **one** — a confirmed second independent refutation would flip the story from
"one contested lab claim under shepherding" to "convergent independent claims". Instead of
silently dropping it, created `wiki/queries/unresolved-newsletter-leads.md`: a register of
newsletter-derived claims that triage could not ingest (unreachable body / uncorroborable
claim), each with what-was-seen, what-was-checked, and concrete resolution steps.

**Rule**: when the only non-skip decision of a run resolves to a no-op AND the underlying
claim would change an existing page if corroborated, record it in
`queries/unresolved-newsletter-leads.md` rather than leaving it only in the triage JSON
(rotation-prone) and log.md (grep-hostile). Rows are marked `resolved` with a date, never
deleted, so a later pipeline can find the lead and the negative evidence together.

## Pattern B: run the negative-corroboration sweep yourself, cheaply, before writing

Triage proved only that the *body* was unreachable. Ingest should separately prove the
*claim* is uncorroborated before treating it as speculative. Two cheap calls, cron-safe
(write script to `/tmp/` via `write_file`, run via `terminal`; **never** `curl | python3` —
`tirith:pipe_to_interpreter` blocks it, and an inline `$(python3 -c ...)` inside a URL
also trips the scanner):

- HN Algolia story search, 3 query phrasings (verbatim subject, topic-expansion,
  keyword-pair) → 0 hits here.
- DuckDuckGo HTML (`html.duckduckgo.com/html/?q="verbatim subject"`) with a browser UA →
  no `result__a` links parsed (9KB page = bot-wall, treat as inconclusive, not as absence).

Record the queries and the null results in the lead page. That is what stops a future run
from redoing the same sweep.

## Pattern C: do not trust an `-triage.json` inbox file's acronym guess, and do not trust "no organic results" as proof of absence

The inbox guessed ETH = "Erdős Tree / Happy Ending conjecture"; the wiki context made
Exponential Time Hypothesis the right reading. Note the residual ambiguity in the lead page
rather than adopting either guess as fact — when the body is unreadable, even the *topic*
is unconfirmed, which is itself a reason to refuse ingestion.

## Pattern D: sibling `index.md` write race during the 10:00 UTC pipeline window

`patch` on `wiki/index.md` returned
`_warning: modified by sibling subagent 'ee65d939-...' but this agent never read it`.
`git status` also showed an unrelated sibling-modified page
(`wiki/queries/modernization-inner-loop-reading.md`). Handling that worked:
1. Index was edited by a `/tmp/` script that anchored on **string markers** (`## RSS Scans`,
   `- [[queries/` line prefix), never line numbers — so a concurrent insert cannot corrupt it.
2. Re-`grep` the target lines after writing: this caught that the `Total pages` bump had
   **not** applied (the script's `^Total pages:` regex missed the actual `> Total pages:`
   blockquote form) → fixed with a targeted `patch`. Always verify counts by grep, not by
   the script's own success prints.
3. Commit with **targeted** `git add <my files>` only; leave sibling-modified files
   (`modernization-inner-loop-reading.md`) untouched and uncommitted.
4. `git pull --rebase` failed on the sibling's unstaged changes — but a plain `git push`
   succeeded (fast-forward, no divergence). Try `git push` directly before assuming you
   must stash a sibling's work.

`python3 scripts/validate_index.py` → clean (3387 lines); pre-commit tag validator passed
3 files. No `--no-verify` needed.
