---
title: "ENPIRE: Agentic Robot Policy Self-Improvement in the Real World"
created: 2026-06-18
type: research-note
source: active-crawl
status: partial_js_extracted
sources:
  - https://research.nvidia.com/labs/gear/enpire/
  - https://x.com/DarthUtopian/status/2066916750592250097
  - https://hn.algolia.com/api/v1/items/48573847
tags:
  - trending
  - active-crawl
research_summary: |
  ENPIRE (Agentic Robot Policy Self-Improvement) from NVIDIA GEAR Lab (Jim Fan),
  CMU, and UC Berkeley. Coding agents (Codex, Claude Code, Kimi Code) autonomously
  develop robot manipulation policies through an environment loop with auto-evaluation
  and auto-reset. Achieves 99% success rate on dexterous tasks. Extracted from
  JS-rendered Next.js page via text scraping.
---

# ENPIRE: Agentic Robot Policy Self-Improvement in the Real World

**Authors**: Wenli Xiao, Jia Xie, Tonghe Zhang, Haotian Lin, Letian "Max" Fu, Haoru Xue, Jalen Lu, Yi Yang, Cunxi Dai, Zi Wang, Jimmy Wu, et al.
**Affiliation**: NVIDIA GEAR Lab, CMU, UC Berkeley
**Project page**: https://research.nvidia.com/labs/gear/enpire/

## Abstract

Achieving dexterous robotic manipulation in the real world relies heavily on human supervision and algorithmic engineering, which is a central bottleneck in the pursuit of general physical intelligence. Although emerging coding agents can generate code to automate algorithm search, their successes remain largely confined to digital environments. We conjecture that the missing abstraction to automate robotics research is a repeatable environment loop with automated evaluation and reset. 

ENPIRE enables coding agents to autonomously develop policies for challenging dexterous manipulation tasks. Powered by ENPIRE, frontier coding agents can autonomously develop a policy to achieve a 99% success rate on tasks such as PushT, organizing pins into a pin box, and using a cutter to cut a zip tie. Computer agents can autonomously perform physical world research, suggest algorithmic hypotheses, and code them, while automated reset and verification provide the scaffold.

## Key Components

### Environment Loop
- Auto Evaluation: Automated success/failure detection for each task attempt
- Auto Reset: Robots reset themselves between attempts without human intervention
- Verification scaffold: Ensures policy correctness through automated testing

### Coding Agent Fleet
- Multiple coding agents (Codex, Claude Code, Kimi Code) work in parallel
- Agents propose algorithmic hypotheses (heuristic learning, behavior cloning, offline/online RL)
- Fleet scaling metrics: Mean Robot Utilization (MRU), Mean Token Utilization (MTU)

### Tasks Demonstrated
1. **PushT**: Pushing a T-shaped object to target position — 99% pass@8
2. **Pin Insertion**: Organizing pins into a pin box
3. **Tie Zip-tie**: Using a cutter to cut a zip tie
4. **GPU Insertion**: More complex industrial manipulation

## Significance

ENPIRE bridges coding agents (traditionally digital-only) with physical robotics, creating a fully autonomous research loop. The system runs fully autonomously on real robots, working only through the automated reset and verification interface. This suggests a practical and scalable path toward autonomously advancing robotics in the real world.

## X/Twitter Context

From @DarthUtopian (Haotian Lin, NVIDIA GEAR Lab): "What if coding agents can perform autoresearch on a fleet of robots to study novel robot learning algorithms and improve policy? Excited to introduce ENPIRE: a harness loop in which the coding agent first constructs its own task-specific interfaces (env.reset / env.get_reward / ...) then iterates overnight. 8 Codex agents, GPU allocation, token budget. 99% success on dexterous tasks."

## References

- Project page: https://research.nvidia.com/labs/gear/enpire/
- X announcement: https://x.com/DarthUtopian/status/2066916750592250097
- HN discussion: https://news.ycombinator.com/item?id=48573847
