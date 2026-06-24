---
title: "AI Affordability Crisis"
created: 2026-06-24
updated: 2026-06-24
type: concept
tags:
  - ai-economics
  - economics
  - token-economics
  - roi
  - ai-cost
  - gpu
  - llm-inference
  - sustainability
  - ai-industry-economics
  - platform-economics
  - labor-economics
  - post-scarcity
  - wealth-distribution
  - token-billing
  - controversy
  - prediction
  - valuation
  - ai-criticism
  - journalist
sources:
  - raw/articles/2026-06-24_dshr_ai-affordability-crisis.md
---

# AI Affordability Crisis

The **AI Affordability Crisis** refers to the growing economic tension between the massive cost of providing AI inference services and the prices users are willing or able to pay. Coined and popularized by skeptics including David Rosenthal (DSHR, digital preservation blogger), Ed Zitron (independent journalist), and Sequoia Capital's David Cahn, the concept describes how AI platforms have been running a "drug-dealer's algorithm" — subsidizing usage to drive adoption, with the expectation that prices would eventually rise to sustainable levels. As of mid-2026, that expectation is increasingly in doubt.

## Core Thesis

### The Subsidy Trap

AI platforms (OpenAI, Anthropic, Microsoft/GitHub Copilot) have been operating at massive losses relative to their token pricing:

| Platform | Subscription | Tokens Burnable | Effective Subsidy Multiple |
|----------|-------------|-----------------|---------------------------|
| OpenAI (ChatGPT Pro) | $200/month | Up to $14,000 in tokens | ~70x |
| Anthropic (Claude Max) | $200/month | Up to $8,000 in tokens | ~40x |
| GitHub Copilot | $10-39/month | Unbounded (moving to metered) | Unknown |

These subsidy multiples mean a user only needs to use ~25% of their rate limit to create a negative gross margin for the provider. SemiAnalysis estimated that under current subsidy levels, all it takes is 25% rate limit utilization to achieve negative 25% gross margin.

### The "First One's Free" Model

As David Rosenthal described it, the platforms adopted the drug-dealer's strategy:
1. **Subsidize heavily**: Burn cash to make AI seem cheap or free
2. **Build dependence**: Get users and enterprises to build workflows around AI
3. **Justify investment**: Use overwhelming demand signals to raise capital
4. **Raise prices later**: Once users are locked in, charge sustainable rates

The crisis emerges because step 4 is proving extremely difficult — enterprises are pushing back on cost, open-weight alternatives are emerging, and the platforms' burn rates are accelerating faster than their paths to profitability.

## Evidence and Data Points

### OpenAI's 2025 Financials (Leaked)

The most concrete evidence came from Ed Zitron's reporting on leaked OpenAI financials:

| Metric | Value |
|--------|-------|
| Annual Revenue | $13.07 billion |
| Annual Costs | $34 billion |
| Operating Loss | $20.92 billion |
| Net Loss (attributable) | $38.53 billion |
| Sales & Marketing Spend | $5.73 billion (44% of revenue) |
| Cash Reserves | ~$25 billion (~half of $50B assets) |

The most striking number: **44% of revenue spent on sales and marketing** — an extraordinary ratio that suggests the hype machine required to sustain the AI bubble is itself incredibly expensive.

### The Cost Structure Problem

AI inference economics face several structural challenges:

1. **GPU capital costs**: Frontier models require expensive GPU clusters (H100, H200, B200) with multi-billion-dollar capital expenditures
2. **Inference energy costs**: Each token generation consumes electricity — the cost is linear with usage, unlike software with near-zero marginal cost
3. **Context window scaling**: Longer contexts (100K-1M tokens) multiply both compute and memory requirements
4. **Agent loops**: Coding agents like [[entities/codex]] and [[entities/claude-code]] generate thousands of tokens per task, with multi-turn agentic loops multiplying usage
5. **Competition for hardware**: AI labs compete with each other and with crypto miners/cloud providers for limited GPU supply

