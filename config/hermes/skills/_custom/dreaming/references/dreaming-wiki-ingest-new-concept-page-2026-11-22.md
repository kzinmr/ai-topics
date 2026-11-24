# Dreaming wiki-ingest — new concept page from a consumed-prior-triage day (VERIFIED 2026-11-22, run 20261122T180040Z)

## Scenario
Upstream dreaming-group completed Pattern E analysis but failed the JSON render (Pitfall #12). Recover the triage from the cron output file's `## Response` → Theme Clusters tail. The prior `triage_latest.json` is from a CONSUMED run — confirm via `grep "dreaming wiki-ingest" wiki/log.md` showing an entry dated AFTER the triage's timestamp. So the day's real take is NOT carried forward; it lives only in the recovered output file.

## The highest-value Pattern-E take is often a research post buried in a marketing batch
Concrete case: an 11-article sitemap batch from a voice-AI company (Cartesia) had been triaged the day before as ONE coarse "blog batch" skip. The substantive research post ("From Tokens to Bytes", a 49KB H-Net scaling-laws paper) was invisible inside that skip. **Discriminator**: when a company batch was batch-skipped, grep the raw dir for large files (`ls -la wiki/raw/articles/ | grep -i <company>`) and open any >20KB one — product marketing posts are small; the rare research post is the big one.

## Enrichment recipe (Takes=1, new concept page)
1. **Read the full raw article** per the BODY-READING MANDATE — use `read_file` with offset pagination for 1000+ line posts. Capture specific metrics verbatim (1.28× / 2.06× / 5.37× / >10× etc.), never paraphrase numbers.
2. **Confirm the gap with two independent probes**, not just entity existence:
   - `find wiki -iname "*<topic>*"` (filename)
   - `grep -ril "<specific-claim keyword>" wiki/concepts wiki/entities` (content)
   Existence of the author's entity page ≠ coverage of the research (cartesia.md was 45 lines, zero H-Net/hierarchical content wiki-wide). Thin page (45 lines) + zero grep hits = genuine take.
3. **Create the concept page**, enrich the thin entity page with a new `## Research: ...` section pointing to it, and fix the entity's pre-existing broken wikilinks while you're in there (`[[concepts/state-space-models]]` ghost → real `[[concepts/ssm-mamba]]`).
4. **Batch-verify every wikilink target** — this is the gate the pre-commit hooks do NOT catch (tag validation and the JP hook both pass on ghost links). One call:
   ```bash
   cd ~/ai-topics/wiki && grep -oE "\[\[[^]|]*" concepts/foo.md entities/bar.md | sed 's/.*\[\[//' | sort -u | while read t; do [ -f "$t.md" ] || [ -f "$t/_index.md" ] && echo "OK $t" || echo "MISS $t"; done
   ```
   Retarget each MISS to the closest real page (find it: `find concepts entities -iname "*kw*"`) or DROP the link. Never mint a stub just to satisfy a Related bullet.
5. **Index insertion**: the Concepts section is only *mostly* alphabetical with a non-alphabetical recent-tail of same-prefix entries. Don't force a re-sort — `grep -n` a stable adjacent `[[concepts/...]]` line, insert after it, bump the `## Concepts (N pages)` header.
6. **Build the triage JSON via a `/tmp/` builder script** (write_file → terminal python3) so `archive_triage.py dreaming --keep-reference` captures the batch skips + refs. Expected on a saturated day: ~19 candidates, ~9 new, ~10 dedup-skipped.

## Two-hook commit sequence on a brand-new concept page (budget for it)
Pre-commit fires hooks in sequence: index validator → tag validation → **JP language hook**. On a fresh concept page, tag validation passes but the **T3 Atomic-Snippets gloss trips the JP hook**:
- The prompt's T3 template says open with `**▶ 一言要約**: ...` — that CJK is EXACTLY what `pre-commit-jp-check.py` blocks on a NEW clean file: `NEW FILE with Japanese content: wiki/concepts/foo.md`.
- Fix: author the summary line in English as `**One-line summary**: ...` from the start. The Japanese stays only in the triage JSON's `reason_ja`/`summary_ja` (cron data, not wiki/).
- Sequence: first commit → tag green, JP hook BLOCKS → patch the gloss to English → re-`git add` → re-commit → both hooks green. Do NOT reflexively `--no-verify`; the JP content is redundant translation, removal is correct.

## Staging on a wide sibling-dirty tree
`git status --short` showed ~16 entries: sibling skill edits (`config/hermes/skills/...`), an unrelated `wiki/queries/modernization-*.md` modification, untracked sibling reference files. Stage ONLY your own artifacts explicitly — concept page, enriched entity, index.md, log.md, the dated archive JSON, archive_index.json — never `git add wiki/`. Commit `6cf315138` (6 files) passed index + tag hooks clean after the JP fix.

## log.md prepend
Header was clean (`grep -c '^# Wiki Log'` == 1 at L1, italic at L3). Ran the canonical `repair_log_md_header.py wiki/log.md /tmp/<entry>.md` anyway (it is idempotent on a clean file). Post-check: blank-line count delta was +1 (healthy) and `git diff --stat` was +11/-1 (a clean insert, NOT over-collapsed). This is the safe default over a hand-rolled prepend.
