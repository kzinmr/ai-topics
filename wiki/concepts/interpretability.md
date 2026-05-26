---
title: "Interpretability (LLM)"
type: concept
aliases:
  - mechanisitic interpretability
  - AI interpretability
created: 2026-05-08
updated: 2026-05-08
tags:
  - interpretability
  - model
  - agent-safety
related:
  - concepts/activation-steering
  - concepts/monosemanticity
  - concepts/rlhf
  - concepts/abliteration
  - entities/anthropic
  - entities/thariq-shihipar
sources:
  - raw/articles/thariq-shihipar-interpretability
  - https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html
  - https://www.anthropic.com/news/golden-gate-claude
  - https://thesephist.com/posts/prism/
---
# Interpretability (LLM)

**Interpretability** is a research field that seeks to understand "what is happening" inside an LLM. It aims to visualize what models are "thinking" and explain it in terms of concrete features and circuits.

> **In a word**: The endeavor to open the LLM's black box and see the gears inside.

## Background: Why Interpretability

As LLM performance improves exponentially, the inability to explain "why the model produced that output" has become the biggest bottleneck for safety and reliability. Even when prompts produce desired outputs, what is actually happening inside the model remains unknown.

As [[concepts/scaling-hypothesis]] shows, the more capable models become, the more human-designed "structure" disappears, and internal explainability decreases. Interpretability research is a direct attempt to confront this **trade-off between performance and controllability**.

## Major Approaches

### Feature Extraction
Decomposes LLM's internal representations (activations) into "features." Each feature corresponds to a specific concept (e.g., "Golden Gate Bridge," "Arabic," "spam email").

- Anthropic's Sparse Autoencoder (SAE) feature decomposition is representative
- Extracts millions of features, labels what each represents
- The same features reliably activate for the same inputs

### Circuit Analysis
Tracks how multiple features connect and interact. Identifies the "computational circuits" behind specific capabilities (mathematical reasoning, code generation, etc.).

### Activation Steering → [[concepts/activation-steering]]
A technique to control model behavior by manipulating the activation strength of specific features. An application of interpretability moving from "understanding" to "controlling."

## Landmarks

| Year | Achievement | Significance |
|----|------|------|
| 2023 | Anthropic, "Toy Models of Superposition" | Theoretically established that features are superimposed |
| 2024.3 | Anthropic, "Scaling Monosemanticity" | Extracted millions of interpretable features from Claude 3 Sonnet |
| 2024.5 | Golden Gate Claude | Demonstrated that amplifying specific features makes Claude adopt that "personality" |
| 2024.10 | Entropix (XJDR, explained by Thariq Shihipar) | Uncertainty detection via entropy/varentropy |
| 2024.11 | Goodfire.ai | Feature manipulation tool for Llama models |
| 2025 | Abliteration (mlabonne) | "Uncensoring" models by deleting RLHF refusal feature directions |

## Significance for Developers

Thariq Shihipar, in "Should Developers Care about Interpretability?" (Nov 2024), demonstrates that interpretability is not merely academic but a practical engineering tool with these applications:

1. **Controlling styles that can't be described in words**: Nuances like "70% kind, 50% concise, 80% professional"
2. **Avoiding RLHF side effects**: Selective manipulation at inference time avoids one-size-fits-all RLHF post-processing
3. **Persistent user preferences**: Maintaining preferences like "answer concisely" that are lost in long conversations, via feature manipulation
4. **Cheap, reproducible classification**: Implementing spam detection etc. via feature activation patterns without training separate models

## Limitations and Challenges

- **Out-of-distribution deviation**: Over-amplifying features can make models "disobey linguistic rules" (brain surgery vs prompting is like "asking politely")
- **Feature label reliability**: Human + machine labeling carries misclassification risk
- **Circuit side effects**: Manipulating one feature may unexpectedly activate other features/circuits (similar problem to RLHF)
- **Broad practical adoption not yet achieved**: Beyond Anthropic's internal use, full production deployment cases are limited

## Related Concepts

- [[concepts/activation-steering]] — Concrete technique for feature manipulation
- [[concepts/scaling-hypothesis]] — Trade-off between scale and controllability
- [[concepts/rlhf]] — Traditional control method; steering aims to complement/replace it
- [[concepts/entropix]] — Adaptive sampling via uncertainty detection

## References

- [Scaling Monosemanticity (Anthropic, 2024)](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html)
- [Golden Gate Claude (Anthropic, 2024)](https://www.anthropic.com/news/golden-gate-claude)
- [Prism: Steering text generation (Linus Lee)](https://thesephist.com/posts/prism/)
- [Should Developers Care about Interpretability? (Thariq Shihipar, 2024)](https://www.thariq.io/blog/interpretability/)