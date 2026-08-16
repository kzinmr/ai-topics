---
title: "GLM-5.3"
created: 2026-08-14
updated: 2026-08-15
type: concept
tags:
  - model
  - open-weight
  - coding-agents
  - cybersecurity
  - china
  - benchmark
  - reasoning
  - agentic-rl
  - long-horizon
  - inference
sources:
  - raw/articles/2026-08-14_zai_glm-5-3.md
  - raw/newsletters/2026-08-14-glm-5-3-how-chinese-labs-keep-stride-with-the-frontier.md
  - raw/newsletters/2026-08-15-nobody-built-a-bigger-model.md
  - https://read.getsuperintel.com/p/nobody-built-a-bigger-model
---

# GLM-5.3

**GLM-5.3** is a frontier open-weights language model released by [[entities/glm-5-zai|Z.AI (Zhipu AI)]] on August 14, 2026. It is the successor to [[concepts/glm-5-2|GLM-5.2]], and — unusually — uses the **same base model as GLM-5.2**, with every capability gain coming from post-training. It is notable for two things: it is the most capable open-weights coding model at release, and its cyber capabilities "developed faster than expected" during post-training, making it the first open-weights model to be competitive with the closed frontier on vulnerability discovery.

## Release Summary

| Attribute | Detail |
|-----------|--------|
| **Base model** | Same as GLM-5.2 (post-training-only upgrade) |
| **Released** | August 14, 2026 |
| **Weights** | Open ~2 weeks after launch (pending safety evaluation/hardening) |
| **Coding** | Most capable open-weights model for coding; +50% over GLM-5.2 on Z.ai Code Bench |
| **Cyber** | SOTA on CyberGym for vulnerability discovery |
| **Training stack** | slime (open-source RL framework) + Megatron + SGLang |

## Coding Capability

GLM-5.3 achieves open-source SOTA on public benchmarks including Terminal Bench 3.0 and Agents' Last Exam:

| Benchmark | GLM-5.2 | GLM-5.3 |
|-----------|---------|---------|
| Terminal-Bench 3.0 | 4.6 | **28.3** |
| DeepSWE v1.1 | 46.2 | **66.9** |
| Agents' Last Exam | 23.8 | **28.5** |

### Z.ai Code Bench

Z.ai introduced an in-house benchmark evaluating coding agents in realistic local development environments along two dimensions: end-to-end completion rate and fine-grained checklist accuracy. GLM-5.3 improves both performance and token efficiency:

