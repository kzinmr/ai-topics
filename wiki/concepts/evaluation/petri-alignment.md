---
title: Petri (Alignment Testing Tool)
created: 2026-05-11
updated: 2026-05-11
type: concept
tags: [anthropic, safety, alignment, evaluation, open-source]
sources: [raw/articles/2026-05-08_anthropic_petri-nla-interpretability.md]
---

# Petri (Alignment Testing Tool)

Anthropic's open-source AI safety evaluation tool. Version 3.0 released and donated to Meridian Labs (May 2026).

## Petri 3.0 Features
- **Architectural improvements**: Better adaptability, realism, and depth in evaluation scenarios
- **"Dish" add-on**: Runs tests using the model's real system prompt and scaffold — more realistic test conditions
- **Bloom integration**: Provides deeper assessments of specific model behaviors
- **Open-source**: Available for external auditing and industry-wide use

## Governance Significance
Anthropic transferred Petri's development to [[entities/meridian-labs|Meridian Labs]], an independent AI evaluation nonprofit. This is a significant governance move: in a field where **trust in the evaluator is nearly as important as trust in the evaluated model**, independence is a feature, not a footnote.

The donation ensures:
- Safety testing results are seen as **neutral and credible** industry-wide
- No single AI lab controls the evaluation tooling
- External researchers and auditors can contribute improvements

## Context
Petri is part of Anthropic's broader safety infrastructure alongside:
- [[concepts/natural-language-autoencoders|Natural Language Autoencoders]] — making model thoughts readable
- [[concepts/constitutional-ai]] — Anthropic's alignment methodology
- [[concepts/rsp|Responsible Scaling Policy]] — Risk-based deployment framework

## Related Pages
- [[entities/anthropic]] — Company overview
- [[entities/meridian-labs]] — Petri's new home
- [[concepts/security-and-governance/ai-safety]] — Safety evaluation landscape
- [[concepts/model-evaluation]] — Evaluation methodologies
- [[concepts/ai-governance]] — AI governance frameworks
