---
title: "RL Systems Mind the Gap: Matching Trainer and Generator Throughput"
source: "SemiAnalysis"
date: 2026-06-16
url: "https://open.substack.com/pub/semianalysis/p/rl-systems-mind-the-gap-matching"
type: article
---

Deep analysis of RL training infrastructure. The key thesis: system efficiency comes down to matching trainer and generator throughput.

Three actors in an RL training system: generator, RL environment, trainer.

GRPO overview: Samples multiple completions per prompt, forms group of rollouts, computes advantage relative to group average. Group reward distribution critical — uniform rewards = no training signal.

PipelineRL introduces asynchrony: trainer pushes new weights to generator while rollouts in progress. Policy staleness tolerated to an extent. Synchronous execution wastes too much compute at scale.

RL environment/sandbox challenges:
- Interaction latency between generator and RL environment critical
- Sandbox startup latency major overhead (Modal optimizes this)
- Sandbox scaling with concurrent rollouts
- Sandbox robustness against model misbehavior (million files, OOM)

Throughput matching framework:
- Generator production rate = concurrent rollouts / end-to-end latency
- Trainer consumption rate = samples per step / training step time
- Effective generation rate = acceptance rate × generator production rate
- Factors: group size (N=8/16/64), reward distribution, batch size, inference throughput, sandbox latency, reward modeling type, concurrency, early pruning, adaptive sampling, policy staleness

Collaborators: Prime Intellect (Matej Sirovatka, Ameen Patel, Sami Jaghouar), Modal (Peyton Walters, Nan Jiang, Erik Dunteman). Feedback from Linden Li (Applied Compute).
