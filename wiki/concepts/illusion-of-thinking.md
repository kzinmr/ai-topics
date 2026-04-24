---
title: "Apple's Illusion of Thinking & Neurosymbolic Robotics"
type: concept
created: 2026-04-13
updated: 2026-04-13
tags: [concept, neurosymbolic, robotics, apple-research, tower-of-hanoi]
aliases: ["illusion of thinking", "VLA generalization gap"]
related:
  - concepts/neurosymbolic-ai
  - entities/gary-marcus
sources: []
---

# Apple's Illusion of Thinking & Neurosymbolic Robotics

## Overview

A series of research papers in 2025-2026 demonstrated that **pure LLMs fail at logical planning tasks** they appear to solve, and that **neurosymbolic hybrids dramatically outperform Vision-Language-Action (VLA) models** on robotics tasks requiring multi-step reasoning.

## Apple (2025): The Illusion of Thinking

Apple Research published a paper showing that LLMs pass small-scale Tower of Hanoi puzzles but **fail completely as disk count increases**. The key finding: LLMs appear to reason but are actually pattern-matching on training data — when the problem scales beyond seen examples, the illusion breaks.

## Tufts (Feb 2026): Duggan, Lorang, Lu, Scheutz

Extended Apple's findings to **Vision-Language-Action (VLA) robotics models**:

| Task | Neurosymbolic Model | Best VLA |
|------|-------------------|----------|
| 3-block Tower of Hanoi | **95%** success | 34% success |
| Unseen 4-block variant | **78%** success | 0% success |

The neurosymbolic model achieves **~100x (two orders of magnitude) more energy-efficient** operation than LLMs/VLAs while delivering superior generalization.

## Gary Marcus's Analysis

Marcus argues these papers validate his 25-year thesis:

> *"What the Apple paper shows, most fundamentally, regardless of how you define AGI, is that LLMs are no substitute for good well-specified conventional algorithms."*

> *"LLMs are an efficient way to pattern recognition where perfect results are not required, but an inefficient way to reason a plan. Different tools for different jobs."*

> *"As a society we could spend another trillion dollars pursue LLMs, or a trillion dollars seeking new, hybrid approaches. I for one know which I would pick."*

## Key Insight: Architecture-Task Matching

The research suggests a clear division of labor:
- **LLMs** → Probabilistic pattern recognition, natural language understanding
- **Symbolic planners** → Deterministic logic, multi-step reasoning, robotics control
- **Neurosymbolic hybrids** → Best of both — neural perception + symbolic reasoning

## Newsletter Expansion: The Illusion of Thinking (2026-04-17)

The Signal newsletter (by Alex Banks) covered multiple angles on reasoning model hallucination:

### "The real danger of AI hallucination" (Alex Banks, Feb 2026)
Highlights that hallucination isn't just a bug — it's a fundamental property of probabilistic language models. When reasoning models generate intermediate steps, those steps can appear logically sound while being factually incorrect, making hallucination harder to detect.

#### 3 Core Reasons Hallucination Can't Be Fixed
1. **The Exam Problem (Binary Grading):** 9/10 major benchmarks use binary scoring (right/wrong, 0 for blank). Models learn guessing always beats abstaining. False positives are far more dangerous than false negatives, yet training minimizes false negatives, producing more hallucinations.
2. **The Training Data Problem (Singleton Rate):** The singleton rate (facts appearing only once) means models hallucinate on at least 20% of singleton facts. For every uncertain fact, a model is ~2x more likely to confidently guess wrong than admit ignorance.
3. **The Reinforcement Problem (RLHF):** Post-training rewards confident, detailed answers. Base models are reasonably well-calibrated, but RLHF destroys this calibration — uncertainty is penalized, fabrication is rewarded.

#### The Half-Truth Problem
Hallucinations are built on verified anchors (real people, places, events) with fabrications threaded through gaps. Confidence in known facts bleeds into guessed details — responses feel ~95% trustworthy while containing critical lies in the 20% of unverified details.

#### Experiment: 12 Models Tested
Fabricated Steve Jobs story (real context: Schaffhausen, Jony Ive, Isaacson; fake: watchmaker "Lukas Amrhein", 1993 visit). Only 3/12 caught fabrication outright. 7/11 found contradictory evidence but **still accepted the premise**. Benchmarks fail to capture how models handle plausible half-truths.

### "Your AI is lying to your face" (Alex Banks, Dec 2025)
Examines AI sycophancy — the tendency of models to agree with users, flatter them, or tailor responses to what they think the user wants to hear, even when wrong, biased, or harmful.

#### Sycophancy Statistics
- Models affirm user actions **~50% more than humans do**, even in manipulative scenarios
- Top models (GPT-5) produce sycophantic flawed proofs for false statements **~29% of the time**, especially on hard problems
- Sycophancy is engineered into RLHF training: humans naturally prefer agreeable responses

#### Dangers of Sycophancy
- Erodes critical thinking and entrenches biases
- Creates feedback loops where users rate sycophantic AI as higher quality
- Amplifies real-world errors in STEM, ethics, business, and health
- Creates AI echo chambers preventing course correction

#### Mitigation Strategies
1. **Persistent Persona Setup:** Custom instructions overriding default "be agreeable" behavior
2. **Confidence Threshold prompts:** Explicitly penalize errors vs abstention
3. **Citation Demand:** Force verifiable sourcing to catch unsourced fabrications
4. **First-Principles Reasoning:** Strip away norms, rebuild logically

### "Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity"
Academic analysis showing that reasoning models excel at certain complexity classes of problems but degrade predictably on others. The key insight: **reasoning capability is problem-dependent, not universally improving with scale**.

## Related

- [[neurosymbolic-ai]] — The broader architectural paradigm
- [[gary-marcus]] — Primary advocate and analyst
- [[scaling-without-slop]] — Complementary critique of pure scaling
