# Dreaming wiki-ingest — 2026-11-07 downstream session recipes

Run: `dreaming-wiki-ingest`. Upstream `dreaming-group` render-failed
(`failed to parse JSON response from dreaming-group output`,
`output_path: /opt/data/.hermes/cron/output/c4a9e8d2f671/2026-11-07_18-20-46.md`).
Recovered from `triage_latest.json` + the upstream commit
`4441f35a dreaming: group triage 2026-11-07 — Takes=3 (carried) refs=9 skips=4, archive 8 new (Pattern E scan)`.
Delivered: `entities/harvey.md` (Fact Graph + FORUM Chicago), `entities/factory.md`
(× HumanLayer acquisition), index.md summaries, SCHEMA tags `ghostty` / `data-center-politics`.

## 1. Index.md: anchor on the WIKILINK, never on a summary string

The planned `step4_index.py` tried to match an **old summary string inside the line** to
replace it. All five entities (`warp-terminal`, `mitchell-hashimoto`, `factory`, `hebbia`,
`decagon`) printed `ENT-NOTFOUND` — the summaries had been rewritten by earlier jobs
(active-crawl, watchdog auto-fix, trending-topics) so the memorised text was gone.
`concepts/agent-experience` also already had both an index entry and a real page
(created 2026-07-09, Modal/Bubna AX framing + Pinecone API principles), so the planned
insert + Concepts count bump were both no-ops.

**Working pattern** (what `step4b_index.py` did — all 5 landed):

```python
for slug, add in apps.items():            # slug = '[[entities/foo]]'
    lines = s.split('\n'); hit = False
    for i, l in enumerate(lines):
        if l.startswith('- ' + slug):      # anchor on the WIKILINK ONLY
            if add.strip() not in l:       # idempotency guard
                lines[i] = l.rstrip() + add
            hit = True; break
    if not hit: print("MISS", slug)
    s = '\n'.join(lines)
```

- **Anchor on the `- [[entities/foo]]` prefix.** Index summaries are the most-contended
  text in the file — five sibling jobs rewrite them daily.
- **Append** (`l.rstrip() + add`), don't replace — replacement destroys a sibling's addition.
- **Idempotency guard** `if add.strip() not in l` makes a compaction-resume a no-op.
- Reconcile headers against real counts afterwards
  (`len(re.findall(r'^- \[\[concepts/', s, re.M))`) and only commit a header fix on a real
  mismatch — never blindly bump by +N. (2026-11-07: Concepts 2313 / Entities 963, both
  already at parity → zero header edits needed.)

## 2. Depth-check BEFORE drafting a section — the cheapest saturation gate

The batch planned new sections for Warp (software-factory thesis, agent-native shell) and
AX. Both were already present: `entities/warp-terminal.md` lines 170–253 carried
"factory engineers, not product engineers", self-improving code review, computer-use
verification, Warp Agent CLI. Two full section drafts were wasted on a saturated page —
the Pattern-A depth check applied *before* writing instead of after.

Before drafting any section, one grep over the target page for the article's most
distinctive tokens (`"8.65"`, `"stdin"`, `"Digital Twins"`, `"bottleneck is you"`). If 2+
hit, it's covered. Also `grep -n "^## " <page> | tail -8`: if the newest heading predates
the article's date, that IS a gap; if a same-week heading exists, it isn't.

Genuine gaps this run did find (correctly): Simon Willison's entity page had no source
newer than Oct 28, so the Nov 3–4 cluster (datasette-agent 0.5a0 `panel`, datasette-apps,
llm 0.37.1) was a real take.

## 3. NEVER use `[[#Exact Heading]]` in-page anchors between newly added sections

Dual-enrichment splits (one article spanning two sections of the same page — Harvey Fact
Graph ↔ FORUM Chicago keynote) tempt you into
`[[#Harvey Fact Graph — one evolving fact record for disputes and investigations (Nov 5, 2026)]]`.
Two failure modes hit in one session:

- The anchor text never byte-matches the real heading (em-dash vs hyphen, a stray "the",
  the trailing parenthetical) → the link is silently dead.
- **Neither pre-commit hook catches a broken wikilink** — only tag validation, index
  validation, and the CJK language check run. The weekly graph-analysis job inherits the debt.

"Fixing" it by making the anchor match the heading exactly is still not verifiable with
`[ -f ]`, and the report-quality wikilink checker mangles it.

**Use prose instead**: "(recorded in the section immediately above)", "see the Fact Graph
section below". Reserve `[[#...]]` for links to *pre-existing* headings you verified with
`grep -n '^## '` in the same session. Pre-commit sweep on your own additions:
`grep -n '\[\[#' <file>` → convert each to prose unless grep-verified.

## 4. Frontmatter `sources:` — only add raw basenames you `ls`-confirmed

A source entry for `raw/articles/2026-11-06_harvey_forum-chicago-recap.md` was written
before checking; only `..._product-announcements.md` exists. The rehash pass silently
`skip`ped it and the dangling reference stayed in the entity page.

Confirm exact basenames with `ls wiki/raw/articles/ | grep <keyword>`, and make the
two-pass sha256 rehash (`parts = s.split('---\n', 2)`, hash `parts[2].strip('\n')`)
**assert** each hashed file exists — an assertion failure is the signal that a source path
was invented.

## 5. Tolerant heading parse in the batch-insert helper

`re.match(r'\s*##\s+(.*)', new_text)` returned `None` →
`AttributeError: 'NoneType' object has no attribute 'group'`, because the staged section
file didn't begin with `## ` after a `.rstrip()` ate the separator. Make it tolerant:

```python
m = re.search(r'^##\s+(.*)', new_text, re.M)   # search + MULTILINE, not match
title = m.group(1).strip() if m else new_text[:40].strip()
```

## 6. Tool-call budget: stop starting new enrichments at ~55% of iterations

This run hit the max-iteration cap mid-work. Left behind: upstream triage + archive + log
committed (`4441f35a`); `harvey.md` (+37), `factory.md` (+20), `index.md` (5 summaries),
`SCHEMA.md` (2 minted tags) **uncommitted and unpushed**; `/tmp/sec_mitchellh.md` and
`/tmp/sec_simon.md` drafted but never applied.

Discipline:
- At ~55% of iterations, stop triaging/enriching and run the **finish sequence**: log
  prepend → index/log reconcile → scoped `git add` → commit → push. Remaining candidates
  go to `/tmp/sec_*.md` drafts for the next cycle.
- Commit **incrementally** — one commit per 2–3 pages — so a capped session leaves committed
  progress instead of a dirty tree.
- The final report MUST name what is uncommitted and list the `/tmp/sec_*.md` drafts the
  next run should apply. An honest "not pushed" beats an implied success.

## 7. Recovery path re-confirmed (archive-only upstream commit)

Upstream render failure + `output_path` present → read
`/opt/data/.hermes/cron/data/dreaming/triage_latest.json` directly. Check
`git log --oneline --since="24 hours ago"` for a sibling `dreaming: group triage ...`
commit. If `git show --stat` touches only `log.md` + archive JSON + `archive_index.json`,
upstream committed the archive but **not** enrichment → downstream must still enrich.
Archive-only commit `4441f35a` confirmed this: downstream enriched Harvey + Factory.
Wording discriminator: upstream log "N references identified" / "NOT yet covered" =
archive-only; "Enriched: [[entities/foo]]" = already done.
