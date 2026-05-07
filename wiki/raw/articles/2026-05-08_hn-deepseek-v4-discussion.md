---
title: "HN Discussion: DeepSeek V4"
source: "Hacker News"
url: "https://news.ycombinator.com/item?id=47884971"
date: 2026-04
scraped: 2026-05-08
type: community-discussion
tags: [deepseek, hn, benchmark, geopolitics, local-llm, pricing]
---

# HN Discussion: DeepSeek V4 — Key Insights

## Performance Beyond Paper
- **SWE-bench Verified: 80.6%** — first open-weights model to cross 80% threshold
- V4-Pro (max thinking) excels at PhD-level probability, statistics, random matrix theory; generates more rigorous proofs than Gemini
- Rivals Claude 3.5 Opus in system design and complex refactoring
- Flash outperforms Qwen 3.5 and matches Gemini-3-Flash in customer support while cheaper
- V4-Pro slightly better than Claude 3.5 Sonnet, trails Opus 4.6 with Thinking enabled

## Local Inference
- **V4-Flash** (~154GB native weights): runs on Mac Studio M3 Ultra (512GB RAM)
- **V4-Pro** (~800GB full precision, ~400GB+ large quants): requires massive VRAM
- Open weights, MIT License

## Pricing & Dev Experience
- API: Pro $1.74/$3.48 per M tokens, Flash $0.14/$0.28
- Docs praised as "no-BS"; integrates with Aider, Claude Code, Zed
- API lacks JSON schema and Batch API; "429 Overload" errors during launch

## Geopolitics
- Chinese-hosted API censored on sensitive topics; local versions bypass
- Some prefer "hard refusal" over Western "moralizing"
- Seen as "dumping" strategy gaining market share despite US sanctions
- "European Option": Mistral/Kyutai caught between low-cost Chinese and high-performance US models
