---
title: "AI Subprime Crisis"
tags:
  - concept
  - ai-economics
  - ai-bubble
  - venture-capital
  - ai-subsidies
  - tech-criticism
created: 2026-04-24
updated: 2026-04-30
type: concept
aliases:
  - subprime-ai
  - ai-chain-of-pain
  - ai-subsidy-crisis
sources:
  - raw/articles/wheresyoured.at--the-subprime-ai-crisis-is-here--278f66de.md
  - https://www.wheresyoured.at/the-subprime-ai-crisis-is-here/
related:
  - entities/ed-zitron-s-where-s-your-ed-at
  - entities/ben-boyter
  - concepts/ais-economics-dont-make-sense
  - concepts/agent-harness
---

# AI Subprime Crisis

**Ed Zitron's** analysis drawing systematic parallels between the 2008 subprime mortgage crisis and the current AI industry economics. The central thesis: the entire generative AI industry is built on **unsustainable subsidies, deceptive pricing, and easy debt** — and when the subsidies end, demand may collapse.

## Key Thesis

The AI industry mirrors the 2008 housing crash through **deceptive pricing, easy debt, and inflated valuations**:

- **Teaser Rates**: AI subscriptions mask actual compute costs (token burn) behind flat monthly fees. Just as ARM mortgages hid rising rates behind introductory periods, AI subscriptions hide the reality that users burn $3–$13 in compute for every $1 of subscription revenue.
- **Universal Credit Expansion**: Subsidies span consumers, startups, and enterprises — everyone gets cheap access to unsustainable products.
- **Illusion of Value**: VC and cheap debt artificially inflate AI demand and valuations. Zitron argues **every bit of AI demand (~$65B in 2025) exists only due to subsidies** — if companies charged sustainable rates, demand would evaporate.
- **Regulatory Denial**: Industry leaders dismiss warnings about unsustainable economics, much like Ben Bernanke's 2005 claim that "there is no housing bubble."

## The AI Funding Structure

Zitron identifies a multi-layered chain with distinct players, each dependent on the layer above:

### The Funders

| Layer | Players | Economics | Risk |
|-------|---------|-----------|------|
| **Data Center Debt** | Blue Owl, MUFG, Goldman Sachs, JPMorgan, Morgan Stanley, SMBC, Deutsche Bank | $178.5B raised in US alone (2025). Per Zitron's model, many projects are unprofitable even with a paying customer. | 200GW announced, only **5GW under construction globally** — most loans on interest-only payments. |
| **Venture Capital** | Dragoneer (Anthropic, OpenAI, Perplexity), Founders Fund, a16z | Investing billions in companies that cannot be taken public (toxic finances) or acquired (no differentiation). | No liquidity mechanism. Going public reveals the ugly financial condition. |
| **Hyperscalers** | Google, Amazon, Microsoft, Meta, Oracle, NVIDIA | Rent GPUs to AI labs AND sell API access. Refuse to break out AI revenues. | Collectively need **$2T in new AI revenues by 2030** for current investments to make sense. |
| **Sovereign Wealth Funds** | GIC (Singapore) — invested in Anthropic | Long-term bets on AI dominance. | Distant time horizons mask near-term cash burn. |
| **Banks (Lines of Credit)** | Provided to both Anthropic and OpenAI | Short-term liquidity for cash-burning lab operations. | Extend the runway, not fix the economics. |

### The Dollar Flow

1. **NVIDIA** sells GPUs to data center developers (the only consistently profitable link)
2. **Data center developers** rent GPUs to AI labs and hyperscalers — at ~$42M/megawatt cost
3. **AI labs** (Anthropic, OpenAI) rent GPUs, train models, sell API access — **both lose billions**
4. **AI startups** buy API access from labs — **every single one is unprofitable**
5. **Consumers & businesses** pay monthly subs — but labs spend $3–13 per $1 of subscription

Key insight from Zitron: OpenAI made $4.3B revenue through Sept 2025 and spent **$8.67B on inference alone**. Anthropic made $5B revenue and spent **$10B on compute** to date. Neither has a path to profitability.

## The Subsidy Economy (Chain of Pain)

### How Subsidies Work

AI companies disguise the true cost of their products through opaque pricing:

| Subscription Tier | Est. Token Burn | Subsidy Ratio |
|-------------------|----------------|---------------|
| Anthropic Pro ($20/mo) | ~$100–$160 in compute | **5–8x subsidy** |
| Anthropic Max ($100/mo) | ~$300–$500+ in compute | **3–5x subsidy** |
| Anthropic Max ($200/mo) | ~$1,000–$2,500+ in compute | **5–13x subsidy** |
| ChatGPT ($20/mo) | ~$60–$160+ in compute | **3–8x subsidy** |
| ChatGPT Pro ($200/mo) | ~$1,400–$2,200+ in compute | **7–11x subsidy** |
| Cursor ($60/mo) | ~$70+ in compute** | **~1.16x (claims near-cost)** |
| Cursor ($200/mo) | ~$400+ | **2x+ subsidy** |

