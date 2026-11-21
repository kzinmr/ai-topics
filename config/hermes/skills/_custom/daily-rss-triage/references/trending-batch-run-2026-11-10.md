# Trending-topics clean run — 2026-11-10 (weekday noon, ~28 calls, 2 commits, hooks green)

Verified skeleton for a noon trending-topics run where sibling jobs already covered part of the day.

## Call sequence (condensed)

1. **State probe**: `git log --oneline -15` + `git status --short` + `ls -t inbox/rss-scans/ | head` + read `~/.hermes/cron/data/{blog_ingest,newsletter}/latest.json` (check timestamps — stale checkpoint rule already in SKILL.md).
2. **HN scan**: `find ~/ai-topics/config/hermes/skills -name hn_algolia_supplement.py` → cp to /tmp/hn → `timeout 150 python3 hn_algolia_supplement.py --days 2 --min-points 20 > out.txt` → read in two `sed -n` passes. Front_page tag decayed as documented; keyword block carried the lead stories.
3. **Points sweep**: own script — `search?tags=story&numericFilters=created_at_i%3E{yday12:00},points%3E100&hitsPerPage=50` + `search_by_date` keyword pass 2 (prompt injection/MCP/coding agent/... points>50). The points sweep caught Strands Decider, TPU 8tx, H100-pricing that the keyword terms missed.
4. **Coverage grep BEFORE proposing pages**: one batched `find concepts entities -iname "*kw*"` loop over ~20 keywords + `grep -i` on index.md. Result: Fable 5.2 / Muse Ember / Strands / gemini-annotators / CoreWeave-bonds / TPU-8tx all UNINGESTED despite blog-ingest having saved simonwillison raws of them — **raw saved ≠ page covered** (this run's key triage distinction).
5. **Batched evidence**: ONE `fetch_sources_1110.py` (Chrome UA + gzip sniff + strip_html, print-and-continue) got **8/8 primaries OK** — including anthropic.com and research.meta.ai — plus ONE comment-mine loop (15 stories, `read(3_000_000)`, depth ≤2, cap 14, min-len 90) in the same script. Combining fetch+mine into one script = 1 write_file + 1 run instead of 2+2.
6. **SCHEMA pre-validation**: whole-word `grep -cw` loop over ALL planned tags in one terminal call. Caught claude-fable-5-2, claude-mythos-5-2, muse-ember, strands-agents, ai-security as missing → minted in the batch script (Models line + Meta line) BEFORE page creation. Zero hook fires.
7. **Staged content + logic split**: `write_file` each raw/page/report to `/tmp/hn/stage/`, batch script only `shutil.copyfile` + two-pass sha256 + heading-anchored appends + index insert with `assert count==1` anchors + log prepend with `ln.strip()=="# Wiki Log"` dedupe.
8. **Scoped `git add`** (15 named files, excluded ~30 concurrent skill files from other jobs), `git commit -m` — passed both hooks, no `--no-verify`.
9. **Post-final-commit count reconciliation** (see pitfall patch): Concepts header 2323 vs 2327 real lines → tiny follow-up commit.

## New/confirmed lessons

- **Sibling-job race on index counts**: the batch script bumped Concepts 2321→2323 for its own 2 inserts, but newsletter-wiki-ingest had ALSO inserted 4 concept lines into index.md between my initial read and my write; `git show HEAD -- wiki/index.md` revealed 14 insertions not 3. Reconciliation must re-count AFTER the final commit (documented) AND the re-count delta vs your own bump tells you a sibling raced you. Do NOT re-run the whole batch script when you see this — fix only the header.
- **anthropic.com is urllib-fetchable** (Chrome UA + gzip branch): NOT in the documented 403 gate class (openai.com/reuters.com/perplexity/reddit/dbreunig). Don't pre-emptively route Anthropic announcements to the Algolia comment tree — fetch the primary directly.
- **hot-post coverage ≠ wiki coverage**: the 09:30 hot-post covered Goldman Claude Code, but the topic lived only in `inbox/trending-reports/` + a passing mention inside `agent-model-drift.md`. When 2+ same-family anecdotes accumulate across hot-posts/threads (here: 100%-AI-mandate retrospective + brain-fry + Goldman restriction), synthesis into a new concept page is the right move — cross-link to the existing page rather than duplicating.
- **`/opt/data/.hermes/home/ai-topics` resolves to `/opt/data/ai-topics`** — staged-file copies printed "hermes-home" paths that looked like the PATH-TRAP dir but were actually correct. `readlink -f` before chasing a suspected stray file.
- Duplicate-page check refinement: for launch events, `grep -il "fable 5.2" concepts/claude/*.md` across the subdir is the deciding test — the index's giant simon-willison summary line mentioned "Fable 5.2" many times and is NOT page coverage.

## Cost profile

2 write_file scans + 1 points sweep + 1 fetch/mine combined + 1 stage script + 1 batch script + 1 report ≈ 6 authored scripts; 2 terminal commits; total ~28 calls. The combined fetch_sources+mine_comments script and the single whole-word SCHEMA grep loop are the two biggest call-savers vs ad-hoc per-source fetches.
