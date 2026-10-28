---
title: "AI Economics: Post-Scarcity Dynamics"
type: concept
created: 2026-06-15
updated: 2026-10-26
tags:
  - economics
  - agi
  - labor-economics
  - post-scarcity
  - political-economy
aliases:
  - AGI Economics
  - Post-Scarcity Economics
  - Economics of AGI
related:
  - [[entities/alex-imas]]
  - [[entities/phil-trammell]]
  - [[entities/jyn]]
  - [[concepts/ai-policy]]
sources:
  - raw/articles/dwarkesh.com--p-alex-imas-phil-trammell--f12d8644.md
  - raw/articles/jyn.dev--rising-tide-raises-rents--0d11198c.md
  - https://www.dwarkesh.com/p/alex-imas-phil-trammell
---

# AI Economics: Post-Scarcity Dynamics

The study of economic dynamics in a world where AI progressively automates more and more tasks, potentially approaching full automation of the supply chain. Key questions: what remains scarce, how does wealth distribute, and what are the political economy implications?

## Core Framework

### The Two-Sector Model

| Sector | Description | Scarcity Driver |
|--------|-------------|-----------------|
| **Automated Sector** | Goods/services where machines handle the entire supply chain | Diminishing marginal utility — satiation |
| **Relational Sector** | Goods/services where human involvement IS the value | Intrinsic human preference for human interaction |

The central question: does the relational sector grow or shrink as a share of the economy?

### The Relational Sector (Alex Imas)

The relational sector consists of goods and services where **the fact that a human was involved is part of the product's value**. Examples:
- Live performers (ballerinas, musicians)
- Human care (therapists, doctors, tutors)
- Human-made art (valued higher than AI art in experiments, but only when unique)
- Financial advice, personal services

**Key finding**: In incentive-compatible experiments, people value human-made art prints significantly higher than AI-made ones when produced as unique items. At scale (500 copies), the human premium disappears — AI is already viewed as a commodity. The critical question: is this preference for human involvement strong enough and broad enough to sustain labor share?

### Network-Adjusted Factor Shares (Phil Trammell)

Nothing has been fully automated yet — when you look **down the supply chain**, labor is adding value at some stage. Computer/electronic products have a stable network-adjusted capital share of ~50%. The AGI threshold: goods whose network-adjusted capital share goes to 1.0 (fully automated supply chain with no human component anyone cares about).

## Key Scenarios

### Scenario 1: Full Employment (Optimistic)
- AI creates more varieties of goods than it destroys jobs
- Elasticity of demand is high enough that cheaper AI services → more spending
- Labor share stays stable (Kaldor fact continues)
- Developing countries benefit from AI technology diffusion

### Scenario 2: The Messy Middle (Moderate Risk)
- AI automates many white-collar jobs but doesn't create enough surplus for redistribution
- Workers displaced faster than new jobs are created
- Political instability from even 2-3% unemployment upticks
- **Imas's conclusion**: This scenario requires implausible economic conditions (negative growth despite expanding technological frontier). The real risk is political, not economic.

### Scenario 3: Labor Share Collapse (Pessimistic)
- New varieties of AI-produced goods expand faster than relational sector demand
- Capital owners accumulate disproportionate wealth
- Von Neumann probes / infinite-optimizers dominate resource allocation
- Labor share approaches zero

### Scenario 4: Commoditization (Electricity Model)
- AI becomes like electricity — broad utility, rents flow to users not producers
- Open-source models close the gap with frontier within 6-9 months
- Everyone gets access; the wealth distributes through the S&P index
- **Dwarkesh's position**: "AI will be much more popular and more likely to lead to broad increases in prosperity if it is as hard to capture the gains of AI as it is to capture the gains of electrification"

## Taxation and Redistribution Mechanisms

| Mechanism | Pros | Cons |
|-----------|------|------|
| **Universal Basic Income** | Immediate floor, simple | Political sustainability risk; dependence on elected officials |
| **Negative Income Tax** | Insurance from day one; scales with earnings | Same political sustainability concerns |
| **Universal Basic Capital** | Property rights; not dependent on political discretion | Targeting problem — what goes in portfolios? Indexing difficulty |
| **Wealth Tax** | Direct redistribution | Distorts investment; politically escalates over time |
| **Index Fund Approach** | Buy the AI economy's output | Requires functioning public markets for AI companies |
| **Sovereign Wealth Funds** | Country-level exposure to AI returns | Requires capital and institutional capacity |

## Rent Extraction: Why UBI Alone Fails (Jynn Nelson, Oct 2026)