This is Zitron's central parallel to subprime ARMs: users were sold a product whose **real cost was hidden**, and whose **value would decay over time** as limits tightened.

### The "Subprime AI Crisis" Timeline

Zitron traces the crisis through concrete events:

| Date | Event | Significance |
|------|-------|-------------|
| Sept 2024 | Zitron first raises "Subprime AI Crisis" hypothesis | Early warning |
| June 2025 | **OpenAI & Anthropic launch priority service tiers** | First major price hike for API customers — requires up-front 3–12 month guarantees |
| July 2025 | Anthropic adds weekly limits to Claude subscriptions | Consumer subscription decay begins |
| Late 2025 | Replit shifts to "effort-based" pricing | Passes inference costs to users via credits |
| Oct 2025 | Augment Code switches to per-message pricing | Users spend $15K in tokens on $250/mo plan |
| Dec 2025 | Anthropic promotes 2x rate limits (Dec 25–31) | "Free" promotion to juice hype before Claude Code IPO push |
| Jan 5, 2026 | Anthropic "ends holiday limits" → users report 60% reduction | First major rate-limit rugpull |
| Feb 12, 2026 | Anthropic closes $30B round after Claude Code media blitz | Marketing-driven fundraising |
| Feb 18, 2026 | Anthropic bans multi-account usage, restricts Claude Code API | Further subscription degradation |
| Feb 2026 | Perplexity aggressively trims rate limits — deep research queries drop from 600/mo → 20/mo | 97% reduction |
| Mar 2026 | Anthropic "peak hours" introduced (5am–11pm PT, Mon–Fri) | Users hitting 61% session limit after **4 prompts** |
| Mar 2026 | OpenAI kills Sora (app + model), was burning $1M–$15M/day | Cost-cutting through product elimination |
| Apr 2026 | Continuous user outrage: "2–3 prompts" hits Max limit | Crisis in full swing |

### Case Studies

**Cursor** — Raised $3.36B total ($2.3B in Nov 2025 alone). $2B ARR (~$166M/mo) by Mar 2026. Forced to shift from per-request to model pricing + 20% fee. Even after changes, gives away $1 in compute per $1 on $200/mo plan. **Cursor users burned $2,192 in tokens on a $200 plan.**

**Augment Code** — Users spent $15,000 in tokens on $250/mo plan. Shifted to confusing credit-based model. Now planning to **remove auto-complete and next-edit features** — claiming developers "are no longer working primarily at the level of individual lines of code."

**Perplexity** — 600+ deep research queries/mo dropped to **20** (97% reduction). Average search limits also severely cut from 300+/day.

**Harvey** — $11B valuation on $190M ARR ($15.8M/mo). Raised $660M in 2025 alone across 3 rounds ($300M + $300M + $160M).

**MiniMax** — $79M revenue, $250.9M loss in 2025.

## Myths Debunked

Zitron forcefully rebuts common AI industry defenses:

| Myth | Rebuttal |
|------|----------|
| **"AI is like AWS"** | AWS cost ~$52B (inflation-adjusted) from 2003 to profitability. OpenAI raised $42B in 2024 alone. Anthropic raised $30B in Feb 2026. |
| **"AI is like Uber"** | Uber had minimal capex ($1.5–2.1B PP&E ever). AI labs have massive and growing capex. Uber burns marketing dollars; AI burns compute dollars. |
| **"They're profitable on inference"** | No public data supports this. Sam Altman's "stylized facts" were about hypotheticals, not real margins. |
| **"They can just raise prices"** | Users are already screaming after limits that let them burn **$10 of compute in 5 hours** on a $200/mo plan. Real pricing would be $1,300+/mo. |
| **"Token costs are going down"** | Token prices drop ≠ cost to serve them drops. New models (reasoning models) burn *more* tokens per task, increasing costs. |
| **"It's the gym model"** | Gym subscriptions decline in usage over time. Heavy AI users are the most valuable *and* most expensive — the model breaks. |

## The "Pale Horses of the AIpocalypse"

Zitron's updated warning signs (April 2026):

