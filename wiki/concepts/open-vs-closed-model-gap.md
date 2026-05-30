---
title: "Open vs. Closed Model Capability Gap"
created: 2026-05-30
updated: 2026-05-30
type: concept
tags: [benchmark, evaluation, model, open-source, comparison]
sources:
  - "wiki/raw/articles/2026-05-28_epoch-ai_open-closed-eci-gap.md"
---

# Open vs. Closed Model Capability Gap

The open vs. closed model capability gap measures how far behind open-weight models lag the most capable proprietary (closed-weight) models, expressed in both **time** (months of delay) and **capability** (ECI points). This is tracked by [[entities/epoch-ai]] using the [[concepts/epoch-capabilities-index|Epoch Capabilities Index (ECI)]].

## Current State (May 2026)

| Dimension | Value | Notes |
|-----------|-------|-------|
| **Time lag** | 4 months | Average gap (Jan 2026–May 2026), up from 3 months (Jan 2023–Oct 2025) |
| **ECI gap** | 8 points | 90% CI: 7–11 units, similar to the gap between GPT-5 and GPT-5.5 |
| **Strict gap** | 6 months | If requiring point estimate to be strictly higher (not just 5% bootstrap overlap) |

## How the Gap Is Measured

Epoch AI uses two complementary methods:

1. **Horizontal (time) gap**: For each day, find the best open-weight model's ECI. Ask: "When was the closed SOTA at this same ECI level?" The answer in days is the time gap. Average across all days in the analysis window.

2. **Vertical (capability) gap**: For each day, measure the ECI point difference between open-weight SOTA and absolute SOTA. Average across the window.

The "catching up" criterion uses bootstrap resampling: an open-weight model is considered to have caught up to a previous SOTA if it outperforms that SOTA in at least 5% of paired bootstrap samples (i.e., the SOTA is not significantly better at the 5% level).

## Historical Trend

| Period | Time Gap | ECI Gap | Source |
|--------|----------|---------|--------|
| Jan 2023 – Oct 2025 | 3 months | ~7 points | [Epoch AI, Oct 2025](https://epoch.ai/data-insights/open-weights-vs-closed-weights-models) |
| Jan 2026 – May 2026 | 4 months | 8 points | [Epoch AI, May 2026](https://epoch.ai/data-insights/open-closed-eci-gap) |

The gap has widened modestly (3→4 months) as frontier development accelerated. However, the gap has **not blown out** despite relentless proprietary model advancement — a sign of open-weight ecosystem strength.

## Model Progression

**Closed-weight SOTA trajectory** (Jan 2023–May 2026):
GPT-4 → o1-mini → o1 → o3 → GPT-5 Pro → GPT-5.3 Codex → GPT-5.5 Pro

**Open-weight SOTA trajectory** (same period):
Llama 2-70B → Mixtral → Llama 3.1-405B → DeepSeek-R1 → DeepSeek-V3 → Qwen3-235B-A22B → Kimi K2.6

## Chinese Dominance of Open-Weight Frontier

A significant shift since late 2025: the open-weight leaderboard is now **Chinese-dominated**. As of May 2026:
- **Kimi K2.6** (Moonshot AI) — top open-weights on Artificial Analysis Intelligence Index
- **GLM-5.1** (Z.ai) — close behind
- **MiniMax-M2.7** — competitive
- **DeepSeek-V4 Pro** — returned to top tier
- Western open-weight models (including OpenAI's gpt-oss-120B) rank lower

This marks a departure from the earlier era when Meta's Llama family was the primary open-weight benchmark.

## Business Implications

### For Enterprise Buyers
A 4-month lag translates to **meaningful capability differences** on tasks requiring frontier-level reasoning, coding, or agentic performance. Anthropic's explosive revenue growth (driven by enterprise Claude adoption) shows businesses are willing to pay for this edge.

### For Developers and Cost-Sensitive Markets
Open-weight models can be **self-hosted, fine-tuned, and deployed without API dependency**. A gap measured in months (not years) makes this trade-off increasingly rational.

### For Proprietary Lab Valuations
OpenAI ($852B) and Anthropic ($965B) valuations implicitly price in a **durable advantage** for proprietary models. If open-weight models maintain a stable 4-month lag despite frontier acceleration, the premium that closed labs can charge faces **long-term pressure**. The key question is whether the gap stays constant, widens, or narrows.

## Limitations

Epoch AI's analysis **likely understates the true gap** because:
1. Leading closed labs do not always release their most capable models (for safety, commercial, or competitive reasons)
2. Only models with enough public benchmark coverage to assign an ECI are included
3. If closed labs are sitting on unpublished models, the real gap is larger

## Related Pages

- [[entities/epoch-ai]] — Organization behind the ECI and this analysis
- [[concepts/epoch-capabilities-index]] — The measurement methodology
- [[comparisons/frontier-models-2026-04]] — Frontier model landscape (Apr 2026)
- [[concepts/open-weights-licensing-tightening]] — Related trend of license tightening
- [[concepts/harness-commoditization]] — How frontier capability commoditizes agent harnesses
