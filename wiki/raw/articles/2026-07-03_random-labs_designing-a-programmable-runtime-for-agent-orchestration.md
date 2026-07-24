---
source: X Article
url: https://x.com/i/article/2073112080140689408
author: Akira / Random Labs
author_handle: "@realmcore_"
title: "Designing a programmable runtime for agent orchestration"
date: 2026-07-03
fetch_method: xurl_plain_text
getxapi: false
source_fallback: false
---

# Designing a programmable runtime for agent orchestration

This article introduces Onyx, our VM for programmable agent orchestration. And by extension, a runtime that turns orchestration into software engineering. By the end of this article, you'll understand the constraints and design decisions that went into building the VM as well as how to create your own programs and architect your agent systems.

## Introduction

Agents are inherently non-deterministic. That's the whole point. If you wanted determinism, you'd be writing software.

But somewhere along the way, everyone using agents collectively wanted to push them further. We learned that breaking execution into structured steps helps performance: Plan, Implement, Review, QA etc. Then we seemingly agreed to write scripts, tools, and skills to steer each agent, to share context across them, and to guardrail them. We then patch these scripts together by piping text between agents, and because we're just passing text around it sort of works.

If you spent enough time on the problem and were particularly clever, you'd have figured out how to get guarantees out of your system so that you could have conditional execution based on a given state. And you'd probably store that state in a parsable markup file or set of markup files to steer your bash scripts. You might've even built a custom cli for your agents to use.

As engineers this is familiar, we use scripts while doing software engineering. However, modern software isn't built by chaining bash scripts and cli tools. Instead, we have programming languages, runtimes, and tool chains to help us engineer our systems. We write software with programming languages because they come with a standard library, clear semantics, and an execution model we can rely on. They have rich ecosystems with toolchains for all of our needs.

The guarantees they give us about our systems allow us to reason at higher levels of abstraction.

But there's no equivalent for engineering agent systems. In order to build systems, Agent orchestration needs to be programmable in the exact same way as modern software.

Today, we are introducing the spec for PROGRAMS (*.program.ts), and Onyx, our VM built for deterministic agent orchestration. This article post explores a history of agent orchestration, the static and runtime semantics of a VM that can run a program, and it's implications for where the field is headed.

## Unsolved Problems in Agent Orchestration

To understand what a runtime for agent orchestration should include, we need to understand the limitations of agents.

An llm agent can be thought of as a json stream generator, fed into a parser, which then dispatches tool calls to an environment in a loop.

Every tool call has the exact same outer schema shape but the content of this output stream is not deterministic.

The combination of determinism and non-determinism is what has made agents so valuable. They are flexible enough to chain sequences of actions in unique ways, but deterministic enough to interact with a computer through tool calls.

Composability is almost free if you are willing to let go of the requirement that the content of that stream be typed. Models are good enough to pipe text in and out within the rails that we provide them: prompts, messages, and tool calls.

This exposes a very composable interface: text

Text is a universal interface. Everything on a computer can be serialized to text even if it is just machine code. If you can have an llm input and output text through this universal interface, you get composability over text streams.

This means the reliability of your agent behavior is directly related to the consistency of the output from the model. High output variability means more erratic agent behavior.

Once you have an interface to compose pieces through, the next constraint you care about is steerability: what you want the agent to do, and how you consistently get it to do what you want.

We steer agents by shifting the distribution it samples from, in other words, prompting.

In 2022, ReAct came out and essentially pioneered agent steerability. In fact, we can go as far as to say it made agents as we know them a thing.

We still needed agents to be smarter. The use of test time compute scaling, productionized by OpenAI's O-series of models, gave model labs the ability to bake in better agent behavior. Outputting more tokens before calling a tool allows the model to escape the output distribution it would have been stuck in had it been constrained on reasoning output length.

As the context length grows unbounded, steering the agent becomes difficult and task completion becomes less likely. Even with a reasoning model, there is no guarantee of recovery, and the agent dies right there. The agent can hit its context limit, declare an early completion, get stuck in a loop, etc.

