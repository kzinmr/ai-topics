---
title: Anthropic
created: 2026-05-29
updated: 2026-05-31
type: entity
tags: [company, lab, anthropic, ai-native, pricing, token-economics, vc, ai-safety, model]
sources: [raw/articles/simonwillison.net--2026-may-29-anthropic--9831b607.md, raw/articles/simonwillison.net--2026-may-28-claude-opus-4-8--8d05463f.md, raw/newsletters/2026-05-29-ainews-anthropic-raises-965b-series-h-releases-opus-4-8-and-dynamic-workflows-ul.md, raw/newsletters/2026-05-30-the-compute-to-cash-race.md, raw/articles/simonwillison.net--2026-may-31-anthropic-run-rate--9dee9002.md]
---

# Anthropic

AI research company and public benefit corporation. Founded 2021 by former OpenAI researchers Dario Amodei (CEO) and Daniela Amodei (President). Creator of the [[Claude models]] family. Major competitor to [[OpenAI]] and [[Google DeepMind]].

## Financials

### Revenue Growth
Anthropic has shared run-rate revenue in funding announcements. The specific calculation methodology (Reuters Breakingviews, Karen Kwok, citing "a person familiar with the matter"):
- **Consumption-based**: last 28 days of sales × 13
- **Subscription-based**: monthly revenue × 12
- Combined = total run-rate

This 13× multiplier on consumption means short-term usage spikes get annualized into headline numbers — an important caveat when comparing to standard ARR. See [[ai-economics]] for the "tokenmaxxing" sustainability debate.

| Date | Run-Rate Revenue | Context |
|------|-----------------|---------|
| Early 2026 | $30B | Axios CEO Jim VandeHei: "can't find any company in any industry, in any era that has scaled organic revenue this quickly" |
| May 2026 | $47B | Announced alongside $65B Series H |

### Series H — Full Details ($65B, May 2026)
- **Valuation**: $965B (exceeding OpenAI's valuation)
- **Raised**: $65B
- **Lead investors**: Altimeter (largest investor), Dragoneer, Greenoaks, Sequoia
- **Run-rate revenue**: $47B (up from $9B in December 2025)
- **Revenue growth**: 5× in 5 months

### Mythos-Class Model Plans
Anthropic's **Mythos-class** model is described as a "new class of model" more capable than Opus. The company is adopting a **stepped-release strategy**:
1. **Opus 4.8** released as a commercially safe model — the most honest Claude model to date
2. **Mythos-class** reserved until stronger safety controls can be implemented for its advanced capabilities
3. This mirrors the earlier decision to withhold the original Mythos model — Anthropic explicitly states it will not release models with dangerous capabilities until control measures are adequate

The strategy positions Anthropic as the most safety-conscious among frontier labs, using multiple capability tiers (Haiku → Sonnet → Opus → Mythos) to manage risk.

- Largest single funding round for an AI company
- Run-rate revenue crossed $47B earlier that month
- Revenue trajectory debated: Ed Zitron expressed skepticism; Simon Willison notes these numbers appear in fundraising announcements, making them subject to securities fraud liability if fabricated

### Revenue Drivers
- Enterprise adoption of Claude models
- "Tokenmaxxing" phenomenon: companies encouraging employees to maximize AI usage without ROI measurement
- Anecdotal report (Axios, May 2026): one company spent $500M in a single month after failing to set usage limits on Claude licenses
- Emerging concern: tokenmaxxing may be unsustainable; some enterprises starting to question ROI (see [[ai-economics]])

## Models

Primary model family: [[Claude models]]

| Model | Release | Key Features |
|-------|---------|-------------|
| Claude Opus 4.5 | Early 2026 | High-capability reasoning |
| Claude Opus 4.6 | Mid 2026 | Fast mode $30/$150 per MTok |
| Claude Opus 4.7 | Mid 2026 | 1M context, 128K output |
| Claude Opus 4.8 | May 28, 2026 | Honesty improvements, mid-conversation system messages, lower prompt cache minimum (1,024 tokens). Benchmarks: SWE-Bench Pro 69.2% (+10pts vs GPT-5.5), FrontierSWE #1, APEX-SWE 45.3% Pass@1, GDPval-AA 1890 Elo, AA Intelligence Index 61.4 |

### Claude Opus Pricing (4.8)
- Standard: $5/M input, $25/M output tokens
- Fast mode: $10/M input, $50/M output (significant reduction from 4.6/4.7's $30/$150; research preview only)

## Safety & Honesty

Claude Opus 4.8 introduced notable honesty improvements:
- 4× less likely than predecessor to allow code flaws to pass unremarked
- Lowest incorrect-rate on all benchmarks among 6 tested models
- Achieves this mainly through abstention rather than higher correct-answer rate
- System card shows measurable reduction in factual hallucination

Training philosophy: train models to avoid unsupported claims and flag uncertainty.

## Technical Features (Opus 4.8)



## Opus 4.8 Benchmark Results

| Benchmark | Opus 4.8 | Comparison |
|-----------|----------|------------|
| SWE-Bench Pro | 69.2% | +10pts vs GPT-5.5 |
| FrontierSWE | #1 | Top-ranked |
| APEX-SWE Pass@1 | 45.3% | GPT-5.3 Codex: 41.5% |
| GDPval-AA Elo | 1890 | +137 vs Opus 4.7 |
| AA Intelligence Index | 61.4 | +4.1 vs Opus 4.7 |
| Efficiency | 15% fewer turns, 35% less output tokens per task | vs Opus 4.7 |

- **Mid-conversation system messages**: Accept `role: "system"` messages after user turns (subject to placement rules). Enables updated instructions without restating full system prompt, preserving prompt cache hits in agentic loops.
- **Lower prompt cache minimum**: 1,024 tokens (down from 4,096 in 4.7)
- **Context window**: 1,000,000 tokens
- **Max output**: 128,000 tokens
- **Knowledge cutoff**: January 2026

## Leadership
- **Dario Amodei** — CEO, co-founder
- **Daniela Amodei** — President, co-founder
- **Jack Clark** — Co-founder, Import AI newsletter, see [[jack-clark]]
- **Andrej Karpathy** — Joined pre-training team (May 2026); previously co-founder of OpenAI, notable for choosing Anthropic over OpenAI return

## Related Pages
- [[Claude models]] — Model family details
- [[ai-economics]] — Tokenmaxxing, AI ROI debate
- [[Gary Marcus]] — AI industry skepticism
- [[OpenAI]] — Primary competitor
- [[Ed Zitron]] — Revenue skepticism
