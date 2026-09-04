# Newsletter Triage 2026-08-09 — SuperIntel+ uid=480 + reversal-trend gap

Validated in the 2026-08-09 10:16 UTC newsletter-triage run (single-newsletter batch, 20 links).

## uid=480 (SuperIntel+ / read.getsuperintel.com) — tokens valid ~16h
- Newsletter "📉 Who Is Really Paying for Cheap Intelligence" (sent 2026-08-08 18:34, processed 2026-08-09 10:16).
- **ALL 20 tracking links resolved HTTP 200 at ~16h old** — same class as uid=443 (~18.5h) and uid=470 (~15h): test ONE link, trust a 200 verdict, resolve the batch normally. Do NOT assume expiry from age.
- Main article: `read.getsuperintel.com/p/who-is-really-paying-for-cheap-intelligence` (Superintel+ paywalled deepdive; ~24 substantive `<p>` visible before the "Subscribe to Superintel+ to read the rest" gate).
- Link distribution (matches inbox pre-triage exactly):
  - Link 1 = main article; Link 2 = duplicate of Link 1 (same resolved title — dedup)
  - Link 3 = @kimmonismus author X profile (skip)
  - Links 4-6 = OpenAI official GPT-5.6 posts (price-performance frontier / product page / efficiency) — all already covered by `concepts/gpt/gpt-5-6.md`
  - Link 7 = DeepSeek price increase (Yahoo Finance) — reference
  - Link 8 = Atlantic Council energy essay (non-AI-specific — skip)
  - Links 9-20 = subscription/social/ad boilerplate: whitelist page, upgrade page, X/IG/Threads/YT/TikTok/LinkedIn profiles, ad page, email prefs, beehiiv home (batch skip)
- Yield: 1 take + 1 reference + 7 skip decisions (batch entry collapsed links 9-20).

## Inbox summary accuracy (positive counter-example)
- The inbox pre-triage summary (`20260809T101608Z.json`) correctly identified the publication (SuperIntel read.getsuperintel.com), classified the OpenAI GPT-5.6 posts critical, DeepSeek high, and flagged links 9-20 as boilerplate — **all confirmed by actual curl resolution** (titles matched exactly).
- Contrast with the "AI Cursor Arrives!" false-positive (DeepMind mouse pointer): inbox summaries are reliable for **priority ordering + publication identification + link-class breakdown**, but verify specific topic claims via curl when they drive take/reference decisions. Here resolved titles matched the summary verbatim, so trust was warranted.

## Reversal-trend gap (NEW coverage heuristic)
- `entities/deepseek.md` had comprehensive coverage of DeepSeek price **CUTS** (Jul 31 V4-Flash-0731 price war, 75% V4-Pro discount, "too cheap to meter" framing) — but the **Aug 6 general price INCREASE notice** + **peak-hour 2x pricing (since Jun 30, Beijing 09:00-12:00 & 14:00-18:00)** was a genuine wiki gap.
- Test: when an article reports a development in the OPPOSITE direction of what an entity page documents (cuts vs increases, expansion vs contraction), the page's existing trend coverage does NOT cover the counter-trend. "Covered trend ≠ covered counter-trend."
- Also captured in the take: the **Moonshot correction** — the "20,000-GPU" figure attached to DeepSeek's increase is from Bloomberg's report about Moonshot (wccftech 08/06), not DeepSeek. Correction notes like this are high-value wiki content because secondary accounts propagate the error.

## Archive verification — stdout wrapper vs flat file structure
- `archive_triage.py` **stdout** prints `{"newsletter": {"ok": ..., "candidates": ..., "new_archived": ..., "dedup_skipped": ..., "archive_path": ..., "total_archive_urls": ...}}` (per-source wrapper key).
- BUT the **archive FILE** at `archive_path` is FLAT: top-level keys = `archived_at`, `triage_run_id`, `source`, `summary_ja`, `decisions` (no `newsletter`/`blog` wrapper).
- Verification pattern that failed: `python3 -c` reading the file and expecting `d['newsletter']` → all None. Correct: parse stdout JSON for stats, and read the file with `d['decisions']` directly (hardcoded path, no pipe).
- Pipe verification `python3 script | python3 -c` is BLOCKED by `tirith:pipe_to_interpreter` — use separate `python3 -c` calls with hardcoded file paths.
