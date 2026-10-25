---
title: "LLM Citation Seeding"
type: concept
created: 2026-10-24
updated: 2026-10-24
tags:
  - llm-citation-seeding
  - disinformation
  - factuality
  - agentic-search
  - agentic-retrieval
  - information-retrieval
sources:
  - https://peec.ai/blog/publish-fake-stats-get-cited-the-tactic-that-put-my-data-all-over-the-web
  - raw/articles/2026-10-22_peec-publish-fake-stats-get-cited.md
related_concepts:
  - ai-search-visibility
  - ai-slop
---

# LLM Citation Seeding

**LLM citation seeding** is the deliberate creation of content whose only purpose is to be retrieved and cited by LLM answer engines — and the demonstration that *fabricated* content can be seeded successfully. The term names both the GEO (generative engine optimization) tactic and the attack surface it exposes: LLMs preferentially hunt for **statistics** when writing, so a site that publishes statistics gets cited regardless of whether the numbers are real.

The canonical evidence is a 2026 experiment by Peec AI's GEO research team: a brand-new domain (`stateglobe.com`) populated with **50,000 entirely invented statistics**, generated in one day with GPT-4.1 for roughly **$50** total ($30 for the stats pages + $20 for 15,000 listicles). None of the numbers was ever checked.

**▶ One-line summary**: 50,000 fake stats on a $50 domain, buried by Google, still cited 7 months on by ChatGPT — and laundered into an academic paper and bank investment research.

## The experiment and its numbers

| Signal | Result after ~7 months |
|---|---|
| Google visibility | Collapsed after two core updates; effectively deindexed, 5–20 impressions/day |
| ChatGPT retrieval | **10,000+ sessions** referred via GA4; **~72,000 ChatGPT-User** fetches in 30 days (the real-time answer agent, not a training crawl) |
| Total bot traffic | 600,000+ requests in 30 days (Cloudflare logs) |
| Inbound links | **330+ referring domains**, including Shopify, Bluehost, DHL |
| High-authority laundering | Cited in an **academic paper**, in **investment research by Qatar's largest financial group**, in an Indian economics publication, in a Canadian influencer-community research report |

The control condition matters: Peec later published a second statistics page with **real, sourced numbers**. Sites suspected of AI-written content began linking to it almost immediately as well — so the link-earning mechanism is "publish statistics," not "publish fake statistics."

## Mechanism: citation laundering

The authors' central concept. On day one a fake number on a new domain has **zero authority**. Then:

1. An LLM retrieves it while filling a statistics gap in an answer.
2. A human pastes the answer into a deck, or publishes it — the number now has a source.
3. An academic paper cites it. A bank cites it.
4. The next retriever (human or model) encounters a statistic *with* a source, and that source is cited by serious institutions.

The data never became true; **each citation only raised its apparent trustworthiness**. The authors flag a terminal escalation: after enough retrieval and citation, the pages enter web crawls, and web crawls enter training data — a GPT-4.1 guess can become something the next model "knows."

## Why Google and ChatGPT diverged

Two different trust pipelines, two different outcomes from the same site:

- **Google** applied quality signals at the page/domain level and buried the site within weeks.
- **ChatGPT** kept fetching it because the retrieval need (a statistic for a real question) was satisfied, and the ChatGPT index does not inherit Google's demotion.

The practical implication is that **deindexing is not cleanup**. A site can be dead to search and alive in answer engines indefinitely. (Cross-reference: [[concepts/ai-search-visibility]], where the Trelly audit found ~51% of answer-engine citations resolve to non-independent editorial coverage.)

## Limitations

- **Single self-interested source.** The experiment was run and reported by a GEO vendor whose product sells answer-engine visibility; it publishes no reproducible dataset or crawl corpus.
- **Correlation with authority is unverified.** The "cited by Shopify/DHL/academic paper" claims rest on Ahrefs/Semrush link counts plus screenshots the authors chose to show; none was independently audited.
- **Confounds with notability.** The site went viral in marketing newsletters (Growth Memo) after launch, so some ChatGPT retrieval and most referring links may be artefacts of publicity rather than of the seeding itself.
- **Prompt-shaped outcome.** "Statistics" is one content genre; the experiment does not establish that LLMs equally favour fabricated claims in other genres.

## Related

- [[concepts/ai-search-visibility]] — audit of where answer-engine citations actually come from
- [[concepts/ai-slop]] — AI-generated content flooding the web, and the corpus LLMs retrieve from
- [[concepts/model-collapse-of-viewpoints]] — convergence of model output toward corpus clichés
- [[concepts/agentic-search]] — the retrieval agents whose citation behaviour this exploits

## Sources

- [What I learned about AI search when I made up 50,000 stats that got cited by ChatGPT — Peec AI](https://peec.ai/blog/publish-fake-stats-get-cited-the-tactic-that-put-my-data-all-over-the-web) (raw: `raw/articles/2026-10-22_peec-publish-fake-stats-get-cited.md`)
