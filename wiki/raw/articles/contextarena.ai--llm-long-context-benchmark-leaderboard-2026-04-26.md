---
title: "Context Arena — LLM Long-Context Benchmark Leaderboard"
url: "https://contextarena.ai/"
fetched_at: 2026-04-26T22:35:00.000000+00:00
source_date: 2026-04-26
tags: [benchmark, long-context, leaderboard]
---

# Context Arena — LLM Long-Context Benchmark Leaderboard

Source: https://contextarena.ai/

Leaderboard: GDM-MRCRv2 Full (8-Needle)

70 LLMs evaluated on long-context retrieval performance across 128k and 1M token windows, tracking accuracy, AUC, token efficiency, and cost.

## Key Definitions & Badges

- **N/A**: No results for this model/bin, potentially due to context window limits.
- **AUC** (Area Under Curve): Normalized to 100%, reflects overall performance across bins, weighted by bin width.
- **🏆**: Top 3 models for that metric (higher score / lower cost is better).
- **🧠**: Reasoning was enabled for this model variant.
- **🤝**: Run sponsored by a provider (API credits donated).
- **NEW**: New results (updated recently).

## Top Performers

| Tier | Model(s) | 128k Accuracy | AUC @1M | Max Context | Token Eff. |
|---|---|---|---|---|---|
| 🥇 Elite | gpt-5.5 (all variants) | 67.0% – 85.8% | 47.3% – 50.9% | 1,050,000 | 0.98x |
| 🥈 Strong | claude-opus-4.6 / sonnet-4.6 | 68.1% – 72.6% | 43.4% – 46.9% | 1,000,000 | 1.13x |
| 🥉 Mid-Tier | gemini-3.1-pro-preview / gpt-5.4 | 54.6% – 67.8% | 33.9% – 40.0% | 1,048,576 | 0.98x – 1.00x |
| ⚡ Budget/Free | deepseek-v4-pro/flash, mimo-v2.5, mistral-small-4 | 17.7% – 48.4% | 14.9% – 28.3% | 1,048,576 | 1.00x – 1.02x |

## Key Performance Notes

- **GPT-5.5** dominates long-context retrieval, maintaining >83% accuracy at 128k and ~50% AUC at 1M across all performance tiers.
- **Claude Opus 4.6 & Sonnet 4.6** show consistent mid-to-high performance but degrade noticeably at 1M context.
- **Gemini 3.1 Pro** exhibits sharp degradation at 1M context (drops to 25.9% accuracy), though it remains competitive at 128k.
- **Reasoning-enabled variants** (psychology badge) generally outperform standard variants within the same model family.

## Cost & Efficiency Analysis

- **Free Models**: deepseek-v4-pro, deepseek-v4-flash, mimo-v2.5, mistral-small-4 (all variants) → $0.00
- **High Cost at 1M Context**: gemini-3.1-pro-preview (~$2,026–$2,110), grok-4.20 (~$1,893–$1,934)
- **Token Efficiency**: Ranges from 0.95x (Grok-4.20) to 1.63x (Claude Opus 4.7). Lower = better.
- **Cost at 128k**: Most top-tier models range between $128–$161. Budget models (gemini-3-flash) cost ~$6–$12.

## Context Window Limits

| Limit Range | Representative Models |
|---|---|
| ~1M Tokens | GPT-5.4/5.5, Claude Opus/Sonnet 4.6/4.7, Gemini 3.1/Flash, Grok-4.20 |
| 2M Tokens | grok-4.20 (only model in dataset) |
| 200k – 400k Tokens | GPT-5.4-nano/mini, Kimi K2.5/K2.6, GLM-5.1, Nemotron-3-Super, Claude Opus 4.7, Claude Haiku 4.5 |

## Actionable Insights

1. **Long-Context Retrieval Leader**: gpt-5.5 variants are the clear winners for 1M+ token tasks.
2. **Cost-Performance Tradeoff**: deepseek-v4-pro and mimo series provide free access with respectable mid-tier performance.
3. **Context Degradation Warning**: gemini-3.1-pro and grok-4.20 show significant accuracy drops at 1M context.
4. **Reasoning Boost**: Models tagged with 🧠 consistently outperform their standard counterparts.
5. **Efficiency Metric**: Prioritize models with Tok Eff. ≤ 1.00x for cost-sensitive deployments.
