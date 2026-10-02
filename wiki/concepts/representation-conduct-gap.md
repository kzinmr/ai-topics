---
title: "Representation-Conduct Gap"
created: 2026-09-27
updated: 2026-09-27
type: concept
tags: [interpretability, agent-safety, multimodal, ai-safety]
aliases:
  - Alignment Illusion
  - Weight-Induced Alignment
  - PA Gap
sources:
  - raw/articles/2026-09-27_arxiv_2609.30210_alignment-illusion-mllm.md
related:
  - concepts/mechanistic-interpretability.md
  - concepts/activation-steering.md
  - concepts/representation-collapse.md
confidence: medium
contested: false
---

# Representation-Conduct Gap

The **representation-conduct gap** (a.k.a. the **alignment illusion**, Zhang et al. 2026)
is the finding that a high internal *visual–text alignment score* in a multimodal LLM is
**not** evidence that the model actually uses the image to answer — because the score
measures geometry in the shared language-model pathway, not content-level cross-modal
interaction. A model can look "well aligned" by standard internal metrics even when the
task-relevant visual content is gone. ^[raw/articles/2026-09-27_arxiv_2609.30210_alignment-illusion-mllm.md]

## The Illusion

MLLMs are usually evaluated for "alignment" with CKA, SVCCA, MIR, or leading
principal-angle cosine. Those tools were built to compare representations from
**independently trained** networks, where high similarity ⇒ convergent features. In an
MLLM, visual and text tokens flow through the **same** Transformer blocks and weights, so
the independence assumption that licenses the interpretation is gone.

**Controlled test.** Across 13 MLLMs from five families (0.5B–72B), replacing
projector-output visual tokens with **Gaussian noise** sharply collapses task accuracy,
yet all four scalar measures **fail to consistently separate** the corrupted stream from
the original. High alignment score + collapsed accuracy = the alignment illusion.

## Root Cause: Weight-Induced Alignment

The shared MLP/attention weights impose similar geometry on both streams even when visual
tokens carry no task-relevant content. Specifically, **anisotropic MLP down-projections**
pull visual and text tokens toward common output directions — a **weight-induced
alignment** that is essentially **one-dimensional**. A scalar score collapses this
spurious component together with genuine content coupling, so it cannot tell them apart.

## The PA Gap Remedy

**Principal-angle gap (PA gap)** = difference between the **top two** principal-angle
cosines (σ₁ − σ₂). It isolates the one-directional (weight-induced) component from
multi-directional visual structure. Under graded visual corruption, the PA gap **tracks
task accuracy more consistently** than the scalar scores; under a structured-but-irrelevant
image it exposes regimes where internal geometry and accuracy come apart.

## Why It Matters (generalizes beyond MLLMs)

Methodological warning for all interpretability work that reads internal similarity as
"the model represents/uses X": when two inputs share a processing pathway, similarity can
be an artifact of the shared weights, not of interaction. This is the
[[concepts/mechanistic-interpretability]] analogue of a broader lesson — **a representation
metric is a diagnostic of geometry, not a proxy for conduct**; calibrate it against
controlled task evidence. Treat it as the interpretability cousin of
[[concepts/representation-collapse]]: in both, an internal similarity signal
over-reports the model's real use of information. Same caution applies to using internal
alignment to justify claims in [[concepts/activation-steering]]: measure the geometry, but
only *controlled interventions on the actual input* license a claim about what the model uses.

## Open Questions

- How far does the illusion extend to text–text or tool-output–text streams in agents,
  where a "shared pathway" is likewise guaranteed?
- Can the PA gap (or a related spectrum statistic) become a standard corruption-calibrated
  control in interpretability pipelines, rather than a one-off diagnostic?
