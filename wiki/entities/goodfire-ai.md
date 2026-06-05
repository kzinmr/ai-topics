---
title: "Goodfire AI"
type: entity
created: 2026-06-05
updated: 2026-06-05
tags:
  - company
  - ai-safety
  - interpretability
  - ml-research
  - research-lab
aliases: [Goodfire, Goodfire Labs]
related:
  - concepts/activation-steering
  - concepts/mechanistic-interpretability
  - concepts/ai-safety
sources:
  - https://www.goodfire.ai
  - https://www.goodfire.ai/company
  - https://www.goodfire.ai/silico
  - https://www.goodfire.ai/research/the-world-inside-neural-networks
  - https://www.goodfire.ai/research/rlfr
  - https://www.goodfire.ai/blog/intentional-design
  - raw/newsletters/2026-06-04-true-positive-weekly-164.md
---

# Goodfire AI

**Goodfire AI** is an AI interpretability research lab and company based in San Francisco (Telegraph Hill), focused on understanding the internal geometry and structure of neural networks to enable precise understanding, debugging, and intentional design of AI systems. They have raised **$59M** from Menlo Ventures, Lightspeed Venture Partners, and Anthropic.

Their core thesis is that neural networks have **structured inner worlds with geometry that reflects the structure of reality** — and that by developing theories and methods that respect neural geometry, we can unlock deeper interpretability, more reliable control, and safer AI.

## Overview

Goodfire was founded by a team of researchers, engineers, and builders who include founding members of interpretability efforts at Google DeepMind and OpenAI, professors on leave, and engineers who built and deployed large-scale ML systems at organizations including OpenAI, Google, and Palantir. Many of the team helped pioneer core research directions in interpretability — from discovering sparse, human-meaningful neural network features using sparse autoencoders, to automated feature interpretation, to extracting knowledge from superhuman models.

The company operates five days a week in-person at their San Francisco office. Their product **Silico** (previously referenced as "Ember" in early schema.org data) is the first platform for intentional model design — an environment for interpreting, debugging, and shaping model behavior.

## Research Agenda: Three Pillars

Goodfire organizes its work around three interconnected pillars:

### Understand

Reverse-engineering the causal mechanisms of AI to reveal its internal structure, uncovering novel science and validating when predictions reflect true understanding.

**Key publications:**
- **"The World Inside Neural Networks"** (May 2026) — A landmark research overview by Ekdeep Singh Lubana, Thomas Fel, Jack Merullo, Michael Byun, Owen Lewis, and Thomas McGrath. Argues that neural geometry (curved manifolds, circular loops, smooth curves in activation space) is the fundamental data structure of neural networks. Demonstrates that steering along manifolds rather than linear directions avoids "voids" in activation space that cause incoherent outputs. Published alongside a companion paper "Steering Along Manifolds to Control Neural Networks."
- **Alzheimer's Biomarker Discovery** (Nature, 2026) — Identified a novel class of biomarkers for Alzheimer's detection by interpreting an epigenomic model. The first major finding in the natural sciences obtained from reverse-engineering a foundation model.
- **Evo 2 Interpretation** (Nature, 2026) — Decoded the internal representations of Arc Institute's Evo 2 genomic model, finding features that map onto biological concepts from coding sequences to protein secondary structure.
- **EVEE** (Explaining 4.2M Genetic Variants) — Used Evo 2 embeddings to predict whether and how genetic variants cause disease, achieving state-of-the-art performance.
- **"Interpreting Language Model Parameters"** (May 2026) — Lucius Bushnaq, Dan Braun, Lee Sharkey, et al. Stochastic parameter decomposition for understanding how weights and gradients contribute to behavior.

### Debug

Precisely debugging issues with model behavior, identifying and removing confounders, and diagnosing failures before they occur in production.

**Key publications:**
- **Performative Chain-of-Thought Detection** — Tracked when models "know" their final answer but continue generating chain-of-thought regardless. Probes enable early exit from reasoning traces, saving up to **68% of tokens** with minimal accuracy loss.
- **EchoJEPA Cardiac Validation** — Analyzed the latent space of a vision model trained on cardiac echocardiography video, revealing which features encoded real clinical understanding versus spurious correlations.
- **Robotics Model Bottleneck Analysis** — Identified information bottlenecks in a robotics model's latent policy structure, tracing unstable behaviors to brittle internal features.

### Design (Intentional Design)

Controlling training precisely to ensure models learn what is wanted with less data and fewer off-target effects. This is Goodfire's most ambitious agenda, articulated by Chief Scientist Thomas McGrath in the essay **"Intentionally Designing the Future of AI."**

The core insight: interpretability tools allow decomposition of models into distinct semantic parts, enabling targeted manipulation of what gets learned from each datapoint — moving from "guess-and-check" training to **closed-loop control**.

