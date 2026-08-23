# 503-Upstream Recovery: Backlog Probe + Link-Stub Newsletter Triage

Session-specific detail for the dreaming-group `HTTP 503: Local LLM server is busy` failure mode
(validated 2026-08-22, commit `7bf4156f`). The SKILL.md Pattern E + selective-staging sections
carry the one-line rules; this file has the reproducible recipe.

## Trigger

Pre-run script returns:
```json
{"ok": false, "error": "failed to parse JSON response from dreaming-group output",
 "output_path": "/opt/data/.hermes/cron/output/<job-id>/<ts>.md"}
```
AND the dreaming-group (18:00 UTC) failed on JSON render with
`RuntimeError: HTTP 503: Local LLM server is busy; Hermes should fall back to the external provider.`

## Step 0 — Confirm what upstream already committed (avoid re-doing its work)

```bash
cd ~/ai-topics
git log --oneline -5                       # look for a dreaming commit ~18:10
grep "$(date +%F).*dreaming" wiki/log.md | head -3
python3 -c "import json;d=json.load(open('/opt/data/.hermes/cron/data/dreaming/triage_latest.json'));print(len(d.get('decisions',[])),'prior decisions')"
ls -la wiki/raw/archived/triage/dreaming/$(date +%F)*.json 2>/dev/null   # did upstream archive?
```
If upstream committed a Pattern E pass (log entry + archive JSON + enriched page), its items are
done. Do NOT re-enrich them. Note the commit SHA in your report's Duplicate Check section.

## Step 1 — Backlog probe (the key difference vs a normal saturation day)

The 503 means the checkpoint candidate list was truncated/incomplete, so the real untriaged pool
is the **backlog**, not today's sitemap batch. `ls -lt wiki/raw/articles/` only shows same-day
files and misses older untriaged posts. Use the collector:

```bash
cd ~/ai-topics && python3 scripts/raw_backlog_collect.py --count 10 --dry-run --estimate 2>&1 | head -80
```
Output is JSON: `candidate_count` (thousands is normal), `archived_urls_count`, and an `articles`
array sorted by `ai-hint` with `archive_status: not_archived` flags + a `body_excerpt` per file.
Pick the highest-value `not_archived` candidate. Typical winner: a benchmark/comparison post
(scraped days ago, never triaged by any pipeline).

> raw_path in the output may show the container-home prefix
> (`/opt/data/.hermes/home/ai-topics/...`) — that is a symlink to the canonical repo, not a
> different location. Read via the canonical path.

## Step 2 — Verify the candidate is a genuine gap (Pattern A depth check)

```bash
# Does a wiki page cover this specific comparison?
grep -in "<model-a>\|<model-b>\|<benchmark>" wiki/index.md | head
grep -n "<specific-metric>\|<benchmark-name>" <candidate-concept-page>.md
# Cross-pipeline dedup — was it processed today by another job?
grep "$(date +%F)" wiki/log.md | grep -i "<keyword>"
```
If a concept page already has the article's specific numbers → downgrade to skip. If the page
exists but lacks the article's data points → take (enrich existing page, not create new).

## Step 3 — Enrich (patch, never write_file on rich pages)

For each target page: bump frontmatter `updated:`, append the source to `sources:` (include the
`---` closing delimiter in the patch old_string so the basename match is unique to frontmatter —
the basename also appears in the body as `Source: [[raw/articles/<basename>]]`), insert a new
subsection with the article's specific claims/metrics, and add ≥2 `[[wikilinks]]` to existing pages.
Batch-verify every new `[[path]]` target with `test -f "wiki/${path}.md"` before committing.

## Step 4 — Triage the sibling skips + link-stub digests

- **Sibling skips**: same-entity comparison posts you didn't enrich (e.g. the GPT-5.6-Sol side of
  a DeepSWE board) → `recommended_action: skip` with reason "marginal value vs the take already
  enriched".
- **Raw newsletter digests** (`wiki/raw/newsletters/*.md`, `tags: [newsletter, raw]`, body is a
  list of substack redirect URLs with NO article text) → triage at subject-line level only:
  `grep -i "<theme>" wiki/index.md`. If the theme is covered by an existing concept page → skip
  with reason "link-stub digest, no body; subject theme covered by <page>". Never force a take —
  the body is unreachable from the stub.

## Step 5 — Save triage JSON, archive, prepend log, commit

```bash
# triage JSON (source MUST be "dreaming", takes first) -> /opt/data/.hermes/cron/data/dreaming/triage_latest.json
python3 scripts/archive_triage.py dreaming --keep-reference
# prepend log entry via /tmp script (see Pitfall #14 entry-file pattern)
git add <enriched pages> wiki/index.md wiki/log.md \
        wiki/raw/archived/triage/archive_index.json \
        wiki/raw/archived/triage/dreaming/$(date +%F)_*.json
git commit -m 'dreaming: wiki-ingest YYYY-MM-DD second pass — <summary>'
git push
```
**Selective staging is mandatory**: `git status --short` will show 100+ sibling-job files
(`config/hermes/skills/*`, `AGENTS.md`, `jobs.json`, untracked `wiki/raw/newsletters/*`).
Stage ONLY your content files + log + archive. Never `git add wiki/`. Pre-commit hooks pass
cleanly on a scoped stage (validated: index-validator + tag-validation, no `--no-verify`).

## CJK / tag pre-flight (before commit)

```bash
grep -Pn '[\x{3040}-\x{30FF}\x{4E00}-\x{9FFF}\x{FF00}-\x{FFEF}]' <touched pages>   # exit 1 = clean
# tags must all be in wiki/SCHEMA.md taxonomy (pre-commit checks staged files)
```

## Outcome shape (2026-08-22)

1 take (DeepSWE V4-Pro-0813 vs Fable 5 head-to-head → enriched
`concepts/ai-benchmarks/deepswe-benchmark.md` + `entities/together-ai.md`), 4 sibling skips,
7 link-stub newsletter digests skipped, 5 archive candidates newly archived (index → 2,786 URLs).
Commit `7bf4156f`, 6 files, hooks clean.
