---
title: "Agents MCP RL — Training Agents with GRPO (Lesson 6 Transcript)"
author: Kyle Corbitt
date: 2025-07-03
date_ingested: 2026-06-11
source: https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
type: transcript
tags:
  - reinforcement-learning
  - grpo
  - agentic-rl
  - reward-engineering
  - agent-evaluation
  - ai-agent-engineering
  - experiment-tracking
  - transcript
related_article: articles/2025-07-03_kylecorbitt_agents-mcp-rl-lesson6.md
participants:
  - Kyle Corbitt (instructor)
  - Will Brown (absent — traveling)
---

# Agents MCP RL — Lesson 6: Training Agents with GRPO (Final Lecture)

Final lecture of the course. Kyle Corbitt covers training run monitoring, experiment iteration patterns, reward function ablations, LM-as-judge without ground truth, dataset size scaling, and answers Q&A on the RL ecosystem.

**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
**Companion slides/code:** [ai-agent-engineering](https://github.com/willccbb/ai-agent-engineering)

---

## Introduction & Logistics

**[00:03:06]** Kyle welcomes the class (~30 participants). Will Brown is out traveling. Agenda: finish the training run from last week, then spend the bulk of time on how to iterate and run fast experiments with RL.

**[00:03:41]** Credits update:
- **Weights & Biases**: Credits delayed — a special landing page link will be sent out Monday/Tuesday next week
- **OpenPipe**: Credits should be available for all accounts; email Kyle if missing
- **Prime Intellect**: Everyone should have credits (contact Will for details)

**[00:05:01]** The course has reached its final lecture. Focus today: finishing the training setup, then practical experimentation patterns.

---

## Training Run Status & Bug Fix

**[00:06:52]** Kyle shows the training code. A few changes since last week:
- Extracted magic numbers to the top of the training file for clarity: `rollouts_per_group`, `epochs`, `groups_per_step`, `learning_rate`
- These are the primary knobs to experiment with

**[00:08:22]** The bug from the previous lesson was an **indentation error** — training lines were indented one level too far, causing `await groups` to be called for every scenario in the batch instead of once. O3 found the fix quickly.

**[00:09:09]** Current training metrics:
- **Reward**: Starting near 0, climbing to ~86% correct answers on the Art E email search task
- **Validation**: Similar trajectory, converging around high-eighties
- **State of the art**: High eighties to low nineties is typical for this kind of task
- Training is stable; ~86 steps completed

---

## Understanding Group Size & Reward Standard Deviation

**[00:11:25]** **Why increase group size?** Two reasons:
1. Not enough variation within each group
2. Training is unstable

**[00:12:07]** Key metric: **reward standard deviation** within a group.
- Measures the spread of scores across rollouts in a single group (scores between 0 and 1)
- Higher std dev = more diversity in outputs = more signal for training
- Current run: std dev ~0.15–0.20 — healthy, not collapsing
- **If std dev collapses near 0**: Need larger groups to get at least some samples with reward differentiation

**[00:13:04]** Current run doesn't need changes — training is stable with good diversity.

---

## Experiment Registry Pattern

**[00:13:26]** Problem: If you keep editing hyperparameters in a single file and kicking off runs, you lose track of what settings produced which results.

**Options:**
1. Duplicate training files per experiment → leads to duplication, hard to mix/match
2. **ART's approach**: `RunConfig` abstraction + experiment registry

**[00:16:09]** `TrainableModel` accepts a configuration object (`RunConfig`). This Pydantic model holds all experiment parameters. The config is:
- Logged to Weights & Biases
- Saved alongside the model checkpoint
- Enables tracking what worked across experiments

**[00:19:11]** Creating an experiment registry file (`all_experiments.py`):
```python
# Base model
models["run_1"] = TrainableModel(...)

# Branch off existing model, override specific params
models["run_2"] = models["run_1"].model_copy()
models["run_2"].name = "run_2"
models["run_2"].config.rollouts_per_group = 8
```

**[00:21:34]** Launch script updated to accept a `--model` argument, passing model name to `train.py` which looks up the experiment from the registry.

**[00:23:28]** **Parallel experiments via SkyPilot**: Cluster name = model name. Each experiment gets its own GPU cluster, enabling parallel runs. Once something is working, run multiple experiments simultaneously with different hyperparameters.

---

## GPU Utilization & Concurrency

**[00:31:49]** Critical metric: **`num_requests_running`** — how many concurrent inference requests are hitting the GPU.

**[00:32:19]** Low GPU utilization in RL typically comes from the **rollout phase**, not training:
- Training (weight updates) is already well-optimized
- Rollouts suffer from: few concurrent requests, external tool latency (web search), **stragglers** (one agent takes 10 turns while others finish in 3)

**[00:32:57]** Target: 30–40 simultaneous requests for an H100 to be well-utilized.

**[00:34:32]** Pattern seen in metrics: spikes to 40 requests, then long gaps with nothing running — indicates optimization opportunity.

**[00:34:58]** ART provides `limit_concurrency` helper:
```python
@limit_concurrency(80)
async def run_agent(model, scenario):
    ...
```
- Useful for large batches (1000+ rollouts) to prevent overload
- Also useful for external API rate limiting

**[00:37:43]** OpenPipe's future hosted backend design: shared GPU fleet across users running RL on the same base model (LoRA fine-tunes). Aggregate usage smooths out spiky patterns, achieving much higher utilization than single-user GPUs.

---

## Reward Function Experiments

### Complex vs. Simple Reward Functions

**[00:43:39]** ART's `metrics` system: within each trajectory, store arbitrary float/int/boolean metrics. These generate W&B graphs for tracking behavior over time.

**[00:43:56]** Rubric concept: a structured tracker populated during agent execution:
```python
rubric.found_right_email = True  # set during rollout
rubric.read_right_email = True
rubric.bad_tool_call_name = False
```

**[00:45:13]** Two reward function variants compared:

**Complex reward** (Model 8):
- Partial credit for finding the right email (+small bonus)
- Partial credit for reading it (+small bonus)
- Partial credit for not attempting invalid emails (+small bonus)
- Bonus for correct sources
- Bonus for fewer turns (efficiency)
- Penalty for formatting errors, invalid tool calls
- **Big reward**: correct final answer

**Super stupid simple reward** (Model 14):
```python
reward = 1.0 if answer_correct else 0.0
```

**[00:46:44]** Surprising result: Model 14 (simple) converged **faster** than Model 8 (complex):
- Model 14: plateauing by step ~90
- Model 8: took ~300–540 steps to plateau
- Both reached similar final accuracy (~86%)

**[00:48:08]** Trade-off: Model 14 is worse at **number of turns** — it takes more turns because it's not rewarded for efficiency. Model 8 consistently takes fewer turns due to the turn-count bonus in the reward.

**[00:48:54]** This trade-off is clearly visible in W&B metrics — number of turns diverges between the two models on both training and validation.

> **Key lesson:** Simple reward functions can converge faster and achieve similar final performance. Complex reward functions give you more control over secondary behaviors (efficiency, tool usage) but may slow convergence.

---

## LM-as-Judge Without Ground Truth (Preview)

**[00:53:44]** **Sneak preview — not for public release yet.**

Experiment: What if the judge model doesn't have access to ground truth? It only sees the 4 rollouts in a group and must rank them relative to each other.

**[00:54:50]** Implementation: `group_judge` — an LM judge that receives all trajectories in a group, a rubric describing what good/bad looks like, and assigns scores (0–1) to each.

**[00:55:43]** The judge sees:
- All 4 trajectories (message histories)
- The emails that were accessed
- No ground truth answer

**[00:56:30]** Results (Model 204, using O3 as judge):
- **Converges faster than any ground-truth-based model**
- Reaches similar final accuracy
- No access to what the "right" answer is

**[00:57:16]** Why it works: The judge can see if one rollout read the right email while others didn't, and score accordingly. It's doing comparative evaluation across trajectories.

**[00:58:02]** Tried with Qwen 3 32B as judge (Model 206) — initially did well but **collapsed** during training. Not foolproof, but promising.

**[00:58:45]** Practical implications: Expands the set of tasks where RL can be applied — no need to know the ground truth, just run multiple rollouts and let the judge compare.

**Cost caveat**: O3-as-judge cost ~$1,000 per run (would have been ~$5,000 before OpenAI's price drop). Training compute was only ~$30–50.

---

## Dataset Size Scaling Experiments

**[01:01:12]** Question: How many training examples do you need?

Experiment: Loop over powers of 4 (1, 4, 16, 64, 256, 1024, 4096 examples), keeping total training steps ~600 by adjusting epochs.

**[01:04:41]** Results:

| Training Examples | Validation Accuracy | Notes |
|---|---|---|
| 1 | ~63% | Still improves! No catastrophic forgetting (unlike SFT) |
| 4 | ~70% | Visible improvement |
| 16 | High 80s | Comparable to best prompted models |
| 64 | Similar to 16 | Marginal improvement |
| 256 | Same as 4096 | Converges to full-data performance |
| 1024+ | Plateau | No additional benefit |

**[01:05:23]** Key insight: **RL does not catastrophically overfit** like SFT. Even looping on a single example doesn't cause collapse — the normalization and selective training (only when there's reward differential) prevents this. This is a major advantage over SFT.

> **Practical guidance:** ~256 examples conservatively sufficient for good results. Even 16 can get you to high-eighties for many tasks.

---

## Q&A: SFT vs. RL for Agents

**[01:16:13]** **Should you skip SFT for multi-turn tool-calling agents?**

Depends on the base model's starting capability:
- Look at initial reward and reward std dev
- If the model gets the answer right some of the time and std dev is decent → skip SFT, go straight to RL
- If the model is hopeless (std dev ~0, rarely succeeds) → do SFT first to bootstrap basic skills

**[01:17:41]** Current best models for agentic tasks: **Qwen 2.5** and **Qwen 3** — good at instruction following and tool calling out of the box, usually don't need SFT.

---

## Q&A: Qwen 3 Training Challenges

**[01:21:12]** Why isn't Qwen 3 used more? The chat template is weird around thinking:
- Multiple ways to control thinking: `/think`, `/no-think` commands
- Most reliable: prepend `<think></think>` XML tags at the start of each turn
- Thinking tokens are only serialized for the most recent turn in multi-turn conversations
- This complicates training (can't train on the full thing at once)
- Difference between 2.5 and 3 is usually not large enough to matter

---

## Q&A: MCP in Training Loops

**[01:12:39]** MCP doesn't have per-user authentication (at least as of mid-2025). In training:
- You need diverse users' data sources
- MCP servers typically connect to one user's data at startup
- This means many server processes needed → annoying
- Expected future fix: multi-user MCP servers

---

## Q&A: Other RL Trainers

**[01:14:05]** Kyle's assessment:
- **Verifiers** (Will Brown's library): Good
- **veRL**: Popular on the academic side
- **RLLM**: Interesting abstractions (from Together/Agentica, Berkeley)
- **SkyRL**: Wrapper of veRL worth checking
- ART was built because existing ones weren't easy enough to use

---

## Q&A: Audio/Video in RL

**[01:23:05]** Most things stay the same. Most trainers (including ART) don't have explicit multimodal support yet, but it's straightforward to add. Key change: ensure good observability support for audio/video.

---

## Q&A: Favorite Agentic Use Cases

**[01:18:57]** Kyle's daily driver: **OpenAI Deep Research** ("game changer").

Common patterns seen in industry:
1. **Research/list building** for outbound sales
2. **Customer support**
3. **Entertainment chatbots**
4. **Root cause analysis of downtime** — agent with access to AWS console, logs, internal tooling; diagnoses alerts automatically ("has a lot of potential")

---

## Q&A: OpenAI's Consulting Move

**[01:08:22]** OpenAI expanding into fine-tuning consulting suggests they're seeing the same thing: **huge gains from lightweight customization on specific tasks**. Even at AGI/ASI level, task-specific training will likely remain valuable — like a new hire being good but still improving after weeks at a company.

---

## Closing

**[01:18:29]** Course concludes. Kyle's email is available for follow-up questions. ART has a Discord (via GitHub project) for technical support. Open-source release and write-up coming for the LM-as-judge results and other improvements.

---

## Companion Resources

| Resource | Description |
|----------|-------------|
| [[concepts/agents-mcp-rl-course\|Course Portal]] | Full course overview and all lesson links |
| [ai-agent-engineering](https://github.com/willccbb/ai-agent-engineering) | Course repository |
| [[raw/articles/2025-07-03_kylecorbitt_agents-mcp-rl-lesson6\|Lesson 6 Summary]] | Structured summary of this lecture |
| [[raw/articles/2025-07-02_kylecorbitt_agents-mcp-rl-lesson5\|Lesson 5 Summary]] | Previous lecture: Formulating Business Problems as RL Tasks |
| [[raw/articles/2025-07-03_willbrown_agents-mcp-rl-lesson5-5\|Bonus Lesson Summary]] | GRPO Details (Will Brown) |
