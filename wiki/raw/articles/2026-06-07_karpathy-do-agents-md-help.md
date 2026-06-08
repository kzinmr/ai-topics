---
title: "Do AGENTS.md Files Actually Help Coding Agents?"
author: Andrej Karpathy (@karpathy)
source: https://x.com/i/article/2063647807437705216
date: 2026-06-07
type: x-article
tags: [coding-agents, agent-context, evaluation, agents-md, swere-bench]
---

Catching up with the agent-related research literature, one paper that definitely got my attention is "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?." It looks into whether adding repository-level instruction files such as AGENTS.md or CLAUDE.md to tell coding agents how to work in a codebase is actually helpful.

The paper evaluates this in two settings. First, it uses SWE-bench Lite, where the authors generate context files because the original repositories do not necessarily contain developer-written ones. Second, they introduce AGENTBENCH, a new benchmark of 138 Python tasks from 12 repositories that already have developer-provided context files. The agents are then evaluated under three conditions: no context file, an LLM-generated context file, and, where available, a developer-written context file. The results are summarized below.

Based on the results shown in the figure above, compared to using no context files, LLM-generated context files reduce task success slightly or don't make a big difference on average. This is maybe surprising but maybe not, because I guess the LLM / agent harness just generates the necessary context information on the fly. The context file is more about improving efficiency between independent sessions.

Also, developer-written context files are better than LLM-generated ones, which is perhaps expected because that's where the domain expertise comes in.

What's very surprising though is that using no context files is also cheaper and more efficient in their benchmarks!

Paper: https://arxiv.org/abs/2602.11988