This cost structure is fundamentally different from traditional SaaS, where marginal costs approach zero. AI has **significant and persistent marginal costs** per query.

### The Pricing Transition

All major platforms have begun transitioning from flat-rate subscriptions to token-based (metered) billing:

- **GitHub Copilot** (Microsoft): Paused new signups for student/paid individual tiers. Moving to token-based billing. Week-over-week costs nearly doubled since January 2026.
- **OpenAI**: ChatGPT Pro/Team/Enterprise moving toward usage-based pricing beyond subscription tiers
- **Anthropic**: Claude Max/Team/Enterprise already token-metered; expanding scope of metered features
- **Microsoft Internal**: Reportedly canceling most Claude Code access for engineers, shifting toward Copilot CLI to control internal AI coding costs

This transition is painful for users accustomed to "unlimited" AI access at fixed monthly prices.

## The Skeptic Tradition

### David Cahn (Sequoia Capital) — 2023-2024

The earliest prominent skeptic was Sequoia Capital's David Cahn:

- **September 2023**: "AI's $200B Question" — identified a massive gap between AI infrastructure investment and revenue
- **June 2024**: "AI's $600B Question" — nine months later, the revenue gap estimate had tripled to $600 billion

Cahn wasn't an AI critic per se (Sequoia is a major AI investor), but his framing acknowledged that the math didn't add up — AI infrastructure investment was vastly outpacing AI revenue generation.

### Ed Zitron — 2025-2026

Independent journalist Ed Zitron has been the most persistent critic of AI platform economics:

- **"AI's Brokenomics"**: Published the SemiAnalysis token-burn data showing 40-70x subsidy multiples
- **OpenAI Financials Leak**: Obtained and published OpenAI's 2025 financials showing $20.92B losses on $13.07B revenue
- **"Where's Your Ed At"**: Regular newsletter documenting the gap between AI hype and economic reality
- **GitHub Copilot scoop**: Broke the story about Microsoft's internal move to token-based billing and Copilot cost crisis

Zitron's reporting is polarizing but has been consistently ahead of mainstream business press on the affordability question.

### David Rosenthal (DSHR) — 2026

David Rosenthal's blog DSHR (focused on digital preservation) has provided a distinctive perspective:

- Brings distributed systems and long-term sustainability thinking to AI economics
- Frames the crisis in terms of preservation and durability — can AI platforms survive the economic transition?
- Highlights the absurdity of marketing spend: "The hype needed to keep the AI bubble inflated is incredibly expensive"
- Curates and synthesizes reporting from Cahn, Zitron, and others into a coherent narrative

Rosenthal's June 2026 post "AI's Affordability Crisis" compiled the flood of mainstream business press coverage that had finally begun acknowledging the problem.

## The Open-Weight Escape Hatch

A key part of the affordability crisis narrative is that alternatives exist:

- **[[entities/deepseek|DeepSeek]]**: Open-weight models competitive with frontier performance at a fraction of the training cost
- **[[concepts/qwen|Qwen]]**: Alibaba's open-weight family with strong multilingual capabilities
- **[[entities/meta|Llama]]**: Meta's open-weight models enabling self-hosted inference
- **GLM 5.2**: Open-weight model closing the gap with frontier models

As commenter Michael Dale noted on DSHR's blog: "What prevents you spending that $8K a month on a Mac mini or AMD machine with half a TB of RAM and running the best open models at the cost of energy after the first month?"

This creates a ceiling on how much platforms can raise prices: if token-based pricing becomes too expensive, enterprises can switch to self-hosted open-weight models with fixed hardware costs and marginal electricity costs.

## The IPO Problem

Three major AI companies are racing toward IPO while losing tens of billions per quarter:

| Company | Status | Challenge |
|---------|--------|-----------|
| SpaceX | IPO filed | Massive losses, implausible profit path (but market doesn't seem to care) |
| [[entities/anthropic|Anthropic]] | IPO in pipeline | Needs to show path to profitability while competing on both price and capability |
| [[entities/openai|OpenAI]] | IPO in pipeline | $38.5B net loss in 2025, needs IPO capital to sustain burn rate |

The problem: going public forces transparency and demands a path to profitability. But raising prices to achieve profitability will:
- Drive users to open-weight alternatives
- Reduce demand (elasticity of demand for AI tokens is unknown but likely high)
- Invite regulatory scrutiny over market power

As Rosenthal noted: "One would think that the last thing two companies racing to IPO despite massive losses and implausible paths to profitability would want would be to engage in a 'drastic' price war."

Yet that's exactly what's happening — OpenAI and Anthropic are engaged in a feature and capability arms race that drives up costs while competing on subscription pricing.

## The "John Henry" Insight

Dan Davies contributed a key insight in his post "tokenalysis and john henry":

> "When large companies are telling their employees to be sensible and use AI tokens wisely, then the game is up. The race is over and John Henry won against the steam hammer. If you need a human being in the loop to decide on the allocation of AI tokens, then all those predictions of mass redundancy are gone."

This is a profound observation: the affordability crisis undermines the core AI narrative of mass automation replacing human workers. If AI is too expensive to use freely, humans must decide when and where to deploy it — which means humans remain in the loop, limiting the scale of labor displacement.

## Counterpoints and Caveats

The affordability crisis narrative has limitations:

1. **Model efficiency is improving**: Each generation of models delivers more capability per token — [[concepts/test-time-scaling]] and distillation reduce inference costs over time
2. **Hardware is getting cheaper**: GPU costs per FLOP decline with each hardware generation (H100 → B200 → B300)
3. **Some users derive massive value**: Enterprise users building production systems may find token costs trivial compared to the labor they replace
4. **Revenue growth is real**: OpenAI's $13B revenue, while dwarfed by costs, represents extraordinary growth from near-zero three years prior
5. **Platform economics may kick in**: If one platform achieves dominance, network effects and scale could drive costs down

However, these counterpoints don't address the fundamental math: even with efficiency improvements, the marginal cost of AI inference is non-zero and scales linearly with usage, unlike traditional software.

## Open Questions

- **Price elasticity**: What happens to AI demand when metered pricing replaces flat subscriptions? Early data from GitHub Copilot's transition will be revealing.
- **Open-weight ceiling**: How close will open-weight models get to frontier performance, and at what hardware cost? If a $10K Mac Studio can run models at 90% of frontier quality, the commercial platforms' pricing power collapses.
- **Consolidation or fragmentation**: Will the affordability crisis drive consolidation (survivors achieve economies of scale) or fragmentation (users defect to open-weight alternatives)?
- **Enterprise willingness to pay**: What is the actual value of AI coding agents, and how does it compare to their token cost when metered?
- **Regulatory intervention**: Could AI affordability become a competition/antitrust issue if dominant platforms use below-cost pricing to eliminate competitors?

## Related Pages

- [[concepts/ai-economics]] — AI Economics overview
- [[concepts/ai-economics-post-scarcity]] — Post-scarcity AI economics
- [[concepts/ai-economics-bubble-venture-capital-subprime]] — AI economics bubble analysis
- [[concepts/ai-industry-financial-sustainability]] — AI industry financial sustainability
- [[concepts/llm-inference]] — LLM inference infrastructure and costs
- [[concepts/token-economics]] — Token economics and pricing models
- [[concepts/gpu-cluster-tco-goodput]] — GPU cluster TCO and goodput analysis
- [[entities/openai]] — OpenAI company overview
- [[entities/anthropic]] — Anthropic company overview
- [[entities/deepseek]] — DeepSeek open-weight models
- [[entities/meta]] — Meta AI (Llama models)
