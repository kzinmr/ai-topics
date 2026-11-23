# Trending-topics clean run — 2026-11-23 (weekday noon)

Stats: ~24 tool calls, 3 commits (13 files + 2 reconciliation files), **both pre-commit hooks green on the FIRST try** (zero hook round-trips), 11/11 primary sources fetched, 10/10 HN comment trees mined.

## Result summary

Created `concepts/pandex-european-law-api.md`, `concepts/worker755-llm-subagent-game.md`, `events/2026-11-22-pequalnp-agent-fleet.md`; appended to `concepts/ai-energy.md`, `concepts/ai-consciousness-debate.md`, `concepts/glm-5-3.md`; 3 raw files with HN-quote appendices; SCHEMA minted `lean` (Models) + `legal-tech` (Meta). Commits: `b205dc854` main, `ff61c7ab3` + `2ff8027ae` reconciliations.

## New lesson 1 — fully-client-rendered vendor blog returns HTTP 200 with ZERO stripped text (z.ai)

`https://z.ai/blog/glm-5.4` returned **HTTP 200** and the fetcher reported `OK glm54: 0 chars`. Trailing-slash and `/news/` variants 404'd. This is a *third* fetch-failure class, distinct from the two already documented:

| class | symptom | right move |
|---|---|---|
| paywall/gate | 401/403 (openai.com, wsj.com, reuters.com) | mine the Algolia comment tree, label source |
| THIN/chrome | 200 but ~4k chars of nav/SEO boilerplate (apiiro.com) | stop retrying, mine the HN tree |
| **zero-body SPA** | **200 but 0 chars after strip_html (z.ai)** | **no URL variant helps — author the page from the HN thread and put an explicit `Status: needs verification` block in the page listing exactly which claims are unverified** |

The "needs verification" block is the important part: name the things you could NOT confirm (parameter count, benchmark suite, context length, architecture details) and say what to confirm them against. Do not present thread-derived architecture claims as article content. Here the recoverable thread facts were: loop-transformer lineage ("one obvious missing piece for latent-space looped thinking", r/LocalLLaMa), the named failure mode ("marathon thinking" = test-time-compute runaway), the no-benchmarks controversy (four opposing readings), and raised subscription limits → inference-cost positioning.

## New lesson 2 — index reconciliation must sweep ALL FIVE section headers, not just the two you touched

The documented post-final-commit check compares the header count to the line count. This run it caught TWO mismatches, and the second was in a section this run never touched:

```
Entities   header=976 lines=976  OK
Concepts   header=2387 lines=2388  <- my run (+2 inserts, but a sibling raced +1)
Events     header=58  lines=58   OK
Comparisons header=35 lines=35   OK
Queries    header=63  lines=64   <- PRE-EXISTING drift from 2026-11-22
```

The Queries drift came from `8000f2ba6` (2026-11-22 19:09, skeleton-enrich) — a day-old commit that inserted a queries line without bumping its header. Attribute it before fixing so the commit message is honest: `git log -1 --format="%h %ci %s" -- wiki/queries/` → that commit. Two separate tiny header-only commits (one for your own race, one for the inherited drift) is cleaner than one combined commit, because the messages document different causes.

Canonical closing routine (do this instead of checking only what you bumped):
```bash
cd ~/ai-topics && for s in Entities Concepts Events Comparisons Queries; do
  h=$(grep -m1 "^## $s" wiki/index.md | sed 's/.*(\([0-9]*\) pages.*/\1/')
  l=$(grep -c "^- \[\[$(echo $s | tr 'A-Z' 'a-z')/" wiki/index.md)
  echo "$s header=$h lines=$l $([ "$h" = "$l" ] && echo OK || echo MISMATCH)"
done
```

## New lesson 3 — `execute_code` blocked-in-cron strikes on typo-fix batches; sequential `patch` is the route

The post-write JP-typo cleanup tried one `execute_code` call with a fixes list; returned `BLOCKED: execute_code runs arbitrary local Python ... Cron jobs run without a user present to approve`. Re-confirmed (2026-09-12, 2026-10-04, 2026-11-23). Correct route: individual `patch` calls (no shell scanner, no CJK-matching risk when `old_string` is a distinctive corrupted token like `营销` / `再燃让`), then re-run `write_report.py` so the source stays the single truth.

## Re-confirmations (no action needed)

- SCHEMA whole-word pre-validation caught both missing tokens before writing: `lean` (2nd sighting of the proper-noun class — the proof assistant; Meta's `lean-startup` substring-passes a naive grep) and `legal-tech`. Mint → single batch write → commit → both hooks green first try.
- Combined `fetch_sources.py` + `mine_comments.py` in ONE script (11 targets + 10 objectIDs, print-and-continue, `read(3_000_000)`, depth ≤2, cap 14, min-len 90) replaced ~20 individual calls. Chrome UA + gzip sniff (`raw[:2]==b'\x1f\x8b'`) needed for Google-served pages.
- Front-page block was genuinely useful this weekday (unlike the 2026-10-22 "decayed" case) — the AI lead stories (Perplexity 605, Anthropic-power 982, local-AI guide 555) appeared in BOTH front-page and keyword blocks; the points-only `>120` sweep still added 2 stories the keyword terms missed (O'Reilly "What Happened to Silicon Valley?" 692, worker755 329). Run all three; do not conclude from any one.
- Report-language gates inside the writing script: `hangul` 0, `brackets 「」` 46/46, `（）` 53/53, ASCII-quote-inside-「」 0. The Han grep is eyeball-only and produced ~340 legitimate hits, which is expected — the useful signal is the *unfamiliar* simplified/corrupted forms (`软件`-class), so skim rather than assert.
- Sibling coverage was heavy (active-crawl 11:00, blog-wiki-ingest 10:09, newsletter 10:14, hot-post 09:30). 5 of 8 report topics were already covered → marked `✅ 済み` with verified paths; only 3 topics warranted new pages. The `find concepts entities -iname` sweep before each proposal is what prevented duplicate creation.
