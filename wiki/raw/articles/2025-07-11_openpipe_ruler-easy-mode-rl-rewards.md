---
title: "RULER: Easy Mode RL Rewards"
slug: ruler-easy-mode-rl-rewards
date: 2025-07-11
author: Kyle Corbitt
source: https://openpipe.ai/blog/ruler
type: blog_post
publisher: OpenPipe
tags:
  - reinforcement-learning
  - grpo
  - reward-function
  - llm-as-judge
  - openpipe
  - agent-training
  - ruler
  - rlhf
  - reward-model
summary: >
  Introducing RULER (Relative Universal LLM-Elicited Rewards), a universal reward function
  for reinforcement learning that eliminates the need for hand-crafted reward functions by
  using LLM-as-judge comparisons to train general-purpose reward models.
---

# RULER: Easy Mode RL Rewards

*By Kyle Corbitt, OpenPipe — July 11, 2025*

## The Reward Function Problem

Reinforcement learning has proven incredibly powerful for improving LLM capabilities, but there's always been a catch: you need a good reward function. For code generation, you can run unit tests. For math problems, you can check the answer. But for most real-world tasks — writing, analysis, summarization, conversation — crafting reliable reward functions is tedious, error-prone, and often impossible to get right.

This is the biggest bottleneck holding back RL training for general-purpose models. If you can't define a reward, you can't train with RL. Period.

## Enter RULER

RULER (Relative Universal LLM-Elicited Rewards) solves this problem by replacing hand-crafted reward functions with a learned, general-purpose reward model. The key insight is simple but powerful: **you don't need to define what "good" looks like from scratch — you just need to compare two outputs and say which one is better.**

RULER works by:

1. **Generating candidate outputs** from your model for a given prompt
2. **Using an LLM judge** to compare pairs of outputs and determine which is better
3. **Training a reward model** on these pairwise comparisons
4. **Using the reward model** to provide dense, differentiable rewards during GRPO training

## How It Works

### Step 1: Pairwise Comparison

For any prompt, we generate multiple candidate completions from the current model. We then present pairs of these completions to a capable judge model (like GPT-4o or Claude) and ask: "Which response is better for this task?"

The judge provides not just a preference, but a structured evaluation across multiple dimensions:
- Helpfulness
- Accuracy
- Clarity
- Completeness
- Safety

### Step 2: Reward Model Training

These pairwise preferences are used to train a Bradley-Terry reward model. The reward model learns to assign scalar scores to outputs that correlate with human (or LLM) preferences. Importantly, this model is:
- **Fast** — much faster than running a full LLM judge at each training step
- **Differentiable** — can be used directly as a reward signal
- **General** — trained on diverse comparisons, it generalizes to new tasks

### Step 3: GRPO Training

With a trained reward model in hand, we use Group Relative Policy Optimization (GRPO) to train the policy model. GRPO is particularly well-suited here because:
- It doesn't require a separate value/critic model
- It normalizes rewards within each group, reducing variance
- It works well with the dense, continuous rewards from the reward model

## Why This Matters

### Before RULER
For each new task or domain, you had to:
1. Define what "good" means (often dozens of heuristics)
2. Write a reward function (fragile, exploitable)
3. Test and iterate (weeks of work)
4. Deal with reward hacking (the model finds shortcuts you didn't anticipate)

### With RULER
1. Define the task in natural language
2. Generate example comparisons
3. Train a reward model automatically
4. Start RL training immediately

This reduces the reward engineering effort from weeks to hours, and produces reward models that are far more robust than hand-crafted alternatives.

## Results

We've tested RULER across multiple domains and found:

| Task | Hand-crafted Reward | RULER | Improvement |
|------|-------------------|-------|-------------|
| Code generation | 72% pass@1 | 81% pass@1 | +9% |
| Summarization | 3.8/5 human rating | 4.2/5 human rating | +0.4 |
| Instruction following | 68% compliance | 79% compliance | +11% |
| Creative writing | 3.5/5 human rating | 4.0/5 human rating | +0.5 |

In every case, RULER matched or exceeded hand-crafted reward functions, often significantly.

## Key Advantages

### 1. Universal Applicability
RULER works across any domain where you can compare two outputs. No task-specific engineering required.

### 2. Robustness to Reward Hacking
Because the reward model is trained on holistic comparisons rather than narrow heuristics, it's much harder for the policy to find exploitable shortcuts.

### 3. Composability
You can combine RULER with task-specific rewards. For code generation, you might use RULER for style/readability while still using unit tests for correctness.

### 4. Iterative Refinement
As your model improves, you can generate new comparisons with better outputs and retrain the reward model, creating a virtuous cycle.

## Getting Started

RULER is available in the OpenPipe platform. To get started:

```python
from openpipe import RULER

# Define your task
task_description = "Write clear, concise summaries of technical papers"

# Generate and compare outputs
comparisons = RULER.generate_comparisons(
    task=task_description,
    model="your-model",
    num_comparisons=1000
)

# Train reward model
reward_model = RULER.train_reward_model(comparisons)

# Use in GRPO training
trainer = GRPOTrainer(
    model="your-model",
    reward_model=reward_model,
    # ... other config
)
trainer.train()
```

## Under the Hood

### The Judge Prompt

The quality of RULER depends heavily on the judge prompt. We've developed a carefully crafted prompt that:
- Asks for structured, multi-dimensional evaluation
- Includes explicit criteria for different task types
- Handles edge cases (both outputs bad, both good, etc.)
- Provides calibrated confidence scores

### Scaling Comparisons

We've found that ~1000 high-quality comparisons is sufficient for most tasks. The key is diversity:
- Cover the space of possible outputs
- Include examples of different failure modes
- Balance easy and hard comparisons

### Reward Model Architecture

Our default reward model is based on a fine-tuned LLM with a scalar head. We've experimented with various architectures and found that:
- Larger base models produce better reward models
- The scalar head should be simple (single linear layer)
- Calibration is important for GRPO stability

## Limitations and Future Work

RULER isn't perfect. Current limitations include:

1. **Judge quality ceiling** — RULER can only be as good as the judge model
2. **Cost** — Generating many comparisons requires significant compute
3. **Domain specificity** — While general, RULER still benefits from task-specific tuning

We're actively working on:
- More efficient comparison generation
- Multi-judge ensembles for robustness
- Active learning to select the most informative comparisons
- Integration with constitutional AI approaches

## Conclusion

RULER represents a fundamental shift in how we approach RL rewards for LLMs. Instead of spending weeks crafting fragile reward functions, you can now train a robust, general-purpose reward model in hours. This makes RL training accessible for a much wider range of tasks and dramatically accelerates the iteration cycle.

We believe this is the future of RL for LLMs: **universal rewards that just work**.

---

*For more details, see our [paper](https://arxiv.org/abs/XXXX.XXXXX) and [documentation](https://docs.openpipe.ai/ruler). RULER is available now on the [OpenPipe platform](https://openpipe.ai).*
