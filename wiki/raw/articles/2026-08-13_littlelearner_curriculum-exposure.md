---
title: "LittleLearner: Language Models Under Pedagogically-Controlled Knowledge Exposure"
url: "https://littlelearner-ll.github.io/"
date: 2026-08-13
fetched_at: 2026-08-16T11:05:00+00:00
source: "littlelearner"
tags: [research, raw]
---

# LittleLearner: Language Models Under Pedagogically-Controlled Knowledge Exposure

2026-08-13

## Talk to LittleLearner

 The hosted 5B model, live in your browser.
 Open in a new tab ↗
 if the chat doesn’t load below.

## A controlled sandbox for studying how models acquire knowledge

 Modern LMs are trained on everything at once, so it is hard to tell whether a new skill
 was learned or merely elicited. We constrain the training distribution itself: an 88B-token
 corpus filtered to the U.S. elementary-school curriculum, with models trained from scratch on it and
 matched unfiltered controls.

 Dataset

### LittleCurriculum

 An 88B-token corpus distilled from FineWeb-Edu through a five-stage filtering pipeline aligned with Common Core standards (K–5).
 Concepts, facts, and vocabulary taught above Grade 5 are explicitly excluded.

 Models

### LittleLearner

 Three scales (0.6B / 1.3B / 5B) trained from scratch on LittleCurriculum: chattable models
 with an interpretable knowledge boundary. Each ships with a matched Unfiltered control
 for clean comparison.

 Findings

### Elicitation, not acquisition

 In our experiments, scaling, SFT+GRPO post-training, and in-context learning amplify what the
 curriculum taught, but none meaningfully improves out-of-scope performance, indicating that the
 pretraining filter sets the effective capability ceiling.

## Model checkpoints

 LittleLearner at three scales (0.6B / 1.3B / 5B), each with a matched Unfiltered control
 sharing its architecture, tokens, and recipe.

 Base: the pretrained model.

 GRPO: math specialists post-trained on MathCAMPS; responses may exhibit a tendency toward math-oriented output.

 Chatty: variants tuned for general chat behavior.

 Scale
 LittleLearner · K–5
 chatty
 Matched control · unfiltered

## Capability stays inside the curriculum

 Can standard interventions push a model past what its pretraining data taught it?
 With the boundary under experimental control, we can ask cleanly. In our experiments, each
 intervention amplifies in-scope ability; none of them meaningfully improves out-of-scope
 performance.

 Scaling
 Post-training
 In-context learning

### Scaling

 Scaling model size improves performance within the model’s controlled knowledge exposure and
 extends modestly to problems along the same learning trajectory, but yields little improvement on
 problems requiring more advanced capabilities outside the exposure.

 MathCAMPS accuracy by grade, across model size

### Post-training

 Post-training through GRPO significantly boosts in-scope K–5 capabilities, but fails to
 recover out-of-scope beyond-K–5 capabilities, even when training with out-of-scope data.

 Post-training amplifies K–5, not the beyond-K–5 gap

### In-context learning

 In-context learning with the prompts we test does not unlock new reasoning capabilities in
 beyond-K–5 for our trained 5B LittleLearner.

 Accuracy by prompting condition

## What will you teach it?

 Because LittleLearner’s training exposure is explicitly specified, behavioral and
 representational changes can be related directly to the concepts you introduce. Three directions
 we’re excited about:

 01
 RL & discovery

### Can RL create capability?

 The prior is restricted to K–5, so capabilities that emerge under RL can be attributed to
 the RL process itself. A tractable proxy for reward-driven discovery.

 02
 Continual learning

### Watch a concept being learned

 Introduce negative numbers and measure sample efficiency, retention, and interference. Or
 probe behavior near the boundary: does it answer, abstain, or hallucinate?

 03
 Educational science

### Machine vs. child learners

 Specified exposure enables controlled human-model comparison. Do models and children need
 similar exposure to learn fractions, or make similar errors on word problems?

 ＋
 Your turn

### Bring your own question

 A known boundary turns your idea into a clean experiment!

## If you find this work useful

 Please cite our paper:

 Copy@misc{littlelearner2026,
 title={LittleLearner: Language Models Under Pedagogically-Controlled Knowledge Exposure},
 author={Fanfei Li and Jana Zeller and Manuel Prada-Corral and Thaddäus Wiedemer and Prasanna Mayilvahanan and Ryan Cotterell and Wieland Brendel},
 year={2026},
 eprint={2608.13545},
 archivePrefix={arXiv},
 primaryClass={cs.CL},
 url={https://arxiv.org/abs/2608.13545}
}
