---
title: "Microsoft MAI Models"
created: 2026-05-12
updated: 2026-07-28
type: concept
tags: [microsoft, model, voice-ai, image-generation, openai, reasoning-model, code-model]
sources: 
  - raw/articles/2026-04-02_geekwire-microsoft-mai-models.md
  - raw/articles/simonwillison.net--2026-jun-2-microsofts-new-models--80348929.md
  - raw/newsletters/2026-06-03-ainews-microsoft-build-mai-thinking-1-and-mai-family-models.md
  - raw/articles/2026-06-03_eliebakouch-mai-tech-report-deep-dive.md
  - raw/articles/2026-06-03_microsoft-mai-thinking-1-tech-report.md
---

# Microsoft MAI Models

Microsoft's in-house AI model family (MAI: Microsoft AI), marking the company's strategic independence from its OpenAI partnership.

## Hill-Climbing Machine Framework

The MAI-Thinking-1 technical report (109 pages, June 2026) introduces a **"hill-climbing machine"** philosophy: treat model development as a system-level optimization problem with sustained, log-linear performance improvement over thousands of RL steps, rather than a series of discrete model releases.

**Three Design Principles:**

1. **Capabilities should be learned, not inherited** — Intelligence imitated through distillation lacks steerability and robustness for long climbs. MAI-Thinking-1 is trained from scratch with zero distillation from third-party models, on exclusively clean, enterprise-grade data with no synthetic pre-training data.

2. **Simplicity is sustainable** — Favor simple, scalable recipes; clean, trustworthy data; and transparent infrastructure that together support climbing from scratch. Complex tricks that work once often break when scaled.

3. **Scientific rigor avoids shortcuts** — Every decision must be testable through data-driven ladders, ablations, and evaluations that expose reliable paths to the top. The scaling ladder methodology (ablation at multiple model sizes) enforces this discipline.

The result: sustained log-linear improvement over thousands of RL steps, with domain-specific specialist climbs (STEM, agentic coding, helpfulness & safety) consolidated into a single model via SFT distillation.

## Models

### MAI-Transcribe-1
Speech-to-text model released April 2, 2026. Claimed as most accurate available. Designed for noisy real-world conditions (call centers, conference rooms). Runs at half the GPU cost of competing state-of-the-art models. Built by a team of just 10 people. Competing directly with OpenAI's [[entities/openai|Whisper]] and Google Gemini on FLEURS benchmark.

### MAI-Voice-1
Voice generation model, now broadly available for commercial use. Generates natural-sounding speech. Supports custom voice creation from short audio samples.

### MAI-Image-2
Image generation model, top-3 on Arena.ai leaderboard. Deployed in Bing and PowerPoint. Broad commercial use now permitted.

## Build 2026 Updates

At Microsoft Build (June 2, 2026), the company announced five new/updated MAI models along with broader platform announcements for agents and developer tooling.

### MAI-Thinking-1
Microsoft's first dedicated reasoning model. A 1-trillion parameter Mixture-of-Experts model with 35B active parameters (per Simon Willison's correction — initial reports misread the MoE sizes). Trained from scratch with zero distillation and zero synthetic data, using 794 billion pages from a proprietary web crawl plus Common Crawl. Accompanied by a 109-page technical report. Microsoft claims it is "preferred to Sonnet 4.6 in our blind human side-by-side evaluations." Initially available only to select early partners.

**Key benchmarks**: AIME 2025 97.0%, AIME 2026 94.5%, SWE-Bench Pro 52.8%, LiveCodeBench v6 87.7%. Human evals: preferred to Sonnet 4.6 (49% win / 6% tie / 45% loss), loses to Opus 4.6 (43% / 5% / 52%).

#### Architecture

