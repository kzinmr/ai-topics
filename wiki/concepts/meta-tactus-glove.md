---
title: "Meta Tactus — Tactile & Pose Sensing Glove"
created: 2026-11-10
updated: 2026-11-10
type: concept
tags:
  - robotics
  - physical-ai
  - meta
  - embodied-ai
  - ai-in-science
  - datasets
sources:
  - raw/newsletters/2026-11-09-import-ai-480-self-sustaining-space-economies-ai-for-science-progress-and-meta-b.md
  - https://importai.substack.com/p/import-ai-480-self-sustaining-space
---

# Meta Tactus — Tactile & Pose Sensing Glove

**Tactus** (Tactile & Pose Sensing Glove) is a research device from **Meta Reality Labs Research**, presented by Jack Clark in **Import AI 480** (Nov 9, 2026). Its purpose is **data collection for dexterous manipulation** — capturing what a hand actually does while grasping objects, which is the scarce resource for training [[concepts/physical-ai|physical AI]] and robot manipulation policies.

## The three design properties (as specified by Meta)

1. **Thin, conformal 3D-knit form factor** — a **1.5 mm fingertip stackup**, deliberately engineered to *minimize interference with natural manipulation*. The glove must not change how the hand grasps, or the data it records stops being representative of unencumbered human manipulation.
2. **Strategically placed capacitive tactile sensors** at manipulation-relevant regions, their placement **informed by empirical contact studies** rather than uniform coverage. Provides **calibrated fingertip force sensing**.
3. **IMU-fused pose tracking** that **maintains accuracy through hand–object occlusions** — precisely the moments (fingers wrapped around an object, object hidden by the hand) where manipulation data is most valuable and vision-only tracking degrades most.

The combination is what Meta calls a "textile-integrated form factor that preserves natural grasp behavior": contact forces, fingertip force calibration, and occlusion-resilient pose in one wearable.

## Why it matters

Clark's framing is the "how would an AI use this?" lens he applies to research papers. A glove like Tactus is a **bidirectional interface**: it *records* human manipulation for training data, and it can *deliver* force feedback to a human operator. Pair it with an autonomous agent and you have the infrastructure for a human acting as the hands of a remote policy — performing physical tasks while receiving live haptic guidance, and simultaneously generating the demonstrations the policy trains on. Clark explicitly disclaims endorsing that future; the analytical point is that **the same device serves data generation and teleoperation**, so manipulation-data pipelines and human-in-the-loop actuation pipelines converge on one piece of hardware.

For the robotics-data problem generally, Tactus sits in the same space as glove/vision-based teleoperation and mocap data rigs: the bottleneck for dexterity is not compute but **high-fidelity contact data from real object interactions**, which is exactly what the calibrated force sensing plus occlusion-robust tracking is built to produce. See [[concepts/physical-ai]].

## Related

- [[entities/meta]] — Reality Labs Research
- [[entities/jack-clark]] — Import AI 480 reporting
- [[concepts/physical-ai]] — the training-data problem the glove addresses
- [[concepts/world-models]] — adjacent embodied-learning substrate

## Sources

- Jack Clark, ["Import AI 480: Self-sustaining space economy"](https://importai.substack.com/p/import-ai-480-self-sustaining-space), Nov 9, 2026 — quoting Meta Reality Labs Research, "Tactus: Tactile & Pose Sensing Glove for Natural Dexterity Data Collection" (arXiv).
