---
title: "In software, the code documents the app. In AI, the traces do."
source: https://www.langchain.com/blog/in-software-the-code-documents-the-app-in-ai-the-traces-do
author: Harrison Chase
date: 2026-01-10
publication: LangChain Blog
type: blog-post
tags:
  - agent-evaluation
  - observability
  - methodology
  - langchain
---

# In software, the code documents the app. In AI, the traces do.

**Author:** Harrison Chase (CEO, LangChain)
**Published:** January 10, 2026
**Source:** https://www.langchain.com/blog/in-software-the-code-documents-the-app-in-ai-the-traces-do

## TL;DR

- In traditional software, the codebase contains the deterministic decision logic — **code documents the app**.
- In AI agents, the code is just scaffolding; the actual decisions happen **at runtime in the LLM**.
- Therefore, the **source of truth shifts from code to traces** — the recorded sequence of steps an agent takes.
- This transforms how we debug, test, optimize, monitor, collaborate, and understand product usage.
- Building agents without proper observability (structured tracing) means working blind.

## 1. Why Code Doesn't Document Agent Behavior

In traditional software, if you want to understand what happens when a user submits a form, you open `handleSubmit()` and read the function. The decision logic is right there … It's deterministic — same input, same code path, same output.

In AI agents, the code is **merely orchestration**. A typical snippet:

```python
agent = Agent(
    model="gpt-4",
    tools=[search_tool, analysis_tool, visualization_tool],
    system_prompt="You are a helpful data analyst..."
)
result = agent.run(user_query)
```

- All the real decision-making — **which tool to call, when to stop, how to reason** — happens inside the model at runtime, not in the code.
- You can still debug the **orchestration layer** (tool calling, parsing), but you cannot debug the **intelligence** — whether the agent makes good decisions, reasons effectively, etc.

> As the LLM drives more and more of your app (as happens with agents), you have less and less visibility into what the app will actually do just by looking at the code.

## 2. Traces as the New Documentation

A **trace** is the sequence of steps an agent takes during a run, documenting:

- Reasoning at each step
- Which tools were called and why
- Outcomes and timing

> This means that operations you would do on code in the software world, you now do on traces in the agent world.

Key implication:

- **Same input, same code, different outputs** is normal — different reasoning chains, tool calls, outcomes.
- The only way to understand *what happened* is to examine traces: compare traces for success vs. failure, before/after prompt changes, patterns of repeated mistakes.

## 3. How This Changes Building Agents

### 3.1 Debugging → Trace Analysis
- The "bug" is no longer a logic error in your code; it's a **reasoning error in the agent's decisions**.
- Example: agent retries a failing API call 5 times without learning from the error message. The code's retry logic works fine; the bug is in the trace — identical tool calls, identical failure, repeated.

### 3.2 You Can't Set a Breakpoint in Reasoning
- Traditional breakpoints don't work because decisions happen inside the model.
- Instead, use **traces + playgrounds**: open a trace right before the bad decision, load that exact state (context, memory, tools, prompt) into a playground, and experiment iteratively — adjust prompt, context, etc. — to see if the agent makes a better choice.

### 3.3 Testing → Eval-Driven
- Testing means **testing traces**, not code paths.
- Two requirements:
  1. **Capture traces** continuously into a dataset for evaluation.
  2. **Eval traces in production** — because agents are non-deterministic, you must monitor for quality degradation and drift post-deployment.

### 3.4 Performance Optimization Changes
- Profiling shifts from code loops to **trace patterns**: unnecessary tool calls, redundant reasoning, inefficient decision paths. The bottleneck is in the agent's decisions, visible only in traces.

### 3.5 Monitoring Shifts from Uptime to Quality
- An agent can be "up" (0 errors) but still fail: succeeding at the wrong task, doing it inefficiently at 10x cost, or giving correct but unhelpful answers.
- Monitor **decision quality**: task success rate, reasoning quality, tool usage efficiency — all require sampling and analyzing traces.

### 3.6 Collaboration Moves to Observability Platforms
- In traditional software, collaboration happens on code (GitHub PRs, issues).
- For agent behavior, the artifact is the **trace**. When debugging why an agent chose a certain path, you share a trace, comment on decision points, discuss alternatives. The observability platform becomes a collaboration tool.

### 3.7 Product Analytics Merges with Debugging
- Product analytics (like Mixpanel) and debugging/logs used to be separate.
- With agents, **user behavior and agent behavior are intertwined**. If 30% of users are frustrated, you must open traces to see what the agent did wrong. Feature requests require examining which tools the agent already uses and what works. Product analytics must be built on traces.

## 4. The Core Takeaway

In traditional software, the code is your documentation. The function tells you what will happen. The control flow is explicit. In AI agents, the trace is your documentation. The trace tells you what actually happened. The decision logic emerges at runtime in the model.

Every practice you've built around code — debugging, testing, optimizing, monitoring, collaborating — needs to be rebuilt around traces. The observability platform becomes as fundamental to agent development as the IDE is to traditional software development.
