---
title: "Production-Ready Agent Engineering — Lesson 5: Formulating Business Problems as RL Tasks"
author: Kyle Corbitt
date: 2025-07-02
date_ingested: 2026-06-11
source: https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
type: article
tags:
  - reinforcement-learning
  - grpo
  - agentic-rl
  - ai-agents
  - tool-calling
  - agent-evaluation
  - reward-engineering
  - vllm
  - lora
  - fine-tuning
  - openpipe
  - education
---

# Production-Ready Agent Engineering — Lesson 5: Formulating Business Problems as RL Tasks

**Lecture transcript:** [[transcripts/2025-07-02_kylecorbitt_agents-mcp-rl-lesson5-lecture]]
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
**Notebook (Lecture 5.5 — Will Brown):** [grpo_details.ipynb](https://raw.githubusercontent.com/willccbb/agent-engineering/refs/heads/main/lectures-1-through-4/lec5-grpo-details/grpo_details.ipynb)
**Instructors:** Kyle Corbitt ([[entities/openpipe]]) & Will Brown ([[entities/prime-intellect]])

---

## Summary

Lesson 5 is the culmination of the course's agent → RL pipeline. Kyle Corbitt live-codes the complete journey from a working email agent to a GRPO training loop — demonstrating how to formulate a real business task (email inbox Q&A) as an RL problem, build a reward signal via LM-as-judge, set up benchmarking infrastructure, and launch a training job on remote GPU. This lecture connects the agent engineering (Lessons 1–2) and evaluation methodology (Lesson 3) to actual RL training (Lesson 4) in a production-quality implementation using OpenPipe's ART framework.

## Key Topics

### Agent Refactoring for RL

- **Scenario-based architecture:** Refactored `run_agent` from simple question→answer to a `Scenario` object containing question, answer, reference message ID, and date constraint
- **`return_final_answer` tool:** Explicit structured output tool (answer + reference message IDs) replacing implicit content return — enables source citation and cleaner loop termination
- **Synthetic QA dataset:** Generated from Enron inbox emails, stored on Hugging Face with train/test splits for holdout evaluation

### Reward Engineering: LM-as-Judge

- **`judge_correctness` function:** LLM-based judge comparing AI-generated answer against reference answer with reasoning trace + Boolean accept/reject
- **Prompt engineering for edge cases:** Reference answers with extra non-necessary information caused false rejections; required rubric refinement by examining judge reasoning traces
- **DSPy comparison:** Kyle finds manual prompt engineering faster than DSPy for this type of calibration task — DSPy edits tend to be too situation-specific
- **Simple reward function:** Binary 0/1 (no partial credit, no efficiency bonus) — sufficient as baseline; real projects add turn-count incentives and hallucination penalties

### Benchmarking Infrastructure

- **Async parallelization:** `asyncio.gather` + `tqdm.asyncio` — 10 scenarios in 25s vs 82s sequential (~3.3x speedup, scales with concurrency)
- **Debugging with Weave (W&B):** Monkey-patches OpenAI SDK and LiteLLM to capture full traces; essential for identifying failure patterns (over-specific keywords, running out of turns)
- **Benchmarking-first workflow:** ~50% of project time spent on benchmarking + debugging before training; prompt engineering can match or beat model training for many tasks

### ART (Agent Reinforcement Trainer) Setup

- **`art.TrainableModel`:** Configuration object specifying base model (Qwen 2.5 14B Instruct), project name, and run name
- **`LocalBackend`:** Spins up vLLM server for inference + weight update server; supports local rollout with remote GPU training
- **LoRA by default:** Modifies small fraction of parameters; full fine-tuning available but experimental
- **`model.register(backend)`:** Prepares the model — loads weights into vLLM, initializes LoRA adapter

### GRPO Training Loop

- **Training iterator:** `iterate_dataset` yields batches of 12 scenarios × 3 epochs
- **Trajectory groups:** 4 rollouts per scenario (same inputs, different sampling) — GRPO normalizes rewards within group
- **`art.Trajectory`:** Tracks full message history + choices (including log probs for training efficiency) + reward
- **`gather_trajectory_groups`:** Runs all rollouts in parallel, waits for completion, then `model.train(finished_groups)` sends to GPU for weight update
- **On-policy loop:** After training, next inference call uses updated model — continuous improvement cycle

### Remote Execution with SkyPilot

- **Self-contained scripts:** Training script must not depend on local data except explicitly uploaded artifacts
- **`generate_database()`:** Pulls ~500K emails from S3 into local SQLite — runs at job start on each new machine
- **H100 requirement:** SkyPilot finds cloud with matching GPU availability
- **Auto-stop:** GPU released immediately when task finishes (set to 200s timeout)

## Key Insights

1. **Benchmark before training:** Prompt engineering and tool design improvements are faster and often sufficient; only move to RL when you've exhausted simpler optimizations
2. **LM-as-judge calibration is non-trivial:** Edge cases in answer comparison require iterative prompt engineering with reasoning trace inspection
3. **Small rollout groups work:** 4 rollouts per group (smaller than typical) yields good results and faster iteration
4. **Temperature 1 is mandatory for GRPO:** Lower temperatures cause mathematical issues in the advantage computation
5. **Caching must be disabled for training:** Multiple rollouts on the same model must be independent; caching only for prompted models
6. **Reward std dev is a key health metric:** If it collapses to 0, the model is output-saturated and stops learning
7. **Log probs in trajectory:** Storing full choice objects (not just messages) avoids expensive log-prob recomputation during training

## Companion Resources

- [grpo_details.ipynb](https://raw.githubusercontent.com/willccbb/agent-engineering/refs/heads/main/lectures-1-through-4/lec5-grpo-details/grpo_details.ipynb) — Lecture 5.5 notebook: GRPO implementation details, VRAM math, tool call masking, KL penalties, length penalties, dynamic sampling, VinePPO
- [ART Trainer blog post](https://corbt.com/posts/art-trainer-a-new-rl-trainer-for-agents) — ART framework announcement and architecture
- [ART·E blog post](https://corbt.com/posts/art-e-mail-agent) — The email agent case study this lesson implements
- [SkyPilot](https://skypilot.co/) — Multi-cloud GPU orchestration used for remote training
- [Weave by W&B](https://wandb.ai/weave) — LLM tracing and debugging tool used in the lecture

## Related

- [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
- [[transcripts/2025-07-02_kylecorbitt_agents-mcp-rl-lesson5-lecture]]
- [[concepts/grpo-rl-training]]
- [[concepts/agentic-rl]]
- [[concepts/art-agent-reinforcement-trainer]]
- [[concepts/reward-hacking]]
- [[concepts/agent-evaluation]]
- [[entities/will-brown]]
- [[concepts/corbett-kyle-corbitt]]
- [[entities/openpipe]]
- [[raw/articles/2025-04-29_corbt_art-e-mail-agent]]
- [[raw/articles/2025-04-14_corbt_art-trainer-new-rl-trainer]]
