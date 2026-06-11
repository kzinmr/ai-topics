---
title: "Analyzing OpenAI's Reinforcement Fine-Tuning: Less Data, Better Results"
author: Kyle Corbitt
date: 2024-12-30
source_url: https://corbt.com/posts/openai-rft
type: article
tags:
  - reinforcement-learning
  - fine-tuning
  - openai
  - rft
  - openpipe
  - reasoning-models
  - grpo
---

# Analyzing OpenAI's Reinforcement Fine-Tuning: Less Data, Better Results

**Author:** Kyle Corbitt
**Date:** December 30, 2024
**Source:** https://corbt.com/posts/openai-rft

---

A few weeks ago, OpenAI announced Reinforcement Fine-Tuning (RFT). This post will cover the technical details of how it works, as well as the types of tasks for which it is a major breakthrough that lets LLMs be applied to even more complex custom tasks.

At a high level, RFT helps a reasoning model such as o1 adapt its thinking to new domains more effectively. And importantly, compared to standard supervised fine-tuning (SFT), RFT allows models to learn from **very small datasets** — "a few dozen" examples, according to OpenAI.

This is a significant breakthrough. Training and inference costs have dropped precipitously, but collecting enough high-quality labeled data remains a bottleneck on applying AI to complex, novel tasks. So reducing the data required by 1+ orders of magnitude is a big deal!

## RFT: How Does It Work?

OpenAI's internal implementation of RFT is not public, but we can make an educated guess about how it works based on their public description and related research. Here are the high-level steps:

1. The user uploads a dataset with **easily verifiable outputs** (this part is important!). Tasks like classification or information extraction, where there is a clear "right" or "wrong" answer, work well. OpenAI puts it this way: "Reinforcement Fine-Tuning excels at tasks where the outcome has an objectively 'correct' answer that most experts would agree with." In the launch video, OpenAI's example task involved mapping a medical case report to a specific genetic mutation.

2. Using that dataset, the RFT training process performs the following loop:

3. Take a batch of dataset inputs, and generate a reasoning trace and output for each one.

4. The grader scores each generated output. The earlier the correct output is in a list, the higher the score. In the example, a score of 1 if the correct answer is in the first position, 0.5 if it's in the second position, and 0 if it's in the third position or not listed.

5. Use PPO or a similar reinforcement learning technique to update the model weights, favoring generated outputs that receive higher grades.

6. Repeat until the model stops improving.

### Let's Talk About That Grading Function!

The reason for asking the model to output a ranked list instead of simply predicting the most likely answer is that it allows the grader to assign **partial credit** to an answer that includes the correct response in a later position.

Being able to assign partial credit is really useful. **In reinforcement learning terms, this makes the reward function more dense.** By giving partial credit for a correct answer that isn't in the top position, a more granular reward signal is provided — one that acknowledges the model is "on the right track" even if it isn't fully correct. This helps stabilize and speed up training, since the model doesn't have to wait for a perfect response to receive positive feedback. Instead, it learns from incremental improvements toward the correct output.

## When Should You Use RFT?

Three main qualifications that make a task a good match for RFT:

1. **The task is difficult.** (If the task is simple, you may not need any fine-tuning at all.)

2. **Outputs are easy to verify.** Because RFT requires grading each output, the task should have a clear verification mechanism. This works well for classification or structured information extraction, but might be less feasible for tasks like summarization or open-ended conversation.

3. **Labeled data is hard to collect.** If you have a lot of pre-labeled data, you will likely get good results with SFT and won't need to resort to RFT, which is more complicated, slow and expensive at both training and inference-time.

One interesting implication is that for very high-volume tasks, RFT may be a useful "stepping stone" towards a more-optimized classical SFT model. For example, if you have 5 million PDFs and need to perform a complicated data extraction task:

1. Use an expert human to hand-label 50-100 examples.
2. Use those examples as the training data to create an RFT model that performs the task well.
3. Use your new RFT model to machine-label an additional 20K examples.
4. Use those 20K examples to train a simpler, faster LLM to do the same task using SFT.
5. Use your simpler, faster LLM to label the remaining ~5M documents.

## The Road Ahead: Open Source RFT?

An active project is underway to develop an **open-source RFT implementation** to fine-tune reasoning models like Qwen's QwQ. Early results are promising, but they want to **test on more datasets** before releasing. If you're a researcher interested in collaborating — or have a dataset well suited to RFT — reach out to kyle@openpipe.ai.
