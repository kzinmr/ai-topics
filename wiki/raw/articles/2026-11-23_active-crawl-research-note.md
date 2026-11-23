---
title: "Active Crawl Research Note — 2026-11-23"
date: 2026-11-23
source: active-crawl
type: research-note
sources:
  - https://hn.algolia.com/api/v1/search  (HN checkpoint, 39 stories, 2026-11-14..19)
  - https://news.ycombinator.com/item?id=50549188
  - https://news.ycombinator.com/item?id=50536468
  - https://www.slowchronicle.com/posts/llm-assisted-reverse-engineering
---

# Active Crawl Research Note — 2026-11-23

## Discovery inputs

- HN Algolia checkpoint (`cron/data/active_crawl/hn_scan.json`, 39 stories, points≥20, 2026-11-14..19)
- Wiki gap analysis via glob/grep against concepts/ + entities/ + log.md

## Topics processed (3)

1. **Maritime (YC F26) — managed cloud for production AI agents** (Launch HN, 60 pts, Nov 18). FULL gap → created `entities/maritime.md`. "Sandboxes solve 10% of the infrastructure problem" thesis; lifecycle mgmt + custom environments + cost optimization ($1/mo 2GB agent); MIT Project NANDA founders. Raw: `raw/articles/2026-11-23_hn_launch-maritime-managed-cloud-for-agents.md`.
2. **StarSling (YC P25) — self-improving CI for agent-volume repos** (Launch HN, 89 pts, Nov 17). FULL gap → created `entities/starsling.md`. Agent loop optimizing CI itself (analyze → propose → side-by-side → statistical gate → PR); Mastra 1,800 PRs/mo; "CI bill got close to our inference bill". Raw: `raw/articles/2026-11-23_hn_launch-starsling-self-improving-ci.md`.
3. **LLM-assisted reverse engineering workflow** (Slow Chronicle, HN 223 pts, Nov 18). PARTIAL gap (concepts/reverse-engineering.md existed without agentic-RE practice) → enriched with Nov 2026 section. Raw already saved 2026-11-18 by upstream pipeline.

## Rejected / skipped

- **GPT-6.2 Astra & Sol** (HN 1339) — covered in `entities/openai-astra.md` §GPT-6.2 by 11-17/18 pipelines.
- **Gemini 4 Neon** (HN 846) — covered `concepts/gemini/gemini-4-neon.md` (blog pipeline + 11-18 active crawl).
- **Energy-Based Reasoners 385×** — `concepts/energy-based-reasoners.md` exists (11-18 active crawl).
- **FrontierHarness Eval v1.1** — `concepts/frontierharness-eval.md` exists (11-19).
- **Harvard code-review bottleneck** — `concepts/code-review-bottleneck.md` covers Chen & Stratton study + raw saved 11-17.
- **Cerebras disaggregated inference** — `concepts/cerebras-disaggregated-inference.md` created 11-17.
- **OpenAI chip design** — section added to `concepts/openai-jalapeno-inference-chip.md` on 11-18.
- **Claude protein sequences (Tu)** — covered in `entities/xinming-tu.md` (incl. Nov-18 update).
- **Windows coding-agent telemetry** — `concepts/windows-coding-agent-telemetry.md` exists.
- **TrnRT (Trainium inference)** — `concepts/trnrt-trainium-inference-engine.md` exists.
- **KPMG audit-agent trial** — single low-quality aggregator source (europeanbusinessmagazine), fails Page Thresholds; re-engage if a primary source (audit firm / regulator) appears.
- **Gemini Tasks free / tiny-voca TTS / DeepSeek-V3-JAX** — thin or low-source-quality; deferred.
