---
title: Louis Abraham
type: entity
created: 2026-08-28
updated: 2026-08-28
tags:
  - person
  - blogger
  - hn-popular
  - open-source
  - indie-maker
  - data-visualization
  - ai-commentary
sources:
  - raw/articles/claude-load-bearing-vocabulary-louis-abraham.md
---

# Louis Abraham

French open-source developer and data tinkerer (louisabraham.github.io), previously known for work on Node/Python tooling and transparency tooling (Black Hole Express, h top sites). In August 2026 his side project **[load-bearing](https://louisabraham.github.io/load-bearing/)** hit Hacker News and became a small viral reference for "AI-speak" detection.

## Load-Bearing Vocabulary Project (Aug 2026)

- Scrapes ~1,000 GitHub pull requests daily; by Aug 28, 2026: **595 days, 461,121 PRs, 51,079,244 words** analyzed.
- Method: corpus clustering — finds words statistically co-frequent with a seed term. Seed "load-bearing" is **39.47× enriched** in its cluster.
- The resulting cluster is an unmistakable **AI-assisted engineering idiolect**: *byte-identical, behavior-preserving, mutation-tested, fail-loud, tripwire, blast-radius, golden, hermetic, adversarially, falsified, ratchet, re-verified, self-heals* — proof-shaped verification rhetoric that Claude-family models produce in PR descriptions.
- Significance: an independent, quantitative lexicon for detecting LLM-authored engineering artifacts; feeds directly into [[concepts/ai-slop|AI slop]] detection and the [[concepts/coding-agents/ai-code-quality|AI code quality]] debate (see also the "load-bearing" term itself becoming a shibboleth, flagged in [[entities/simon-willison]]'s orbit).

## Related

- [[concepts/coding-agents/ai-code-quality]] — the debate the corpus evidence informs
- [[concepts/ai-slop]] — style-detection framing
- [[entities/anthropic]] — maker of the Claude family whose idiolect the cluster captures

## Sources

- "The load-bearing vocabulary of Claude" (2026-08-28) ^[raw/articles/claude-load-bearing-vocabulary-louis-abraham.md]
