---
title: "Vibe-Eval"
type: concept
created: 2026-05-08
tags:
  - benchmark
  - multimodal
  - evaluation
  - hard-eval
  - personalized-eval
related_concepts:
  - concepts/ai-benchmarks-evals-overview
  - concepts/mmmu
  - concepts/chatbot-arena
  - concepts/multimodal-evaluation
related_entities:
  - entities/reka-ai
  - entities/florian-brand
---

# Vibe-Eval

## Overview

Vibe-Eval is a hard, open-ended multimodal evaluation suite created by Reka AI and released in May 2024. It consists of 269 high-quality image-text prompts with gold-standard reference responses, hand-crafted by AI experts (the Reka team themselves) rather than outsourced annotators. The benchmark has a dual purpose: (1) "vibe-checking" multimodal chat models on day-to-day tasks, and (2) rigorously probing the capabilities of frontier models with extremely difficult prompts.

What sets Vibe-Eval apart is its design philosophy: the prompts were created by people who deeply understand what frontier models can and cannot do. The "hard set" (100 prompts) was specifically constructed from tasks that **Reka Core itself could not solve** at the time of creation, along with other frontier models — creating a set where >50% of prompts defeat all tested models.

The name "Vibe-Eval" reflects the philosophy that everyone can (and should) have their own evaluation tailored to the tasks they care about. Reka's release is one instance of this pattern, and the team encourages others to build their own.

## What It Measures

| Aspect | Detail |
|--------|--------|
| **Domain** | Multimodal chat — visual understanding + language reasoning |
| **Task type** | Open-ended visual question answering with diverse, difficult prompts |
| **Format** | Image + text prompt → free-text response (compared against gold-standard human answer) |
| **Evaluation** | Automatic: Reka Core as evaluator judge (free API) comparing model output to human reference |
| **Human validation** | Periodic human ELO evaluations for models that perform well on automatic scores |

Vibe-Eval covers a deliberately broad range of multimodal tasks — from everyday image understanding ("what's happening in this photo?") to difficult reasoning that requires extracting subtle visual details, connecting them with world knowledge, and producing coherent explanations. No two prompts are alike.

**Two difficulty tiers:**
- **Normal set** (169 prompts): Diverse, varied difficulty, no specific constraints. Representative of day-to-day multimodal use.
- **Hard set** (100 prompts): Prompts where Reka Core partially or completely failed. Designed to induce separability between frontier models.

## Data Sourcing

| Detail | Value |
|--------|-------|
| **Total prompts** | 269 (169 normal + 100 hard) |
| **Prompt creators** | Reka AI team members — actual AI researchers/engineers, not external annotators |
| **Reference answers** | Gold-standard human responses, authored by the Reka team and reviewed multiple times |
| **Hard prompt criterion** | Reka Core produced a partially or completely incorrect response |
| **Quality assurance** | Multiple rounds of internal review |
| **Release date** | May 1, 2024 |
| **Paper** | "Vibe-Eval: A hard evaluation suite for measuring progress of multimodal language models" (arXiv:2405.02287) |
| **License** | Open-source (GitHub: `reka-ai/reka-vibe-eval`, Hugging Face: `RekaAI/VibeEval`) |

The key innovation in data sourcing is **who** creates the prompts. Reka argues that typical annotators, not being calibrated to frontier model capabilities, cannot reliably design prompts that challenge state-of-the-art systems. AI experts who regularly interact with these models can.

## Key Numbers

### Human Baseline
The Reka team conducted formal human evaluations using a third-party annotation company, collecting ~20K pairwise preferences across 13 models (including ties). Human ELO rankings were computed and compared against automatic Vibe-Eval scores.

### Top Model Scores

**Original paper results (May 2024, 13 models evaluated):**
| Model | Overall Vibe-Eval Score |
|-------|------------------------|
| Gemini 1.5 Pro | Highest (exact % not publicly disclosed) |
| GPT-4V | Second-highest (comparable tier to Gemini) |
| Reka Core | Third tier |
| Claude 3 Opus | Third tier |
| Claude 3 Sonnet | Mid-tier |
| LLaVA-1.6-34B | Best open-source |
| Fuyu-8B | Lowest |

**Recent leaderboard results (May 2026, Google-evaluated models):**
| Model | Score |
|-------|-------|
| Gemini 2.5 Pro Preview | 0.672 |
| Gemini 2.5 Pro | 0.656 |
| Gemini 2.5 Flash | 0.654 |
| Gemini 1.5 Pro | 0.539 |
| Gemini 1.5 Flash | 0.489 |

Note: Scores are out of 1.0. The top score of 67.2% highlights how difficult this benchmark remains — even the best models get nearly a third of prompts wrong.

### Key Findings from the Paper
1. **Hard prompts are difficult to create**: Non-trivial to design prompts that are challenging but not impossible.
2. **Hard prompts are difficult to evaluate**: Human raters show higher variance on hard prompts due to ambiguity in partial credit assignment.
3. **Inverse scaling occurs**: On a notable number of hard prompts, larger frontier models (Opus, GPT-4V, Gemini) fail while smaller models (Reka Edge 7B, IDEFICS-2 8B) succeed — an interesting phenomenon more common in multimodal than text-only settings.
4. **Model-based evaluation correlates with human judgment**: Reka Core as automatic evaluator produces rankings that align with human ELO.

## @xeophon's Key Insight

> Everyone can (and should) have their own Vibe-Eval. It's a set of prompts about topics interesting to you, covering a broader range of tasks than standardized benchmarks. The data collection was done by the Reka team themselves — actual AI experts rather than outsourced annotators. This philosophy of personalized evaluation is valuable because standardized benchmarks can't capture what matters for every use case.

