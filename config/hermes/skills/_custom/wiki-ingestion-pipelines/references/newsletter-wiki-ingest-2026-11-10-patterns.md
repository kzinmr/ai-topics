# newsletter-wiki-ingest patterns — 2026-11-10 (run_id 20261110T101014Z)

## 1. Script-output parse failure ≠ checkpoint loss
The cron pre-run script reported `{"ok": false, "error": "failed to parse JSON response from newsletter-triage output"}` pointing at `cron/output/<job>/<ts>.md`. The checkpoint `cron/data/newsletter/triage_latest.json` was fully intact and parseable. **Always read `triage_latest.json` first; the output .md wrapper failure is a false alarm in most cases.** Also check `wiki/raw/archived/triage/newsletter/{date}_{run_id}.json` — if it exists, the triage job already ran `archive_triage.py` and you must NOT re-archive.

## 2. Iteration-cap mid-run: commit EARLY on 9+ page batches (again confirmed)
This run executed 10 page writes + SCHEMA + index edits and hit the max-iteration limit **before the log.md entry and git commit/push**, leaving the whole batch uncommitted in the working tree. The next run must replay from `git status --short -- wiki/`. Rule (already in the main skill, re-validated): after the first 3-4 page writes, do a first commit (pages only), then a second commit for index/log. A partially-committed batch is recoverable; an all-uncommitted batch at cap is a hazard (sibling jobs can sweep or clobber it).

## 3. Raw-newsletter filename trap
The triage JSON's `raw_path` fields are **not reliable** for the newsletter digest files. `process_email.py` names raw digests `{DATE}-{safe_slug(subject)}.md` using the **email's date** (Import AI 480 was dated `2026-11-09-...` while the ingest run date was 2026-11-10), and slugifies the subject (truncated to 80 chars, e.g. `...-and-meta-b.md`). Before citing `raw/newsletters/...` in a page's `sources:` frontmatter, verify with:
```bash
ls wiki/raw/newsletters/ | grep "2026-11-09\|2026-11-10" | grep -i "import\|aakash\|lenny"
```
Fix the reference in the page rather than trusting the triage-provided path.

## 4. Substack body fetch without web_extract (curl + `<article>`/`<p>` extraction)
For Substack posts, `subprocess.run(["curl","-sL",url])` + regex `<article>...</article>` + `<p|h2|h3>` extraction with tag-strip worked reliably in cron via write_file→terminal (3 URLs, one pass, ~30s total):
- `open.substack.com/pub/{pub}/p/{slug}` for Aakash → 61 paras / 9.3KB body.
- Custom domain (`www.lennysnewsletter.com/p/{slug}`) when the article tag yields <5 paras → fall back to whole-page `<p>` extraction with filter `len>80 and "font-" not in t and "{" not in t` (kills CSS chrome). Got 4.1KB usable body from the How I AI episode page (episode notes are a standalone article — do NOT auto-skip podcast posts).
- `importai.substack.com/p/{slug}` direct domain → 18 long paras / 15.8KB.
JSON-LD `body_html` was empty in all three cases (known pattern — metadata only).

## 5. Broken-wikilink prevention for enrichments
When adding `[[concepts/...]]` wikilinks inside enrichment sections, verify the target exists BEFORE final commit (`ls` the dir or `find`). This run caught a invented path `concepts/harness-engineering/generator-evaluator-loops` (does not exist) and swapped it for the real `concepts/agentic-engineering/first-run-the-tests`. Pre-commit hooks do NOT validate wikilinks.

## 6. index.md alphabetical insertion via script
Robust pattern used this run: read index lines, find section heading index, insert new `- [[...]]` line before the first `^- (?:\d+\|)?\[\[(slug)\]\]` whose slug sorts after the new key; fallback = after last `- [[` line in section. Then regex-bump `(N pages)` headers and `> Total pages:`. validate_index.py passed first try.

## 7. Contested-framing handling (METR "early RSI phase")
A second source (newsletter commentary) characterized METR's ~2x acceleration assessment as "Claude is in the early phase of RSI" — stronger than METR's own wording. Followed the AGENTS.md "don't erase contradictions" rule: added a dated subsection attributing the stronger framing to commentary, not to METR, keeping the original METR section intact. Good template for any newsletter-vs-primary-source framing gap.

## 8. CJK-quote SyntaxError re-encounter
An index blurb containing ASCII double-quotes inside a Python string (`"giving Claude Code ears"`) produced `SyntaxError: invalid syntax. Perhaps you forgot a comma?` at write_file lint time. Fix as per `cron-builder-script-cjk-pitfalls.md`: strip the inner quotes or use 「」; keep index blurbs quote-free.
