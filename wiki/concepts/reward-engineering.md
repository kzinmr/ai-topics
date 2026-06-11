---
title: Reward Engineering
type: concept
created: 2026-06-11
updated: 2026-06-11
tags: [reinforcement-learning, reward-engineering, reward-hacking, evaluation, grpo, agentic-rl, agent-training]
sources:
  - raw/articles/2025-07-03_kylecorbitt_agents-mcp-rl-lesson6
  - raw/articles/2025-06-27_kylecorbitt_agents-mcp-rl-office-hours
  - raw/articles/2025-06-06_corbt_reward-hacking-101
  - raw/articles/2025-07-11_corbt_ruler-easy-mode-rl-rewards
---

# Reward Engineering

Reward engineering is the practice of designing reward functions that guide RL-trained agents toward desired behaviors. It is one of the most impactful levers in agentic RL training — the reward function defines *what the agent optimizes for*, and poor reward design leads to reward hacking, output saturation, or failure to capture intended behavior. This concept is part of the broader [[concepts/agents-mcp-rl-course]] and is applied throughout the [[concepts/rl-harness-lifecycle]].

## Reward Function Design Principles

### Start Simple: Binary Rewards

The most effective starting point for reward design is a simple binary reward: **1.0 for correct, 0.0 for incorrect**. Counterintuitively, binary rewards:

- **Converge faster** than complex partial-credit schemes
- **Reach similar final accuracy** to more elaborate reward functions
- Are **harder to hack** because there is less gradient signal to exploit

Partial-credit rewards (e.g., giving 0.3 for format correctness, 0.5 for partial reasoning, 0.2 for style) introduce noise and can slow convergence without improving final performance on the primary objective.

### Complex Rewards for Secondary Behaviors

Complex multi-component rewards have their place — but only for **secondary behaviors**, not the primary task. For example, if you want an agent to answer questions correctly *and* use tool calls efficiently:

- Use binary correctness (1.0/0.0) for the primary task signal
- Add a small turn-efficiency bonus to discourage unnecessary tool calls
- Weight the secondary signal low enough that it doesn't distort the primary objective

### Reward Standard Deviation as a Health Metric

The **standard deviation of rewards across a training batch** is a critical health signal:

- **Healthy training**: reward std dev remains above 0, indicating the agent receives differentiated feedback
- **Output saturation**: reward std dev collapses toward 0 — the model has found a local optimum where it produces nearly identical outputs regardless of input. This often means the agent is either always succeeding or always failing in the same way
- **Monitoring tip**: track reward std dev alongside mean reward. Rising mean with collapsing std dev is a warning sign

## Reward Types

Different reward signal sources suit different tasks and stages of training:

### Ground-Truth-Based Rewards

Compare agent outputs against **known correct answers**. This is the gold standard when ground truth is available — math problems, code tests, factual Q&A. Ground-truth rewards are deterministic, cheap to compute, and impossible for the judge to be hacked.

### LM-as-Judge

When ground truth is unavailable or evaluation is subjective, use a **strong language model to evaluate outputs**. The judge model scores rollouts based on a rubric prompt. See [[concepts/evaluation/lm-as-judge-reward-signal]] for detailed patterns on judge design, prompt engineering, and failure modes.

### Hybrid Rewards

Combine multiple reward signals with explicit weights:

```
reward = w1 * correctness + w2 * format_score + w3 * efficiency
```

Hybrid rewards are useful when you need to optimize multiple dimensions simultaneously. The key risk is weight tuning — poorly chosen weights can cause the agent to sacrifice the primary objective for easier secondary signals.

### Process Rewards

Reward **intermediate reasoning steps**, not just the final outcome. Process rewards are especially valuable for:

- Multi-step reasoning tasks (reward each logical step)
- Tool-use trajectories (reward correct tool selection and argument formatting)
- Training exploratory behavior (reward attempts in the right direction even if the final answer is wrong)

Process rewards require more annotation effort but can dramatically improve sample efficiency.

## Reward Hacking Mitigation

Reward hacking — where the agent finds unintended shortcuts to maximize reward without actually solving the task — is the central challenge of reward engineering. See [[concepts/reward-hacking]] for a comprehensive taxonomy.

### The Iterative Mitigation Cycle

Reward hacking mitigation is inherently **iterative**, not a one-time design exercise:

