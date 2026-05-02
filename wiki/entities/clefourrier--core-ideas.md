---
title: "Clémentine Fourrier — Core Ideas & Philosophy"
type: entity
parent: clefourrier
created: 2026-04-10
updated: 2026-04-13
tags:
  - person
  - evaluation
  - philosophy
  - model
  - benchmark
sources: []
---

# Clémentine Fourrier: Core Ideas & Philosophy

Back to main profile: [[clefourrier]]

## Reproducible Evaluation Is Non-Negotiable

Fourrier's most provocative and widely-cited insight came from a simple experiment: **changing only the order of few-shot examples in a prompt can shift evaluation scores by up to 3 points**. This finding, shared in a March 2024 post that generated significant discussion, demonstrated that:

> *"Any kind of model score, provided without an evaluation script for reproducibility, is basically bullshit."*

This principle became the foundation of her advocacy for **standardized, reproducible evaluation frameworks** like LightEval and the Open LLM Leaderboard. She argues that without exact evaluation scripts that can be re-run, comparison between models is meaningless.

## Rankings vs. Scores: The Stability Problem

Fourrier (citing work by Moritz Hardt at the Max Planck Institute) has shown that **neither automated benchmarks nor human-judged leaderboards provide stable, consistent rankings** under minor perturbations. Adding a weak contender to an arena can shift the Elo rankings of strong models; small score modifications can reorder benchmarks. This insight drove her push for **robust evaluation methods** that produce stable rankings, not just raw scores.

> *"If scores, by themselves, are not that relevant, could using the relative ordering of models tell us something of value instead?"*

## Three Pillars of LLM Evaluation

In her influential May 2024 blog post "Let's talk about LLM evaluation" (207 upvotes), Fourrier established a clear taxonomy of evaluation approaches:

1. **Automated benchmarking** — Running models on standardized test suites (MMLU, HellaSwag, TruthfulQA, ARC, etc.)
   - Fast, cheap, reproducible
   - Can be gamed through data contamination
   - Limited in measuring real-world capabilities

2. **Human judges** — Having people evaluate model outputs
   - Most aligned with actual user preferences
   - Extremely expensive and slow to scale
   - Subject to annotator biases and inconsistencies

3. **Model-as-a-judge** — Using strong LLMs to evaluate weaker ones
   - Scalable and cost-effective
   - But "remains to be rigorously tested and proven" for reliability
   - Risk of bias toward models similar to the judge

## We Cannot Evaluate "General Capabilities" Yet

Fourrier argues that the AI community **has not defined what "general model capabilities" means**, making it impossible to evaluate them rigorously. This is a fundamental critique of the field:

> *"Contrary to hype, we cannot really evaluate 'general model capabilities' at the moment, first and foremost because we have not defined what that means."*

She sees LLM evaluation as a research field "very much in its infancy" with "a lot to be done."

## GAIA: Real-World Tasks Over Synthetic Puzzles

The GAIA benchmark (co-created with Meta and AutoGPT, ICLR 2024) represents Fourrier's philosophy in action. Instead of asking expert-level trivia questions, GAIA poses **tasks that are conceptually simple for humans (92% accuracy) but extremely challenging for AI** — requiring multi-step reasoning, tool use, web browsing, and multi-modal handling.

The gap is stark: **GPT-4 with tools achieves only ~15%** on GAIA, while humans score 92%. This demonstrates that even the most capable models lack the fundamental abilities needed for real-world assistant tasks.

## High-Signal Evaluations for Training

In her advocacy for the *FineTasks* blog, Fourrier emphasizes the importance of **selecting training evaluations with the highest signal**:

> *"An high signal eval actually tells you precisely, during training, how well & what your model is learning, allowing you to discard the bad runs/bad samplings."*

This practical insight helps teams avoid wasting compute on training runs that can't be meaningfully assessed.

## CO₂ Transparency in Model Evaluation

In January 2025, Fourrier co-authored an analysis of **CO₂ emissions from evaluating 3,000+ models on the Open LLM Leaderboard**. Key findings:

- Bigger models have higher CO₂ costs, but the **score-to-emission ratio decreases** — diminishing returns on compute
- MoE (Mixture of Experts) models have a **relatively poor leaderboard score-to-emission ratio** despite their efficiency claims
- **Instruction-tuned models often outperform their base models** on the leaderboard but can have higher emissions due to verbosity
- **Small models (< 10B parameters) achieve scores around 35-45 for less than 5kg CO₂**

The goal: provide transparency and encourage model creators to **balance performance with environmental impact**.

## The Smol Training Playbook: Open-Source Model Building

In October 2025, Fourrier co-authored *The Smol Training Playbook: The Secrets to Building World-Class LLMs* with the Hugging Face team. This comprehensive guide documents the **complete journey of training SmolLM2**, including:

- Failures and infrastructure breakdowns (not just the final recipe)
- Why they restarted a training run after 1T tokens
- How to balance competing objectives (multilinguality, performance, efficiency)
- When to pretrain vs. fine-tune
- How to select evaluations that give good early signal

The playbook emphasizes that **fine-tuning for 1T tokens is more economical than starting from scratch** for 10T+ tokens.

## Open-Source Advocacy

Fourrier's work consistently emphasizes **openness, transparency, and reproducibility**. She has:

- Open-sourced LightEval (2.4k+ stars, 445 forks)
- Published the LLM Evaluation Guidebook under CC BY-NC-SA 4.0
- Maintained the Open LLM Leaderboard as a public good
- Community-translated her guidebook into Chinese and French
- Helped ~50 external teams build their own evaluation pipelines
- Advocated for open evaluation standards across the industry
