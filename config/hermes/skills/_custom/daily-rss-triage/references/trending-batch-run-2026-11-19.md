# Trending-topics batch run — 2026-11-19 (weekday-noon clean run)

Reference for a clean `daily-rss-triage` / trending-topics run. ~14 tool calls, **1 commit (a8b6462f, 11 files)**, both pre-commit hooks green (after one tag fix), 8/8 primaries fetched, 5/5 lead stories comment-mined. Weekday noon, sibling jobs (active-crawl 11:00, hot-post 09:30, blog/newsletter ingest ~07:xx) had already created/updated most of the day's topics — so the honest output was a coverage table with a handful of genuinely-new pages, NOT batch new-page creation.

## What landed (verify against real git, not from memory)

- **NEW** `concepts/gemini/gemini-4-neon.md` — Google DeepMind Gemini 4 fast/price-efficient tier. #3 AA Intelligence Index (61, xhigh), Vals #2 (70.9%), #1 Legal Research / Tax Agent / AutomationBench / Vending-Bench 2, #2 Arena Agent Arena (1336). $3/$15 per 1M (cached input $0.15 = 95% off), 1M context. micjm projected Agent-Duel Elo ~1,066 vs Opus 5.5 1,078 from 127 tok/s on OpenRouter (vs Carbon 46 tps). HN 866p.
- **NEW** `concepts/nginx-http2-rce.md` — CVE-2026-123633 / CVE-2026-123007, CVSS 4.0 9.2 unauth HTTP/2 RCE in NGINX itself, 225M+ sites, CVE-123007 back to 1.9.5 (2015), F5 patched within ~30 min. Five independent teams (Wiz/Ikotas/Metnir/Rapid7/Xint). HN 1412p = day's #1. Linked to `systemic-software-breakdown` + `ai-vulnerability-discovery`.
- **APPEND** `concepts/microsoft-mai-models.md` — Ignite 2026 seven-model MAI family (Cyber 2 Flash / Code 2 / Code 2 Flash / Image 2.7 / Realtime 1 / Transcribe 2 / Decision 1.1) + Maia 200 accelerator + MAI Licensed Weights. HN 552p, vendor-run numbers.
- **APPEND** `entities/radixark.md` — DaisyRose-27B (Qwen3.8-27B + Miles RL; 1,200 tasks / 18 days / 144 H200; Terminal-Bench 4.1 pass@1 5.6%→12.0%). HN 223p.
- **APPEND** `concepts/gemini/index.md` — Neon section.
- 2 raws (`raw/articles/2026-11-18_blog.google_gemini-4-neon.md`, `..._wiz.io_nginx-http2-rce.md`), SCHEMA mint `model-release`, index +2 concept lines, log prepend, JP report `inbox/rss-scans/trending-topics-2026-11-19.md`.

Uncovered-but-reported (next-run candidates, NOT pages): KPMG UK 100-agent audit (467p), All About Berlin AI-Overviews death (783p, fold into `google-ai-overviews-liability`), Anthropic IPO pricing + safety-coalition (262/134p), Ruby2Shell (179p → systemic-software-breakdown).

## Three new pitfalls that cost round-trips (the rest was the documented clean path)

### 1. `append_section()` `^updated:` regex must be scoped to the frontmatter block
The whole-file `^updated:` trap is usually documented for the log-prepend case, but it also bites a reused single-page append helper — `re.sub(r"^updated: .*$", ..., count=1, flags=re.M)` replaces the FIRST `updated:` anywhere in `s`, which is fragile if a body heading ever carries one. Slice to the frontmatter, then splice back:
```python
head_end = s.find("---\n", 4)        # end of closing frontmatter fence
if head_end != -1:
    fm  = s[:head_end]
    fm2 = re.sub(r"^updated: .*$", f"updated: {TODAY}", fm, count=1, flags=re.M)
    s   = fm2 + s[head_end:]
```
Worked clean on 3 append targets in one script.

### 2. Log-prepend idempotency guard: test the exact entry HEADER, not a substring of the head
The naive `if "<subject>" not in s[:600]` guard false-negatives on a busy day — a sibling's earlier same-day entry (`## [2026-11-19] active-crawl ...`) fills the first ~600 chars, so the substring scan sees the subject and SKIPS your prepend. Use the precise form, combined with the strip()-based `# Wiki Log` dedupe:
```python
entry_header = f"## [{TODAY}] trending-topics"
if entry_header not in s:
    s2 = entry + "\n" + s
    out=[]; seen=False
    for ln in s2.split("\n"):
        if ln.strip()=="# Wiki Log":
            if seen: continue
            seen=True
        out.append(ln)
    s2="\n".join(out)
    if not s2.lstrip().startswith("# Wiki Log"):
        s2 = "# Wiki Log\n\n" + s2.lstrip("\n")
```
On this run the prepend fired once and left a duplicate `# Wiki Log` (the second one sits above the lower intro block) — the strip()-based dedupe (not exact-match) collapsed it to exactly 1.

