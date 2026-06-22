---
title: "AI Doesn't Have ROI"
type: concept
created: 2026-06-15
updated: 2026-06-15
tags:
  - economics
  - roi
  - ai-cost
  - company
  - ai-adoption
  - token-billing
aliases:
  - AI ROI Problem
  - AI Cost Measurement
related:
  - [[entities/ed-zitron]]
  - [[concepts/ai-economics-post-scarcity]]
  - [[concepts/ai-agent-engineering]]
sources:
  - raw/articles/wheresyoured.at--ai-doesnt-have-roi--02bc55ce.md
  - https://www.wheresyoured.at/ai-doesnt-have-roi/
---

# AI Doesn't Have ROI

A framework articulated by [[entities/ed-zitron]] in June 2026 arguing that the AI industry faces a fundamental measurement problem: **neither the cost nor the return of AI can be reliably quantified**, making traditional ROI analysis impossible.

## The Measurement Problem

### Why AI Costs Can't Be Measured

1. **Token billing opacity**: AI subscriptions hide true per-prompt costs behind flat-rate subscriptions ($20-$200/month), conditioning users to ignore the real cost of each interaction
2. **Hallucination uncertainty**: Every interaction can go wrong in unpredictable ways, making the expected cost of a "completed task" impossible to calculate
3. **Variable token consumption**: Different prompts, contexts, and model behaviors consume wildly different amounts of tokens for the same nominal task
4. **No standard unit of work**: Unlike traditional software (where a "transaction" or "query" is well-defined), AI interactions vary in complexity and output quality

### Why AI Returns Can't Be Measured

1. **Quality variability**: The same AI task produces different outputs each time, making output value hard to standardize
2. **Human oversight cost**: AI requires "eternal vigilance" — humans must constantly verify outputs, adding hidden labor costs
3. **Error cost asymmetry**: A single catastrophic AI error can destroy value far exceeding the savings from automation
4. **No baseline comparison**: For novel tasks that AI enables, there's no pre-AI baseline to compare against

## Enterprise Impact (June 2026)

### GitHub Copilot Token Billing Crisis

Microsoft moved all GitHub Copilot customers from premium request-based billing to **token-based billing** in Q1 2026. Immediate consequences:
- Users burning 50% of monthly credits in a single prompt
- 31-60% credit consumption in just a few prompts or hours
- Enterprise customers who had been conditioned to think of AI as "unlimited" suddenly facing real cost constraints
- Walmart setting token limits on internal "Code Puppy" AI tool
- Amazon VP telling employees "don't use AI just for the sake of using AI"

### Industry-Wide Cost Obfuscation

Ed Zitron documents that **every AI subscription service** operates on subsidized economics:
- Anthropic: $8-$13.50 in token costs for every $1 of subscription revenue
- OpenAI: Similar subsidy structure
- AI startups: Literally sending every VC dollar directly to inference costs
- The subsidy model worked while growth was the priority, but breaks at enterprise scale

## The "Cost of Intelligence" Paradox

While per-token costs of models are decreasing, **total cost per task is increasing** because models use far more tokens for the same work:
- "Imagine if gas got cheaper but the distance to your destination kept getting longer"
- Extended thinking, tool use, and multi-step reasoning dramatically increase token consumption
- The cost of a single complex task can exceed a month's subscription fee

## Connection to AI Economics

This connects to the broader [[concepts/ai-economics-post-scarcity]] discussion: if enterprises can't measure AI ROI, they can't make rational investment decisions. The current AI spending boom is based on **strategic FOMO** rather than measurable returns.

## Key Quotes

> "If you can't measure how good something is, how much it might cost, or what your return on investment might be, it's fair to ask why you're even paying for it in the first place."
> — Ed Zitron, June 2026

> "AI labs may be able to run their own infrastructure and save some costs, but we have no evidence that this makes anything 'profitable.'"
> — Ed Zitron, June 2026
