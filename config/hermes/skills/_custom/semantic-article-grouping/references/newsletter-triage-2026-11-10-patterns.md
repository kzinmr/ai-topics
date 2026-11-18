# Newsletter Triage Patterns — 2026-11-10 (run 20261110T101014Z)

Batch: 5 newsletters (Import AI 480 / Lenny's How I AI / Superintel+ / AI by Aakash / Simon Willison's Newsletter). Result: 5 takes, 3 references, 13 skips. Archive OK, commit 51ed4162.

## 1. Builder-script pitfalls hit (both are TypeError-before-JSON-write, not JSON-parse failures)

### 1a. `item()` helper with required positional `excerpt` breaks skip entries
When the builder uses a `make()`/`item()` helper and fills `body_excerpt` in a **post-pass** from an `EXC` dict (keyed by item_id) — a good pattern for long CJK excerpts — the helper signature must default it:

```python
def item(key, iid, title, url, action, stars, reason, path, excerpt=""):  # "" default REQUIRED
```

If `excerpt` is a required positional and the ~13 skip calls omit it, the script dies with
`TypeError: item() missing 1 required positional argument: 'excerpt'` **before** any JSON is written. Distinct from the documented `stars=None` TypeError — same class: every helper parameter that some decision category legitimately omits needs a default.

### 1b. Embedded ASCII double-quotes inside CJK reason strings (confirmed again)
`grep すると "beep" の記載がゼロ` inside a `"..."` Python string → `SyntaxError: invalid syntax. Perhaps you forgot a comma?` at the string's first line. Fix: replace ASCII quotes with 「」 before running. The `write_file` lint (ast.parse) catches it pre-execution — always read the lint output instead of running the script first.

## 2. Resolution outcome: all-Substack batch = no beehiiv pitfalls
When the batch has exactly ONE beehiiv newsletter (here Superintel+, 20 v2/c/ links) and the rest are Substack, the beehiiv token-expiry/Cloudflare decision tree applies only to that one newsletter. Inbox summary said `importance: low` + subject was pure corporate gossip (CEO affair / spy probe) → batch-skipped all 20 links without resolving ANY of them. Rule of thumb: for a beehiiv newsletter whose subject is clearly non-technical AND the inbox summary marks it low, skip all links at topic level — don't spend a test resolution.

## 3. Curl + `<article>` extraction worked on the first try for all 4 Substack posts
Script pattern (write_file → terminal, cron-safe): parallel dict of posts, `curl -sL -A "Mozilla/5.0..."`, `<article>` tag fallback to `<div class="body">`, strip script/style, extract `<p|h2|h3|li>` with len>40, dedupe external links after stripping `?utm_`/`&utm_`. Yields: Aakash 70 paras, Simonw 163 paras, Import AI 21, Lenny's 18 — all full bodies, no paywall interstitials. Note JSON-LD `meta` came back `{}` for ALL four (consistent with the documented body_html/JSON-LD unreliability caveat) — the `<article>` fallback was the actual content source. Don't waste effort on JSON-LD when the article-tag path is in the same script.

Also: `<title>` came back empty for all four (titles rendered client-side) — use the checkpoint `source_name` (subject) as the title, not the scraped `<title>`.

## 4. Coverage-gap signals that produced takes (grep-verified, worth reusing as probes)
- **Spotify Shunt/Honk (Claude Code token-cost optimization)**: `grep -ril "shunt"` across entities/concepts/events hit only an unrelated word in seangoedecke-com.md → genuine blank. Claude Code enterprise cost case studies are a **recurring uncovered niche** — check `entities/claude-code.md` only carries the Shopify LLM-proxy case.
- **Simon Willison quote/newsletter article**: raw file was already saved by blog-ingest same-day, BUT `grep -i "beep" entities/simon-willison.md` → zero hits. Classic "raw saved ≠ entity captured": blog-ingest saves the raw file, the entity page still needs the take. Always grep the ENTITY for the article's keyword, not just check raw/articles existence.
- **Fable 5.2 / Muse Ember mentions in Simonw newsletter TOC line**: already raw-saved by today's blog-ingest (log.md `## [2026-11-10] ingest | blog-ingest` lists them) and newsletter body had only a one-line TOC mention → cross-pipeline skip. Checkpoint: a topic appearing in the newsletter merely as a "Plus X and Y" TOC line adds nothing over the blog-domain raw.

## 5. Same-newsletter multi-section takes
AI by Aakash post = sponsor block + PM evals + weekly news digest + Shunt deep dive. Produced TWO takes from one message_id (Shunt deep-dive → new concept; METR RSI/GDPx news digest → `concepts/recursive-self-improvement.md` + `entities/metR.md`) plus one reference (personal 8-task PM evals). Pattern: in aggregator-style Substacks, split take decisions per content section, not per post — and dedup on `(item_id, title)` not URL, since all sections share the post URL.

## 6. Inbox summary quality this run
Inbox pre-triage (20261110T101014Z-triage.json) was accurate on all 5 classifications (4 ingest / 1 skip) — no subject-line misestimation this time. Continue using it for priority ordering; body read still required per BODY-READING MANDATE (the Aakash post's real value — Shunt numbers — was not in the inbox summary at all).
