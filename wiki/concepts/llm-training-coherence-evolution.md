---
title: "LLM Training Coherence Evolution"
type: concept
created: 2026-04-24
updated: 2026-04-24
tags: [training, coherence, fine-tuning, instruction-tuning, Giles-Thomas]
aliases: ["ift-training-evolution", "llm-training-coherence"]
related: , , [[entities/gpjt]]
sources:
  - url: "https://www.gilesthomas.com/2026/04/how-an-llm-becomes-more-coherent-over-training"
    author: "Giles Thomas"
    date: "2026-04-14"
    title: "How an LLM becomes more coherent as we train it"
  - url: "https://www.gilesthomas.com/2026/04/llm-from-scratch-32l-interventions-instruction-fine-tuning-tests"
    author: "Giles Thomas"
    date: "2026-04-14"
    title: "Writing an LLM from scratch, part 32l — Interventions: updated instruction fine-tuning results"
---

# LLM Training Coherence Evolution

How an LLM's coherence and usefulness improve as training progresses, with empirical analysis from Giles Thomas's "Writing an LLM from Scratch" series.

---

## Coherence Over Training

Giles Thomas's Part 32l series tracks how an LLM becomes more coherent during training, analyzing the correlation between loss curves and IFT (Instruction Fine-Tuning) scores.

### Key Findings

**Loss-IFT Correlation**: Training loss decreases monotonically, but coherence (measured via IFT scores) improves non-linearly. Early training shows rapid loss reduction with modest coherence gains. Mid-training marks a transition point where the model begins producing structurally coherent responses.

**FineWeb-Edu Results**: The model trained on FineWeb-Edu exceeded expectations in coherence metrics. This suggests the curated quality of FineWeb-Edu provides stronger signal for coherent language modeling compared to broader web corpora.

### Coherence Milestones

| Training Phase | Loss Trend | Coherence Signal | Notes |
|---------------|-----------|------------------|-------|
| Early | Rapid decrease | Minimal | Model learns surface patterns, not structure |
| Mid | Decelerating | Emerging | Structural coherence begins |
| Late | Plateau | Strong | Useful responses emerge |
| IFT Stage | Post-training | Tunable | Usefulness optimized via interventions |

---

## Instruction Fine-Tuning (IFT) Interventions

The updated IFT results focus on **actual usefulness** rather than synthetic benchmarks. This shift reflects a broader trend in the community toward real-world evaluation.

### Intervention Types

**Prompt Interventions**: Testing how different prompt styles affect model output quality. Some phrasings elicit more coherent responses even from models with identical training.

**Response Quality Metrics**: Moving beyond perplexity-based metrics to measures of actual utility:
- Can the model solve the requested task?
- Is the output factually accurate?
- Is the format appropriate for the use case?

### IFT Evaluation Updates

Giles Thomas's updated results emphasize:
1. **Real-world task performance** over synthetic benchmarks
2. **Consistency across diverse prompts** rather than single-case optimization
3. **User-aligned outcomes** — does the model do what the user actually needs?

---

## Implications for Training Strategy

### 1. Coherence is a Training Phase, Not a Feature

Coherence emerges naturally through sufficient training on quality data. The key insight is that **loss alone doesn't predict coherence** — models can have low loss but still produce incoherent responses on novel prompts.

### 2. FineWeb-Edu Quality Advantage

The FineWeb-Edu corpus's curated nature provides better coherence signal than broader web data. This supports the trend toward high-quality, filtered training corpora over quantity-focused approaches.

### 3. IFT for Usefulness, Not Accuracy

The shift toward usefulness-focused IFT suggests:
- **Benchmark overfitting** is a real problem — models optimized for synthetic scores may fail on real tasks
- **User-centric evaluation** is critical — coherence means different things to different users
- **Intervention design** matters — how you structure fine-tuning data determines what the model learns

---

## Connection to AI Coding Reliability

These findings have direct implications for [[ai-coding-reliability]]:
- **Coherence ≠ correctness** — A model can be coherent while being wrong
- **IFT helps but doesn't solve** — Fine-tuning for coding tasks still requires human verification
- **Training data quality matters** — Code-specific fine-tuning on quality repositories should improve coding reliability

## Related Concepts
- [[concepts/ai-coding-reliability]] — Why review and verification remain essential
- [[concepts/ai-agent-traps]] — How coherence illusions create agent failures
-  — Broader IFT patterns and techniques

## Sources
- [Giles Thomas: How an LLM becomes more coherent as we train it](https://www.gilesthomas.com/2026/04/how-an-llm-becomes-more-coherent-over-training) — Empirical coherence analysis
- [Giles Thomas: Interventions: updated IFT results](https://www.gilesthomas.com/2026/04/llm-from-scratch-32l-interventions-instruction-fine-tuning-tests) — Updated usefulness-focused IFT evaluation
