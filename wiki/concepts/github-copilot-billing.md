---
title: "GitHub Copilot Token-Based Billing"
tags: [github-copilot]
created: 2026-04-24
updated: 2026-04-24
type: concept
---

# GitHub Copilot Token-Based Billing Transition

## Overview

In April 2026, Microsoft announced a major shift in GitHub Copilot's pricing model from **requests-based billing** to **token-based billing**, alongside tightening rate limits across all tiers. This change reflects the real compute costs that AI companies have been subsidizing and marks the end of the "subsidized AI" era.

## Key Changes

### Pricing Model Transition

| Aspect | Old Model | New Model |
|--------|-----------|-----------|
| Billing Unit | Per request (interaction) | Per token consumed (input + output) |
| Cost Visibility | Fixed monthly fee | Pay per actual usage |
| Model Cost | Uniform request cost | Variable by model capability |

### Model Request Multipliers

Different models now consume requests at different rates:

| Model | Premium Request Multiplier | Impact |
|-------|---------------------------|--------|
| GPT-5.4 Mini | 0.33x | Most efficient |
| Claude Opus 4.6 | 3x | Significantly more expensive |
| **Claude Opus 4.7** | **7.5x** | Most expensive, ~250% more than Opus 4.6 |

### Rate Limits

Microsoft is tightening rate limits across all tiers:
- New signups for Copilot Pro ($10/month) and Pro+ ($39/month) individual plans are **paused**
- Student plan signups are also paused
- Free trials of paid individual plans suspended "to fight abuse"

### Model Access Changes

**Removed from Copilot Pro ($10/month):**
- Entire Anthropic Opus family

**Removed from Copilot Pro+ ($39/month):**
- Opus 4.6 Fast (retired April 10, 2026)
- Opus 4.6 and Opus 4.5 (being removed in coming weeks)
- Transitioning to Opus 4.7 only

## Financial Context

### Cost Escalation
- Week-over-week GitHub Copilot costs **nearly doubled since January 2026**
- Token-based billing has been a "top priority" for Microsoft
- Reflects actual compute costs that AI companies have been absorbing

### Industry Trend
This move follows similar actions by other AI companies:
- **Anthropic** shifted enterprise users to token-based billing
- **OpenAI, Cursor, and others** facing similar compute cost pressures

## Impact Analysis

### For Individual Developers
- Users will pay closer to **actual cost of compute**
- Premium models like Opus will be tier-gated by subscription level
- Lower-cost plans lose access to frontier models

### For AI Service Providers
- The "subsidized AI" era is ending
- Token-based pricing exposes true infrastructure costs
- Premium models become economically differentiated

## Quotes

> "The party appears to be ending for subsidized AI products."
> — Edward Zitron, Where's Your Ed At

## Related Concepts

- [[concepts/token-economics]] — LLM inference cost analysis
- [[concepts/ai-bubble-economics]] — AI service economics
- [[concepts/github-copilot-billing]] — Related GitHub Copilot coverage

## References

- [Where's Your Ed At: Exclusive Report](https://www.wheresyoured.at/news-microsoft-to-shift-github-copilot-users-to-token-based-billing-reduce-rate-limits-2/)
- [Official GitHub Blog: Changes to Copilot Plans](https://github.blog/changelog/2026-04-20-changes-to-github-copilot-plans-for-individuals/)