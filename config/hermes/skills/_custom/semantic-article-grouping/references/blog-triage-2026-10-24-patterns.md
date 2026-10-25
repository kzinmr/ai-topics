# Blog Triage Patterns — 2026-10-24 (run 20261024T100007Z)

14 candidates → 3 takes, 2 references, 5 skip decisions (2 of them batch entries).

## 1. blog-ingest commit ≠ blog-triage consumed (CRITICAL dedup pitfall)

Same-day git commit `wiki: blog-ingest <date> — N raw articles (Kimi K3.1 Pro, RMSNorm, ...)`
landed ~1 minute before this triage ran. That commit means **raw files were saved only**, not
that the batch was triaged. Reading log.md / git log alone suggests a duplicate invocation and
tempts a full-batch skip — wrong conclusion.

The authoritative duplicate signal is **`triage_latest.json`'s own `checkpoint_run_id`** vs the
current checkpoint's `run_id`. On this run `triage_latest.json` carried
`checkpoint_run_id: 20261019T100541Z` (5 days stale) → batch was fresh, triage required.

Checklist before declaring "already processed":
1. `python3 -c "import json;d=json.load(open('<...>/blog_ingest/triage_latest.json'));print(d.get('triage_timestamp'), d.get('checkpoint_run_id'))"` — stale run_id ⇒ proceed normally.
2. log.md `blog-ingest` commit ⇒ raw saving only, no triage information.
3. log.md `blog-triage` / `blog-wiki-ingest` entries for the same run_id ⇒ genuine duplicate.

## 2. Bot-wall interstitial detection (Anubis / Techaro)

`xeiaso.net` candidate came through as a 517 B file whose entire body was the Anubis anti-bot
page ("Making sure you're not a bot!", "This website is running Anubis version v1.28.2-...").
Symptom: raw file size < ~700 B, title is a bot-check string, frontmatter otherwise valid.
Decision: skip, star 1, note in reason_ja that the body is unreachable and the URL slug suggests
the real article may already exist in the backlog. Do NOT retry curl for triage-level value.

## 3. Premium paywall truncation (wheresyoured.at "Premium:" posts)

Truncates at ~6 KB with a "Read the full story / Sign up now" tail. The free portion still
carries quotable numeric claims (here: Blackstone $275B of ~$1.4T AUM in data centers, $2.3B
CoreWeave debt financing, public pensions ≈32% of funding per Bloomberg Intelligence). Rule:
reference (not take), `candidate_wiki_path` = author entity page, capture the free-preview
numbers verbatim, note 「有料部分の本文は取得不可」 in reason_ja.

## 4. Coverage-gap query patterns that produced the takes

- **Model-release version gap**: `grep -ril "K3.1" wiki/{concepts,entities,events}` returned only
  an unrelated benchmark page while `concepts/kimi-k3.md` existed at `updated: 2026-08-24`.
  Family concept page existing ≠ point-release covered. Also check the company entity's line
  count — `entities/moonshot-ai.md` = 16 lines = skeleton needing enrichment alongside the new
  concept page.
- **Author-entity section gap**: `entities/gilesthomas.md` had from-scratch / JAX / parameter
  anatomy / Chinchilla sections but zero on normalization → the RMSNorm experiment article was a
  genuine ★★★★☆ author-entity update. Run `grep -n "^## \|^### " <entity>.md` to enumerate
  sections before deciding "covered".
- **Product-name-absent-from-wiki signal**: `grep -ril "livekit" entities concepts` → zero hits,
  and Modal's own entity documented "GPU snapshots" but not "Sticky Sessions" → official vendor
  integration post = take-as-existing-page-update.

## 5. Duplicate entity pages noticed

`entities/giles-thomas.md` (92 lines) and `entities/gilesthomas.md` (228 lines) coexist for the
same person. When enriching, target the richer page; flag the pair for curator consolidation.

## 6. Script hygiene that worked

Single `write_file` → `/tmp/blog_triage_<date>.py` → `python3 -c "import ast;ast.parse(...)"` gate
→ `python3 /tmp/...py`. The ast.parse gate costs one call and blocks the recurring CJK
SyntaxError class. Helper `make()` + `batch()` functions kept the decisions array compact
(5 entries for 14 candidates) with no duplicate item_ids.

## 7. Out-of-scope categories confirmed as batch-skips

Raymond Chen / Old New Thing COM internals, dfarq Windows anniversary posts, filfre.net
retro-computing serials, Jeff Geerling consumer hardware teardowns, The Verge hardware reviews,
Doctorow non-AI essays (writing craft, general tech policy links). Group into 1-2 batch entries
rather than individual decisions.
