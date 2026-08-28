# Cross-Reference — 2026-08-15 (gap-day report-miss pattern)

Worked example from 2026-08-15: **no 08-14 report existed** (anchor = 08-13), and the
08-13 report had MISSED four major stories that the wiki HAD covered. Key lesson:
**wiki coverage and report coverage are independent artifacts** — do not drop a topic
because log.md shows pages were created; check whether the LAST REPORT mentioned it.

## Report-miss detection

The 08-13 report (generated 12:19 UTC) missed, and this run correctly surfaced:
- **Gemini 3.7 Flash** (8/13, blog.google) — HN 953pts/484c, biggest story of window
- **GLM-5.3** (8/14, z.ai) — HN 1103pts/543c, emergent cyber capabilities
- **GPT-5.6 Sol Ultrafast** (8/13, OpenAI + Cerebras) — Cerebras post 701pts/272c
- **OpenAI/Anthropic IPO wave** (8/13-15) — OpenAI $40B run rate, Anthropic $2T IPO

All four were wiki-covered (active-crawl created gemini-3-7-flash / deepseek-harness /
responsible-scaling-policy / agent-skill-supply-chain-attacks pages; gpt-5-6.md got the
Ultrafast section on 8/14). The 8/13 report simply didn't mention them — either published
after its generation window or on the gap day 8/14.

**Detection recipe** (fast, <2 min):
1. `head -80 wiki/log.md` → confirms what the morning pipelines created (already-covered signal)
2. Read the LAST report's topic list → confirms what was REPORTED (dedup anchor)
3. For anything the pipelines ingested that the last report lacks, run the HN query
   (scripts/hn_calibrate.py) → if points are high (>400), it is a report-miss, report it
   as a NEW topic even though the wiki page exists. The report is the user-facing
   deliverable; the wiki is the durable layer.

## Residual carryover

The 08-13 report flagged qwen-3-8.md's missing "open-weights actually released 8/12-13"
section (vLLM same-day, B300/MI355X 4bit, text-only limitation, Unsloth 1bit 4.9TB→397GB)
as its only residual. On 08-15 it was STILL pending: `grep -niE "vllm|b300|mi355x|unsloth|4bit"`
on wiki/concepts/qwen-3-8.md returned nothing and frontmatter `updated:` was 08-13.

**Lesson**: carry un-done residuals forward in the action table across reports, and verify
residual state by keyword grep of the target page, NOT by frontmatter `updated:` date
(a page can be touched without containing the required section). Pattern:
`grep -niE "<distinctive keywords from the residual>" wiki/<target>.md`.

## Confirmed patterns (3rd recurrence)

- active-crawl ran (created 5 concept pages) and wrote NO `*trending-topics-research*`
  note — log.md head-scan is the reliable "did active-crawl run" signal. Volume-based
  skip of full HN sweep is stable; only targeted point-score queries needed.
- Morning pipelines pre-ingested 6/7 topics → wiki-action table mostly ✅ with the
  qwen-3-8 residual as the one genuine leftover.
- Daily report is save-only (untracked in git; no commit). Confirmed again.
- HN calibration via scripts/hn_calibrate.py (urllib, search_by_date, `%3E` for `>` in
  numericFilters) worked cleanly in cron mode with zero delegation failures.
