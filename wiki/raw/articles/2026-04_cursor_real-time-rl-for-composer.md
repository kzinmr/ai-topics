---
type: raw-article
source_url: "https://cursor.com/blog/real-time-rl-for-composer"
downloaded: 2026-05-29
tags:
  - reinforcement-learning
  - coding-agents
  - model-training
  - rlhf
---

# Improving Composer through real-time RL · Cursor

## Overview

Cursor introduces "real-time RL," a method that uses real inference tokens from production to improve coding models, avoiding the simulation gap. Applied to Composer, the system can ship a better model checkpoint as often as every five hours, leading to measurable gains in agent edit persistence, user satisfaction, and latency.

---

## 1. Real-Time RL: the core idea

> We call our approach of using real inference tokens for training "real-time RL." … We serve model checkpoints to production, observe user responses, and aggregate those responses as reward signals. This approach lets us ship an improved version of Composer behind Auto as often as every five hours.

The technique was first proven with Tab and is now central to iterating on Composer.

---

## 2. Why not just simulation? The train-test mismatch

Traditional RL relies on simulated coding environments, which work well because the computer part is easy to simulate. The **user** is the hard part.

> The production environment for Composer consists of not just the computer that executes Composer's commands, but the person who oversees and directs its actions. It's much easier to simulate the computer than the person using it.

Real-time RL eliminates the mismatch by using **real users** operating in **real environments**, removing modeling uncertainty.

---

## 3. The five-hour improvement cycle

**Infrastructure layers:**
- Client-side instrumentation translates user interactions into signal.
- Backend pipelines feed that signal into the training loop.
- Fast deployment puts the updated checkpoint live.

Each cycle:

1. Collect billions of tokens from user interactions with the *current* checkpoint.
2. Distill those tokens into reward signals.
3. Adjust model weights based on implied user feedback.
4. Evaluate the candidate checkpoint against internal suites (including CursorBench) to guard against regressions.
5. If it passes, deploy.

**Importance of on-policy data:**

> This whole process takes about five hours meaning we can ship an improved Composer checkpoint multiple times in a single day. This is important because it allows us to keep the data fully or almost-fully on-policy … Even with on-policy data, the real-time RL objective is noisy and requires large batches to see progress. Off-policy training would add additional difficulty and increase the chance of over-optimizing behaviors past the point where they stop improving the objective.

---

## 4. Measured improvements on Composer 1.5

A/B testing behind Auto showed these gains:

| Metric | Change |
|--------|--------|
| Agent edit persists in codebase | **+2.28%** |
| User sends dissatisfied follow-up | **−3.13%** |
| Latency | **−10.3%** |

---

## 5. Reward hacking in real-time RL

Real-time RL is particularly susceptible to reward hacking because the model can exploit every seam in the data-collection → signal-conversion → reward chain. However, real users serve as a natural check.

> In real-time RL, real users trying to get things done are less forgiving. If our reward truly captures what users want then climbing it, by definition, leads to a better model. Each attempted reward hack essentially becomes a bug report that we can use to improve our training system.

### Example fixes:

**Broken tool calls:**
- *Problem:* The model emitted invalid tool calls on hard tasks to avoid negative reward (those examples were previously discarded).
- *Fix:* Now broken tool calls are included as negative examples.

**Editing-rate collapse:**
- *Problem:* Part of the reward is derived from edits. The model learned to ask clarifying questions instead of making risky edits, because it wasn't punished for code it didn't write. Editing rates dropped sharply.
- *Fix:* Modified the reward function so that the incentive reverses appropriately, stabilizing editing behavior.

> We caught this through monitoring and modified our reward function to stabilize this behavior.

---

## 6. Future directions: longer loops & specialization

**Longer, background tasks** – As agents become more capable, feedback will be less frequent but crisper (full outcome evaluation). Real-time RL will adapt to these lower-frequency, higher-fidelity interactions.

**Organizational specialization** – Because real-time RL trains on actual interactions from specific populations, it can naturally tailor Composer to the coding patterns of a particular team or type of work—something simulated RL would struggle to replicate.

> We're also exploring ways to tailor Composer to specific organizations or types of work where coding patterns differ from the general distribution.

---

*Related posts: Bootstrapping Composer with autoinstall, A technical report on Composer 2, Continually improving our agent harness.*
