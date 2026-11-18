# beehiiv uid=902 — "AI 2027" newsletter (AI Futures Project / Lightcone Infrastructure)

Observed 2026-11-12 triage (run_id 20261112T101034Z): subject "🚨 AI 2027 Authors Now Expect 2027 Takeoff",
20 `link.mail.beehiiv.com/v2/c/...` tracking links, all HTTP 403 (~15h after send, no redirect chain).

## Publication identity

- **publisher**: AI 2027 / AI Futures Project, designed by Lightcone Infrastructure
- **authors**: Daniel Kokotajlo, Scott Alexander, Thomas Larsen, Eli Lifland, Romeo Dean (research pages credited
  to Eli Lifland, Nikola Jurkovic, FutureSearch)
- **beehiiv source_label**: `uid=902`
- **topic space**: AGI timeline forecasting, takeoff speed, compute forecast, AI goals, security forecast

## Why this one is NOT resolvable (unlike other beehiiv pubs)

Most beehiiv pubs have a canonical article host you can pivot to when tracking tokens expire. This one does not:

| Attempt | Result |
|---|---|
| `link.mail.beehiiv.com/v2/c/...` (any link) | 403, no redirect chain → token expired (batch verdict after testing 1-3 links) |
| `get2027.com`, `ai2027.getbeehiiv.com`, `read.ai-2027.com`, `ai-2027.io` | empty response (0 bytes) — these do not exist |
| `ai2027.substack.com` | resolves but is a **different** publication ("craig warner") |
| DuckDuckGo `html.` and `lite.` endpoints for the exact subject | 0 results |
| HN Algolia `search_by_date` for `"AI 2027" takeoff` / `Kokotajlo timeline` | 0 relevant hits |

**Do not burn calls on more guesses.** Test one beehiiv link (403 confirmed) → skip straight to the official site.

## Usable substitute source: the official project site (curl-able, no auth)

```
https://ai-2027.com/                      # 1.9MB static page, full scenario text
https://ai-2027.com/research              # supplements index (Compute/Timelines/Takeoff/AI Goals/Security Forecast)
https://ai-2027.com/research/timelines-forecast   # 1.4MB, 72k chars of extracted text
https://ai-2027.com/research/takeoff-forecast
https://ai-2040.com/                      # "Plan A" sequel scenario (Larsen, Dean, Halstead, Lifland, Greenblatt, Kokotajlo)
https://aifuturesmodel.com/               # interactive forecast model (3.3MB, JS app — no extractable prose)
```

Extraction recipe that works (scripts are stripped before tag-strip or the 1.9MB page floods with JS):

```python
h2 = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', html, flags=re.DOTALL|re.I)
txt = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h2))
```

`ai-2027.com/blog`, `/newsletter`, `/updates` all return the same 391KB "404 - Page Not Found" SPA shell with no
links — do not treat the 200 as content.

## ⚠️ Subject-line overclaim trap (this is the durable lesson)

Subject: "🚨 AI 2027 Authors Now Expect **2027 Takeoff**". The official site's own caveat says:

> "2027 was our **modal** (most likely) year at the time of publication, our **medians were somewhat longer**.
> (Added Nov 22 2025, to prevent misunderstandings: we don't know exactly when AGI will be built.)"

and `research/timelines-forecast` carries "2025 Dec 31 update: revamped timelines and takeoff model at
aifuturesmodel.com", with the May 2025 model update *lengthening* Eli's median to 2029.

So the headline could mean either (a) a genuine median shortening back to 2027, or (b) a re-assertion of the modal
year they always had. **Body unreachable → you cannot distinguish. Never ship a `take` on this subject line.**
Record it as a durable lead and let the IMAP re-fetch settle it; when the body does land, the modal-vs-median
distinction must be written into the event page as a dated contested claim (per AGENTS.md 矛盾を消さない).

## Correct triage outcome when body is unreachable

- `recommended_action: reference`, ★★★★☆, `candidate_wiki_path: queries/unresolved-newsletter-leads.md`
  (the durable-lead page pattern from `newsletter-wiki-ingest-2026-11-01-patterns.md`)
- reason_ja must state the verified coverage gap (see below) and the IMAP follow-up Message-ID
- batch-skip the remaining tracking links as one entry (`item_ids: [...]` array), citing the 1-3 link sample
- archive with `python3 ~/ai-topics/scripts/archive_triage.py newsletter --keep-reference`

## Verified wiki coverage gaps (as of 2026-11-12 — re-verify, may be closed since)

- `entities/daniel-kokotajlo.md` — absent (0 hits)
- `entities/eli-lifland.md` — absent
- `events/*ai-2027*` — absent
- `concepts/superintelligence.md`, `concepts/agi-economics.md` — 20-line stubs → stub-as-take-signal applies
- `concepts/ai-timelines-esni-tasks.md` — 92 lines, substantive but March-2026-vintage ESNI analysis; does **not**
  carry the AI 2027 scenario milestones (superhuman coder 2027 / generally superintelligent AI 2028)

## Tooling note

`web_search` is **not in this profile's toolset** (available: delegate_task, execute_code, memory, patch, process,
read_file, search_files, session_search, skill_*, terminal, todo, vision_analyze, write_file). For discovery use
`curl` via a `/tmp/` script against `html.duckduckgo.com/html/?q=`, `lite.duckduckgo.com/lite/?q=`, or
`hn.algolia.com/api/v1/search_by_date?query=...&tags=story`. A 14KB DDG response with 0 parsed `result__a` links
means no results, not a parse failure — confirm by checking the response size against a known-good query.
