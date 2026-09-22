---
source_url: https://arxiv.org/abs/2609.09233
ingested: 2026-09-22
sha256: d23de56378ce73cd5837ed0c803a0881d36c16c616d094f7859a477d68f3f75c
---

# Subagents vs Agent Skills: Executing Reusable Knowledge for Long-Horizon Agentic Tasks

**arXiv:** 2609.09233v1 (cs.AI) — submitted 2026-09-07
**Authors:** Wasu Top Piriyakulkij, Rachel Lawrence, Alicia Curth, Sushrut Karmalkar, Niranjani Prasad
**Abstract URL:** https://arxiv.org/abs/2609.09233

## Abstract

How can language model agents effectively leverage libraries of reusable knowledge to solve long-horizon tasks? Recent work has increasingly focused on agent skills: reusable capabilities represented as skill packages, i.e., multi-file bundles containing instructions, scripts, and other resources that help agents perform specific tasks. Agent skills are typically executed by loading their skill instructions into an agent's context and relying on the agent to follow them. As task horizons grow, however, this approach becomes increasingly brittle, because reasoning quality degrades as more information accumulates in the context window. We investigate an alternative approach in which skill packages are instead invoked as subagents. Rather than loading skill instructions into the main context, subagent execution spawns fresh context windows dedicated to solving individual subtasks. We show that subagent execution outperforms agent-skill execution when skill packages expose clear input-output contracts and their instructions encode the procedural knowledge needed to fulfill those contracts. The tradeoff is additional communication overhead, as extra tokens are required to coordinate between the main agent and its subagents. Our results show that the benefit of reusable knowledge depends not only on its content, but also on how it is organized and invoked.
