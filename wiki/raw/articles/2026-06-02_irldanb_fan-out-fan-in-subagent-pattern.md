---
title: "Fan-out-fan-in: the more important subagent pattern"
author: "@irl_danB (dan)"
date: 2026-06-02
source: https://x.com/irl_danB/status/2061605758551335081
quoted: https://x.com/dexhorthy/status/2061231982005383666
tags: [subagents, agent-design-patterns, fan-out, agentic-engineering]
---

# Fan-out-fan-in: The More Important Subagent Pattern

In response to @dexhorthy's question "What do you use subagents for?", @irl_danB responds:

> many things, but my favorite: the good old fan-out-fan-in
>
> and I think there is more to this than "you can parallelize token spraying" (which... is fun, but... careful)
>
> rather, the more important fan-out pattern is one in which each branch...

The insight: fan-out isn't just about parallelizing work for speed. The more important use case is having **independent branches explore different solution strategies simultaneously**, each with its own context and approach, then merging results. This is distinct from "token spraying" (naive parallelism) — it's about **parallel exploration with diverse paths**, where each subagent brings a different perspective or methodology to the same problem.

This relates to the concept of [[concepts/subagent-patterns|Pattern 2: Fan-Out]] but adds depth: the value isn't just in parallel execution, but in parallel *reasoning diversity*.
