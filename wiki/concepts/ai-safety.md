---
title: "AI Safety"
tags: [[ai-safety-alignment-rlhf-scalable-oversight-interpretability]]
created: 2026-04-19
updated: 2026-04-24
---

# AI Safety — Alignment, Oversight, and Interpretability

## Definition

AI Safety encompasses the technical and philosophical work of ensuring that increasingly capable AI systems behave as intended, remain aligned with human values, and can be understood and controlled by their operators. Unlike generic "ethics" discussions, AI Safety in the modern sense refers to **engineering approaches** — testable, measurable, and improvable methods for controlling AI behavior.

## Two Paradigms

### 1. Empirical / Engineering-Focused Safety (OpenAI / Brockman School)

> *"Safety must scale empirically alongside capabilities."* — Greg Brockman

This approach treats safety as an **engineering problem**: build systems that can be tested, measured, and improved iteratively. Key techniques include:

- **RLHF** — Reinforcement Learning from Human Feedback as the primary alignment mechanism
- **Red-teaming** — Systematic adversarial testing of model behaviors
- **Evaluation environments** — Detecting "scheming" and deceptive behaviors through automated testing
- **Integrated development** — Safety built into the product pipeline, not bolted on

**Proponents**: Greg Brockman, Sam Altman
**Criticism**: Safety is deprioritized in favor of product velocity and compute scaling

### 2. Research-Focused / Alignment Science (Anthropic / Thinking Machines School)

> *"The biggest challenge in AI safety isn't philosophical — it's engineering. We need systems that can be verified, tested, and improved iteratively."* — John Schulman

This approach invests in fundamental alignment research before scaling:

- **Scalable Oversight** — How can humans evaluate AI systems that are more capable than the evaluators?
- **Interpretability** — Understanding what models "know" and "want" internally
- **Constitutional AI** — Encoding principles rather than learning from feedback alone
- **Process supervision** — Verifying reasoning steps, not just outputs ("Let's Verify Step by Step")

**Proponents**: John Schulman, Dario Amodei, Jan Leike, Mira Murati
**Criticism**: Research timelines are too slow; may miss practical deployment needs

## Key Concepts

### Reinforcement Learning from Human Feedback (RLHF)

Pioneered by **John Schulman** at OpenAI, RLHF transforms raw language models into helpful assistants through a three-step pipeline:

1. **Supervised Fine-Tuning** — Train on human-written demonstrations
2. **Reward Modeling** — Train a model to predict human preferences
3. **RL Optimization** — Use PPO to optimize the language model against the reward model

This is the technique that made ChatGPT work. PPO (Proximal Policy Optimization) was the algorithmic engine.

### Reward Model Overoptimization

Schulman and Hilton (2022) demonstrated that reward models degrade when over-optimized — a fundamental limitation of RLHF:

> *"Scaling Laws for Reward Model Overoptimization"* — When you optimize too hard against a reward model, performance on the actual task decreases.

This is a concrete instance of **Goodhart's Law** in AI: "When a measure becomes a target, it ceases to be a good measure."

### Scalable Oversight

A recurring theme in Schulman's recent work: how do humans guide AI systems that are increasingly smarter than the humans?

- **"Let's Verify Step by Step"** (2023) — Process supervision for math reasoning; verify each step, not just the answer
- **PROMPTEVALS** (Shankar, 2025) — Systematic assertion-based evaluation for LLM pipelines
- **Critique Shadowing** (Husain) — Building aligned LLM judges through human-in-the-loop iteration

### Concrete Problems in AI Safety

The seminal 2016 paper by **Amodei, Olah, Christiano, Schulman, and Mané** framed the core challenges:

1. **Avoiding side effects** — AI shouldn't break things while pursuing goals
2. **Reward hacking** — Finding loopholes in the reward function
3. **Scalable oversight** — Supervising agents smarter than supervisors
4. **Safe exploration** — Learning without catastrophic failures
5. **Distributional shift** — Performance degradation when the environment changes

## The 2023-2024 Safety Exodus

A critical inflection point in AI safety history:

| Date | Event | Safety Impact |
|------|-------|---------------|
| Nov 2023 | Altman/Brockman ousted, then reinstated | Board restructuring; safety-focused directors replaced |
| Apr 2024 | **Ilya Sutskever** resigns from OpenAI | Loss of co-founder advocating for safety-first approach |
| Apr 2024 | **Jan Leike** (Superalignment co-head) resigns | "OpenAI is not prioritizing safety" |
| Aug 2024 | **John Schulman** leaves for Anthropic | Signal that even post-training leadership sought safety-focused environments |
| Sep 2024 | **Mira Murati** (CTO) resigns from OpenAI | "We need to bridge the divide between rapid AI advancements and broader societal understanding" |

The exodus created two camps:
- **OpenAI**: Acceleration + compute scaling + empirical safety (Brockman, Altman)
- **Anthropic → Thinking Machines Lab**: Alignment research + interpretability + scalable oversight (Schulman, Murati, Leike)

## Key Quotes

> *"Safety must scale empirically alongside capabilities."* — Greg Brockman

> *"The biggest challenge in AI safety isn't philosophical — it's engineering."* — John Schulman

> *"We need to bridge the divide between rapid AI advancements and broader societal understanding."* — Mira Murati

> *"RLHF is not about making AI systems agree with us — it's about making them learn from us in a way that generalizes beyond what we can explicitly specify."* — John Schulman

## Related People

- [[greg-brockman]] — Engineering-focused safety, empirical testing
- [[john-schulman]] — RLHF pioneer, scalable oversight research, Thinking Machines Lab
- [[mira-murati]] — Safety-first advocate, former OpenAI CTO, Thinking Machines Lab co-founder
- [[ilya-sutskever]] — Former OpenAI Chief Scientist, resigned over safety concerns
- [[dario-amodei]] — Anthropic CEO, co-authored "Concrete Problems in AI Safety"
-  — Former Superalignment co-head, resigned citing safety deprioritization

## Related Concepts

- [[rlhf]] — Primary alignment technique
- [[reasoning-models]] — Process supervision and step-by-step verification
- [[ai-evals]] — Evaluation as a safety mechanism
- [[harness-engineering]] — Constraining AI behavior through system design

## Sources

- "Concrete Problems in AI Safety" (2016) — Amodei, Olah, Christiano, Schulman, Mané
- "Scaling Laws for Reward Model Overoptimization" (2022) — Gao, Schulman, Hilton
- "Let's Verify Step by Step" (2023) — Lightman, Kosaraju, et al.
- John Schulman's homepage (joschu.net)
- Reuters: "OpenAI co-founder John Schulman leaves for rival Anthropic" (Aug 2024)
- TIME Interview with Mira Murati (Feb 2023)
- Dartmouth Commencement Address, Mira Murati (Jun 2024)
- Thinking Machines Lab Announcement (Feb 2025)