## Pulling Guarantees out of a Non-Deterministic System

The solutions to this were varied, but one stands out: The Ralph Loop, made by Geoffrey Huntley.

He introduced the idea that you could bound agent execution, and then use those bounds to reason about task completion. This allows the Ralph Loop to do something magical: it provides something you can rely on in a non-deterministic system.

A spark of determinism.

## Fighting the limits of context length

There's a problem though, a fresh agent loses coherence across runs, but a single agent runs out of context given enough time.

Enter RLM by Omar Khattab and Alex Zhang. RLM gave us a concept for how to interact with long context (i.e. an agent run) in a structured way. RLM was inspired by CodeAct, a paper from 2024 that demonstrated using code to orchestrate operations. The agent writes scripts that orchestrate operations inside a REPL to then retrieve an output. RLM operates in the same way with the additional caveat that it uses variables to store context and do operations on that context. It additionally allows for recursive LLM calls in the REPL.

## Moving from individual loops to scaling orchestration

OpenAI's Deep research was one of the earliest examples of a deterministic workflow that had a general execution shape or schema with small variability on a run by run basis.

Cursor took the idea of determinism much further when Wilson Lin demonstrated a harness that orchestrated agents to build a browser. He built a bespoke harness for coordinating large amounts of work using parallel planner agents and task agents.

## Using termination conditions for bounded execution

In May, Codex introduced the idea of a goal which uses a verifier loop to hillclimb against some desired end state until a task is complete. You can think of this as a production ready version of the Ralph loop, built into codex.

Karpathy's autoresearch is similar to Codex's /goal and the Ralph loop. It combines the verifiable termination condition of goal with the execution bounding of a Ralph loop over iterations, allowing it to continuously drive towards a goal.

## Making orchestration flexible

In March of this year, we introduced Slate, the first coding agent to use code for live subagent orchestration in the style of RLM. It is still the only well used coding agent that uses code to do live agent orchestration. In Slate, threads can be spawned, paused, resumed, and steered in real time.

## Designing the runtime

When we design a language and a runtime for that language, we need to think about the constraints we want to be able to reason about, and what we care about being easily expressible. Then we can break the resulting semantics into two categories: static semantics and runtime semantics.

### VM Requirements

1. Persistent state management
2. Type guarantees
3. Control flow primitives
4. Clear structure for error handling (try-catch)
5. Resource management (agent parallelism, cost, model selection)
6. Execution Isolation
7. Lifecycle control
8. Composability
9. Visibility
10. Durability

## Onyx Primitives

### run and spawn
- `run`: Runs a blocking agent in the foreground
- `spawn`: Runs an agent in the background

Run supports enforced output types through zod, and direct model overrides.

### State
State namespaces are declared, directly named, and persisted over time. Both agents and code read the state. Agents read state through a dedicated tool. State and schema adherence gate subagent completion.

### Checkpoint
A checkpoint notifies the main agent with a fixed shape object, allowing the main agent to track task progress.

### Sleep
Sleep does what you would expect.

### Error Semantics
Errors are thrown loudly - agent failures, budget exhaustion, illegal state modifications, etc. This gives explicit ways to prepare and program around failures.

## Autoresearch as a Program

The article demonstrates how Karpathy's autoresearch can be represented as a program. The program runs a setup agent, then enters a loop of experiment agents. Each experiment gets a fresh agent. The agent and program share state.

## Future Work

The durability model for programs is the remaining VM requirement not yet defined.

References:
- ReAct (Yao et al., 2022)
- The Ralph Loop (Geoffrey Huntley)
- RLM (Zhang, Kraska, Khattab, Dec 2025)
- CodeAct (Wang et al., ICML 2024)
- OpenAI Deep Research (Feb 2025)
- Cursor Scaling Agents (Jan 2026)
- Codex Goals (May 2026)
- Karpathy autoresearch
- Claude Dynamic Workflows
- Skill Chaining (Random Labs)
