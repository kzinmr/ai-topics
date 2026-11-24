# blog-wiki-ingest 2026-11-23 (run 20261123T100944Z) — wikilink verification + false-alarm

## Pre-run `ok:false` false alarm (one more confirmed instance)
Pre-run script reported `{"ok": false, "error": "failed to parse JSON response from blog-triage output"}`.
The checkpoint `triage_latest.json` (10:26 UTC) was valid and matched `latest.json` run_id — a fresh batch, NOT consumed. This is the documented wrapper-parse false alarm (`references/ingest-pre-run-parse-false-alarm.md`): **read `triage_latest.json` FIRST before concluding empty.** Confirmed again. Do not re-triage; proceed straight to ingest.

## Wikilink-target verification before commit (the real lesson)
When you ADD wikilinks to a new page / new section (takes + references), grep-check every target actually exists before committing. Broken links slip past `validate_index.py` (which only checks index.md structure) and the tag validator.

Recipe — extract `[[slug]]` targets from each edited page and stat the file:
```bash
for f in events/new-event.md concepts/scaling-laws.md; do
  echo "-- $f --"
  grep -oE "\[\[[a-zA-Z0-9/_.#-]+\]\]" wiki/$f \
    | sed 's/\[\[//;s/\]\]//;s/#.*//;s/|.*//' | sort -u | while read slug; do
      [ -n "$slug" ] && { [ -f "wiki/$slug.md" ] || echo "MISSING: $slug"; }
    done
done
```

**Pitfall 1 — `.md`-suffix false positives.** If you write `[[raw/articles/foo--hash.md]]` (suffix included), the naive checker appends another `.md` → "MISSING" even though the raw file exists. Normalize: `slug="${slug%.md}"` before `[ -f ... ]`. Raw-article links DO exist with the `.md` suffix on disk — only the checker was wrong.

**Pitfall 2 — plausible-but-nonexistent concept slugs.** Common AI-wiki concepts have non-obvious actual slugs; verify, don't assume:
- "the Bitter Lesson" → `concepts/rich-suttons-bitter-lesson` (NOT `concepts/bitter-lesson`)
- "evals vs monitoring" → `concepts/evaluation/evals-vs-monitoring-debate` (NOT `concepts/evals-vs-monitoring`)
- "superintelligence" family → `concepts/technological-singularity`
- formal verification → `concepts/formal-verification-llm-agents` (exists)
When a guessed slug is MISSING, `find wiki/concepts -iname "*keyword*"` for the real one. Pre-existing broken links in untouched `See Also` blocks are NOT yours to fix in this commit (context lines in `git diff` lack a `+` prefix — confirm you didn't introduce them).

## Coverage-gap take confirmation (this batch, all genuine)
- Alpöge/Claude Riemann claim: new event page. grep `alpoge|riemann` returned only Anthropic RH *lower-bound* + OpenAI Lean batch + Jacobian pages — none the full-RH proof → greenfield event page OK; cross-link to `entities/anthropic`, `concepts/claude-fable-jacobian-conjecture`, `concepts/openai/formal-math-publication-2026`.
- OpenAI perplexity reveal → `concepts/scaling-laws` had ZERO `perplexity` mentions → genuine section gap (added `perplexity` tag, SCHEMA-legal).
- Hotz "slopcore" → entity lacked orthogonality-thesis rejection + GPT-6.2 take → new subsection under the recurring "the singularity is nearer" series (a multi-essay series: add timeline row + dated subsection).

## Sibling-subagent re-read pattern (re-confirmed)
`patch` returned `_warning: modified by sibling subagent ... never read it` on george-hotz, troy-hunt, simon-willison, seangoedecke, lcamtuf, index.md. Sibling runs add timeline-table rows / note entries. Always re-`grep`/`sed -n` the region immediately before each patch — siblings added a Nov-18 timeline row and Oct/Nov notes I hadn't seen. One patch accidentally duplicated a phrase in an adjacent row; caught it by re-reading the diff.

## archive_triage idempotency
`python3 scripts/archive_triage.py blog --keep-reference` → `{"ok":true,"message":"All items already archived (dedup)","archived":0}` because the triage step already archived the skip+reference subset. Archive file exists at `raw/archived/triage/blog/2026-11-23_20261123T100944Z.json`. Idempotent — safe to re-run.
