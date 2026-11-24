# Dreaming wiki-ingest — group-stage triage-only clean run (2026-11-21)

Downstream `dreaming-wiki-ingest` run that recovered a triage the upstream dreaming-group
saved before its JSON render failed (`ok:false`, `output_path` present). Validated recipe
for the **archive-only-commit → downstream enriches** variant, with three refinements worth
reusing.

## Triage JSON newer than the upstream commit → enrichment is still pending (decisive test)

Concrete state this session:
- Pre-run script: `{"ok": false, "error": "failed to parse JSON response from dreaming-group output", "output_path": ".../2026-11-21_18-18-13.md"}`.
- `triage_latest.json` mtime **18:16**, 20 decisions (0 takes, 5 refs, 15 skips).
- Upstream commit `79be01b2` at **18:17** — `git show --stat` = exactly 3 files
  (`wiki/log.md`, `archive_index.json`, `triage/dreaming/<date>_<run_id>.json`), NO entity/concept
  page.

That is the **archive-only-commit** variant (see SKILL.md Pitfall #21 "Variant — archive-only
commit"). The decisive discriminator vs "upstream already enriched": `git show --stat <commit>`
touches NO entity/concept page AND the triage has `refs > 0`. When both hold, downstream MUST
run the Deep Sleep verification gate + enrichment. Do NOT conclude "Takes=0 so nothing to do".

(Contrast: if `git show --stat` DOES touch entity pages, or the log entry uses past-tense
"Enriched: [[entities/foo]]", upstream enriched → downstream is a saturation/log-only pass.)

## Wrong-page-pointer recovery: sweep the WHOLE wiki tree, not the triage's guessed path

The triage engine assigns `candidate_wiki_path` from keywords and can name a plausible-but-wrong
page, and can also miss that the coverage lives under a `subdir/`. Two concrete misses this run:

| Reference | Triage guessed | Real coverage location |
|-----------|----------------|------------------------|
| Signal restricting AI agents | `concepts/website-blocking-of-ai-agents.md` | `concepts/security-and-governance/os-agent-capture-privacy.md` — iOS27/Android/macOS countermeasures, two OS-vendor demands, accessibility-permission skeleton key, HN 556 pts. **Already covered → skip.** |
| arXiv:2611.21885 weight self-rewriting | `concepts/language-model-weight-self-rewriting.md` (correct) | Confirmed created TODAY by trending-topics `528cb33d`, cites the arXiv id + raw + 6.6pt/27B/80% figures. **Already covered → skip.** |

Discipline: for EACH reference, don't just open `candidate_wiki_path`. Sweep the whole tree:
```bash
cd ~/ai-topics/wiki && find concepts entities -iname "*<topic-kw>*" -o -iname "*<person-or-org>*"
grep -ril "<topic phrase>" concepts/ entities/      # catches subdir + display-name slugs
```
Then read the candidate page's BODY (not just frontmatter `sources`). A topic that lives in a
`security-and-governance/` subdir, or under a person/organization entity page, or in a sibling
concept created same-day by trending-topics, is "already covered" even though it's not at the
guessed path. Classifying it ✅ with the real path + line refs is the actionable log record.

## Enrichment spans concept page + author-entity page (one article, two targets)

Sean Goedecke "Why output caching doesn't work" is BOTH a durable inference-economics insight
AND a notable author-entity addition; the triage named only `concepts/prompt-caching.md`.
Enriched BOTH:
- `concepts/prompt-caching.md` → `## Output Caching Does Not Work` section carrying the
  load-bearing number: agent output tokens are **~50% reasoning + ~44% tool calls → only ~6% is
  visible repetition**, so Amdahl's law caps output-caching savings at ~4%; real lever is
  intelligence (5×-pricier model, 6×-fewer tokens → cheaper).
- `entities/seangoedecke-com.md` → `### Why Output Caching Doesn't Work (November 2026)`
  subsection under Core Ideas, summarizing the author's take, wikilink back to the concept.
- Added the raw to BOTH frontmatter `sources`.

Rule: when `source_name` is a tracked individual-author blog, always check for an author entity
page and split the enrichment (concept gets the technique + number, entity gets a dated `###`
take + link back). Same principle as the two-company-partner dual-enrichment case, on the
author-vs-concept axis.

## Pitfall #22 archive-clobber RECURRED — recovery is `git checkout HEAD --`

`archive_triage.py dreaming --keep-reference` re-run (downstream after upstream already
committed the archive) SHRANK the dated JSON from 18 decisions to 5 (`-182` lines) and bumped
the `archive_index.json` `updated` timestamp. Same `triage_run_id`, same overwrite failure mode
documented in Pitfall #22 (the "merge" fix validated 2026-08-23 is apparently not in the
deployed `~/.hermes/scripts/` copy, or regressed). Fast recovery, both files:
```bash
git checkout HEAD -- wiki/raw/archived/triage/dreaming/<date>_<run_id>.json \
                      wiki/raw/archived/triage/archive_index.json
```
The URL index stays monotonic (restoring the dated JSON needs no index repair; the
`total_archive_urls` is already correct in HEAD). Detection: `git diff --stat` shows large
deletions on the archive JSON, or its decision count < the first-pass count. **Do NOT** stage
the clobbered archive + timestamp churn — restore first, then stage only your content + log.md.

## Sibling-modified warning mid-patch (handled)

`patch` returned `_warning: modified by sibling subagent '<uuid>' but this agent never read it`
on `entities/seangoedecke-com.md`, `concepts/mcp.md`, `entities/sierra.md` — sibling cron jobs
(busy 18:00–18:35 UTC window) were editing the same pages. Because every patch used a
UNIQUE multi-line anchor, all landed content-correct. Rule (already in semantic-article-grouping
/ wiki-ingest refs): on a sibling warning, RE-GREP the anchor fresh before the next patch and
keep anchors unique; never positional/fuzzy on a contended page.

## Selective staging on a quiet tree (committed clean, both hooks green, no --no-verify)

```bash
git add wiki/concepts/prompt-caching.md wiki/entities/seangoedecke-com.md \
        wiki/concepts/mcp.md wiki/entities/sierra.md wiki/log.md
git commit -m 'dreaming: wiki-ingest ...'   # Tag validation 5 files; language check (0 CJK)
git push   # 79be01b2..c05bb3fa main -> main
```
Staged exactly the 4 enriched content pages + log.md. The restored (no-op) archive files and
`archive_index.json` were intentionally NOT staged (pure timestamp churn discarded by checkout).
Log prepend: wrote entry to `/tmp/dreaming_log_<pipeline>_<date>_<hhmm>.md` + a `/tmp/` insert
script anchoring on the italic line + single `\n`, entry begins with a leading blank line, no
global blank-line collapse. Post-verify: `grep -c '^# Wiki Log'` == 1, entry appears once,
blank-line count changed by ~2.

## Report format used (Takes=0 + refs) — well received

Used the standardized reference-verification table (`| Candidate | Status | Details |`) with
Already covered (real path + what's covered) vs Genuine gap (why + which page), plus a
Consolidation Summary and Updated Pages section with the load-bearing numbers verbatim. This is
the `references/reference-verification-report-format.md` layout — apply it on every
Takes=0-but-refs-exists day.

## SKILL.md size note

`dreaming/SKILL.md` is at the 100,000-char limit (≈100,803 before this reference was added) —
new incremental learnings MUST go into `references/` files, not the SKILL.md body, until it is
split/trimmed. The dual-enrichment "concept page + author-entity page" split and the
"whole-tree sweep before declaring already-covered" rules above are NOT yet inline in SKILL.md
because of that cap; this file is their home.