Jynn Nelson's ["A rising tide raises all rents"](https://jyn.dev/rising-tide-raises-rents/) is the sharpest available critique of the UBI-first consensus in AI distribution debates, and it adds a dimension the mechanisms table above entirely omits: **the supply side of necessities**. ^[raw/articles/jyn.dev--rising-tide-raises-rents--0d11198c.md]

### The Poverty-Equilibrium / Rent-Capture Argument

Nelson starts from Eliezer Yudkowsky's observation (in "Universal Basic Income and Poverty") that a "Poverty Equilibrium" somehow survived a 100-fold productivity increase over a millennium, and Yudkowsky's admission that he does not understand why. Nelson's answer: **rent-seeking and incumbent effects**.

> A world where everyone has, say, a guaranteed minimum of 50k annual income, is a world where rental housing costs about 25k a year and the rest goes to food, utilities, transport and healthcare.

The mechanism is demand-side intervention meeting fixed supply: making food/utilities/transport/healthcare cheaper does not help in the long term, because **housing swallows an ever-increasing proportion of income**. Nelson cites **Henry George** (*Progress and Poverty*), **Enrico Moretti** (*Local Labor Markets*) and **Richard Hornbeck** as all predicting near-total capture of productivity gains by landlords and economic rent-collectors where housing supply is constrained.

This is the missing row in the mechanisms table above: UBI's failure mode is not merely "political sustainability" but **capitalisation into land rent**.

### Five Possible Worlds

Nelson's scenario taxonomy is more granular than the four scenarios above, and adds a political-collapse branch the Imas/Trammell framing lacks:

| World | Description |
|-------|-------------|
| **Status quo** | AI impact comparable to the mobile phone — culture changes, world doesn't. (Nelson considers this unlikely.) |
| **Messy transition** | Acemoglu–Restrepo **reinstatement effect** holds (NBER 2019, "Automation and New Tasks"): fewer programmers, more UI designers / sales engineers / HCI researchers. Labour loses power vs capital, inequality worsens, but people can still make rent. |
| **Reinstatement failure → plutocracy** | Jobs change faster than people retrain; a narrowing fraction of wealth goes to those who work for a living. Geopolitical analogue: countries without GPU foundries or a place in their supply chain face "a post-modern version of colonialism, mediated through markets rather than force." |
| **Butlerian Jihad** | Unchecked, the plutocracy is unstable — plutocrats automate away the labour that generates their own income. Revolution is then likely to look like Frank Herbert or *A Canticle for Leibowitz* rather than post-scarcity communism: "Indiscriminate destruction; mass pogroms; loss of human knowledge; book burnings." Nelson's point: the unemployed are angry and will not distinguish AI used for solar panels from AI used for drones. **Revolution is not inherently liberatory** — even Robespierre supported property rights. |
| **Rentier world** | Welfare extended into UBI ("bread and circuses") — people can rent enough to survive, but scarcity is everywhere and almost no one owns anything that gives them power. Explored in Marshall Brain's *Manna*. |
| **Post-scarcity world** | *Manna*'s second world: no land ownership, land and production split equally. Nelson endorses the ownership model while rejecting its constant-surveillance apparatus. |

### The Proposal: Tax Rents, Not Capital

Nelson's prescription generalises the **Land Value Tax** to all scarce, non-produced resources:

1. **LVT is an efficient tax** (no deadweight loss) precisely because land supply is fixed — landlords are already charging all tenants can afford, so a tax increase cannot be passed on. Via Lars Doucet: George's remedy captures the annual rental value of land *excluding* improvements, practically "a conventional property tax paired with a universal building exemption," and George opposed taxes on both labour and capital.
2. **Extend to other fixed-supply goods**: radio spectrum, IPv4 addresses, mineral/resource rights, utility contracts. For public property the mechanism is periodic **re-auction of the right** (not the capital built on it) — the US FCC already auctions spectrum; a losing broadcaster keeps its towers and only loses the spectrum.
3. **Cash-flow tax** generalises LVT beyond land, keeping "tax rents, deduct investment." The UK IFS formulation: tax all receipts immediately, deduct all outgoings at the same rate — at a 25% rate the government "covers 25% of the investment cost and takes 25% of the return, essentially becoming a compulsory silent partner." Consequence: *"Any project that is worthwhile before tax will be worthwhile after tax"* — and loss-making companies receive a **refund**, not merely a deduction. Nelson's MSP anecdote illustrates why this is needed: a former owner with no role in the business lives off a retained manufacturer repair authorisation, i.e. income from controlling access to a scarce good rather than from labour, risk or investment — economic rent inextricable from the genuine work performed under it.
4. **Deductions must apply to wages, not just capital investment**, otherwise the tax incentivises investment over labour.
5. **Distribute as an unconditional Citizen's Dividend** (no means-testing), tying dividends to the whole economy rather than the minimum needed to live. Precedents: Alaska Permanent Fund, Norway's oil/hydropower model (Norway already applies a cash-flow-style tax to resource-rent industries).