### 3. Thirteenth instance of the page-name≠tag family: generic `agent` tag
Tagged the Gemini 4 Neon page with `agent` as ordinary agent vocabulary — the hook blocked the commit because **bare `agent` is NOT a whole-word SCHEMA token** (the taxonomy has `ai-agent`, `ai-agents`, `agents`, `coding-agent`, `coding-agents`, `multi-agent`, ... but `agent` passes only as a SUBSTRING of those — the substring-grep trap again). The page already carried `coding-agent`, so the fix was to DROP the generic `agent` (no SCHEMA mint). Same family as `legal`→`law`, `readability`, `licensing`, `lean`→`formal-methods`, `responsible-scaling`→`responsible-scaling-policy`, `agentic-commerce`. Rule stands: `grep -cw <tag> SCHEMA.md` EVERY planned tag whole-word — including plain single-word domain nouns you'd never doubt — and on a single-tag fire, if the page already has a specific sibling tag, DROP rather than mint.

## Positive confirmations (no action, the documented recipe held)

- `hn_algolia_supplement.py --days 2 --min-points 20` (run `timeout 150 … > out.txt`, read in two sed passes) + the keyword block BOTH needed: keyword pass caught Gemini 4 Neon, MAI Ignite, GPT-6.2, Anthropic IPO, KPMG audit, All About Berlin, DaisyRose; the points>120 sweep caught NGINX RCE + the AI-slop/audit stories the keyword terms missed.
- `fetch_sources.py` (Chrome UA + `Accept-Encoding: gzip` + gzip sniff `raw[:2]==b'\x1f\x8b'` + strip_html, print-and-continue) got **8/8** primaries first pass (blog.google, microsoft.ai, wiz.io, verialabs, radixark, europeanbusinessmagazine, nicolasbouliane, micjm) — none in the 403 gate class this run. `mine_comments.py` (per-story dict, `read(3_000_000)`, depth ≤1–2, cap ~8–14, min-len 90) produced report-grade author-quoted comments for all 5 lead stories in one run.
- Pre-delivery gates on the JP report: `hangul=0`, `brackets 「」 balanced (16/16)`, `parens （） balanced (49/49)`. The Han-grep EYEBALL gate caught two simplified-Chinese leaks the Hangul-only grep misses — `廉价`→`安価` and `创作者`→`創作者` — both fixed in the SOURCE `write_report.py` via `patch` and re-run (not just `sed -i` on the output), since the report-writing script is re-runnable. This re-confirms the 2026-11-17 Han-gate pitfall.
- No pipes to interpreters (the `cat file | python3 -c` and `cat file.txt | python3 -c` attempts were both BLOCKED by `tirith:pipe_to_interpreter`; switched to `python3 -c "open(...).read()"` inside a single python invocation). `execute_code` was not attempted (known-blocked in cron).
- SCHEMA self-tag pre-check caught `model-release` (0 whole-word hits) and minted it on the Models line (line 32, the richer Models category) BEFORE the commit. The batch script's heading-anchored insert-before-Related/See-Also/Sources worked across heterogeneous page shapes; the two-pass raw sha256 over body-after-frontmatter landed correct; scoped `git add` (11 files) excluded the ~15 concurrent sibling-job `config/hermes/skills/` + `wiki/` changes.
- Post-final-commit index reconciliation: `grep -c '^- \[\[concepts/'` = 2378 matched the header, `^- \[\[entities/` = 972 matched — no reconciliation commit needed (the documented two-step still worth running).

## Reusable fetch/mine scripts (this run's working skeleton)

- `/tmp/hn/fetch_sources.py`: `TARGETS=[(name,url),...]` loop, Chrome UA + gzip branch + strip_html, saves `/tmp/hn/articles/<name>.txt`, prints `OK name: N chars <<first 120>>` or `FAIL name: <code>` and CONTINUES.
- `/tmp/hn/mine_comments.py`: `IDS={name:objectID}` loop, Algolia `/items/<oid>` `read(3_000_000)`, walk `children` depth ≤1–2, strip tags, min-len ~90, cap ~8–14, print `[author] text[:480]`.
- `points_sweep.py`: `search?tags=story&numericFilters=created_at_i%3E{yesterday12:00},points%3E120&hitsPerPage=50` (URL-encode `>` as `%3E`).
