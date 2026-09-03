---
title: "World Labs"
created: 2026-09-03
updated: 2026-09-03
type: entity
tags: [company, world-models, spatial-intelligence, video-generation]
aliases: ["World Labs Inc", "Marble"]
sources:
  - raw/articles/worldlabs-ai--blog-atlas.md
  - raw/articles/2026-08-25_dan-jeffries-featherless-dataset-optimization.md
  - raw/articles/2026-08-12_nvidia-gtc-ai-agents-2026-08-12.md
related:
  - entities/fei-fei-li
  - concepts/world-models-science
  - concepts/world-model-taxonomy
  - entities/deepmind
  - entities/nvidia
confidence: medium
---

# World Labs

World Labs is a spatial-intelligence startup founded by [[entities/fei-fei-li|Fei-Fei Li]] building **Marble**, a commercial generative 3D world model that turns prompts, images, and video into persistent, exportable 3D environments (Gaussian splats + meshes). As of September 2026 it is the only company shipping a "3D world model" as a paid product, in a field where most competitors (Genie 3, Sora prototypes, Cosmos) generate pixels instead of persistent geometry.

## Product: Marble

- Generates 3D worlds from text, images, and video inputs; outputs are **persistent, editable, and exportable** (game engines, USDZ/GLB for Vision Pro / Quest 3).
- 0.2 update (2026-09-02) adds: world editor with compositing and in-world painting, High-Fidelity mode (detailed small scenes, up to 4 images), NeRF-2-World & 3D paint, multi-image conditioning up to 24 images, physics colliders, API access for paid tiers, expansion into architecture/real estate/game development.
- Pricing tiers: Free, Standard $28/mo, Pro $76/mo, Max $220/mo.

^[[raw/articles/worldlabs-ai--blog-atlas.md]]

## Thesis: Spatial Intelligence

Li's core argument (September 2026 essay): 3D is not a niche vertical but the medium through which intelligent systems interact with reality — humans navigate, plan, and reason spatially, and generative models so far only produce "surface reflections of reality" (pixels). Marble is the attempt to generate the underlying space instead. Key claim: pixel-only synthesis cannot guarantee spatial coherence; persistent worlds require an explicit 3D representation. See [[concepts/world-model-taxonomy]].

## Competitive Position (September 2026)

| Competitor | Approach | Structured 3D? |
|---|---|---|
| Google DeepMind Genie 3 | Interactive video world model | No |
| NVIDIA Cosmos | World foundation models for physical-AI simulation | Partial (sim layer) |
| OpenAI | Action-conditioned video exploration | No |
| Meta | "Vidolmolins" playable world model demo | No |
| Tencent HunyuanWorld | Video + voxel/CAD variants | Partial |
| Decart Oasis | Real-time interactive video | No |

See [[concepts/world-model-taxonomy]] for the full six-category breakdown.

## Ecosystem Footprint

- Cited as a **pretrained-checkpoint consumer** in dataset-optimization workflows: Featherless' data-opt pipeline ran `microsoft/llada2-1-triune-122b-a12b` *with* Marble among its model sets (dataset engineering — see [[concepts/dataset-engineering]]).
- Appears in the [[entities/nvidia|NVIDIA]] GTC 2026 AI-agent ecosystem map, positioned in the world-model/spatial-data column alongside NVIDIA/Omniverse and Genesis AI.

## See Also

- [[entities/fei-fei-li]] — founder
- [[concepts/world-model-taxonomy]] — six-category framework
- [[concepts/world-models-science]] — the scientific concept
- [[concepts/generative-ai]] — the broader generative space

## Sources

- raw/articles/worldlabs-ai--blog-atlas.md
- raw/articles/2026-08-25_dan-jeffries-featherless-dataset-optimization.md
- raw/articles/2026-08-12_nvidia-gtc-ai-agents-2026-08-12.md