- **Max effort**: 34.5% at ~75K output tokens/task (vs. GLM-5.2's 23.4% at 96K)
- **High effort**: 31.4% at ~50K tokens, surpassing Claude Opus 4.8 (29.5% at 120K)
- Remains behind [[entities/fable|Claude Fable 5]] (39.5% at Max effort)

## Emergent Cyber Capabilities

The most discussed aspect of the release. Vulnerability-discovery data and environments were added to the training mix, and cyber capability scaled faster than expected — the model began reasoning across multiple exploitation stages and forming coherent plans for complete exploitation chains:

| Benchmark | GLM-5.2 | GLM-5.3 | Mythos 5 | GPT-5.6 Sol |
|-----------|---------|---------|----------|-------------|
| CyberGym (vuln discovery) | 77.2% | **84.5%** | 83.8% | 83.6% |
| ExploitBench | 24.4% | **54.4%** | 78.0% | 76.5% |
| ExploitGym (tasks/2h, /6h) | 29, 39 | **105, 130** | 181, 247 | — |

The pattern across the three is consistent: **the further up the exploitation chain a benchmark sits, the larger the gain from GLM-5.2 — and the wider the remaining gap to the closed frontier.** GLM-5.3 tops the closed frontier on CyberGym but remains well behind [[entities/anthropic|Anthropic]]'s Mythos 5 on end-to-end exploitation (ExploitBench, ExploitGym).

### Real-World Disclosure Ledger

Working with security teams in China against real-world codebases, GLM-5.3 identified **2,436 vulnerabilities across 269 projects** (1,097 medium-to-high severity), spanning kernels, OSes, browser engines, and network protocols. The oldest flaw dated to 1981; on average a vulnerability lived 26.6 years before discovery. This became the **Z.ai Security Disclosure Ledger** (cvd.z.ai), a public record of findings as they move through coordinated disclosure.

The emergent-cyber framing connects GLM-5.3 to the broader [[concepts/china-agentic-coding-sprint|Chinese open-weights competition]] and the debate over closed-model cyber gating (see [[concepts/cyber-frontier-models|cyber capability]] and Anthropic's Mythos/Fable access restrictions).

## Post-Training Approach: Environment Scaling

As agent capability improves, the difficulty of scaling post-training shifts from the model to the **environment**. Z.ai built pipelines that synthesize long-horizon environments end to end (research agents collect task patterns; a judge agent verifies solvability; verifiers are synthesized without access to reference solutions). GLM-5.3 carries over GLM-5.2's RL strategies including **SAO with compaction**, which helps gains persist on long-horizon tasks.

## Post-Training Economics: Capability Is Manufactured One Domain at a Time (Superintel+)

Superintel+'s ["Nobody Built a Bigger Model" deepdive](https://read.getsuperintel.com/p/nobody-built-a-bigger-model) (Aug 15, 2026, mostly paywalled) frames the same release as evidence that **post-training has "quietly become the main event"** — several labs froze pretraining and "went to work on what happens afterwards":

- **"Scaling post-training is all we did for GLM-5.3"** — the article stresses this sentence from Z.ai's release post as something "frontier labs almost never write down": the underlying 743B base model was "left completely untouched."
- **Uneven gains are the mechanism, not noise**: the same training run multiplied Terminal-Bench 3.0 by 6.15 (4.6→28.3 in the 59 days between release posts), roughly doubled ExploitBench (24.4→54.4), but moved Terminal-Bench 2.1 only 81.0→88.2 and ALE 23.8→28.5, with HLE with Tools at 54.7→62.5 — and the vendor "did not hide the losses" on three of the six published benchmarks. Superintel+ reads this as capability being **manufactured, one domain at a time** (the thesis in the article's section header).
- **Two caveats attached to every number**: 28.3 still means the model "fails roughly seven tasks out of ten" (a move from near-total failure to mostly-failure), and every figure is vendor-produced with no independent evaluator verification.
- **Post-training compute vs pretraining compute**: the article cites one company that "admitted its post-training compute exceeded its pre-training compute" and published the curve — the "clearest evidence" of the compute-shift thesis; it also argues such evidence keeps coming from Chinese/open-weight labs "and what their Western counterparts are not saying" (paywalled section).
- **"Three walls where this stops working"**, including one a frontier lab documented against its own model (paywalled section).

The framing complements [[entities/nathan-lambert|Lambert]]'s strategic analysis below and the [[concepts/post-training/post-training]]-centric direction of open-model competition — while adding the caveat that large post-training gains on hard-from-low-base benchmarks do not yet equal reliable task completion.

## Training Infrastructure (slime)

GLM-5.3 runs on **slime**, Z.ai's open-source post-training framework, with Megatron on the training side and [[concepts/inference/sglang|SGLang]] on the rollout side. Notable improvements:

- **Algorithmic**: top-p mask, top-k and full-vocabulary OPD, R3-style setups, full numerical training–rollout alignment (logprob difference at 1e-7, >99.99% reduction).
- **Resource efficiency**: local-storage caching layer, multi-teacher OPD with dynamic teacher switching, workload-aware heuristics — improving end-to-end RL training throughput by **>2.3×**.

## Access and Pricing

- API model `glm-5.3` with three thinking effort levels (`reasoning_effort`).
- **GLM Coding Plan** moved to a **points-based quota** system (input/cached/output priced separately); off-peak hours (outside 14:00–18:00 UTC+8 weekdays) consume 50% of standard points.
- **98%+ cache hit rate** (~30% more effective tokens); **1.5× limited-time quota boost** (up to 180% standard quota through August 31).

## Position in the Open-Weights Landscape

GLM-5.3 continues the rapid pace of Chinese open-weights development documented in [[concepts/china-agentic-coding-sprint]] and [[concepts/glm-5-2]]. Its post-training-only upgrade (same base as GLM-5.2) is an unusual demonstration that frontier-scale gains can be achieved without new pretraining — a signal for the [[concepts/post-training/post-training|post-training]]-centric direction of current open-model competition. Its emergent cyber capabilities also make it a focal point in the debate over whether open weights plus removable guardrails change the attacker/defender balance (see the HN discussion around release).

## Strategic Analysis: How Chinese Labs Keep Stride (Nathan Lambert / Interconnects)

[[entities/nathan-lambert|Nathan Lambert]]'s Interconnects analysis (Aug 14, 2026) frames GLM-5.3 as evidence of a **structural release-cycle advantage** for Chinese labs rather than a one-off model milestone.

### Parameter Count and Efficiency

- GLM-5.3 is roughly **~750B parameters — about a third of Kimi K3** — yet lands at the frontier of agentic coding benchmarks, making it a strong efficiency data point for the open-weights race.
- The model is currently available in Z.ai's coding plan, coming to API soon, and **open weights on Hugging Face in ~2 weeks** (pending safety hardening).

### Z.ai Post-Training Strength vs Kimi Pretraining Strength

Lambert draws a division of labor across the Chinese open-model ecosystem:

- **Z.ai (GLM series)**: Known for **post-training** excellence — the same-base-model upgrade (GLM-5.2 → 5.3) is a pure post-training play enabled by strong RL pipelines (see [[concepts/post-training/post-training]] and the slime infrastructure above).
- **Moonshot (Kimi K3)**: Known for **pretraining** strength — the 2.3T-parameter K3 is the scale leader, but Kimi's post-training lags behind GLM's efficiency per parameter.

### GLM Series Timeline

| Version | Date | Notes |
|---------|------|-------|
| GLM (original) | 2021 | First-generation autoregressive model (10B/130B, THUDM) |
| ChatGLM | 2023–2024 | Chat-oriented line, open weights (chatglm-6b, GLM-4) |
| GLM-5 | 2026 | Frontier open-weight generation |
| GLM-5.2 | 2026-06-22 | Immediate predecessor, same base as 5.3 |
| GLM-5.3 | 2026-08-14 | Post-training-only upgrade, ~750B params |

### Chinese Labs' Release-Cycle Advantage

- Lambert argues Chinese labs operate on **daily/weekly release cadence vs US labs' monthly** — a self-improvement loop fueled by **user data**: open weights deployed widely generate usage signals that feed the next post-training round.
- This makes the open-weights ecosystem a **compound learning engine**: each release captures more real-world tasks, and the RL data advantage compounds across the fleet of open deployments.
- Contrast with US closed labs: capability gains are gated by internal data collection and slower release cycles.

### Rise of the Chinese RL Data Industry

- Lambert highlights a **new data-services industry in China**: US data companies are now **selling training/eval data to Chinese labs** (GLM-5.3's real-world disclosure ledger of 2,436 vulns across 269 projects is one example of data-augmented post-training).
- This inverts the older distillation narrative — the flow of RL data now partially runs *from* the US *to* China's open labs.

### Staged Release Policy & Monitoring

- Z.ai's staged rollout (coding plan → API → HF weights) is read as a **safety-monitoring experiment**: the request classifier and **CoT monitoring** used in the GLM Coding Plan let Z.ai observe misuse before releasing weights broadly.
- Lambert flags **open-weights diffusion concerns**: once weights ship, guardrails become removable, so the staging window is the lab's only chance to measure real-world behavior in a controlled channel.

### Open-Weights Diffusion Concern

- The strategic risk Lambert emphasizes: open-weights distribution of a model with emergent cyber capabilities (see the CyberGym/ExploitBench results above) is a **one-way door** — post-release, the model can be fine-tuned to remove safety guardrails, so the safety evaluation performed pre-release must be conservative. This connects to the broader debate in [[concepts/cyber-frontier-models|cyber capability gating]] and [[concepts/china-agentic-coding-sprint|Chinese open-weights competition]].

## Related Pages

- [[concepts/glm-5-2]] — Predecessor (same base model)
- [[concepts/glm-5-1]] — Earlier generation
- [[entities/glm-5-zai]] — Z.AI (Zhipu AI) entity
- [[concepts/china-agentic-coding-sprint]] — Chinese open-weights competition context
- [[concepts/index-share]] — IndexShare attention (GLM-5.2)
- [[concepts/post-training/post-training]] — Post-training concepts
- [[entities/fable]] — Claude Fable 5 (closed-frontier benchmark reference)
- [[entities/anthropic]] — Mythos/Fable cyber-gating context
