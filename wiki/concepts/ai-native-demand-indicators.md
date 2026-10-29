---
title: "AI-Native Demand Indicators"
created: 2026-10-26
updated: 2026-10-26
type: concept
tags:
  - ai-economics
  - ai-industry-economics
  - economics
  - market-dynamics
  - ai-adoption
  - ai-investment
  - infrastructure
  - gpu
  - prediction
sources:
  - raw/newsletters/2026-10-25-the-signal-old-holes-new-helpers-and-ai-in-a-box.md
---

# AI-Native Demand Indicators

## Why this page exists

The AI build-out debate is mostly argued on the **supply** side (GW, GPUs, data
centres, debt) because those numbers are disclosed. The **demand** side is where the
genuinely falsifiable numbers live, and they are rarely tabulated in one place. This
page collects demand-side data points — with source, date and definition — so that
"are we overbuilding?" claims can be checked against something other than vibes.

## The demand-side numbers

### AI spend as a share of payroll (a16z portfolio, Aug–Oct 2026)

Gavin Baker (CIO/managing partner, Atreides Management) told David George on
**The a16z Show** that AI-native companies in a16z's portfolio now spend **around
10% of their payroll on AI**, while "old-economy" firms that are doing it well spend
**about 1%**.

The 10%-vs-1% gap is the load-bearing number: if spending a tenth of payroll on AI
becomes normal for competent incumbents, the current data-centre stock is nowhere
near sufficient — and that is *before* most knowledge workers start. Baker also
reported that his **own firm's AI use rose ~100-fold between March and August 2026**.

### Heavy-AI-user penetration

George's estimate (same episode): **fewer than 10 million heavy AI users today, out
of roughly 1.5 billion knowledge workers** — under 1% penetration. His conclusion:
*"we're nowhere on the demand side."*

Definitional caution: "heavy user" is undefined and is the whole ballgame. Token
usage is extremely concentrated — a small number of power users generate a large
fraction of tokens — so a penetration figure that counts *people* will understate
token concentration while overstating how much of the knowledge-worker population is
materially affected.

### Baker's supply-side position

Baker spent the summer asking AI leaders one question — *"Can you tell me one
quantitative data point in your business that's getting worse? Just one."* — and says
**nobody gave him one**. His stated worry is building **too little, not too much**:

- It is rare to find companies that can invest hundreds of billions and earn it back
  within a year — and most current spending comes from **companies' own cash rather
  than debt** (which he reads as the safer financing structure; contrast
  [[concepts/subprime-data-center-crisis]]).
- If supply cannot keep up, AI gets more expensive, producing **"compute
  inequality"** — big companies and wealthy individuals can afford frontier
  capability, everyone else cannot.

Compute inequality is a distribution claim, not an abundance claim, and it is the
policy-relevant version of the supply question: it is compatible both with plenty of
capacity for those who can pay and with severe under-supply for everyone else. See
[[concepts/token-economics]] and [[comparisons/llm-api-pricing]].

## Companion metric: financing conditions

Demand strength only converts into build-out if it can be financed. The two numbers
to watch, per the same Signal issue (Chamath Palihapitiya on All-In, and Dario
Perkins of TS Lombard):

| Indicator | Oct 2026 level / projection |
|-----------|------------------------------|
| 10-year US Treasury yield | closed **5.13%** (Oct 21) |
| Chamath's break threshold | **5.5–6%** — "any business that makes its money on a financing spread will get hurt… You're going to be roadkill" |
| New AI-company bond issuance | ~**$700B** projected for 2027 (Perkins, via CNBC) |
| US tech giants' share of new non-financial euro bonds | **~10%** (ECB, Aug 2026) — contagion channel to Europe |
| CoreWeave single-bond yield | record **15.76%** (Oct 22); CDS cost **~3×** year-to-date |

The mechanism worth naming explicitly: CoreWeave sells compute on **long fixed-price
contracts** and **borrows to buy the chips**. Rising borrowing cost shrinks margin →
lenders charge more → margin shrinks again. Demand can be real and the balance sheet
can still fail; the two are separate questions, which is why both halves of this page
matter.

## How to use these numbers

- Treat **payroll-share of AI spend** as the adoption-depth metric and **heavy-user
  penetration** as the adoption-breadth metric. They can diverge sharply.
- Demand claims without a denominator ("AI demand is insatiable") are not usable —
  ask whether the number is per-company, per-worker, or in tokens.
- When both the 10-year yield **and** AI credit spreads rise together, that is the
  signal that the financing channel — not demand — becomes binding.

## Related Pages

- [[concepts/ai-economics-post-scarcity]] — the abundance-side framing
- [[concepts/subprime-data-center-crisis]] — the debt/credit channel
- [[concepts/gpu-cluster-tco-goodput]] — supply-side cost per useful token
- [[concepts/gpu-cloud-rankings]] — Nebius publishing live spot prices as a transparency move
- [[entities/gavin-baker]] — primary source for the demand metrics above

## Sources

- [[raw/newsletters/2026-10-25-the-signal-old-holes-new-helpers-and-ai-in-a-box.md|The Signal — "Old Holes, New Helpers, and AI in a Box"]] (Alex Banks, Oct 25, 2026) — Baker/Gavin Baker a16z Show metrics, Chamath debt thresholds, CoreWeave yields, ECB euro-bond share.
- [a16z Show: Gavin Baker — Why AI demand is outrunning compute supply](https://a16z.com/podcast/gavin-baker-why-ai-demand-is-outrunning-compute-supply/)
- [CNBC: AI credit risk / debt](https://www.cnbc.com/2026-10-22/ai-credit-risk-debt.html)
- [ECB blog: US tech giants in euro bond markets](https://www.ecb.europa.eu/press/blog/date/2026/html/ecb.blog20260831~dac6a37e73.en.html)
- [Benzinga: CoreWeave bond yield record](https://www.benzinga.com/markets/bonds/26/10/62541064/coreweave-debt-stress-mounts-bond-yield-hits-record-as-stock-suffers-44-billion-wipeout)
