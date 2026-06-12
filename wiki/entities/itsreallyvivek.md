---
title: "Vivek (@itsreallyvivek)"
type: entity
created: 2026-06-08
updated: 2026-06-08
tags:
  - person
  - educator
  - rlhf
  - alignment
  - x-account
aliases:
  - itsreallyvivek
  - Vivek
sources:
  - https://x.com/itsreallyvivek
  - raw/articles/2026-06-07_itsreallyvivek_rlhf-what-every-programmer-should-know.md
related:
  - "[[concepts/post-training/rlhf]]"
---

# Vivek (@itsreallyvivek)

Vivek is an AI educator and X/Twitter writer who authors deep-dive technical explanations of AI alignment concepts. Their writing style focuses on building intuition from first principles with concrete examples and mathematical grounding.

## Key Work

### "What every programmer should know about RLHF" (Jun 2026)

A comprehensive, ground-up guide to Reinforcement Learning from Human Feedback. Covers:

- **The RLHF pipeline**: SFT → Reward Model Training → PPO loop
- **Bradley-Terry preference modeling** with full mathematical derivation
- **KL penalty rationale** — why the "leash" prevents reward hacking, explained via actor-critic metaphor
- **Failure modes**: reward hacking, distributional shift, labeler bias
- **Post-RLHF landscape**: DPO, Constitutional AI, RLAIF
- **Philosophical point**: measured preferences vs actual values vs what's genuinely good

The article distills the concept to its essence: "A human preference turned into a scalar, turned into a gradient, turned into a behavior you interact with every day."

Next in series: DPO explained from scratch.

## Writing Style

- First-principles approach with concrete labeling examples
- Mathematical grounding (formulas included inline)
- Metaphor-based explanations (actor-critic, taste, leash)
- Direct, pedagogical voice

## Cross-References

- [[concepts/post-training/rlhf]] — The concept page enriched from this article
- [[concepts/dpo]] — Next article in series (announced)
