---
title: "Trending Topics Research — Active Crawl 2026-07-17"
date: "2026-07-17"
date_fetched: "2026-07-17"
type: research_note
sources:
  - https://hn.algolia.com/api/v1/search (multiple queries)
  - https://news.ycombinator.com/ (front page scan)
  - xurl search (5 queries via X/Twitter API)
  - /opt/data/.blogwatcher/blogwatcher.db (direct SQLite query)
  - /opt/data/ai-topics/wiki/ (coverage gap analysis)
---

# Trending Topics Research — Active Crawl 2026-07-17

## Discovery Methodology
- **HN Algolia**: 45+ AI-relevant search terms across July 14-17, 2026. Filtered for points ≥ 10. 49 raw matches → 15 curated.
- **X/Twitter (xurl)**: 5 targeted queries (agent coding, model releases, OpenAI/Anthropic/DeepSeek, reasoning/inference, AI safety). ~100 raw → 10 curated.
- **Blogwatcher DB**: SQLite direct query for last 3 days, 50 most recent articles.
- **Wiki Gap Analysis**: Cross-referenced all discovered topics against ~1,896 concept pages and ~852 entity pages.

## Top 15 HN Stories (by points)

| # | Title | Points | Date | Wiki Coverage |
|---|-------|--------|------|---------------|
| 1 | Kimi K3: Open Frontier Intelligence | 1,677 | Jul 16 | COVERED (concepts/kimi-k3.md) |
| 2 | Cursor 0day: Full Disclosure | 453 | Jul 14 | PARTIAL (cursor pages exist, no security-specific) |
| 3 | Gemma 4 26B on 13-year-old Xeon | 324 | Jul 15 | COVERED |
| 4 | NotebookLM → Gemini Notebook | 314 | Jul 16 | FULL GAP → Created |
| 5 | YC founders at OpenAI/Anthropic | 298 | Jul 16 | FULL GAP |
| 6 | Claude Fable 5 vs GPT-5.6 Music Video | 288 | Jul 16 | PARTIAL |
| 7 | LM Studio Bionic agent | 264 | Jul 16 | PARTIAL (entity exists) |
| 8 | LLM Critics Are Right | 237 | Jul 16 | FULL GAP |
| 9 | Human-in-the-loop is tired (Pydantic) | 232 | Jul 17 | COVERED |
| 10 | Detecting LLM-Generated Texts with Classical ML | 204 | Jul 16 | FULL GAP → Created |
| 11 | AI Voice Fraud (Three-Second Theft) | 188 | Jul 15 | FULL GAP → Created |
| 12 | Demis Hassabis AI Safety Plan | 157 | Jul 14 | FULL GAP |
| 13 | Little Book of Reinforcement Learning | 145 | Jul 16 | FULL GAP |
| 14 | CUDA Alternatives (Spectral Compute) | 141 | Jul 14 | FULL GAP (403 blocked) |
| 15 | Soofi S German 30B Model | 139 | Jul 16 | FULL GAP → Created |

## Pages Created (4)

1. **concepts/ai-voice-fraud.md** — AI Voice Fraud
2. **concepts/gemini-notebook.md** — Gemini Notebook (NotebookLM rebranding)
3. **concepts/llm-text-detection-classical-ml.md** — LLM Text Detection with Classical ML
4. **concepts/soofi-s.md** — Soofi S German 30B Model

## Sources Blocked
- **Spectral Compute / HPCwire** (hpcwire.com): HTTP 403

## Topics Not Created (rationale)
- Kimi K3: Already well-documented (concepts/kimi-k3.md, entities/kimi.md, entities/moonshot-ai.md)
- Cursor 0day: Partial coverage, but existing 7 cursor pages cover the IDE comprehensively
- Gemma 4 CPU inference: Already covered (concepts/cpu-inference-llm.md, concepts/gemma-family.md)
- LM Studio Bionic: Entity exists (entities/lm-studio.md), Bionic-specific concept could be added in future
- DeepSeek-V4: Already covered (concepts/deepseek-v4.md)
- Claude Code: Extensive coverage (18+ pages across concepts/claude-code/)
- Human-in-the-loop: Already covered (concepts/human-in-the-loop.md)