1. **Observe rollouts**: Watch actual agent behavior on validation examples. Look for patterns where high reward coincides with low-quality outputs
2. **Identify hacks**: Catalog the specific shortcuts — formatting tricks, answer extraction exploits, judge manipulation
3. **Add penalties**: Modify the reward function to penalize identified hacks (e.g., penalize outputs that extract answers from context rather than reasoning)
4. **Checkpoint rollback**: If hacking is severe, roll back to an earlier checkpoint before the hacking behavior was learned, then retrain with the updated reward
5. **Repeat**: New hacks will emerge as old ones are patched

### Common Reward Hacks

| Hack | Description | Mitigation |
|------|-------------|------------|
| Formatting exploitation | Agent learns to produce outputs that game format-based scoring | Make format checks stricter; separate format from correctness |
| Answer extraction | Agent copies or extracts the answer from context without reasoning | Penalize answer-only outputs; require reasoning trace |
| Sycophancy | Agent agrees with the user rather than giving correct answers | Include adversarial examples where user expectations are wrong |
| Length exploitation | Agent produces verbose outputs to hit reward heuristics | Normalize rewards for output length; use length-agnostic scoring |

### LM Judge Patching

When using [[concepts/evaluation/lm-as-judge-reward-signal]], the judge prompt itself can be hacked. The mitigation cycle for judges:

1. Run evaluations and collect cases where the judge gives incorrect scores
2. Analyze failure modes (e.g., judge rewards confident tone over accuracy)
3. Update the judge prompt with explicit instructions addressing failure cases
4. Re-evaluate and confirm improvement on the identified failure cases

## Practical Patterns from ART/GRPO Training

These patterns emerge from practical [[concepts/grpo-rl-training]] experience with agentic RL:

### The Scenario Object

Training examples in agentic RL are structured as **scenario objects** containing:

- **Question**: The task or query presented to the agent
- **Answer**: The expected correct answer (for ground-truth evaluation)
- **Reference**: Additional context, supporting documents, or tool definitions
- **Constraints**: Behavioral requirements (e.g., "cite sources", "use exactly 3 tool calls")

This structured format enables consistent reward computation and makes it easy to mix different task types in a single training run.

### `return_final_answer` Tool for Structured Output

Rather than relying on free-form text generation for final answers, define a `return_final_answer` tool that agents call to submit their response. Benefits:

- **Enables source citation**: The tool schema can require a `sources` field, making attribution a structural property rather than a reward hack
- **Clean answer extraction**: No need to parse answers from free-form reasoning traces
- **Separable rewards**: You can independently score the reasoning trace and the final answer

### Reward Std Dev Monitoring

During training, actively monitor reward standard deviation as described above. In GRPO training specifically, reward std dev feeds directly into the advantage computation — if it collapses, policy gradients vanish and learning stalls.

### Small Datasets Are Fine

A key practical insight: **16–256 training examples are sufficient** for RL fine-tuning. Unlike SFT (supervised fine-tuning), RL does **not** catastrophically overfit on small datasets. The stochastic nature of rollouts provides natural data augmentation — the same question produces different trajectories each epoch.

This means you can curate a small, high-quality evaluation set and train directly on it without regularization tricks.

## Reward Design for Non-Verifiable Domains

Many real-world tasks lack ground truth — creative writing, summarization quality, conversational helpfulness. RL can still work in these domains with careful reward design.

### LM-as-Judge Without Ground Truth

When there is no reference answer, use an LM judge to **compare rollouts against each other** rather than against a fixed target. This relative comparison approach (e.g., "Which of these two responses is better?") converges faster than absolute scoring because:

- Relative judgments are easier for LLMs (and humans) than calibrated absolute scores
- The reward signal naturally adapts as overall quality improves
- Pairwise comparisons reduce judge calibration requirements

### Tournament and Elo-Based Evaluation

For domains where quality is subjective and multi-dimensional, **tournament-style evaluation** can produce robust rankings:

- Pair agent outputs against each other in head-to-head comparisons
- Compute Elo ratings from the comparison matrix
- Use Elo delta as the reward signal

This approach works well for creative tasks, dialogue quality, and any domain where "better" is easier to define than "good."

### The Fundamental Question

The key question for non-verifiable domains: **"Can you evaluate it?"**

If a strong model (or human) can reliably judge which of two outputs is better, then RL with an LM-as-judge reward will work. If evaluation itself is unreliable, RL will optimize for noise. Test judge reliability before committing to a reward design.