### Transition Engineering (the politically hard part)

Nelson is explicit that "hi could you dismantle the political machine please" will not work, because the opposition — landlords, homeowners, conglomerates, banks — derives its political power *from* the rents in question:

- **Homeowners**: defer the LVT increase until first sale, charging interest on the deferral, so fixed-income owners avoid a cost spike. Crucially this is a **one-time** deferment — unlike **California's Prop 13**, it disappears after the first sale. Goal is not to punish ownership but to stop life savings being locked in homes and unearned landlord profit. Nelson: *"I do not believe that home ownership is intrinsically good."*
- **Businesses**: the cash-flow tax discounts every investment, so raising the rate is not necessarily adverse — more up-front cash permits more risk-taking. Strongest opposition comes from low-investment, high-profit firms, i.e. precisely the rentiers. Easing in is possible: keep current profit-tax rates while adding investment deductions until the two rates match, only then raise the overall rate.
- **Open problems Nelson concedes**: the tax must be high enough that dividends cover lost work hours during transition, and there must be a way to prevent corporate relocation to low-tax jurisdictions.

### Assessment

The contribution to this page is the **supply-side rebuttal to demand-side redistribution**: UBI, negative income tax and index-fund approaches all raise purchasing power without touching who owns the fixed factors, and therefore leak into rent. Nelson's closing axioms: *"Land is different from capital. Economic rent is a curse. Economic security is freedom."*

Caveat for wiki readers: Nelson self-identifies as outside economics ("i don't know jack shit about economics") and the proposal is normative and unpriced — the cash-flow tax literature (IFS's Adam & Miller, "Full expensing and the corporation tax base") is invoked at the level of intuition, not modelling. It is best read as a well-cited argument, not a policy evaluation.

## Key Economic Concepts

### Kaldor Fact
Labor share of economic output has been ~60% for hundreds of years despite massive automation. This stability is the starting puzzle — why hasn't automation destroyed labor share historically?

### Lump-of-Labor Fallacy
The mistaken belief that there's a fixed amount of work to be done. David Ricardo predicted mass unemployment from the Industrial Revolution — instead, automation made goods cheaper, people had more money to spend on services, and employment grew.

### Elasticity of Demand
The critical parameter. If AI makes software 10× cheaper, does total spending on software go up or down? For elastic goods (software), cheaper → more consumption → more employment in complementary tasks. For inelastic goods (insulin, food), cheaper → same consumption → no employment boost.

### Jevons Paradox
As something gets cheaper, you want so much more of it that total spending increases. Famously happened with coal in Britain. The claim with AI/software: it's a good where cheaper → more consumption is structurally likely.

### O-Ring Theory of Jobs
A job is a chain of tasks where one failure destroys the whole output (like the Challenger shuttle O-ring). If AI automates 9/10 tasks but the 10th isn't automated to the same standard, you might not want to automate even the 9/10. Symmetrically: once AI handles 9/10 to superhuman standard, the human doing the last 1/10 becomes a bottleneck.

### Investment-Specific Technical Change
The price of capital goods falling relative to consumption goods. One robot now → 100 robots next year, but the price of robots halves every 18 months. Standard macro models treat output as a chimera that can be allocated 1:1 to capital or consumption — this breaks down when capital goods have their own deflationary dynamics.

## Key Figures

- [[entities/alex-imas]] — Director of AGI Economics at Google DeepMind, Professor at UChicago
- [[entities/phil-trammell]] — Head of Economics at Epoch AI, Stanford research scholar
- [[entities/dario-amodei]] — CEO of Anthropic; wrote "Policy on the AI Exponential" on AI speed vs policy response
- [[entities/dwarkesh-patel]] — Podcast host who facilitated the Imas-Trammell discussion
- [[entities/jyn]] — Jynn Nelson; compiler engineer whose "A rising tide raises all rents" supplies the Georgist / rent-capture critique of UBI above

## Related Concepts

- [[concepts/ai-policy]] — AI governance, regulation, and safety policy
- [[concepts/agentic-engineering]] — How AI changes the nature of software engineering work
- [[concepts/open-source-ai-must-win]] — Open model competition and its economic implications
- [[concepts/recursive-self-improvement]] — Technical trajectory that drives economic scenarios
