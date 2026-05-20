---
title: "Building effective agents — Simon Willison's annotation"
type: raw_article
created: 2024-12-20
source: https://simonwillison.net/2024/Dec/20/building-effective-agents/
author: Simon Willison
---

# Building effective agents

Simon Willison's commentary on the Anthropic article "Building Effective Agents" by Erik Schluntz and Barry Zhang.

## Key Points

My principal complaint about the term "agents" is that while it has many different potential definitions most of the people who use it seem to assume that everyone else shares and understands the definition that they have chosen to use.

This outstanding piece by Erik Schluntz and Barry Zhang at Anthropic bucks that trend from the start, providing a clear definition that they then use throughout.

They discuss "agentic systems" as a parent term, then define a distinction between "workflows" - systems where multiple LLMs are orchestrated together using pre-defined patterns - and "agents", where the LLMs "dynamically direct their own processes and tool usage". This second definition is later expanded with this delightfully clear description:

> Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain "ground truth" from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control.

That's a definition I can live with!

They also introduce a term that I really like: the augmented LLM. This is an LLM with augmentations such as tools - I've seen people use the term "agents" just for this, which never felt right to me.

The rest of the article is the clearest practical guide to building systems that combine multiple LLM calls that I've seen anywhere.

Most of the focus is actually on workflows. They describe five different patterns for workflows in detail:

- **Prompt chaining**, e.g. generating a document and then translating it to a separate language as a second LLM call
- **Routing**, where an initial LLM call decides which model or call should be used next (sending easy tasks to Haiku and harder tasks to Sonnet, for example)
- **Parallelization**, where a task is broken up and run in parallel (e.g. image-to-text on multiple document pages at once) or processed by some kind of voting mechanism
- **Orchestrator-workers**, where a orchestrator triggers multiple LLM calls that are then synthesized together, for example running searches against multiple sources and combining the results
- **Evaluator-optimizer**, where one model checks the work of another in a loop

These patterns all make sense to me, and giving them clear names makes them easier to reason about.

When should you upgrade from basic prompting to workflows and then to full agents? The authors provide this sensible warning:

> When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all.

But assuming you do need to go beyond what can be achieved even with the aforementioned workflow patterns, their model for agents may be a useful fit:

> Agents can be used for open-ended problems where it's difficult or impossible to predict the required number of steps, and where you can't hardcode a fixed path. The LLM will potentially operate for many turns, and you must have some level of trust in its decision-making. Agents' autonomy makes them ideal for scaling tasks in trusted environments.

> The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails

They also warn against investing in complex agent frameworks before you've exhausted your options using direct API access and simple code.

The article is accompanied by a brand new set of cookbook recipes illustrating all five of the workflow patterns. The Evaluator-Optimizer Workflow example is particularly fun, setting up a code generating prompt and an code reviewing evaluator prompt and having them loop until the evaluator is happy with the result.
