---
title: "ART·E: How We Built an Email Research Agent That Beats o3"
author: Kyle Corbitt
date: 2025-04-29
source_url: https://corbt.com/posts/art-e-mail-agent
type: article
tags:
  - reinforcement-learning
  - agents
  - grpo
  - openpipe
  - art
  - email
  - benchmark
  - reward-hacking
---

# ART·E: How We Built an Email Research Agent That Beats o3

**Author:** Kyle Corbitt
**Date:** April 29, 2025
**Source:** https://corbt.com/posts/art-e-mail-agent

---

OpenPipe built "ART·E" — an email research agent trained with reinforcement learning (RL) that is faster, cheaper, and more accurate than OpenAI's o3 on the task of answering natural-language questions by searching an email inbox. They open-sourced both the [final model](https://huggingface.co/OpenPipe/art-e-008) and [all training code](https://github.com/OpenPipe/ART/tree/main/examples/art-e).

## Task Definition

Searching an email inbox to answer natural-language questions (e.g., "How do I RSVP for my daughter's classroom party?", "What time is my brother's flight on Friday?").

## Synthetic Data

Used the Enron email dataset (500K emails released during litigation). Selected 8 test inboxes and 20 train inboxes. Generated ~4K synthetic question-answer pairs using GPT-4.1, with `how_realistic` scores to filter out implausible questions.

## Environment

The agent has 3 tools: `search_emails` (FTS5 full-text search), `read_email` (full body retrieval), and `return_final_answer`. A simple agentic loop runs for up to 10 turns.

## Benchmarking

Tested multiple off-the-shelf prompted models before training. This is important to fix environment/tool issues and establish baselines.

## Reward Function

Multi-objective reward including: answer correctness (primary), minimizing turns (latency proxy), penalizing hallucinations, and unsuccessful partial credit attempts (finding/reading the right email didn't help since the model already learned from the final-answer signal).

## Training

Used their open-source ART library with GRPO (Group Relative Policy Optimization). Batch of 12 questions, 4 trajectories per question (48 total per step). Training took ~1 day on a single H100 GPU at a cost of ~$80.

## Results

The trained model surpassed o3 in accuracy, used fewer turns, and hallucinated less. Training cost was ~$80.
