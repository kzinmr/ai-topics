---
title: "Kimi K2.7-Code"
created: 2026-06-13
updated: 2026-06-18
type: concept
tags:
  - kimi
  - moonshot
  - code-model
  - coding-agents
  - reasoning
  - token-economics
  - open-source
  - model
  - open-weight
  - inference
sources: [raw/articles/2026-06-13_fireworks-ai_kimi-k2p7-code.md, raw/articles/together.ai--blog-kimi-k2-7-code-vs-claude-fable-5--42700c0e.md]
---

# Kimi K2.7-Code

## Overview

Kimi K2.7-Code is an open-weight coding model released by [[entities/moonshot-ai|Moonshot AI]] on June 12, 2026. It is the latest iteration in the Kimi K2 line, purpose-built for long-horizon agentic coding tasks. The model was launched with day-0 availability on Fireworks AI serverless inference.

K2.7-Code's defining innovation is **token efficiency**: it uses roughly 30% fewer reasoning tokens than [[concepts/kimi-k2-6|Kimi K2.6]] while scoring significantly higher on coding benchmarks, translating to meaningfully lower cost per completed agentic task.

## Architecture

K2.7-Code shares the same architectural foundation as the rest of the K2 family:

| Specification | Value |
|--------------|-------|
| Total Parameters | ~1T |
| Active Parameters | 32B per token |
| Architecture | Mixture of Experts (MoE) |
| Context Window | 256K tokens |
| Optimization | Long-horizon agentic coding |

The 1T/32B MoE design means the model activates only 32 billion parameters per forward pass, enabling efficient inference while drawing on a much larger total capacity.

## Token Efficiency: The 30% Reduction

The headline metric for K2.7-Code is not a benchmark score but a behavioral improvement: it produces **roughly 30% fewer reasoning tokens** than K2.6 while achieving higher accuracy. This inverts the usual tradeoff where higher scores come at the cost of longer chains of thought.

### Why Fewer Reasoning Tokens Matters

In the era of coding agents, token economics shift fundamentally from per-token cost to per-task cost:

- **Context compounding**: Each turn's reasoning tokens become input context for every subsequent turn. Verbose reasoning from turn 3 is re-read on turn 4, 5, 6, and beyond — you pay to write those tokens once but to read them back dozens of times.
- **Faster loops**: Shorter reasoning chains mean each agent loop completes faster, reducing wall-clock time for the entire task.
- **Fewer retries**: More focused reasoning chains tend to produce fewer dead ends, retries, and circular loops that silently inflate cost.

A 30% reduction in reasoning tokens is therefore worth more than a 30% price cut. A price cut applies once, per token. Token discipline applies across the entire trajectory: shorter generations, smaller context on every subsequent turn, faster loops, and fewer retries.

This shift in perspective — from **per-token rate cards** to **cost per completed task** — is central to understanding K2.7-Code's value proposition. For more on this paradigm, see [[concepts/token-economics|token-economics]].

## Benchmark Performance

Despite using fewer reasoning tokens, K2.7-Code posts solid gains across coding evaluations compared to K2.6:

| Benchmark | Improvement vs. K2.6 |
|-----------|---------------------:|
| Kimi Code Bench v2 | +21.8% |
| Program Bench | +11.0% |
| MLS Bench Lite | +31.5% |

These gains demonstrate that token efficiency need not come at the expense of capability — the model reasons more concisely and more accurately.

## Pricing & Serving

K2.7-Code pricing matches Moonshot's public API rates:

| Token Type | Price per 1M Tokens |
|-----------|-------------------:|
| Input | $0.95 |
| Output | $4.00 |
| Cache Hits | $0.19 |

On Fireworks AI, the model is available with three serving tiers designed for bursty agentic traffic:

- **Standard** — Elastic, pay-per-token default. All existing API calls work without modification.
- **Priority** — For traffic that cannot tolerate shedding during peak congestion. Requests receive stronger admission control on the shared fleet at roughly **1.5×** Standard pricing. The knob here is reliability, not speed.
- **Fast** — A dedicated high-throughput serving path running the same weights at **100+ generated tokens per second**, at roughly **2×** Standard pricing. Accessed via a dedicated Fast model ID. Fast is the compounding play with K2.7-Code's shorter reasoning chains, though it was not yet available at launch.

Model ID: `accounts/fireworks/models/kimi-k2p7-code`

## Comparison to K2.6 and Other Coding Models

K2.7-Code differs from [[concepts/kimi-k2-5|Kimi K2.5]] and K2.6 not in architecture but in optimization focus. While K2.5 and K2.6 emphasized benchmark leadership and multimodal capability, K2.7-Code is explicitly tuned for **agentic code generation economics** — making long-horizon coding agents cheaper and faster to run, not just scoring higher in isolation.

The key competitive insight: K2.7-Code's rate card is nearly identical to K2.6's, but its **cost per finished task is meaningfully lower** due to the token efficiency gains. In an ecosystem where coding agents routinely consume billions of tokens per day across parallel tasks, this efficiency compounds rapidly.

## Cost Comparison: Together AI Experiment (June 2026)

Together AI ran an empirical comparison between Kimi K2.7 Code and Claude Fable 5 for landing page generation:

- **Cost advantage**: Kimi K2.7 Code cost ~94% less than Claude Fable 5 (~16x cheaper on average)
- **Specific example**: B2B SaaS landing page cost $0.04 with Kimi vs $1.09 with Claude Fable (~27x cheaper)
- **Quality gap**: Claude Fable scored higher on GPT-5.5-judged rubric, but Kimi remained competitive on design, structure, and page quality
- **Design MCP server pattern**: Biggest quality improvement came from providing Kimi with visual inspiration via a custom MCP server containing screenshots of well-designed landing pages
- **100-page scenario**: Generating 100 pages would save ~$94 with Kimi vs Fable
- Source: raw/articles/together.ai--blog-kimi-k2-7-code-vs-claude-fable-5--42700c0e.md

## Related Pages

- [[concepts/kimi-k2-6|Kimi K2.6]] — Previous generation (April 2026)
- [[concepts/kimi-k2-5|Kimi K2.5]] — Earlier K2 family model (January 2026)
- [[entities/moonshot-ai|Moonshot AI]] — Organization behind the Kimi model line
- [[concepts/token-economics|Token Economics]] — The per-token vs. per-task cost paradigm
