# Trending-topics clean run — 2026-11-25 (weekday noon)

Verified 2026-11-25. ~26 tool calls, **1 commit (29 files), both pre-commit hooks green FIRST try**,
14/20 primary fetches + 20/20 HN comment trees, zero hook round-trips, zero rework.

## What made it one-shot green

1. **Batched whole-word tag pre-check before writing anything.** One terminal call ran
   `grep -cw <tag> SCHEMA.md` over ~60 candidate tags at once across the three relevant category
   lines. Caught 8 misses up front and minted them all before any page write, so the tag hook never
   fired:
   - Meta line: `ai-reputation`, `priority-dispute`, `platform-risk`, `trade-secret`,
     `ai-competition`, `ai-alignment`
   - Domain Concepts line: `agent-loyalty`, `corporate-alignment`
   Note `ai-alignment` was then **dropped** from the agent-loyalty page anyway (the real page is
   `concepts/alignment-relativity` / `concepts/ai-alignment` does not exist) — minting is cheap but
   still check the same-topic sibling's actual frontmatter first.
2. **Coverage sweep per topic**: `find concepts entities -iname "*kw*"` (recursive from wiki root)
   for ~25 keywords in ONE terminal call before proposing pages. Caught that `events/anthropic-ipo-*`,
   `entities/openai-astra` (already had the GPT-6.2 Astra/Sol section), `concepts/shirudo-ebpf-shield-runtime`,
   `concepts/bonsai-27b`, `concepts/agent-collusion-public-infrastructure`, `entities/prism-ml`,
   `entities/yann-lecun` all existed → append, not create.
3. **Staged page bodies via `write_file` → `/tmp/hn2/page_*.md`, batch script only `shutil.copyfile`**
   (documented 2026-10-30 rule). Script stayed pure logic; content never inside triple-quoted literals.
4. **Post-write wikilink `[ -f ]` sweep** over all 19 targets of the 4 new pages. Found 8 ghosts —
   see the class below.

## NEW fetch class: GitHub blob/tree/PDF pages are thin-rendered (not just SPA vendor blogs)

`fetch_sources.py` reported `THIN` (not FAIL) for:
- `github.com/openai/math/blob/main/preprints/<dir>/paper.pdf` → 776 chars
- `github.com/openai/math/tree/main/preprints/<dir>` (×2) → ~2,300 / ~2,655 chars

GitHub renders blob and tree views client-side, so `strip_html` returns only chrome. **A repo ROOT
page still fetches fine** (README survives after ~2,500 chars of nav) — the failure is specific to
`/blob/` and `/tree/` paths. Recovery: save the Algolia comment tree as the raw file with a `note:`
in frontmatter explaining the thin fetch, and cite the preprint URL under `sources:`. Do not burn
calls on URL variants.

**Corollary for batch scripts: `THIN` == not-fetched.** A batch that prints `OK/THIN` and continues
is not a coverage report; count THIN as a miss and fall back to the comment tree.

## Weekday vs weekend query count (re-confirmation with a negative)

`hn_algolia_supplement.py --days 2 --min-points 20` alone (front page 30 + keyword 27 → 24 AI-relevant
after dedup) surfaced **every** lead story: Anthropic IPO break 405p, LeCun 2001p, Harley agent-loyalty
977p, matrix-mult 705p, Bonsai 471p, Ask-HN distillation 321p, protein design 284p, side channel 269p.
The documented extra points-only sweep is a **weekend** requirement; on a hot weekday it is a wasted
call. Rule: run it only if the keyword block looks stale/thin.

## Ghost-wikilink class, extended: "obvious" concept names that are TAGS not PAGES

Four of the eight ghosts came from writing `[[concepts/vendor-lock-in]]`, `[[concepts/platform-risk]]`,
`[[concepts/on-policy-distillation]]`, `[[entities/vllm]]` — each of which **is a SCHEMA tag** (so it
passes the tag pre-check and feels verified) but is **not a page path**. The real pages were
`concepts/context-engineering/context-lock-in`, `concepts/industrial-scale-distillation-attacks-accusation`,
`concepts/post-training/on-policy-distillation`, `concepts/inference/vllm`. Rule: tag-status and
page-existence are independent checks; a token's presence in SCHEMA says nothing about whether a page
of that name exists. Only `[ -f "<target>.md" ]` counts, and when it misses, `find concepts entities
-iname "*kw*"` before retargeting or dropping.

## Navigation tail (idempotent, one script)

`nav_update.py` did index + log after the page batch:
- index sorted insert scoped to section bounds (`## Concepts` → next `## `), skipping `_index` lines;
  re-derived bounds before EACH insert (the 2026-11-12 pitfall).
- header counts recomputed from `grep -c`-equivalent regex, not incremented.
- log prepend with `ln.strip() == '# Wiki Log'` dedupe, insertion after header + italic intro.
Post-commit parity check was a NO-OP (`## Concepts (2397 pages)` == 2397 lines), same as 2026-11-24 —
build the check into the closing routine, expect to do nothing.

## Reconfirmed with no action needed

- `git commit -m` in cron passed both hooks, no `--no-verify`, no editor prompt.
- Scoped `git add` (29 files) excluded ~12 concurrent `config/hermes/skills/**` changes from sibling jobs.
- `openai.com/index/*` is now **urllib-fetchable** (20k–27k chars, Chrome UA + gzip sniff) — no longer
  in the 403 gate class; the 403 class remains `claude.com`-adjacent SPA pages and `reuters`/`wsj`/`bloomberg`
  (401/403) and `reddit` (403).
- `novaramedia.com` → 4,112 chars THIN (low-credibility aggregator, not worth recovery).
- Report pre-delivery gate clean: Hangul 0, `「」` 44/44, `（）` 45/45, Han eyeball list = only real JP
  kanji compounds.
