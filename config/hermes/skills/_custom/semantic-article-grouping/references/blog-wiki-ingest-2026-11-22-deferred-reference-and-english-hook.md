# blog-wiki-ingest — deferred-reference recovery + English-only pre-commit hook (2026-11-22)

Two patterns from the blog-wiki-ingest run on batch `20261122T100039Z`.

## Pattern 1: "deferred reference" — triage archives a reference WITHOUT applying it

**Situation.** A prior triage-reconstruction commit (here `60255f63`) ran the batch as
take 0 / reference 1 / skip 13, ARCHIVED all 14 items to
`wiki/raw/archived/triage/blog/<date>_<run_id>.json`, but its own `reason_ja` explicitly
said it would NOT edit the wiki — it left the single `reference` item parked in the archive
("reference 扱いでアーカイブに留置"). Meanwhile the substantive `take`-equivalent articles
were already consumed by the earlier `blog-wiki-ingest` commit (`5cbae342`).

**Lesson.** A batch can reach a state where every take is applied, every skip is archived,
and the one `reference` is silently never applied to its `candidate_wiki_path`. The
downstream `blog-wiki-ingest` job MUST scan the triage decisions array for `reference` items
and verify each one was actually written to disk — not just that the archive contains it.
The archive existing is NOT evidence the reference was applied to the entity page.

**Verification recipe (per reference item):**
```bash
# candidate_wiki_path = entities/andrew-nesbitt.md, raw hash = 280f8438
find ~/ai-topics/wiki -name "<slug>.md"           # page exists?
grep -c "<raw-hash-or-title>" wiki/entities/<slug>.md   # article content present in BODY?
grep -nE "^updated: <today>" wiki/entities/<slug>.md    # updated date bumped?
```
If the raw hash/title is absent from the body (or `updated:` is stale), the reference was
NEVER applied → this job applies it (enrich, bump `updated:`, add raw to `sources:` + `## References`).
This is the **reference half** of the existing "log.md coverage claim ≠ applied content" and
"duplicate-invocation recovery — verify references, not just takes" lessons: a reference can be
archived-and-declared-done while its entity page has zero article-specific content.

**Recurring-series gap test.** Nesbitt's "This Week in Package Management" digests accumulate
as dated subsections under `entities/andrew-nesbitt.md` (Oct 24 / Oct 30 / Nov 7 / Nov 14 / …).
The newest edition being absent from the section list is the take/reference signal even though
sibling editions are fully covered. Grep the section headings (`grep -nE '^### ' page.md`) to
confirm the specific dated edition is the gap before enriching.

## Pattern 2: pre-commit hook enforces ENGLISH-ONLY wiki content (NOT documented in this skill)

The ai-topics repo has a **third** pre-commit validator beyond the two this skill documents
(`validate_index.py`, `pre-commit-tag-validator.py`): a **Japanese/CJK content gate**. It
BLOCKS a commit that introduces Japanese characters into a "previously clean" non-`raw/` wiki
file. It fired on a `wiki/log.md` entry that embedded a Japanese quote lifted from the triage
`reason_ja`.

```
❌ BLOCKED: Japanese content introduced to previously clean files:
   NEW Japanese introduced to clean file: wiki/log.md
   Wiki language policy: All non-raw/ wiki content must be in English.
   To skip this check: git commit --no-verify
```

**Correct fix — translate, do NOT `--no-verify`.** This is a real policy, not a tag-taxonomy
edge case. Reword the CJK passage into English (e.g. replace a quoted Japanese `reason_ja`
sentence with an English paraphrase) and re-commit. Reserve `--no-verify` for genuine
tag-taxonomy residue only (per existing guidance).

**Operational consequence for this triage/ingest class:** triage `reason_ja` / `summary_ja` /
`body_excerpt` are CJK by design and live in the **checkpoint JSON** under
`~/.hermes/cron/data/<pipeline>/` (not a wiki file) — those are fine. But when you copy a
triage reason into `wiki/log.md` or a wiki page, **strip or translate the Japanese first**.
The downstream `*-wiki-ingest` job that writes log.md must therefore emit English log prose,
even though the upstream triage JSON it consumes is Japanese.

## Misc confirmed-this-run (already-known, re-validated — no action needed)
- Script reported `failed to parse JSON response from blog-triage output` on the cron
  **markdown** output, but the checkpoint `triage_latest.json` was valid → the checkpoint file
  remains the authoritative source (skill's Pipeline Resilience section). Trust the checkpoint.
- `git pull --rebase` blocked by a sibling subagent's unstaged file; plain `git push` after the
  commit succeeded (`46a31d4e..ab25757b`). Sibling-file-write-race → leave it unstaged, push plain.
- Duplicate `updated:` line in entity frontmatter (lines 4 and 7) — de-dup while bumping the date.