## Strengths

1. **Expert-crafted prompts**: Created by AI researchers who understand model capabilities, not general annotators — resulting in more precisely targeted difficulty.
2. **Challenging and non-saturating**: >50% of hard-set prompts are failed by all frontier models, leaving substantial headroom for progress.
3. **Open-ended format**: Unlike multiple-choice benchmarks (e.g., MMMU), Vibe-Eval tests free-form visual understanding in a more naturalistic way.
4. **Human validation loop**: Combines automatic evaluation (fast, cheap) with periodic human ELO (rigorous, calibrated).
5. **Free evaluator access**: Reka Core API is free for evaluation purposes, lowering barriers to entry.
6. **Philosophy of personalization**: Encourages the community to build their own vibes, reducing overfitting to a single benchmark.

## Weaknesses

1. **Small dataset**: Only 269 prompts, which limits statistical power and increases vulnerability to overfitting.
2. **Evaluator bias**: Reka Core as the automatic evaluator may favor models similar to itself, particularly on the hard set (which was constructed from Core's own failures).
3. **Limited public results**: As of May 2026, only Google-evaluated models appear on public leaderboards, making cross-lab comparisons difficult.
4. **Subjective grading**: Even with a reference answer, determining partial credit on open-ended responses involves judgment calls.
5. **Single-team perspective**: The prompts reflect what the Reka team finds interesting/useful, which may not generalize to all use cases (though this is partly by design).
6. **No audio/video**: Currently image+text only, not covering the full multimodal spectrum.

## Evaluation Methodology

Vibe-Eval employs a two-tier evaluation approach that balances speed and rigor:

### Automatic Evaluation (Primary)
Reka Core serves as an automated text-based evaluator. It receives the image, the prompt, the gold-standard human reference answer, and the model's response, then produces a score. The Reka team showed that Reka Core evaluator rankings strongly correlate with human ELO rankings, validating the automatic approach.

Key design choices:
- **Free evaluator access**: Reka Core API is free of charge for Vibe-Eval evaluation, removing cost barriers.
- **Reference-based**: The evaluator compares against a human-written gold answer, not an absolute quality scale.
- **Lightweight**: Designed to be run quickly and frequently, complementing periodic formal human evaluations.

### Human Evaluation (Validation)
For models that perform well on automatic scores, Reka periodically conducts formal human evaluations using a third-party annotation company. Human annotators see the user prompt, image, and reference answer, then rank model responses. Approximately 20K pairwise preferences (including ties) were collected across 13 models in the original study.

The paper found that:
- **Normal prompts** have lower human rater variance — evaluators largely agree on what constitutes a good response.
- **Hard prompts** have higher rater variance — evaluators struggle more with partial credit and ambiguous failures.

This divergence itself is a finding: hard prompts expose not just model limitations but also the difficulty of evaluating creative, open-ended multimodal responses.

## The Personalized Eval Philosophy

Vibe-Eval embodies a philosophical stance about AI evaluation: **standardized benchmarks are necessary but insufficient**. The name "Vibe-Eval" isn't just branding — it captures the idea that every user, developer, or organization should have their own evaluation capturing what matters to them:

- A medical AI company might create a Vibe-Eval of radiology images and clinical notes.
- A game development studio might create a Vibe-Eval of concept art interpretation and narrative consistency.
- An individual researcher might create a Vibe-Eval of their specific domain's hard cases.

Reka's release is one implementation of this pattern — a "vibe check" for multimodal chat — but the framework is designed to be replicated. This philosophy reduces the risk of Goodhart's Law: when a metric becomes a target, it ceases to be a good metric. If everyone has their own eval, no single benchmark can be gamed.

## Inverse Scaling Phenomenon

One of Vibe-Eval's most intriguing findings is the presence of **inverse scaling**: prompts where larger, more capable models fail while smaller models succeed. The paper found this occurred more frequently in multimodal settings than text-only settings. Possible explanations:

1. **Overthinking**: Larger models may over-analyze visual details, reading meaning into noise that smaller models correctly ignore.
2. **Training distribution mismatch**: Larger models trained on broader data may have learned spurious visual-textual correlations.
3. **Output diversity**: Larger models may produce more creative but less grounded responses.

This finding has implications for model deployment: sometimes a smaller, cheaper model is not just "good enough" but actually *better* for specific multimodal tasks.

## Related Wiki Pages

- `concepts/ai-benchmarks-evals-overview` — Overview of the AI benchmarks and evals landscape
- `concepts/mmmu` — MMMU, the multiple-choice multimodal benchmark that Vibe-Eval complements
- `concepts/chatbot-arena` — Chatbot Arena, the human-preference platform Vibe-Eval complements
- `concepts/multimodal-evaluation` — Overview of multimodal evaluation approaches
- `entities/florian-brand` — @xeophon, author of the AI Benchmarks & Evals analysis series
- `entities/reka-ai` — Reka AI, creators of Vibe-Eval

## Sources

1. Padlewski, P., Bain, M., Henderson, M., et al. (2024). "Vibe-Eval: A hard evaluation suite for measuring progress of multimodal language models." arXiv:2405.02287. https://arxiv.org/abs/2405.02287
2. Reka AI. "Vibe-Eval: A new open and hard evaluation suite for measuring progress of multimodal language models" blog post. https://reka.ai/news/vibe-eval
3. Reka AI. `reka-vibe-eval` GitHub repository. https://github.com/reka-ai/reka-vibe-eval
4. Reka AI. VibeEval dataset on Hugging Face. https://huggingface.co/datasets/RekaAI/VibeEval
5. LLM Stats — Vibe-Eval Leaderboard. https://llm-stats.com/benchmarks/vibe-eval
