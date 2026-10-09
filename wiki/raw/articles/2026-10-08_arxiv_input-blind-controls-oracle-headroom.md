---
source_url: https://arxiv.org/abs/2610.10368
ingested: 2026-10-08
sha256: e4aef57c7e998495d184c281105780293ddf540deaba2a3ef8213df8d351eb10
---

# Input-Blind Controls Produce Substantial Oracle Headroom for Layer Programs in Multiple-Choice Evaluation

- **arXiv:** arXiv:2610.10368
- **Authors:** Yibei Guo, Rui Liu
- **Published:** 2026-10-07
- **Source URL:** https://arxiv.org/abs/2610.10368

## Abstract

Adaptive computation aims to improve language-model inference by tailoring execution to each input. For layer programs, oracle evaluations use known answers to estimate the potential gain from this flexibility, before a practical selector is available. However, a gain from selection does not by itself explain why the chosen programs help. This study examines this distinction using 32 layer-skipping and repetition programs on two models and 4,413 multiple-choice items. The analysis compares their gains over a fixed action selected without the evaluation prompt with those of input-blind perturbations at the same sites, re-evaluating selections on another prompt. With shared option order, the controls give 10.2-11.8 and 15.6-19.4 percentage points of headroom on Qwen3-4B-Base and Llama-3.1-8B, exceeding the real programs' 9.0 and 10.1 in all three random-direction draws per model. They match answer-change rate only, and the ordering depends on the menu: in post hoc comparisons, real programs lead on Llama's repeat-only menu in every draw. A smaller KL-calibrated comparison, including an input-dependent control, favours real programs in point estimate, with inconclusive corrected tests. Fixed letter offsets produce headroom of similar scale. Rotating options sharply reduces both families' headroom, while leaving positive real-minus-control differences of 1.4-2.3 and 3.7-4.5 points; their magnitudes and statistical support depend on further adjustments and the reference. A supplementary generated-answer test finds that search-selected programs keep a 26.0-point advantage over programs selected for other problems after rewording, without a placebo comparison. These results show that substantial headroom can persist across prompts with shared option order without establishing a benefit specific to the selected layer computation; neither ordering against these controls identifies that benefit.
