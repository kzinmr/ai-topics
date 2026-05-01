---
title: "Better Harness: A Recipe for Harness Hill-Climbing with Evals"
source: "https://blog.langchain.com/better-harness-a-recipe-for-harness-hill-climbing-with-evals/"
date: 2026-04-08
author: Vivek Trivedy (LangChain)
tags: [harness-engineering, agents, evals, langchain, optimization, generalization]
---

# Better Harness: A Recipe for Harness Hill-Climbing with Evals

**Source:** LangChain Blog
**Key Concept:** Using evaluations (evals) as a learning signal to autonomously improve agent harnesses while avoiding overfitting.

## 核心理念: Evals as Training Data
In classical ML, training data updates model weights. In agent engineering, **evals guide harness updates.**
- **The Signal:** Evals encode desired behaviors. Each case provides a signal (e.g., "did the agent take the right action?") that guides the next edit to the harness.
- **The Goal:** Build a "Better-Harness" system that moves beyond simple update algorithms into a compound engineering system: **Data Sourcing → Experiment Design → Optimization → Review & Acceptance**

## 1. Sourcing High-Quality Evals
Quality is prioritized over quantity to ensure a strong learning signal.
- **Hand-curated:** High-value examples of specific desired behaviors.
- **Production Traces:** Mining failures from real interactions. Dogfooding and sharing trace links (e.g., in Slack) builds shared knowledge.
- **External Datasets:** Useful but require manual adjustment to reflect specific desired behaviors.
- **Tagging:** Every eval is tagged by category (e.g., "tool selection," "multi-step reasoning").

## 2. Designing for Generalization
To prevent agents from "cheating" (reward hacking/overfitting to specific eval text):
- **Holdout Sets:** Essential proxy for true generalization.
- **Human Review:** Acts as a second signal to catch instructions that are overfit or wasteful of tokens.
- **Prompting:** Explicitly prompting the agent to avoid overfitting.

## 3. The Better-Harness Recipe (Optimization Loop)
1. **Source & Tag:** Mix hand-written, production, and external evals.
2. **Split Data:** Create **Optimization** and **Holdout** sets per category.
3. **Baseline:** Run initial experiments to ground all future updates.
4. **Optimize (Autonomous):** Diagnose using traces, scope to one targeted change.
5. **Validate:** Check if change passes new evals without regressing on previously passing cases.
6. **Human Review:** Sanity check for edge cases and token efficiency.

## 4. Real-World Results
Experiments using **Claude Sonnet 4.6** and **Z.ai's GLM-5** identified successful harness changes:

| Shared Change | Instruction Added | Effect |
| :--- | :--- | :--- |
| **Use reasonable defaults** | "Use reasonable defaults when the request clearly implies them." | Agent stopped blocking on trivial missing wording. |
| **Respect constraints** | "Do not ask for details the user already supplied." | Stopped redundant follow-up questions. |
| **Bound exploration** | "Do not keep issuing near-duplicate searches..." | Prevented infinite search loops. |
| **Prioritize questions** | "Ask domain-defining questions before implementation questions." | Improved logic flow in vague scenarios. |

## 5. Maintenance & The Future
- **Regression Testing:** Evals act as a "Test Driven Development" (TDD) suite for agents.
- **Spring Cleaning:** Evals should not grow indefinitely; remove saturated or outdated evals regularly.
- **Automated Flywheel:** more usage → more traces → more evals → better harness