**Key publications:**
- **RLFR (Reinforcement Learning from Feature Rewards)** — Uses lightweight probes on a model's internal representations as reward signals for RL. Applied to hallucination reduction in Gemma-3-12B-IT, achieving **58% hallucination reduction** at **~90x lower cost per intervention** than LLM-as-judge (Gemini 2.5 Pro + web search), with no degradation on standard benchmarks. The probe signal remains useful even after substantial training, enabling test-time scaling.
- **Self-Correcting Search for Materials Discovery** — Gave a diffusion model a feedback loop from its own internals, resulting in **~30% more viable candidate materials** with target properties.

## Product: Silico

Silico is Goodfire's platform for intentional model design, described as enabling engineers to "build AI models with the precision of written software." Features include:

| Capability | Description |
|------------|-------------|
| **Predict** | See inside every prediction — decompose models into interpretable features, detect when predictions are driven by real understanding vs. spurious correlations |
| **Health Check** | Run comprehensive diagnostics on internal representations (undertraining, bottlenecks, feature collapse) |
| **Debug** | Precisely debug model failures, identify and remove confounders |
| **Improve** | Shape model behavior using internal representations for better sampling, search, and predictions |
| **Generalize** | Target specific learned structures to shift training distribution, objective, or architecture |

Silico works across all types of AI models: LLMs, vision models, robotics models, and life sciences models. It is accessed via request.

## Key People

| Person | Role |
|--------|------|
| **Thomas McGrath** | Chief Scientist — Authored "Intentionally Designing the Future of AI"; leads the intentional design research agenda |
| **Ekdeep Singh Lubana** | Lead author on neural geometry research ("The World Inside Neural Networks") |
| **Thomas Fel** | Co-author on neural geometry and interpretability research |
| **Jack Merullo** | Co-author on neural geometry research |
| **Michael Byun** | Blog author, researcher |
| **Owen Lewis** | Co-author on multiple publications |
| **Lucius Bushnaq** | Lead author on parameter interpretability ("Interpreting Language Model Parameters") |
| **Lee Sharkey** | Co-author on parameter interpretability |
| **Atticus Geiger** | Co-author on manifold steering research |
| **Noah Goodman** | Co-author on manifold steering research |
| **Can Rager** | Co-author on manifold steering research |
| **Daniel Wurgaft** | Co-author on manifold steering research |

## Customers & Partners

- **Arc Institute** — Partnership on Evo 2 genomic model interpretability
- **Mayo Clinic** — Healthcare AI interpretability
- **Microsoft** — Foundation model interpretability
- **Prima Mente** — AI systems
- **Rakuten** — Production AI systems; SAE-based PII detection probes

## Neural Geometry: Core Technical Thesis

Goodfire's research agenda is built on the observation that neural networks represent concepts not as linear directions but as **curved manifolds** in activation space:

- Months of the year form **circular loops**
- Historical years form **smooth curves**
- Car positions in a physics simulation form **1D strings**
- The tree of life lies on a **complex manifold** in genomic models
- Colors are represented on surfaces structured by **hue, saturation, and lightness**

This geometry matters for control: steering along a linear path between positions on a manifold can pass through "voids" where the model's output becomes garbled or teleports to unintended states. Steering **along the manifold** preserves coherence.

Goodfire positions this as complementary to (and more powerful than) sparse autoencoders (SAEs), which tend to "shatter" manifolds into many small unrelated pieces. Their unsupervised pipeline discovers manifold structure that SAEs miss.

## Related Concepts

- [[concepts/activation-steering]] — Feature-level model control; Goodfire's manifold steering is a more precise alternative to linear steering vectors
- [[concepts/mechanistic-interpretability]] — Understanding model internals; Goodfire's neural geometry approach operates at the representation level rather than circuit level
- [[concepts/ai-safety]] — AI alignment and safety; Goodfire's intentional design agenda is an alignment technique for steering training outcomes
- **intentional-design** — Goodfire's paradigm for using interpretability during training (no standalone concept page yet)
- **neural-geometry** — The study of curved geometric structure in neural network representations (no standalone concept page yet)

## Sources

- Goodfire AI Website: https://www.goodfire.ai/
- Company Page: https://www.goodfire.ai/company
- Silico Product Page: https://www.goodfire.ai/silico
- "The World Inside Neural Networks": https://www.goodfire.ai/research/the-world-inside-neural-networks
- "Intentionally Designing the Future of AI": https://www.goodfire.ai/blog/intentional-design
- "RLFR: Features as Rewards": https://www.goodfire.ai/research/rlfr
- True Positive Weekly #164 (raw article): raw/newsletters/2026-06-04-true-positive-weekly-164.md
