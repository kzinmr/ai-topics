---
title: "How we teach AI models"
author: Lee Robinson (@leerob)
date: 2026-07-24
source: https://x.com/leerob/status/2080467752897146898
source_type: x_article
url: https://x.com/i/article/2080455318128009217
tweet_id: "2080467752897146898"
article_id: "2080455318128009217"
author_id: "81712767"
metrics:
  bookmarks: 1112
  impressions: 61574
  likes: 821
  retweets: 77
---

# How we teach AI models

*By Lee Robinson (@leerob) — 2026-07-24*

How do AI models learn new skills and behaviors?
The process is surprisingly human and easy to understand, even if you don't have a machine learning background.

## Helpful colleagues

AI models, increasingly used through agents, are similar to a helpful colleague. What traits do the best people you've worked with share?

Maybe you thought of coworkers who were great communicators, or who had the judgment to know when to ask for help versus when to figure it out themselves. There are also more human qualities, like being personable, empathetic, and kind. But I particularly enjoy working with people who can take ambiguous problems and find ways to solve them.

So how do we get a model to act like that ideal colleague? We need to first write down our version of the "correct" behavior. This document is called a **model specification**, **principles**, **constitution**, or similar. It's used both for internal alignment and as a guideline for testing model behavior (i.e. evals) during training.

## How do we get better at our jobs?

My over-simplification is to try hard things, fail, learn, and get better through repetition.

If you're onboarding a new teammate, you don't expect them to be productive on day one. They need to learn how to use your systems and tools, and how your team works together. Humans, with all our imperfections, are quite good at learning new skills (and remembering them).

Let's say you want to become the best basketball player in the world. Which approach should you take to improve your skills?

1. **Read everything ever written** about the game of basketball. We're going to ignore being limited to 24 hours in a day.
2. **Play 10,000 games** of basketball. The same time-bending rules apply. You learn through trial and error, reviewing film, grading your decision making, and improving during practice.

Knowledge and experience are two different stats, and ideally you want to max both. It reminds me of how people talk about "book smarts" versus "street smarts". The best players have each.

How do we learn things faster? **With a coach!** The ideal coach will watch you play, tell you what to fix, and always push you against your current limits. They'll teach you how to make high-quality decisions when you're on your own, nudging your brain weights toward better decisions over time.

## How do models learn?

Models don't learn exactly like humans, but human learning provides a useful analogy.

These models start by learning to predict patterns from an enormous library of other people's experience (i.e. **pretraining**). They actually can read every book on basketball!

After pretraining, you have a **base model**. The model may be very "book smart" (e.g. it knows everything about ancient history) but it is imperfect and has some quirks. It doesn't feel great to talk to and can make mistakes.

You then show the model many examples of great behavior you want it to mimic (i.e. **supervised fine-tuning**, or SFT). Think about this like studying film of great players. This gets you far, but you can't become great only by copying someone else's moves.

You need to watch the model do real work so you can help it learn and improve. To shape its behavior, you let the model play simulated games and reward it when it does well (i.e. **reinforcement learning**, or RL). This reward is like a coach's feedback, where you tell the model if the decisions it made were good or bad, nudging it to improve with more attempts.

New research also suggests that more generalizable qualities like **truthfulness** can be learned during RL. If you teach the model to be more honest when answering questions from one domain, values like truthfulness can generalize when answering any question.

## Grading the model

We measure whether models are improving in two main ways: **practice tests** where they can review the answers, and **final exams** where they've never seen the questions before.

It would be hard for humans to know if we're improving at calculus, for example, without testing for understanding. If you take a test and fail, you know exactly where you need to improve, but this only works when the domain being tested (e.g. math) has an answer key.

One of the main challenges for training large AI models is creating a diverse set of "tests". These tests could be on anything from math to coding. If you can create an answer key, then the models can try the test many times and learn to improve.

What about measuring intelligence across many different tasks? Think about AP exams, which cover subjects from calculus to history. Many of these exams combine multiple-choice questions scored by correctness with free-response questions graded against a rubric.

This is similar to how we evaluate models with **benchmarks**. Some benchmarks measure objectively verifiable things (e.g. did the tests pass?) and others ask a separate model to grade the results using a rubric (i.e. **LLM-as-judge**). These results give you a reference to understand if the model is actually learning and improving during training.

Critically, benchmarks are intended to test unseen or "held-out" tasks. Otherwise, it would be a bit like memorizing all the answers to your test, and then showing up and writing them down from memory, which isn't a true measure of intelligence.

## Intelligence alone isn't enough

If you're a genius, but rude and socially unaware, chances are people won't like you.

We can all probably think of someone we know like this. It's not enough to just be smart! This is why **aligning models to act "correctly"** (according to the model spec we defined) is incredibly important.

Imagine you had a friend who ended every conversation with some now-popularized LLM slop like "Honestly? That's the tell". You'd quickly get tired of talking with them.

Engineers and researchers training models spend a bunch of time talking to a new model before it's finished. They document all the quirks and places where it could improve. This could be overuse of stock phrases like "Bottom line:" or sacrificing clarity for a shorter bullet point, leading to some weird unintelligible language with overly complex words.

With the issues identified, they can then work to train the model further and penalize bad behaviors, slowly leading to a model with more aligned behavior. Additionally, they can A/B test the model in production and measure whether users preferred responses from the new version and had better outcomes.

## Continual learning

You might expect these models to improve and get smarter over time.

But that's not how they work today! Learning only happens when the model is training. Your conversations don't update the model's intelligence in real time.

Instead, you need to write down things to remember, typically as rules or skills. Agents can then read these files and include them in context when prompting the model.

This naive approach to memory through files has worked surprisingly well, but there's more work to do before agents can learn and remember skills the same way a new colleague would.

---

Teaching models to be helpful is a deep topic. Hopefully this high-level overview was interesting enough to inspire you to go learn more.

## Referenced URLs

- [Google AI Principles](https://ai.google/principles/)
- [OpenAI Model Spec](https://model-spec.openai.com/2025-12-18.html)
- [Anthropic Constitution](https://www.anthropic.com/constitution)
- [OpenAI Alignment](https://alignment.openai.com/beneficial-rl/)
