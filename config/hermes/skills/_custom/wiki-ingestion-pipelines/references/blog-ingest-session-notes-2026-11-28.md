# Blog-ingest agent stage — 2026-11-28 session notes (run 20261128T100029Z)

29 scanned / 20 fetched / 14 script-saved + 3 recovered / 2 new entities + 5 pages updated / commit a9a29a7a1.

## New recovery subclass: short "beat" pages fail the min-length guard (NOT unscrapeable)

`simonwillison.net/2026/Nov/27/datasette-mcp/` landed in `unsaved_articles` even though the page is plain static HTML — because it is a Willison **"beat"**: ~10 lines of content (release title + one sentence + tag list) inside a 388-line HTML shell, so readability extraction falls under `persist_blog_articles`' ~100-char threshold. This is a **false-negative, not a JS-shell case**.

Diagnostic that distinguishes the two: `curl -sL <url> | wc -c` plus a read of the HTML. If the HTML is full-size and the article text is visibly present in the markup (for Willison: inside `<div class="beat-content">` / `<span class="beat-commit">` / `<div class="beat-note blogmark-body">`), hand-write the raw. If the body is an empty `<div id="root">`/`__NEXT_DATA__` shell, it's genuinely unscrapeable — leave it (see the 2026-11-25 TruthSocial note).

Hand-written raw must match the sibling's frontmatter exactly (`title`, `url`, `fetched_at`, `source`, `tags: [blog, raw]`) and use a plausible 8-hex suffix; copy the pattern from the same-day `datasette-charts` file. Then patch **both** `cron/data/blog_ingest/latest.json` and the run archive (append to `saved_articles` with `raw_path`, drop from `unsaved_articles`, add to `supplemental.extra_saved`).

The 2026-11-25 recovery recipe (`bi.persist_blog_articles` via plain `python3`, `HERMES_HOME` defaulted, `sys.path.insert(0, "/opt/data/.hermes/scripts")`) worked again unchanged — dwarkesh.com Substack transcript 695 lines, construction-physics 152 lines, both one-shot.

## grep-count skip heuristic is unsafe for Doctorow link-posts

`grep -c -iE "openai|anthropic|claude|gpt|llm"` returned **2** on pluralistic taylor-made, which per the 2026-11-25 note would mean "skip and archive." Wrong call: the post's thesis is entirely about AI adoption and even contains the explicit marker *"In case you have any doubt, yes, this is a post about AI."* Doctorow buries the AI framing under a century of Taylorism history, so brand-name density is low while AI relevance is total.

Fix applied: for pluralistic.net and other essay-style link-posts, check for an explicit "this is a post about AI" / "AI" thesis marker in the first ~40 lines before skipping on a low brand-grep count. Low grep = *investigate*, not skip.

## Tag taxonomy: `open-weights` is not a canonical tag

Pre-commit blocked `wiki/entities/ege-erdil.md` for tag `open-weights`. Canonical alternatives in SCHEMA.md include `ai-economics`, `ai-forecasting`, `ai-risk`, `economics`, `model`. Use `ai-risk`/`ai-forecasting` for forecaster entities. Do not `--no-verify`; swap the tag.

## Single-source new-entity pages: add an explicit confidence note

Created `entities/ege-erdil.md` from ONE podcast episode. Pattern that worked: `confidence: medium` in frontmatter, a blockquote **Confidence note** naming exactly which fields are thinly sourced (bio table, co-author list) vs well sourced (positions section), and "treat X as the well-sourced core". Without this, a later run will read the bio table as verified fact.

## Sibling-write warnings on hot files are expected, not alarming

`patch` flagged that sibling subagents had touched `entities/simon-willison.md`, `entities/dwarkesh-patel.md`, `concepts/ai-rd-acceleration-doubling.md`, `wiki/index.md`. Every time, `git diff --stat` afterward showed a **pure insertion** (e.g. log.md 34 insertions / 0 deletions). The warning fires on "sibling wrote and I didn't read it this session," not on an actual clobber — verify with `git diff --stat` and proceed; do not re-read 1100-line pages reflexively.

## Index placement for person entities

Alphabetical by file slug within the `## Entities` section; find the neighbourhood with `grep -n "entities/<prefix>" index.md` and insert after the closest preceding slug (`daniel-kokotajlo` after `daniel-miessler`, `ege-erdil` after `eli-thegreenplace-net`). Index pre-commit reports total line count on success (`✓ wiki/index.md clean (3581 lines)`) — use it to confirm the commit hook actually ran.

## Skip list (left to blog-triage, one-line reasons in log entry)

construction-physics "The Invention Algorithm" (raw saved, zero LLM content — TRIZ/Kauffman NK/morphological analysis; would only earn a page if tied to agentic discovery à la concepts/frostbite-ai-designed-cpu), dfarq ×3 (computing history), shkspr.mobi CO-alarm review, johndcook ×2 (math), oldnewthing (WinRT), miguelgrinberg (spam bots ≠ agent defense), berthub.eu (Dutch gov IT).
