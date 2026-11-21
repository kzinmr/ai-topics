# Trending batch run — 2026-11-20 (weekday noon, ~20 calls, 1 commit 16 files, BOTH hooks green FIRST try)

Clean run. Reusable facts:

- **Fetch results (fetch_sources.py batch, 12 targets)**: 8/12 OK. FAIL class this run:
  - `ounapuu.ee` 404 (post still on HN front page — personal-blog 404s happen; save HN comment tree as `type: hn-discussion` raw, documented class).
  - `simonwillison.net/2026/Nov/20/token-fraud-is-here-and-its-bad/` 404 on guessed URL — the real slug was `.../token-fraud-is-here-and-its-bad/` with the "(YouTube)" link-blog form; ALSO the morning blog-ingest had already saved the exact raw (`simonwillison.net--2026-nov-20-token-fraud...`). Always `ls wiki/raw/articles/ | grep <kw>` BEFORE fetching a willison post — blog-ingest at 10:00 UTC beats the noon run.
  - `businesswire.com` 403 (new gate class: press-release wires) — classify from HN thread + title, cite the misanthropicstatement.com link found in top comment.
  - `git-aarvin.github.io/mei/` and `micjm.com` THIN (1.3k/1.6k chars, JS-rendered) → skip retries, mined the HN trees instead (documented apiiro class, re-confirmed on github.io pages).
- **`anthropic.com/research/*` fetches fine** (29k chars, Chrome UA, no 403) — same class as the documented anthropic.com/news note.
- **HN front_page tag NOT fully decayed on this Monday-noon run**: front-page block carried same-day OpenSSL PG19/FFmpeg but the AI leads (Anthropic Nasdaq 1095p, Gemini Neon, Fuck Your AI Safeguards 563p) came from the keyword block as usual — keyword pass remains primary.
- **Sibling-job coverage**: blog-ingest (10:00) had already captured the Anthropic IPO Techmeme aggregation as a manual-capture raw (`techmeme.com--261118-p34--...--manual01.md`) — reuse it as a source line for the event page instead of re-fetching paywalled Reuters (401 class).
- **Pre-validated tag set all green first commit**: whole-word grepped every tag incl. `chip-design` (turned out already in SCHEMA Models line — my earlier grep of `grep -cw "chip-design" SCHEMA.md` returned 1 and I trusted it; the nav script re-verified with a tokenized parse before minting, which correctly no-op'd). The tokenized-parse-before-mint idiom (`re.search` on the category line + token split) is the safe pattern vs bare grep.
- **Report typo class re-confirmed**: writing the JP report inside a Python dict/string produced one simplified-Chinese leak (`开源` for オープンソース) — the Han-eyeball gate flagged it only because I also ran a post-write `grep -n "开源"` pass. Concrete addition to the gate: grep the FINISHED report for the common leak set `开源|软件|银行|审查|哪个|创作者|廉价` (not just the in-script suspects list), fix with `sed -i`.
- Log prepend: the existing `# Wiki Log` + `_Log of all..._` intro means the entry must be inserted AFTER the intro line, and a blank line between intro and `## [date]` header needs re-adding — build both into the nav script.
