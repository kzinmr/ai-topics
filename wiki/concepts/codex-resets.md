---
title: "Codex Resets — OpenAI Usage Limit Reset Dynamics"
created: 2026-07-19
updated: 2026-07-19
type: concept
tags:
  - codex
  - openai
  - product
  - pricing
  - token-economics
sources:
  - raw/articles/2026-07-19_codex-resets.md
---

# Codex Resets

## Overview

Codex resets are unscheduled, no-notice replenishments of weekly usage quotas for [[entities/codex|OpenAI Codex]] and ChatGPT Work paid users. OpenAI has been aggressively resetting limits — sometimes multiple times in a 24-hour window — as part of a competitive strategy against [[entities/anthropic|Anthropic]]. The phenomenon became prominent enough that a dedicated tracking site, [codex-resets.com](https://codex-resets.com/), was created to monitor these unpredictable "miracles," as the community calls them. As of July 2026, OpenAI has bestowed 35 resets with an average interval of 8.9 days, though the longest drought stretched to 67.7 days.

## What Codex Resets Are

A Codex reset is a full replenishment of a user's weekly usage limit — effectively gifting ~$25 worth of usage for a $100/month Codex Pro plan — without prior announcement. [[concepts/codex/codex-agent-loop|Codex]] uses two quota mechanisms: a 5-hour rate limit and a weekly usage cap. Resets target the weekly cap, granting users a fresh 100% allocation.

The resets are announced via X (formerly Twitter) by Thibault Sottiaux (@thsottiaux), OpenAI's VP of Consumer, typically paired with milestone celebrations:

- **7M active users** (July 9): Banked reset introduced — users can apply the reset from desktop or web at their discretion
- **8M active users** (July 10): Full reset, 5-hour rate limit waived to allow "exploring the boundaries of GPT-5.6 Sol"
- **9M active users** (July 10, same day): Second reset in a single 24-hour period
- **Banked resets** (July 12-13): Credits that expire within 30 days; extended to 500K users; web/mobile redemption added
- **Weekend reset** (July 14 or 17): "Oops... I did it again" — another full reset for all paid users

The tracking site codex-resets.com catalogs every tweet, featuring a waiting-game visualization of the 26-week reset history and the "longest drought endured" counter (67.7 days).

## Competitive Dynamics

### OpenAI vs Anthropic Reset Schedules

The reset frequency surge is inseparable from the [[entities/anthropic|Anthropic]] competitive dynamic:

| Dimension | OpenAI (Codex) | Anthropic (Claude Code) |
|-----------|----------------|-------------------------|
| **Cadence** | Irregular, aggressive (sometimes 2x/day) | Predictable, typically Thursday/Friday |
| **User sentiment** | Excitement + fear of wasting quota | Alienation (fixed schedule frustrates users who hit limits mid-week) |
| **Rate limit policy** | 5-hour rate limit sometimes waived entirely | Standard staggered rate limiting |
| **Innovation** | Banked resets (user-controlled timing) | No equivalent |

OpenAI's strategy of frequent, unscheduled resets keeps users engaged and prevents them from switching to competitors when quotas run out. The community interpretation is that OpenAI is deliberately burning money on inference costs to capture mindshare ahead of a rumored IPO, while Anthropic's more measured cadence reflects a different growth philosophy.

The coordinated timing is notable: both companies intensified resets in July 2026 following frontier model releases (Fable 5, GPT-5.6 Sol), suggesting a broader market-share battle in the coding agent space.

## Economic Implications

### The Burn-Rate Calculus

Frequent resets represent a significant inference cost subsidy. A single global reset across 9M+ active users, each consuming up to $25 worth of compute, implies per-reset costs in the tens of millions. With 35 resets bestowed and accelerating frequency, the subsidy may run into hundreds of millions annually.

This must be contextualized against:
- OpenAI's massive CapEx (billions in GPU infrastructure)
- Pre-IPO positioning: demonstrating user growth and engagement metrics
- The [[concepts/token-economics|token economics]] reality that inference costs decline with scale and optimization

### Power User Economics

Heavy users report spending $10,000/month on API credits versus the $100-$200/month Codex Pro plan with Sol and Ultra modes. The reset subsidies make subscription plans dramatically cheaper than API usage for equivalent compute — a deliberate pricing distortion. Some users create urgency to "spin down" quota before an anticipated reset, creating behavioral patterns that benefit engagement metrics.

### Pricing Model Tensions

This dynamic intersects with broader [[concepts/outcome-based-pricing|pricing model]] debates in the AI agent industry. Subscription plans with unpredictable resets undermine the predictability that enterprise customers require, while simultaneously creating a perception of extraordinary value for individual power users. Observers note this is unsustainable as a long-term pricing strategy — resets at this frequency effectively make quotas meaningless.

## Community Reaction

The Hacker News discussion ([197 points](https://news.ycombinator.com/item?id=48963465)) captured several community perspectives:

- **"Burning money for mindshare"**: The dominant interpretation — OpenAI is subsidizing inference at a loss to lock users into the Codex ecosystem before an IPO
- **"Net dopamine deficit"**: What's intended as a gift creates anxiety about "wasting" unused quota; users set phone reminders for reset times
- **"Codex is eating the API business"**: Users migrating from $10K/month API spend to Codex Pro plans represent a revenue cannibalization risk
- **The codex-resets.com tracker itself**: The fact that a dedicated monitoring site exists and gained HN traction demonstrates how unusual and noteworthy this practice has become

The "banked resets" feature (user-controlled timing for applying a reset credit) was seen as a response to the anxiety around unpredictable timing — giving users agency over when to use their gift.

## Related Pages

- [[entities/codex]] — OpenAI Codex entity overview
- [[concepts/codex/codex-agent-loop]] — Codex agent architecture and operation
- [[entities/openai]] — OpenAI entity page
- [[entities/anthropic]] — Anthropic entity page
- [[concepts/token-economics]] — LLM inference cost economics
- [[concepts/outcome-based-pricing]] — Pricing models for AI agents
- [[concepts/agent-quota-resets]] — Broader concept of agent quota reset dynamics
- [[concepts/codex/codex-superapp]] — Codex superapp positioning
