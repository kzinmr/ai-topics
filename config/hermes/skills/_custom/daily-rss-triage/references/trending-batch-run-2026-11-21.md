# Trending batch run — 2026-11-21 (verified)

Weekend (Saturday) 12:00 UTC clean run. ~20 calls, 1 commit (20 files), hooks green after ONE tag fix, 10/12 source fetches OK, 12/12 comment-mine OK.

## Run shape (reusable skeleton)

1. State probe: `date -u`, `ls -t inbox/rss-scans/ | head`, `git log --oneline -15`, read `cron/data/blog_ingest/latest.json` (30 new) + `cron/data/newsletter/latest.json` (2 processed — Anthropic IPO S-1 already ingested at 10:55 by newsletter-wiki-ingest).
2. Copy `hn_algolia_supplement.py` from `_custom/daily-rss-triage/scripts/` to /tmp, run `timeout 150 ... > /tmp/hn/out.txt`, read in two `sed -n` passes. Front_page tag block was FRESH this run (24 stories incl. same-day 2682pt GRH story) — on Saturday noon the front-page scan carried the real signal, unlike the documented weekday decay case. Keyword block added Frostbite (already covered yesterday), Signal, sell-off, Google-union.
3. `find concepts entities events -iname` sweep for every candidate topic BEFORE proposing pages. Discovered: `concepts/inkling.md` + `concepts/inkling-2-small.md` exist (Mini = new release, append to inkling.md), `events/anthropic-nasdaq-debut-2026.md` exists (created yesterday), `concepts/signal.md` is a 23-line STUB (append a real section), no self-rewrite / OS-agent-capture pages.
4. Batched `fetch_sources.py` (Chrome UA + gzip sniff): 10/12 OK; FAILs = researchgate 403 (hungry-butler, classified from HN only) and ounapuu.ee 404 (fuck-your-ai-safeguards — skip or classify from thread).
5. Batched `mine_comments.py` (12 stories, read(3_000_000), depth<=2, cap 14, min-len 90): 12/12.
6. Two staged new pages via write_file (NOT triple-quoted in batch script), batch_update.py: raws x10 with `sha256: pending` + two-pass recompute → copy staged pages → heading-anchored appends x5 (Related→Related Pages→Sources→References fallback) → index sorted-insert with `_index` skip + count bump → log prepend with strip()-based H1 dedupe. All idempotency guards fired clean.
7. JP report via `write_report.py` (json-free plain write) with in-script gates: hangul count 0, han-eyeball list empty, 「」 42/42, （） 64/64. Still shipped 5 typos caught by the read-back grep (see below).
8. Scoped `git add` (20 files), `git commit -m`, one hook round-trip, push.

## Tag fires this run (page-name≠tag family, 8th/9th instances)

- `self-improvement` BLOCKED the new `concepts/language-model-weight-self-rewriting.md`: the token is NOT in SCHEMA even though `concepts/recursive-self-improvement.md` exists as a page — substring grep hits the longer tokens and passes a naive check; only `grep -cw self-improvement` returns 0. Fix: swapped to `self-improving` (already on the AI Agents category line).
- `operating-system` pre-validated as 0 — do NOT use it even though `concepts/operating-systems.md` (PLURAL) exists as a page. This run's page used `agent-governance, interoperability, surveillance, trust, privacy, agent-security` instead, all verified `grep -cw` = 1+.
- Working tag sets verified green this run: `[privacy, agent-safety, ai-safety, surveillance, trust, agent-security, agent-governance, interoperability]` and `[recursive-self-improvement, self-improving, model, training, ai-safety, interpretability, open-source, model-editing]`.

## JP-report typo classes that the in-script gates MISSED (read-back grep is the real gate)

The write_report.py gates (hangul count / han-eyeball / bracket balance) all passed while the report still shipped:
- Chinese `惯用` inside 「非惯用ドメイン解放」 (single-CJK-word leak, the han{2,} eyeball list didn't include it) — fixed via sed to 非日常.
- A raw markdown-italic underscore fragment `_distribution coercion_` with a stray Japanese-possessive の — rewritten to 教育テックにおける distribution coercion.
- `精度が上がるだけ` (awkward calque) → `上がり続けた`; `安全神話はどうか壊れるのか` → `はどう壊れるのか` (misspacing of どうして/どう).
- Missing space before `autoresearch`.
Rule: after the gates, ALSO grep the finished report for `[的惯]` plus a manual read of any `_italic_` spans and 「」 contents; fix via `sed -i` (report is hook-exempt).

## Wiki navigation notes

- `concepts/security-and-governance/agent-sandboxing.md` is the real path (top-level `concepts/agent-sandboxing.md` does NOT exist) — wikilink accordingly.
- Index insert for `concepts/security-and-governance/...` sorts under its full path string, which lands it after plain `concepts/s...` entries — acceptable, section is only mostly alphabetical.
- Post-commit count reconciliation clean (2382/972 both headers match grep counts; log H1 count exactly 1).

## Coverage notes for the next run

- GRH twin-announcement (Alpöge 2682pt + Masullo 2157pt + Tao 462pt + Buckmaster NS blowup 298pt): raw for Tao fetched, no wiki page yet — create `concepts/grh-announcements-2026-11.md` or extend `events/openai-navier-stokes-scooping-2026.md`; Alpöge PDF + Lean tar.gz not yet analyzed.
- Google union school-AI petition (277pt): raw saved, uningested — candidate `concepts/ai-in-education`.
- llms.txt/MCP-didnt-work essay (31pt): raw saved — candidate append to an existing MCP page (find first).
- DreamCoder (229pt, Mickey Petersen): raw saved — entity-ify under concepts/coding-agents/.
- "Fuck Your AI Safeguards" (609pt, ounapuu.ee, 11/19): fetch 404'd, uningested, high NJ score — retry fetch or Algolia tree (id 50562262) next run.
