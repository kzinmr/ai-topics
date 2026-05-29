---
title: Claude Models
created: 2026-05-29
updated: 2026-05-29
type: concept
tags: [model, text-generation, llm, anthropic, pricing, ai-safety, prompt-caching, agentic-engineering, reasoning]
sources: [raw/articles/simonwillison.net--2026-may-28-claude-opus-4-8--8d05463f.md, raw/articles/simonwillison.net--2026-may-28-llm-anthropic--93579451.md]
---

# Claude Models

Family of large language models developed by [[Anthropic]]. Named after Claude Shannon. Known for emphasis on safety, honesty, and helpfulness.

## Model Versions

### Claude Opus 4.8 (May 28, 2026)

Latest release. Self-described as "a modest but tangible improvement" — notable for Anthropic's unusually honest framing of an incremental release.

**Key improvements:**

1. **Honesty**: ~4× less likely to allow code flaws to pass unremarked. Lowest incorrect-rate on all benchmarks among 6 tested models (achieved through abstention on uncertain questions). System card confirms lowest factual hallucination rate.

2. **Mid-conversation system messages**: Accepts `role: "system"` messages after user turns. Enables updating instructions mid-conversation without restating the full system prompt — preserves prompt cache hits and reduces input cost in agentic loops. Anthropic Python SDK updated to support this.

3. **Lower prompt cache minimum**: 1,024 tokens (down from 4,096 in 4.7). Cheaper caching for shorter conversations.

**Specs:**
- Context window: 1,000,000 tokens
- Max output: 128,000 tokens
- Knowledge cutoff: January 2026
- Pricing: $5/M input, $25/M output (standard); $10/M input, $50/M output (fast mode, research preview)
- Fast mode price drop: 4.6/4.7 fast mode was $30/$150 per MTok

**Tooling support:** [[llm-anthropic]] 0.25.1 (Simon Willison's LLM library) adds `claude-opus-4.8` model alias and `-o fast 1` option.

### Claude Opus 4.7
- 1M context, 128K output
- Prompt cache minimum: 4,096 tokens
- Knowledge cutoff: January 2026

### Claude Opus 4.6
- Fast mode pricing: $30/M input, $150/M output

### Claude Opus 4.5
- Earlier high-capability model

## Honesty Philosophy

Anthropic trains models to avoid unsupported claims. Opus 4.8's system card quantifies this: lowest incorrect-rate across all benchmarks, prioritizing abstention over confident wrong answers. This represents a deliberate design choice favoring trustworthiness over apparent capability.

## Developer Ecosystem

- **llm-anthropic** (Simon Willison's LLM plugin): Python/CLI tool for interacting with Claude models
- **Anthropic Python SDK**: Updated for mid-conversation system messages
- Default `max_tokens` now set to model maximum output (was 8,192)

## Related Pages
- [[Anthropic]] — Company behind Claude
- [[prompt-caching]] — Mechanism enabled by mid-conversation system messages
- [[llm-anthropic]] — Simon Willison's Python/CLI tool
- [[ai-economics]] — Tokenmaxxing and AI ROI debate
- [[Datasette]] — Simon Willison's SQLite tool (uses llm-anthropic)
