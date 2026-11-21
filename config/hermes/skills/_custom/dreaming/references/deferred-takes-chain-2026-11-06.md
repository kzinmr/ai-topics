# Deferred-takes chain across dreaming cycles (2026-11-06 / 11-07)

Referenced from SKILL.md's Pattern-E zero-take paragraph, which previously carried this
body inline: *"triage_latest.json decision field is `recommended_action`, NOT `action` —
JSON is a 1-run window — sweep log.md for prior 'deferred' takes; verify by grepping the
page, not git log."*

## The field name is `recommended_action`

Every decision object in `${HERMES_HOME}/cron/data/dreaming/triage_latest.json` uses
`recommended_action` (`take` | `reference` | `skip`). Reading `d["action"]` returns
`KeyError` / silently `None`, which makes a whole decisions array look like zero takes.
This is the #1 cause of a downstream cycle wrongly concluding "Takes=0" and skipping
enrichment that the upstream actually planned.

Count with the correct key (cron-safe, no pipe-to-interpreter):

```bash
python3 -c "import json; d=json.load(open('/opt/data/.hermes/cron/data/dreaming/triage_latest.json')); a=[x.get('recommended_action') for x in d['decisions']]; print(len(a), a.count('take'), a.count('reference'), a.count('skip'))"
```

## The triage JSON is a ONE-RUN window — takes get deferred, not deleted

`triage_latest.json` only ever describes the most recent `dreaming-group` pass. A `take`
that the downstream `dreaming-wiki-ingest` did not execute (iteration cap, render failure,
a verification gate downgrading it, or a sibling job winning the race) does **not** persist
as a take in the next cycle's JSON — the next group pass re-triages from scratch and often
re-classifies the same article as `skip` because it now looks "already covered" by a page
that a *different* job half-created.

So: **a genuine take can vanish between cycles without ever landing on disk.**

### Recovery: sweep log.md for prior deferred takes

Before finalising that a cycle is Takes=0, grep the log for takes that were announced but
never delivered:

```bash
grep -niE "dreaming.*(take|enrich|candidate)" wiki/log.md | head -30
grep -n "$(date -d yesterday +%F)" wiki/log.md | grep -i dreaming
```

Read each candidate entry's wording:
- `"Reference candidate for enrichment"`, `"NOT yet covered in entity page"`,
  `"N references identified"` (future tense) → triage-only commit, enrichment still owed.
- `"Enriched: [[entities/foo]]"`, `"Pages created"` (past tense) → delivered, skip it.

Confirm with `git show --stat <that-commit>`: if it touched only `log.md` + archive JSON +
`archive_index.json`, no content landed and the work is owed.

## Verify coverage by grepping the PAGE, not the git log

The decisive test for "was this take actually delivered?" is the target page's current
content, not the commit history — a page can appear in a `git show --stat` diff via a
sibling's frontmatter-only touch or an unrelated section append, which makes it look like
your section landed when it did not.

Per owed take, all three must hold before you call it covered:
1. `grep -n "<raw-article-hash-or-title>" <target page>` hits in the **body**, not just `sources:`
2. `updated:` in frontmatter is the delivery date
3. a real `## section` heading for it exists

A `sources:` URL alone is never coverage. This is the same "sources listed ≠ content
captured" trap documented in Pattern E, applied to your own prior run's claims.

## Budget rule that prevents creating new deferred takes

This chain is mostly self-inflicted by hitting the tool-call cap mid-enrichment. Commit
enrichment incrementally (one commit per 2–3 pages) and start the finish sequence
(log prepend → index reconcile → scoped `git add` → commit → push) at ~55% of the
iteration budget. See `references/dreaming-wiki-ingest-2026-11-07-recipes.md` §6.
