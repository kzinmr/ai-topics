---
title: "One Right Answer or Many? A Useful Distinction for Evaluating and Fine-Tuning LLMs"
author: Kyle Corbitt
date: 2025-01-14
source_url: https://corbt.com/posts/deterministic-vs-freeform-tasks
type: article
tags:
  - fine-tuning
  - evaluation
  - llm
  - openpipe
  - reinforcement-learning
  - rlhf
  - dpo
  - temperature
---

# One Right Answer or Many? A Useful Distinction for Evaluating and Fine-Tuning LLMs

**Author:** Kyle Corbitt
**Date:** January 14, 2025
**Source:** https://corbt.com/posts/deterministic-vs-freeform-tasks

---

I recently wrote about reinforcement fine-tuning (RFT). In that post, I defined the class of tasks for which RFT is a good fit in this way:

> [RFT] works well for classification or structured information extraction, but might be less feasible for tasks like summarization or open-ended conversation.

This distinction actually comes up a lot, not just in relation to RFT! "Best practices" around evaluation and fine-tuning techniques tend to differ significantly depending on whether your task has **one** right answer (I'll call these _deterministic_ tasks), or **many** potential right answers (I'll refer to these as _freeform_).

In this post I'll work to sharpen that distinction and share some of the techniques that best lend themselves to each.

## Deterministic or Freeform? Let's Define Terms.

**Deterministic** tasks have one (or a few) correct outputs for a given input, and the model should always produce the correct output. This category includes most classical ML workloads such as classification and information extraction, as well as newer flows such as copilots that convert a natural-language user intent into a concrete action.

**Freeform** tasks have many (sometimes infinite) "correct" outputs for a given input. Things like writing summaries, drafting emails, or writing chatbot responses are all **freeform** tasks.

A good heuristic is to ask yourself the following question: _"given a known-correct output, can I write a simple piece of code that checks whether an unknown output is also correct?"_ If the answer is "yes", your task is deterministic. Otherwise, it's probably freeform.

## So How Common Are These?

LLMs are widely used for both deterministic and freeform tasks. To get a sense of their relative popularity, I wrote a quick script to go through 1000 recent datasets on OpenPipe and classify each one as "deterministic" or "freeform", as well as its high-level category. The breakdown showed that (among OpenPipe users) about **63%** of tasks are freeform, and **37%** are deterministic.

Interestingly though, when limiting to the top 30 datasets by inference usage, we find the opposite pattern — **60%** are actually deterministic tasks! Hypothesis: computers usually consume the output of deterministic tasks but humans usually consume the output of freeform tasks, and computers can process a lot more information than humans.

## Difference #1: Ideal Temperature

One relatively well-known difference between deterministic and freeform tasks is the ideal temperature to use at generation time. A higher "temperature" makes a model more creative by introducing a bit of randomness into the sampled tokens. This can be helpful for freeform tasks, but is almost always harmful for deterministic ones. We recently evaluated a deterministic task where dropping the temperature from 0.7 (the default used by OpenAI and many other providers) to 0 increased benchmark performance from 71 to 76%, which is a significant jump!

In general, I recommend using temperature=0 for deterministic tasks and evaluating temperatures in the 0.7 to 1.0 range for freeform ones.

## Difference #2: Evaluations

### Evaluating Deterministic Tasks

The beautiful thing about deterministic tasks is that model performance can be **relatively easily evaluated**. Typically this involves gathering a high-quality "golden dataset" containing many inputs and known-correct outputs. Once this is done you can easily evaluate a new prompt or model by running it against all of your inputs, gathering the new outputs, and programmatically comparing them to your known-correct outputs.

This ease of evaluation makes optimization much easier. You can experiment on different prompts and models with more confidence if you have a reliable way of measuring performance! Because of this, for deterministic tasks I recommend building at least a seed golden dataset and evaluation suite **first**, before even starting to iterate on prompts or models.

### Evaluating Freeform Tasks

On the other hand it is **very difficult to evaluate** freeform tasks in practice. Having a "golden dataset" may not be that helpful — if you're writing a chatbot, knowing one assistant message is good doesn't really help you decide whether another alternative message is good or not.

Despite this difficulty, some kind of evaluation feedback loop is necessary to iterate on your system without introducing regressions. There are a number of approaches we see users take in practice:

1. **Vibe checks**: this is the "default" evaluation method. Run several different inputs through your system, look at the outputs, and decide if they look reasonable.
2. **LLM-as-judge**: Use another model to review the freeform outputs and decide whether each one is "good" or "bad".
3. **User Feedback**: allow end users to upvote/downvote responses, propose changes, request regenerations, etc.
4. **Business Metrics**: your system is designed to achieve some outcome. Measure that metric, and see whether changes to your AI system have any impact on it.

## Difference #3: Fine-Tuning

### Fine-Tuning for Deterministic Tasks

* **RFT**. Reinforcement fine-tuning (RFT) is a new technique that trains a reasoning model like o1 to operate in a new domain.
* **Smaller models.** You can often effectively train a far smaller model for deterministic tasks like classification and information extraction without degrading performance. We've seen projects where customers successfully move from GPT-4o to a fine-tuned Llama 3.2 3B, which cuts costs by >100x.
* **Design for logprobs**. Consider asking the model to output a single distinct token for each possible class so you can examine the logprobs.
* **Consider alternative architectures**. Tasks like classification and span extraction can be completed effectively by relatively small encoder models like ModernBERT.

### Fine-Tuning for Freeform Tasks

* **Consider DPO**. Direct Preference Optimization (DPO) is a technique for training your model on **pairs** of outputs, one "accepted" and one "rejected".
* **Consider RLHF**. Training a **reward model** to predict actual business metrics, and then improving your fine-tuned model via PPO or its modern variants.

## Key Takeaways

* Use **temperature=0** for deterministic tasks and higher temperatures for freeform tasks.
* Evaluations differ: deterministic tasks can leverage golden datasets, while freeform tasks may need vibe checks, LLM-as-judge, or user feedback.
* Fine-tuning options: RFT works well for deterministic tasks, while freeform tasks benefit from preference-based methods like DPO or RLHF.
* Smaller fine-tuned models can drastically cut inference costs and latency, especially for deterministic tasks.