MAI-Thinking-1 uses an **interleaved dense/MoE architecture** where high-sparsity MoE layers (8 of 512 experts activated per token) alternate with small dense FFN blocks. The model adopts the **LatentMoE** design (originating from NVIDIA's Megatron-LM), applying a shared down-projection to compress representations before expert routing, using a 2x compression factor and 3x expansion within each expert. Global-batch load balancing is used, with the aggregation strategy found to matter more than the loss function type. The interleaved layout outperforms the more common "MoE-every-layer" approach on actual training throughput (EGTime) despite comparable FLOP efficiency (EGFLOPs), as the dense FFN layers enable higher hardware utilization on 8K GB200 GPUs.

#### Scaling Ladder Methodology

MAI's core research methodology is the **scaling ladder**: ablations are run at multiple model sizes with constant tokens-per-active-parameter (TPP), comparing scaling curves against baselines. Architecture ablations are conducted near the Chinchilla-optimal region, while data ablations use the full mixture approach (downsampling data sources in the ladder to mimic multi-epoch training). This empirical ladder approach enables data-driven decisions on architecture, data blending, and training hyperparameters.

#### Three-Specialist RL Training

Rather than training one model for all capabilities, MAI trains **three domain-specific specialist models** from MAI-Base-1 using independent RL climbs, then consolidates them into a single model via SFT distillation followed by a final lightweight RL climb:

| Specialist | Focus Area | Reward Mechanism |
|------------|-----------|-----------------|
| **STEM Reasoning** | Math, science, competitive coding | Verifiable rewards on 5M+ verifiable samples; self-distillation to recover from numeric instabilities |
| **Agentic Coding** | SWE-bench, tool use, code agent tasks | Task-specific reward functions for code execution and tool interaction |
| **Helpfulness & Safety** | Human preference, safety compliance | Diverse reward types combining safety guardrails with helpfulness metrics |

#### Training Infrastructure

The model was pre-trained on **8K NVIDIA GB200 GPUs** on a Microsoft-operated Azure cluster. Training achieved **90% goodput** (usable training throughput) through custom infrastructure optimization including dropless MoE implementation supporting variable message sizes. The inference serving stack is **MAIA-200**. The entire training used **30T tokens** processed entirely in-house from raw web/books/code/papers — no open-source training datasets and no synthetic pre-training data.

**Key innovation**: MAI demonstrates that training a competitive reasoning model from scratch with zero distillation from third-party models is feasible at the 1T-parameter scale, using enterprise-grade data curation and a modular RL climb architecture.

#### Pre-Training Data Composition

MAI-Base-1's 30T-token pre-training corpus was built entirely in-house from raw HTML/PDF/books/code, with no open-source training datasets and no synthetic data. Data was processed through proprietary pipelines: HTML extraction, heuristic filtering, exact/fuzzy dedup, cross-source dedup, embedding generation, and PII/safety filtering. Final composition (from the 109-page tech report):

| Source Family | Unique Tokens (T) | Training Tokens (T) | Mix % | Avg. Epochs |
|--------------|-------------------|--------------------|-------|-------------|
| Code | 7.4 | 16.4 | 54.6% | 2.22x |
| STEM | 2.2 | 4.7 | 15.8% | 2.17x |
| Math | 0.3 | 1.6 | 5.4% | 5.28x |
| Books & journals | 0.6 | 0.9 | 3.1% | 1.65x |
| PDFs | 2.7 | 1.4 | 4.7% | 0.53x |
| Web text | 8.1 | 4.5 | 14.9% | 0.55x |
| Multilingual (other) | 8.1 | 0.5 | 1.7% | 0.06x |

Code dominated the mixture at 54.6%, followed by STEM (15.8%) and web text (14.9%). Math was the most heavily upsampled (5.28x epochs). Multilingual data was aggressively downsampled (0.06x). Data sources had knowledge cutoffs from June 2025 (GitHub code) to March 2026 (books/journals).

#### Self-Distillation for RL Stability

A key innovation enabling the thousands-of-steps RL climb is **self-distillation**: when RL crashes occur or the base policy needs updating, the model generates reasoning traces from recent healthy checkpoints, filters them for quality, and uses them via SFT to recover the RL policy without losing learned capabilities. This is critical because RL climbs from scratch (starting with no prior reasoning traces) face long-term training stability as a central challenge.

#### Adaptive Entropy Control in GRPO

The RL recipe modifies standard GRPO with **adaptive entropy control**: a dynamic upper clip bound adjusted via an integral controller that tracks target policy entropy. When entropy drops too low, the clipping bound widens to allow more aggressive token probability updates; when entropy is high, the bound tightens. Combined with an **outer ratio clip** (hard cap on all ratio branches), this prevents the gradient-norm explosions that standard GRPO's unclipped branches can cause at scale.

#### Rocket RL Infrastructure

The RL framework is called **Rocket**, built on Ray actors with SGLang-based serving:

- **Controller**: Loads RL tasks, sends to problem workers, receives completed rollouts with grading metadata, filters and batches for the learner. Supports both on-policy and off-policy RL (primarily off-policy at scale).
- **Problem Worker**: Generates rollouts with a two-stage early-exit strategy (16 rollouts first, if pass rate in range then 128 full rollouts), computes normalized advantages, implements fault tolerance.
- **Rollout Worker**: Generates single rollouts with tool-calling capability, optionally grades, supports multi-step agentic interactions.

The two-stage early-exit strategy dramatically reduces wasted compute: if 16 quick rollouts all pass or all fail, the task is aborted without generating 128 full rollouts.

### MAI-Code-1-Flash
A code-specialist model with 137B total parameters and 5B active (MoE). Built end-to-end by Microsoft using "appropriately licensed data." Purpose-built for GitHub Copilot and VS Code to deliver high performance at lower cost. Rolling out to GitHub Copilot individual users in Visual Studio Code.

### MAI-Image-2.5
Updated image generation model building on MAI-Image-2. Details on specific improvements were shared at Build.

### MAI-Transcribe-1.5
Updated speech-to-text model following MAI-Transcribe-1 (April 2026). Performance and accuracy improvements.

### MAI-Voice-2
Updated voice generation model following MAI-Voice-1 (April 2026). Improved naturalness and voice customization capabilities.

### Platform Announcements
Alongside the models, Microsoft announced several related initiatives at Build:
- **Windows as an agent runtime** — positioning Windows as the native execution environment for AI agents
- **GitHub Copilot app** — a standalone application expanding Copilot beyond IDE integration
- **Web IQ for agents** — a new capability enabling agents to intelligently browse and extract information from the web

## Strategic Significance

The April 2026 MAI model launch was Microsoft's first major model release since CEO Satya Nadella's March 2026 reorganization, where [[entities/mustafa-suleyman]] shifted from Copilot oversight to focus on frontier model development and superintelligence.

The Build 2026 announcements mark a significant acceleration: with MAI-Thinking-1 and MAI-Code-1-Flash, Microsoft now competes directly with OpenAI on reasoning and code models, while expanding the platform vision with Windows as an agent runtime, GitHub Copilot app, and Web IQ. The MAI model family covers voice, image, code, and reasoning — a full-stack AI strategy that reduces reliance on OpenAI.

Microsoft plans to eventually build a frontier LLM "completely independent" of OpenAI if needed. All MAI models are available on Microsoft Foundry and MAI Playground.

## Related Pages
- [[entities/microsoft]] — Microsoft entity page
- [[entities/mustafa-suleyman]] — Microsoft AI CEO
- [[entities/openai]] — OpenAI partnership context
- [[concepts/ai-services-joint-ventures]] — OpenAI DeployCo and enterprise AI services
