# Cross-Reference 2026-08-05 — Daily Run Notes

Wednesday run. No active-crawl research note (4th consecutive day) → volume-based skip (84 DB articles ≥ 20 threshold) + **8 targeted HN Algolia queries** (stable default). Dedup anchor = 08-03 daily + 08-03 weekly digest.

## Missing previous-day report
- No `trending-topics-2026-08-04.md` on disk → anchor was the 08-03 daily report + 08-03 weekly digest.
- Gap-day topics (08-03 evening → 08-05) were fair game ONLY after the wiki log head-scan confirmed no pipeline ingestion.

## Morning-pipeline dedup via `head -80 wiki/log.md`
Log head-scan (10:00–11:00 UTC entries) showed active-crawl + blog-wiki-ingest + newsletter-wiki-ingest had ALREADY ingested: steve-yegge (incl. Model Welfare Part 2), ed-zitron (AI Demand Bubble), minimax (H3), openai-codex (ChatGPT Work), megakernel-inference (MoK), anthropic-cybersecurity-eval-incidents (AISI report), events/openai-apple-conflict-2026 (PI stage), llm-generated-vulnerability-reports, ai-agent-safety-incidents, ds4-deepseek-flash-metal, sierra (Context Engine), lcamtuf (Meta: 7000), cory-doctorow.
**Result: 7 of 9 wiki actions were already ✅; residuals = `concepts/ai-economics` (updated 7/13, stale), `entities/elevenlabs` (updated 8/1, stale), `entities/warp` (MISSING → new-page candidate).**
Technique: grep frontmatter `updated:` dates on candidate pages = fast "needs update vs done" discriminator.

## Brotli scrape-failure stub
- `raw/articles/2026-08-05_elevenlabs_automatic-speech-recognition-asr.md` = 14 lines, content only `Scrape failed: brotli: decoder process called with data when 'can_accept_more_data()' is False`.
- Pattern: sitemap scraper writes a stub file on brotli decode error. Grep `Scrape failed` / check <1KB before deep reading; retry `curl -sL --compressed`; else web_search / secondary coverage.

## OpenAI News JS gate
- `curl` on `openai.com/index/third-party-cyber-evaluations-involving-openai-models` returned exactly `Enable JavaScript and cookies to continue`.
- Distinct message from SPA "You need to enable JavaScript." — same treatment: title + secondary coverage (AISI report ref already in wiki carried the substance), mark `本文未取得` in the report.

## trending_topics.py 0-newsletter quirk
- Script counted **0 newsletters**; `ls -t wiki/raw/newsletters/` showed **11 digest files** (08-03→08-05). Ran the subject-line scan manually anyway; AINews 8/5 subject "megakernels are so dead and so back" confirmed the MoK topic.

## HN calibration (8 targeted queries, curl-to-file)
| Topic | HN points | Rating |
|---|---|---|
| Warp Agent CLI | 104pts/62c | ★★★★☆ |
| AI Demand Bubble (Zitron) | 106pts/137c | ★★★★☆ |
| MiniMax H3 (ComfyUI day-0) | 329pts/93c | ★★★★☆ |
| Yegge Model Welfare Part 2 | 23pts/10c (Part 1: 80pts/75c) | ★★★★☆ (thought-leader weighting: Part 1 traction + controversy) |
| Cursor MoK | 12pts/0c | ★★★☆☆ |
| OpenAI×Apple PI | 1pt (Reuters link) | ★★★★☆ (significance, not HN — legal stories run low) |
| ChatGPT Work | Latent Space 2pts | ★★★★☆ (major product, platform significance) |

## Report decisions
- **Company concentration note** applied (OpenAI in 3/8 topics) per monoculture heuristic.
- **Voice cluster** (GPT-Live full-duplex + ElevenLabs ASR/HR/IVR) kept as wiki-action-only (elevenlabs.md stale 8/1), not a top-8 topic — trending script flagged `voice/speech` as new-page candidate; routed to `concepts/voice-ai-agents` 新設候補 in the action table.
- **T1 slop grep** run on the daily report (NO_SLOP_FOUND) — cheap quality gate that extends naturally to daily runs, not just the weekly digest.
