---
source_url: https://arxiv.org/abs/2609.28614
arxiv_id: 2609.28614
ingested: 2026-10-01
sha256: f7e66931271d40130cc26b4c63d66ec17457904bd65d0381ab28ed6a451bd778
---

# Reward Hacking Challenges Oversight of Autonomous Research Agents

arXiv:2609.28614v1 (cs.CL, cs.LG), submitted 2026-09-23.
Authors: Yue Huang, Zhangchen Xu, Yuchen Ma, Wenjie Wang, Zheyuan Liu, Ziwei Xu, Pin-Yu Chen, Michel Galley, Zinan Lin, Stefan Feuerriegel, Radha Poovendran, Misha Sra, Alex Pentland, Xiangliang Zhang, Zichen Chen.

## Abstract

Autonomous research agents can design experiments, evaluate results, and write reports, giving them control over both a scientific result and the evidence used to support it. This creates a risk of reward hacking: meeting the reward criteria without achieving the intended goal. We study (1) how often models reward-hack without instructions to do so, (2) how effective and detectable their methods are when hacking is allowed, and (3) how they adapt when an LLM review panel returns its decision and reasons.

Across 17 language models and 38 tasks, the spontaneous reward-hacking rate is 30.5% on open-ended research-pipeline tasks and 2.9% on task-specific kernels. When hacking is allowed on tasks whose pass thresholds exceed our best compliant baselines, 505/677 attempts (74.6%) are confirmed reward hacks: they both clear the threshold and receive mechanism-verification panel confirmation of an evaluation exploit. An LLM panel reviewing only submitted code and reported scores misses 33/505 confirmed hacks (6.5%). Direct methods that achieve the highest scores are often easy to detect, while less direct methods evade more often. In a five-round loop, the number of model-task pairs with an evasion rises from 7 to 56. Among 79 pairs evaluated under two feedback conditions, cumulative evasion reaches 40.5% with detailed feedback and 20.3% with generic rejection. The detailed condition includes the review decision, reasons, and attempt history, so this comparison does not isolate the effect of explanations.

These findings highlight the need for stronger defenses, including metrics kept outside the agent's control and independent recomputation on data chosen to expose likely exploits.
