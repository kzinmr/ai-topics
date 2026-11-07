---
title: "HF Harness Adapters: LoRA RL Training Inside Real Agent Harnesses"
created: 2026-11-07
updated: 2026-11-07
type: event
tags:
  - announcement
  - lora
  - huggingface
  - agentic-coding
  - coding-agents
  - ai-agents
  - liquid-ai
  - reward-hacking
  - developer-tooling
sources:
  - https://huggingface.co/blog/harness-hub/harness-adapters
  - https://x.com/tomaarsen/status/2118721388873998444
  - https://x.com/harness-hub/status/2118708539610857960
---

# HF Harness Adapters Launch (Nov 2026)

## What happened

On **2026-11-06** the Hugging Face `harness-hub` team (Younes Belkada, Lysandre Debut,
Nathan Habib) announced that **harness adapter training is live**, with a full blog post
"Harness adapters: Safe RL for efficient agentic development" and a public live dashboard
streaming the training runs. [[entities/tom-aarsen|Tom Aarsen]] amplified it on X
("Very glad to see this is now live!") quoting the announcement tweet.

A **harness adapter** is one LoRA adapter per (base model × agent harness) pair, trained
with reinforcement learning on verifiable tasks *inside unmodified agent harnesses* —
`pi`, `opencode` and `hermes`. The goal is not a smarter chatbot but a **cheaper, more
accurate local coding agent**: on held-out eval tasks the smoke runs make **fewer tool
calls than the base model while keeping or improving its accuracy**, with a small reward
bonus `0.1 × (1 − calls / 15)` applied only to correct rollouts.

## Why it matters

This is the first public, reproducible recipe for **RL training inside third-party agent
harnesses without forking them** — the harnesses run in their own sandbox per rollout
through OpenEnv's Harbor integration, and their requests go to the trainer's vLLM so that
**training uses exactly the tokens the harness saw, with no re-tokenisation**. That
eliminates the train/serve prompt skew that plagues most agent-RL setups (see
[[concepts/agent-harnesses]]).

Key ingredients:

- **LoRA is the natural fit.** Rank-32 adapters on every linear layer (`all-linear`) mean
  one vLLM server hosts the base weights once plus every harness's policy at once. Trainers
  hot-swap adapter versions by name; in-flight rollouts finish on the old version, so
  nothing pauses. For the small model, the three per-harness trainers even **share one GPU**
  because an agent rollout spends most of its time in the sandbox, not generating
  (~35 s of forward/backward per step vs several minutes waiting for rollouts).
- **Cost asymmetry made explicit.** Evaluating nine checkpoints of LFM2.5-24B-A2B
  (1,350 agent sessions) ran in a single H200 job in under an hour for **≈$5 of GPU time**;
  merging each checkpoint into full weights and serving them one by one would have cost
  **≈$90**. This is the clearest published number yet for why adapters beat full-weight
  checkpoints in agent-RL loops.
- **Safe RL via `safeagents`.** A proxy sits between harness and model and inspects every
  tool call with rule-based detectors; reward-hacking attempts are blocked, score 0, and are
  replaced by text explaining *why*, which nudges the model to explore another path.
  See [[concepts/reward-hacking-research-agents]].
- **Environments from public agent trajectories.** `Repo2RLEnvs` turns open coding sessions
  people published on the Hub (from `pi`, Claude Code, Codex and others) into verifiable
  tasks via a six-step pipeline: `atif-scan` screening (drops trajectories with reward
  tampering or benchmark leakage) → filesystem replay → unit-of-work discovery → LLM-written
  contracts/tests → Docker build + offline check. Task types: **repair** (fix a bug),
  **build** (from scratch, graded by hidden tests), **extend** (follow-up changes),
  **qa** (fact computed from public Hub data). Only the contract/test-writing step uses an
  LLM — `Mistral-Large-4-1T-A52B` as teacher; 259 of 270 tasks carry teacher-written tests.
  Mixed with `SmolDataEnvs` (Kaggle-notebook data-analysis questions).

## Models and hyperparameters

| Model | What it is | Role | Steps | SmolDataEnvs | Repo2RLEnvs | Tasks | Agent steps |
|---|---|---|---|---|---|---|---|
| `LiquidAI/LFM2.5-24B-A2B` | MoE, 2B active params | main run | 200 | 100 medium + 200 hard | 230 | 530 | 17 |
| `LiquidAI/LFM3-1.7B` | small hybrid w/ short convolutions | main run | 400 | 300 medium + 250 hard | 230 | 780 | 17 |
| `webAI-Official/TwIL-8B` | dense 8.8B reasoning model (from Granite 4.2) | experiment | 300 | 150 medium + 250 hard | 230 | 630 | 30 |

Shared: **GRPO** via TRL's `AsyncGRPOTrainer` + tree attention, LR 1e-5, 8 rollouts per
task, temperature 0.8, up to 32,768 output tokens per turn, rollouts at most 4 weight
updates stale, 4 gradient-accumulation steps, checkpoint every 10 steps (each evaluated).
Token budget per micro-batch: 131,072 (LFM2.5) / 65,536 (LFM3-1.7B, TwIL-8B), so tasks per
step is variable — LFM2.5 trained on ~8 tasks (64 rollouts) per step, TwIL-8B's smoke run
on about one. 40 Repo2RLEnvs + 150 SmolDataEnvs tasks are held out and never trained on.
Infrastructure: **HF Jobs**, 2×H200 for LFM3-1.7B and 4×H200 for the others.

The **TwIL-8B** case is the interesting scientific question: its model card states it was
*never trained on agentic data*, so the run asks whether a pure reasoning model can be
turned into a competent agent purely by in-harness RL (it needs 30 agent steps and a
20-minute timeout vs 17 for the others). Related: [[concepts/agent-native-tool-fallacy]].

## Lineage

An earlier, smaller release covered **LFM2.5-24B-A2B only**, under `pi`, `hermes` and
`claude-code`; it showed positive signals in both tool-calling efficiency and held-out
accuracy, and community adoption drove the expansion to more models, four task types, and
the `safeagents` safety layer. The companion methodology post is the "ultimate guide to
multi-harness RL".

## Status / open items

- Results quoted here are the team's own **smoke-test** numbers on held-out tasks — no
  independent replication yet, so treat the tool-call-efficiency claim as self-reported.
- The post ends with an opening for third parties to **train an adapter for their own
  agent**, which would test whether the recipe transfers beyond `pi`/`opencode`/`hermes`.
- Raw article not scraped into `raw/articles/` this run (HF blog body read directly from
  `__NEXT_DATA__`/HTML); cite the blog URL as source.

## Related

- [[entities/tom-aarsen]] — HF Fellow who amplified the launch
- [[entities/hugging-face]] — host of the training runs, Hub trajectories, and HF Jobs
- [[entities/liquid-ai]] — LFM2.5 / LFM3 base models
- [[concepts/agent-harnesses]] — the harness abstraction adapters are trained inside
- [[concepts/reward-hacking-research-agents]] — what `safeagents` mitigates
- [[entities/the-harness-blog]] — prior harness-related coverage

## Sources

- Blog: https://huggingface.co/blog/harness-hub/harness-adapters (published 2026-11-06)
- Announcement tweet: https://x.com/harness-hub/status/2118708539610857960
- Aarsen amplification: https://x.com/tomaarsen/status/2118721388873998444
