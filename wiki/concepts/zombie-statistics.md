---
title: "Zombie Statistics — AI-Quoted Numbers Without Studies"
created: 2026-10-30
updated: 2026-10-30
type: concept
tags: [zombie-statistics, hallucinations, factuality, llm-citation-seeding, information-ecosystem, ai-slop]
confidence: medium
sources:
  - raw/articles/trakkr.ai--zombie-stats--f1c32803.md
  - "https://news.ycombinator.com/item?id=50290283"
related:
  - "[[concepts/llm-citation-seeding]]"
  - "[[concepts/ai-hallucination-factuality]]"
  - "[[concepts/ai-slop]]"
  - "[[concepts/zombie-internet]]"
---

# Zombie Statistics — AI-Quoted Numbers Without Studies

Trakkr Research study #013 (Mack Grenfell, 2026-10-28, HN 167pts): asked **ChatGPT, Perplexity, Gemini, Claude and Google AI Overviews** 200 everyday number-questions, then followed **1,285 quoted statistics** back to their sources. **Fewer than half led to a study that says the same thing.**

## Trail outcomes (1,285 traced statistics)

| Outcome | Share |
|---|---|
| Sourced — study found, says the same thing | **40%** |
| Changed — study found but number/population/date differs | 8% |
| Can't check — named source doesn't contain the number, or is paywalled/gone | 40% |
| Nowhere — no study anywhere on the trail | **11%** |

The canonical example: *"44% of salespeople give up after just one follow-up attempt"* — quoted identically by all five assistants, with **no study behind it at all**. Numbers also drift between assistants on the same question (e.g. "paycheck to paycheck" 48%–59%, "small businesses with a website" 73%–83%).

Trakkr also audited **52,930 Google AI Overviews answers** (Sep 25 – Oct 25 2026): 4.4% carried a statistic; 300 traced by hand showed the same ~40%-sourced profile.

## Assessment

- Single-source study by a commercial AI-visibility vendor (Trakkr sells "get cited by AI" tooling), so the incentive runs toward finding citation failures; the methodology is published with per-statistic trails, and the 11% "Nowhere" + 40% "Can't check" split is consistent with prior link-rot literature.
- Distinct from classic hallucination: the numbers usually **originate in listicle/aggregator pages** that cite nothing — the model faithfully reproduces a number that was never sourced. The failure lives in the information ecosystem, which is where the remedy (follow the citation twice, treat stats as leads rather than sources) lands.

## Related

- [[concepts/llm-citation-seeding]] — the marketing response: seeding content so LLMs cite you
- [[concepts/ai-hallucination-factuality]] — neighboring failure class (fabricated vs. faithfully-propagated-unsourced)
- [[concepts/zombie-internet]] — AI-generated content feeding AI answers
- [[concepts/ai-slop]] — listicle farms as the breeding substrate
