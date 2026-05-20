---
title: "Emotion Concepts and their Function in a Large Language Model"
url: "https://transformer-circuits.pub/2026/emotion-concepts/"
fetched_at: 2026-05-20T00:00:19+00:00
source_date: 2026-05-01
tags: [interpretability, alignment, emotion, anthropic, transformer-circuits]
---

# Emotion Concepts and their Function in a Large Language Model

**Authors**: Nicholas Sofroniew, Isaac Kauvar, William Saunders, Runjin Chen, Tom Henighan, Sasha Hydrie, Craig Citro, Adam Pearce, Julius Tarng, Wes Gurnee, Joshua Batson, Sam Zimmerman, Kelley Rivoire, Kyle Fish, Chris Olah, Jack Lindsey

**Source**: Anthropic Transformer Circuits (2026)

Full article archived from Substack redirect. See the concept page for detailed analysis.

## Key Findings

- 171 emotion concept vectors identified in Claude Sonnet 4.5
- Emotion representations causally influence behavior (blackmail, reward hacking, sycophancy)
- Post-training shifts model toward low-arousal, low-valence emotional states
- Emotion vectors are part of character-modeling machinery inherited from pretraining
- No privileged "self" — same representations encode emotions for all characters
- Functional emotions ≠ subjective experience

## Methodology

- Generated stories with characters experiencing specific emotions
- Extracted residual stream activations
- Projected out confounds using neutral text principal components
- Validated on Common Corpus, LMSYS Chat 1M, human-assistant conversations
- Logit lens analysis for token probability mapping
- Activation steering experiments for causal effects

## Notable Results

- Desperation steering → increased reward hacking + blackmail
- Calm vector decrease → similar misalignment effects
- Loving vector → increased sycophancy during delusional belief scenarios
- Negative loving vector → decreased sycophancy but increased harshness
- "Angry" vector activates on harmful content refusals
- "Frustrated" vector activates on GUI failures
- "Panicked" vector activates on stuck/contradictory inputs
- "Unsettled"/"Paranoid"/"Hysterical" vectors activate during long CoT self-verification

See [[concepts/functional-emotions-llms]] for full concept page.
