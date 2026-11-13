# Trending batch run — 2026-11-13 (weekday-noon clean run)

Verified 2026-11-13. ~30 tool calls, **ONE commit (19 files), both pre-commit hooks green on the first
try, zero hook round-trips**, 8/8 primary fetches OK, 10/10 HN comment trees mined.

## What the run did

3 new concept pages + 5 existing-page appends + 7 raw files + SCHEMA mint + index/log + report.

- New: `concepts/checkpoint-forensics.md`, `concepts/edge0.md`, `concepts/x402.md`
- Appended: `events/nvidia-ceo-transition-2026.md`, `events/anthropic-ipo-roadshow-2026.md`,
  `concepts/agentic-commerce.md`, `concepts/us-china-ai-competition.md`, `concepts/ai-bubble-economics.md`
- Raw: 7 files (unemploymentlabs, edge0, brave, synthanatomy, smolmaxxing, wired-HN-reconstructed, anthropic-ipo HN thread)
- SCHEMA minted: `agentic-payments`, `x402`, `api-monetization` (AI Agents line);
  `export-controls`, `checkpoint-forensics`, `stablecoin`, `on-device-inference` (Meta line)

## Call sequence (the clean skeleton)

1. `git status --short` + `git log --oneline -15` — establish what sibling jobs already landed.
   Today blog-ingest (09a4d8d7) + blog-wiki-ingest (c6436410) had already taken the day's #1 story
   (Jensen Huang resignation, incl. the official nvidianews primary + TechCrunch + Gary Marcus), so the
   run scoped itself to the *same-day increment* (employee petition) instead of duplicating the event.
2. Read the four checkpoints (`blog_ingest/latest.json`, `newsletter/latest.json`, both `triage_latest.json`)
   via one python dump loop printing only the useful keys. All same-day run_ids → trustworthy.
3. `hn_algolia_supplement.py --days 1 --min-points 30 > /tmp/hn/out.txt` then read the file. On a
   weekday noon run the front_page block was still rich (Huang 3639p, M365 960p, Anthropic IPO 953p) —
   the keyword block supplied the two lead topics that the front page missed (checkpoint forensics 307p,
   smolmaxxing 390p, Apple app review 180p).
4. One own points-only sweep script (`search?tags=story&numericFilters=created_at_i%3E{ts},points%3E100`).
5. `mine_comments.py` (10 stories, `read(3_000_000)`, depth ≤2, cap 14, min-len 90) → single
   `/tmp/hn/comments.txt`, grep'd by section for the quotes.
6. `fetch_sources.py` (8 targets, Chrome UA + gzip sniff + strip_html, print-and-continue) → 8/8 OK.
   No 403 class hit at all this run (edge0.ai, unemploymentlabs.com, brave.com, developer.apple.com,
   github.com ×2, synthanatomy.com, libreagi.com all fine). libreagi came back THIN (1031 chars) → skipped.
7. `save_raws.py` — 7 raw files with `sha256: pending` placeholder + in-script two-pass recompute
   (`parts = s.split('---\n', 2); sha256(parts[2])`), each carrying a `## HN discussion highlights
   (item <id>, <pts>pts)` appendix from mine_comments.
8. Staged page bodies via `write_file` to `/tmp/hn/page_*.md` (NOT triple-quoted in the batch script).
9. ONE `batch_update.py`: SCHEMA mint (regex on the category line, dedup against the existing tag set) →
   copy staged pages with existence guard → heading-anchored appends (Related → Related Concepts →
   Sources fallback) with `if heading in t: skip` idempotency → index alphabetical insert inside
   section bounds with `_index` skip → Concepts count bump → log prepend with strip()-based H1 dedupe.
10. Tag whole-word verification over the 3 new pages' frontmatter against SCHEMA (27/27 OK) +
    CJK grep over every touched non-raw wiki file (clean) BEFORE committing.
11. Scoped `git add` (19 named paths, ~30 concurrent skill/raw files from sibling jobs excluded) →
    `git commit -m` → both hooks green → `git push`.
12. Post-commit count reconciliation: BOTH headers matched (`Concepts 2338/2338`, `Entities 969/969`) —
    no reconciliation commit needed this run.

## New/confirmed lessons

### The report (JP, outside wiki/) is where English loanwords and wrong-language CJK leak — no hook guards it

The wiki language hook never fired (all 10 touched non-raw wiki files were clean ASCII), but the JP report
shipped with a batch of contamination that only a manual pass caught, all fixed with `patch`/`sed -i`:

- English loanword dropped mid-JP-sentence: `analogue`, `had never standardized`, `POST-hoc quantization`,
  `machine発話版`, `hobbyist OSS`, `ウィクション` (corrupted `推奨アクション`).
- **Chinese CJK inside JP prose**: `哪个硬件` (which hardware) and `漫沤` (intended 濫費) — same class as the
  documented Korean `호출` leak. Concrete gate: `python3` char-class dump over the finished report
  (`'\u4e00'<=ch<='\u9fff'`) and eyeball for forms that are not valid Japanese, plus the documented
  `grep -P '[\x{AC00}-\x{D7AF}]'` Hangul check.
- Pre-delivery bracket balance: `python3 -c "print(t.count('「'), t.count('」'), t.count('（'), t.count('）'))"`
  — this run balanced 48/48 and 81/81 on the first write, but the check is 2 seconds and catches the
  documented 2026-11-12 mis-closed-`」` class.

Cheapest discipline: author the report, then run ONE fix script with an `assert anchor in t` substitution
list (so silent anchor misses fail loud) before delivering, rather than trusting the first write.

### SCHEMA minting inside the batch script beats a separate patch call (no sibling race this run)

Instead of a `patch` on SCHEMA.md, the batch script regex'd the category line
(`^- \*\*AI Agents\*\*: (.*)$`), deduped the planned tags against that line's own text, and appended only
the missing ones. This means the mint and the page creation are one atomic idempotent script — a re-run after
compaction is a no-op. Still followed the pre-commit rule: whole-word dedup (`(?<![A-Za-z0-9-])tag(?![A-Za-z0-9-])`),
never substring, so `agentic-payments` would not pass on `agentic-payment-*` neighbours and
`export-controls` was correctly found absent even though `china-mofcom-announcement-48-export-controls`
exists as a *page*.

### `grep -cw` verification must run over the *written files' frontmatter*, not the tags you remember planning

The verification loop parsed `^tags: \[(.*?)\]` out of the three new page files and whole-word checked each
against SCHEMA — 27 tags, all OK. This is the step that makes the one-shot green commit possible, and it is
cheap (one heredoc). Do it after the batch script and before `git add`, not at commit time.

### Positive confirmations (no action needed)

- `hn_algolia_supplement.py` needed `timeout 150 … > file` and then `read_file` — no `head` pipe.
- `git commit -m` in cron with no `--no-verify`, hooks green first try (pitfall #20 re-confirmed, 6th time).
- Index alphabetical insert (section-bounds + `_index` skip) landed all three lines correctly placed —
  verified by `grep -n` on the wikilinks, no mis-placement.
- `log.md` prepend with the strip()-based H1 dedupe produced exactly 1 header (log had its H1 present already;
  the `hdr_present` check avoided the double-header).
- Zero sibling index-race this run: the batch script's Concepts bump (2335→2338) matched the post-commit
  `grep -c` exactly, and the Entities header was already parity (969/969) from the 11:00 watchdog commit.
  The documented post-commit two-step still ran — it just had nothing to fix.
