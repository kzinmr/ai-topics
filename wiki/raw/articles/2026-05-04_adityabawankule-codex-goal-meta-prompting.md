---
title: "Codex /goal: How to Meta Prompt It For Days of Autonomous Work (2026)"
source: "https://www.adityabawankule.io/blog/codex-goal-meta-prompting"
date: 2026-05-04
author: "Aditya Bawankule"
scraped: 2026-05-10
tags: [coding-agents, openai, prompting, agentic-engineering]
---

# Codex /goal: How to Meta Prompt It For Days of Autonomous Work (2026)

May 4, 2026 | Aditya Bawankule

Codex's **/goal** command is the most important thing to land in AI coding this year. Hand it an objective and Codex will keep working through it for hours, sometimes across an entire night, without you babysitting a single turn. The problem is that the prompt you type after /goal is doing most of the work, and the prompt you'd write yourself almost never has enough in it.

The fix is letting another AI write the /goal prompt for you. Once you stop hand-writing the mission, Codex starts producing the kind of output that makes you recheck the diff because you don't believe it.

## What Is the Codex /goal Feature?

/goal is a slash command in the Codex CLI that turns Codex into a long-horizon autonomous agent. You give it a high-level mission, and it keeps working, planning, executing, and self-correcting, until the mission is done. Hours of continuous work in a single invocation.

It shipped in Codex CLI 0.128.0. Enable via: `codex features enable goals`. This is different from a normal Codex prompt. A normal prompt runs a few turns and stops. /goal sets up a persistent objective the agent commits to, and Codex will keep iterating against that objective across many cycles of plan, act, verify, and correct.

## Why Hand-Written /goal Prompts Don't Work

A short prompt fed into /goal produces results that might as well have come from a regular prompt. If your mission is vague, the agent burns its long horizon on the wrong things. Humans are bad at writing /goal prompts because we underestimate what the agent needs to know to stay on track without us. We write like we're going to be in the loop. With /goal, you're not in the loop.

## How to Meta Prompt Codex /goal

Open a second AI session that already has context on your repo: ChatGPT with the project connected, Claude inside the codebase, or a separate Codex window in the same directory. Then ask it to write the prompt for you:

> I'm about to use Codex's /goal command. Before you write anything, look up how /goal actually works in the Codex CLI so your output matches what the agent expects. Then walk through this codebase and pick the three highest-leverage missions /goal could realistically finish in one run. For each one, hand me a complete /goal prompt I can paste straight into the terminal: scope, constraints, files in play, definition of done, and the checks the agent should run before it considers the mission complete.

The AI is forced to look up /goal before it writes anything, so the prompt isn't guessing. It has to read the actual project before proposing missions, which kills generic suggestions. And you walk away with three options instead of staking everything on one prompt.

## Why Meta Prompting Beats Prompt Engineering

Meta prompting works because writing prompts is itself a skill an LLM can do better than you, especially when you give it the context. You know your project, but the AI knows what kinds of instructions agents respond to, what edge cases they tend to miss, and how to phrase acceptance criteria so they don't get reinterpreted halfway through a run.

## When to Actually Use /goal

/goal shines on missions with a clear definition of done and a lot of mechanical work between here and there: migrating a codebase, refactoring a subsystem end-to-end, building a feature that touches many files, upgrading dependencies across a monorepo.
