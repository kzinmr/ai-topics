---
title: "The Scaling Hypothesis"
author: Gwern Branwen
url: https://gwern.net/scaling-hypothesis
published: 2020-05-28
updated: 2022-01-02
source: gwern.net
type: essay
tags:
  - scaling-hypothesis
  - scaling-laws
  - gpt-3
  - meta-learning
  - emergent-agency
  - bitter-lesson
  - gwern
---

# The Scaling Hypothesis

Gwern Branwen's seminal 2020 essay that formalized the Scaling Hypothesis — the theory that the "secret" to AGI is not complex, hand-crafted algorithms, but rather simple neural architectures applied to diverse data at massive scales.

## Summary

The Scaling Hypothesis posits that intelligence is an emergent property of simple neural units and learning algorithms when applied to diverse experiences at massive scale. GPT-3 (175B parameters, released May 2020) served as the primary proof of concept, demonstrating that increasing parameters from GPT-2 (1.5B) did not hit diminishing returns.

### Key Arguments

1. **Meta-Learning**: GPT-3 learned how to learn — it can follow directions and perform new tasks from a few examples without weight updates (in-context learning).

2. **Hardware Overhang**: GPT-3 was trained on an "obsolete" 2018 architecture. Its success suggests we are limited by organizational conviction to scale, not hardware.

3. **The "Last Bits" Theory**: The final decrements in prediction error are the most "intelligent." For a language model, "the truth is that which keeps on predicting well — because truth is one and error many."

4. **Emergent Agency ("It From Byte")**: Agency is an emergent property of modeling complex data. "A sufficiently accurate simulation of an agent just is an agent."

5. **Neural Nets are "Lazy"**: They will use shortcuts (memorization) if the problem is too easy. Massive data forces them to learn abstract "algorithms" because memorizing every possible combination becomes more "expensive" than learning the underlying rule.

### Strong vs Weak Scaling Hypothesis

- **Strong Scaling Hypothesis**: Once we find a scalable architecture (like self-attention or convolutions), we can simply train ever larger NNs and ever more sophisticated behavior will emerge naturally.
- **Weak Scaling Hypothesis** (DeepMind's view): AGI requires finding the right algorithms piece by piece; scale helps but is not sufficient.

### Prospects

Gwern extrapolated GPT-3's scaling curve, estimating ~2.2 million × the compute of GPT-3 would reach human parity, and calculated this would be feasible by ~2027 (assuming compute doubling every 3.4 months) or by ~2038 (assuming algorithmic efficiency halves costs every 16 months).

### Critiquing the Critics

Gwern critiques mainstream AI researchers for:
- Dismissing scaling as "brute force"
- Having no coherent model of AI progress
- Making falsified predictions without reflection
- Speaking with "the voice of authority" rather than making quantifiable predictions

### Core Architecture

- **Strong vs. weak scaling**: Gwern distinguishes OpenAI's belief (scale alone drives improvement) from DeepMind's approach (right algorithms still needed)
- **Why pretraining works**: The pretraining thesis — as models eliminate surface-level prediction errors, they must eventually learn true reasoning/causality to continue improving
- **The ensemble effect**: Large models act as ensembles of sub-networks, enabling Occam's razor effect where simple generalizable solutions beat overfit ones

## Structure of the Essay

1. **Meta-Learning** — How GPT-3's attention mechanisms serve as "fast weights" that learned to learn
2. **Flexing GPT** — Demonstrations of GPT-3's capabilities despite obsolete architecture
3. **Baking The Cake** — GPT-3 as part of AGI, not the whole picture
4. **Scaling** — Scaling curves and why they haven't bent
   - Blessings of Scale
   - Scaling Hypothesis (strong vs weak)
5. **Why Does Pretraining Work?** — The pretraining thesis and "last bits" theory
6. **Prospects** — Hardware overhang, organizational conviction, OpenAI vs DeepMind
7. **Critiquing The Critics** — Voice of authority, failure to learn from falsified predictions
8. **Appendix: It From Byte** — Emergent agency from non-agentic data
   - All Is Atoms & Void
   - Intentional Interpretive Stance
   - Ambient Agency
