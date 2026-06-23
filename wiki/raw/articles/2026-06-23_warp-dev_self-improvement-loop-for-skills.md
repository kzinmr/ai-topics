---
title: "Self-improvement loop for skills"
url: https://www.warp.dev/blog/self-improvement-loop-for-skills
date: 2026-06-23
source: warp.dev
---

# Self-improvement loop for skills

AI agents can now edit files, run commands, and create entire applications. But each of these abilities gets worse at scale. The reason is simple: when an agent performs a skill, it has to hold the entire "how" in its context window. As the steps grow, the agent must decide between a context window full of instructions or incomplete coverage.

This creates an efficiency problem that compounds. An agent that can write a single file spends tokens re-learning how to coordinate a multi-file change every time. An agent with orchestration logic bloats its prompt and drifts.

Warp's approach is to treat skills as composable, executable units that improve themselves through execution. We call this the self-improvement loop for skills, and it's the foundation of how our AI agent handles increasingly complex developer workflows.

## The problem with static instructions

When you give an agent a task, it can succeed in two ways: by retrieving stored instructions or by reasoning through the problem fresh. Neither scales well.

Stored instructions are brittle. They describe what worked in one context but break when the environment shifts. A build command documented for one repository structure fails on another. A deployment script that assumes a specific directory layout produces silent errors when the layout changes.

Reasoning from scratch is expensive. Each time the agent encounters a familiar problem, it burns tokens rediscovering the solution path. At small scale this is tolerable, but across thousands of invocations, it becomes a significant cost center.

The fundamental issue is that neither approach captures what actually happened during execution. The instruction doesn't know it failed. The reasoning doesn't persist. The agent's knowledge about its own performance is ephemeral.

## How skills work in Warp

A skill in Warp is a reusable procedure that an agent can invoke. Skills are defined in YAML and contain three parts: a description of what the skill does, the steps it performs, and the context it needs.

Here's a simplified example of a skill:

```yaml
name: run-tests
description: Run the test suite and report results
steps:
  - run: npm test
  - if: exit_code != 0
    then:
      - run: npm test -- --verbose
      - write: test-failure-report.md
        with: "{{ test_output }}"
```

The agent doesn't need to know the internals of the skill. It sees the name and description, decides whether to invoke it, and the skill handles execution. This separation is what makes composition possible: the agent reasons about what to do, and skills handle how.

Skills are stored in a workspace-local directory and can be shared across projects. When an agent invokes a skill, it loads only that skill's definition into context, rather than the instructions for every possible action.

## The self-improvement loop

After a skill executes, Warp evaluates the outcome. This evaluation happens automatically, without human intervention. The system looks at three signals:

1. Did the skill complete successfully?
2. Did the output match the expected format?
3. Did the agent need to intervene or retry?

When these signals indicate a problem, Warp updates the skill definition. This isn't a fine-tuning step or a model weight change. It's a revision of the skill's YAML — the steps, the context requirements, the error handling logic.

For example, if a skill that deploys to a staging environment fails because it didn't account for a new authentication requirement, the self-improvement loop adds the authentication step to the skill definition. The next invocation includes that step automatically.

The loop follows this cycle:

**Execute** → **Evaluate** → **Revise** → **Execute**

Each iteration makes the skill more robust. Skills that start as simple sequences of commands accumulate error handling, environment checks, and fallback strategies through repeated use.

## Why this works at scale

The self-improvement loop solves the scaling problem in three ways:

**First, it reduces context load.** Instead of holding the full execution history in context, the agent references a compact skill definition that encodes the lessons of past executions. A skill that took 50 lines of reasoning to develop might compress to a 10-line YAML definition.

**Second, it localizes failures.** When a skill fails, the failure is isolated to that skill's definition. The agent doesn't need to re-examine its entire approach — it revises the specific skill and retries. This means failures don't cascade into broader context pollution.

**Third, it creates a feedback signal that compounds.** Each execution produces information that improves the next execution. Unlike static documentation, which degrades as the environment changes, skills in the self-improvement loop stay current because they're continuously updated by real execution data.

## Composition and modularity

The self-improvement loop also makes composition more reliable. When skills are static, combining them requires the agent to anticipate every interaction. When skills improve themselves, the composition becomes more robust over time because each skill adapts to the context in which it's invoked.

Consider a workflow that chains three skills: extract data, transform it, and load it into a database. If the extraction skill encounters a new data format, the self-improvement loop updates the extraction skill to handle it. The downstream skills don't need to change because they receive the same transformed output they always have.

This modularity means that complex workflows can be built from simple skills without the combinatorial explosion of edge cases that would otherwise require explicit handling.

## Practical implications

For developers using Warp, the self-improvement loop means that agent capabilities get better with use. A skill that fails on Monday might succeed on Tuesday because the system learned from the failure. This isn't magic — it's a structured approach to capturing execution feedback and encoding it in reusable definitions.

The loop also changes how developers think about agent instructions. Instead of writing comprehensive instructions upfront, developers can write minimal skill definitions and let the system fill in the gaps through execution. This shifts the developer's role from instruction author to skill reviewer, which is a more sustainable relationship as the number of skills grows.

## What this means for AI agents

The self-improvement loop represents a shift from static to dynamic agent capabilities. Traditional agents operate on fixed instruction sets that require manual updates. Agents with self-improving skills operate on instruction sets that evolve through use.

This has implications beyond Warp. Any system that deploys AI agents for recurring tasks faces the same scaling problem. The solution isn't more instructions or larger context windows — it's structured feedback loops that let the agent's capabilities grow with its experience.

Warp's self-improvement loop for skills is one implementation of this principle. The core idea — execute, evaluate, revise, repeat — is applicable wherever agents need to perform reliable, repeatable tasks at scale.
