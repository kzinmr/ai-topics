---
title: "Out-of-Domain Finetuning to Bootstrap Hallucination Detection"
source: "https://eugeneyan.com/writing/finetuning/"
author: "Eugene Yan"
date: 2024-05-20
tags: [fine-tuning, hallucination, NLI, evaluation, factual-consistency, bootstrapping]
---

# Out-of-Domain Finetuning to Bootstrap Hallucination Detection

By **Eugene Yan** — Explores how to improve factual inconsistency (hallucination) detection by bootstrapping with out-of-domain data. Core finding: pre-finetuning on Wikipedia data significantly enhances a model's ability to detect hallucinations in News summaries.

---

## Core Methodology: NLI for Hallucination Detection

Hallucination detection treated as **Natural Language Inference (NLI)** task:
- **Premise:** The source document
- **Hypothesis:** The generated summary
- **Goal:** Predict if hypothesis is *entailed by*, *neutral to*, or *contradicts* the premise. Contradiction = hallucination.

**Model:** BART variant fine-tuned on MNLI dataset. Drop "neutral" dimension, softmax on remaining "contradiction" and "entailment" logits.

```python
def get_prob_of_contradiction(logits):
    # Drop neutral logit (index=1), softmax, get prob of contradiction (index=0)
    prob = F.softmax(logits[:, [0, 2]], dim=1)[:, 0]
    return prob
```

---

## Experiment: FIB vs. USB Datasets

### Factual Inconsistency Benchmark (FIB)
- **Domain:** News (CNN/Daily Mail and XSUM)
- **Structure:** Pairs of summaries (one consistent, one inconsistent) per article
- **Challenge:** Inconsistent summaries use source words but phrase them incorrectly

### Unified Summarization Benchmark (USB)
- **Domain:** Wikipedia
- **Structure:** Labels based on edits to summary sentences
- **Caveat:** Dataset is "noisy"; some "inconsistent" labels are grammatical/formatting corrections, not factual errors

---

## Results

| Training Stage | PR AUC | Recall (@0.8) | Precision (@0.8) |
|:---|---:|:---:|:---:|
| **Non-finetuned** | 0.56 | Low | Low |
| **Finetuned on FIB only (10 epochs)** | 0.69 | 0.02 | 0.67 |
| **USB (3 epochs) + FIB (10 epochs)** | **0.85** | **0.50** | **0.91** |

### Key Insights
- **Hidden learning:** Finetuning on USB alone didn't improve FIB scores, but prepared the model to learn much more effectively from FIB data
- **Production readiness:** Combined approach enabled reliable classification threshold (0.8) that wasn't possible otherwise
- **25x recall boost:** At 0.8 threshold, bootstrapped model increased recall from 0.02 to 0.50

---

## Key Takeaways
1. **Bootstrap with out-of-domain data:** Use permissive open-source datasets (Wikipedia/USB) to improve target domain (News/FIB) performance
2. **Transfer learning beyond pretraining:** Transfer learning is highly effective during fine-tuning stage, not just initial pretraining
3. **Data blending:** Sequential stages used for clarity; blending into single stage would likely yield similar benefits

> "We may not need to collect as much finetuning data for our tasks if there are open-source, permissive-use datasets that are somewhat related."

## Resources
- **Code:** [visualizing-finetunes GitHub](https://github.com/eugeneyan/visualizing-finetunes)
- **Model Technique:** QLoRA used for experiments
