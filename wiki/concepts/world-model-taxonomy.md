---
title: "World Model Taxonomy"
created: 2026-09-03
updated: 2026-09-03
type: concept
tags: [world-models, spatial-intelligence, video-generation, research]
sources:
  - raw/articles/worldlabs-ai--blog-atlas.md
related:
  - concepts/world-models-science
  - concepts/world-models-for-agents
  - entities/world-labs
  - entities/fei-fei-li
  - entities/deepmind
confidence: medium
---

# World Model Taxonomy

A classification of how "world model" is used across the industry, derived from the World Labs / Google DeepMind / NVIDIA / OpenAI / Meta / Tencent / Decart competitive scan of September 2026. The term covers at least six distinct technical commitments; conflating them makes vendor claims impossible to evaluate. See [[concepts/world-models-science]] and [[concepts/world-models-for-agents]] for the broader concept and [[entities/world-labs]] for the flagship commercial example.

## The Six Categories

| Category | Output | Mechanism | Examples | Maturity |
|----------|--------|-----------|----------|----------|
| **1. Gaussian Splat world model** | Persistent, editable 3D Gaussian fields | AI generates a scene → it exists as a queryable 3D data structure | [[entities/world-labs]] Marble (persistent worlds, editor, API) | Commercial (paid tiers) |
| **2. Interactive video-gen world model** | Pixels, no persistent state | Real-time autoregressive video diffusion conditioned on actions | Genie 3 ([[entities/deepmind]]), Oasis (Decart), Cosmos (NVIDIA), HunyuanWorld (Tencent), Meta's "Vidolmolins" | Demo/research stage |
| **3. Action-conditioned video** | Pixels driven by action conditioning | Sora-style generation steered by actions | [[entities/openai]] "toynet" prototypes | Prototype |
| **4. Latent-prediction world model** | Latent states (not media) | V-JEPA 2-style prediction in representation space | [[entities/meta]] V-JEPA 2 | Research |
| **5. Video-as-reality-simulator** | Pixels, framed as physical truth | Video generation repositioned as embodied simulation | [[entities/deepmind]] Veo 3.1 claim: "world's best video model… a real reality simulator" | Marketing layer on category 2 |
| **6. Voxel / CAD world model** | Structured 3D (voxel meshes, geometry) | Generation into explicit geometric representations | Tencent HunyuanWorld variants | Research/early |

## Why the Distinction Matters

Categories 1 and 6 commit to **persistent, queryable 3D structure**: geometry exists independent of observation, is exportable (to game engines, USDZ/GLB), and survives being looked away from. Categories 2, 3, and 5 commit only to **pixels** — what Fei-Fei Li calls "reality synthesis." The open question is whether pixel-only world models can guarantee spatial consistency at scale:

> *"You cannot build a persistent, editable, spatially coherent world by only synthesizing the pixels that humans perceive — no matter how good the models get. They can look extremely convincing, but nothing guarantees that the underlying space is coherent."* — [[entities/fei-fei-li|Fei-Fei Li]]

^[[raw/articles/worldlabs-ai--blog-atlas.md]]

Category 4 (latent prediction) is orthogonal to the pixels-vs-structure axis: it produces no media at all and is aimed at robot planning rather than content — the same motivation behind DeepMind's Gemini Robotics 2 effort (see [[concepts/gemini/gemini-robotics-2]]).

## Vendor Claims (September 2026)

- **World Labs (Marble)** — the only company currently claiming a *shipped* 3D world model; "first 3D world model accessible to everyone," paid tiers with API coming (0.2 update, 2026-09-02).
- **NVIDIA (Cosmos)** — positions its world foundation models as a *simulation layer* for physical AI developers rather than a consumer product.
- **OpenAI** — action-conditioned video exploration, no structured-3D product announced.
- **Meta** — "Vidolmolins" described as a "full-scale world model that can be played"; demo-stage.

## Open Questions

- Can video-only models (categories 2/3/5) be regularized into genuine spatial consistency, or does persistence require an explicit 3D representation?
- Will Gaussian-splat pipelines (category 1) scale to large, dynamic scenes, or remain a "spatial generation" tool for static scenes?
- Does the market need one taxonomy — or are "world model" products competing on fundamentally different axes and merely sharing a label?

## See Also

- [[concepts/world-models-science]] — scientific world models
- [[concepts/world-models-for-agents]] — world models for agents
- [[concepts/jepa-world-models]] — the latent-prediction approach (category 4)
- [[entities/world-labs]] — Marble product and Spatial Intelligence thesis
- [[entities/deepmind]] — Genie 3, Veo 3.1 framing
- [[entities/nvidia]] — Cosmos world foundation models

## Sources

- raw/articles/worldlabs-ai--blog-atlas.md