| Warning Sign | Current Status |
|-------------|----------------|
| AI lab price increases / service degradation | **Active** — Anthropic peak hours, Perplexity 97% cut |
| Big tech capex reduction | Watch for Q2 2026 earnings |
| AI startup price hikes / service cuts | **Active** — Cursor, Augment, Replit all affected |
| Layoffs at AI companies | Watch |
| Data center deal collapse (pre-construction) | **Warning** — only 5GW/200GW built |
| Data center collapse (mid-construction) | Watch |
| Constructed data center failure | Watch |
| CoreWeave debt raising trouble | **Active** — Lancaster PA data center issues |
| Stargate Abilene (OpenAI's flagship) failure | Watch |
| OpenAI/Anthropic IPO delays | Watch — both companies are "financial Chernobyl" |
| **Blue Owl** financial trouble | Watch — the "loosest lender in the AI bubble" |
| **SoftBank** financial trouble | Watch — raised $40B debt payable in 1 year, over-leveraged on ARM |
| ARM stock tanking (< $80) | Watch — threatens SoftBank's $15B margin loan |
| NVIDIA customer payment issues | Watch |
| NVIDIA earnings miss | Watch |

## Critical Financial Data (Expanded)

| Entity | Key Metric | Status |
|--------|------------|--------|
| OpenAI (thru Sept 2025) | $4.3B Revenue vs **$8.67B Inference Spend** | Structurally unprofitable |
| Anthropic | $5B Revenue vs **$10B+ Compute Spend** | Structurally unprofitable |
| Anthropic Total Raised | ~$46.5B+ ($16.5B in 2025, $30B in Feb 2026) | Infinite fundraising |
| OpenAI Total Raised | $42B+ in 2024 alone | Infinite fundraising |
| CoreWeave (2025) | **-6% Operating Margin, -29% Net Loss** | Negative margins |
| Cursor | $3.36B Raised, ~$2B ARR | Subsidizes $1 compute per $1 on $200 plan |
| Harvey | $200M at $11B Val, $190M ARR | High valuation, low revenue |
| MiniMax (2025) | $79M Revenue, **$250.9M Loss** | 3.2x loss/revenue ratio |
| US Data Centers | **$178.5B Debt (2025)**, 200GW announced | Only 5GW under construction |
| AI Industry Revenue | ~$65B (2025) | Entirely subsidy-dependent |
| Blue Owl | Loosest data center lender | Over-exposed to bubble |
| SoftBank | $40B debt (due in 1 year) for OpenAI stake | Precarious leverage on ARM stock |

## Key Insight: Trained Expectations

Zitron's behavioral insight: AI companies have **trained their users to expect unsustainable service levels**. A user who bought Claude Pro in Dec 2025 could burn $2,500 in tokens. By Apr 2026, the same subscription might allow $500. Users cannot predict what their subscription will be worth in 3 months.

> "These annual subscriptions amount to... a level of consumer deception that deserves legal action and regulatory involvement."

The crisis is self-reinforcing: raising prices → user anger → churn to cheaper/open models → less lab revenue → more price hikes.

## Critical Perspectives

- **[[entities/ed-zitron-s-where-s-your-ed-at|Ed Zitron]]** — Primary analyst, originated the "Subprime AI Crisis" framing in Sept 2024. Also author of "The AI Industry Is Lying to You" and "Four Horsemen of the AIpocalypse."
- **[[entities/ben-boyter|Ben Boyter]]** — Also critiques AI economics from the B2A perspective, though focuses on token efficiency for agents rather than macroeconomics.

## Graph Structure Query

```
[ai-subprime] ──author──→ [entity: ed-zitron-s-where-s-your-ed-at]
[ai-subprime] ──contrasts──→ [concept: ai-productivity-optimism]
[ai-subprime] ──relates-to──→ [concept: agent-harness]
[ai-subprime] ──relates-to──→ [concept: ai-economics]
[ai-subprime] ──warns-about──→ [entity: openai]
[ai-subprime] ──warns-about──→ [entity: anthropic]
[ai-subprime] ──warns-about──→ [entity: coreweave]
[ai-subprime] ──warns-about──→ [entity: cursor]
```

Authored by [[entities/ed-zitron-s-where-s-your-ed-at|Ed Zitron]], contrasts with mainstream AI productivity optimism, relates to the [[concepts/agent-harness]] economics (how much harness infrastructure costs) and broader AI industry financial analysis.

## Related Concepts

- [[entities/ed-zitron-s-where-s-your-ed-at]] — Ed Zitron, the primary analyst
- [[concepts/agent-harness]] — Harness economics relate to the cost structure Zitron critiques
- [[entities/ben-boyter]] — Token efficiency perspective on AI economics
- [[concepts/ai-economics]] — Broader AI industry economics

## Sources

- [The Subprime AI Crisis Is Here](https://www.wheresyoured.at/the-subprime-ai-crisis-is-here/) — Ed Zitron, Apr 2026
- [Four Horsemen of the AIpocalypse](https://www.wheresyoured.at/four-horsemen-of-the-aipocalypse/) — Ed Zitron
- [The AI Industry Is Lying to You](https://www.wheresyoured.at/the-ai-industry-is-lying-to-you/) — Ed Zitron
- [AI's Economics Don't Make Sense](https://www.wheresyoured.at/ais-economics-dont-make-sense/) — Ed Zitron (Mar 2026)
