---
title: "Training Agents with Reinforcement Learning — Lightning Lesson"
author: Will Brown
date: 2025-06-10
date_ingested: 2026-06-10
source: https://maven.com/p/c3950c/training-agents-with-reinforcement-learning
type: lecture-summary
tags:
  - ai-agents
  - reinforcement-learning
  - grpo
  - tool-calling
  - agent-evaluation
  - verifiers
  - education
---

# Training Agents with Reinforcement Learning — Lightning Lesson

**Instructor:** Will Brown (Research Lead, [[entities/prime-intellect]])
**Date:** June 10, 2025 (pre-course Lightning Lesson)
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
**Lecture notebook:** [[transcripts/2025-06-10_willbrown_training-agents-with-rl-notebook|Notebook Walkthrough]]
**GitHub:** [agent-engineering/lightning-lessons/search.ipynb](https://github.com/willccbb/agent-engineering/blob/main/lightning-lessons/search.ipynb)
**Maven page:** [Training Agents with Reinforcement Learning](https://maven.com/p/c3950c/training-agents-with-reinforcement-learning)

## Summary

A ~65-minute Lightning Lesson that bridges agent building and RL training. The lesson builds a **Wikipedia search agent** end-to-end: from local file search tools (ChromaDB + embeddings) through synthetic QA data generation, baseline evaluation with LLM judges, and into live GRPO training with the [verifiers](https://github.com/PrimeIntellect-ai/verifiers) library. This is the practical companion to the course's RL thesis — showing how to go from a working agent to a *trained* agent.

## Video Chapters

| Timestamp | Chapter |
|-----------|---------|
| 00:02:29 | Pre-Talk Setup and Q&A |
| 00:09:15 | Introduction to Agent Training with RL |
| 00:11:28 | Task Setup: Wikipedia Search Agent |
| 00:13:49 | Building the Agent's Search Tools |
| 00:18:50 | Generating a Synthetic Question-Answer Dataset |
| 00:23:10 | Introducing the 'Verifiers' RL Framework |
| 00:26:08 | Setting Up the Evaluation Rubric with an LLM Judge |
| 00:30:01 | Running a Baseline Evaluation with DeepSeek V2 |
| 00:35:51 | Creating a Training Dataset from Agent Traces |
| 00:39:05 | Explaining the GRPO Reinforcement Learning Algorithm |
| 00:42:51 | Reviewing the Live RL Training Run |
| 00:47:43 | Case Study: Training a Wordle-Playing Agent |
| 00:53:02 | Q&A: Training Duration and Checkpointing |
| 01:00:05 | Q&A: RAG Chunking and Tool Orchestration |
| 01:05:02 | Q&A: Curriculum Learning |
| 01:07:21 | Conclusion |

## Key Topics

### 1. Task Setup: Wikipedia Search Agent

The lesson builds a search agent over a local Wikipedia corpus using three tools:
- `search_pages(query)` — ChromaDB title-embedding similarity search (top 10)
- `view_sections(page_id)` — returns section headings of a page
- `read_section(section_id)` — reads a specific section's content

This mirrors real research agent patterns: **search → navigate → read** with progressive disclosure.

### 2. Building Local Search Tools

Uses **ChromaDB** with OpenAI `text-embedding-3-small` for persistent vector storage:
- Indexes Wikipedia page titles as documents
- Embedding-based similarity search for initial retrieval
- Section-level navigation for targeted reading

Key insight: the tools are **deterministic and local** — no API rate limits, no external dependencies during evaluation. This is critical for RL training where you need to run thousands of rollouts.

### 3. Synthetic QA Dataset Generation

Generates trivia-style QA pairs from Wikipedia articles using GPT-4.1 Mini:
- Questions framed as "advanced pub trivia" — self-contained, no article reference
- Answers are short (1-5 words) for automated evaluation
- Async generation with concurrency control (semaphore = 3)
- ~750 questions from 150 pages (5 per page)
- Published to HuggingFace: `wiki-trivia-questions`

### 4. The Verifiers RL Framework

[Verifiers](https://github.com/PrimeIntellect-ai/verifiers) (by Will Brown) provides:
- `vf.ToolEnv` — environment wrapping tools + system prompt + dataset
- `vf.RubricGroup` — composable evaluation rubrics
- `JudgeRubric` — LLM-as-judge evaluation
- `vf_env.evaluate()` — run rollouts and compute rewards
- `vf_env.make_dataset()` — convert traces to trainable datasets

### 5. Evaluation with LLM Judge

Uses `JudgeRubric` with GPT-4.1 Nano as the judge model:
- Evaluates whether the agent's final answer matches the expected answer
- Composable with the tool-use rubric (format compliance, tool call validity)
- Also tested with Gemma 3 12B as a cheaper judge alternative

### 6. Baseline Evaluation with DeepSeek V3

Runs baseline evaluation on DeepSeek V3 (0324) via DeepInfra:
- 10 samples → 200 samples for full baseline
- Traces saved as HuggingFace dataset: `V3-wiki-trivia-tool-use`
- Provides the "before RL" performance benchmark

### 7. GRPO Training Explained

**Group Relative Policy Optimization** — the core RL algorithm:
- For each question, generate G completions (a "group")
- Score each completion with the reward function
- Compute advantages: normalize rewards within the group
- Update policy to increase probability of above-average completions
- No separate critic model needed (unlike PPO) — ~50% less compute

Key equation: advantage = (reward - mean) / std, computed per group.

### 8. Case Study: Wordle-Playing Agent

A Wordle-playing agent as a second RL training example:
- Demonstrates that the verifiers framework works across different task types
- Tool-based interaction (guess letters, receive feedback)
- Reward = game completion metrics

### 9. Q&A Highlights

- **Training duration:** Hours, not days — GRPO is sample-efficient
- **Checkpointing:** Save intermediate checkpoints to resume or compare
- **RAG chunking:** Section-level retrieval avoids chunk boundary issues
- **Tool orchestration:** Agent learns tool use patterns through RL reward signals
- **Curriculum learning:** Start with easy questions, gradually increase difficulty

## Companion Resources

| Resource | Description |
|----------|-------------|
| [search.ipynb](https://github.com/willccbb/agent-engineering/blob/main/lightning-lessons/search.ipynb) | Main lesson notebook (Wikipedia search agent + RL training) |
| [verifiers](https://github.com/PrimeIntellect-ai/verifiers) | RL environment library for training and evaluating LLMs (~4,000 stars) |
| [wiki-trivia-questions](https://huggingface.co/datasets/willccbb/wiki-trivia-questions) | Synthetic QA dataset generated in the lesson |
| [V3-wiki-trivia-tool-use](https://huggingface.co/datasets/willccbb/V3-wiki-trivia-tool-use) | DeepSeek V3 baseline traces |

## Related

- [[concepts/agents-mcp-rl-course]] — Course portal page
- [[entities/will-brown]] — Instructor profile
- [[transcripts/2025-06-10_willbrown_training-agents-with-rl-notebook|Notebook Walkthrough]] — Detailed code walkthrough
- [[raw/articles/2025-06-10_willbrown_build-your-own-research-agent-lightning|Lightning Lesson 1: Build Your Own AI Research Agent]]
- [[concepts/grpo-rl-training]] — GRPO algorithm details
- [[concepts/agentic-rl]] — RL for agents paradigm
- [[concepts/agent-evaluation]] — Evaluation methodology for RL reward signals
- [[entities/prime-intellect]] — Will Brown's organization
