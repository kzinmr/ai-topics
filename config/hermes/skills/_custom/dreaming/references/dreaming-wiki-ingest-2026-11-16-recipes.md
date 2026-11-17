# Dreaming wiki-ingest — 2026-11-16 recipes & pitfalls

Session: dreaming-group render-failed (output 5,387 lines), downstream recovered the 4
reference candidates from the output file's `## Response` section, ran the Deep Sleep
gate, enriched 2 pages / skipped 2, archived 8 new URLs, commit `2ff8a645` clean through
all hooks. Saturation day (total_articles 0 / recent_raw_articles 253).

## 1. Deep Sleep gate — the "already-covered / no-second-source" skip verdicts that recur

Two reference candidates correctly downgraded to skip, each representing a CLASS the
triage engine cannot see:

- **Paywalled HN-reconstruction stub with no second source** (Gödel notebooks / Guardian).
  The raw file is a stub whose entire body is HN-thread quotes + a "paywalled; article body
  not fetched" line. All the article's facts (person, grant amount, shorthand name, theorem
  count, HN item id + points) are ALREADY verbatim in the raw. Adding them to a concept page
  that is scoped to a DIFFERENT sub-topic (the math page covers Astra's 10 results, not
  Gödel's shorthand) would be net-new synthesis on a single paywalled source with no
  corroboration → **skip, do not force a take**. The raw IS the durable record.
  Discriminator: does the candidate page actually cover the article's SPECIFIC sub-topic?
  If the existing same-domain page is scoped elsewhere, and the raw is a stub with no second
  source, the honest verdict is skip-with-note, not "create new" or "force a reference".

- **Sitemap re-scrape of an article a prior cycle already enriched** (Hex "robots to rewrite
  Hex", scraped Nov 13, content Nov 12). The entity page already had a full 7-rule playbook
  section citing the SAME raw basename. The upstream grouping stage re-surfaced it as a fresh
  reference candidate because its checkpoint window re-included the file. Detection that
  caught it: `grep -n "<article heading keyword>" entities/<page>.md` returns a dated section
  that quotes the same content — that's a false positive, not a gap. The "sources listed ≠
  content captured" check cuts BOTH ways: here sources AND content were present, so it's a
  skip, full stop.

## 2. Scrape-date ≠ content-date — flag stale sitemap articles in the note itself

A raw file's `created:`/scraped date (and even its `lastmod:`) can be the SITEMAP-CRAWL date,
while the article's real publication date is much older — printed in the body chrome
("Aug 28, 2025" body date, scraped 2026-11-16, lastmod faked to 2026-11-15). If you write the
enrichment as if it were a same-day development, the wiki page lies about recency.

Rule: when adding a sitemap-scraped reference, grep the body for the human-readable pub date
(the line under the headline, e.g. `Aug 28, 2025` / `November 12, 2026`). If it diverges from
the scrape date by more than a few days, **state the content date inline in the added section
and tag the note "late ingestion, not a new development"**. Cheap probe:
`grep -nE "(January|February|March|April|May|June|July|August|September|October|November|December) [0-9]{1,2}, 20[0-9]{2}" raw/articles/<file>`
and compare against the frontmatter `lastmod:`. This also explains why an "obviously old"
product post (a 2025 MCP-server writeup) suddenly appears in a Nov 2026 sitemap batch.

## 3. Hand-rolled log prepend on a CLEAN header can still emit a stray blank line / visual duplicate header

Even with exactly one `# Wiki Log` in the file, a prepend script that inserts
`"\n" + entry + "\n\n"` after the italic anchor leaves a BLANK LINE at L1, and the head then
reads `blank / # Wiki Log / blank / (entry near header)` — `grep -c '^# Wiki Log'` still == 1
so the cheap integrity probe passes, but the top is malformed.

Cheapest correct fix when there is genuinely ONE header (6-line script, lighter than the full
`repair_log_md_header.py`):
```python
log = open(p).read(); lines = log.split("\n")
while lines and lines[0].strip()=="": lines.pop(0)        # kill leading blanks
if lines and lines[0].strip()=="# Wiki Log":              # drop an immediately-following dup
    j=1
    while j<len(lines) and lines[j].strip()=="": j+=1
    if j<len(lines) and lines[j].strip()=="# Wiki Log": del lines[j]
open(p,"w").write("\n".join(lines))
```
Better default: run `config/hermes/skills/_custom/dreaming/scripts/repair_log_md_header.py` as
the FIRST log action every cycle (handles single / buried / duplicate header uniformly). Always
check `grep -n "^# Wiki Log"` for the LINE NUMBER, not just the count.

## 4. Enrichment authoring hygiene that kept the commit one-shot clean

- **Wikilink sweep before running the batch script**: every `[[target]]` in new sections gets
  `os.path.exists(f"wiki/{t}.md")`. This run `[[concepts/agent-memory]]` was a MISS — real page
  is `concepts/lifelong-agent-memory.md`. Fix the guess to a real page, never mint a stub to
  satisfy a Related bullet.
- **`grep -c 'sources:'` false-positive**: asserting `s.count('sources:')==1` on an entity page
  FAILS on a healthy file because prose can contain `... sources:` (e.g. "Harvey Knowledge
  sources: internal ..."). Don't treat that as duplicate frontmatter — `grep -n "sources:"` and
  eyeball: only a line at column 0 (`sources:`) is the YAML key. Assert on `^sources:` with re.M.
- **Recovery-path consistency**: when the upstream render failed and `triage_latest.json` is
  stale/consumed (confirmed via a same-or-later log.md dreaming entry), rebuild the triage JSON
  from the output file's `## Response` and re-save to the canonical path with `source:
  "dreaming"` before running `archive_triage.py dreaming --keep-reference` — the archive script
  reads `recommended_action` + `url` from that file, so the recovered decisions must live there,
  not only in your head.

## Triage reason overclaims data the article lacks (validated 2026-11-17)

Dreaming-group reason_ja claimed Harvey "2027 budget data" — the raw body (12.6KB, ~110 lines of nav chrome) contained NO proprietary numbers, only a generic framework. The Deep Sleep gate caught it by reading the FULL body. Correct action: enrich the framework, downgrade the section framing ("methodology", not "data"), note the downgrade in the log. Do NOT skip the reference (vendor framework is durable knowledge); do NOT manufacture claimed numbers.

## Sitemap-scrape title/body mismatch (validated 2026-11-17)

postnord raw had H1 "How Yahoo Scout became conversational..." + stray Yahoo-VP quote, but the body is entirely the PostNord case study (per URL slug + named quotes). Trust URL slug + substance of named quotes over scraped H1 when they conflict.

## Archive-only upstream commit + full triage JSON = downstream enriches (2026-11-17)

Upstream committed ONLY archive JSON + index (no pages, no log entry); triage_latest.json carries the real refs. Downstream archive re-run returns archived:0 "All items already archived (dedup)" — expected. Selective staging when sibling tree is dirty.
